#!/usr/bin/env python3
"""Toplu ölçüm (G-0053 planı, K-034 elle): istihbarat/olcumler/izleme_listesi.json'daki
hesapları scripts/hesap_olc.py ile ölçer, ham sonucu tek dosyaya yazar.
Kullanım: python3 -I scripts/olcum_toplu.py [--liste YOL] [--cikti-klasor YOL]
Kredi harcamaz; Claude ajanı gerektirmez. Engel/CAPTCHA aşılmaz (hesap_olc.py)."""
import argparse, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent

def olc(platform, hesaplar):
    if not hesaplar:
        return []
    r = subprocess.run([sys.executable, "-I", str(KOK / "scripts/hesap_olc.py"), platform, *hesaplar],
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return [{"hata": (r.stdout + r.stderr)[:500]}]

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--liste", default=str(KOK / "istihbarat/olcumler/izleme_listesi.json"))
    p.add_argument("--cikti-klasor", default=str(KOK / "istihbarat/olcumler"))
    a = p.parse_args(argv)
    liste = json.loads(Path(a.liste).read_text(encoding="utf-8"))
    bas = datetime.now(timezone.utc)
    sonuc = {"olcum_basla_utc": bas.isoformat(timespec="seconds"), "liste": a.liste,
             "youtube": olc("youtube", liste.get("youtube", [])),
             "tiktok": olc("tiktok", liste.get("tiktok", []))}
    sonuc["olcum_bitis_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    hedef = Path(a.cikti_klasor) / (bas.strftime("%Y-%m-%dT%H%MZ") + ".json")
    hedef.write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
    hata = sum(1 for p_ in ("youtube", "tiktok") for x in sonuc[p_] if "hata" in x or "engel" in x)
    print(json.dumps({"dosya": str(hedef), "youtube": len(sonuc["youtube"]), "tiktok": len(sonuc["tiktok"]), "engel_veya_hata": hata}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
