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
