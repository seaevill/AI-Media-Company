"""tahmin_karsilastir testleri. Çalıştır: python3 -m pytest tests/test_tahmin_karsilastir.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tahmin_karsilastir as tk  # noqa: E402

def tahmin(hesap, platform, n48, a48, n14, a14, yon, k48=0.0, k14=0.0):
    return {"platform": platform, "hesap": hesap,
            "t0": {"alan_takipci": "takipci_tam" if platform == "tiktok" else "abone_yaklasik",
                   "alan_medyan": "video_izlenme_medyan" if platform == "tiktok" else "shorts_izlenme_medyan"},
            "tahmin": {"takipci_48s": {"nokta_pct": n48, "aralik80_pct": a48},
                       "takipci_14g": {"nokta_pct": n14, "aralik80_pct": a14}, "medyan_14g_yon": yon},
            "saf_kiyas": {"degisim_yok": {"takipci_48s_pct": 0.0, "takipci_14g_pct": 0.0, "medyan_14g_yon": "aynı"},
                          "klip_sikligi_kurali": {"takipci_48s_pct": k48, "takipci_14g_pct": k14, "medyan_14g_yon": "aynı"}}}

def olcum(tt, yt):
    return {"tiktok": [{"hesap": "@" + h, "takipci_tam": f, "video_izlenme_medyan": m} for h, f, m in tt],
            "youtube": [{"hesap": h, "abone_yaklasik": f, "shorts_izlenme_medyan": m} for h, f, m in yt]}

T0 = olcum([("a", 1000, 100), ("b", 2000, 100)], [("@y", 100000, 1000)])
TAHMIN = {"tahminler": [
    tahmin("@a", "tiktok", 1.0, [0.0, 2.0], 5.0, [2.0, 8.0], "artar", 0.2, 1.0),
    tahmin("@b", "tiktok", 0.0, [-1.0, 1.0], 0.0, [-1.0, 1.0], "aynı"),
    tahmin("@y", "youtube", 0.0, [-0.5, 0.5], 1.0, [0.0, 2.0], "azalır"),
    {"platform": "tiktok", "hesap": "@yok", "t0": {}, "tahmin": None, "atlandi": "okunamadı"}]}

def test_48s_hata_ve_aralik():
    s = olcum([("a", 1010, 100), ("b", 2000, 100)], [("@y", 100000, 1000)])
    r = tk.karsilastir(TAHMIN, T0, s, "48s")
    a = next(x for x in r["satirlar"] if x["hesap"] == "@a")
    assert a["gercek_pct"] == 1.0 and a["hata"] == 0.0 and a["aralik_isabet"] is True
    assert r["ozet"]["n"] == 3
    assert r["ozet"]["mae_bizim"] == 0.0
    assert abs(r["ozet"]["mae_degisim_yok"] - (1.0 / 3)) < 1e-9
    assert r["ozet"]["bizim_iki_kiyasi_de_yeniyor"] is True  # 0 < 0.333 ve 0 < 0.267
    assert abs(r["ozet"]["mae_klip_sikligi_kurali"] - 0.8 / 3) < 1e-9

def test_aralik_kacirma():
    s = olcum([("a", 1100, 100), ("b", 2000, 100)], [("@y", 100000, 1000)])  # a: +10%
    r = tk.karsilastir(TAHMIN, T0, s, "48s")
    a = next(x for x in r["satirlar"] if x["hesap"] == "@a")
    assert a["aralik_isabet"] is False and a["hata"] == -9.0

def test_14g_yon():
    s = olcum([("a", 1050, 130), ("b", 2000, 110)], [("@y", 101000, 700)])
    r = tk.karsilastir(TAHMIN, T0, s, "14g")
    d = {x["hesap"]: x for x in r["satirlar"]}
    assert d["@a"]["gercek_yon"] == "artar" and d["@a"]["yon_isabet"] is True
    assert d["@b"]["gercek_yon"] == "aynı" and d["@b"]["yon_isabet"] is True
    assert d["@y"]["gercek_yon"] == "azalır" and d["@y"]["yon_isabet"] is True
    assert r["ozet"]["yon_isabet_bizim"] == 1.0
    assert abs(r["ozet"]["yon_isabet_degisim_yok"] - 1 / 3) < 1e-9

def test_eksik_hesap_atlanir():
    s = olcum([("a", 1010, 100)], [("@y", 100000, 1000)])
    r = tk.karsilastir(TAHMIN, T0, s, "48s")
    assert r["ozet"]["n"] == 2 and r["ozet"]["atlanan"][0]["hesap"] == "@b"

def test_gecersiz_ufuk():
    try:
        tk.karsilastir(TAHMIN, T0, T0, "7g")
    except ValueError:
        return
    assert False

def test_cli_yazar(tmp_path):
    for ad, v in (("t.json", TAHMIN), ("t0.json", T0), ("s.json", T0)):
        (tmp_path / ad).write_text(json.dumps(v), encoding="utf-8")
    c = tmp_path / "c.json"
    assert tk.main(["--tahmin", str(tmp_path / "t.json"), "--t0", str(tmp_path / "t0.json"),
                    "--sonraki", str(tmp_path / "s.json"), "--ufuk", "14g", "--cikti", str(c)]) == 0
    assert json.loads(c.read_text())["ozet"]["n"] == 3

def test_gercek_tahmin_dosyasi_ve_t0_kendiyle_sifir_degisim():
    kok = Path(__file__).resolve().parent.parent / "istihbarat/olcumler"
    t = json.loads((kok / "tahminler_2026-11-28.json").read_text(encoding="utf-8"))
    t0 = json.loads((kok / "2026-11-28T1104Z.json").read_text(encoding="utf-8"))
    r = tk.karsilastir(t, t0, t0, "48s")
    assert r["ozet"]["n"] == 39
    assert r["ozet"]["mae_degisim_yok"] == 0.0
