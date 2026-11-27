#!/usr/bin/env python3
"""Vardiya yöneticisinin görev seçicisi (deterministik).

Kullanım:
  python3 -I scripts/gorev_sec.py [--simdi 2026-11-27T10:00:00+02:00] [--durum vardiyalar/DURUM.json]

Çıktı (stdout, JSON): {"karar": "gorev"|"devam"|"is_yok"|"sinir", "gorev": {...}|null, "gerekce": "..."}
Kurallar YONETICI.md §4 ile birebir aynıdır; bu dosya değişirse YONETICI.md de değişir.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

KOK = Path(__file__).resolve().parent.parent
ONCELIK = ["P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7"]
ALINABILIR = {"approved", "queued", "needs_revision"}
BITMIS = {"completed", "cancelled", "archived"}


def yukle(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def zaman(s):
    if not s:
        return None
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def vardiya_takimi(cfg, simdi_yerel):
    s = simdi_yerel.hour
    for aralik, takim in cfg.get("vardiya_ipuclari", {}).items():
        if aralik.startswith("_"):
            continue
        a, b = (int(x) for x in aralik.split("-"))
        if a <= s < b:
            return takim
    return None


def sec(durum, cfg, simdi):
    tz = ZoneInfo(cfg.get("saat_dilimi", "UTC"))
    yerel = simdi.astimezone(tz)
    lim = cfg["limitler"]
    gorevler = {g["id"]: g for g in durum.get("gorevler", [])}

    # 1) Yarım kalmış iş önce (P1 kuralı): simdi doluysa ve görev bitmemişse devam.
    sid = durum.get("simdi")
    if sid and sid in gorevler and gorevler[sid]["durum"] not in BITMIS:
        g = gorevler[sid]
        if g["durum"] in {"in_progress", "review", "needs_revision"}:
            if g.get("deneme", 0) >= lim["gorev_deneme_azami"] and g["durum"] == "needs_revision":
                return {"karar": "engel", "gorev": g, "gerekce": "deneme hakkı doldu; blocked yapılıp Bora'ya bildirilmeli"}
            return {"karar": "devam", "gorev": g, "gerekce": "simdi alanındaki yarım görev tamamlanmadan yeni görev alınmaz"}

    # 2) Günlük sınır.
    gun = durum.get("gunluk", {})
    if gun.get("tarih") == yerel.date().isoformat() and gun.get("ajanli_kosu", 0) >= lim["gunluk_ajanli_kosu_azami"]:
        return {"karar": "sinir", "gorev": None, "gerekce": "günlük ajanlı koşu sınırı doldu; yalnızca rapor"}

    # 3) Aday filtrele.
    adaylar = []
    for g in durum.get("gorevler", []):
        if g["durum"] not in ALINABILIR:
            continue
        if not g.get("onay"):
            continue
        if g.get("deneme", 0) >= lim["gorev_deneme_azami"]:
            continue
        if any(gorevler.get(b, {}).get("durum") != "completed" for b in g.get("bagimliliklar", [])):
            continue
        en_erken = zaman(g.get("en_erken"))
        if en_erken and en_erken > simdi:
            continue
        adaylar.append(g)

    if not adaylar:
        return {"karar": "is_yok", "gorev": None, "gerekce": "onaylı, bağımlılığı tamam, zamanı gelmiş görev yok (Anayasa 21: dur)"}

    ipucu = vardiya_takimi(cfg, yerel)
    adaylar.sort(key=lambda g: (
        ONCELIK.index(g.get("oncelik", "P7")),
        0 if g.get("departman") == ipucu else 1,
        g.get("olusturma", ""),
        g["id"],
    ))
    return {"karar": "gorev", "gorev": adaylar[0], "gerekce": f"en yüksek öncelik {adaylar[0].get('oncelik')}; vardiya ipucu={ipucu}"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--simdi")
    p.add_argument("--durum", default=str(KOK / "vardiyalar/DURUM.json"))
    p.add_argument("--config", default=str(KOK / "vardiyalar/CONFIG.json"))
    a = p.parse_args()
    simdi = zaman(a.simdi) if a.simdi else datetime.now(timezone.utc)
    sonuc = sec(yukle(a.durum), yukle(a.config), simdi)
    json.dump(sonuc, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
