#!/usr/bin/env python3
"""Hesap ölçer — kamuya açık platform sayfasından DOĞRUDAN sayı okur (arama özeti değil).

Kullanım:
  python3 -I scripts/hesap_olc.py youtube @NeuralViz [@başka ...]
  python3 -I scripts/hesap_olc.py tiktok meowtakeover [başka ...]

Çıktı: her hesap için JSON — ölçüm zamanı (UTC), URL, HTTP kodu, okunan ham alanlar ve
türetilen değerler. YouTube: abone metni + Shorts sekmesindeki ilk N klibin izlenmesi
(medyan, en düşük, en yüksek, aykırı değer oranı). TikTok: statusCode (0 = var,
10221 = yok), takipçi, beğeni, video sayısı. Giriş, CAPTCHA veya bot korumasına takılırsa
"engel" alanına yazar ve AŞMAZ.
Sınır: YouTube Shorts sekmesindeki sıralama ve kapsam garanti değildir (genelde en yeni
~30 klip). TikTok'ta video başına izlenme bu yöntemle okunmaz.
"""
import json
import re
import statistics
import subprocess
import sys
from datetime import datetime, timezone

UA = "Mozilla/5.0"
CARPAN = {"thousand": 1e3, "million": 1e6, "billion": 1e9, "K": 1e3, "M": 1e6, "B": 1e9}


def getir(url):
    r = subprocess.run(["curl", "-s", "-L", "-m", "30", "-A", UA, "-H", "Accept-Language: en",
                        "-w", "\n__HTTP__%{http_code} %{url_effective}", url], capture_output=True, text=True)
    govde, _, son = r.stdout.rpartition("\n__HTTP__")
    kod, _, nihai = son.partition(" ")
    return govde, kod, nihai


def sayiya(metin):
    m = re.match(r"([\d.,]+)\s*(thousand|million|billion|K|M|B)?", metin.strip())
    if not m:
        return None
    sayi = float(m.group(1).replace(",", ""))
    return int(sayi * CARPAN.get(m.group(2) or "", 1))


def youtube(handle):
    handle = handle if handle.startswith("@") else "@" + handle
    url = f"https://www.youtube.com/{handle}/shorts"
    govde, kod, nihai = getir(url)
    s = {"platform": "youtube", "hesap": handle, "url": url, "olcum_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "http": kod, "kaynak_turu": "GÖRDÜM (platform sayfası)"}
    if "sorry" in nihai or "consent." in nihai:
        s["engel"] = f"yönlendirme: {nihai} (aşılmadı)"
        return s
    if kod == "404":
        s["durum"] = "hesap bulunamadı (404)"
        return s
    abone = re.findall(r'"metadataParts":\[\{"text":\{"content":"([^"]*subscribers)"', govde)
    s["abone_metni"] = abone[0] if abone else None
    s["abone_yaklasik"] = sayiya(abone[0].replace(" subscribers", "")) if abone else None
    izlenmeler = [sayiya(x) for x in re.findall(r'"accessibilityText":"[^"]*?, ([\d.,]+ (?:thousand|million|billion)?\s*views)', govde)]
    izlenmeler = [i for i in izlenmeler if i is not None]
    s["shorts_n"] = len(izlenmeler)
    if izlenmeler:
        med = statistics.median(izlenmeler)
        s.update({"shorts_izlenme_medyan": int(med), "shorts_en_dusuk": min(izlenmeler), "shorts_en_yuksek": max(izlenmeler),
                  "en_yuksek_medyana_orani": round(max(izlenmeler) / med, 1) if med else None,
                  "shorts_izlenmeler": izlenmeler})
        if s["abone_yaklasik"]:
            s["medyan_izlenme_abone_orani"] = round(med / s["abone_yaklasik"], 3)
    else:
        s["not"] = "Shorts izlenmesi okunamadı (sekme boş, yapı değişti ya da Shorts yok)"
    return s


def tiktok(handle):
    handle = handle.lstrip("@")
    url = f"https://www.tiktok.com/@{handle}"
    govde, kod, nihai = getir(url)
    s = {"platform": "tiktok", "hesap": "@" + handle, "url": url, "olcum_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "http": kod, "kaynak_turu": "GÖRDÜM (platform sayfası, gömülü veri)"}
    def al(alan):
        m = re.search(rf'"{alan}":(\d+)', govde)
        return int(m.group(1)) if m else None
    s["statusCode"] = al("statusCode")
    s["durum"] = {0: "hesap var", 10221: "hesap bulunamadı"}.get(s["statusCode"], "bilinmiyor")
    if s["statusCode"] == 0:
        s.update({"takipci": al("followerCount"), "begeni_toplam": al("heartCount"), "video_sayisi": al("videoCount")})
        if s["takipci"] is None:
            s["engel"] = "sayılar gömülü veride yok (giriş/bot koruması olabilir; aşılmadı)"
    return s


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("youtube", "tiktok"):
        print(__doc__)
        return 2
    fn = youtube if sys.argv[1] == "youtube" else tiktok
    print(json.dumps([fn(h) for h in sys.argv[2:]], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
