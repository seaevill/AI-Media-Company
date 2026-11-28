#!/usr/bin/env python3
"""Ham ölçüm dosyasından "sağlıklı" eşiği duyarlılık analizi + TikTok son klip yaşı/yayın sıklığı (G-0053).

Kullanım:
  python3 -I scripts/duyarlilik_analizi.py istihbarat/olcumler/2026-11-27.json [g0048]
  (g0048: yalnız G-0048 örneklemindeki hesaplar)

Girdi: scripts/hesap_olc.py çıktısının birleştirildiği {"olcum_basla_utc", "youtube": [...], "tiktok": [...]} dosyası.
Ağ yok, kredi yok. Eşik: sağlıklı = medyan/takipçi >= oran_esigi VE en yüksek/medyan <= yuksek_esigi.
Filtre (G-0048 ile aynı): klip sayısı n >= 8 ve takipçi >= 1000.
TikTok'ta iki sürüm: "haric" = sabitlenmiş tahmini klipler çıkarılmış (aracın varsayılanı),
"dahil" = embed'deki tüm klipler (en yüksek/medyan, tüm klip medyanına göre).
"""
import json
import statistics
import sys
from datetime import date, datetime

# G-0048 örneklemi (rapor tablosu, n>=8 ve >=1000 takipçi şartını geçen hesaplar). Ham dosyada olmayanlar atlanır.
G0048_YT = ("@BandarApnaDost", "@meowtakeover", "@MPMinds_", "@tailbitpets", "@storyarcpaws", "@funntastic_AI",
            "@HasanAi202", "@kittenstoriesdaily01", "@catrealmai", "@animalshortssb", "@AiKittenverse", "@ai.shxdda",
            "@Yellowchicksss")
G0048_TT = ("@meowtakeover", "@mpminds", "@tailbitpets", "@chubbycat_1", "@aibeaststudio", "@pablo.prompt",
            "@cat_tommmy", "@asmraiworks", "@catrealmai", "@satisfyingclips50", "@poutyfrenchie")
ORAN_ESIKLERI = (0.05, 0.1, 0.2)
YUKSEK_ESIKLERI = (5, 10, 20)


def saglikli(oran, yuksek, oran_esigi, yuksek_esigi):
    if oran is None or yuksek is None:
        return False
    return oran >= oran_esigi and yuksek <= yuksek_esigi


def _ref_tarih(olcum_utc):
    return datetime.fromisoformat(olcum_utc.replace("Z", "+00:00")).date()


def satirlar(veri):
    """Ham ölçümden hesap-platform satırları. Filtre uygulamaz."""
    out = []
    for h in veri.get("youtube", []):
        if h.get("shorts_n"):
            out.append({"platform": "YT", "hesap": h["hesap"], "takipci": h.get("abone_yaklasik"), "n": h["shorts_n"],
                        "oran": h.get("medyan_izlenme_abone_orani"), "yuksek": h.get("en_yuksek_medyana_orani"),
                        "yuksek_dahil": None, "son_klip": None, "gun": None, "sikilik": None,
                        "olcum_utc": h["olcum_utc"]})
    for h in veri.get("tiktok", []):
        klipler = h.get("embed_klipler") or []
        if not klipler:
            continue
        ref = _ref_tarih(h["olcum_utc"])
        sab = set(h.get("sabitlenmis_tahmin", []))
        son = [k for k in klipler if k["id"] not in sab]
        tum = [k["izlenme"] for k in klipler]
        med_tum = statistics.median(tum)
        tarihler = sorted(date.fromisoformat(k["tarih"]) for k in son if k.get("tarih"))
        son_klip = tarihler[-1] if tarihler else None
        aralik = (tarihler[-1] - tarihler[0]).days if len(tarihler) > 1 else None
        out.append({"platform": "TT", "hesap": h["hesap"], "takipci": h.get("takipci_tam") or h.get("takipci"),
                    "n": h.get("video_n", len(son)), "oran": h.get("medyan_izlenme_takipci_orani"),
                    "yuksek": h.get("en_yuksek_medyana_orani"),
                    "yuksek_dahil": round(max(tum) / med_tum, 1) if med_tum else None,
                    "son_klip": son_klip.isoformat() if son_klip else None,
                    "gun": (ref - son_klip).days if son_klip else None,
                    # klip/gün: embed örneğindeki (sabitlenmişsiz) klipler arası ortalama sıklık; örnek 10-13 klip
                    "sikilik": round((len(tarihler) - 1) / aralik, 2) if aralik else None,
                    "olcum_utc": h["olcum_utc"]})
    return out


def g0048(rows):
    """Yalnız G-0048 örneklemindeki satırlar (ham dosyada bulunanlar)."""
    return [r for r in rows if r["hesap"] in (G0048_YT if r["platform"] == "YT" else G0048_TT)]


def uygun(s, min_n=8, min_takipci=1000):
    return s["n"] >= min_n and (s["takipci"] or 0) >= min_takipci


def izgara(rows, oranlar=ORAN_ESIKLERI, yuksekler=YUKSEK_ESIKLERI):
    """{(platform, surum): {(oran, yuksek): [sağlıklı hesaplar]}}; TT için haric+dahil, YT için haric."""
    sonuc = {}
    for pl, surum, alan in (("YT", "haric", "yuksek"), ("TT", "haric", "yuksek"), ("TT", "dahil", "yuksek_dahil")):
        sel = [r for r in rows if r["platform"] == pl and uygun(r)]
        sonuc[(pl, surum)] = {"n": len(sel)}
        for o in oranlar:
            for y in yuksekler:
                sonuc[(pl, surum)][(o, y)] = [r["hesap"] for r in sel if saglikli(r["oran"], r[alan], o, y)]
    return sonuc


def siralar(xs):
    """Ortalama sıralar (bağlarda ortalama)."""
    srt = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(srt):
        j = i
        while j + 1 < len(srt) and xs[srt[j + 1]] == xs[srt[i]]:
            j += 1
        for k in range(i, j + 1):
            r[srt[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(x, y):
    if len(x) != len(y) or len(x) < 3:
        return None
    rx, ry = siralar(x), siralar(y)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    pay = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    payda = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return round(pay / payda, 3) if payda else None


def main():
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        veri = json.load(f)
    rows = satirlar(veri)
    if len(sys.argv) == 3 and sys.argv[2] == "g0048":
        rows = g0048(rows)
    print("# Duyarlilik izgarasi (oran esigi x yuksek/medyan esigi) -> saglikli sayisi / n")
    g = izgara(rows)
    for (pl, sv), d in g.items():
        print(f"\n{pl} {sv} (n={d['n']})")
        print("oran\\yuksek " + " ".join(f"{y:>6}" for y in YUKSEK_ESIKLERI))
        for o in ORAN_ESIKLERI:
            print(f"{o:>11} " + " ".join(f"{len(d[(o, y)]):>6}" for y in YUKSEK_ESIKLERI))
        print("  0,1/10 sağlıklı:", ", ".join(d[(0.1, 10)]) or "-")
    tt = [r for r in rows if r["platform"] == "TT" and r["gun"] is not None and r["oran"] is not None]
    print("\n# TikTok: hesap, takipci, son klip, gun, klip/gun, medyan/takipci")
    for r in sorted(tt, key=lambda r: r["gun"]):
        print(f"{r['hesap']:<20} {r['takipci']:>10} {r['son_klip']} {r['gun']:>4} {r['sikilik']} {r['oran']}")
    print("Spearman(son klip yaşı gün, medyan/takipçi), n=%d: %s" % (len(tt), spearman([r["gun"] for r in tt], [r["oran"] for r in tt])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
