# Mesleki Yöntemler — Kaynaklı Derleme (3 uzmanlık)

Tarih: 2026-11-27 · Hazırlayan: araştırma ajanı (Claude) · Durum: ham kaynak derlemesi, karar dayanağı değil (CLAUDE.md kural 3, 8)

## Önce bilinen eksikler (okumadan geçme)

- **Bu oturumda açabildiğim sayfa yalnızca `support.google.com` (YouTube Yardım) sayfaları.** arxiv.org, openaccess.thecvf.com, backlothelp.netflix.com, developers.tiktok.com, ads.tiktok.com, help.runwayml.com, openai.com, Wikipedia, dergi siteleri, crossref/openalex: **proxy 403 / ENOTFOUND** (ÖLÇTÜM: curl ve WebFetch çıktısı). `www.tiktok.com/creator-academy` 200 döndü ama sayfa JavaScript ile yükleniyor, metin gelmedi → açılmadı sayılır.
- CLAUDE.md'deki K-013 satırı TikTok/Trends'in açık olduğunu söylüyor; **bu alt oturumda TikTok yardım/geliştirici sayfaları açılmadı** (ÖLÇTÜM). Ortam farkı olabilir; ana oturum kontrol etmeli.
- Akademik makalelerin **hiçbirinin tam metnini okumadım.** Varlıklarını ve özetlerini iki yoldan doğruladım: WebSearch özeti ve Consensus veritabanı kaydı (başlık, yazar, yıl, dergi, özet metni). İkisi de **ÖZET** etiketindedir.
- Kitap, kurs, video incelemedim (Catmull "Creativity, Inc." dahil). Pixar dailies bilgisi tek bir editör röportajının arama özetinden geliyor.

Etiketler: **AÇILDI** = sayfayı curl ile indirip metnini okudum (2026-11-27) · **ÖZET** = yalnızca arama özeti / veritabanı özeti.
Kaynak türleri: resmî belge · akademik makale · uygulayıcı röportajı · eğitim · satıcı (vendor) yardım sayfası.

---

## Alan 1 — Animasyon / AI video kalite kontrolü

**1.1 İki ayrı eksende puanlama: "istenen oldu mu" ≠ "fizik doğru mu"**
- YÖNTEM: Her klip iki ayrı soruyla değerlendirilir: (a) metne/senaryoya uyum (semantic adherence), (b) fiziksel sağduyu (nesneler gerçek dünyadaki gibi davranıyor mu). İstemler malzeme etkileşimine göre gruplanır (katı-katı, katı-sıvı, sıvı-sıvı). En iyi model bile ikisini birlikte ancak %39,6 oranında tutturmuş.
- KAYNAK: Bansal vd., "VideoPhy: Evaluating Physical Commonsense for Video Generation", arXiv 2406.03520 (ilk sürüm 2024-06-05; ICLR 2025) — https://arxiv.org/abs/2406.03520 · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: QC formunda "senaryo uyumu" ve "fizik" iki ayrı sütun olur; biri geçip diğeri kalırsa klip "geçti" sayılmaz.

**1.2 Fiziği izlemeden önce yaz, sonra kontrol et**
- YÖNTEM: PhyGenBench 27 fizik yasasını 4 alanda 160 istemle test eder; değerlendirici (PhyGenEval) önce istemdeki fizik yasasını çıkarır, sonra videoyu buna göre katmanlı (üç kademeli) denetler. Yazarlara göre model büyütmek ya da istem mühendisliği dinamik (hareket/kuvvet) hatalarını çözmüyor.
- KAYNAK: Meng vd., "Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation", arXiv 2410.05363 (Ekim 2024; ICML 2025, PMLR v267) — https://arxiv.org/abs/2410.05363 · akademik makale
- ETİKET: ÖZET (katmanların tam tanımını açamadım)
- BİZE UYGULANIŞI: Klibi açmadan önce "bu sahnede ne olmalı" (ör. kapı menteşe etrafında döner, düşen nesne yere değer) maddeleri yazılır; kare kare bakış bu listeye karşı yapılır.

**1.3 "Gerçekçi görünüyor" fizik kanıtı değildir**
- YÖNTEM: Physics-IQ, 66 senaryoda 396 gerçek videonun başını modele verip devamını tahmin ettirir; bulgu: fiziksel anlama sınırlı ve **görsel gerçekçilikle ilişkisiz**. Repo, yerine "Physics-IQ Verified" sürümünü önerir.
- KAYNAK: Motamed vd., "Do Generative Video Models Understand Physical Principles?", arXiv 2501.09038 (Ocak 2025; WACV 2026) — https://arxiv.org/abs/2501.09038 · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Bekçi/ajan değerlendirmesinde "çok gerçekçi duruyor" cümlesi QC gerekçesi olarak kabul edilmez; temas anı ayrıca incelenir.

**1.4 Kaliteyi boyutlara ayır; hatayı kategori + zaman + konumla kaydet**
- YÖNTEM: VBench kaliteyi 16 ayrık boyuta böler (iki üst grup: video kalitesi ve koşula uyum; örn. özne tutarlılığı, zamansal titreme, hareket akıcılığı, mekânsal ilişki) ve her boyutu insan tercihiyle doğrular. Artefakt veri setleri hatayı konumuyla işaretler: GenVID ~80 bin videoda 10 kategoriyi Görünüm / Hareket / Kamera eksenlerinde toplar; BrokenVideos 3.254 videoda piksel maskesi; GeneVA kutu + serbest metin açıklaması kullanır.
- KAYNAK: Huang vd., "VBench", arXiv 2311.17982 (Kasım 2023; CVPR 2024) — https://arxiv.org/abs/2311.17982 · "Artifact-Aware Evaluation for High-Quality Video Generation", arXiv 2601.20297 (2026) — https://arxiv.org/abs/2601.20297 · Lin vd., "BrokenVideos", arXiv 2506.20103 (2025) — https://arxiv.org/abs/2506.20103 · "GeneVA", arXiv 2509.08818 (2025) — https://arxiv.org/abs/2509.08818 · akademik makale
- ETİKET: ÖZET (kategori listelerinin tamamını göremedim)
- BİZE UYGULANIŞI: Her bulgu tek satır: `kategori (görünüm/hareket/kamera) · zaman kodu · kadrajda yer · kanıt karesi`; "genel olarak iyi" notu yazılmaz.

**1.5 Teslim QC: ciddiyet derecesi + hata kodu + zaman kodu**
- YÖNTEM: Netflix Asset QC hataları üç derecede not eder: **Blocker** (yayınlanamaz), **Issue** (düzeltilmeli), **FYI** (not, düzeltme gerekmez). Sözlükte kalıcı ve aralıklı ölü/sıcak piksel ayrı kodlanır; düşen kare (eksik/bozuk) ve donmuş kare (komşu karenin kopyası) ayrı kodlardır. İçerik ışık-flaş (fotosensitif epilepsi, PSE) testine girebilir; sonuç geçse de kalsa da teslim edilir.
- KAYNAK: Netflix Partner Help Center — "Introduction to Netflix Quality Control (QC)" https://backlothelp.netflix.com/hc/en-us/articles/115000353211 ; "The Production QC Glossary" https://backlothelp.netflix.com/hc/en-us/articles/21890106462611 ; "Netflix Branded Content QC Error Code Glossary" https://backlothelp.netflix.com/hc/en-us/articles/360050414074 ; "Photosensitive Epilepsy Test Results Submission Instructions" https://backlothelp.netflix.com/hc/en-us/articles/360048850953 · resmî belge (tarih görülemedi)
- ETİKET: ÖZET (alan adı bu oturumda engelli)
- BİZE UYGULANIŞI: Mevcut `animasyon-kalite-kontrol` bulgularına Blocker/Issue/FYI derecesi eklenir; tek Blocker klibi yayından alır; hızlı flaş/yanıp sönme içeren klip ayrıca işaretlenir.

**1.6 Dailies (günlük inceleme) ritmi**
- YÖNTEM: Pixar'da animatörler sabah yönetmene çekimleri gösterir, yönetmen her çekime not verir, gün içinde düzeltilir, akşam tekrar bakılır; yönetmen onaylayınca çekim "final"lenip kurguya gider. Odadaki herkes not verebilir, son söz yönetmendedir. Netflix'in canlı çekim dailies rehberi kalibre edilmiş monitör ve yazılı renk yönetim planını şart koşar.
- KAYNAK: Frame.io Insider, "Incredibles 2 and an Inside Look at the Secret to Pixar's Success" (2018-06-18, Pixar editörüyle röportaj) — https://blog.frame.io/2018/06/18/making-incredibles-2/ · uygulayıcı röportajı ; Netflix "Dailies Best Practices" (2021) — https://backlothelp.netflix.com/hc/en-us/articles/4415931246995 · resmî belge
- ETİKET: ÖZET (iki sayfa da açılmadı)
- BİZE UYGULANIŞI: Bora = yönetmen rolü; klip "final" ancak Bora'nın notu kapandığında olur (CLAUDE.md kural 4 ile aynı yön); inceleme hep aynı ekran/ayarla yapılır.

**1.7 Süreklilik (continuity) kaydı**
- YÖNTEM: Senaryo süpervizörü her çekim için hareket (oturuyor/ayakta), aksesuar, ışık, bakış çizgisi (eyeline) ve ekran yönünü (screen direction) kaydeder; bu notlar günler sonra çekilen bağlantılı sahnede tekrar açılır. Saat gibi zaman belirten nesneler sahne boyunca aynı kalmalı.
- KAYNAK: University of Texas RTF318 ders wikisi "The script supervisor" — https://cloud.wikis.utexas.edu/wiki/spaces/rtf318/pages/80022254 · eğitim ; No Film School, "What Exactly Does a Script Supervisor Do?" — https://nofilmschool.com/what-does-script-supervisor-do · eğitim/blog ; Wikipedia "Script supervisor" — https://en.wikipedia.org/wiki/Script_supervisor · ansiklopedi
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Çok çekimli işte her klip için 5 alanlı süreklilik satırı (hareket · aksesuar · ışık · bakış · yön) tutulur; montajda iki klip yan yana gelmeden bu satırlar karşılaştırılır.

**1.8 Üreticilerin kendi itiraf ettiği hata türleri**
- YÖNTEM: OpenAI, Sora duyurusunda modelin karmaşık sahne fiziğinde zorlanabileceğini, neden-sonucu kaçırabileceğini (kurabiyeden ısırık alınır ama iz kalmaz), sol-sağ karıştırabileceğini ve zamana yayılan olay tariflerinde zorlanabileceğini yazdı. Runway Gen-4 rehberi olumsuz ifadenin ("hareket etme") desteklenmediğini, öngörülemez hatta ters sonuç verebileceğini söylüyor.
- KAYNAK: OpenAI, Sora tanıtım sayfası (2024-02-15) — https://openai.com/sora · resmî beyan ; Runway Help Center, Gen-4 video istem rehberi — https://help.runwayml.com/hc/en-us/articles/39789879462419 · resmî belge
- ETİKET: ÖZET
- BİZE UYGULANIŞI: QC kontrol listesine "eylem sonrası iz kaldı mı" (neden-sonuç) ve "sol/sağ doğru mu" maddeleri girer; istemlerde "yapma" yerine olması gereken yazılır.

---

## Alan 2 — Pazar istihbaratı (hesap/format analizi)

**2.1 Kanalın kendi ortalamasına göre değerlendirme ("typical performance")**
- YÖNTEM: YouTube Analytics bir videonun izlenmesini o kanalın "tipik performansı" ile karşılaştırır; tipik izleyici tutma, kanalın **benzer uzunluktaki son 10 videosundan** hesaplanır. Genel bakış raporu izlenmenin neden olağandan yüksek/düşük olduğunu açıklayabilir.
- KAYNAK: YouTube Help, "Content tab analytics tips" — https://support.google.com/youtube/answer/12942217 ; "Get an overview of channel performance" — https://support.google.com/youtube/answer/9314414 ; "Understand your YouTube content performance" — https://support.google.com/youtube/answer/12220281 · resmî belge (erişim 2026-11-27)
- ETİKET: AÇILDI
- BİZE UYGULANIŞI: Bir videoyu "başarılı" saymadan önce aynı kanalın benzer uzunluktaki son ~10 içeriğine göre kıyaslarız; YouTube'un kendi tanımını taklit eder.

**2.2 Hangi metrik kamuya açık, hangisi değil**
- YÖNTEM: Kamuya açık izlenme, video **oynamaya başladığı anda** sayılır (Shorts, uzun video, canlı); **Kasım 2026'dan itibaren** açık izlenme sayısı TV'de birlikte izleyen kişi tahminlerini (co-view) de içeriyor. Ortalama izleme süresi, "stayed to watch" (Short'un ilk saniyelerini geçenlerin yüzdesi), engaged views, gösterim ve tıklama oranı yalnızca kanal sahibinin Studio'sunda. YPP geliri hâlâ "engaged views" ile hesaplanıyor. Data API'de dislike sayısı 2021-12-13'ten beri gizli.
- KAYNAK: YouTube Help, "How engagement metrics are counted" — https://support.google.com/youtubecreatorstudio/answer/2991785 (AÇILDI) ; answer/12220281 (AÇILDI) ; "Check your YouTube thumbnail impressions…" — https://support.google.com/youtube/answer/9314486 (AÇILDI) ; YouTube Data API revision history — https://developers.google.com/youtube/v3/revision_history (ÖZET) · resmî belge
- ETİKET: AÇILDI (dislike satırı ÖZET)
- BİZE UYGULANIŞI: Rakip analizinde dışarıdan yalnızca açık izlenme/beğeni/yorum görürüz; Kasım 2026 öncesi ve sonrası izlenme sayıları **aynı ölçek değil**, karşılaştırmada tarih notu düşülür; tutma oranı rakip için "TAHMİN"dir.

**2.3 Kapak/başlık testi tıklama ile değil izleme payı ile karar verir**
- YÖNTEM: YouTube A/B testi (en fazla 3 seçenek) kazananı "watch time share" ile ve istatistiksel anlamlılıkla belirler; yalnızca tıklama oranına göre başka kazanan çıkabileceğini açıkça yazar. Shorts'ta test yok.
- KAYNAK: YouTube Help, "A/B test titles & thumbnails" — https://support.google.com/youtube/answer/16391400 · resmî belge (erişim 2026-11-27)
- ETİKET: AÇILDI
- BİZE UYGULANIŞI: Kendi uzun videolarımızda başarı ölçüsü tıklama değil izleme payıdır; Shorts için böyle bir araç olmadığından format testi elle (ayrı yayınlarla) yapılır.

**2.4 TikTok: veriye kim erişebilir**
- YÖNTEM: TikTok Analytics (ortalama izleme süresi, videoyu sonuna kadar izleme yüzdesi) yalnızca hesap sahibine görünür. Research API `view_count`, `share_count` gibi alanları verir ama yalnızca onaylı, kâr amacı gütmeyen araştırmacılara ve proje bazında; SSS'ye göre sayılar 10 güne kadar gecikebilir.
- KAYNAK: TikTok Creator Academy, "tool-analytics-intro" — https://www.tiktok.com/creator-academy/en/article/tool-analytics-intro (eğitim) ; TikTok for Developers, Research API codebook ve FAQ — https://developers.tiktok.com/doc/research-api-codebook , https://developers.tiktok.com/doc/research-api-faq · resmî belge
- ETİKET: ÖZET
- BİZE UYGULANIŞI: TikTok rakip analizinde yalnızca sayfada görünen izlenme/beğeni/yorum/paylaşım kullanılır; tutma iddiası kurulmaz; Research API bizim için büyük olasılıkla kapalı (TAHMİN: ticari şirket uygun değil).

**2.5 Aykırı değer (outlier) skoru: tanımı tek değil**
- YÖNTEM: Skor = video izlenmesi ÷ aynı kanalın taban çizgisi. vidIQ tabanı "benzer zaman aralığındaki ortalama" olarak tanımlar (örn. 1.000 izlenme alan kanalda 10.000 = 10x). Diğer araçlar **medyan** kullanır, çünkü tek viral video ortalamayı şişirir; video kendi tabanından çıkarılmalı. Araçlar arasında standart tanım yok; 2x/10x eşikleri gelenek, standart değil.
- KAYNAK: vidIQ Help Center, "Outliers" — https://support.vidiq.com/en/articles/9660010-outliers · satıcı yardım sayfası ; vidIQ blog "vidIQ Outliers Tool" — https://vidiq.com/blog/post/vidiq-outliers-tool/ · satıcı ; Overseeros, "Best YouTube outlier tools" (2026) — https://www.overseeros.com/blog/best-youtube-outlier-tools · uygulayıcı blog
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Kendi tanımımız yazılı olur: `izlenme ÷ kanalın son N (≥10) videosunun medyanı, video hariç, aynı format`; raporda hangi tabanın kullanıldığı her seferinde belirtilir.

**2.6 Ağır kuyruklu dağılım ve tahmin edilemezlik → ortalama yanıltır**
- YÖNTEM: YouTube izlenme popülerliği kesik kuyruklu bir kuvvet yasası izler (1,69 milyon video üzerinde). Yapay müzik pazarı deneyinde (14.341 katılımcı) sosyal etki arttıkça hem eşitsizlik hem tahmin edilemezlik arttı; en iyiler nadiren kötü, en kötüler nadiren iyi gitti ama "arada her sonuç mümkündü".
- KAYNAK: Cha vd., "I Tube, You Tube, Everybody Tubes", ACM IMC 2007 — https://www.cl.cam.ac.uk/~jac22/camhor/mia_imc07_sumitted.pdf · akademik makale ; Salganik vd., "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market", Science, 2006 — https://consensus.app/papers/details/w:f9f0da13-cd97-42c4-b77b-f5f06c4f7f16/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Kanal/format kıyasında ortalama değil medyan raporlanır; tek bir viral video "format işe yarıyor" kanıtı sayılmaz, en az birkaç tekrar aranır.

**2.7 Hayatta kalma yanlılığı: başarısız örneği de topla**
- YÖNTEM: Wald'ın uçak hasarı çalışması, yalnızca dönen uçaklara bakmanın yanıltıcı olduğunu gösteren klasik örnektir; birincil kaynak rehberi Mangel & Samaniego (1984). AMS köşe yazısı, popüler anlatının belgesinin zayıf olduğunu, büyük kısmının "makul yeniden kurgu" olduğunu not ediyor.
- KAYNAK: Mangel & Samaniego, "Abraham Wald's Work on Aircraft Survivability", JASA 79(386):259–267, 1984, doi:10.1080/01621459.1984.10478038 · akademik makale ; AMS Feature Column "The Legend of Abraham Wald" (2016-06) — https://www.ams.org/samplings/feature-column/fc-2016-06 · eğitim
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Her format raporunda aynı formatı deneyip tutmayan hesaplar (karşı örnek) da listelenir; sadece başarılıları içeren rapor eksik sayılır.

**2.8 Örnekleme: çerçeveyi veri toplamadan önce yaz**
- YÖNTEM: API ile toplanan küçük örnekler çevredeki (periferik) etkinliği doğru göstermez; hashtag ile seçim ve tek platforma dayanmak örneklem yanlılığı yaratır; insanlar platformlara rastgele dağılmaz (yaş, gelir, internet becerisi).
- KAYNAK: González-Bailón vd., "Assessing the bias in samples of large online networks", Social Networks, 2014 ; Tüfekçi, "Big Questions for Social Media Big Data…", ICWSM 2014 ; Hargittai, "Is Bigger Always Better?…", Annals AAPSS, 2015 — (Consensus kayıtları: https://consensus.app/papers/details/w:00d500ef-9777-469f-b03c-5668b22222b9/ , https://consensus.app/papers/details/w:8387b620-c00f-43ef-9b42-a95c83651244/ , https://consensus.app/papers/details/w:ff47b058-7ec5-44a8-a20f-e5ff126e2af2/) · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Her araştırmanın başına "örnekleme çerçevesi" satırı: hangi platform, hangi arama/hashtag, kaç hesap, hangi tarih, neden bu hesaplar; "algoritma bana bunu gösterdi" örneklem sayılmaz.

---

## Alan 3 — Viral içerik analizi

**3.1 Yüksek uyarılma (arousal) duyguları paylaşımı artırır — ama sınırlı kapsamla**
- YÖNTEM: NYT'nin 3 aylık tüm makaleleri üzerinde: olumlu içerik olumsuzdan daha çok paylaşılıyor; yüksek uyarılmalı duygular (hayranlık/awe, öfke, kaygı) daha viral, düşük uyarılmalı (üzüntü) daha az; şaşırtıcılık, ilginçlik ve pratik yarar kontrol edildiğinde de geçerli. Almanya'daki tekrar çalışması etkilerin hepsini tekrarlayamadı ve olumluluk-viralite ilişkisinin ters-U olduğunu öne sürdü.
- KAYNAK: Berger & Milkman, "What Makes Online Content Viral?", Journal of Marketing Research, 2012 — https://consensus.app/papers/details/w:9136dcb7-b6d9-4e49-b18d-d1825c3c2e89/ ; Heimbach vd., "The impact of content sentiment and emotionality on content virality", IJRM, 2016 — https://consensus.app/papers/details/w:173f38f0-a8a6-4561-aa19-8ebcb4b345c3/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Viral analizinde "hangi duygu, ne kadar uyarıcı" sorusu sorulur; ama veri haber makalesi e-posta paylaşımı — kısa video için HİPOTEZ olarak kullanılır, kanıt olarak değil.

**3.2 Video paylaşımında eğlence, sürpriz, karakter; erken marka kötü**
- YÖNTEM: Video reklam paylaşımında eğlence, heyecan, ilham ve sıcaklık paylaşımı artırıyor; sürpriz, olay örgüsü, karakterler (bebek, hayvan, ünlü) duygu uyandırıyor; markanın erken/uzun/sürekli gösterilmesi paylaşımı düşürüyor; bulgular bağımsız örnekte tahmin gücünü korudu.
- KAYNAK: Tellis vd., "What Drives Virality (Sharing) of Online Digital Content?", Journal of Marketing, 2019 — https://consensus.app/papers/details/w:0c77c560-1510-4b93-9fd0-84019f2b2935/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Karakter odaklı kısa animasyonda kanal adı/logo ilk saniyelere konmaz; sürprizin yeri analiz formunda ayrı satırdır. (Not: çalışmadaki "ideal uzunluk 1,2–1,7 dk" reklamlar için, Shorts'a taşınmaz.)

**3.3 "Viral" çoğu zaman tek büyük yayın**
- YÖNTEM: Twitter'da bir milyar yayılım olayı üzerinde "yapısal viralite" ölçüsü: popüler içerik hem tek büyük yayınla hem kişiden kişiye büyüyebiliyor, ama yapısal viralite genelde düşük ve popülerlik büyük ölçüde **en büyük tek yayının** büyüklüğüyle belirleniyor.
- KAYNAK: Goel vd., "The Structural Virality of Online Diffusion", Management Science (Consensus kaydında 2015) — https://consensus.app/papers/details/w:d8fc3061-374b-4801-9fac-97edbbfc934f/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Bir videonun neden patladığını açıklarken önce dağıtım sorulur (büyük hesap paylaştı mı, algoritma öne mi çıkardı); içerik özelliği ancak bundan sonra tartışılır.

**3.4 Mizah: ihlal + zararsızlık (benign violation)**
- YÖNTEM: Gülme, bir ihlal aynı anda zararsız görüldüğünde ortaya çıkar; ihlali zararsız kılan üç koşul: kabul edilebilir kılan alternatif bir norm, ihlal edilen norma zayıf bağlılık, psikolojik mesafe. Warren & McGraw (2016) altı çalışmada bu tanımın mizahı mizah olmayandan "uyumsuzluk" (incongruity) tanımlarından daha iyi ayırdığını raporluyor. 2023 tekrar çalışması teoriyi kısmen destekledi (mesafe etkisi bulunmadı).
- KAYNAK: McGraw & Warren, "Benign Violations: Making Immoral Behavior Funny", Psychological Science, 2010 — https://consensus.app/papers/details/w:c75f118a-e5b6-41db-af90-ddef9d7ec7ee/ ; Warren & McGraw, "Differentiating what is humorous from what is not", JPSP, 2016 — https://consensus.app/papers/details/w:00a3e22e-eb72-4d99-b089-cb2cc8f6c6bb/ ; Franchin vd., Motivation and Emotion, 2023 — https://consensus.app/papers/details/w:c0138998-8e2d-49cb-9c5c-3c8f2d0a176b/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Her komedi fikri için iki satır yazılır: "ihlal ne?" ve "neden zararsız?"; ikisinden biri boşsa fikir zayıf adaydır — ama nihai hakem Bora ve izleyicidir (kural 3, 8).

**3.5 Mizahta şiddet × mesafe etkileşimi**
- YÖNTEM: Beş çalışma: ağır ihlaller (trajedi) zaman/sosyal/mekânsal olarak uzakken daha komik; hafif ihlaller (aksilik) yakınken daha komik.
- KAYNAK: McGraw vd., "Too Close for Comfort, or Too Far to Care?", Psychological Science, 2012 — https://consensus.app/papers/details/w:5f0e4ca0-410c-4f10-913b-afe70eda2017/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Karakter komedisinde küçük aksilikler izleyiciye yakın/tanıdık kurulur; ciddi kaza esprisi yapılacaksa abartı/çizgi film mesafesi şart.

**3.6 İzleyici tutma eğrisini okumak (resmî)**
- YÖNTEM: YouTube'un "key moments" raporu dört an türü verir: **Intro** (ilk 30 sn; izleyicinin ≥%50'si kalıyorsa "tipik üstü giriş"), **Top moments** (neredeyse kimsenin bırakmadığı yer), **Spikes** (tekrar izlenen/paylaşılan yer — ama "içerik anlaşılmadı, tekrar izlendi" anlamına da gelebilir), **Dips** (atlanan/bırakılan yer). Öneriler: kapak ve başlık içeriği doğru yansıtsın; güçlü an geç geliyorsa öne alın.
- KAYNAK: YouTube Help, "Measure key moments for audience retention" — https://support.google.com/youtube/answer/9314415 ; "Content tab analytics tips" — https://support.google.com/youtube/answer/12942217 · resmî belge (erişim 2026-11-27)
- ETİKET: AÇILDI
- BİZE UYGULANIŞI: Kendi videolarımızda bir tepe (spike) görünce "başarılı an" demeden önce "anlaşılmadığı için mi tekrar izlendi" sorusu sorulur; en iyi an ilk saniyelere çekilir.

**3.7 Kanca (hook) ölçümü: Shorts ve TikTok**
- YÖNTEM: YouTube Shorts'ta resmî kanca göstergesi "stayed to watch": Short'un ilk saniyelerini geçen izleyicilerin yüzdesi (yalnızca sahibin Studio'sunda). TikTok'un performans reklamı rehberi kancayı başa koymayı önerir ama sayfa sürümleri tutarsız: biri "ilk 3 saniye", diğeri "ilk 6 saniye" diyor; internette dolaşan "%63/%67" gibi rakamlar TikTok belgesinde doğrulanamadı.
- KAYNAK: YouTube Help answer/12220281 — https://support.google.com/youtube/answer/12220281 (AÇILDI) ; TikTok Ads Help, "Creative best practices for performance ads" — https://ads.tiktok.com/help/article/creative-best-practices (ÖZET) · resmî belge
- ETİKET: AÇILDI (YouTube) / ÖZET (TikTok)
- BİZE UYGULANIŞI: Kanca başarısını kendi Shorts'larımızda "stayed to watch" ile ölçeriz; "ilk 3 saniye kuralı" kesin kural değil, test edilecek varsayım olarak yazılır. (TikTok rehberi reklam içindir, organik içeriğe aynen taşınmaz.)

**3.8 Kısa video izleme davranışı: süre baskın, kanıt zayıf**
- YÖNTEM: TikTok reklam verisinde izleyicilerin çoğu videonun ilk çeyreğinde ayrılıyor; kontrollü deneyde videonun sonuna kadar izlenmesini en iyi tahmin eden şey **video süresi**, sona kadar izleme oranı nadiren %60'ı aşıyor. Kanca stili üzerine çalışma (80 video, 4 Myanmar hesabı) merak ve "acı noktası" kancalarının bilgi kancasından daha çok etkileşim aldığını buldu — örneklem çok küçük.
- KAYNAK: Salminen vd., "Engagement Patterns in TikTok: An Analysis of Short Video Ads", ACM HT 2024 — https://consensus.app/papers/details/w:e37b87c7-c330-4750-bc44-36aa2b5d9cb2/ ; Vieira vd., "Exploring the Limits of Predicting User Watching Behavior with Short-Form Videos on TikTok", ACM WebSci 2026 — https://consensus.app/papers/details/w:89e30e4d-545b-4492-8cf6-1972d1de81bf/ ; Phyoe, IJIRA 2026 — https://consensus.app/papers/details/w:7ba4d268-2321-4830-a308-2855919f58ab/ · akademik makale
- ETİKET: ÖZET
- BİZE UYGULANIŞI: Rakip kıyasında tamamlanma/tutma iddiaları süreye göre normalize edilmeden yapılmaz; kanca stili bulguları zayıf kanıttır, A/B karşılaştırmasıyla doğrulanmadan kurala çevrilmez.

---

## Alan başına en güçlü 3 kaynak (gerekçe: birincil + doğrulanmış varlık + bize doğrudan uygulanabilirlik)

- **Alan 1:** VideoPhy (arXiv 2406.03520) · Physics-IQ (arXiv 2501.09038) · Netflix QC sözlüğü/Asset QC (backlothelp) — üçü de ÖZET.
- **Alan 2:** YouTube Help "typical performance / typical retention" (12942217) — AÇILDI · YouTube Help "How engagement metrics are counted" (2991785) — AÇILDI · Salganik vd. 2006 Science — ÖZET.
- **Alan 3:** Berger & Milkman 2012 (+ Heimbach 2016 tekrar çalışması) — ÖZET · McGraw & Warren 2010 / Warren & McGraw 2016 — ÖZET · YouTube Help "key moments for audience retention" (9314415) — AÇILDI.

## Açık kalan işler
- arxiv.org, openaccess.thecvf.com, backlothelp.netflix.com, ads.tiktok.com, developers.tiktok.com ağ izninde değil; açılırsa ÖZET maddeleri AÇILDI'ya çevrilebilir (özellikle PhyGenEval katmanları, BrokenVideos/GenVID kategori listeleri, Netflix hata kodları).
- Consensus bu oturumda ücretsiz planla çalıştı; tam metin alıntısı yok.

## 2026-11-28 ek: AI video hata önleme yöntemleri (G-0042)

Etiketler: **AÇILDI** = sayfayı curl ile indirip metnini okudum (2026-11-27 oturumu) · **ÖZET** = yalnızca WebSearch özeti. Çoğu kaynak satıcı (vendor) blogu: kendi ürününü satıyor, bağımsız ölçüm değil. **Bulunamayan:** iç içe geçme/kapı-menteşe/prop bırakma için doğrudan kaynak bulunamadı (aramada yalnızca genel "basit tut, kes" önerisi); bu sınıflarda dayanak bizim kendi hatalarımız (`produksiyon/basarisiz-uretimler/README.md`). Resmî Kling/Runway/MiniMax/Veo-best-practice sayfaları ağ nedeniyle açılmadı (arxiv, runway, minimax, kling, nofilmschool, videomaker: proxy 403 / bağlantı yok).

**E1. Tek eylem, tek kamera hareketi**
- YÖNTEM: Kısa klipte tek ana kamera hareketi ve tek özne eylemi; çok yönlü kamera ve ani yön değişimi kaçınılır, enerji gerekiyorsa kurgu ritmiyle verilir. Çok olay gerekiyorsa ayrı çekim üretip kurguda birleştir.
- KAYNAK: Higgsfield, "How to Avoid Distortions in AI Videos: 10 Tips" (2026-07-18) https://higgsfield.ai/blog/how-to-avoid-distortions-ai-videos — AÇILDI (vendor) · Wavespeed Kling özeti (bir kamera hareketi, özne eylemi, bitiş) — ÖZET (sayfa 403) · MiniMax/Hailuo rehber özetleri (veed.io, kapwing; tek ana kamera + tek eylem) — ÖZET
- BİZE UYGULANIŞI: Çekim listesinde her çekim tek eylem + sabit kamera; mini/flash/hailuo sahnesi (3 karakter + metre + koli + kamera) bu kuralı çiğnemişti.

**E2. Yazıyı başlangıç/son uç kareyle ve "yok" kilitleriyle sabitle**
- YÖNTEM: İlk kare (image-to-video) klibin açılış karesi sayılır; Veo/Seedance ilk-son kare girdisi iki ucu sabitler, uçlar arası fark büyüdükçe model ara hareketi daha çok uydurur. İstemde "no logos, no readable text" ve "only these two people exist" gibi sayı/kimlik kilitleri kullanılır.
- KAYNAK: Google Cloud Veo 3.1 rehberi (2025-10-16) https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 — AÇILDI (ilk-son kare özelliği, olumsuz istemi "yok" diye değil istenen betimleyerek yazma) · Higgsfield Seedance 2.5 prompt rehberi https://higgsfield.ai/blog/seedance-2-5-prompting-guide — AÇILDI (örneklerde "No logos, no readable text", "Only these two people exist", "member-count lock", "STILLNESS LOCK", "Screen direction never flips"; sayfa tarihi görülmedi) · Google Cloud Vertex AI ilk-son kare sayfası — ÖZET (fark büyüdükçe uydurma)
- BİZE UYGULANIŞI: Her çekim istemine "N karakter, X kadrajda yok, yön sola" kilidi; yazı gerektiren nesneler (saat, etiket) boş üretilir, kurguda eklenir (mevcut storyboard "3/C" kuralıyla aynı yön).

**E3. Çok çekimde bir şeyi değiştir; sert kesme (hard cut) ile böl**
- YÖNTEM: Çekimler arasında yalnız bir değişken (yer ya da açı ya da ışık) değişir; model tarafında çok çekimli istemler "Shot 1/Shot 2 … Hard cut" biçiminde yazılır; mekân tanımı belirsizse çekimler arası kayar.
- KAYNAK: Higgsfield distorsiyon rehberi (madde 8, 9, 10: tek değişken, kısa klip + ilk/son kare zinciri, en zor çekimi önce dene) — AÇILDI (vendor) · Higgsfield Seedance 2.5 rehberi ("vague location is the most common reason a multi-shot sequence starts drifting") — AÇILDI · Runway Seedance 2.5 rehberi (Shot 1, 2, 3 sırası; sabit kalacakları sonda yaz) — ÖZET
- BİZE UYGULANIŞI: Storyboard çekimleri tek değişkenle ilerler; en riskli çekim (iki karakterin yakın olduğu) ilk ve tek başına test edilir, bu da `takim.md` adım 4'teki "en ucuz tek test" ile uyumludur.

**E4. Hareketi başlangıç ve bitiş pozisyonuyla tarif et; el/yüz hatası için yüzü doldurma, çerçevele**
- YÖNTEM: "Koşuyor" yerine başlangıç ve bitiş vücut/el pozisyonu yazılır; el hareketi için gerçek pozisyonun referans görseli eklenir; eller kıyafet/battaniye içinde gizlenebilir (Seedance örnek istemlerinde "Hands hidden inside the blanket"); el ve yüz ayrıntısı prompt'un ilk satırında, ikincil ayrıntılardan önce yazılır. Aşırı yüklü prompt'ta ilk bozulan el ve yüzdür.
- KAYNAK: Higgsfield, "Why AI Video Still Gets Hands and Faces Wrong" (2026-07-24) https://higgsfield.ai/blog/ai-video-hands-faces — AÇILDI (vendor) · Higgsfield Seedance 2.5 rehberi (örnek istem) — AÇILDI · hackernoon/magichour/dreamina "elleri kadraj dışına al" önerileri — ÖZET
- BİZE UYGULANIŞI: Prop tutma/bırakma: prop elde başlar, elde biter; el gerektirmeyen çözüm (prop zaten masada/yerde) tercih; kanat/pati + damga gibi küçük ayrıntı ayrı yakın plan çekim.

**E5. Kesmeyle gizleme: cut on action, tepki/insert çekimi**
- YÖNTEM: Hareket sürerken kesmek geçişi izleyiciye fark ettirmez (hareketli öğeler iki çekimde aynı konumda olmalı). Düzeltilemeyen bir geçiş/temas anı tepki çekimi, kadraj dışı ya da kısa insert ile gizlenir; üretimde "birden çok vuruşlu sekansı ayrı çekimlerle üretip montajda birleştir".
- KAYNAK: Wikipedia, "Cutting on action" https://en.wikipedia.org/wiki/Cutting_on_action — ÖZET (arama özeti; sayfa açılmadı) · Adobe "What is continuity editing" — ÖZET · Dreamina/Capcut, elser.ai "fix bad AI video shot" özetleri (tepki çekimi, iki karelik insert) — ÖZET
- BİZE UYGULANIŞI: Karakterlerin fiziksel teması modelden istenmez; temas çekim A'da (kaz kapıya doğru), tepki çekim B'de (vombat), "çarpma/geçme" sesle ve kesmeyle verilir (kapi_v1 iç içe geçmesinin tasarımsal karşılığı).

**E6. Fizik zayıflığı: kasa (conservation), nesne kalıcılığı, menteşe**
- YÖNTEM: Fizik benchmarkları modellerin momentum/kütle korunumunda, menteşe/kapı gibi kısıtlı hareketlerde ve nesne kalıcılığında zayıf kaldığını gösteriyor; "gerçekçi görünüyor" fiziği kanıtlamıyor. Pratik sonuç: fizik bağımlı etkileşim (kayma, kopma, kapı) modele güvenilmeden tasarlanır; imkânsızsa kesmeyle ya da statik kareyle verilir.
- KAYNAK: VideoPhy-2, arXiv 2503.06800 https://arxiv.org/abs/2503.06800 — ÖZET (en iyi model zor altkümede %32,6 [v1]; momentum/kütle korunumunda zayıf) · Physics-IQ arXiv 2501.09038 ve VideoPhy 2406.03520 — ÖZET (bölüm 1.1 ve 1.3'te zaten var) · PhyGenBench arXiv 2410.05363 — ÖZET (model büyütmek/istem mühendisliği dinamik hatayı çözmüyor)
- BİZE UYGULANIŞI: "Çekimi yeniden yaz" eşiği: koli kayması, şerit metre kopması, kapı açılması tek başına yüksek risk; bizim kanıtlarımız (koli süzüldü: tekrar testinde 4 kör çıktının 2'si net hata, 2'si şüphe olarak yazdı, metre yok oldu) bunu destekliyor. Bunlar aracın gerçek kanıtı değil, tasarım tercihidir.

**E7. Karakter sayısı ve kimlik kilidi**
- YÖNTEM: Kimlik anchor'ı (referans görsel) kullan; çok karakterli sahnede "tam N kişi, tekrar yok" kilidi; iki karakter yakın etkileşimde kimlik bulanması kesişim noktasında görünür, en zor çekim önce test edilmeli.
- KAYNAK: Higgsfield distorsiyon rehberi (madde 3, 10) — AÇILDI (vendor) · Higgsfield Seedance 2.5 rehberi ("member-count lock, exactly four, never five, never duplicated") — AÇILDI
- BİZE UYGULANIŞI: ≥ 3 karakter tek çekimde = "yeniden yaz" (kendi benchmark'ımızda 3 karakter, 3 modelde de bozuldu).

**E8. Ses ve zamanlama montajda**
- YÖNTEM: Veo 3.1 rehberi diyalog/SFX/ortam sesini istemde ayrı satır olarak ister; Seedance rehberi sesi "en son, tek kural" olarak yazar (örn. "No music, no discernible dialogue"). Zamanlama ve şakanın vuruşu modele değil kesme noktasına bağlanır.
- KAYNAK: Veo 3.1 rehberi (SFX/Ambient noise satırları) — AÇILDI · Higgsfield Seedance 2.5 rehberi (AUDIO bölümü) — AÇILDI
- BİZE UYGULANIŞI: Şakanın kilit anı görselden çok sesle ve kesmeyle taşınır; ses her raporda "dinlenmedi" etiketiyle kalır (kural 4).

### Test (TAHMİN, üretimle test edilmedi): `produksiyon/storyboard/2026-11-27-ucuncu-kat-b1.md` klip B ve test sahnesi

| Çekim (eski) | ÖNCE (eski, tek klip) | SONRA (yeniden tasarım) |
|---|---|---|
| B klip K5–K7 7 sn: oturan Tomruk + kayan koli + 3 karakter yukarıdan + metre kopuyor | iç içe geçme Y (3 karakter, koli üstünde); yüzen nesne Y (koli kayması); ince esnek Y (metre kopar uçar); karakter sayısı Y; kilit an O; morf O | **B1** (3 sn): sabit kamera, Tomruk koli üstünde oturur, koli hareketsiz, eğim yok (yüzen nesne D, çoğalma D) · **B2** (3 sn): yalnız Anahtar alt kat, dikey bakış, damgayı kaldırır (1 karakter) · **B3** insert (2 sn): Cetvel korkuluk, metre sarkık ve sabit (kopma yok); kopma sesi + kurguda kesme; "koli kayıyor" = ses + iki kare arası kesme |
| K8–K9 (Anahtar damga, Tomruk yürür) | prop tutma O (damga havada); yön O (sırt kamerada yürüme); dönüş O | damga zaten kanatta, hareketsiz; Tomruk yürümez: kamera önden, Tomruk durur, kesme sonrası merdivende |
| K10 etiket | yazı Y ("3/C") | boş etiket üret, kurguda ekle (zaten öyle) |
| **Toplam** | Y: 4, O: 5 | Y: 0, O: 2 (karakter sayısı tek, kilit an O: küçük damga → yakın plan çekim) |

---

## 2026-11-28 ek: komedi ve kreatif yazım (G-0055)

Hazırlayan: araştırma ajanı (Claude) · Durum: ham kaynak derlemesi, karar dayanağı değil (CLAUDE.md kural 3, 8). Beceri dosyası yazılmadı. `denetim/komedi-beceri/` klasörü açılmadı (kör test).

### Önce bilinen eksikler (okumadan geçme)

- **Sayfa olarak yalnızca 3 resmî YouTube Yardım sayfası AÇILDI** (curl, 2026-11-28). Komedi uygulayıcı sayfalarının (Substack, NBC, NPR, Masterclass, Backstage, Wikipedia, dergiler) **hiçbiri açılamadı**: curl çıktısı bağlantı yok (000), WebFetch `ENOTFOUND` (ÖLÇTÜM; bu alt oturumun ağ izni yalnızca support.google.com/youtube ve youtube.com). Bu nedenle komedi yöntemlerinin tamamı **ÖZET** etiketlidir (WebSearch özeti ya da Consensus kaydı).
- **Hiçbir kitabın metnini okumadım.** UCB Comedy Improv Manual, Truth in Comedy ve Toplyn kitabı için yalnızca künye (ISBN/yayıncı) arama özetinden; **hangi bölümde ne yazdığını bilmiyorum** — bölüm numarası/sayfa verilmedi, uydurmadım. Kitaplardan gelen her bilgi ikincil kaynağın (blog/eğitmen) özetinden geliyor, kitabın kendisinden değil.
- Röportaj/video (Seinfeld NYT videosu, ZAZ röportajları, Chris Rock) izlenmedi/okunmadı; içerik arama özeti. Tırnak içi alıntı **yok**; bütün cümleler benim özetimdir.
- Akademik makalelerin tam metnini okumadım; Consensus kaydı (başlık, yazar, yıl, dergi, özet) ÖZET sayılır. "Timing is Everything" (2026) arXiv ön baskıdır (hakem değerlendirmesi görülmedi).
- **Bulunamayan:** (a) "misdirection" için adlandırılmış uygulayıcı kaynak (aramada çıkmadı; akademik karşılığı aşağıda); (b) "tek şakanın tekrarı" için doğrudan kaynak; (c) "alts" için yalnızca tanım özeti, biçim/süreç ayrıntısı yok; (d) Mel Brooks'un kendi yöntemi (yalnızca ZAZ özetleri çıktı); (e) Eric Andre.
- Etiketler: **AÇILDI** = curl ile indirip metni okudum (2026-11-28) · **ÖZET** = arama özeti/veritabanı kaydı. Tarafsızlık: satıcı blogları (vidIQ, 1of10, TubeBuddy, CapCut) kendi ürününü satar; kurs/eğitmen blogları (Hoopla, Will Hines, Toplyn) kendi okulunu/kitabını satar.
- **Bütün "NASIL TEST EDİLİR" ölçütleri benim önerimdir (HİPOTEZ).** Hiçbiri bu kaynaklarda "komediyi ölçer" diye doğrulanmadı; komedi ölçülemiyor (K-031 dersi). Kör puanlamada **ön eleme** ölçütü olarak kullanılabilir, "komik" kanıtı sayılmaz.

### Kaynak sayımı

AÇILDI: 3 sayfa (YouTube Yardım). ÖZET: yaklaşık 40 URL/kayıt (WebSearch özetleri ~30, Consensus kayıtları 9) + 3 kitap künyesi (okunmadı).

### K1. Skeçin "oyunu" (game of the scene): ilk olağandışı şey

- YÖNTEM: Skeç, önce sıradan bir zemin ("base reality") kurar; zeminden ilk sapan öğe "ilk olağandışı şey"dir; geri kalan skeç bu tek örüntüyü bulup oynamaktır (olay örgüsü ya da bahis değil, olağandışı olanı oynamak). Eğitmen notları, ilk olağandışı şeyi **fazla** olağandışı yapmanın sık hata olduğunu ve acemilerin esprinin peşine erken düştüğünü söylüyor.
- KAYNAK: M. Besser, I. Roberts, M. Walsh, *The Upright Citizens Brigade Comedy Improvisation Manual*, Comedy Council of Nicea, 2013, ISBN 9780989387804 (künye: WorldCat/AbeBooks arama özeti) — **kitap okunmadı, bölüm bilinmiyor** · ikincil özetler: Will Hines substack ("Teaching Game of the Scene"), Hoopla Improv "A quick guide to Game of the Scene", improv-toolbox "Repeat the first unusual thing", Script Magazine "Improvising Screenplays…Using the Game of the Scene" — hepsi ÖZET (eğitmen/okul tarafı, tarafsız ölçüm değil).
- BİZE UYGULANIŞI: Her skeç/klip için tek cümle "oyun": "[sıradan durum] + [tek sapma]". Senaryo 3 sn içinde sıradan zemini gösterir, sapma ilk 5 sn içinde belirir; sonraki her an aynı sapmanın tırmanışıdır. AI video tarafında bu zaten "tek eylem, tek sapma" kuralıyla (E1) uyumlu.
- NASIL TEST EDİLİR (kör puanlama): okuyucu skeci okuyup "oyunu tek cümleyle yaz" der; **3 okuyucudan en az 2'si aynı oyunu yazarsa geçer**; farklı yazarlarsa skeç birden çok fikre dağılmıştır. İkinci ölçüt: sapma ilk üçte birde belirdi mi (evet/hayır).

### K2. Tırmandırma (heightening)

- YÖNTEM: Oyun bulunduktan sonra "bu doğruysa başka ne doğru?" sorusuyla aynı örüntü artan şiddette/mantıkla tekrarlanır; her tekrar bir öncekinden **farklı ve daha büyük**, ama aynı kuraldan çıkar.
- KAYNAK: Will Hines ("Teaching Game 2: Heighten and Explore"), Funny How ("heighten and explore"), The Free Association ("easy ways to heighten game") — ÖZET (eğitmen blogları). UCB kitabı için yukarıdaki not geçerli: kitabın bu başlıktaki bölümünü okumadım.
- BİZE UYGULANIŞI: Skeçte en az 3 vuruş; her vuruş bir öncekini bir boyutta (sayı, ölçek, mantık derinliği, sosyal bedel) büyütür; tekrar ama aynı şiddette değil. Video süresi kısa olduğu için "tırmanış" tek kurguda 3 kesme ile verilir.
- NASIL TEST EDİLİR: vuruşları sırala; **her vuruşun öncekinden daha yüksek mi/farklı mı olduğu** evet/hayır. Aynı şiddette tekrar = "tek şaka tekrarı" hatası (Hata H3).

### K3. Şaka yapısı: kurulum / vuruş; kurulum arızası

- YÖNTEM: Şakanın iki ana öğesi kurulum (setup) ve vuruş (punchline); vuruş kurulumu "ödüllendirir". Chris Rock'a atfedilen gözlem (aktarma): şaka tutmuyorsa genelde seyirci **önermeyi/kurulumu** anlamamıştır; vuruşu değiştirmeden önce kurulum denenir. Joe Toplyn'in çerçevesi: şaka = konu + açı + vuruş; vuruş üretmek için konunun çağrışımlarını bağlamak ve sorular sormak (6 "Punch Line Maker" teknikten ikisi blogda geçiyor).
- KAYNAK: Funny How, "Chris Rock: It's not working because the audience doesn't understand the premise" — ÖZET (Rock'ın kendi sözü doğrulanmadı, Substack aktarımı); MasterClass "What is a punchline" — ÖZET (satıcı); Joe Toplyn, *Comedy Writing for Late-Night TV*, Twenty Lane Media, 2014, ISBN 978-0-615-95389-2 — **kitap okunmadı**, blog joetoplyn.com özetleri — ÖZET (yazar kitabını satıyor); Script Magazine "Comedy Writing: How to Fix a Broken Joke" — ÖZET.
- BİZE UYGULANIŞI: Şaka kırık görününce önce kurulum kısaltılır/netleştirilir. Her gag için üç satır: konu, açı, vuruş.
- NASIL TEST EDİLİR: şakanın "kurulum" ve "vuruş" cümlesini okuyucu ayrı ayrı işaretler; **işaretlenemiyorsa yapı yoktur**. Kurulum, vuruşu anlamak için gerekmeyen cümle içeriyor mu (evet = fazla uzun).

### K4. Üçlü kural (AAB) ve yanıltma

- YÖNTEM: İki benzer öğe örüntüyü kurar, üçüncü kırar (AAB). Tekrar sayısı iki: az olursa örüntü yok, çok olursa (AAAB) kırma gecikir.
- KAYNAK: Rozin vd., "Documenting and explaining the common AAB pattern in music and humor", *Emotion*, 2006 — https://consensus.app/papers/details/w:8acf310e-31f8-4e7f-b21c-7b711e80d728/ — ÖZET (şaka örnekleminde AAB baskındı, deneyde AB ve AAAB'ye göre en etkiliydi; özet böyle diyor, tam metin okunmadı) · McKeague, "Comedy comes in threes", *Comedy Studies*, 2021 — https://consensus.app/papers/details/w:ba3e4cbe-b501-4bbc-aa13-50cbb594797b/ — ÖZET (kavramsal çerçeve, deneysel değil). **Yanıltma (misdirection):** adlandırılmış uygulayıcı kaynak bulunamadı; akademik karşılığı beklenti-uyumsuzluk-çözüm modeli: Chang vd., *Brain Sciences*, 2023 (fMRI, üç öğeli şakalar; beklenti ve uyumsuzluk evreleri ayrıldı) https://consensus.app/papers/details/w:f0cfbf9d-1541-4546-9447-0ba3a7b44da8/ ; Xie vd., ACL 2021 (kurulum belirsizlik, vuruş şaşırtma) https://consensus.app/papers/details/w:b6d1e23c-b559-4f11-8519-8d6747876837/ — ÖZET.
- BİZE UYGULANIŞI: Listeleme/tekrar kurgularında iki aynı + bir farklı vuruş; üçüncü öğe ikisinin ima ettiği beklentiyi bozar. Yanıltma: kurulum izleyiciyi tek okumaya götürür, vuruş ikinci okumayı verir (bu yönteme ayrı kaynak yok; hipotez).
- NASIL TEST EDİLİR: üçlü yapıda iki aynı + bir farklı mı (evet/hayır); okuyucu "3. öğeden önce ne bekledin?" sorusuna yazılı cevap verir, **vuruş o cevaptan farklıysa geçer**, aynıysa tahmin edilebilir.

### K5. Geri çağırma (callback)

- YÖNTEM: Daha önceki şakaya sonradan dönüş; gülme hem ilk şakadan hem dönüşün sürprizinden gelir; kurulum ve vuruşun zamanla ayrılıp sonradan birleşmesi.
- KAYNAK: Backstage "How to Use Callbacks in Your Comedy" — ÖZET (sayfa açılmadı; sektör yayını) · The Pudding "stand-up" yapı analizi (hakkında özet var, okunmadı).
- BİZE UYGULANIŞI: Seri bölümlerde (kreatif takım adım 4) bir bölümün tekrar eden öğesi sonraki bölümde dönüş olur; 15-30 sn klip içinde: 1. sn'de gösterilen nesne son sn'de vuruş olur (aynı zamanda döngü, bkz. K10).
- NASIL TEST EDİLİR: iki an arasında açıkça bağlanan tek öğe var mı; **ikinci kullanım ilk kullanımı bilmeden de çalışıyor mu** (tek başına okunur mu, evet/hayır).

### K6. Masa okuması, punch-up ve "alts"

- YÖNTEM: SNL tipi hafta: Pazartesi fikir toplantısı, Çarşamba tüm yazar/oyuncu/yöneticiyle masa okuması, ardından seçim ve yeniden yazım. Masa okuması **güvenilir tahmin aracı değil**: bir yapımcı "Çarşamba okunan Cumartesi yayınlanandan çok farklı olabilir" diyor; Nate Bargatze'ın en iyi skeci masa okumasında tutmamış, yine de yayına girmiş (başlık özeti). Punch-up: ekip bir taslağı gruplayıp şaka ekler/geliştirir/keser. "Alts": bir satır için birden çok alternatif satır; showrunner seçer (Veep odası anlatımı). Birbiglia, ilk şakalarını komedyen arkadaşlara okutup öneri aldığını söylüyor.
- KAYNAK: NBC Insider "How do SNL sketches make it on air" ve DGA Quarterly (Bahar 2015) — ÖZET (ikincisi eski, 2015); Cracked, Nate Bargatze başlığı — ÖZET (yalnız başlık/özet); Scriptnotes bölüm 551 ve 688 (John August) — ÖZET (alts tanımı, Birbiglia); Stage32 punch-up atölyesi — ÖZET (satıcı).
- BİZE UYGULANIŞI: Her gag için en az **3 alternatif satır** yazılır, seçim kör puanlamayla; okuma "tek kişi sesli okur" biçiminde yapılır (yazar kendi okumaz). Masa okuması sonucu "komik kanıtı" değil, yalnızca kırık yer tespitidir (CLAUDE.md kural 8 ile uyumlu).
- NASIL TEST EDİLİR: aynı gag için 3 alt, isimsiz, sırası karıştırılmış; 3 bağımsız okuyucu birini seçer; **seçimlerin dağılımı** kaydedilir (3'ü de farklı seçtiyse güçlü bir alt yok). Not: örneklem 3, sonuç kesin değil.

### K7. Reklam parodisi yapısı

- YÖNTEM: Gerçek reklam biçiminin dilini/görsel kurallarını doğru kullan (ayrıntı parodiyi satar); ürün kötü olabilir ama skeç **gerçek dünya hakkında bir fikir** söylemeli; "var olmayan sorun + etkisiz çözüm" kalıbı SNL yazım notlarında anılıyor; son cümle hem reklam biçimine uygun hem de şaka olmalı. Tek şaka 2 dakikayı taşımaz: ilerleme (bir şeyin değişmesi) gerekir. ZAZ (Airplane!) örneği: oyuncular komedi içinde olduklarını bilmiyormuş gibi ciddi oynar; dramatik oyuncular seçildi.
- KAYNAK: No Film School "How to make perfect parody" ve Celtx "How to write a parody" — ÖZET (kurs/yazılım satıcıları) · NPR transkript (1202582056), Salon (2023), AV Club oral history (Airplane!), Total Film — ÖZET (açılmadı; kitap: *Surely You Can't Be Serious*, Macmillan; okunmadı).
- BİZE UYGULANIŞI: **Kurgusal marka zorunlu** (kreatif kural 1). Format: tanım (30 sn reklam iskeleti: sorun / ürün / kanıt / sloganı) + tek gizli sapma; ciddi ses ve ciddi görsel, sapma yalnız içerikte. AI video: ciddi tonu ışık/ses talimatıyla ver, gerçek dışı sahneyi haber gibi sunma (kalite madde 8).
- NASIL TEST EDİLİR: okuyucu "bu hangi reklam türünün parodisi?" sorusuna yazılı cevap verir (**tanınmıyorsa biçim zayıf**); "skeç ürün hakkında mı, dünya hakkında mı bir fikir söylüyor?" (tek cümle); son cümle şaka mı (evet/hayır).

### K8. Absürt/sürreal komedi: "sıradan absürt"

- YÖNTEM: Absürt, sıradan durumun mantığına **sadık kalarak** itilir: karakter kendini haklı sanır, geri adım atmaz, hatadan çıkış arayıp daha derine girer. Eleştirmenler *I Think You Should Leave*'in absürtlüğünü günlük hayatın zaten absürt olan yanının aynası sayıyor; Fielder'ın yönteminde fantezi değil, gerçek durumun giderek aşırı uca götürülmesi. Sam Richardson yapıyı "A'dan B'ye, sonra F'ye" diye tarif ediyor (beklenen C yerine sıçrama). Yapım notu: Robinson-Kanin uzun yazıp kesiyor.
- KAYNAK: The Ringer (2019), Den of Geek, Yahoo, LARB "The Way We Laugh Now", Common Reader (WUSTL) — ÖZET (eleştiri/röportaj, hepsi ikincil; yöntemi yazarların kendisi "kural" diye koymuyor) · Psyche, CBC (Hedberg) — ÖZET.
- BİZE UYGULANIŞI: Absürt fikir = sıradan bağlam + tek aşırı davranış; karakter davranışı izleyiciye "mantıklı" gelmeli. Fotogerçekçi AI'da "sıradan sahne + tek imkânsız öğe" (tek sapma, K1 ile aynı kural). Marka/kişi taklidi yok (Anayasa 13).
- NASIL TEST EDİLİR: sapmanın **karakter için mantığını** okuyucu tek cümleyle yazabiliyor mu; tırmanışta karakter geri adım atıyor mu (atıyorsa absürt değil, açıklama). Sapma tek mi (evet/hayır).

### K9. Mizah teorisi: ihlal + zararsızlık

- YÖNTEM: Yeniden yazılmadı: bkz. bu dosyada **3.4** (McGraw & Warren 2010; Warren & McGraw 2016; Franchin 2023). Ek bulgu: Warren vd., "What Makes Things Funny?", *Personality and Social Psychology Review*, 2020 — https://consensus.app/papers/details/w:229d5cad-c50a-4835-a3a1-aee026d79d3b/ — ÖZET: incelemeye göre **şaşırtma ve üstünlük tek başına mizahı mizah olmayandan ayırmıyor**; eşzamanlılık, ihlal ve zararsız değerlendirme ayırıyor.
- BİZE UYGULANIŞI: Şaşırtma yetmez; fikir **bir ihlal + onu zararsız kılan bir şey** (mesafe, kurgusallık, alternatif norm) taşımalı. Kurgusal karakter/marka zararsızlık sağlar; ağır ihlal (travma, gerçek kişi) zararsızlığı bozar ve Anayasa 11'e de takılır.
- NASIL TEST EDİLİR: iki ayrı soru: "ne ihlal ediliyor?" ve "neden zararsız?" okuyucu cevap yazar; ikisinden biri boş kalırsa uyarı. **Bu ölçüt gülme ölçmez**, yalnızca yapı kontrolüdür.

### K10. Kısa videoda ilk saniye kancası ve döngü

- YÖNTEM: (a) Resmî: YouTube'da Shorts için "stayed to watch" (Studio, yalnız sahibi görür); retention grafiğinde yükselme = izleyenler o bölümü izliyor/tekrar izliyor/paylaşıyor, düşüş = bırakıyor. (b) Resmî: **31 Mart 2025'ten beri Shorts görüntülemesi, Short'un her başlaması veya tekrarında sayılıyor, en az izleme süresi şartı yok; eski ölçü "Engaged views" adıyla Analytics'te kalıyor** → döngü ham görüntülemeyi şişirir, kalite ölçüsü olarak "engaged views" ve "stayed to watch" kullanılmalı. (c) Satıcı/uygulayıcı tavsiyesi: ilk 1-3 sn'de ödülü ya da net görseli göster, sonu başa bağla (eşleşen kare, ses döngüsü); kaynaklar süre konusunda çelişiyor (1-2 sn / 3 sn); %70-79 "geçer", %80+ "güçlü" gibi eşikler YouTube'dan doğrulanmadı. (d) Akademik zayıf kanıt: TikTok reklam verisinde izleyicilerin çoğu videonun ilk çeyreğinde ayrılıyor (Salminen vd., 2024); 12 kişilik niteliksel çalışma görsel tetikleyici kategorileri (hareket, yüz/göz teması, kontrast, yazı) sıralıyor (Ridha, 2026, düşük güven).
- KAYNAK: **AÇILDI** (2026-11-28): YouTube Community "A Change to How We Count Views on Shorts" https://support.google.com/youtube/thread/333869549 · "Measure key moments for audience retention" https://support.google.com/youtube/answer/9314415 · "Get started creating YouTube Shorts" https://support.google.com/youtube/answer/10059070 (yalnızca "Get feedback" düğmesinin kanca/tempo analizi yaptığı satırı alakalı). **ÖZET:** vidIQ (Shorts kancaları, döngü), 1of10 analytics, TubeBuddy, CapCut "loop count" (CapCut: döngü sayısının tek başına öneriyi artırdığı platformca söylenmedi) — hepsi satıcı; Consensus: Salminen 2024 https://consensus.app/papers/details/w:e37b87c7-c330-4750-bc44-36aa2b5d9cb2/ , Xiao 2024 (60 satıcı, 2.511 TikTok reklamı: çekim sayısı ve görüntü karmaşıklığı ters-U ilişki) https://consensus.app/papers/details/w:8192b443-9423-41cb-8101-f20b6b6f0f5a/ , Ridha 2026 https://consensus.app/papers/details/w:19b89d35-3070-4a67-bd06-150129779bfd/ . Mevcut 3.7 (kanca ölçümü) tekrar edilmedi.
- BİZE UYGULANIŞI: Klibin 0-2 sn'sinde sapma/vuruşun görsel ipucu (K1); son kare ilk kareye eşleşir (nesne, ışık, ses seviyesi) → döngü. Başarı ölçüsü: "stayed to watch" ve engaged views (ham görüntüleme değil). Süre normalizasyonu şart (3.7).
- NASIL TEST EDİLİR (kör, yayın öncesi): sessiz izleme ilk 2 sn'de okuyucuya "ne olacağını/neden bakılacağını tahmin et" (**merak kancası var mı**, evet/hayır); son kare-ilk kare uyumu (kare karşılaştırma, ÖLÇÜM yapılabilir); ses döngüsü: sondaki sessizlik/çatlak (not: ben sesi dinleyemem, bu madde Bora'ya bırakılır). Gerçek hakem yayın sonrası "stayed to watch" olacaktır.

### K11. Zamanlama: vuruştan önce duraklama

- YÖNTEM: 828 profesyonel Çince stand-up performansında zamansal özellikler (vuruş öncesi duraklamaların uzaması, tepe şaşırtma) izleyici beğenisini anlamsal uyumsuzluktan daha çok öngördü; başka bir çalışma canlı komedide tekrarlanan ve sıkı zamanlı materyali haritaladı.
- KAYNAK: "Timing is Everything: Temporal Scaffolding of Semantic Surprise in Humor", Cognitive Science Society 2026 (arXiv ön baskı) https://consensus.app/papers/details/w:411fae8c-c3f3-4764-8350-feb29e1912b9/ — ÖZET, ön baskı, dil/kültür farkı var (Çince canlı performans, kısa video değil) · Pope vd., *PNAS Nexus*, 2026 https://consensus.app/papers/details/w:76264a27-5590-473d-bab0-7a466c1166eb/ — ÖZET.
- BİZE UYGULANIŞI: Kurguda vuruştan önce kısa bir boşluk (kesme/sessizlik) denenir; "kaç kare" konusu burada kanıtlanmış değil, **hipotez**. Kuralı Bora izleyerek ayarlar.
- NASIL TEST EDİLİR: aynı klibin iki montajı (duraklamalı / duraklamasız), tek değişken; kör okuma (yalnız metin değil, **video** gerektirir, Bora izler); kararı kör puan değil gerçek izleyici verir.

### Sık hatalar (başarısız örnek kalıpları)

- **H1. Açıklanan vuruş:** şakayı anlatmak/açıklamak. Kaynak: Substack yazıları ve kısa-yazı rehberleri ("seyirci zekâsına güven") — ÖZET, düşük-orta güven (blog). Test: vuruştan sonra kurulumu tekrar eden ya da "yani şu demek" diyen cümle var mı (evet = hata).
- **H2. Uzun kurulum:** kurulum meandering/çok iş yaparsa seyirci vuruştan önce kopar; vuruş zayıfsa önce kurulum bakılır (Script Magazine, Funny How, Chuffah — ÖZET). Test: kurulumdaki **vuruşu anlamak için gereksiz** cümle sayısı (hedef 0); kısa videoda kurulum toplamın ilk üçte birini geçmesin (hipotez, kaynaksız eşik).
- **H3. Tek şakanın tekrarı:** doğrudan kaynak bulunamadı; dayanak K2 (tırmanış gerekir) ve reklam parodisi notu (tek şaka iki dakikayı taşımaz, ilerleme gerekir: No Film School özeti). Aynı vuruşun şiddetini artırmadan tekrarı = hata. Bizim kayıtlarda bu hata ayrıca aranmadı.
- **H4. Fazla olağandışı ilk adım** (K1, eğitmen özetleri): sapma zeminden kopuk olursa tırmanacak yer kalmaz. Test: sapma zemin ile aynı cümlede anlaşılıyor mu.
- **H5. Masa okumasını kanıt sanmak:** bkz. K6 (okuma sonucu yayın başarısını öngörmüyor). Bizim kuralımız zaten aynı (CLAUDE.md 3, 8).

### En sağlam 5 yöntem (bizim için, güven sırası ile)

1. **K10 (kanca/döngü ölçüsü):** tek AÇILDI resmî kaynak; ölçü tanımı net (engaged views, stayed to watch). Taktik tavsiyeleri ise satıcı.
2. **K1 (oyun + ilk olağandışı şey):** üç bağımsız eğitmen özetinde tutarlı; kitap okunmadı; ölçütü (3 okuyucu aynı oyunu yazıyor mu) basit ve test edilebilir.
3. **K4 (AAB/üçlü kural):** tek hakemli deneysel makale özeti (Rozin 2006) + kavramsal makale; yöntem kısa videoya doğrudan taşınır.
4. **K9 (ihlal + zararsızlık):** en çok atıf alan akademik çerçeve, 2020 incelemesi var; yalnızca yapı kontrolü, gülme ölçmez.
5. **K3 (kurulum arızası, kırık şakada önce kurulumu düzelt):** birden çok bağımsız yazar rehberi ve Rock aktarımında hemfikir; kaynaklar ikincil.

(K6/K8/K7 faydalı ama kaynakları ikincil ya da tek yönlü; K11 ön baskı ve kültür farkı nedeniyle en zayıf.)

### Açık kalan işler

- Komedi uygulayıcı sayfalarının açılması için ağ izni (örn. substack, nbc.com, npr.org, scriptmag.com, masterclass.com, backstage.com) ya da Bora'dan metin; açılırsa yukarıdaki ÖZET etiketleri AÇILDI'ya çevrilebilir.
- Kitaplar için bölüm düzeyinde kaynak: Bora kitabı/alıntıyı verirse işlenir (UCB manual, Truth in Comedy, Toplyn).
- Bu bölüm yalnızca bilgi; beceri dosyası ve öncesi/sonrası kör test ayrı adım.
