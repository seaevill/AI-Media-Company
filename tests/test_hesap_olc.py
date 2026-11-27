"""hesap_olc.py TikTok ayrıştırma testleri (ağsız, kaydedilmiş HTML). Çalıştır: python3 -m pytest tests/"""
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent
sys.path.insert(0, str(KOK.parent / "scripts"))
import hesap_olc as ho  # noqa: E402

FIX = KOK / "fixtures"


def oku(ad):
    return (FIX / ad).read_text(encoding="utf-8")


def test_profil_var():
    s = ho.tiktok_profil_ayikla(oku("tiktok_profil_meowtakeover.html"))
    assert s["statusCode"] == 0 and s["durum"] == "hesap var"
    assert s["takipci"] == 2600000 and s["begeni_toplam"] == 169800000 and s["video_sayisi"] == 406
    assert s["takipci_tam"] == 2628454
    assert "engel" not in s


def test_profil_yok():
    s = ho.tiktok_profil_ayikla(oku("tiktok_profil_unit3c.html"))
    assert s["statusCode"] == 10221 and s["durum"] == "hesap bulunamadı"
    assert "takipci" not in s


def test_profil_sayisiz_sayfa_engel():
    s = ho.tiktok_profil_ayikla('<html>{"statusCode":0}</html>')
    assert "engel" in s


def test_embed_izlenmeler_ve_sabitlenmis():
    s = ho.tiktok_embed_ayikla(oku("tiktok_embed_meowtakeover.html"), "meowtakeover")
    assert len(s["embed_klipler"]) == 13
    assert len(s["sabitlenmis_tahmin"]) == 3  # baştaki 3 eski klip
    assert s["video_n"] == 10
    iz = s["video_izlenmeler"]
    assert s["video_en_dusuk"] == min(iz) == 32000
    assert s["video_en_yuksek"] == max(iz) == 2700000
    assert s["video_izlenme_medyan"] == 1069200  # (938400 + 1200000) / 2
    assert s["en_yuksek_medyana_orani"] == 2.5
    assert s["son_klip_tarih_araligi"] == ["2026-11-14", "2026-11-27"]


def test_embed_hesap_yok():
    s = ho.tiktok_embed_ayikla(oku("tiktok_embed_unit3c.html"), "unit3c")
    assert s == {"embed_hata_kodu": 10221}


def test_embed_veri_yoksa_engel():
    s = ho.tiktok_embed_ayikla(oku("tiktok_embed_v2_kabuk.html"), "meowtakeover")
    assert "engel" in s


def test_video_tarihi():
    assert ho.video_tarihi("7656580362805513490") == "2026-06-28"
    assert ho.video_tarihi("bozuk") is None


def test_sabitleme_yoksa_hepsi_sayilir():
    html = ('<script id="__FRONTITY_CONNECT_STATE__">{"source":{"data":{"/embed/@x":{"isError":false,'
            '"videoList":[{"id":"300","playCount":5},{"id":"200","playCount":1},{"id":"100","playCount":3}]}}}}</script>')
    s = ho.tiktok_embed_ayikla(html, "x")
    assert s["sabitlenmis_tahmin"] == [] and s["video_n"] == 3 and s["video_izlenme_medyan"] == 3
