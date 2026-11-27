"""gemini_video.py testleri — ağ YOK (istek kurma, önbellek anahtarı, kayıt). Çalıştır: python3 -m pytest tests/"""
import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import gemini_video as gv  # noqa: E402

ON_IKI = ["kanca", "kesmeler", "sure", "ses", "karakterler", "mizah", "surpriz", "paylasim_hipotezi",
          "yorum_hipotezi", "uretim_tahmini", "prensipler", "bizim_icin_fikirler"]


@pytest.fixture(autouse=True)
def ag_yok(monkeypatch):
    def yasak(*a, **k):
        raise AssertionError("testte ağ çağrısı yapıldı")
    monkeypatch.setattr(gv.urllib.request, "urlopen", yasak)


@pytest.mark.parametrize("url", ["https://www.youtube.com/shorts/dQw4w9WgXcQ", "https://youtu.be/dQw4w9WgXcQ?si=x",
                                 "https://www.youtube.com/watch?feature=share&v=dQw4w9WgXcQ"])
def test_youtube_anahtari(url):
    assert gv.onbellek_anahtari(url) == "youtube:dQw4w9WgXcQ"


def test_dosya_anahtari_sha256(tmp_path):
    f = tmp_path / "a.mp4"
    f.write_bytes(b"\x00sahte video")
    assert gv.onbellek_anahtari(str(f)) == "sha256:" + hashlib.sha256(b"\x00sahte video").hexdigest()
    assert gv.dosya_adi("youtube:abc") == "youtube_abc.json"


def test_sema_12_alan():
    assert gv.SEMA["type"] == "OBJECT" and list(gv.SEMA["properties"]) == ON_IKI
    assert gv.SEMA["required"] == ON_IKI


def test_istek_govdesi_youtube_ve_dosya():
    g = gv.istek_govdesi("https://www.youtube.com/shorts/dQw4w9WgXcQ")
    parca = g["contents"][0]["parts"]
    assert parca[0] == {"file_data": {"file_uri": "https://www.youtube.com/shorts/dQw4w9WgXcQ"}}
    assert g["generationConfig"]["responseMimeType"] == "application/json"
    assert g["generationConfig"]["responseSchema"] is gv.SEMA
    g2 = gv.istek_govdesi("https://generativelanguage.googleapis.com/v1beta/files/x", "video/mp4")
    assert g2["contents"][0]["parts"][0]["file_data"]["mime_type"] == "video/mp4"


def test_anahtar_basligi(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    assert gv.anahtar_basligi() == {"x-goog-api-key": "proxy-injected"}
    monkeypatch.setenv("GEMINI_API_KEY", "test-degeri")
    assert gv.anahtar_basligi() == {"x-goog-api-key": "test-degeri"}


def test_dry_run_anahtari_yazmaz(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(gv, "VIU", tmp_path)
    monkeypatch.setattr(gv.onbellekte_mi, "__defaults__", (tmp_path,))
    monkeypatch.setenv("GEMINI_API_KEY", "GIZLI-DEGER-123")
    assert gv.main(["https://youtu.be/dQw4w9WgXcQ", "--dry-run", "--model", "gemini-x"]) == 0
    cikti = capsys.readouterr().out
    assert "GIZLI-DEGER-123" not in cikti
    assert "models/gemini-x:generateContent" in cikti and "youtube:dQw4w9WgXcQ" in cikti
    assert not (tmp_path / "analiz-kaydi.json").exists()


def test_kayit_ve_tekrar_yok(tmp_path):
    (tmp_path / "analiz-kaydi.json").write_text(json.dumps({"_aciklama": "x", "analizler": []}))
    assert not gv.onbellekte_mi("youtube:abc", tmp_path)
    gv.kaydet("youtube:abc", "https://youtu.be/abc", "m", {"kanca": {}}, tmp_path)
    assert gv.onbellekte_mi("youtube:abc", tmp_path)
    k = json.loads((tmp_path / "analiz-kaydi.json").read_text())
    assert k["_aciklama"] == "x" and [r["anahtar"] for r in k["analizler"]] == ["youtube:abc"]
    d = json.loads((tmp_path / "analizler" / "youtube_abc.json").read_text())
    assert d["analiz"]["onbellek_anahtari"] == "youtube:abc" and d["kanca"] == {}
    with pytest.raises(RuntimeError):
        gv.kaydet("youtube:abc", "https://youtu.be/abc", "m", {}, tmp_path)


def test_onbellekte_ise_api_cagrilmaz(monkeypatch, tmp_path, capsys):
    (tmp_path / "analiz-kaydi.json").write_text(json.dumps({"analizler": [{"anahtar": "youtube:dQw4w9WgXcQ"}]}))
    monkeypatch.setattr(gv.onbellekte_mi, "__defaults__", (tmp_path,))
    assert gv.main(["https://youtu.be/dQw4w9WgXcQ"]) == 0  # urlopen çağrılsaydı ag_yok patlardı
    assert "önbellekte" in capsys.readouterr().out


def test_hata_mesajlari():
    assert "anahtar başlığı yanlış ya da anahtar yok" in gv.hata(403, b'{"error":{"message":"denied"}}')
    assert "anahtar geçersiz" in gv.hata(400, b'{"error":{"message":"API key not valid","status":"INVALID_ARGUMENT",'
                                              b'"details":[{"reason":"API_KEY_INVALID"}]}}')
    assert gv.hata(500, b"bozuk") == "HTTP 500: bozuk"
