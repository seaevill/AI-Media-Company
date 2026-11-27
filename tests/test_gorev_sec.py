#!/usr/bin/env python3
"""Görev seçici testleri. Çalıştır: python3 -I tests/test_gorev_sec.py"""
import json, sys, copy
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import gorev_sec as gs  # noqa: E402

CFG = json.loads((Path(__file__).resolve().parent.parent / "vardiyalar/CONFIG.json").read_text())
T = datetime(2026, 11, 27, 8, 0, tzinfo=timezone.utc)  # Atina 10:00 -> ipucu produksiyon-maliyet

def g(i, **k):
    d = {"id": i, "baslik": i, "oncelik": "P4", "departman": "pazar-istihbarati", "onay": "A0",
         "onay_seviyesi": "A0", "durum": "queued", "deneme": 0, "bagimliliklar": [], "olusturma": "2026-11-27T00:00:00Z"}
    d.update(k); return d

def durum(*gorevler, simdi=None, gunluk=None):
    return {"gorevler": list(gorevler), "simdi": simdi, "gunluk": gunluk or {}}

sonuclar = []
def test(ad, kosul):
    sonuclar.append((ad, kosul)); print(("GEÇTİ " if kosul else "KALDI ") + ad)
test.__test__ = False  # pytest bunu test sanmasın

r = gs.sec(durum(g("G-1", oncelik="P5"), g("G-2", oncelik="P3")), CFG, T)
test("öncelik sırası: P3, P5'ten önce", r["gorev"]["id"] == "G-2")
r = gs.sec(durum(g("G-1", onay=None)), CFG, T)
test("onaysız görev alınmaz", r["karar"] == "is_yok")
r = gs.sec(durum(g("G-1", durum="completed"), g("G-2", durum="waiting_owner", onay=None)), CFG, T)
test("tamamlanan görev tekrar alınmaz; iş yoksa dur", r["karar"] == "is_yok")
r = gs.sec(durum(g("G-1", bagimliliklar=["G-2"]), g("G-2", durum="waiting_owner", onay=None)), CFG, T)
test("bağımlılığı bitmemiş görev alınmaz", r["karar"] == "is_yok")
r = gs.sec(durum(g("G-1", en_erken="2026-12-01T00:00:00Z")), CFG, T)
test("zamanı gelmemiş görev alınmaz", r["karar"] == "is_yok")
r = gs.sec(durum(g("G-1", deneme=2)), CFG, T)
test("deneme hakkı dolan görev alınmaz", r["karar"] == "is_yok")
r = gs.sec(durum(g("G-1", durum="in_progress"), g("G-2", oncelik="P0"), simdi="G-1"), CFG, T)
test("yarım görev varken yenisi alınmaz (P0 bile)", r["karar"] == "devam" and r["gorev"]["id"] == "G-1")
r = gs.sec(durum(g("G-1"), gunluk={"tarih": "2026-11-27", "ajanli_kosu": CFG["limitler"]["gunluk_ajanli_kosu_azami"]}), CFG, T)
test("günlük sınır dolunca yalnızca rapor", r["karar"] == "sinir")
r = gs.sec(durum(g("G-1", departman="pazar-istihbarati"), g("G-2", departman="produksiyon-maliyet")), CFG, T)
test("eşit öncelikte vardiya ipucu (Atina 10:00 → produksiyon)", r["gorev"]["id"] == "G-2")
r = gs.sec(durum(g("G-1", durum="needs_revision", deneme=2), simdi="G-1"), CFG, T)
test("iki düzeltmeden sonra engel", r["karar"] == "engel")

# İkinci koşu simülasyonu: ilk koşunun yazdığı durumla aynı görev tekrar seçilmemeli
d = durum(g("G-1", oncelik="P4"), g("G-2", oncelik="P5"))
r1 = gs.sec(d, CFG, T)
d2 = copy.deepcopy(d)
for x in d2["gorevler"]:
    if x["id"] == r1["gorev"]["id"]:
        x["durum"] = "completed"; x["deneme"] = 1
r2 = gs.sec(d2, CFG, T)
test("ikinci koşu bir sonraki görevi alır, tamamlananı değil", r1["gorev"]["id"] == "G-1" and r2["gorev"]["id"] == "G-2")

r = gs.sec(durum(g("G-1", durum="in_progress", oncelik="P4"), g("G-2", oncelik="P2")), CFG, T)
test("simdi boşken yetim in_progress görev bitirilir (kuru koşu A bulgusu)", r["karar"] == "devam" and r["gorev"]["id"] == "G-1")
r = gs.sec(durum(g("G-1", durum="review", oncelik="P5"), g("G-2", durum="in_progress", oncelik="P1")), CFG, T)
test("birden çok yarım görevde en öncelikli önce", r["gorev"]["id"] == "G-2")
r = gs.sec(durum(g("G-1", departman="kreatif-direktor")), CFG, T)
test("ipucu eşleşmezse gerekçe bunu söyler", "ipucu etkisiz" in r["gerekce"])

kalan = [a for a, k in sonuclar if not k]
print(f"{len(sonuclar)-len(kalan)}/{len(sonuclar)} geçti")


def test_gorev_sec_hepsi():  # pytest toplayıcısı için; doğrudan çalıştırma davranışı aynı
    assert not kalan, kalan


if __name__ == "__main__":
    sys.exit(1 if kalan else 0)
