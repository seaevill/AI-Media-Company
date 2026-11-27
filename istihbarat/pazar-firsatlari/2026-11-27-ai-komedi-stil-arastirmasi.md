# AI Komedi / Kısa Video: Görsel Stil ve Şaka Yapısı Pazar Araştırması

- Görev: G-0030 (A0, kredi 0) · Araştırma tarihi: 2026-11-27 · Hazırlayan: pazar-istihbarati
- Soru: 2025-2026 gerçek pazarında hangi AI komedi/eğlence formatları ve görsel stiller büyük izlenme/takipçi alıyor, hangileri batıyor?
- Yöntem: WebSearch + doğrudan sayfa okuma (YouTube kanal sayfaları, TikTok profil sayfası gövdesindeki `statusCode`/`followerCount`). Giriş, CAPTCHA, API aşılmadı. Tüm sayaçlar 2026-11-27'de okundu; "sayfa" diye işaretli değerler birincil, "haber/blog" diye işaretliler ikincildir.
- Bilgi sınıfı: tablolardaki sayılar **doğrulanmış** (tarihli kaynak). "Neden çalıştı" sütunları **hipotezdir**. Videoların kendisi izlenmedi, kareler görülmedi (bkz. kısıtlar); stil etiketleri kaynak metinlerine ve başlıklara dayanır.
- "Beğeni/video" ve "medyan" değerleri benim hesabımdır (sayfadaki değerlerden türetilmiş); sayfa değeri değildir.

## 0. Tek paragraf sonuç

Pazarda büyük ölçekli AI eğlence başarıları gerçek ve bol; ama **bizim stil ve şaka tercihlerimize (mat/soluk 3D, sözsüz, fiziksel etkileşim, çok olay, zamanlama modelde) uyan tek bir doğrulanmış başarılı hesap bulamadım.** Başarılı örneklerin ortak paydası stil değil: (1) tek ve hemen tanınan karakter, (2) tek net fikir, (3) komedinin yazı, ses/seslendirme, altyazı ve kurguyla kurulması, (4) güçlü ses/duygu çengeli. Yüksek izlenmeli sözsüz hesapların çoğu "komedi" değil sevimlilik veya duygusal melodramla büyüyor. Yüksek izlenme çoğu hesapta takipçi veya ikinci platforma dönüşmüyor. Kısa ömürlü/kapanan örnekler de çok (Fruit Love Island, ban/silinen kanallar, Sora).

## 1. Örnek tablosu (doğrulanabilir; ≥15)

Sütunlar: Platform/URL · Sayı (kaynak, tarih) · Stil · Şaka yapısı · Konuşma · Hipotez · Güven. Tüm sayfa değerleri 2026-11-27.

| # | Hesap | Platform / URL | Sayı | Stil | Şaka/içerik yapısı | Konuşma | Neden çalışıyor (HİPOTEZ) | Güven |
|---|---|---|---|---|---|---|---|---|
| 1 | Neural Viz | YouTube https://www.youtube.com/@NeuralViz · TikTok https://www.tiktok.com/@neuralviz | YT 237K abone, 57 video (sayfa). TT 366.864 takipçi, 7.585.280 beğeni, 58 video (sayfa). Son 30 YT videosu: medyan 235K, en yüksek 639K ("This Is News"), en düşük 56K. En son YT yüklemesi "6 ay önce" | Fotogerçekçiye yakın canlı-çekim görünümlü uzaylı/yaratık karakterler (Monoverse); mockumentary | Deadpan mockumentary: sokak röportajı, haber, polis programı; yazılmış replik ve karakter komedisi. WIRED özeti: senaryoyu yaratıcı yazıyor, storyboard/tutarlılık için araç zinciri kullanıyor, karakterleri kendi performansıyla (Runway Act-One/Two) canlandırıyor | Konuşmalı (İngilizce) | Komedi **yazıdan ve insan performansından** geliyor; model yalnızca görüntü. Tek biçimli "program" şablonu yeni bölüm üretmeyi kolaylaştırıyor. Son 5 yüklemede (56K-116K) izlenme ilk yıl bölümlerinin (medyan ~235K) altında | Yüksek (sayılar), orta (üretim yöntemi: WIRED'in kopya sayfaları üzerinden) |
| 2 | Bandar Apna Dost | YouTube https://www.youtube.com/@BandarApnaDost | 3,96M abone, 77 video (sayfa). Shorts sekmesinde görünen 30 klip: medyan 3,35M, en yüksek 90M, en düşük 51K. Önceki ölçüm 2,76M abone / 2,07 milyar toplam izlenme (Business Standard, 2025-12-31, Kapwing'e dayalı) | Gerçekçi görünümlü maymun + güçlü insan karakter; AI | Başlıklar Hindistan ordusu/vatan/aile melodramı ("Heart Touching", "Indian Army") ve aksiyon; eski videolar komik maymun vlog (6K-200K) | Sözsüz (diyalogsuz, Hintçe başlık) | En büyük klipler komedi değil **duygusal/vatansever melodram**; evrensel jest dili + yerel kimlik çengeli. Komik eski vlog'lar çok daha az izlenmiş (6K-200K) | Yüksek (sayı), orta (yorum) |
| 3 | meowtakeover | TikTok https://www.tiktok.com/@meowtakeover · YouTube https://www.youtube.com/@meowtakeover | TT 2.627.586 takipçi, 169.764.992 beğeni, 405 video (sayfa; ~419K beğeni/video). YT 25,2K abone, 404 video (sayfa); YT Shorts (30) medyan 20,5K, en yüksek 2,1M. KYM: 39,7M ve 107,5M izlenmeli videolar (wiki, düşük güven) | Sevimli AI yavru kedi grubu; cilalı, parlak | Dans/mini eylem + trend ses; "şaka" yok, sevimlilik ve ses | Sözsüz | Sevimlilik + trend ses + her videoda aynı üçlü kedi; remix kültürü. TikTok'ta dev, YouTube'da küçük: izlenme platformlar arasında geçmiyor | Yüksek (sayılar) |
| 4 | MPminds ("Chubby" kedi) | TikTok https://www.tiktok.com/@mpminds | 1.352.411 takipçi, 32.036.438 beğeni, 188 video (sayfa; ~170K/video) | Stilize/sevimli AI kedi karakteri ("Chubby") | Duygusal mini hikâye + şarkı | Sözsüz/şarkı | Tek tekrar eden karakter + duygu; ama format "çocukları ağlatma" itibar sorunu taşıyor (repo Kart 5) | Orta |
| 5 | Fruit Love Island (@ai.cinema021) | TikTok (hesap kapalı/bulunamadı: statusCode 10221) | 9 günde 3,1M takipçi (X paylaşımı ~2026-03-22), 10 günde 3,3M (Khaleej Times/AOL, Nisan 2026); 20 bölüm ~300M izlenme (The Star, 2026-04-08). Seri 28 Mart 2026'da durdu | Stilize/gerçekçi karışık meyve-kafalı karakterler, Love Island parodisi | Reality TV parodisi: önceden bilinen format + absürt öncül + dramatik seslendirme + izleyici oylaması | Konuşmalı (seslendirme, altyazı) | Tanıdık format + etkileşimli eşleştirme oyu. Eleştiri: hatalı kollar, kopuk bölümler, "mantıksız olay örgüsü" | Yüksek (olay), orta (rakamlar) |
| 6 | TailBitPets (Rufus) | TikTok https://www.tiktok.com/@tailbitpets · YouTube https://www.youtube.com/@tailbitpets | TT 856.695 takipçi, 44.700.610 beğeni, 587 video (sayfa; ~76K/video). YT 153K abone, 562 video (sayfa); Shorts (30) medyan 38K, en yüksek 1,9M, en düşük 4,8K. (Repo Kart 24'te Daily Dot/Dexerto: 42,8K / 38K takipçi, Ocak 2026 civarı) | Gerçekçi görünümlü AI köpek ("Rufus"), tek karakter, az hareket | Kısa sahne + **altyazı/başlıkta punchline** ("The helmet is rated for speeds he will never reach"); köpek ifadesi tek kare | Sözsüz (başlık-ifade) | Tek ifade karesi + yazılı espri. Takipçi eski haberlerdeki 42,8K'dan 856K'ya çıkmış (farklı tarih/kaynak, doğrudan kıyas değil). Videolar arası yayılım büyük (4,8K-1,9M) | Yüksek (sayılar), orta (yorum) |
| 7 | Granny Spills | TikTok https://www.tiktok.com/@grannyspills · YouTube https://www.youtube.com/@grannyspills | TT 1.165.031 takipçi, 16.128.528 beğeni, 714 video (sayfa; ~23K/video). YT 2,32K abone, 322 video (sayfa). Repo Kart 3'teki "YouTube 2,1M" iddiası (CreatorDB) **yanlış/hatalı görünüyor**: sayfa 2,32K diyor | Gerçekçi AI yaşlı kadın persona, kameraya doğrudan | Tek karakter, "dobra tavsiye/hot take" tek cümle zıtlığı | Konuşmalı | Tek karakter + zıtlık (tatlı görünüm, sert söz). Platformlar arası çok eşitsiz | Yüksek (sayılar) |
| 8 | Yeti Vlog Life / Big Yowie (Bigfoot-yeti vlog kümesi) | TikTok https://www.tiktok.com/@yetivloglife | yetivloglife: 310.267 takipçi, 4.191.368 beğeni, **12 video** (sayfa; ~349K/video). Big Yowie: 250K takipçi, 35M izlenme, 20 paylaşım (Kapwing blogu, tarih belirsiz) | Gerçekçi görünümlü AI yaratık selfie vlog (Veo 3) | Tek karakter kameraya konuşur, ses/aksan/replik; Kapwing: yaratıcı storyboard ve kurgu bilgisiyle çekiyor (180 derece kuralı) | Konuşmalı | Yeni araç "vay" etkisi + güçlü tek karakter (aksan, şapka). Araç kaynaklı format; Kapwing taraflı kaynak (araç satıcısı) | Orta |
| 9 | Chloe VS History | YouTube https://www.youtube.com/@chloevshistory | 431K abone, 70 video (sayfa). Son 8 uzun video: medyan 684,5K; en yüksek 3,2M (Titanic 1912), 3,1M (Tudor London); en yeni (1 ay önce) 237K | Gerçekçi insan persona, POV vlog (insan olduğu izlenimi) | Tarihi olayda "ben şu an oradayım" POV, hafif mizah | Konuşmalı | Sabit persona + POV. Kaynak notu: gerçek insan sanılması ifşa/itibar riski (repo Kart 9) | Yüksek (sayılar) |
| 10 | The Dor Brothers | YouTube https://www.youtube.com/@thedorbrothers | 277K abone, 84 video (sayfa). Son videolar: 309K ("GTA VI: Cursed Trailer", 7 gün), 119K, diğerleri 23K-177K | Gerçekçi, karanlık/sinik AI satir kısa filmleri | Parodi/siyasi-kültürel hiciv, sahte fragman | Konuşmalı | Tanınan referansa (GTA vb.) dayalı hiciv; ama marka/IP ve gerçek kişi riski yüksek | Orta |
| 11 | Goldie & Frenchie (DogPack köpek podcast) | Instagram/TikTok (resmi hesap adı doğrulanamadı) | 1M+ takipçi (The Hustle); 1,5 milyar izlenme (tanıtım basın bülteni, Webull'da yayımlanmış) — **taraflı kaynak** | Gerçekçi AI köpekler (Veo 3), ~8 sn klipler | Masa başı sabit plan, iki köpek **konuşur**, yazılı replikle zıtlık; Warner Bros aynı formatı tanıtımda kullanınca tepki aldı | Konuşmalı | Çok az hareket, ifade + replik; ama uygulama (DogPack) tanıtımı için üretilmiş: ticari amaçlı | Orta-düşük |
| 12 | alexey_pigeon (Italian brainrot: Cappuccino Assassino, Chimpanzini Bananini) | TikTok https://www.tiktok.com/@alexey_pigeon · YouTube https://www.youtube.com/@alexey_pigeon | TT 408.140 takipçi, 25.428.705 beğeni, 130 video (sayfa). YT 134 abone | Sürreal 3D hibrit yaratıklar | Saçma isim + sahte İtalyanca ses, tekrar eden "lore" | Sahte dil (anlamsız ses) | İç şaka/çocuk kültürü; ses karakterin kendisi. Sahipsiz IP: para başkalarına gitti (repo Kart 17) | Orta |
| 13 | Infinite Unreality | TikTok https://www.tiktok.com/@infiniteunreality · YouTube https://www.youtube.com/@infiniteunreality | TT 253.335 takipçi, 9.712.690 beğeni, 485 video (sayfa; ~20K/video). YT 478 abone | Gerçekçi görünümlü "ev/kamera" klipleri | Tek seferlik sürreal sahne ("gerçek mi?") | Çoğunlukla sözsüz | Gerçek sanılması; karakter yok, bağ zayıf | Orta |
| 14 | Basin Creek Retirement Village | TikTok https://www.tiktok.com/@basincreekretirement · YouTube https://www.youtube.com/@basincreekretirement | TT 66.329 takipçi, 5.849.573 beğeni, 386 video (sayfa). YT 5,6K abone; YT Shorts (30) medyan 1,15K, en yüksek 5,4K | Gerçekçi yaşlı bakım evi sakinleri, kameraya sorulu cevaplı | Kameraya mini röportaj ("What keeps you going?") | Konuşmalı | İfşa sonrası ilgi düştü (hipotez); sözlü röportaj biçimi tek başına yetmiyor | Orta |
| 15 | veo3aimemes | TikTok https://www.tiktok.com/@veo3aimemes | 16.027 takipçi, 1.515.137 beğeni, 11 video (sayfa; ~138K/video) | Gerçekçi Veo 3 "AI skit" | Kısa skit; bio: "Funny AI skits (not real videos)" | Konuşmalı | Küçük hesap, az videoyla yüksek beğeni/video; PJ Ace de "300 takipçili hesapta bir videoyla 3M izlenme" (X paylaşımı, Haziran 2025, kendi beyanı) diyor | Orta |
| 16 | "Veo 3 sokak röportajı / prompt theory" akımı | TikTok (tek tek klipler) | Mayıs 2025: sokak röportajı klibi 14M+ izlenme (Nomusica). "Prompt Theory" klibi @hashem.alghaili sayfasında 279,2K beğeni, 6.080 yorum (arama sonucu özeti; yaratıcı atfı çelişkili: @Intern_SaharaAI de anılıyor) | Gerçekçi konuşan Veo 3 karakterleri | "Biz AI değiliz" absürt öncül; "gerçek mi" şokunun komediye çevrilmesi | Konuşmalı | Araç ilk çıktığı anın "vay" etkisi; tek video başarısı kalıcı talep kanıtı değil | Orta-düşük |
| 17 | agnightlive ve 80'ler AI sitkomları | TikTok https://www.tiktok.com/@agnightlive (**bulunamadı: statusCode 10221**) | Temmuz 2025 haber: haftalık, ~1 dk bölüm, bazı klipler 600K'ya kadar (Newswav) | Gerçekçi 80'ler sitkom estetiği | Sitkom kalıbı (tekrarlı kadro, tanıdık format) | Konuşmalı | Nostalji + tanıdık format; kalıcılık kanıtı yok (hesap artık yok) | Düşük |

## 2. Başarısız, küçük, kapanan veya zarar gören örnekler (hayatta kalma yanlılığı kontrolü)

| Örnek | Kanıt | Ders (HİPOTEZ) |
|---|---|---|
| VEO Punchlines (YouTube https://www.youtube.com/channel/UCYbvkLfnQS8983p8xj24emQ) | 31,3K abone, 136 video; bakılan 6 videoda medyan ~8,1K, en yüksek 29K, biri 71 izlenme (sayfa, 2026-11-27); bir başlık "It's so bad, it's not even funny" | Araç demosu + toplama klip + "Veo 3 komedi" etiketi izleyici çekmiyor; karakter/özgün öncül yok |
| Funny AI Animations / Cartoo Comedy (YouTube kanalları) | Funny AI Animations: 28 video (sayfa), tarif "3D cartoon style, Veo 3"; abone sayısı sayfada görünmedi. Cartoo Comedy: 8 abone, 22 video (sayfa) | Genel "AI çizgi film komedi" kanalları tutmuyor. Not: 2D/kil/anime AI komedi için **büyük bir başarılı örnek bulamadım**; yalnızca bu küçük hesapları buldum |
| Basin Creek Retirement YouTube tarafı | TikTok 66K takipçi, YouTube Shorts medyanı 1,15K (sayfa) | TikTok'taki ilgi ikinci platforma geçmedi |
| Meowtakeover ve TailBitPets'in YouTube tarafı | Meowtakeover: TT 2,63M vs YT 25,2K; TailBitPets: TT 857K vs YT 153K | "Büyük izlenme" ≠ platformlar arası kitle |
| Fruit Love Island | Hesap bulunamadı (10221), 22 bölümden ~12'si şikâyetle kaldırıldı, seri 28 Mart 2026'da durdu (Gizmodo/Daily Dot, repo B1) | Tek hesap/tek platform riski, AI karşıtı toplu şikâyet |
| YouTube Ocak 2026 temizliği | 16 kanal, 35M+ abone, 4,7 milyar izlenme silindi veya temizlendi; CuentosFacinantes ~5,9M abone (Kapwing aktarımı IBTimes, Tubefilter 2026-01-29). Bandar Apna Dost listede ama hâlâ aktif (3,96M) | Şablon/tekrar üretim "spam" sayılıyor; kimi büyük kanallar ayakta |
| Screen Culture / KH Studio | 2M+ abone, 1 milyar+ izlenme; Aralık 2025'te sonlandırıldı (heise, TheWrap; repo B2) | Yanıltıcı meta veri ve IP |
| "Nothing, Forever" (AI Seinfeld) | Twitch 14 gün askı, Şubat 2023 (TechCrunch 2023-02-06 başlıklı sayfa, NBC, Vice); yaratıcılar moderasyon filtresini doğru kullanmadıklarını söyledi; sebep model üretimi stand-up şakası | **Şakayı modele bırakmak** moderasyon ve kalite riski; Bu örnek 2023, yalnızca eski kanıt |
| Sora uygulaması | OpenAI 24 Mart 2026'da kapatma duyurusu (NPR/Axios, repo B4) | Tek araca bağımlı hesap (Basin Creek) yarı yolda kaldı |
| Warner Bros AI köpek podcast tanıtımı | Online tepki (Softonic, aifilms.ai özetleri; taraflı) | Büyük marka bile AI etiketli kampanyada tepki alabiliyor |

## 3. Stil karşılaştırması (fotogerçekçi vs stilize 3D vs 2D vs kil vs anime)

| Stil | Doğrulanmış örnekler | Ölçek (kanıtlı) | Şaka yapısı eğilimi | Riskler | Not |
|---|---|---|---|---|---|
| **Fotogerçekçi görünümlü, insan-dışı karakter** (yaratık/hayvan: Yeti, Bandar maymun, Rufus, DogPack köpekler, Neural Viz uzaylıları) | #1, #2, #6, #8, #11 | En büyük kanıtlı ölçek burada: Bandar 3,96M, TailBitPets 857K TT, Yeti 310K (12 videoyla) | Tek karakter, ifade/replik, mockumentary/vlog, altyazı espri | "Gerçek mi" tartışması; etiket; gerçek sanılırsa tepki (Basin Creek, Infinite Unreality) | İnsan-dışı karakter "gerçek sanılma" itibar riskini azaltıyor (hipotez) |
| **Fotogerçekçi görünümlü insan persona** (Granny Spills, Chloe, Basin Creek) | #7, #9, #14 | Orta (431K-1,17M) ama çok eşitsiz | Tek cümle zıtlık, POV | Aldatma algısı, itibar, repo B9 | Platformlar arası geçmiyor (#7) |
| **Stilize/parlak 3D, sevimli hayvan/obje** (meowtakeover, MPminds, meyve) | #3, #4, #5 | TikTok'ta en büyük sayılar (2,63M, 1,35M, 3,3M/10 gün) | Komedi değil sevimlilik + ses/duygu; reality parodisi | Çocuk içeriği algısı, doygunluk, şikâyet | "Cilalı/parlak" görünüyorlar (kaynak metin); **mat/soluk değil** |
| **Sürreal 3D hibrit/brainrot** (Italian brainrot) | #12 | 408K TT ama tür çok daha büyük (oyun/oyuncak) | Saçma ses + isim | Sahipsiz IP, düşüş (repo Kart 17) | Karakter + ses = IP |
| **2D çizgi film** | Doğrulanabilir büyük örnek **bulunamadı** | — (yalnızca 8 aboneli Cartoo Comedy) | — | — | Kanıt yok ≠ imkânsız; araştırma sınırlı |
| **Kil (claymation)** | Doğrulanabilir hesap **bulunamadı** | — | — | — | Yalnızca satıcı blogları "trend" diyor (autoclips.app vb., taraflı) |
| **Anime** | Doğrulanabilir komedi hesabı **bulunamadı** | — | — | — | Yalnızca TikTok keşfet sayfaları (beğeni sayıları, görüntülenme değil) |

Okuma: AI komedide pazar şu an **insan-dışı fotogerçekçi görünümlü karakter** ve **sevimli parlak 3D** tarafında kanıt veriyor. 2D/kil/anime tarafı "başarısızlık kanıtı" değil, "kanıt bulamadım".

## 4. Şaka yapısı karşılaştırması

| Yapı | Örnek | Komediyi kim taşıyor? | Kanıt |
|---|---|---|---|
| Deadpan mockumentary (röportaj, haber, polis programı) | Neural Viz | **Yazı + insan performansı** | #1 (medyan 235K, YT; 367K TT) |
| Karaktere kameraya tek cümle zıtlık | Granny Spills, Yeti vlog | Replik/ses/aksan | #7, #8 |
| Başlık/altyazı punchline + hayvan ifadesi | TailBitPets | **Altyazı + tek ifade karesi** | #6 (medyan 38K, tepe 1,9M) |
| Tanıdık format parodisi | Fruit Love Island, 80'ler sitkom, Dor Brothers | Format bilgisi + seslendirme | #5, #10, #17 |
| Sevimlilik + trend ses | meowtakeover | Ses + sevimlilik, şaka yok | #3 |
| Duygusal melodram, sözsüz | Bandar (büyük klipler) | Müzik + jest, komedi değil | #2 |
| Saçma isim/ses (brainrot) | Italian brainrot | Ses | #12 |
| Fiziksel etkileşim, çok olaylı slapstick | Doğrulanmış büyük başarı **bulunamadı**. En yakın: Bandar'ın eski komik maymun vlog'ları (6K-200K) | Model | Zayıf |

## 5. Konuşmalı vs sözsüz

- **Sözsüz büyük sayılar:** Bandar (YT Shorts medyan 3,35M), meowtakeover, MPminds. Ancak bunlar komedi değil, duygu/sevimlilik. Bandar başlıkları Hintçe: sözsüz olması dil bağımlılığını tamamen kaldırmıyor, yerel kitle ve platform çengeli devrede.
- **Konuşmalı ama dil bağımlı:** Neural Viz (İngilizce yazı) YT'de medyan 235K, ama son uzun videolar 56K-116K; Chloe medyan 684K (İngilizce). Konuşmalı içerik daha az sayıda büyük başarı verdi ama yazılı komedi ancak konuşmayla mümkün.
- **Altyazı/başlık köprüsü:** TailBitPets sözsüz görüntü + yazılı espri kullanıyor; sözlü dil gerektirmeden mizah taşıyor (kanıt: başlıklar, #6). Çok dilli altyazıyla ölçeklenebilir (hipotez).
- **Kontrollü karşılaştırma yok:** Aynı fikrin konuşmalı/sözsüz sürümlerini karşılaştıran veri bulamadım. "Sözsüz = global = daha çok izlenme" **kanıtlanmış bir ilişki değil**. Kapwing aktarımı: Güney Kore'nin trend AI kanalları en çok toplam izlenmeyi (8,45 milyar), İspanya en çok abone (20,22M) getirmiş (düşük kalite "slop" kanalları, komedi değil). Bu, dil bağımlılığı için dolaylı bir göstergeden fazlası değil.

## 6. Komedi zamanlamasını modele değil montaja bırakanlar

- **Neural Viz:** senaryo elle yazılıyor, performans yaratıcının kendisinden (mocap), model yalnızca yüzeyi veriyor (WIRED özeti, ikincil kopya).
- **Big Yowie:** Kapwing'e göre yaratıcı storyboard ve kurgu bilgisini (180 derece kuralı) kullanıyor (taraflı blog).
- **TailBitPets:** punchline görüntüde değil **başlıkta** (YT Shorts başlıkları, sayfada görüldü).
- **Fruit Love Island:** seslendirme + tema müziği + sunucunun izleyici yorumlarını okuması; komedi montaj/sese yatırılmış (haber özeti).
- **DogPack:** ~8 sn Veo 3 klipleri, yazılı replik (The Hustle).
- **İnsan komedi:** "Veo 3 gibi davranan" gerçek TikTok kullanıcıları milyonlarca izlenme topladı (Ars Technica/itc.ua özeti): zamanlamayı insan veriyor.
- **Karşı sinyal:** "AI komedi zamanlamasını kendi başına yapar" iddiası yalnızca araç satıcılarından (Agent Opus, Reap vb., taraflı); aynı sayfalar nihai kurguyu insanın yapması gerektiğini söylüyor. Hiçbir başarılı örnekte "zamanlamayı model kurdu" kanıtı bulamadım. Tek tersi örnek Nothing, Forever (model üretimi şaka) ve sonucu moderasyon sorunu.

## 7. Tek karakter, az hareket, ifade/diyalog ağırlıklı formatlar

Örnekler: Neural Viz röportaj/talking head, Yeti selfie vlog, Granny Spills kameraya konuşma, Rufus tek plan, DogPack masa başı, Basin Creek mini röportaj. Hepsinde fizik zayıflığı sorun olmuyor. Ancak **bu format tek başına yetmiyor:** Basin Creek aynı kalıpla YT medyanı 1,15K'da kaldı. Çalışanlarda ortak: **keskin karakter fikri** (alien deadpan, aksanlı yaratık, tatlı ama sert büyükanne, küçük köpek + ciddi iş) ve yazılı replik.

## 8. Bizim "mat 3D, soluk renk" estetiğine yakın başarılı hesap var mı?

**Hayır, doğrulanmış bir tane bulamadım.** İncelenen başarılı hesapların kaynak metinleri parlak/sevimli (meowtakeover, MPminds) ya da fotogerçekçi görünümlü (Bandar, Rufus, Neural Viz) diyor. Uyarı: kareleri göremedim (thumbnail sunucusu proxy tarafından 403), bu yüzden "tam olarak mat/soluk olmadığını" kanıtlayamam; kanıt eksikliği = pazar doğrulaması yok. Bu, ChatGPT ön teşhisini ("mat 3D/soluk estetik pazar doğrulaması olmadan seçildi") destekler. Fiziksel etkileşim, çok olay ve sözsüz fiziksel şaka için de doğrulanmış büyük başarı bulunamadı.

## 9. ChatGPT ön teşhisiyle karşılaştırma

| İddia | Sonuç |
|---|---|
| Mat 3D/soluk estetik pazar doğrulaması olmadan seçildi | Destekleniyor: yakın başarılı örnek bulunmadı |
| Fiziksel etkileşimler zayıf | Dolaylı destek: başarılı örneklerde şaka fiziksel değil; kanıt yokluğu |
| Çok olay | Dolaylı destek: başarılı örneklerin çoğu tek fikir/tek plan |
| Komedi zamanlaması modele bırakıldı | Güçlü destek: hiçbir başarılı örnek modele bırakmıyor (yazı/performans/kurgu/altyazı) |

## 10. Bizim için 5 çıkarım (hepsi HİPOTEZ; kanıtlanmış yöntem değil)

1. **Stili bağımlı değişken yapma; premise ve karakteri başa al.** Mat/soluk 3D için pazar kanıtı yok; parlak sevimli 3D ve insan-dışı fotogerçekçi görünüm için var. Mevcut stili "varsayılan" olmaktan çıkar; küçük, tek değişkenli bir stil testi planla (A2 onayı gerekir, bu görevde yapılmadı).
2. **Komediyi önce yazıda ve kurguda kur.** Her video: tek fikir, tek olay, setup → bekleme → punchline; punchline altyazıda, sesle veya tepki karesinde. Modelden yalnızca "hareketsiz ifadeli kare + kısa hareket" iste. Zamanlamayı montajda ses efekti/kesme/altyazı ile kur.
3. **Tek karakter, az hareket, ifade/diyalog.** Fiziği atla. İnsan-dışı (hayvan/yaratık) ve açıkça kurgusal karakter; gerçek insan benzeri persona itibar riski taşıyor (Basin Creek, Chloe).
4. **Sözsüzlüğü komedi için varsayılan yapma.** Sözsüz büyük başarılar duygu/sevimlilik. Komedi için kısa yazılı replik/altyazı (TR+EN) dene; "tek dil" bağımlılığını altyazıyla azalt. Bunun için kontrollü aynı-fikir-iki-sürüm testi planla.
5. **Tek platforma, tek araca, şablona güvenme.** İzlenme platformlar arasında geçmiyor (TT 2,63M vs YT 25,2K), şablon toplu üretim silinebiliyor (Ocak 2026), AI etiketi etkileşimi düşürüyor (CBS araştırma özeti: tam-AI içerikte ~46 puan; repo B7: TikTok'ta -%21,2). Karakter + dünya + isim yapısı kur, aracı değiştirilebilir tut.

Not: 3. ve 4. maddeler Anayasa 14 (AI kimliği, gerçekçi içerikte açıklama) ve Anayasa 22 ile uyumlu olmalı.

## 11. Riskler (fotogerçekçi AI komedi)

- AI etiketi: TikTok'ta etkileşim cezası; etiketi gizlemek kural ihlali (Anayasa 12-14).
- Yanıltıcılık: "gerçek sanılma" viral olsa da öfkeyle bitiyor (Infinite Unreality, Basin Creek, TailBitPets).
- Platform kuralı: YouTube spam/yanıltıcı meta veri politikası (Screen Culture, Ocak 2026 temizliği).
- Gerçek kişi/marka taklidi: Dor Brothers, ünlü bebek podcast vb. bizim için yasak (Anayasa 11, 13).
- Meyve/obje formatında şiddet alt türü (GNET, 2026-08-10; repo Kart 2).

## 12. Erken sinyal ve yaşam döngüsü (kısa)

Yaşam döngüsü sınıflandırması yapılmadı: veri (zaman serisi) yok. Gözlenen sinyaller: araç yeni çıkınca format doğuyor (Veo 3 vlog/sokak röportajı, Sora), küçük hesaplarda anormal performans (#8, #15), platformlar arası geçmeme (#3, #6, #7), doygunluk (Fruit Love Island kopyaları). Hiçbiri tek başına gelecek popülerliği göstermez.

## 13. Araştırma kısıtları

- WebFetch bu ortamda yalnızca izin verilen host'lara açık: sloptvnews.com ve en.wikipedia.org çözümlenemedi; haber/Wikipedia sayfaları yalnızca WebSearch özetleri üzerinden okundu (birincil metin okunmadı). Özetler hatalı olabilir.
- YouTube/TikTok videoları izlenmedi; küçük resim sunucusu i.ytimg.com proxy tarafından 403 (aşılmadı). Stil ve renk yorumları metne dayanır; "mat/soluk" tespiti mümkün olmadı.
- TikTok profil sayfası takipçi/beğeni/video sayısı verdi; tek video izlenmesi vermedi. YouTube Shorts izlenmeleri sekmedeki ilk 30 klipten alındı; sıralama (en yeni/popüler) garanti değil, medyanlar örnekleme kaydırmasına açık.
- Google Trends: sayfa 200 verdi ama JS tabanlı; bu görevde veri çıkarılmadı.
- Instagram, Facebook ve Reels sayıları alınamadı (bu ortamda test edilmedi; repo K-013'e göre sınırlı).
- Birçok kaynak taraflı: Kapwing, AutoClips, AtlasCloud, Revid, Fiverr/Gumroad satıcıları, DogPack basın bülteni. Rakip özel verisi (retention, gelir) bilinmiyor; gelir hesaplanmadı.
- Neural Viz ve Fruit Love Island ayrıntıları ikincil kopyalardan (WIRED özeti, haber özetleri).
- "Wrong Channel TV" gibi arama özetinde önerilen hesaplar doğrulanamadı (TikTok'ta sıfır takipçili aynı adlı hesap, YouTube'da başka kanal) ve tabloya alınmadı.
- 2D, kil, anime AI komedi için büyük örnek bulunamadı; bu bulgu aramanın sınırıdır, imkânsızlık kanıtı değildir.

## 14. Kaynaklar (görülme tarihi: 2026-11-27, aksi belirtilmedikçe)

Birincil sayfalar: https://www.youtube.com/@NeuralViz · /@BandarApnaDost · /@chloevshistory · /@thedorbrothers · /@tailbitpets · /@meowtakeover · /@grannyspills · /@basincreekretirement · /@infiniteunreality · /@alexey_pigeon · /channel/UCYbvkLfnQS8983p8xj24emQ · /channel/UCBmYV0_-7m0OeryGSeQ72ZQ · /channel/UCJz2R2Uue_u5_SWxnwsTXdA; https://www.tiktok.com/@meowtakeover · @mpminds · @grannyspills · @tailbitpets · @alexey_pigeon · @neuralviz · @yetivloglife · @infiniteunreality · @basincreekretirement · @veo3aimemes · @hashem.alghaili; https://www.youtube.com/oembed (Neural Viz video başlığı doğrulaması).

İkincil/arama: Kapwing AI slop raporu https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/ ; Kapwing Bigfoot https://www.kapwing.com/resources/what-it-takes-to-make-viral-ai-video-content-we-asked-bigfoot/ ; Business Standard (repo Kart 8); The Star https://www.thestar.com.my/lifestyle/entertainment/2026/04/08/ai-generated-fruit-love-island-takes-tiktok-by-storm ; Tubefilter https://tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/ ; IBTimes https://www.ibtimes.co.uk/youtube-cracks-down-ai-generated-content-1800213 ; The Hustle https://thehustle.co/news/how-mans-best-friend-became-mans-favorite-podcaster ; Webull basın bülteni https://www.webull.com/news/15866099234413568 ; Nomusica https://www.nomusica.com/this-ai-made-street-interview-is-so-real-people-cant-believe-its-fake/ ; TechCrunch https://techcrunch.com/2023/02/06/ai-generated-seinfeld-suspended-on-twitch-for-ai-generated-transphobic-jokes/ ; Newswav https://newswav.com/article/ai-generated-sitcoms-are-making-waves-on-tiktok-A2507_rpUYg0 ; CBS araştırması https://www.cbs.dk/en/articles/ai-labels-reduce-social-media-engagement ; PJ Ace X paylaşımı https://x.com/PJaccetturo/status/1931960645345501333 ; Neural Viz WIRED kopyası https://celebsover50.pages.dev/story/the-future-of-ai-media-parody-of-the-apocalypse-guy-named-josh (ikincil kopya); repo: `istihbarat/rakip-analizleri/2026-11-27-ilk-tarama.md`.

## 2026-11-28 ek: konuşmasız AI hayvan pazarı — ölçülmüş (G-0048)

- Görev: G-0048 (A0, kredi 0) · Hazırlayan: pazar-istihbarati · Ölçüm: `python3 -I scripts/hesap_olc.py youtube|tiktok ...`, **2026-11-27 22:12–22:15 UTC** (başlıktaki 11-28 görev tarihidir). Ek sayfa metni okuması: `curl` ile hesapların YT açıklaması / TT bio alanı (aynı saat aralığı).
- Etiketler: ÖLÇTÜM = araç/curl çıktısı, sayfa metni dahil. OKUDUM-ÖZET = arama özeti (veri değil, ipucu). TAHMİN. **GÖRDÜM hiçbir satırda yok: hiçbir video izlenmedi, ses dinlenmedi.**

**Önce bilinen hatalar ve sınırlar**
1. "Konuşmasız" sütunu hiçbir hesapta doğrulanmadı (video izlenmedi). Üç hesapta yalnız haber özeti var, kalanı "bilinmiyor".
2. "AI kanıtı"nın çoğu hesabın kendi beyanı değil, üçüncü taraf haber/blog. En az üç hesapta kanıt zayıf ya da tersi (aşağıda: tailbitpets, officialdivingdog, HasanAi202).
3. **TikTok sayısı yalnızca embed sayfasındaki son ~10 klibe dayanır** (araç tarafından). Sabitlenmiş klipler araçta **tahmini** (başta en çok 3 klip, ardından daha yeni klip varsa). Araç `en yüksek/medyan` oranını sabitlenmişleri çıkarıp hesaplıyor; sabitlenmişler çoğu hesapta asıl viral klip. Bu yüzden tabloda sabitlenmişlerin izlenmesini ayrı yazdım.
4. YouTube Shorts sırası garanti değil (araç "genelde en yeni ~30–48"); YT'de sabitleme ayrılamıyor ve tarih okunmuyor.
5. **Büyüme ölçülemedi.** Elimizde tek kesit var; zaman serisi yok. Hiçbir hesaba "büyüyor" yazılmadı. Eski takipçi sayıları (haber) tarihli/ölçülmemiş.
6. Yeni aday hedefi (10) tutmadı: WebSearch hesap adı/handle vermedi (bkz. "Yeni adaylar"). Instagram ölçülmedi (kapalı).
7. Aynı adlı YT/TT sayfalarının aynı kişi olduğu çoğunlukta doğrulanamadı (bkz. "Kimlik notu").

### Durum kuralı (yalnız ölçülebilen veri)
- **çökmüş:** hesap/içerik ölçümde yok ya da yeni klip yarısının medyanı eski yarının <%5'i (n≥8, sıra varsayımıyla).
- **durgun:** TT'de en yeni klip 90 günden eski (video kimliğinden tarih, araç) ya da yeni/eski yarı oranı <0,2.
- **büyüyor:** zaman serisi olmadığı için hiçbir satıra verilemedi.
- Aksi hâlde **bilinmiyor**. "Aktif" yalnızca "son klip tarihi" olarak yazıldı.

### Ölçüm tablosu
Sütunlar: hesap (URL) · platform · takipçi/abone · son klip medyanı (n) · medyan/takipçi · en yüksek/medyan (TT'de sabitlenmişsiz) · sabitlenmiş klip izlenmeleri (TT, tahmini) · AI kanıtı · konuşmasız kanıtı · durum. `—` = okunamadı/yok. TT medyanı sabitlenmişleri çıkarır. Takipçi sayıları ölçüm anı; YT abone sayısı yuvarlak (3 anlamlı hane).

| hesap | pl. | takipçi | son klip medyanı | med/takipçi | yüksek/med | sabitlenmiş | AI kanıtı | konuşmasız | durum |
|---|---|---|---|---|---|---|---|---|---|
| [@BandarApnaDost](https://www.youtube.com/@BandarApnaDost) | YT | 3.960.000 | 5.750.000 (n=48) | 1,45 | 25,0× | araç ayırmıyor | YT açıklaması: "write original prompts and use AI tools" (hesap beyanı, ÖLÇTÜM-sayfa metni); Kapwing (OKUDUM-ÖZET) | Haber: "no talking" (OKUDUM-ÖZET) | bilinmiyor (tek kesit) |
| [@BandarApnaDost](https://www.tiktok.com/@BandarApnaDost) | TT | 10 | ölçülemedi | — | — | — | aynı adlı sayfa, kimlik eşleşmesi doğrulanamadı (bkz. kimlik notu) | — | bilinmiyor (klip izlenmesi okunamadı) |
| [@meowtakeover](https://www.youtube.com/@meowtakeover) | YT | 25.200 | 22.500 (n=48) | 0,893 | 93,3× | araç ayırmıyor | KnowYourMeme "AI Kittens Dancing" (OKUDUM-ÖZET); hesabın kendi beyanı yok | KYM: müzikli (OKUDUM-ÖZET) | bilinmiyor (tek kesit) |
| [@meowtakeover](https://www.tiktok.com/@meowtakeover) | TT | 2.628.915 | 1.069.250 (n=10) | 0,407 | 2,5× | 108.900.000 / 32.800.000 / 73.100.000 | ↑ aynı hesap | ↑ | bilinmiyor (tek kesit; aktif, son klip 2026-11-27) |
| [@MPMinds_](https://www.youtube.com/@MPMinds_) | YT | 1.320.000 | 17.500 (n=48) | 0,013 | 10,9× | araç ayırmıyor | KYM/Daily Dot (OKUDUM-ÖZET); hesap beyanı yok | KYM (OKUDUM-ÖZET) | durgun (yeni/eski 0,15) |
| [@MPMinds_](https://www.tiktok.com/@MPMinds_) | TT | 0 | ölçülemedi | — | — | — | aynı adlı sayfa, kimlik eşleşmesi doğrulanamadı (bkz. kimlik notu) | — | bilinmiyor (klip izlenmesi okunamadı) |
| [@mpminds](https://www.youtube.com/@mpminds) | YT | 28 | ölçülemedi | — | — | araç ayırmıyor | aynı adlı sayfa, kimlik eşleşmesi doğrulanamadı (bkz. kimlik notu) | — | bilinmiyor (klip izlenmesi okunamadı) |
| [@mpminds](https://www.tiktok.com/@mpminds) | TT | 1.352.685 | 4.414 (n=10) | 0,003 | 1,4× | 52.100.000 / 51.400.000 | ↑ aynı hesap | ↑ | bilinmiyor (tek kesit; aktif, son klip 2026-10-28) |
| [@tailbitpets](https://www.youtube.com/@tailbitpets) | YT | 153.000 | 65.500 (n=48) | 0,428 | 58,0× | araç ayırmıyor | **Doğrulanmadı**: bio "Original creator of the viral nervous dog videos", AI demiyor; yalnız Daily Dot yorumcu şüphesi (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@tailbitpets](https://www.tiktok.com/@tailbitpets) | TT | 856.739 | 12.550 (n=10) | 0,015 | 4,0× | 7.500.000 / 36.100.000 / 49.300.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit; aktif, son klip 2026-11-27) |
| [@officialdivingdog](https://www.youtube.com/@officialdivingdog) | YT | 21 | 384 (n=8) | 18,29 | 10,7× | araç ayırmıyor | **AI kanıtı yok; tersi işaret**: bio "Remembering Chief the Diving Dog 2014-2025" (anma), sabitli klip 2022 tarihli (video kimliğinden) → gerçek köpek hesabı olması muhtemel (TAHMİN) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@officialdivingdog](https://www.tiktok.com/@officialdivingdog) | TT | 154.231 | 5.266 (n=8) | 0,034 | 4,5× | 3.391 / 34.000 / 8.500.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit; aktif, son klip 2026-10-26) |
| [@pablo.prompt](https://www.youtube.com/@pablo.prompt) | YT | — | ölçülemedi | — | — | araç ayırmıyor | Bio: "AI Video Creator / Educador en AI Videos" (hesap beyanı); hayvan klibi içeriği doğrulanmadı | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@pablo.prompt](https://www.tiktok.com/@pablo.prompt) | TT | 269.595 | 103.000 (n=9) | 0,382 | 15,5× | 8.200.000 / 5.100.000 / 846.400 | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit; aktif, son klip 2026-11-26) |
| [@cat_tommmy](https://www.youtube.com/@cat_tommmy) | YT | 209 | 50 (n=18) | 0,239 | 200,0× | araç ayırmıyor | Hesap beyanı yok; "AI Cat Stories" haber özeti (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@cat_tommmy](https://www.tiktok.com/@cat_tommmy) | TT | 360.200 | 4.853 (n=10) | 0,013 | 1,5× | 16.800.000 / 7.900.000 / 7.300.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-11-22, 370 gün) |
| [@chubbycat_1](https://www.youtube.com/@chubbycat_1) | YT | 6 | 29 (n=3) | 4,83 | 1,2× | araç ayırmıyor | Hesap adı "Chubby Cat Ai" (beyan, zayıf); TikTok AI etiketi arama özeti (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | bilinmiyor (n<8) |
| [@chubbycat_1](https://www.tiktok.com/@chubbycat_1) | TT | 4.911.945 | 4.450.000 (n=10) | 0,906 | 11,8× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-12-11, 351 gün) |
| [@aibeaststudio](https://www.youtube.com/@aibeaststudio) | YT | — | ölçülemedi | — | — | araç ayırmıyor | Hesap adı "Ai Beast"; bio kurs satıyor (taraflı, beyan zayıf) | bilinmiyor (izlenmedi) | bilinmiyor (klip izlenmesi okunamadı) |
| [@aibeaststudio](https://www.tiktok.com/@aibeaststudio) | TT | 1.488.305 | 140.200 (n=10) | 0,094 | 27,1× | 34.300.000 / 88.200.000 / 39.600.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | çökmüş (yeni yarı/eski yarı medyan 0,03) |
| [@storyarcpaws](https://www.youtube.com/@storyarcpaws) | YT | 550.000 | 674.500 (n=48) | 1,23 | 274,3× | araç ayırmıyor | Yalnız Medium özeti (OKUDUM-ÖZET, zayıf); kanal metni AI demiyor | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@storyarcpaws](https://www.tiktok.com/@storyarcpaws) | TT | 2 | 41 (n=1) | 20,50 | 1,0× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (n<8) |
| [@funntastic_AI](https://www.youtube.com/@funntastic_AI) | YT | 572.000 | 47.000 (n=29) | 0,082 | 2,1× | araç ayırmıyor | NPR: yapımcı kendi beyanı (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@funntastic_AI](https://www.tiktok.com/@funntastic_AI) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@HasanAi202](https://www.youtube.com/@HasanAi202) | YT | 11.900 | 6.300 (n=46) | 0,529 | 603,2× | araç ayırmıyor | Vuela (satıcı blogu, OKUDUM-ÖZET); kanal metni "micro research cameras" diyor, AI demiyor | bilinmiyor (izlenmedi) | çökmüş (yeni yarı/eski yarı medyan 0,01) |
| [@HasanAi202](https://www.tiktok.com/@HasanAi202) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@asmraiworks](https://www.youtube.com/@asmraiworks) | YT | 4 | 60 (n=3) | 15,00 | 1,4× | araç ayırmıyor | YT açıklaması "ai generated videos"; TT bio "learn how I make these" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (n<8) |
| [@asmraiworks](https://www.tiktok.com/@asmraiworks) | TT | 172.619 | 580.700 (n=10) | 3,36 | 6,9× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-07-08, 507 gün) |
| [@impossibleais](https://www.youtube.com/@impossibleais) | YT | — | ölçülemedi | — | — | araç ayırmıyor | Kanıt yok (bio boş); haber (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | bilinmiyor (klip izlenmesi okunamadı) |
| [@impossibleais](https://www.tiktok.com/@impossibleais) | TT | 170.096 | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | çökmüş (1 video kaldı; TAHMİN: içerik silinmiş) |
| [@ai.shxdda](https://www.youtube.com/@ai.shxdda) | YT | 39.200 | 9.150 (n=48) | 0,233 | 4,8× | araç ayırmıyor | YT açıklaması "AI artist" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@ai.shxdda](https://www.tiktok.com/@ai.shxdda) | TT | 0 | 3 (n=10) | — | 3,3× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (0 takipçi, 3 izlenme: büyük olasılıkla ilgisiz hesap) |
| [@SuperCatLeague](https://www.youtube.com/@SuperCatLeague) | YT | 15 | ölçülemedi | — | — | araç ayırmıyor | Guardian/Kapwing (OKUDUM-ÖZET) | bilinmiyor (izlenmedi) | çökmüş (haber: ~3,9M abone, OKUDUM-ÖZET → ölçülen 15 abone, 0 Shorts) |
| [@SuperCatLeague](https://www.tiktok.com/@SuperCatLeague) | TT | 0 | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (klip izlenmesi okunamadı) |
| [@aimeowrealm](https://www.youtube.com/@aimeowrealm) | YT | 170 | 983 (n=48) | 5,79 | 35,6× | araç ayırmıyor | YT açıklaması "Where AI meets Imagination" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@aimeowrealm](https://www.tiktok.com/@aimeowrealm) | TT | 8 | 21 (n=5) | 2,62 | 1,6× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (n<8) |
| [@kittenstoriesdaily01](https://www.youtube.com/@kittenstoriesdaily01) | YT | 846.000 | 2.100 (n=25) | 0,002 | 4,4× | araç ayırmıyor | YT açıklaması "AI-crafted" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@kittenstoriesdaily01](https://www.tiktok.com/@kittenstoriesdaily01) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@catrealmai](https://www.youtube.com/@catrealmai) | YT | 1.380.000 | 9.200 (n=48) | 0,007 | 7,8× | araç ayırmıyor | YT açıklaması "AI videos" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@catrealmai](https://www.tiktok.com/@catrealmai) | TT | 737.732 | 5.904 (n=10) | 0,008 | 3,0× | 24.200.000 / 5.500.000 / 9.000.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-11-21, 371 gün) |
| [@animalshortssb](https://www.youtube.com/@animalshortssb) | YT | 367.000 | 230 (n=48) | 0,001 | 1,8× | araç ayırmıyor | YT açıklaması "AI-generated animal videos" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@animalshortssb](https://www.tiktok.com/@animalshortssb) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@AiKittenverse](https://www.youtube.com/@AiKittenverse) | YT | 19.500 | 25.000 (n=48) | 1,28 | 3,8× | araç ayırmıyor | YT açıklaması "AI Kitten Verse… AI creativity" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@AiKittenverse](https://www.tiktok.com/@AiKittenverse) | TT | 29.449 | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (klip izlenmesi okunamadı) |
| [@satisfyingclips50](https://www.youtube.com/@satisfyingclips50) | YT | — | ölçülemedi | — | — | araç ayırmıyor | TT bio "AI ASMR videos using Google's VEO3" (hesap beyanı) | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@satisfyingclips50](https://www.tiktok.com/@satisfyingclips50) | TT | 13.866 | 2.278 (n=10) | 0,164 | 3,6× | 733.900 / 2.100.000 / 6.500.000 | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-07-27, 488 gün) |
| [@poutyfrenchie](https://www.youtube.com/@poutyfrenchie) | YT | — | ölçülemedi | — | — | araç ayırmıyor | vidIQ (OKUDUM-ÖZET); hesap beyanı yok | bilinmiyor (izlenmedi) | çökmüş (haber: 1,3M abone, OKUDUM-ÖZET → şimdi 404, ÖLÇTÜM) |
| [@poutyfrenchie](https://www.tiktok.com/@poutyfrenchie) | TT | 1.766 | 5.241 (n=10) | 2,97 | 60,1× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | durgun (son klip 2025-10-18, 405 gün) |
| [@AIanimalShorts26](https://www.youtube.com/@AIanimalShorts26) | YT | 6 | 1.400 (n=7) | 233,33 | 3,0× | araç ayırmıyor | Kanal adı (beyan zayıf) | bilinmiyor (izlenmedi) | bilinmiyor (n<8) |
| [@AIanimalShorts26](https://www.tiktok.com/@AIanimalShorts26) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@WildAIShorts](https://www.youtube.com/@WildAIShorts) | YT | 12 | 1.300 (n=17) | 108,33 | 3,8× | araç ayırmıyor | Kanal adı (beyan zayıf) | bilinmiyor (izlenmedi) | çökmüş (yeni yarı/eski yarı medyan 0,01) |
| [@WildAIShorts](https://www.tiktok.com/@WildAIShorts) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@Yellowchicksss](https://www.youtube.com/@Yellowchicksss) | YT | 3.140.000 | 55.000 (n=31) | 0,018 | 43,6× | araç ayırmıyor | Hesap beyanı yok (açıklama "kids channel… rhymes"); eğitim videosu özetleri (OKUDUM-ÖZET, taraflı) | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@Yellowchicksss](https://www.tiktok.com/@Yellowchicksss) | TT | 0 | ölçülemedi | — | — | — | aynı adlı sayfa, kimlik eşleşmesi doğrulanamadı (bkz. kimlik notu) | — | bilinmiyor (klip izlenmesi okunamadı) |
| [@wild-alarm](https://www.youtube.com/@wild-alarm) | YT | 713.000 | ölçülemedi | — | — | araç ayırmıyor | YT açıklaması "brought to life through the power of AI" (hesap beyanı) | bilinmiyor (izlenmedi) | bilinmiyor (klip izlenmesi okunamadı) |
| [@wild-alarm](https://www.tiktok.com/@wild-alarm) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@zero_qq-s4k](https://www.youtube.com/@zero_qq-s4k) | YT | 35.800 | 2.050 (n=48) | 0,057 | 322,9× | araç ayırmıyor | YT açıklaması AI restoran reklamı (hesap beyanı) — **hayvan değil, kapsam dışı** | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit) |
| [@zero_qq-s4k](https://www.tiktok.com/@zero_qq-s4k) | TT | — | ölçülemedi | — | — | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | hesap bulunamadı (404/10221; bu platformda bu adla yok) |
| [@savannahrush](https://www.youtube.com/@savannahrush) | YT | — | ölçülemedi | — | — | araç ayırmıyor | aynı adlı sayfa, kimlik eşleşmesi doğrulanamadı (bkz. kimlik notu) | — | bilinmiyor (klip izlenmesi okunamadı) |
| [@savannahrush](https://www.tiktok.com/@savannahrush) | TT | 725 | 640 (n=10) | 0,883 | 1,5× | — | ↑ aynı hesap | bilinmiyor (izlenmedi) | bilinmiyor (tek kesit; aktif, son klip 2026-11-27) |
**Kimlik notu (aynı adlı YT/TT eşleşmesi).** Doğrulandı (iki sayfanın kendi metni): MPMinds = TT `@mpminds` + YT `@MPMinds_` (ikisinde de aynı iş e-postası), tailbitpets = TT + YT (aynı bio "Official Home of Rufus & TailBitPets"). **Doğrulanamadı:** meowtakeover TT bio İspanyolca/İngilizce (e-posta meowtakeover@gmail.com) iken YT açıklaması Arapça ("Meowtakeover official account" + "بساس جدة", Cidde kedileri) → farklı sahip olabilir; cat_tommmy, Bandar (TT 10 takipçi), Yellowchicksss (TT sıfır), savannahrush (TT 725 takipçi; haberdeki kanalla aynı olduğu belli değil) da doğrulanamadı. Tablodaki "aynı adlı sayfa" satırları ilgisiz hesap olabilir; istatistiklere girmedi.

### Özet istatistikler (n≥8 klip ve ≥1.000 takipçi şartı; kapsam dışı: officialdivingdog [gerçek köpek hesabı olması muhtemel], zero_qq-s4k [reklam, hayvan değil])

| | YouTube (13 hesap) | TikTok (11 hesap) |
|---|---|---|
| Son klip medyanlarının medyanı | **22.500** | **12.550** |
| medyan/takipçi, hesaplar arası medyan | 0,233 | 0,164 (ASMR 2 hesap hariç 9 hesapta 0,094) |
| "Sağlıklı" (med/takipçi ≥0,1 **ve** yüksek/med ≤10) | **2/13**: ai.shxdda (39K abone), AiKittenverse (19,5K) | **3/11**: meowtakeover (aktif); asmraiworks ve satisfyingclips50 (ASMR, **ikisi de >480 gün durgun**) |
| "Tek viral" (yüksek/med >10) | **7/13** (Bandar 25×, meowtakeover-YT 93×, MPMinds_ 10,9×, tailbitpets-YT 58×, storyarcpaws 274×, HasanAi202 603×, Yellowchicksss 44×) | **4/11** sabitlenmişsiz (pablo.prompt 15,5×, chubbycat_1 11,8×, aibeaststudio 27×, poutyfrenchie 60×); **sabitlenmişler dahil 10/11** (yalnız asmraiworks ≤10) |
| Ne sağlıklı ne tek viral | 4 (funntastic, kittenstoriesdaily01, catrealmai, animalshortssb: hepsinde med/abone ≤0,082) | 4 (mpminds, tailbitpets, cat_tommmy, catrealmai: hepsinde med/takipçi ≤0,015) |

Notlar: "sağlıklı" eşiği kullanıcının tanımıdır. Sabitlenmişler dahil edilince TT'de sağlıklı sayısı 1/11'e düşer ve o da durgundur. Yüksek/medyan >10 eşiği "tek viral" tanımı olarak benim eklememdir (skill'in ≥3 şüphe eşiği ayrıca geçerli).

### Yeni adaylar (WebSearch, ≤10) ve sonuç
WebSearch hiçbir sorguda doğrulanabilir "konuşmasız AI hayvan" handle listesi vermedi; adlar haber/rehber özetlerinden geldi, handle'ı ben tahmin edip doğrudan sayfada sınadım. **Kullanılabilir ölçüm veren yalnızca 1–2:**
- **Ölçüldü ve tabloda:** Yellowchicksss (YT 3,14M abone; tutorial özetlerinde "AI chick rescue", açıklama çocuk kanalı → Anayasa 22 riski), wild-alarm (YT 713K abone, AI beyanı var, Shorts izlenmesi okunamadı), zero_qq-s4k (AI reklam kanalı, kapsam dışı).
- **Bulunamadı (404 / 10221), tabloya girmedi:** la.team.france, the_hamster_rave, dramacatuniverse, meowziqi, chickofhonor (TT'de 0 takipçi/1 video, YT 404), aijestdaily. **Kimlik doğrulanamadı:** savannahrush, AIWildWonders (YT 3 abone, haberdeki ~192K abonelik kanal başka ID), autoscope (YT 56, TT 1,6K), bigyowie (TT 79 takipçi; Kapwing'in 151K'lık hesabı değil).
- Bu satırlar uydurma değil, ama "pazar örneği" de sayılamaz. Hedef (10 yeni ölçülmüş aday) **karşılanmadı**.

### Başarısız / küçülmüş / kaybolmuş örnekler (hayatta kalma yanlılığı)
- YT @SuperCatLeague: haber ~3,9M abone (OKUDUM-ÖZET) → ölçülen 15 abone, 0 Shorts (ÖLÇTÜM). YT @poutyfrenchie: haber 1,3M abone → 404 (TT'de 1.766 takipçili aynı adlı hesap var, kimlik ?).
- TT @impossibleais: 170.096 takipçi, **1 video** (içerik silinmiş olabilir, TAHMİN). TT @satisfyingclips50: sabitlenmiş klipler 6,5M/2,1M/0,7M ama takipçi 13.866, medyan 2.278, son klip 2025-07-27.
- Abonesi var, izleyicisi yok (YT): kittenstoriesdaily01 846K abone / medyan 2.100 (0,002); animalshortssb 367K / 230 (0,001); catrealmai 1,38M / 9.200 (0,007); Yellowchicksss 3,14M / 55.000 (0,018); MPMinds_ 1,32M / 17.500 (0,013).
- chubbycat_1: 4,9M takipçi, son klip medyanı 4,45M (0,906, ölçülen en güçlü klip başı performans) ama **son klip 2025-12-11 (351 gün önce)**; 28 video. Büyük ama 11,5 aydır sessiz.
- Kimin silindiği/kapatıldığı (platform mu sahibi mi) ölçümle ayrılamıyor.

### 5 ders (her biri hesap sayısıyla)
1. **Takipçi sayısı izleyici sayısı değildir.** Ölçülen 24 hesap-platform çiftinin 9'unda med/takipçi <0,02 (YT 5/13, TT 4/11). Takipçisi >500K olan 13 çiftte (YT 7, TT 6) "sağlıklı" tanımını geçen yalnız 1 (TT meowtakeover). Kanıt: ÖLÇTÜM, 24 çift.
2. **Büyük görünen sonuçların çoğu tek viral klibe dayanıyor; TikTok'ta bu sabitlenmiş klipte saklı.** YT'de 7/13, TT'de sabitlenmişler dahil 10/11 hesap yüksek/medyan >10. TT'de sabitlenmişsiz oran medyanı 4,0×, sabitlenmişli 629×. Örn. mpminds: sabitlenmiş 52,1M ve 51,4M, son 10 klibin medyanı 4.414. Kanıt: ÖLÇTÜM; "sabitlenmiş" araç tahmini (TAHMİN katmanı).
3. **Hesapların yarısından fazlası sessizleşmiş.** TT'de 11 hesaptan 6'sında son klip >90 gün önce (chubbycat_1 351 gün, cat_tommmy 370, catrealmai 371, satisfyingclips50 488, asmraiworks 507, poutyfrenchie 405). Aktif 5: meowtakeover, mpminds, tailbitpets, pablo.prompt, aibeaststudio. Kanıt: tarih video kimliğinden (araç), embed örneği en yeni klipleri veriyor varsayımıyla (meowtakeover'da doğrulandı); neden bilinmiyor.
4. **Platformlar arası aktarım ölçülen çiftlerde yok, yönü de tek değil.** Kimliği doğrulanmış 2 çift: MPMinds (TT 1,35M takipçi / son klip medyanı 4.414; YT 1,32M abone / 17.500) ve tailbitpets (TT 857K / 12.550; YT 153K / 65.500): ikisinde de YT'nin klip başı medyanı TT'den yüksek. "TT 2,63M vs YT 25,2K" (meowtakeover) farkı ise kimliği doğrulanamayan çifte dayanıyor. Kanıt: ÖLÇTÜM, 2 doğrulanmış çift (az); TT medyanı yalnız 10 klip.
5. **"AI + konuşmasız" etiketi çoğu hesapta kanıtsız.** Tabloda adı geçen hesaplardan, hesabın kendi beyanı olan 12 (Bandar, asmraiworks, ai.shxdda, aimeowrealm, kittenstoriesdaily01, catrealmai, animalshortssb, AiKittenverse, satisfyingclips50, pablo.prompt, wild-alarm, zero_qq-s4k) ve hesap adında "AI" geçen 4 (chubbycat_1, aibeaststudio, AIanimalShorts26, WildAIShorts); tailbitpets, storyarcpaws, HasanAi202, officialdivingdog, cat_tommmy'de beyan yok; officialdivingdog'da anma bio'su ve 2022 tarihli sabitlenmiş klip var (gerçek köpek, TAHMİN). Konuşmasız: 0 hesap GÖRDÜM. Kanıt: ÖLÇTÜM (bio metni), sayılar bu listeyle sınırlı.

### Önceki iki rapor (G-0030 ana rapor + k029 pilotları) ile karşılaştırma

| Önceki bulgu | Sonuç | Dayanak |
|---|---|---|
| "TikTok hesaplarında medyan ölçülemedi" (pilot sınırı) | **Giderildi** | 11 TT hesabında n≥8 (bu ek) |
| Takipçi ≠ izlenme (MPMinds 0,013, catrealmai 0,007, kittenstories 0,002, animalshortssb 0,0006) | **Doğrulandı**, TT'ye de genişledi | YT sayıları aynı gün yeniden ölçüldü, uyuştu; TT: mpminds 0,003, cat_tommmy 0,013, catrealmai 0,008, tailbitpets 0,015 |
| En yüksek/medyan 25–603× (Bandar 25, meowtakeover-YT 95, storyarcpaws 274, HasanAi202 603) | **Doğrulandı** (93,3×, 25,0×, 274,3×, 603,2×) ve TT'de sabitlenmişlerle daha da büyük | tek viral bağımlılığı |
| "HasanAi202 çökmüş (TAHMİN)" | **Kısmen doğrulandı**: yeni klip yarısı/eski yarı = 0,01; TT'de hesap yok. Sıra varsayımı ve yeni klip yaşı yanlılığı kalıyor | n=46 |
| "TikTok'ta format YouTube'dan çok daha iyi" (meowtakeover TT 2,63M vs YT 25K; pilot ders 1) | **Kısmen çürütüldü / belirsiz**: kimliği doğrulanan 2 çiftte YT klip başı medyanı TT'den yüksek; meowtakeover eşleşmesi doğrulanamadı | bkz. ders 4 |
| "Tek platforma bakarak karar verilmemeli" | **Destekleniyor** (iki platform ölçmek farkı gösterdi) | — |
| "Platform riski gerçek (Super Cat League sıfırlandı)" | **Ölçüm yeniden doğruladı** (15 abone, 0 Shorts), neden hâlâ OKUDUM-ÖZET; Pouty Frenchie YT 404 | — |
| "tailbitpets = gerçekçi AI köpek" (G-0030 satır 6) | **Doğrulanamadı**: bio yaratıcıyı "viral nervous dog videos'un orijinal yaratıcısı" diye tanıtıyor, AI demiyor; AI kanıtı tek haber şüphesi. G-0030'daki "fotogerçekçi insan-dışı AI karakter en büyük ölçek" çıkarımı bu hesapta AI kanıtı olmadan duruyor | ders 5 |
| "officialdivingdog = AI olimpiyat atlama akımı hesabı" (pilot yedek aday) | **Çürütüldü (TAHMİN düzeyinde güçlü)**: anma bio'su, 2022 sabitlenmiş klip | bio + video kimliği tarihi |
| "funntastic_AI durgun (572K, medyan 47K, 0,08)" | **Sayı doğrulandı** (47.000; 0,082); "büyümüyor/düşüyor" yargısı zaman serisi olmadığı için hâlâ TAHMİN. TT'de hesap yok (10221) doğrulandı | n=29 |
| "impossibleais 1 video / satisfyingclips50 viral takipçiye dönmedi" | **Doğrulandı** (1 video; 13.866 takipçi, medyan 2.278) | — |
| "Sağlıklı: Bandar 25×, AiKittenverse 3,8×" (pilot ders 2) | **Düzeltme:** Bandar tanıma göre sağlıklı değil (25×>10); AiKittenverse ve ai.shxdda sağlıklı ama küçük (<40K) | tablo |
| "Mat/soluk 3D için pazar kanıtı yok" (G-0030 §8) | **Bu ölçüm konuyla ilgili değil** (stil ölçülmedi) | — |

### Araştırma kısıtları
- TikTok embed örneği ~10–15 klip; sabitlenmişler tahmini; takipçi dışı etkileşim (paylaşım, tamamlama) ölçülemez. Gelir hiçbir hesap için hesaplanmadı (rakip özel verisi yok).
- YouTube Shorts tarih/sabitleme vermiyor; sıralama varsayım.
- Instagram/Facebook ölçülmedi. Videolar izlenmedi; AI etiketi (TikTok) klip düzeyinde araçta okunmuyor.
- Kapwing, KYM, Daily Dot, NPR, vidIQ, Medium, FluxNote, Vuela, Deevid gibi kaynakların bir bölümü taraflı (araç/kurs satıcısı) ve yalnız özetle okundu.
- aibeaststudio ve asmraiworks bio'larında kurs/eğitim satışı var (taraflı hesaplar; kendi başarılarını pazarlıyor olabilirler).

SKILL: pazar-istihbarati-olcum v1

## 2026-11-28 ek: konuşmasız insan yapımı animasyon kıyası (G-0051)

- Görev: G-0051 (A0, kredi 0) · Hazırlayan: pazar-istihbarati · Ölçüm: `python3 -I scripts/hesap_olc.py youtube|tiktok ...`, **2026-11-27 22:27–22:29 UTC** (başlıktaki 11-28 görev tarihidir). Hesap açıklaması/bio okuması: `curl` (aynı saat). Soru: konuşmasız/az konuşmalı, tek şakalı, karakterli kısa animasyon formatı AI olmadan da çalışıyor mu?
- Etiketler: ÖLÇTÜM = araç/curl çıktısı. OKUDUM-ÖZET = arama özeti (ipucu, veri değil). TAHMİN. **GÖRDÜM hiçbir satırda yok: hiçbir video izlenmedi, ses dinlenmedi.**
- "Sağlıklı" tanımı G-0048'den aynen: medyan/takipçi >= 0,1 **ve** en yüksek/medyan <= 10. "Tek viral" = en yüksek/medyan > 10. TikTok'ta ikisi de sabitlenmişsiz (araç varsayılanı) ve sabitlenmiş dahil yazıldı.

**Önce bilinen hatalar ve sınırlar**
1. **"Konuşmasız" kanıtı hiçbir hesapta ölçümle doğrulanmadı.** Hesap beyanı (YT açıklaması/TT bio) hiçbirinde konuşmasızlıktan söz etmiyor (ÖLÇTÜM, 6 YT açıklaması + 3 TT bio okundu). Kiwisburnttoast için yalnız Cartoon Brew arama özeti ("almost no dialogue", OKUDUM-ÖZET). Filmbilder/Animanimals için arama özeti "dialogue-free" (OKUDUM-ÖZET; kanal başka sanatçıların işlerini de gösteriyor, Shorts içeriği izlenmedi). Simon's Cat, Shaun the Sheep, Mr Bean için bu görevde kaynak okumadım: "konuşmasız" genel bilgi, **TAHMİN**. Wikipedia'ya bu ortamda erişilemedi (curl 000). Lazy Square için "konuşmasız mı" bilinmiyor.
2. **Aday sayısı hedefi (10-15) tutmadı.** WebSearch yalnız birkaç handle verdi; handle'ı tahmin edip körlemesine ölçmedim. Sınanan her tahmin kimlik kontrolüyle (bio/açıklama) tabloya girdi ya da düşürüldü. Ölçülen insan yapımı hesap: 5 resmî-marka satırı + 3 bağımsız hesap (+1 sesli bağımsız, karşılaştırma dışı).
3. **Bağımsız grup n=3 hesap (YT 3 + TT 1 çift). Bu bir pazar örneklemi değil; ucu ucuna "var/yok" kanıtı.** Üstelik üçü de basın/blog'da çıktığı için bulundu: hayatta kalma yanlılığı güçlü. Küçük/kapanmış insan yapımı konuşmasız hesap için **ölçülebilir aday bulamadım** (bkz. aşağı).
4. TikTok sayıları embed sayfasındaki son 10-13 klibe dayanır; **aynı dakikada iki okuma farklı örnek verebiliyor** (javadoodles TT medyanı 7.797 ve 24.200). Sabitlenmişler araçta tahmini (TAHMİN katmanı). YT Shorts sıralaması ve tarihi okunamıyor: YT "son klip tarihi" yazılamadı.
5. Büyüme ölçülemedi (tek kesit). Kimse "büyüyor" diye işaretlenmedi. Gelir hesaplanmadı.

### Ölçüm tablosu
Sütunlar: hesap (URL) · tür · platform · takipçi/abone · son klip medyanı (n) · min-max (YT) / en yüksek (TT) · med/takipçi · yüksek/med (TT: sabitlenmişsiz → dahil) · son klip tarihi · konuşmasız kanıtı · kimlik/not. Ölçüm zamanları: YT 22:27:29-22:28:22Z, TT 22:27:32-22:29:08Z.

**A. Resmî marka (bilinirlik etkisi var)**

| hesap | tür | pl. | takipçi | medyan (n) | min-max/en yüksek | med/tak. | yüksek/med | son klip | konuşmasız kanıtı | not |
|---|---|---|---|---|---|---|---|---|---|---|
| [@simonscat](https://www.youtube.com/@simonscat) | resmî marka | YT | 6,64M | 77.000 (48) | 13.000-3.000.000 | 0,012 | 39,0× | okunamadı | TAHMİN (kaynak okunmadı) | açıklama "animated series... Simon's Cat Shorts" (ÖLÇTÜM) |
| [@simonscat](https://www.tiktok.com/@simonscat) | resmî marka | TT | 4.338.688 | 9.838 (10) | en yüksek 194.200 | 0,002 | 19,7× → dahil 2.243× (sabitlenmiş 26,8M ve 597.900, TAHMİN) | 2026-11-27 (aralık 11-17..11-27) | TAHMİN | bio "Official TikTok! ... By Simon Tofield", doğrulanmış rozet (ÖLÇTÜM). `@simonscatofficial` TT'de yok (10221) |
| [@ShaunTheSheepOfficial](https://www.youtube.com/@ShaunTheSheepOfficial) | resmî marka | YT | 14M | 68.000 (47) | 26.000-225.000 | 0,005 | 3,3× | okunamadı | TAHMİN | açıklama "official Shaun the Sheep YouTube channel" (ÖLÇTÜM). `@shaunthesheep` YT'de 404 |
| [@ShaunTheSheepOfficial](https://www.tiktok.com/@ShaunTheSheepOfficial) | resmî marka | TT | 1.451.350 | **ölçülemedi** | — | — | — | — | TAHMİN | embed sayfası HTTP 400 / hata 10221 (aşılmadı). Bio "Shaun's official TikFlock", doğrulanmış. Aynı adlı `@shaunthesheep` TT'de 35 takipçi, 0 video: ilgisiz |
| [@mrbean](https://www.youtube.com/@mrbean) | resmî marka, **karma (canlı çekim + animasyon)** | YT | 36,2M | 34.500 (48) | 5.800-176.000 | 0,001 | 5,1× | okunamadı | TAHMİN | açıklama "Official Mr Bean YouTube Channel... classic series... new animated adventures" (ÖLÇTÜM); animasyon payı bilinmiyor |
| [@mrbean](https://www.tiktok.com/@mrbean) | resmî marka, karma | TT | 7.879.740 | 141.550 (10) | en yüksek 1.200.000 | 0,018 | 8,5× (sabitlenmiş yok) | 2026-11-27 (11-21..11-27) | TAHMİN | bio "official home of Mr Bean on TikTok", doğrulanmış |

**B. Bağımsız / küçük stüdyo (bilinirlik etkisi daha az)**

| hesap | tür | pl. | takipçi | medyan (n) | min-max/en yüksek | med/tak. | yüksek/med | son klip | konuşmasız kanıtı | not |
|---|---|---|---|---|---|---|---|---|---|---|
| [@filmbilder](https://www.youtube.com/@filmbilder) | bağımsız stüdyo (Stuttgart), kanal başka sanatçıları da gösterir | YT | 2,0M | 68.500 (26) | 5.000-429.000 | 0,034 | 6,3× | okunamadı | OKUDUM-ÖZET (Animanimals "dialogue-free") | açıklama "studio in Stuttgart... independent films" (ÖLÇTÜM). Handle 3. taraf izleyiciden geldi; kimlik açıklamayla doğrulandı. TT `@filmbilder`: 5 takipçi/5 video/2021, kimlik doğrulanamadı → tabloya girmedi |
| [@lazysquare](https://www.youtube.com/@lazysquare) | bağımsız tek kişi | YT | 656K | 146.000 (17) | 25.000-9.400.000 | 0,223 | 64,4× | okunamadı | **bilinmiyor** | açıklama "Alex, independent one-person studio... Lazy Square... dark-humor animation" (ÖLÇTÜM; Cartoon Brew özetiyle aynı kişi). TT `@lazysquare` (13 takipçi, 0 video) ve `@lazy_square` (79, 2019) ilgisiz → TT: aday yok |
| [@kiwisburnttoast](https://www.youtube.com/@kiwisburnttoast) | bağımsız tek kişi | YT | 102K | 165.000 (26) | 25.000-3.200.000 | 1,618 | 19,4× | okunamadı | OKUDUM-ÖZET (Cartoon Brew: "almost no dialogue", pantomim) | açıklama "I do cartoons and comics now". Handle Cartoon Brew URL adından (TAHMİN-türetme) |
| [@kiwisburnttoast](https://www.tiktok.com/@kiwisburnttoast) | bağımsız tek kişi | TT | 198.098 | 87.350 (10) | en yüksek 201.600 | 0,441 | **2,3×** → dahil 162,9× (sabitlenmiş 15,7M, 4,1M, 1,8M, TAHMİN) | 2026-11-19 (aralık 08-26..11-19) | OKUDUM-ÖZET | bio "Animator art person"; YT ile aynı kişi olduğu **doğrulanamadı** (zayıf: ad eşleşmesi) |

**C. Karşılaştırma dışı (konuşmasız değil, ses/replik çok)**

| hesap | tür | pl. | takipçi | medyan (n) | en yüksek | med/tak. | yüksek/med | not |
|---|---|---|---|---|---|---|---|---|
| [@javadoodles](https://www.youtube.com/@javadoodles) | bağımsız | YT | 2,07M | 119.500 (46) | 1.500.000 | 0,058 | 12,6× | açıklama "weird animator... adult language" (ÖLÇTÜM) + AWN: ses/diyalog odaklı (OKUDUM-ÖZET) → konuşmasız grubundan **çıkarıldı** |
| [@javadoodles](https://www.tiktok.com/@javadoodles) | bağımsız | TT | 1.230.819 | 24.200 (10; ilk okuma 7.797) | 172.100 | 0,020 | 7,1× → dahil 877× (sabitlenmiş 32,8M/10,8M/7,1M, 2022-24, TAHMİN) | örnek okumalar arası kararsız |

**Aday yok / ölçülemedi (uydurma yok):** Pingu resmî (WebSearch resmî handle vermedi; üçüncü taraf "My Pingu TV" vb. resmî değil), Mr Bean Animated ayrı kanal (handle yok), Land of Boggs (BuzzFeed; handle yok), Patrick Smith, Dominic Carola, Sydney the Song Cat, Nutshell Animations (anlatımlı; konuşmasız değil). Danny Casale: YT `@coolmancoffeedan` 404; TT'de aynı adlı hesap 179 takipçi/2 video/2018, kimlik doğrulanamadı → girmedi. Leo_claydreams (Lovart blogu, 89K): YT 404, TT 10221 → yok. Shaun the Sheep TT klip medyanı ve tüm YT son-klip tarihleri okunamadı.

### Başarısız/küçük örnekler (hayatta kalma yanlılığı)
- Ölçülebilir **küçük ya da kapanmış insan yapımı konuşmasız animasyon hesabı bulunamadı**: bu bir "yok" kanıtı değil, aramamın sınırıdır (WebSearch handle vermedi). Bağımsız grup yalnızca basında çıkanlardan oluştu → iyimser yanlı.
- Resmî markalarda "zayıf" taraf var: Mr Bean YT 36,2M abone / medyan 34.500 (0,001); Shaun YT 14M / 68.000 (0,005); Simon's Cat TT 4,34M / 9.838 (0,002). Büyük marka büyük takipçiyi izlenmeye çevirmiyor.
- Simon's Cat TT: 4,3M takipçi, son 10 klip medyanı 9.838; sabitlenmiş klip 26,8M (TAHMİN) tüm tabloyu çarpıtıyor.

### Özet istatistikler (konuşmasız/az konuşmalı insan yapımı: A + B, javadoodles hariç)

| | İnsan yapımı YT | İnsan yapımı TT | AI (G-0048) YT | AI (G-0048) TT |
|---|---|---|---|---|
| Ölçülen hesap-platform çifti | 6 (resmî 3, bağımsız 3) | 3 (resmî 2, bağımsız 1); +1 ölçülemedi | 13 | 11 |
| Son klip medyanlarının medyanı | 72.750 | 87.350 | 22.500 | 12.550 |
| medyan/takipçi, medyanların medyanı | 0,023 | 0,018 | 0,233 | 0,164 |
| "Sağlıklı" (>=0,1 ve <=10×) | **0/6** | **1/3** hariç (Kiwisburnttoast); **0/3** sabitlenmiş dahil | 2/13 (%15) | 3/11 hariç (%27); 1/11 dahil |
| "Tek viral" (>10×) | 3/6 (simonscat, lazysquare, kiwisburnttoast) | 1/3 hariç (simonscat); 2/3 dahil | 7/13 | 4/11 hariç; 10/11 dahil |

**Bilinirlik ayrımı (iki ayrı satır grubu):**

| Grup | n (çift) | medyan/takipçi, medyanların medyanı | Sağlıklı (hariç) | Tek viral (hariç) |
|---|---|---|---|---|
| Resmî marka (5 ölçülen) | 5 | **0,005** (0,001-0,018) | 0/5 | 1/5 |
| Bağımsız (4 ölçülen) | 4 | **0,332** (0,034-1,618) | 1/4 (yalnız Kiwis TT) | 2/4 (YT: lazysquare, kiwisburnttoast) |
| AI grubu (G-0048) | 24 | YT 0,233 / TT 0,164 | 5/24 | YT 7/13, TT 4/11 |

Okuma (ölçüm ve çıkarım ayrı): (ÖLÇTÜM) Resmî markalarda med/takipçi 0,001-0,018, yani AI grubunun ~30-100 katı altında; ama mutlak klip medyanı (34K-141K) AI grubunun medyanlarından (12K-22K) yüksek. Bağımsız insan yapımlarda med/takipçi AI grubuyla aynı düzeyde ya da üstünde (0,223-1,618; Filmbilder 0,034 hariç). (ÇIKARIM, TAHMİN düzeyi) Büyük markaların düşük oranı, takipçi sayısının eski bilinirlikle/TV geçmişiyle şişmesine ve Shorts/TT kitlesinin abone olmayan izleyiciden oluşmasına bağlı olabilir; ölçüm bunu ayırmıyor.

### Cevap: "Konuşmasız format kendi başına çalışır mı?"
**Kanıt düzeyi: düşük-orta; "var" yönünde zayıf, "garanti" yönünde değil.**
1. İnsan yapımı konuşmasız/az konuşmalı animasyon **çalışabiliyor** (ÖLÇTÜM): Kiwisburnttoast TT'de 198K takipçide son klip medyanı 87K (0,441, sabitlenmişsiz 2,3×, son klip 2026-11-19); YT'de 102K abonede 165K (1,6). Lazy Square 656K abonede 146K. Yani format AI olmadan da, küçük hesapta da takipçi dışı erişim alabiliyor. Konuşmasız olduğu bu görevde doğrulanmadı (OKUDUM-ÖZET/bilinmiyor).
2. **Ama "kendi başına yeter" değil:** aynı gruptaki bağımsızlarda da tek viral örüntüsü var (lazysquare 64×, kiwisburnttoast YT 19×, sabitlenmişler dahil Kiwis TT 163×), 4 çiftin 1'i "sağlıklı" (AI: 5/24). Fark AI grubundan belirgin biçimde iyi değil: bağımsız n=4 ile "AI'dan daha sağlıklı" denemez. Büyük resmî markalar sağlıklı çıkmadı (0/5): format tek başına yetmiyor, **dağıtım ve kitle oranı** belirleyici.
3. **AI vs insan sorusu:** bu ölçümde AI grubunun "sağlıklı" oranı insan yapımlardan düşük bulunmadı (AI %21, insan 1/9 = %11; n çok küçük). "AI olduğu için çalışmıyor" ya da "insan yapımı olduğu için çalışıyor" iddiasını bu veri **desteklemiyor ve çürütmüyor**.

### Bizim için 3 ders (hepsi HİPOTEZ)
1. **Medyan/takipçi, markanın gücünü değil formatın erişimini ölçer; bizim hesaplar bilinirlik avantajı olmadan başlayacak.** Bu yüzden başarı ölçütü olarak bağımsızların (0,2-1,6) ve AI grubunun medyanını (0,16-0,23) kullan; resmî markaları (0,001-0,018) hedef olarak alma. İlk 10 klipte medyan/takipçi >=0,1 ve yüksek/medyan <=10 (sabitlenmişsiz) aynı eşiği önceden yazılı başarı kriteri yap.
2. **Tek sabitlenmiş viral klibe yaslanma; sistemi "medyan klip"e kur.** Kiwis TT'de sabitlenmişsiz 2,3× ama dahil 163×; Simon's Cat 2.243×. Konuşmasız tek şaka formatında bile hesabın gerçek sağlığı sabitlenmişsiz medyanda okunur. Test planında "sabitlenmiş yok, her klip aynı ağırlıkta" ölç.
3. **Format kanıtlandı sayılmasın: en yakın doğrulama bağımsız, tek kişili, YouTube+TikTok'ta ayrı ayrı ölçülen hesaplar (Kiwisburnttoast, Lazy Square), ve bunların konuşmasızlığı doğrulanmadı.** Bora'nın izlemesiyle hangi klibin gerçekten sözsüz ve tek şakalı olduğu netleşmeden "konuşmasız format = kanıtlı" yazma. Sonraki ölçüm adımı: bu iki hesabın son 10 klibini izleyip (Bora/görüntü erişimi gerekir) sözsüz/tek şaka oranını say; handle'sı belli 5+ küçük bağımsız hesap eklemek için Bora'dan aday listesi iste.

### Araştırma kısıtları
- WebSearch yalnız birkaç handle verdi; Pingu, Mr Bean Animated, Land of Boggs, Patrick Smith, Dominic Carola, Sydney the Song Cat, Danny Casale (doğrulanamadı) ölçülemedi. Wikipedia/haber siteleri bu ortamda açılmadı.
- Instagram ölçülmedi. Videolar izlenmedi, ses dinlenmedi. YT Shorts tarihi/sabitleme okunamıyor. TikTok embed örneği 10-13 klip, okumalar arası kararsız. Shaun the Sheep TT embed hatası (aşılmadı).
- Takipçi dışı etkileşim, izlenme süresi, gelir bilinmiyor; gelir hesaplanmadı. Handle kaynakları: TikTok newsroom (simonscat), British Comedy Guide ve TikTok/Aardman duyuruları (Shaun), vidIQ (mrbean), 3. taraf izleyici (filmbilder), Cartoon Brew (lazysquare, kiwisburnttoast adları).

SKILL: pazar-istihbarati-olcum v1
