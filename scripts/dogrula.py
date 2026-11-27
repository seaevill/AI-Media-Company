#!/usr/bin/env python3
"""Bekçi 1. katman mekanik kontrolleri + kuyruk tutarlılığı.

Kullanım: python3 -I scripts/dogrula.py [--degisen dosya1 dosya2 ...]
Çıkış kodu 0 = temiz, 1 = bulgu var. Bulgular stdout'a yazılır.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
DURUMLAR = {"proposed", "approved", "queued", "in_progress", "review", "needs_revision",
            "waiting_owner", "blocked", "completed", "cancelled", "archived"}
ONCELIK = {f"P{i}" for i in range(8)}
SIR_DESENLERI = [r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
                 r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
                 r"(?i)(password|api_key|secret|token)\s*[=:]\s*['\"][^'\"\s]{8,}",
                 r"AKIA[0-9A-Z]{16}", r"xox[baprs]-[A-Za-z0-9-]{10,}"]
KORUNAN = [re.compile(p) for p in [r"^ANAYASA\.md$", r"^sirket/", r"^takimlar/[^/]+/kurallar\.md$", r"^denetim/BEKCI-KURALLARI\.md$"]]
SAYI_YASAK = re.compile(r"\b\d+\s*(saatte|saat\s*bir|dakikada)\b", re.I)


def izlenen_dosyalar():
    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=KOK, capture_output=True, text=True, check=True).stdout
        return [l for l in out.splitlines() if l]
    except Exception:
        return [str(p.relative_to(KOK)) for p in KOK.rglob("*") if p.is_file() and ".git/" not in str(p)]


def kuyruk_kontrol(bulgular):
    durum = json.loads((KOK / "vardiyalar/DURUM.json").read_text(encoding="utf-8"))
    cfg = json.loads((KOK / "vardiyalar/CONFIG.json").read_text(encoding="utf-8"))
    ids = [g["id"] for g in durum["gorevler"]]
    for i in {x for x in ids if ids.count(x) > 1}:
        bulgular.append(f"KUYRUK: yinelenen görev kimliği {i}")
    idset = set(ids)
    basliklar = {}
    for g in durum["gorevler"]:
        gid = g["id"]
        if g.get("durum") not in DURUMLAR:
            bulgular.append(f"KUYRUK: {gid} geçersiz durum '{g.get('durum')}'")
        if g.get("oncelik") not in ONCELIK:
            bulgular.append(f"KUYRUK: {gid} geçersiz öncelik '{g.get('oncelik')}'")
        onay = g.get("onay") or ""
        if g.get("onay_seviyesi") in {"A2", "A3"} and g.get("durum") in {"approved", "queued", "in_progress"}:
            if not onay.startswith("Bora"):
                bulgular.append(f"KUYRUK: {gid} {g['onay_seviyesi']} ama onay Bora'dan değil: '{onay}'")
            if g["onay_seviyesi"] == "A2" and "max" not in onay:
                bulgular.append(f"KUYRUK: {gid} A2 onayında azami kredi yok")
        if g.get("onay_seviyesi") == "A0" and onay and onay != "A0":
            bulgular.append(f"KUYRUK: {gid} A0 görevinin onay alanı 'A0' olmalı")
        for b in g.get("bagimliliklar", []):
            if b not in idset:
                bulgular.append(f"KUYRUK: {gid} bilinmeyen bağımlılık {b}")
        if g.get("deneme", 0) > cfg["limitler"]["gorev_deneme_azami"]:
            bulgular.append(f"KUYRUK: {gid} deneme sayısı sınırı aşıyor")
        anahtar = (g.get("baslik", "").strip().lower(), g.get("surum", 1))
        if anahtar in basliklar and g["durum"] not in {"cancelled", "archived"}:
            bulgular.append(f"KUYRUK: {gid} ile {basliklar[anahtar]} aynı başlık ve sürüm (tekrar iş)")
        basliklar[anahtar] = gid
    if durum.get("simdi") and durum["simdi"] not in idset:
        bulgular.append("KUYRUK: simdi alanı var olmayan göreve işaret ediyor")
    no = max([int(i.split("-")[1]) for i in ids] or [0])
    if durum["sayac"]["son_gorev_no"] < no:
        bulgular.append("KUYRUK: sayac.son_gorev_no en büyük görev numarasından küçük")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--degisen", nargs="*", default=None, help="Denetlenen değişiklikteki dosyalar (Bekçi)")
    a = p.parse_args()
    bulgular = []
    for yol in izlenen_dosyalar():
        if yol.startswith("arsiv/") or yol.startswith("scripts/") or yol.startswith("tests/"):
            continue
        tam = KOK / yol
        if not tam.is_file() or tam.stat().st_size > 2_000_000:
            continue
        if tam.suffix.lower() in {".mp4", ".mov", ".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            bulgular.append(f"MEDYA: {yol} repoya medya dosyası eklenmemeli (bkz. README §Medya)")
            continue
        metin = tam.read_text(encoding="utf-8", errors="ignore")
        for d in SIR_DESENLERI:
            if re.search(d, metin):
                bulgular.append(f"SIR: {yol} sır görünümlü dize ({d})")
        if Path(yol).name in {".env"} or Path(yol).name.startswith(".env."):
            if Path(yol).name != ".env.example":
                bulgular.append(f"SIR: {yol} .env dosyası repoda")
    yon = (KOK / "vardiyalar/YONETICI.md").read_text(encoding="utf-8")
    if SAYI_YASAK.search(yon):
        bulgular.append("TEK-KAYNAK: YONETICI.md sıklık sayısı içeriyor; sıklık yalnızca CONFIG.json'da yazılır")
    if a.degisen is not None:
        for yol in a.degisen:
            if any(k.search(yol) for k in KORUNAN):
                bulgular.append(f"KORUNAN: {yol} ajanlar için salt okunur (Anayasa 19) — yalnızca Bora birleştirir")
    kuyruk_kontrol(bulgular)
    for b in bulgular:
        print(b)
    print("TEMİZ" if not bulgular else f"{len(bulgular)} BULGU")
    sys.exit(1 if bulgular else 0)


if __name__ == "__main__":
    main()
