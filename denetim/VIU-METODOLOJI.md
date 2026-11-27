# VIU — Video analiz metodolojisi (K-028 Görev 2)

VIU iki iş yapar: **(1) kendi üretimimizin kalite denetimi** (`denetim/VIU-PROTOKOLU.md`, yayın kapısı) ve **(2) pazardaki başarılı/başarısız videoların istihbaratı** (bu dosya). İkisi aynı ham analizi paylaşır; bir video **bir kez** analiz edilir, sonuç `denetim/viu/analiz-kaydi.json`'a yazılır ve konseyler bu kaydı okur (yeniden analiz yok — K-028 Görev 4).

## Temel kural: gözlem ≠ çıkarım
Her alan üç etiketten birini taşır:
- **GÖZLEM** — videoda doğrudan görülen/duyulan, zaman damgalı (ör. "0:01.2 kedi takım elbiseyle masaya oturur").
- **ÖLÇÜM** — araçla ölçülen (süre, kesme sayısı, ses düzeyi, kare farkı, ffprobe).
- **ÇIKARIM** — yapay zekânın yorumu (ör. "paylaşılma motivasyonu: tanınabilir iş hayatı acısı"); her çıkarım bir güven derecesi ve dayandığı gözlem(ler)le yazılır.
Platformun herkese açık sayıları (izlenme, beğeni) kaynak + tarih ile **ÖLÇÜM (kamuya açık)** olarak yazılır. Retention, paylaşım oranı, gelir gibi özel veriler **yazılmaz**; "bilinmiyor".

## 12 görev → analiz şeması alanları
| # | Görev | Alan(lar) | Tür |
|---|---|---|---|
| 1 | İlk 0–2 sn dikkat mekanizması | `kanca`: {ilk_kare_aciklama, ilk_2sn_olay, mekanizma: merak / şok / tanıdıklık / absürt görüntü / soru / ses, metin_var_mi} | GÖZLEM + ÇIKARIM |
| 2 | Sahne geçişleri | `kesmeler`: [{t, tur: kesme/geçiş/zoom}], kesme_sayisi, ort_cekim_suresi | ÖLÇÜM (video_qc + model) |
| 3 | Süre | `sure_sn`, `bolumler`: kurulum / gelişme / sürpriz / tepki zaman aralıkları | ÖLÇÜM + GÖZLEM |
| 4 | Konuşma ve ses efektleri | `ses`: {konusma_var_mi, dil, transkript_ozeti, ses_efektleri:[{t, ne}], muzik: var/yok/telifli olabilir} | GÖZLEM |
| 5 | Karakter davranışı | `karakterler`: [{ad/tanım, imza_davranis, ifade_anlari:[t]}] | GÖZLEM |
| 6 | Görsel mizah ve absürtlük | `mizah`: {tur: beklenti kırılması / tekrar–kırılma / tepki / high-low kontrast / anti-mizah …, an: t} | GÖZLEM + ÇIKARIM |
| 7 | Beklenmedik sonuç | `surpriz`: {t, ne, kurulumla_baglanti} | GÖZLEM |
| 8 | Paylaşılma motivasyonu | `paylasim_hipotezi`: [{motivasyon, dayanak_gozlem, guven}] | ÇIKARIM |
| 9 | Yorum/tartışma potansiyeli | `yorum_hipotezi` + (varsa) kamuya açık ilk 20 yorumun tema özeti (kaynak + tarih) | ÇIKARIM + ÖLÇÜM (kamuya açık) |
| 10 | Üretim yöntemi ve maliyet | `uretim_tahmini`: {AI mi/gerçek mi/karışık, olası araç, çekim sayısı, tahmini kredi aralığı} | ÇIKARIM (her zaman "tahmin") |
| 11 | Çalışma prensipleri | `prensipler`: [kısa kural cümleleri] | ÇIKARIM |
| 12 | Özgün fikirlere dönüştürme | `bizim_icin_fikirler`: [prensip → özgün fikir; kopyalanan öğe YOK] | ÇIKARIM (kreatife girdi) |
Ek: `kaynak`: {url/dosya, platform, hesap, yayın_tarihi, kamuya_acik_sayilar + tarih}, `analiz`: {arac, model, tarih, maliyet, fps, onbellek_anahtari}.

## Çalışma akışı
1. **Önbellek kontrolü:** anahtar = platform + video kimliği (URL'den) ya da yerel dosyada SHA-256. `analiz-kaydi.json`'da varsa yeniden analiz edilmez.
2. **VIU-1 (yerel, ücretsiz):** `scripts/video_qc.py` (yerel MP4 varsa) → ölçümler.
3. **VIU-otomatik (Gemini, onay sonrası):** aynı şema `responseSchema` olarak verilir; tek çağrıda 12 alan. Düşük fps (≈1 kare/sn) genel akış, kilit anlar için kırpılmış aralıkta yüksek fps (araç incelemesi G-0033 sonucuna göre).
4. **VIU-2 (Claude ajanı, görsel):** yalnız kendi üretimimiz için zorunlu; pazar videolarında örneklem kontrolü (Gemini'nin zaman damgalarından 3'ü kare çıkarılıp doğrulanır).
5. **Kayıt:** `denetim/viu/analizler/<anahtar>.json` + `analiz-kaydi.json` satırı. Konsey/kreatif bu dosyayı okur.

## Hukuk ve platform
- YouTube: resmî Gemini API YouTube URL'sini doğrudan kabul ediyor (doğrulanacak, G-0033). **yt-dlp ile indirme yok** (YouTube hizmet şartları).
- TikTok/Instagram: indirme yok; yalnızca kamuya açık sayfa metni/meta veri ve Bora'nın kendi hesabından elle kaydettiği dosyalar (kişisel analiz amaçlı; yeniden yayın yok).
- Analiz edilen hiçbir videodan karakter, sahne, ses veya senaryo kopyalanmaz; yalnızca prensip çıkarılır (Anayasa 13).
