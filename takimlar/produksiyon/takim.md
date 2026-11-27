# Takım: produksiyon

**Görev:** Storyboard, prompt, model seçimi, kredi tahmini, onaylı üretim ve benchmark.

**Ajan:** `.claude/agents/produksiyon-maliyet.md`

**Koşu adımları:**

1. Ücretsiz hazırlık: senaryo → açılış hipotezi → storyboard → prompt.
2. Salt-okuma ile bakiye ve fiyat tahmini (`balance`, `estimate_*_cost`).
3. Onay alanında 'max N kredi' yoksa burada dur ve Bora için maliyet özetini yaz.
4. Onay varsa önce en ucuz yeterli model ile tek test; sonra gerekirse karşılaştırma.
5. Her üretim (başarısız dahil) kredi ve benchmark kaydına.

**Çıktı sonrası:** Bekçi denetimi; `defter.md`'ye tek ders.
