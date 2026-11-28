#!/usr/bin/env python3
"""Önceden kayıtlı tahminleri sonraki ölçümle karşılaştırır (G-0061, K-036). Yalnız stdlib.
Kullanım: python3 -I scripts/tahmin_karsilastir.py --tahmin T.json --t0 T0.json --sonraki S.json --ufuk 48s|14g [--cikti C.json]
Her tahmin için: gerçek değişim %, hata (tahmin-gerçek), %80 aralık isabeti, (14g) medyan yön isabeti.
Özet: bizim tahmin vs saf kıyas 'degisim_yok' ve 'klip_sikligi_kurali' (ortalama mutlak hata, puan).
Bu betik tahmin dosyasını DEĞİŞTİRMEZ."""
import argparse, json, sys
from pathlib import Path

ESIK = 0.20  # 'aynı' bandı

def anahtar(platform, hesap):
    return (platform, hesap.lower().lstrip("@"))

def indeksle(olcum):
    return {anahtar(p, x.get("hesap", "")): x for p in ("youtube", "tiktok") for x in olcum.get(p, []) if "hesap" in x}

def deger(x, alan, yedek=None):
    v = x.get(alan)
    if v is None and yedek:
        v = x.get(yedek)
    return v

def yuzde(yeni, eski):
    if eski in (None, 0) or yeni is None:
        return None
    return (yeni - eski) / eski * 100.0

def yon(oran):
    if oran is None:
        return None
    return "artar" if oran > 1 + ESIK else ("azalır" if oran < 1 - ESIK else "aynı")

def mae(liste):
    liste = [v for v in liste if v is not None]
    return sum(liste) / len(liste) if liste else None

def karsilastir(tahmin, t0, sonraki, ufuk):
    if ufuk not in ("48s", "14g"):
        raise ValueError("ufuk 48s ya da 14g olmalı")
    i0, i1 = indeksle(t0), indeksle(sonraki)
    satirlar, atlanan = [], []
    for r in tahmin["tahminler"]:
        k = anahtar(r["platform"], r["hesap"])
        t = r.get("tahmin")
        if not t:
            continue
        a, b = i0.get(k), i1.get(k)
        if not a or not b:
            atlanan.append({"hesap": r["hesap"], "platform": r["platform"], "neden": "t0 ya da sonraki ölçümde yok"})
            continue
        ft, mt = r["t0"]["alan_takipci"], r["t0"]["alan_medyan"]
        yedek = "takipci" if ft == "takipci_tam" else None
        f0, f1 = deger(a, ft, yedek), deger(b, ft, yedek)
        m0, m1 = a.get(mt), b.get(mt)
        gercek = yuzde(f1, f0)
        if gercek is None:
            atlanan.append({"hesap": r["hesap"], "platform": r["platform"], "neden": "takipçi okunamadı"})
            continue
        alan = "takipci_" + ufuk
        t_nokta = t[alan]["nokta_pct"]; lo, hi = t[alan]["aralik80_pct"]
        kiyas = r["saf_kiyas"]
        s = {"hesap": r["hesap"], "platform": r["platform"], "t0_takipci": f0, "sonraki_takipci": f1,
             "gercek_pct": round(gercek, 4), "tahmin_pct": t_nokta, "hata": round(t_nokta - gercek, 4),
             "mutlak_hata": round(abs(t_nokta - gercek), 4), "aralik_isabet": bool(lo <= gercek <= hi),
             "kiyas_degisim_yok_mh": round(abs(kiyas["degisim_yok"]["takipci_%s_pct" % ufuk] - gercek), 4),
             "kiyas_sik_kural_mh": round(abs(kiyas["klip_sikligi_kurali"]["takipci_%s_pct" % ufuk] - gercek), 4)}
        if ufuk == "14g":
            oran = (m1 / m0) if (m0 and m1 is not None) else None
            gy = yon(oran)
            s.update({"medyan_t0": m0, "medyan_sonraki": m1, "gercek_yon": gy, "tahmin_yon": t["medyan_14g_yon"],
                      "yon_isabet": (gy == t["medyan_14g_yon"]) if gy else None,
                      "kiyas_yon_isabet": (gy == "aynı") if gy else None})
        satirlar.append(s)
    ozet = {"ufuk": ufuk, "n": len(satirlar), "atlanan": atlanan,
            "mae_bizim": mae([s["mutlak_hata"] for s in satirlar]),
            "mae_degisim_yok": mae([s["kiyas_degisim_yok_mh"] for s in satirlar]),
            "mae_klip_sikligi_kurali": mae([s["kiyas_sik_kural_mh"] for s in satirlar]),
            "aralik_isabet_orani": mae([1.0 if s["aralik_isabet"] else 0.0 for s in satirlar])}
    if ufuk == "14g":
        v = [s for s in satirlar if s.get("yon_isabet") is not None]
        ozet["yon_isabet_bizim"] = mae([1.0 if s["yon_isabet"] else 0.0 for s in v])
        ozet["yon_isabet_degisim_yok"] = mae([1.0 if s["kiyas_yon_isabet"] else 0.0 for s in v])
    b = ozet["mae_bizim"]; ks = [x for x in (ozet["mae_degisim_yok"], ozet["mae_klip_sikligi_kurali"]) if x is not None]
    ozet["bizim_iki_kiyasi_de_yeniyor"] = bool(b is not None and ks and all(b < x for x in ks))
    ozet["not"] = "n küçükse sonuç kesin değildir; tek pencere. Kıyası yenmek yetenek kanıtı değil, ipucudur."
    return {"ozet": ozet, "satirlar": satirlar}

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--tahmin", required=True); p.add_argument("--t0", required=True)
    p.add_argument("--sonraki", required=True); p.add_argument("--ufuk", required=True, choices=["48s", "14g"])
    p.add_argument("--cikti")
    a = p.parse_args(argv)
    y = lambda f: json.loads(Path(f).read_text(encoding="utf-8"))
    sonuc = karsilastir(y(a.tahmin), y(a.t0), y(a.sonraki), a.ufuk)
    if a.cikti:
        Path(a.cikti).write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(sonuc["ozet"], ensure_ascii=False, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
