"""duyarlilik_analizi.py testleri (ağsız, sentetik veri). Çalıştır: python3 -m pytest tests/test_duyarlilik.py"""
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent
sys.path.insert(0, str(KOK.parent / "scripts"))
import duyarlilik_analizi as da  # noqa: E402


def test_saglikli_sinir_degerleri_dahil():
    assert da.saglikli(0.1, 10, 0.1, 10)
    assert not da.saglikli(0.0999, 10, 0.1, 10)
    assert not da.saglikli(0.1, 10.1, 0.1, 10)
    assert not da.saglikli(None, 5, 0.1, 10)


def test_spearman_tam_ters_ve_tam_ayni():
    assert da.spearman([1, 2, 3, 4], [10, 20, 30, 40]) == 1.0
    assert da.spearman([1, 2, 3, 4], [40, 30, 20, 10]) == -1.0
    assert da.spearman([1, 2], [1, 2]) is None  # n<3


def test_siralar_baglarda_ortalama():
    assert da.siralar([5, 5, 1]) == [2.5, 2.5, 1.0]


def _tt(ad, tak, izl, sab=()):
    # id üst 32 bit = unix saniyesi; 2026-11-01 ~ 1793491200
    base = 1793491200
    klipler = [{"id": str((base + i * 86400) << 32), "tarih": f"2026-11-{i + 1:02d}", "izlenme": v} for i, v in enumerate(izl)]
    return {"hesap": ad, "olcum_utc": "2026-11-27T22:00:00+00:00", "takipci_tam": tak, "embed_klipler": klipler,
            "sabitlenmis_tahmin": [klipler[i]["id"] for i in sab], "video_n": len(izl) - len(sab),
            "medyan_izlenme_takipci_orani": 0.5, "en_yuksek_medyana_orani": 2.0}


def test_satirlar_tt_dahil_surum_sabitlenmis_katar():
    veri = {"youtube": [], "tiktok": [_tt("@a", 100000, [10_000_000] + [100] * 9, sab=(0,))]}
    (r,) = da.satirlar(veri)
    assert r["platform"] == "TT" and r["n"] == 9
    assert r["yuksek_dahil"] == 100000.0  # 10M / medyan(100)
    assert r["gun"] is not None and r["son_klip"] == "2026-11-10"


def test_izgara_esik_degisince_sayi_degisir():
    yt = [{"hesap": "@x", "olcum_utc": "2026-11-27T22:00:00+00:00", "shorts_n": 10, "abone_yaklasik": 5000,
           "medyan_izlenme_abone_orani": 0.07, "en_yuksek_medyana_orani": 8.0}]
    g = da.izgara(da.satirlar({"youtube": yt, "tiktok": []}))
    d = g[("YT", "haric")]
    assert d[(0.1, 10)] == [] and d[(0.05, 10)] == ["@x"] and d[(0.05, 5)] == []


def test_uygun_filtre():
    assert not da.uygun({"n": 7, "takipci": 5000})
    assert not da.uygun({"n": 10, "takipci": 999})
    assert da.uygun({"n": 8, "takipci": 1000})


def test_g0048_filtresi():
    rows = [{"platform": "YT", "hesap": "@BandarApnaDost"}, {"platform": "YT", "hesap": "@simonscat"},
            {"platform": "TT", "hesap": "@simonscat"}, {"platform": "TT", "hesap": "@mpminds"}]
    assert [r["hesap"] for r in da.g0048(rows)] == ["@BandarApnaDost", "@mpminds"]
