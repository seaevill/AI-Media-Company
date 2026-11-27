#!/usr/bin/env python3
"""Video Intelligence Unit — otomatik katman (VIU-1).

Bir videoyu kare kare inceler ve görsel inceleme (VIU-2) için malzeme hazırlar.
Kredi harcamaz, medya dosyasını repoya yazmaz.

Kullanım:
  python3 -I scripts/video_qc.py <video.mp4> --cikti <klasör> [--fps 8] [--ad isim]

Çıktılar (<klasör>/<ad>/):
  rapor.json              ölçümler ve bayraklar
  tum_kareler_*.png       tüm video, saniyede --fps kare, numaralı kontak tabloları
  supheli_<t>.png         her şüpheli an için ±0,75 sn, 12 kare/sn, büyük boy tablo
Ölçümler:
  - teknik: çözünürlük, en-boy, süre, fps, ses kanalı, ses düzeyi, sessiz bölümler
  - hareket: ardışık kareler arası ortalama mutlak fark (küçültülmüş gri), medyan ve
    sıçrama bayrakları (fark > medyan + 4·MAD ve > 2×medyan): kesme, ışınlanma,
    kaybolma–belirme, ani nesne değişimi adayları
  - donma: ardışık fark ~0 olan ≥ 0,5 sn bölümler
  - ışık: ortalama parlaklık (karanlık sahne uyarısı: < 45/255)
Sınırlar: iç içe geçme, uzuv hatası, menteşe yönü gibi anlamsal hatalar sayısal olarak
güvenilir tespit EDİLEMEZ; bunlar VIU-2 görsel incelemesinin işidir (denetim/VIU-PROTOKOLU.md).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def calistir(komut):
    return subprocess.run(komut, capture_output=True, text=True)


def probe(yol):
    r = calistir(["ffprobe", "-v", "error", "-show_entries",
                  "stream=codec_type,width,height,r_frame_rate,duration:format=duration",
                  "-of", "json", str(yol)])
    d = json.loads(r.stdout or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in d.get("streams", []) if s.get("codec_type") == "audio"), None)
    num, den = (v.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
    fps = float(num) / float(den or 1) if float(den or 1) else 0
    w, h = int(v.get("width", 0)), int(v.get("height", 0))
    return {"genislik": w, "yukseklik": h, "en_boy": f"{w}:{h}", "dikey_9_16": bool(h and abs(w / h - 9 / 16) < 0.02),
            "sure_sn": round(float(d.get("format", {}).get("duration", 0)), 3), "kaynak_fps": round(fps, 3),
            "ses_kanali": a is not None}


def ses_olc(yol):
    r = calistir(["ffmpeg", "-hide_banner", "-i", str(yol), "-af", "volumedetect,silencedetect=n=-45dB:d=0.4", "-f", "null", "-"])
    out = r.stderr
    def bul(anahtar):
        for satir in out.splitlines():
            if anahtar in satir:
                try:
                    return float(satir.split(anahtar)[1].split()[0])
                except Exception:
                    return None
        return None
    sessiz = []
    bas = None
    for satir in out.splitlines():
        if "silence_start:" in satir:
            bas = float(satir.split("silence_start:")[1].split()[0])
        if "silence_end:" in satir and bas is not None:
            son = float(satir.split("silence_end:")[1].split()[0])
            sessiz.append([round(bas, 2), round(son, 2)])
            bas = None
    return {"ortalama_db": bul("mean_volume:"), "tepe_db": bul("max_volume:"), "sessiz_bolumler": sessiz}


def kareleri_oku(yol, fps, olcek=96):
    """Küçültülmüş gri kareleri bellek içine okur (hareket analizi için)."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(yol), "-vf", f"fps={fps},scale={olcek}:-2,format=gray",
                        "-f", "rawvideo", "-"], capture_output=True)
    ham = np.frombuffer(r.stdout, dtype=np.uint8)
    p = probe(yol)
    h = int(round(p["yukseklik"] * olcek / max(p["genislik"], 1) / 2) * 2) or olcek
    n = ham.size // (olcek * h)
    return ham[: n * olcek * h].reshape(n, h, olcek).astype(np.float32)


def kontak_tablosu(yol, fps, hedef, bas=None, sure=None, genislik=240, sutun=8):
    girdi = ["-ss", str(bas), "-t", str(sure)] if bas is not None else []
    gecici = Path(hedef).with_suffix(".kareler")
    gecici.mkdir(parents=True, exist_ok=True)
    calistir(["ffmpeg", "-v", "error", "-y", *girdi, "-i", str(yol), "-vf", f"fps={fps},scale={genislik}:-2",
              str(gecici / "k_%04d.png")])
    kareler = sorted(gecici.glob("k_*.png"))
    if not kareler:
        return []
    ornek = Image.open(kareler[0])
    w, h = ornek.size
    sayfa_kare = sutun * 4
    sayfalar = []
    for s in range(0, len(kareler), sayfa_kare):
        grup = kareler[s:s + sayfa_kare]
        satir = (len(grup) + sutun - 1) // sutun
        tablo = Image.new("RGB", (sutun * w, satir * (h + 16)), "white")
        ciz = ImageDraw.Draw(tablo)
        for i, k in enumerate(grup):
            x, y = (i % sutun) * w, (i // sutun) * (h + 16)
            tablo.paste(Image.open(k).convert("RGB"), (x, y + 16))
            t = (bas or 0) + (s + i) / fps
            ciz.text((x + 3, y + 2), f"{t:5.2f}s", fill="black")
        cikti = f"{hedef}_{s // sayfa_kare + 1}.png"
        tablo.save(cikti)
        sayfalar.append(cikti)
    for k in kareler:
        k.unlink()
    gecici.rmdir()
    return sayfalar


def analiz(yol, cikti, fps, ad):
    klasor = Path(cikti) / ad
    klasor.mkdir(parents=True, exist_ok=True)
    teknik = probe(yol)
    ses = ses_olc(yol) if teknik["ses_kanali"] else {"ortalama_db": None, "tepe_db": None, "sessiz_bolumler": []}
    kareler = kareleri_oku(yol, fps)
    farklar = np.abs(np.diff(kareler, axis=0)).mean(axis=(1, 2)) if len(kareler) > 1 else np.array([])
    bayraklar, donmalar = [], []
    if farklar.size:
        med = float(np.median(farklar))
        mad = float(np.median(np.abs(farklar - med))) or 0.01
        esik = max(med + 4 * mad, 2 * med, 1.0)
        for i, f in enumerate(farklar):
            if f > esik:
                bayraklar.append({"zaman_sn": round((i + 1) / fps, 2), "fark": round(float(f), 2),
                                  "medyana_oran": round(float(f) / max(med, 0.01), 1),
                                  "tur": "ani değişim (kesme / ışınlanma / kaybolma–belirme adayı)"})
        dur = None
        for i, f in enumerate(farklar):
            if f < 0.15:
                dur = i if dur is None else dur
            else:
                if dur is not None and (i - dur) / fps >= 0.5:
                    donmalar.append([round(dur / fps, 2), round(i / fps, 2)])
                dur = None
        if dur is not None and (len(farklar) - dur) / fps >= 0.5:
            donmalar.append([round(dur / fps, 2), round(len(farklar) / fps, 2)])
        hareket = {"medyan_fark": round(med, 3), "esik": round(esik, 3), "en_yuksek_fark": round(float(farklar.max()), 2)}
    else:
        hareket = {}
    parlaklik = round(float(kareler.mean()), 1) if kareler.size else None
    tum = kontak_tablosu(yol, fps, klasor / "tum_kareler")
    supheli = []
    for b in bayraklar[:8]:
        bas = max(0.0, b["zaman_sn"] - 0.75)
        supheli += kontak_tablosu(yol, 12, klasor / f"supheli_{b['zaman_sn']:.2f}", bas=bas, sure=1.5, genislik=360, sutun=6)
    uyarilar = []
    if not teknik["dikey_9_16"]:
        uyarilar.append("9:16 değil")
    if not teknik["ses_kanali"]:
        uyarilar.append("ses kanalı yok")
    if parlaklik is not None and parlaklik < 45:
        uyarilar.append(f"karanlık sahne (ortalama parlaklık {parlaklik}/255): kilit anlar okunmayabilir")
    if bayraklar:
        uyarilar.append(f"{len(bayraklar)} ani değişim anı: görsel incelemede zorunlu bakılacak")
    if donmalar:
        uyarilar.append(f"{len(donmalar)} donma bölümü")
    rapor = {"video": str(yol), "ad": ad, "teknik": teknik, "ses": ses, "hareket": hareket,
             "ani_degisimler": bayraklar, "donmalar": donmalar, "ortalama_parlaklik": parlaklik,
             "otomatik_uyarilar": uyarilar, "kontak_tablolari": tum, "supheli_an_tablolari": supheli,
             "sinir": "Anlamsal hatalar (iç içe geçme, uzuv, menteşe, nesne çoğalması, komedi okunurluğu) VIU-2 görsel incelemesi gerektirir."}
    (klasor / "rapor.json").write_text(json.dumps(rapor, ensure_ascii=False, indent=2), encoding="utf-8")
    return rapor


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--cikti", required=True)
    p.add_argument("--fps", type=float, default=8)
    p.add_argument("--ad")
    a = p.parse_args()
    ad = a.ad or Path(a.video).stem
    r = analiz(Path(a.video), a.cikti, a.fps, ad)
    print(json.dumps({k: r[k] for k in ("ad", "teknik", "ses", "hareket", "ani_degisimler", "donmalar", "ortalama_parlaklik", "otomatik_uyarilar")}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    sys.exit(main())
