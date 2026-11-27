#!/usr/bin/env python3
"""İçerik Mahkemesi skoru: konsey tablolarındaki (Profil|Kriter|Puan|...) satırları ayrıştırır,
kriter başına ortalama alır, MAHKEME.md ağırlıklarıyla 0-100 skor hesaplar.
Kullanım: python3 -I scripts/mahkeme_skor.py <konsey dosyaları...> [--ek "fikir:kriter=puan" ...]"""
import re, sys, json
AG = {"dikkat": 20, "paylas": 20, "surdur": 15, "yorum": 10, "ozgun": 10, "maliyet": 10, "seri": 10, "gelir": 5}
def kriter(k):
    k = k.lower()
    for anah, ad in [("dikkat", "dikkat"), ("paylaş", "paylas"), ("sürdür", "surdur"), ("izlenme", "surdur"), ("retention", "surdur"),
                     ("yorum", "yorum"), ("tartış", "yorum"), ("özgün", "ozgun"), ("maliyet", "maliyet"), ("seri", "seri"), ("gelir", "gelir")]:
        if anah in k: return ad
    return None
def fikir(baslik):
    b = baslik.lower()
    if "üçüncü kat" in b or "ucuncu-kat" in b: return "Üçüncü Kat"
    if "dağ kileri" in b or "dag-kileri" in b: return "Dağ Kileri"
    if "kayıp eşya" in b or "kayip-esya" in b: return "Kayıp Eşya Bürosu"
    return None
puan = {}  # (fikir, kriter) -> [(konsey, p)]
args = sys.argv[1:]; ekler = []
if "--ek" in args:
    i = args.index("--ek"); ekler = args[i+1:]; args = args[:i]
for yol in args:
    konsey = yol.split("2026-11-27-")[-1].replace(".md", "")
    simdiki = None
    for satir in open(yol, encoding="utf-8"):
        if satir.startswith("#") and "FİKİR" in satir.upper() or (satir.startswith("#") and fikir(satir)):
            simdiki = fikir(satir) or simdiki
        if simdiki and satir.startswith("|"):
            h = [x.strip() for x in satir.strip().strip("|").split("|")]
            if len(h) >= 3:
                m = re.fullmatch(r"(\d+(?:[.,]\d+)?)", h[2].replace("*", ""))
                kr = kriter(h[1])
                if m and kr:
                    puan.setdefault((simdiki, kr), []).append((konsey, float(m.group(1).replace(",", "."))))
for e in ekler:
    f, kv = e.split(":"); k, v = kv.split("=")
    puan.setdefault((f, k), []).append(("finans", float(v)))
sonuc = {}
for f in ["Üçüncü Kat", "Dağ Kileri", "Kayıp Eşya Bürosu"]:
    satirlar = {}; toplam = 0; eksik = []
    for k, w in AG.items():
        v = puan.get((f, k), [])
        if not v: eksik.append(k); continue
        # Önce konsey içi ortalama, sonra konseyler arası ortalama (kalabalık konsey baskın olmasın)
        kons = {}
        for c, p in v: kons.setdefault(c, []).append(p)
        ort = sum(sum(x)/len(x) for x in kons.values())/len(kons)
        satirlar[k] = {"ortalama": round(ort, 2), "konseyler": {c: round(sum(x)/len(x), 1) for c, x in kons.items()}, "n": len(v)}
        toplam += ort * w / 10
    agirlik_var = sum(AG[k] for k in satirlar)
    sonuc[f] = {"skor": round(toplam, 1), "normalize_skor": round(toplam * 100 / agirlik_var, 1) if agirlik_var else None, "eksik_kriter": eksik, "kriterler": satirlar}
json.dump(sonuc, sys.stdout, ensure_ascii=False, indent=1)
