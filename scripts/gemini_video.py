#!/usr/bin/env python3
"""VIU-otomatik: kamuya açık YouTube URL'si ya da yerel MP4'ü resmî Gemini API ile analiz eder.

Kullanım:
  python3 -I scripts/gemini_video.py <youtube-url | dosya.mp4> [--model M] [--dry-run]
  python3 -I scripts/gemini_video.py --anahtar-testi      # GET /v1beta/models, yalnız HTTP kodu

Şema: denetim/VIU-METODOLOJI.md'deki 12 görev alanı (responseSchema, JSON modu).
Önbellek: anahtar youtube:<video_id> ya da sha256:<dosya özeti>; sonuç
denetim/viu/analizler/<anahtar>.json + denetim/viu/analiz-kaydi.json satırı. Kayıtlı anahtar
YENİDEN ANALİZ EDİLMEZ. Kimlik: x-goog-api-key başlığı = $GEMINI_API_KEY ya da "proxy-injected"
(ortam vekili gerçek anahtarı ekler). Anahtar hiçbir dosyaya/çıktıya yazılmaz.
YouTube indirilmez (yt-dlp yok); URL doğrudan file_data.file_uri olarak verilir.
"""
import argparse, hashlib, json, os, re, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://generativelanguage.googleapis.com"
KOK = Path(__file__).resolve().parent.parent
VIU = KOK / "denetim" / "viu"
VARSAYILAN_MODEL = "gemini-3.5-flash"  # 2026-11-28: 2.5 yeni kullanıcıya kapalı (404); 3.8-flash 503 verdi

S, N, I, B = ({"type": t} for t in ("STRING", "NUMBER", "INTEGER", "BOOLEAN"))
def nesne(**p): return {"type": "OBJECT", "properties": p, "required": list(p)}
def liste(x): return {"type": "ARRAY", "items": x}
CIKARIM = nesne(motivasyon=S, dayanak_gozlem=S, guven={"type": "STRING", "enum": ["düşük", "orta", "yüksek"]})
SEMA = nesne(  # 12 görev = 12 üst alan (VIU-METODOLOJI tablosu sırasıyla)
    kanca=nesne(ilk_kare_aciklama=S, ilk_2sn_olay=S, metin_var_mi=B, mekanizma={"type": "STRING", "enum": [
        "merak", "şok", "tanıdıklık", "absürt görüntü", "soru", "ses"]}),
    kesmeler=nesne(liste=liste(nesne(t=N, tur={"type": "STRING", "enum": ["kesme", "geçiş", "zoom"]})),
                   kesme_sayisi=I, ort_cekim_suresi_sn=N),
    sure=nesne(sure_sn=N, bolumler=nesne(kurulum=S, gelisme=S, surpriz=S, tepki=S)),
    ses=nesne(konusma_var_mi=B, dil=S, transkript_ozeti=S, ses_efektleri=liste(nesne(t=N, ne=S)),
              muzik={"type": "STRING", "enum": ["var", "yok", "telifli olabilir"]}),
    karakterler=liste(nesne(tanim=S, imza_davranis=S, ifade_anlari=liste(N))),
    mizah=nesne(tur=S, an=N),
    surpriz=nesne(t=N, ne=S, kurulumla_baglanti=S),
    paylasim_hipotezi=liste(CIKARIM),
    yorum_hipotezi=S,
    uretim_tahmini=nesne(tur={"type": "STRING", "enum": ["AI", "gerçek", "karışık"]}, olasi_arac=S,
                         cekim_sayisi=I, tahmini_kredi_araligi=S),
    prensipler=liste(S),
    bizim_icin_fikirler=liste(nesne(prensip=S, ozgun_fikir=S)),
)
ISTEM = ("Bu kısa videoyu şemaya göre Türkçe analiz et. Zamanları saniye (t) olarak ver. GÖZLEM alanlarına "
         "yalnızca videoda görülen/duyulanı yaz; çıkarımlarda (paylasim_hipotezi, yorum_hipotezi, uretim_tahmini, "
         "prensipler, bizim_icin_fikirler) dayandığın gözlemi belirt. uretim_tahmini her zaman tahmindir. "
         "bizim_icin_fikirler videodan karakter, sahne, ses veya senaryo KOPYALAMAZ; yalnız prensipten özgün fikir.")


def youtube_kimligi(url):
    m = re.search(r"(?:youtube\.com/(?:watch\?(?:.*&)?v=|shorts/|embed/|live/)|youtu\.be/)([\w-]{11})", url)
    return m.group(1) if m else None


def onbellek_anahtari(kaynak):
    vid = youtube_kimligi(kaynak)
    if vid:
        return f"youtube:{vid}"
    h = hashlib.sha256()
    with open(kaynak, "rb") as f:
        for parca in iter(lambda: f.read(1 << 20), b""):
            h.update(parca)
    return f"sha256:{h.hexdigest()}"


def dosya_adi(anahtar): return anahtar.replace(":", "_") + ".json"


def kayit_oku(viu=VIU):
    p = viu / "analiz-kaydi.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"analizler": []}


def onbellekte_mi(anahtar, viu=VIU):
    return (viu / "analizler" / dosya_adi(anahtar)).exists() or any(
        r.get("anahtar") == anahtar for r in kayit_oku(viu).get("analizler", []))


def kaydet(anahtar, kaynak, model, sonuc, viu=VIU):
    if onbellekte_mi(anahtar, viu):
        raise RuntimeError(f"{anahtar} zaten önbellekte; üzerine yazılmaz")
    tarih = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (viu / "analizler").mkdir(parents=True, exist_ok=True)
    kayit = {"kaynak": {"url_veya_dosya": kaynak}, "analiz": {"arac": "gemini_video.py", "model": model, "tarih": tarih,
             "onbellek_anahtari": anahtar}, **sonuc}
    (viu / "analizler" / dosya_adi(anahtar)).write_text(json.dumps(kayit, ensure_ascii=False, indent=1), encoding="utf-8")
    k = kayit_oku(viu)
    k.setdefault("analizler", []).append({"anahtar": anahtar, "kaynak": kaynak, "model": model, "tarih": tarih,
                                          "dosya": f"denetim/viu/analizler/{dosya_adi(anahtar)}"})
    (viu / "analiz-kaydi.json").write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def anahtar_basligi(): return {"x-goog-api-key": os.environ.get("GEMINI_API_KEY") or "proxy-injected"}


def istek_govdesi(file_uri, mime=None):
    fd = {"file_uri": file_uri, **({"mime_type": mime} if mime else {})}
    return {"contents": [{"role": "user", "parts": [{"file_data": fd}, {"text": ISTEM}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": SEMA}}


def istek(url, veri=None, basliklar=None, yontem=None):
    """Döner: (HTTP kodu, yanıt başlıkları, gövde baytları). Hata kodu da döner, istisna atmaz."""
    if isinstance(veri, (dict, list)):
        veri = json.dumps(veri).encode()
        basliklar = {"Content-Type": "application/json", **(basliklar or {})}
    r = urllib.request.Request(url, data=veri, method=yontem, headers={**anahtar_basligi(), **(basliklar or {})})
    try:
        with urllib.request.urlopen(r, timeout=300) as y:
            return y.status, dict(y.headers), y.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def hata(kod, govde):
    if kod == 403:
        return "HTTP 403: anahtar başlığı yanlış ya da anahtar yok (vekil x-goog-api-key eklemiyor olabilir)"
    try:
        mesaj = json.loads(govde)["error"]["message"]
    except (ValueError, KeyError, TypeError):
        mesaj = govde[:200].decode("utf-8", "replace")
    if kod == 400 and b"API_KEY_INVALID" in govde:
        return f"HTTP 400: anahtar geçersiz — vekil yer tutucuyu gerçek anahtarla değiştirmiyor olabilir ({mesaj})"
    return f"HTTP {kod}: {mesaj}"


def yukle(yol):
    boy = os.path.getsize(yol)
    kod, bas, g = istek(f"{API}/upload/v1beta/files", {"file": {"display_name": Path(yol).name}}, {
        "X-Goog-Upload-Protocol": "resumable", "X-Goog-Upload-Command": "start",
        "X-Goog-Upload-Header-Content-Length": str(boy), "X-Goog-Upload-Header-Content-Type": "video/mp4"})
    yurl = {k.lower(): v for k, v in bas.items()}.get("x-goog-upload-url") or {k.lower(): v for k, v in bas.items()}.get("x-goog-upload-control-url")
    if kod != 200 or not yurl:
        sys.exit(hata(kod, g))
    kod, _, g = istek(yurl, Path(yol).read_bytes(), {"X-Goog-Upload-Offset": "0", "X-Goog-Upload-Command": "upload, finalize"})
    if kod != 200:
        sys.exit(hata(kod, g))
    dosya = json.loads(g)["file"]
    for _ in range(60):  # video işlenene kadar bekle (ACTIVE)
        if dosya.get("state") == "ACTIVE":
            return dosya["uri"]
        if dosya.get("state") == "FAILED":
            sys.exit("Files API: video işlenemedi (FAILED)")
        time.sleep(5)
        kod, _, g = istek(f"{API}/v1beta/{dosya['name']}")
        dosya = json.loads(g) if kod == 200 else dosya
    sys.exit("Files API: 5 dakikada ACTIVE olmadı")


def main(argv=None):
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("kaynak", nargs="?")
    a.add_argument("--model", default=VARSAYILAN_MODEL)
    a.add_argument("--dry-run", action="store_true", help="isteği yazdır, gönderme")
    a.add_argument("--anahtar-testi", action="store_true", help="GET /v1beta/models; HTTP kodunu yazdır")
    o = a.parse_args(argv)
    if o.anahtar_testi:
        kod, _, g = istek(f"{API}/v1beta/models")
        print(f"GET {API}/v1beta/models -> HTTP {kod}" + ("" if kod == 200 else " | " + hata(kod, g)))
        return 0 if kod == 200 else 3
    if not o.kaynak:
        a.error("kaynak gerekli")
    yerel = not youtube_kimligi(o.kaynak)
    if yerel and not Path(o.kaynak).is_file():
        a.error("YouTube URL'si değil ve dosya bulunamadı")
    anahtar = onbellek_anahtari(o.kaynak)
    if onbellekte_mi(anahtar):
        print(f"önbellekte: {anahtar} -> denetim/viu/analizler/{dosya_adi(anahtar)} (yeniden analiz yok)")
        return 0
    url = f"{API}/v1beta/models/{o.model}:generateContent"
    if o.dry_run:
        uri = "<Files API yüklemesinden sonra>" if yerel else o.kaynak
        print(json.dumps({"POST": url, "basliklar": {"x-goog-api-key": "*** (gizli)"}, "onbellek_anahtari": anahtar,
                          "govde": istek_govdesi(uri, "video/mp4" if yerel else None)}, ensure_ascii=False, indent=1))
        return 0
    uri = yukle(o.kaynak) if yerel else o.kaynak
    kod, _, g = istek(url, istek_govdesi(uri, "video/mp4" if yerel else None))
    if kod != 200:
        print(hata(kod, g), file=sys.stderr)
        return 3
    yanit = json.loads(g)
    sonuc = json.loads(yanit["candidates"][0]["content"]["parts"][0]["text"])
    sonuc["_kullanim"] = yanit.get("usageMetadata")
    kaydet(anahtar, o.kaynak, o.model, sonuc)
    print(f"kaydedildi: denetim/viu/analizler/{dosya_adi(anahtar)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
