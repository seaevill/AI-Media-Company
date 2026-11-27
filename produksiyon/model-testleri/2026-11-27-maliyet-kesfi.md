# G-0007 — Higgsfield model ve maliyet keşfi (yalnızca okuma)

Tarih: 2026-11-27 · Araçlar: `balance`, `models_explore`, `estimate_video_cost`, `estimate_image_cost` (Higgsfield MCP). **Harcanan kredi: 0.** Hiçbir üretim işi başlatılmadı.
Bakiye: 1.935,39 kredi, plan Ultra (`balance`, 2026-11-27). Ücretsiz/"unlim" hakkı: `models_explore` yanıtında `unlim.available=false` (şu an kullanılabilir ücretsiz üretim hakkı görünmüyor). Manifestodaki "3 ücretsiz hareket kontrolü hakkı" bu araçla doğrulanamadı.

## Tahmini kredi — tek klip, 9:16 dikey
| Model | Ayar | Tahmini kredi | Saniye başına | Not (katalog açıklamasından) |
|---|---|---:|---:|---|
| Minimax Hailuo 2.3-fast | 6 sn, 768p | **4** | 0,67 | Doğal fizik, yüz ifadesi; en-boy seçeneği listede yok (kontrol gerekli) |
| Wan 2.6 | 5 sn, 720p | **7,5** | 1,5 | Stilize, deneysel |
| Seedance 2.0 Mini | 8 sn, 720p, ses açık | **8** | 1,0 | "Bütçe" sürüm, referans/kimlik desteği |
| Grok Video 1.5 Lite | 8 sn, 720p | **8** | 1,0 | Hızlı, metin/ilk kare |
| MAGI-2 | 8 sn, 1080p sabit, ses | **20** | 2,5 | Düşük maliyetli ses+görüntü, yavaş |
| Seedance 2.5 (taslak) | 8 sn, 480p taslak | **24** | 3,0 | Taslak 7 gün içinde sonlandırılabilir (sonlandırma ayrıca ücretli) |
| Seedance 2.5 Flash | 8 sn, 720p, ses | **40** | 5,0 | |
| Seedance 2.5 (varsayılan) | 8 sn, 720p, ses | **56** | 7,0 | Katalogda "varsayılan video modeli" |

Görsel (karakter referansı, kapak): GPT Image 2.6 1k düşük kalite **0,75**; Nano Banana 2 1k **1,5** (çizgi/karikatür karakter için önerilen).

## Çıkarımlar (hipotez — kalite henüz test edilmedi)
1. **Saniye başına en pahalı (7,0) ile en ucuz (0,67) arasında ~10,5 kat fark var** (Bekçi düzeltmesi: önceki '14 kat' farklı süreli klipleri kıyaslıyordu). 8 saniyelik klip varsayılan modelde 56 kredi, 8 sn bütçe modellerinde (Seedance 2.0 Mini, Grok Lite) 8 kredi = 7 kat. Kalite farkı, özellikle absürt/stilize formatlarda yeterli olabilir — **kanıtlanmadı**.
2. Kabaca bütçe: 1.935 kredi ≈ 34 adet varsayılan-model klibi **veya** ≈ 240 adet bütçe-model klibi (başarısız üretimler hariç). Başarısız oran bilinmiyor.
3. Bu nedenle ilk ücretli adım "deney" değil **benchmark** olmalı: aynı kısa sahne (tek karakter, tek mekân) 3 modelde, birer kez → ~4 + 8 + 56 = **~68 kredi**. Ölçüt: kullanılabilir saniye başına kredi + karakter tutarlılığı (`benchmark.csv`).
4. Karakter tutarlılığı için referans görsel (≈1–2 kredi) + referans destekli video modeli (Seedance 2.0 Mini) en ucuz yol görünüyor.
5. Ses: platform müziği ticari kullanımda risklidir (platform kuralları dosyası); modelin ürettiği ses ya da sözsüz format tercih edilmeli.

## Açık sorular
- Ultra planın aylık ücreti ve kredi yenilenme tarihi → kredi başına € (Bora).
- Tahminler gerçek faturayla aynı mı? İlk onaylı üretimde `tahmini_kredi` ↔ `gercek_kredi` karşılaştırılacak.
- Kling MCP fiyatları henüz okunmadı (bağlantı denenmedi).
