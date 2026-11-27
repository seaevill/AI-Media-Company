# Video analiz araçları: 4 açık kaynak MCP + resmî Gemini API (G-0033, K-028)

- **Tarih:** 2026-11-27 · **Hazırlayan:** teknik araştırmacı (A0) · **Durum:** araştırma, karar değil
- **Yöntem:** 4 repo `git clone` ile scratch klasörüne indirildi ve **yalnızca okundu** (`cat`, `grep`). Hiçbir kod, kurulum, build ya da test çalıştırılmadı. Kod repoya kopyalanmadı.
- **Sınır:** github.com web/API bu ortamda 403 verdiği için yıldız, issue ve indirme sayıları görülemedi. ai.google.dev de kapalıydı (DNS çözülmüyor). Gemini bilgileri **WebSearch özetlerinden** alındı ve her satırda belirtildi.

## 1. Kısa sonuç

**Öneri: 5. seçenek, yani resmî Gemini API ile kendi küçük aracımız.** İncelenen dört proje tek kişilik ya da çok genç projeler. İkisi YouTube'u **yt-dlp ile indiriyor**; bu VIU-METODOLOJI'deki "indirme yok" kuralını çiğner. Hiçbiri `responseSchema` ile bizim 12 alanlı VIU JSON'umuzu üretmiyor. En iyi fikirler `DerYUYU/gemini-video-mcp` projesinde: agentic işleme, low çözünürlük, kırpma ve token raporu. Bu fikirler kodu almadan, ~150 satırlık kendi aracımızda uygulanabilir.

## 2. İncelenen sürümler

| # | Proje | Commit | Son commit | Commit sayısı / dönem | Katkıcı |
|---|---|---|---|---|---|
| 1 | DerYUYU/gemini-video-mcp | e95e8e1 | 2026-10-27 | 20 (13'ü 20 Eyl, 6'sı 21 Eyl, 1'i 27 Eki) | 1 kişi (Yilcay Birinci) |
| 2 | jordanrendric/claude-video-vision | 4a4f990 | 2026-10-06 | ≥79 (sığ klon, 31 Mar–6 Eki 2026) | 7 kişi + dependabot; ana yazar 37 commit |
| 3 | KitDevUA/video-vision-mcp | 128b7d7 | 2026-08-06 | 17 (30 Haz–2 Tem, 1'i 6 Ağu) | 1 kişi |
| 4 | oudam-meas/youtube-vision-mcp | e783ae3 | 2026-08-30 | 17'sinin hepsi tek gün (30 Ağu), telefondan (Termux) | 1 kişi (3 farklı imza) |

Dördü de MIT lisanslı. Lisans kullanıma engel değil.

## 3. 14 kriterli karşılaştırma

Puan: ✅ iyi · ⚠️ kısmi / riskli · ❌ yok / uygun değil

| Kriter | 1 gemini-video-mcp | 2 claude-video-vision | 3 video-vision-mcp | 4 youtube-vision-mcp | 5 Resmî Gemini API (kendi aracımız) |
|---|---|---|---|---|---|
| 1. Güvenlik ve kod kalitesi | ⚠️ İyi yazılmış: argv ile `spawn` (shell yok), URL'ler sıkı doğrulanıyor, anahtar loglanmıyor. Test yok. Repoda `.claude/` hook'ları var. | ⚠️ İyi test kapsamı (~179 test, CI). Ancak `.mcp.json` `npx -y claude-video-vision@latest` çalıştırıyor: repodaki değil, npm'deki **sabitlenmemiş** kod çalışır. | ❌ Keyfi dosya okuyup Google'a yüklüyor, SSRF koruması kısmi, ffmpeg ikilisi ve Whisper modeli çalışma anında **sağlama kontrolü olmadan** indiriliyor. | ❌ Python sürümü 0.0.0.0:8000'de **kimlik doğrulamasız** açılıyor. Worker sürümü anahtarı URL'de taşıyor. Test yok. | ✅ Kod bizim, küçük ve denetlenebilir. Tek resmî SDK ya da düz HTTPS. |
| 2. Güncellik / bakım | ⚠️ 1 ay önce, tek kişi | ✅ En canlı proje (7 katkıcı, dependabot) | ❌ 4 aydır sessiz | ❌ Tek günlük proje | ✅ Google bakıyor. Interactions API hâlâ `v1beta` (WebSearch) |
| 3. YouTube | ✅ Resmî yol: Gemini'ye URL veriliyor, indirme yok | ❌ yt-dlp ile tam video indiriliyor (`video-source.ts:179`) | ❌ yt-dlp ile indiriliyor (`url_loader.py:53-67`) | ✅ Resmî yol: `file_data.file_uri` | ✅ Resmî: yalnız herkese açık videolar, istek başına 1 video, ücretsiz katmanda günde 8 saat (WebSearch, Gemini dokümanı) |
| 4. Instagram/TikTok | ⚠️ Instagram yt-dlp ile indiriliyor (ToS riski). TikTok bilerek kapalı. | ❌ Desteklemiyor | ⚠️ Instagram/TikTok listede yok. Vimeo, Loom, Twitch vb. yt-dlp ile indiriliyor. | ❌ Yok | ✅ Bilerek yok. Yalnızca Bora'nın kendi kaydettiği dosyalar ya da kendi üretimimiz (VIU-METODOLOJI) |
| 5. Yerel MP4 | ✅ Files API'ye yükleme, 48 saat yeniden kullanım, uzantı listesi | ✅ ffmpeg ile kare çıkarma | ✅ Var, ama uzantı kontrolü yok | ❌ Yok | ✅ Files API (2 GB/dosya, 48 saatte silinir; WebSearch, Vertex/Gemini dokümanı) |
| 6. Görüntü + ses | ✅ Gemini ikisini birlikte okuyor | ⚠️ Kareleri **Claude** görüyor, ses ayrı modele gidiyor. Bağlam ve Claude kotası pahalı. | ✅ Gemini katmanında birlikte. Diğer katmanlarda kare ve transkript ayrı. | ✅ Gemini | ✅ Gemini tek çağrıda |
| 7. Zaman damgası | ✅ Kapsamlı start/end, mm:ss | ✅ HH:MM:SS segmentleri | ⚠️ Yalnız prompt'ta istenen MM:SS | ⚠️ Yalnız prompt metni | ✅ Prompt + kırpma (`videoMetadata` start/end) |
| 8. Kare örnekleme ayarı | ⚠️ fps yok. low/high çözünürlük ve agentic/static seçimi var. | ✅ fps, segment başına fps, `view_sample` | ⚠️ `frame_interval` var ama Gemini katmanında **yok sayılıyor** (`server.py:55`) | ❌ Yok | ✅ `videoMetadata.fps`, `media_resolution`, agentic işleme (WebSearch) |
| 9. Ücretsiz kullanım | ✅ Ücretsiz katmanda çalışıyor. Model zinciri, model başına günlük kotayı katlıyor. | ✅ Kareler Claude'da, ses Gemini ücretsiz katmanında ya da yerel Whisper'da | ✅ Yerel Whisper katmanı tamamen ücretsiz | ✅ Ücretsiz katman | ✅ Ücretsiz katman var. **Ama ücretsiz katmanda Google girdileri ürün geliştirmek için kullanabilir ve insanlar inceleyebilir** (Gemini API Ek Şartları) |
| 10. Analiz başına maliyet | ✅ Her yanıtta token raporu. Varsayılan agentic, kırpmada otomatik static-low. | ⚠️ Gemini ucuz, ama Claude kare başına görsel token harcıyor (100 kareye kadar) | ⚠️ Maliyet raporu yok, kırpma yok, tam video | ❌ Kontrol yok, tam video | ✅ Biz belirleriz: low çözünürlük, kırpma, agentic, `maxOutputTokens`, `usageMetadata` kaydı |
| 11. Bulut vardiyası | ✅ stdio + Node 22. Yalnız Instagram için yt-dlp gerekiyor. | ⚠️ ffmpeg zorunlu, Node ≥24, npx/npm erişimi | ⚠️ uv/pip, ffmpeg (yoksa internetten indiriyor), pywhispercpp derleme | ⚠️ Uzak sunucu gerekiyor (Cloudflare hesabı ya da açık port) | ✅ Tek HTTPS host (`generativelanguage.googleapis.com`, bu ortamdan erişilebilir). Anahtar dosyaya girmez; proxy ağ sırrı olarak `x-goog-api-key` başlığına eklenebilir. |
| 12. JSON çıktı | ❌ Markdown metin, şema yok | ⚠️ Yalnız ses transkripti için `responseJsonSchema` var (`gemini-api.ts:137-171`) | ❌ Markdown | ❌ Metin | ✅ `responseSchema` / `responseJsonSchema` ile VIU 12 alanı |
| 13. Önbellek | ⚠️ Yalnız yüklenen dosya 48 saat yeniden kullanılıyor. Sonuç önbelleği yok. | ✅ Oturum manifest'i, indirmeler 7 gün | ✅ SHA-256 içerik adresli sonuç önbelleği, 24 saat | ❌ Yok | ✅ Kendi `analiz-kaydi.json` önbelleğimiz (her video bir kez analiz edilir, K-028). Context caching takip soruları için isteğe bağlı. |
| 14. Platform/IP uyumu | ⚠️ YouTube uyumlu. Instagram indirme ToS riski. | ❌ YouTube indirme + 7 gün diskte saklama | ❌ Çok platformdan indirme, keyfi HTTP indirme | ✅ Yalnız resmî YouTube yolu | ✅ Indirme yok. Yalnız prensip çıkarma (Anayasa 13). |

## 4. Güvenlik bulguları (dosya:satır)

### 4.1 DerYUYU/gemini-video-mcp (Node ≥22, ESM; bağımlılıklar: `@google/genai ^2.23`, `@modelcontextprotocol/sdk ^1.30`, `zod`; lockfile var, 133 paket; kurulum betiği olanlar: `@google/genai`, `protobufjs`)
- **Olumlu:** yt-dlp `spawn(befehl, argumente)` ile, shell olmadan çağrılıyor. Windows `.cmd` için de `shell:true` kullanılmıyor (`src/ytdlp.js:407-416`).
- **Olumlu:** URL, yt-dlp'ye gitmeden önce sabit host listesi ve bütüne sabitlenmiş bir regex'ten geçiyor. URL doğrulanmış parçalardan yeniden kuruluyor. Bu, argüman enjeksiyonunu (`-` ile başlayan değer) da engelliyor (`src/quelle.js:30-31, 86-111`). YouTube kimliği 11 karakterlik regex ile denetleniyor (`src/youtube.js:46`).
- **Olumlu:** Anahtar ortamdan okunuyor (`src/gemini.js:53`). Hata metinleri anahtarı yazmıyor (`src/gemini.js:499-505`). Ham yığın izi dönmüyor (`src/index.js:232-236`).
- **Olumlu:** Instagram'ın geçici klasörü ve Google'daki kopyası `finally` bloğunda siliniyor (`src/analyze.js:154-157`, `src/ytdlp.js:335-343`).
- **Risk (orta):** Yerel yol aracı, uygun uzantılı **herhangi bir mutlak yoldaki** dosyayı Google'a yükler (`src/lokal.js:244-295`). Model yanlış yol seçerse özel bir video buluta gider. Kopya 48 saat Google'da kalır (`src/lokal.js:181-194`). Ücretsiz katmanda bu içerik eğitim veya inceleme amaçlı kullanılabilir.
- **Risk (düşük):** `.env` paket klasöründen okunuyor (`src/index.js:223-229`). Bizim kuralımızla (.env yok) çelişir; ortam değişkeniyle çalışabiliyor.
- **Risk (düşük):** Repoda Claude Code hook'ları var (`.claude/settings.json`, `.claude/hooks/guard.mjs`). Repo Claude Code ile açılırsa `node` hook'u otomatik çalışır. İçerik zararsız görünüyor (yalnız `.env` koruması ve `node --check`), ama "incelenmemiş kod çalışmaz" kuralı gereği klasör asla proje olarak açılmamalı. Repoda ajanlara talimat veren bir `CLAUDE.md` de var; bunu güvenilmez veri sayıyoruz.
- **Risk (düşük):** Çağrılar `client.interactions.create` ile `v1beta` Interactions API'ye gidiyor (`src/gemini.js:191`). Beta API değişirse araç kırılır.
- **Not:** Model zinciri 429 (kota) hatasında otomatik olarak başka modele geçiyor (`src/gemini.js:21-29, 111-177`). Bu ücretsiz kotayı katlıyor, ama hangi modelin cevap verdiği değişiyor. Kalite karşılaştırmasında modeli sabitlemek gerekir.
- **Test:** Yok (`CLAUDE.md:13` "Keine Tests"). **Telemetri:** Bulunmadı; yalnız Google'a ve Instagram için yt-dlp'ye gidiyor.

### 4.2 jordanrendric/claude-video-vision (TypeScript, Node ≥24; bağımlılıklar: MCP SDK, zod; isteğe bağlı `@google/genai`, `openai`)
- **Risk (yüksek, tedarik zinciri):** Eklenti, repodaki kodu değil npm'deki `claude-video-vision@latest` paketini çalıştırıyor (`.mcp.json`: `npx -y claude-video-vision@latest`). İncelediğimiz kod ile çalışacak kod aynı olmayabilir ve her oturumda yeni sürüm gelebilir. Yayın `--provenance` ile yapılıyor (`.github/workflows/release.yml:47`); bu kısmen hafifletiyor.
- **Risk (orta, platform):** YouTube videosu yt-dlp ile tamamen indiriliyor ve `~/.claude-video-vision/downloads` altında 7 gün tutuluyor (`mcp-server/src/utils/video-source.ts:12, 172-217`; `config.ts:19`).
- **Risk (orta, prompt enjeksiyonu):** YouTube açıklaması (4.000 karaktere kadar) olduğu gibi Claude'a gidiyor (`video-source.ts:277`, `tools/video-watch.ts:285-286`). Yabancı bir videonun açıklaması ajana talimat sızdırabilir.
- **Risk (düşük):** Silero VAD modeli `curl` ile sağlama kontrolü olmadan indiriliyor (`backends/local.ts:110-117`). Whisper modelinde SHA-256 kontrolü var (`local.ts:77-95`).
- **Olumlu:** Tüm dış komutlar `execFile` ile, shell olmadan çalışıyor (ffmpeg, yt-dlp, whisper-cli). Girdi zod ve HH:MM:SS regex'iyle doğrulanıyor (`tools/video-watch.ts:112-131`). Geçici kare klasörü siliniyor (`tools/video-watch.ts:174, 343`). Gemini'ye yüklenen ses dosyası `finally` ile siliniyor (`backends/gemini-api.ts:188-190`).
- **Mimari not:** Görüntüyü Gemini değil Claude yorumluyor (çerçeveler base64 olarak dönüyor). Gemini yalnızca ses için kullanılıyor. Bu, "Gemini görüntü+ses istihbarat servisi" hedefimize (K-028) uymuyor.
- **Test:** Var (vitest, ~179 test, Ubuntu+macOS CI). **Telemetri:** Yok (`PRIVACY.md` beyanı; kodda bulunmadı).

### 4.3 KitDevUA/video-vision-mcp (Python ≥3.10, hatchling; bağımlılıklar: `mcp`, `httpx`, `pillow`, `yt-dlp`, `openai`, `groq`, `google-genai`, `pywhispercpp`, `static-ffmpeg`; hepsi `>=` ile sabitlenmemiş, `uv.lock` var)
- **Risk (yüksek, veri sızıntısı):** `file_path` için uzantı ya da konum denetimi yok. Var olan **her dosya** kabul ediliyor (`sources/resolver.py:120-124`). 18 MB altındaki dosya, `read_bytes()` ile okunup inline olarak Google'a gönderiliyor (`backends/tier3_gemini.py:56-58`).
- **Risk (orta, SSRF):** Özel IP kontrolü yalnız ilk URL'de yapılıyor. Yönlendirmeler izleniyor (`sources/url_loader.py:21-26, 73`; yorumda kabul ediliyor). yt-dlp yolunda bu kontrol hiç yok (`url_loader.py:84-85`). HTTP indirmesinde boyut sınırı yok, disk dolabilir (`url_loader.py:70-78`).
- **Risk (orta, tedarik zinciri):** ffmpeg sistemde yoksa `static-ffmpeg` çalışma anında ikili dosya indiriyor (`media/installer.py:43-56`). Whisper modeli sağlama kontrolü olmadan indiriliyor (`media/installer.py:122-126`).
- **Risk (düşük):** `.env`, çalışma dizininden yukarı doğru **bulunan ilk** dosyadan okunuyor (`config.py:24-26`). Başka bir projenin `.env`'si yanlışlıkla yüklenebilir. `GOOGLE_API_KEY` de kabul ediliyor (`config.py:80`).
- **Risk (düşük):** Files API'ye yüklenen dosya silinmiyor, 48 saat sonra kendiliğinden düşmesine bırakılıyor (`backends/tier3_gemini.py:60-69`). Sunucu, kullanıcı sormadan video analizini "proaktif" öneren talimatlar içeriyor (`server.py:23-27`).
- **Olumlu:** `subprocess.run` liste argümanlarıyla, shell olmadan çalışıyor (`media/ffmpeg_tools.py:31` vd.). Bulut katmanında bir kez gizlilik uyarısı veriliyor (`privacy.py:20-29`). İçerik adresli önbellek var (`cache.py:20`).
- **Test:** 17 test (pytest, CI). **Telemetri:** Bulunmadı.

### 4.4 oudam-meas/youtube-vision-mcp (Python `server.py` 90 satır + Cloudflare Worker TS 177 satır)
- **Risk (yüksek):** Python sunucusu `0.0.0.0:8000` adresinde, kimlik doğrulaması **olmadan**, streamable-http ile açılıyor (`server.py:91-93`). Ağdaki herkes Bora'nın Gemini kotasını kullanabilir.
- **Risk (orta):** Worker, anahtarı URL sorgusunda taşıyor (`cloudflare-worker/src/index.ts:71`, `?key=`). Ham Gemini hata gövdesi istemciye dönüyor (`index.ts:85-88`). `observability` açık (`wrangler.jsonc:41-43`). URL'deki anahtar log'a düşmüyor gibi görünüyor, ama doğrulanmadı.
- **Risk (orta):** `youtube_url` doğrulanmıyor. Herhangi bir URI doğrudan Gemini'ye gidiyor (`server.py:35-43`, `index.ts:105`). Kullanıcı sorusu prompt'a ham olarak ekleniyor (`server.py:87`); bu yalnız model düzeyinde bir risk.
- **Bağımlılık:** `agents ^0.0.100` (1.0 öncesi), Worker için lockfile yok (`cloudflare-worker/package.json`). `requirements.txt` sabitlenmemiş.
- **Olumlu:** Worker'da Bearer jetonu sabit sürede karşılaştırılıyor (`index.ts:155-162, 201-208`). Commit öncesi sır tarama hook'ları var (`.githooks/`).
- **Test:** Yok. **Telemetri:** Yok (Cloudflare log'ları hariç).

### 4.5 Ortak not
Dört projede de `eval` ya da shell üzerinden komut çalıştırma yok. Shell enjeksiyonu riski düşük. Asıl riskler şunlar: **platform kuralları** (yt-dlp), **veri çıkışı** (keyfi dosya yükleme), **tedarik zinciri** (`@latest`, çalışma anında ikili indirme) ve **kimlik doğrulamasız ağ servisi**.

## 5. Resmî Gemini API: bulgular (WebSearch özetleri, ai.google.dev doğrudan açılamadı)

| Konu | Bulgu | Kaynak (WebSearch, 2026-11-27) | Güven |
|---|---|---|---|
| YouTube URL | Yalnız herkese açık videolar. İstek başına 1 video. Ücretsiz katmanda günde en fazla 8 saat YouTube; ücretli katmanda süre sınırı yok. | ai.google.dev/gemini-api/docs/video-understanding | Orta-yüksek |
| Yerel MP4 | Files API: dosya başına 2 GB, proje başına 20 GB, 48 saatte silinir. ~20 MB altı inline. | Vertex/Gemini dokümanı; incelenen kodlardaki yorumlar | Orta |
| Kare örnekleme | Static işleme varsayılan olarak 1 fps, API'den ayarlanabilir (`videoMetadata.fps`). | blog.google "agentic video" yazısı + docs özeti | Orta |
| Kırpma | `videoMetadata` start/end offset eski generateContent dokümanında var. **Forum raporu:** YouTube URL'sinde kırpma yalnız kareye uygulanıyor, ses tüm videodan işleniyor (olası regresyon). Interactions API'de `start_offset`/`end_offset` (incelenen kod 1). | discuss.ai.google.dev konu 178970 | Düşük-orta, **doğrulanmadı** |
| Token/saniye | Static varsayılan: **263 token/sn**. Gemini 3+ için `media_resolution`: düşük/varsayılan **70 token/kare**, yüksek **280 token/kare**; ses **25 token/sn**. Yani low ≈ 95–100 token/sn (1 fps). Kod 1'in ölçümü de bununla uyumlu (~100 / ~300). | ai.google.dev media-resolution ve video-understanding özetleri | Orta |
| Agentic işleme | 1 Eylül 2026: `processing: "agentic"`. Google'a göre token tüketiminde %88'e varan düşüş, maliyette %66'ya varan düşüş. Ek ücret yok. 3.7 Flash, 3.6 Flash ve 3.5 Flash-Lite'ta var. Interactions API hâlâ beta. Token kullanımı değişken. | blog.google "Introducing agentic video understanding"; rits.shanghai.nyu.edu | Orta (üretici beyanı) |
| Yapılandırılmış JSON | `responseMimeType: application/json` + `responseSchema`/`responseJsonSchema` çalışıyor. Kod 2'de canlı kullanım var (`gemini-api.ts:137`). | Kod incelemesi; Gemini dokümanı (doğrudan okunamadı) | Orta-yüksek |
| Context caching | Açık önbellek depolaması: 2026 sonuna kadar 1M token/saat için 0,50 $ (bazı kopyalarda 1,00 $). Önbellekli token fiyatı ayrı. Örtük önbellekte depolama ücreti yok, indirim garantisi yok. Forum: Gemini 4'te açık önbellek kaldırılmış olabilir. | ai.google.dev/pricing kopyaları; discuss.ai.google.dev konu 200723 | **Düşük, doğrulanmadı** |
| Ücretsiz katman | Var, ama kota (istek/gün) bulunamadı. Kod 1'in iddiası: 3.8 Flash için günde 20 istek (`src/gemini.js:425`); **doğrulanmadı**. Ücretsiz kullanımda girdi ve çıktılar Google ürünlerini geliştirmek için kullanılabilir ve insanlar okuyabilir. Faturalı projede bu yapılmaz. | Gemini API Additional Terms (arşiv sürümleri) | Orta (şartlar) / düşük (kota) |
| Fiyat: Gemini 3.8 Flash | Giriş 0,75 $/1M, çıkış 3,75 $/1M (düşünme tokenları dahil) — **31 Aralık 2026'ya kadar**. 1 Ocak 2027'den itibaren 1,50 $ / 7,50 $. Çıkış tarihi 2 Eylül 2026. | gcn.com, artificialanalysis.ai, thebridge.jp, eesel.ai | Orta |
| Fiyat: Gemini 3.5 Flash-Lite | Giriş 0,30 $/1M (DeepMind model sayfası), çıkış 2,50 $/1M (Vercel, sağlayıcı fiyatını yansıttığını söylüyor). Vertex'te 0,54 $. | deepmind.google/models/gemini/flash-lite; vercel.com | Orta |
| Fiyat: 3.6 / 3.7 Flash | Kaynaklar çelişkili (0,375 $ – 0,75 $ giriş). | ai.google.dev/pricing kopyaları | Düşük |

## 6. Maliyet tahmini (tek analiz, VIU 12 alanlı JSON)

Varsayımlar: static işleme, 1 fps. Video girişi **varsayılan 263 token/sn** ya da **low ≈100 token/sn**. Prompt + şema ≈1.000 token, JSON çıktısı ≈2.000 token. Düşünme tokenları çıktı olarak faturalanır; ayarlanmazsa maliyet artar (`thinkingBudget` düşük tutulmalı).

| Video | Giriş token (varsayılan / low) | **Ücretsiz katman** | 3.8 Flash, 2026 fiyatı (varsayılan / low) | 3.8 Flash, 2027 fiyatı (varsayılan / low) | 3.5 Flash-Lite (varsayılan / low) |
|---|---|---|---|---|---|
| 30 sn | ~8.900 / ~4.000 | 0 $ (kota içinde) | **~0,014 $** / ~0,011 $ | ~0,028 $ / ~0,021 $ | ~0,008 $ / ~0,006 $ |
| 60 sn | ~16.800 / ~7.000 | 0 $ | **~0,020 $** / ~0,013 $ | ~0,040 $ / ~0,026 $ | ~0,010 $ / ~0,007 $ |
| 10 dk | ~158.800 / ~61.000 | 0 $ (YouTube'da günde 8 saat sınırı) | **~0,127 $** / ~0,053 $ | ~0,25 $ / ~0,11 $ | ~0,053 $ / ~0,023 $ |

- **Agentic modla 10 dk:** Kod 1'in README'si 15 dakikalık videoda ~7.400–8.200 token ölçtüğünü iddia ediyor (generateContent ile 85.480). Doğruysa 10 dakika ≈0,01–0,02 $ eder. **Bu bir üretici iddiası, doğrulanmadı.** Ayrıca agentic modda kare/zaman kesinliği daha düşük (kod 1: "agentic sabit offset bilmez").
- **Pratik ölçek:** Ayda 100 kısa video (≤60 sn) ve 10 uzun video (10 dk), 3.8 Flash 2026 fiyatıyla ≈ 100×0,02 + 10×0,13 ≈ **3,3 $/ay**. 2027 fiyatıyla ≈ 6,6 $/ay. Low çözünürlükte bunun yaklaşık yarısı.
- **Hesap:** 30 sn × 263 = 7.890 + 1.000 = 8.890 token × 0,75 $/1M = 0,0067 $, artı 2.000 × 3,75 $/1M = 0,0075 $, toplam ≈ 0,014 $. Diğer satırlar aynı yolla hesaplandı.
- **Ücretli katman bu görevin dışında.** Ücretli API ve faturalı proje Bora onayı ister (K-028: "Ücretli API aboneliği yok"; YETKI-MATRISI A2/A3).

## 7. Önerilen mimari

**Seçim: 5. seçenek, resmî Gemini API ile kendi küçük aracımız (`scripts/viu_gemini.py` gibi, tek dosya).** Dört projenin hiçbiri kurulmaz. Kod 1'den yalnızca **fikirler** alınır (kod kopyalanmaz): agentic/static seçimi, varsayılan low çözünürlük, kırpma, her çağrıda token kaydı, açıklayıcı hata mesajları.

**Gerekçe (kanıta dayalı):**
1. **Platform uyumu:** YouTube'da tek resmî yol URL'yi Gemini'ye vermek. Kod 2 ve 3 yt-dlp ile indiriyor; VIU-METODOLOJI kuralını çiğner.
2. **JSON:** VIU 12 alanı `responseSchema` ile tek çağrıda alınabilir. Hiçbir projede bu yok.
3. **Güvenlik:** Bağımlılık ve saldırı yüzeyi en küçük. `@latest`, çalışma anında ikili indirme ve açık port yok. Yerel dosya yolu, izin verilen bir klasörle sınırlanır (kod 1 ve 3'teki keyfi yol sorununun çözümü).
4. **Bulut vardiyası:** Yalnız `generativelanguage.googleapis.com` gerekiyor. Anahtar dosyaya ya da ortama yazılmaz; ortamın **ağ sırrı** olarak `x-goog-api-key` başlığına proxy tarafından eklenir (CLAUDE.md "sırlar dosyaya yazılmaz" kuralına uygun).
5. **Maliyet:** Kısa videoda analiz başına ~1–2 sent; önbellekle her video bir kez analiz edilir.
6. **Bakım:** ~150 satırlık kendi kodumuz, tek kişilik bir yabancı projeye bağımlılıktan daha sürdürülebilir.

**Nerede ne çalışır:**

| Katman | Yerel (Bora'nın bilgisayarı) | Bulut vardiyası |
|---|---|---|
| YouTube (herkese açık) | Gerekmez | ✅ URL → Gemini, agentic ya da static-low, JSON → `denetim/viu/analizler/` |
| Instagram/TikTok | Bora'nın uygulama içinden kendi kaydettiği dosya → Gemini Files API (kişisel analiz, yeniden yayın yok) | ❌ İndirme yok. Yalnız herkese açık sayfa metni ve meta veri (mevcut kural). |
| Kendi üretimimiz (Higgsfield/Kling çıktısı) | İsteğe bağlı | ✅ Kendi dosyamız; Files API'ye yükle, analiz et, **hemen sil** |
| Ücretsiz yerel ölçümler | `scripts/video_qc.py` (VIU-1, ffmpeg) | ffmpeg varsa aynı |
| Önbellek | — | `analiz-kaydi.json`: anahtar = platform+video kimliği ya da SHA-256 |

**Kurallar:**
- (a) Ücretsiz katmana yalnızca **herkese açık pazar videoları** gönderilir. Yayınlanmamış kendi üretimimiz ücretsiz katmana gönderilmez, çünkü Google içeriği okuyabilir. Bunun için faturalı proje gerekir (Bora kararı).
- (b) Model adı her analizde kaydedilir ve otomatik model değişimi kapalı tutulur.
- (c) `thinkingBudget` ve `maxOutputTokens` sınırlanır.
- (d) Analiz başına token ve maliyet `vardiyalar/CONFIG.json`'daki bütçe sınırıyla karşılaştırılır (sayı yalnız orada durur).

**Bora'dan gereken kararlar:**
1. Gemini API anahtarı (AI Studio, ücretsiz) oluşturulsun mu? Anahtar ortamın ağ sırrı olarak girilir, sohbete yazılmaz.
2. Kendi üretimimizi analiz etmek için faturalı proje açılsın mı (A3)?

**Alternatif yol:** Anahtar gelmezse VIU-1 (yerel ffmpeg ölçümleri) + VIU-2 (Claude ajanının kare incelemesi) ile devam edilir. Yavaştır ama ücretsizdir.

## 8. Doğrulanamayanlar

- ai.google.dev açılamadı. Bütün Gemini bilgileri WebSearch özetlerinden; fiyat sayfası kopyaları birbiriyle çelişiyor (özellikle 3.6/3.7 Flash ve context caching).
- Ücretsiz katmanın istek/gün kotası bulunamadı ("3.8 Flash günde 20 istek" yalnızca kod 1'in iddiası).
- YouTube URL'sinde `videoMetadata` kırpmanın sesi de kırpıp kırpmadığı belirsiz (forum: ses kırpılmıyor, maliyet ~20 katına çıkabilir). İlk benchmark'ta `usageMetadata` ile ölçülmeli.
- Agentic modun gerçek token tasarrufu (Google %88, kod 1 %91 diyor) bağımsız olarak doğrulanmadı.
- Interactions API'de `responseSchema` / `response_format` desteği ve agentic modla birlikte kullanılabilirliği doğrulanmadı. Gerekirse JSON için generateContent ile static mod kullanılır.
- Gemini 4 ile açık context caching'in kaldırıldığı iddiası (forum) doğrulanmadı.
- GitHub yıldız, issue ve npm/PyPI indirme sayıları görülemedi (github.com 403). claude-video-vision sığ klonlandığı için toplam commit sayısı ≥79.
- npm'deki `claude-video-vision@latest` paketinin repo ile aynı olup olmadığı kontrol edilmedi (paket indirilmedi).
- Instagram ve TikTok'un güncel otomatik toplama şartları bu aramada gelmedi. Mevcut kural (indirme yok) geçerli; kaynak: `istihbarat/platform-analizleri/2026-11-27-platform-kurallari.md`.
- YouTube ToS'taki indirme yasağına ilişkin kaynaklar eski (2016–2022). Güncel metin doğrudan okunmadı.

## Kaynaklar (WebSearch, 2026-11-27)
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/
- https://rits.shanghai.nyu.edu/ai/gemini-agentic-video-understanding/
- https://ai.google.dev/gemini-api/docs/video-understanding · https://ai.google.dev/gemini-api/docs/interactions/video-understanding
- https://ai.google.dev/gemini-api/docs/media-resolution
- https://ai.google.dev/gemini-api/docs/pricing (yalnızca arama kopyaları)
- https://discuss.ai.google.dev/t/videometadata-clipping-on-youtube-urls-no-longer-clips-audio-frames-still-clipped-20x-token-inflation-on-long-videos/178970
- https://discuss.ai.google.dev/t/title-gemini-4-removes-explicit-context-caching-my-per-call-cost-goes-up-4x-with-no-way-to-control-it/200723
- https://gcn.com/google-ships-gemini-flash-stronger-agentic/21390/ · https://artificialanalysis.ai/articles/gemini-3-8-flash · https://eesel.ai/blog/gemini-3-8-flash-pricing
- https://deepmind.google/models/gemini/flash-lite/ · https://vercel.com/ai-gateway/models/gemini-3.5-flash-lite
- https://ai.google.dev/gemini-api/terms-archive/terms_09_25_25 · https://simonwillison.net/2024/Oct/17/gemini-terms-of-service
- https://www.youtube.com/terms · https://developers.google.com/youtube/terms/developer-policies · https://uwaterloo.ca/copyright-at-waterloo/faq-0-9
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding
