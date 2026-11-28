#!/usr/bin/env python3
"""Hesap ölçer — kamuya açık platform sayfasından DOĞRUDAN sayı okur (arama özeti değil).

Kullanım:
  python3 -I scripts/hesap_olc.py youtube @NeuralViz [@başka ...]
  python3 -I scripts/hesap_olc.py tiktok meowtakeover [başka ...]

Çıktı: her hesap için JSON — ölçüm zamanı (UTC), URL, HTTP kodu, okunan ham alanlar ve
türetilen değerler. YouTube: abone metni + Shorts sekmesindeki ilk N klibin izlenmesi
(medyan, en düşük, en yüksek, aykırı değer oranı). TikTok: statusCode (0 = var,
10221 = yok), takipçi, beğeni, video sayısı (profil sayfası, yuvarlanmış + statsV2'de tam
sayı) ve embed sayfasındaki (https://www.tiktok.com/embed/@hesap) son kliplerin izlenmesi
(playCount): medyan, en düşük, en yüksek, en yüksek/medyan. Giriş, CAPTCHA veya bot
korumasına takılırsa "engel" alanına yazar ve AŞMAZ.
Sınır: YouTube Shorts sekmesindeki sıralama ve kapsam garanti değildir (genelde en yeni
~30 klip). TikTok embed sayfası ~10-15 klip verir; başta sabitlenmiş (pinned) klipler olabilir
— sabitleme bayrağı yok, tarih (video kimliğinden) sırasına bakılarak TAHMİN edilir ve
"son klip" istatistiğinden çıkarılır. Profil sayfasında video listesi boş gelir (itemList: []);
/embed/v2/<id> sayfası veri taşımaz (yalnız JS kabuğu).
"""
import json
import re
import statistics
import subprocess
import sys
import time
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


def youtube_shorts_ayikla(govde):
    """Shorts sekmesi HTML'inden [{videoId, izlenme, baslik}] (sayfadaki sırayla; aynı id bir kez)."""
    cikti, gorulen = [], set()
    for vid, metin in re.findall(
            r'"entityId":"shorts-shelf-item-([\w-]{11})","accessibilityText":"((?:[^"\\]|\\.)*)"', govde):
        if vid in gorulen:
            continue
        m = re.search(r'^(.*), ([\d.,]+(?: thousand| million| billion)?|No) views? - play Short$', metin)
        if not m:
            continue
        gorulen.add(vid)
        izl = 0 if m.group(2) == "No" else sayiya(m.group(2))
        cikti.append({"videoId": vid, "izlenme": izl, "baslik": m.group(1)})
    return cikti


def youtube(handle):
    handle = handle if handle.startswith("@") else "@" + handle
    url = f"https://www.youtube.com/{handle}/shorts"
    govde, kod, nihai = getir(url)
    s = {"platform": "youtube", "hesap": handle, "url": url, "olcum_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "http": kod, "kaynak_turu": "ÖLÇTÜM (araç, platform sayfası)"}
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
    s["shorts_klipler"] = youtube_shorts_ayikla(govde)
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


def gomulu_json(html, script_id):
    m = re.search(rf'<script id="{script_id}"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def tiktok_profil_ayikla(govde):
    """Profil HTML'inden statusCode + hesap sayıları (eski alan adları korunur)."""
    def al(alan):
        m = re.search(rf'"{alan}":(\d+)', govde)
        return int(m.group(1)) if m else None
    s = {"statusCode": al("statusCode")}
    s["durum"] = {0: "hesap var", 10221: "hesap bulunamadı"}.get(s["statusCode"], "bilinmiyor")
    if s["statusCode"] == 0:
        s.update({"takipci": al("followerCount"), "begeni_toplam": al("heartCount"), "video_sayisi": al("videoCount")})
        if s["takipci"] is None:
            s["engel"] = "sayılar gömülü veride yok (giriş/bot koruması olabilir; aşılmadı)"
        m = re.search(r'"statsV2":\{"followerCount":"(\d+)"', govde)
        if m:
            s["takipci_tam"] = int(m.group(1))
    return s


def video_tarihi(vid):
    """TikTok video kimliğinin üst 32 biti yükleme anının Unix saniyesidir."""
    try:
        return datetime.fromtimestamp(int(vid) >> 32, timezone.utc).date().isoformat()
    except (ValueError, OverflowError, OSError):
        return None


def tiktok_embed_ayikla(html, handle):
    """embed/@hesap HTML'inden klip listesi + izlenme özeti. Ham medya adresleri alınmaz."""
    durum = gomulu_json(html, "__FRONTITY_CONNECT_STATE__")
    if durum is None:
        return {"engel": "embed sayfasında gömülü veri yok (CAPTCHA/bot koruması ya da yapı değişti; aşılmadı)"}
    veri = (durum.get("source", {}).get("data", {}) or {}).get(f"/embed/@{handle}")
    if not veri:
        return {"engel": "embed verisinde hesap düğümü yok (yapı değişti olabilir)"}
    if veri.get("isError"):
        return {"embed_hata_kodu": veri.get("errorCode")}
    klipler = [{"id": v.get("id"), "tarih": video_tarihi(v.get("id")), "izlenme": v.get("playCount")}
               for v in veri.get("videoList") or [] if isinstance(v.get("playCount"), int) and not v.get("privateItem")]
    # Sabitlenmiş tahmini: baştaki (en çok 3) klip, kendisinden sonra gelen daha yeni bir klip varsa.
    sabit = 0
    while sabit < min(3, len(klipler) - 1) and int(klipler[sabit]["id"]) < max(int(k["id"]) for k in klipler[sabit + 1:]):
        sabit += 1
    s = {"embed_klipler": klipler, "sabitlenmis_tahmin": [k["id"] for k in klipler[:sabit]]}
    son = [k["izlenme"] for k in klipler[sabit:]]
    s["video_n"] = len(son)
    if son:
        med = statistics.median(son)
        s.update({"video_izlenme_medyan": int(med), "video_en_dusuk": min(son), "video_en_yuksek": max(son),
                  "en_yuksek_medyana_orani": round(max(son) / med, 1) if med else None,
                  "video_izlenmeler": son, "son_klip_tarih_araligi": [klipler[-1]["tarih"], klipler[sabit]["tarih"]]})
    else:
        s["not"] = "embed sayfasında izlenme sayısı olan klip yok"
    return s


def tiktok(handle):
    handle = handle.lstrip("@")
    url = f"https://www.tiktok.com/@{handle}"
    govde, kod, nihai = getir(url)
    s = {"platform": "tiktok", "hesap": "@" + handle, "url": url, "olcum_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "http": kod, "kaynak_turu": "ÖLÇTÜM (araç, platform sayfası, gömülü veri)"}
    s.update(tiktok_profil_ayikla(govde))
    if s["statusCode"] == 10221:
        return s
    eurl = f"https://www.tiktok.com/embed/@{handle}"
    egovde, ekod, _ = getir(eurl)
    if ekod.startswith("5"):  # gözlenen: ara sıra geçici 500; tek tekrar (engel aşma değil)
        time.sleep(3)
        egovde, ekod, _ = getir(eurl)
    s["embed_url"], s["embed_http"] = eurl, ekod
    if ekod.startswith("5"):
        s["embed_hata"] = f"embed sayfası sunucu hatası {ekod} (2 deneme; geçici olabilir)"
        return s
    e = tiktok_embed_ayikla(egovde, handle)
    if "engel" in e:
        s["embed_engel"] = e.pop("engel")
    s.update(e)
    takipci = s.get("takipci_tam") or s.get("takipci")
    if s.get("video_izlenme_medyan") is not None and takipci:
        s["medyan_izlenme_takipci_orani"] = round(s["video_izlenme_medyan"] / takipci, 3)
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
