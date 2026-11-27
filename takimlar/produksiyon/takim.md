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

## Klip kalite kontrolü (2026-11-27, Bora'nın yakaladığı iç içe geçme hatasından sonra)
Bir klip için "çalıştı/kullanılabilir" demeden önce:
1. Tüm klip 2 kare/sn döşeme (genel akış).
2. Her temas, geçiş, kapı/nesne etkileşimi ve iki karakterin yaklaştığı an için ±1,5 sn **≥ 6 kare/sn, tam çözünürlük** (ffmpeg `-ss … -t 3 -vf fps=6`).
3. Kontrol listesi: iç içe geçme · kaybolma–yeniden belirme · uzuv sayısı/kopma · nesne çoğalması · istenmeyen yazı/rakam · ses kanalı var mı.
4. Bulgu varsa klip "hayır"; ses dinlenmediyse "ses dinlenmedi" yazılır. Son söz insan izlemesindir.
