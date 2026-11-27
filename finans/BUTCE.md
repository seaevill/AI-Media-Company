# BÜTÇE

Kaynak: manifesto §23, §27. **Genel harcama yetkisi yok** (Bora, 2026-11-27). Sayısal sınırların tek kaynağı `vardiyalar/CONFIG.json > butce`.

## Bilinen durum (gözlem, 2026-11-27)
| Kalem | Değer | Kaynak | Not |
|---|---|---|---|
| Higgsfield planı | Ultra; aylık ~4.800 TL, 3.000 kredi (**Bora beyanı, kesin değil**) → ~1,6 TL/kredi | Higgsfield `balance` + Bora, 2026-11-27 (K-015) | Plan ücreti kesinleşince güncellenecek |
| Higgsfield kredi bakiyesi | 1.935,39 | aynı | Manifestodaki eski görüntüyle aynı; yenilenme tarihi bilinmiyor |
| Hareket kontrolü ücretsiz hakları | bilinmiyor (eski gözlem: 3) | — | Üretim öncesi yeniden kontrol |
| Claude aboneliği | bilinmiyor | — | ALONI ve diğer projelerle paylaşılıyor; yeni şirket onları engellememeli |
| Harcanan kredi | 0 | finans/kredi-kayitlari.csv | |

**Kredi ≠ para.** Kredinin parasal değeri = plan ücreti ÷ aylık kredi (ücretsiz haklar ve ek paket fiyatı ayrı). Yaklaşık değer (beyana dayalı): **~1,6 TL/kredi**; yani 8 kredilik bir klip ~13 TL, 56 kredilik bir klip ~90 TL, 80 kredilik benchmark ~128 TL. Kullanılmayan kredinin devredip devretmediği bilinmiyor.

## Önerilen dağılım (ÖNERİ — Bora onaylamadan harcama yetkisi değildir)
Eski reklam-stüdyosu dağılımı (%80 müşteri / %15 portföy / %5 influencer) artık geçerli değil. AI Media önceliğine göre öneri, mevcut 1.935 kredi için:

| Kova | Oran | ~Kredi | Ne için |
|---|---:|---:|---|
| Model/maliyet keşfi (benchmark) | %10 | ~190 | Aynı kısa sahne 2–3 ucuz modelde; kullanılabilir saniye başına kredi |
| EXP-0001 ana deney (bir karakter, 3–5 kısa video) | %35 | ~680 | %60 kovası: talebi gözlenmiş formatın özgün uyarlaması |
| Küçük konsept testleri (2 konsept × 2 video) | %20 | ~390 | %30 kovası |
| Radikal deney | %5 | ~100 | %10 kovası |
| Yedek (yeniden üretim, başarısız çıktı) | %30 | ~575 | Başarısız üretimler de kredi yer |

Her deney ayrıca A2 onayı ve **azami kredi** ister. Kova bütçesi otomatik yetki değildir.

## Kontroller
- Üretimden önce tahmin (`estimate_*_cost`), onaylı sınırla karşılaştırma; aşım = dur.
- Her üretim satırı `kredi-kayitlari.csv`'ye (başarısızlar dahil).
- Haftalık raporda: harcanan kredi, kullanılabilir saniye başına kredi, bin görüntülenme başına kredi (yayın sonrası).
