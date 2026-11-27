# Kuruluş denetimi — 2026-11-27

Denetçi: Bekçi (`.claude/agents/bekci.md`). Denetlenen SHA: `d7d85176c825978b98b8777e9c582a6ddf590848` (`git rev-parse HEAD` ile doğrulandı).
Not: Denetim sırasında HEAD `bc2d118` oldu (3 yeni commit). `git diff d7d8517 HEAD` yalnızca `denetim/dis-denetim/`, `karakterler/adaylar/`, `toplantilar/gundem/` ve `takimlar/kreatif/defter.md` dosyalarına dokunuyor; bu denetimin kapsadığı dosyaların hiçbiri değişmedi. Onaylar yalnızca `d7d8517` içindeki haliyle geçerlidir.
Üreticiler: Chief of Staff (G-0001, G-0007), pazar-istihbarati (G-0003–G-0006). Bekçi bu işleri üretmedi.

## Çalıştırılan mekanik kontroller (kendim)
- `python3 -I tests/test_gorev_sec.py` → 14/14 geçti.
- `bash tests/test_kilit.sh` → 7/7 geçti.
- `python3 -I scripts/dogrula.py --degisen $(git diff --name-only 4b825dc… HEAD)` → **14 BULGU**, hepsi `KORUNAN:` (ANAYASA.md, denetim/BEKCI-KURALLARI.md, 7 adet `sirket/*`, 6 adet `takimlar/*/kurallar.md`). Sır, medya, kuyruk, tek-kaynak bulgusu yok. E-posta/token deseni için ayrıca tüm repoyu taradım: gerçek kişi verisi veya sır yok (eşleşenler yalnızca `dogrula.py` içindeki desen metinleri).

## Araştırma kısıtı (örneklem doğrulaması için)
Bu ortamda WebFetch kullanılmadı; yalnızca WebSearch. Hiçbir kaynak sayfası tam metin açılmadı; doğrulamalar arama sonuç özetlerine ve birden fazla bağımsız haber sonucuna dayanıyor. "Tuttu" = özetlerde aynı değer ve tarih görüldü; "doğrulanamadı" = arama özetinde karşılığı çıkmadı (yanlış olduğu anlamına gelmez).

---

```
KARAR: İNSAN ONAYI GEREKLİ
GÖREV: G-0001   TAKIM: chief-of-staff (kuruluş iskeleti)   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- 3 (1. katman): ANAYASA.md, sirket/* (7 dosya), takimlar/*/kurallar.md (6 dosya) ve denetim/BEKCI-KURALLARI.md bu commit'lerde ilk kez OLUŞTURULUYOR; dogrula.py 14 KORUNAN bulgusu veriyor. Kurala göre bu doğrudan RED sebebidir ve yalnızca Bora birleştirebilir. Ben bulguyu kendi başıma yok sayamam (BEKCI-KURALLARI korunan dosya). RED yerine İNSAN ONAYI GEREKLİ veriyorum çünkü: (a) önceden Bora onaylı bir sürümün üzerine yazılan bir değişiklik yok, manifesto §09 "maddeleri ANAYASA.md içerisinde oluştur" diyor; (b) asıl soru dosyaların içeriğinin Bora'nın niyetine uyup uymadığı ve bunu yalnızca Bora söyleyebilir. Bora bu 14 dosyayı okuyup onaylamadan G-0001 tamamlanmış sayılmaz.
- 16 / YETKI-MATRISI kural 1 ve A4: DURUM.json G-0001'i "onay: A0" olarak işaretlemiş (vardiyalar/DURUM.json G-0001) ama bu görev A4 dosyalarını (ANAYASA, sirket/, kurallar.md) oluşturuyor; matris A0 tanımında "Anayasa/sirket/kurallar hariç" diyor. Yani görev kendi matrisine göre A0 olamaz. Gerekçe makul (Bora'nın manifesto talimatı) ama kuyrukta "Bora, 2026-11-27, manifesto §09" gibi açık onay yazılmamış.
- 7 (Anayasa 19) / mekanik koruma boşluğu: dogrula.py KORUNAN listesi (scripts/dogrula.py satır 20) yalnızca ANAYASA.md, sirket/, kurallar.md ve BEKCI-KURALLARI.md'yi kapsıyor. YETKI-MATRISI A4 "bütçe sınırları, güvenlik kuralları" da Bora'ya ait diyor, ama vardiyalar/CONFIG.json (bütçe, limitler), .claude/agents/bekci.md, scripts/dogrula.py ve tests/ korumasız: bir ajan bunları değiştirip Bekçi'yi veya bütçe sınırını zayıflatsa 1. katman RED vermez. Düzeltilmesi Bora'nın kararıdır (korunan liste).
- 7 (Anayasa 17 / M-001 tek kaynak): CONFIG.json "tek kaynak" ilkesi büyük ölçüde tutuyor (YONETICI.md'de sıklık sayısı yok, gorev_sec ve kilit.sh CONFIG'den okuyor). Ama kontrol yalnızca YONETICI.md'de regex arıyor (dogrula.py satır 23, 98-100): KARARLAR.md:13 (K-006) "3 saatte bir" yazıyor (CONFIG aralik_saat: 3 ile aynı sayı, ikinci kaynak); düzeltme hakkı "iki / 2" sayısı sirket/AJAN-KIMLIGI.md:29, denetim/BEKCI-KURALLARI.md:38, .claude/commands/kos.md:11 ve tests'te ayrı yazılı (CONFIG limitler.bekci_duzeltme_hakki: 2); Higgsfield bakiyesi 1.935,39 CLAUDE.md:36, finans/BUTCE.md:9 ve CONFIG'de üç kez. Bunlar şu an tutarlı (çelişki yok) ama ALONI'deki çelişki hatasının kaynağı olan yapı. Not düzeyinde.
- 15: hafiza/BASARISIZLIKLAR.md:4 referans video başarısızlığını "G-0002" diye kaydetmiş; görev G-0003 (G-0002 ortam denetimi). vardiyalar/DEVIR-TESLIM.md "G-0006 sürüyor" diyor, DURUM.json G-0006'yı review gösteriyor (eski bilgi).
ANAYASA 24 MADDE KONTROLÜ (manifesto §09 ile satır satır): 24 madde de ANAYASA.md'de var, numaralar ve başlıklar aynı. Anlam kaybı yok. Fark listesi (hepsi izlenebilir, ikisi Bora'nın bilmesi gereken):
  * Madde 1: eklenmiş cümle "Kaynağı gösterilemeyen sayı çıktıya girmez" manifestoda yok; Chief of Staff ilavesi (ruhuna uygun, Bora bilmeli).
  * Madde 11: manifesto "organik tartışma, absürt mizah, parodi ve yaratıcı provokasyon DEĞERLENDİRİLEBİLİR" der; ANAYASA "serbesttir" yazıyor ve "yaratıcı provokasyon" düşmüş. "Serbest" "değerlendirilebilir"den güçlü; yasak listesi aynen duruyor, risk düşük ama Bora'nın görmesi gereken bir söz değişikliği.
  * Madde 10: "hesap açma" ve "ödeme" eklenmiş (kısıtı sıkılaştırıyor; manifesto §30/§37 ile uyumlu).
  * Madde 3 "diploma", Madde 18 "indirgenemez" cümlesi, Madde 22 ilk cümlenin "psikolojik sorunlarını sömürmek" ifadesi kısaltılmış; anlam korunmuş.
  * "Uygulama notu" (çelişki sırası ANAYASA → YETKI-MATRISI → CLAUDE.md → YONETICI.md → takım dosyaları; "bu dosyada değişiklik doğrudan RED") manifestoda yok; Chief of Staff eklemesi, BEKCI-KURALLARI madde 3 ile tutarlı.
YETKİ MATRİSİ ↔ KURULUŞ EMRİ (manifesto satır 3195 "ücretli üretim, gerçek yayın, dış iletişim veya yeni harcama için genel yetki vermiyorum"): UYUMLU. A2 deney bazında + azami kredi, A3 yalnızca Bora iş bazında, "Kalıcı yetkiler" tablosu boş, CONFIG genel_harcama_yetkisi:false, zamanlayıcı pasif, DURUM.json'da A2/A3 görevlerin hiçbiri onaylı değil (G-0010..G-0013, G-0018 onay=None). Tek genişleme: matris kural 4, MCP'lerde bakiye/model/fiyat OKUMA sorgularını A0 sayıyor; bu manifestoda yazmıyor, Chief of Staff'ın yorumu (G-0007 bu yoruma dayanıyor). Bora onayı kapsamına alınmalı.
MANİFESTO İLKE ÖRNEKLEMİ (§11–§36'dan 5 ilke, dosyalarda arandı): 
  * §20 puanlama ağırlıkları (20/20/15/10/10/10/10/5 + 80/65/50 bantları) → konseyler/medya-mahkemesi/MAHKEME.md'de aynen VAR; "Bekçi veto'su puandan bağımsız" VAR.
  * §21 %60/%30/%10 dağılımı ve "kesin harcama yetkisi değildir" → STRATEJI.md ve finans/BUTCE.md'de VAR.
  * §33 vardiya raporu 7 başlık → raporlar/templates/VARDIYA-RAPORU.md aynen VAR.
  * §36 kalıcı yayın yetkisi sınırları (hesap, platform, kategori, Bekçi onayı, sıklık, süre, durdurma) → YETKI-MATRISI "Kalıcı yetkiler" sütunları VAR.
  * §18 erken sinyal 12 madde: KISMEN KAYIP. takimlar/pazar-istihbarati/takim.md:13 "manifesto §18'in 12 sinyali" diye yalnızca atıf yapıyor; 12 sinyalin listesi arsiv/ dışında hiçbir yerde yok ve pazar-istihbarati ajanının okuma listesinde arsiv/ yok (hafızasız ajan okuyamaz). Trend radarında (istihbarat/trend-radari) 6 serbest "erken sinyal" var, 12'ye eşlenmemiş. Düzeltme: 12 sinyalin listesini takim.md'ye (korunan değil) taşımak; kurallar.md korunan olduğundan oraya yazılmaz.
ÖRNEKLEM DOĞRULAMASI: Bu görev araştırma değil; örneklem G-0003–G-0007 bloklarında.
NOTLAR: Testler gerçek ve geçiyor; testlerde silinmiş/atlanmış test yok. Kilit mekanizması test_kilit.sh'de geçici depolarda sınanıyor (uzak repo yok). Kuru koşu kaydı (vardiyalar/run-logs) kendi açık sorunlarını dürüstçe listeliyor (etkileşimli oturumu kilide zorlayan mekanizma yok; PR akışı sınanamadı). Yöntem olarak iyi: kuruluş dosyalarında uydurma sayı veya "yayında/kanıtlandı" abartısı görmedim.
DÜZELTME İÇİN: Bora ANAYASA.md, sirket/*, takimlar/*/kurallar.md ve denetim/BEKCI-KURALLARI.md'yi (özellikle Madde 1, 10, 11 söz farkları ve A0 sayılan MCP okuma sorguları) okuyup onaylamalı; G-0001 onayı "Bora, 2026-11-27, kuruluş dosyaları" olarak kayda geçmeli, korunan dosya listesine CONFIG.json ve bekci.md/dogrula.py eklenip eklenmeyeceğine Bora karar vermeli.
```

---

```
KARAR: ONAY
GÖREV: G-0003   TAKIM: pazar-istihbarati   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- (yok) Dosya kendi sınırını dürüstçe yazıyor: üç video açılamadı, içerik "bilinmiyor"; KALITE-STANDARTLARI madde 4 (erişilemeyen kaynaklar) ve manifesto §03 talimatı ("erişemediğin videoyu izlemiş gibi davranma") yerine getirilmiş. Manifesto §03 satırlarındaki 1.047/389/658 $ ve 23×12=276 $ iddiaları dosyada doğru aktarılmış ve "doğrulanamadı" etiketli.
ÖRNEKLEM DOĞRULAMASI:
- 276 − 99 − 19,52 = 157,48 $ aritmetiği: tuttu (hesapladım).
- Mark Tilbury "I Tried The LAZIEST Way to Make Money With AI" 7 günlük AI influencer deneyi, Claude + Higgsfield, yüz yok: tuttu (transkript özeti sitelerinde başlık ve kurgu eşleşiyor). Aranan 23 satış / 12 $ / 276 $ rakamları arama özetimde çıkmadı: doğrulanamadı; dosya zaten bunu "yaratıcının beyanı, bağımsız teyit yok" diye etiketliyor, abartı yok.
- Dosyanın "kurucunun üç video ID'si bu içeriklerle eşleşmedi" tespiti: arama kendi tarafımda da üç ID'yi vermedi; tutarlı.
NOTLAR: Higgsfield "yıllık gelir hızı 13 ile çarpılıyor" ve Adweek sponsor notu üçüncü taraf özetinden; kullanılmadan önce yeniden bakılmalı (dosya zaten öyle diyor). G-0009 (ağ izni sonrası yeniden inceleme) bekliyor; bu ONAY, videoların içeriği hakkında değil, dosyanın dürüstlüğü hakkındadır.
DÜZELTME İÇİN: Gerekmiyor.
```

---

```
KARAR: DÜZELTME GEREKLİ
GÖREV: G-0004   TAKIM: pazar-istihbarati   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- 14 / KALITE-STANDARTLARI 1-5: istihbarat/platform-analizleri/2026-11-27-gelir-modelleri.md §4 madde 4 "Instagram Gifts ve YouTube fan funding … Küçük ama doğrulanmış gelir" yazıyor; aynı dosyanın tablosu (satır 3 ve 8) bu iki yol için "Gelir verisi bilinmiyor", platform dosyası Instagram Gifts için güven "Orta" (2023 ülke listesi) diyor. Doğrulanan şey erişim uygunluğu (o da orta güven); gelir doğrulanmış değil. "Doğrulanmış" etiketi abartılmış.
- 14: gelir-modelleri.md §4 madde 2 ve platform-kurallari.md §6 madde 8 "YouTube'u önceliklendir / Mümkünse 31 Ocak 2027'den önce eşiği geçmeyi hedefle", "Bu tarih, YouTube'a öncelik vermek için bir neden". İki sorun: (a) 31 Ocak 2027 yeni eşiklerin geçerlilik tarihi değil Studio'da yeni şartların KABUL son günü; yeni eşikler 1 Şubat 2027'de başvuranlara uygulanıyor (dosya satır 42'de doğru yazıyor, öneride karışmış). (b) Henüz hesap yokken (hesap açma A3, onaysız) ~65 günde 1.000 abone + 4.000 saat ya da 10M Shorts görüntüleme hedefi gerçekçilik kontrolü olmadan öneriliyor; dosyanın kendi RPM hesabıyla (10M × ~$0,05 ≈ $500) bile sınırlı değer. Öneri "öneri" etiketli ama dayanağı yok.
- 11/12: gelir-modelleri.md tablo satır 10 "TikTok Shop Yunanistan'da yok" kesin yazıyor; platform dosyası aynı konuda "açılış teyit edilmedi, aday ülke" diyor (Orta güven). İki dosya birbirini tutmuyor; "bilinmiyor/teyit edilmedi" olmalı.
ÖRNEKLEM DOĞRULAMASI (5 iddia):
- YouTube YPP 1 Şubat 2027: yeni başvuranlar 1.000 abone + 8.000 saat (365 gün) YA DA 90 günde 20M nitelikli Shorts; mevcut üyeler etkilenmiyor; Shorts Creator Pool payı için 90 günde 10M şartı; Studio'da 31 Ocak 2027'ye kadar yeni şartların kabulü; Fan Funding/alışveriş (500 abone / 3.000 saat / 3M) değişmiyor: TUTTU (YouTube blog'u ve vidIQ, NewscastStudio, SEJ, TheNextWeb, MediaPost özetleri aynı; basın dilinde 10M şartı "mevcut kuralın devamı" olarak da anlatılıyor, dosya bunu mevcut tabloda tutarlı veriyor). "Premium'dan pay" ibaresi arama özetlerimde çıkmadı: doğrulanamadı (not).
- Shorts Creator Pool'da yaratıcı payı %45: TUTTU.
- TikTok Creator Rewards: 10.000 takipçi, 30 günde 100.000 görüntüleme, en az 1 dakikalık video, 18+; Yunanistan hiçbir listede yok: TUTTU (ülke listeleri kaynaklar arasında çelişkili, resmi liste yok; dosya bunu zaten "büyük olasılıkla uygun değil, resmi teyit yok" diye yazıyor).
- Instagram Graph API kayan 24 saatte 50 gönderi (karusel 1): TUTTU (Meta sayfalarında 50; bir Markdown kopyasında 100 görülüyor, dosya "bazı eski sayfalarda 25/100" notunu zaten taşıyor).
- AB AI Yasası Madde 50(4) deployer deepfake etiketi 2 Ağustos 2026'dan beri yürürlükte; Digital Omnibus ile 50(2) işaretleme 2 Aralık 2026'ya ertelendi (yalnızca piyasadaki sistemler için): TUTTU; Omnibus'un resmen kabulü kaynaklarda çelişkili, dosya bunu "doğrulanamadı" diye yazıyor.
NOTLAR: Genel kalite yüksek: her sayı URL + görülme tarihi taşıyor, "bilinmiyor" bol kullanılmış, kaynak türü (Resmi arama özeti / İkincil / RAPOR / İDDİA) etiketli ve sayfaların açılamadığı en başta söyleniyor (§0). "Resmi (arama özeti)" etiketi sayfalar açılmadığı için doğrulama gücü olarak orta okunmalı. İddia edilen 2027 eşik değişikliğini bağımsız olarak doğruladım; G-0014 bu iddiayı "resmi kaynaktan doğrula" diye bekliyor, bu denetim ikincil kaynaklarla ve YouTube blog sonucuyla teyit etti ama resmi yardım sayfasını açmadı. Yunan vergi/AADE notu ve "hukuki görüş değildir" uyarısı yerinde.
DÜZELTME İÇİN: "Doğrulanmış gelir" ifadesini erişim uygunluğu (orta güven) olarak düzelt, 31 Ocak 2027 önerisini terimler kabul tarihi ile eşik tarihini ayırarak ve gerçekçilik/A3 notuyla yeniden yaz, TikTok Shop satırını platform dosyasıyla aynı hâle getir.
```

---

```
KARAR: ONAY
GÖREV: G-0005   TAKIM: pazar-istihbarati   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- (yok) Dosya, KALITE-STANDARTLARI 1, 4, 5, 6 ve pazar-istihbarati kurallarına uyuyor: erişilemeyen siteler baştan söyleniyor, hiçbir cümle birebir alıntı değil (parafraz), her satır GÜÇLÜ/ORTA/ZAYIF güç etiketi taşıyor, doğrulanamayan iddialar ("ona atfetme / kullanma") ayrıca işaretli, persona soruları "X şöyle düşünürdü" değil "belgelenmiş yöntemine göre" biçiminde (Anayasa 14, konseyler/README kural 4), 9 maddelik doğrulama listesi sonda (G-0015).
ÖRNEKLEM DOĞRULAMASI (3 iddia):
- Khaby Lame, Ocak 2026'da şirketini (Step Distinctive) Rich Sparkle Holdings'e ~975 milyon dolarlık tamamı hisse anlaşmasıyla sattı, yüz/ses/davranış "AI dijital ikiz" izni dahil; sonra anlaşma sönümlendi (hisse >%90 düştü, kapanış belirsiz, aracı kurumlar işlemi kısıtladı): TUTTU (Fortune, Bloomberg, Entrepreneur, TheWrap, Tubefilter özetleri). Dosyadaki "değer yaklaşık %90 düştü" ifadesi anlaşmanın değil hisse fiyatının düşüşü; kaynaklara göre doğru ama cümle kayıyor (not).
- Ryan Trahan "50 States in 50 Days" St. Jude için 11 milyon doların üstünde bağış (Haley Pham ile): TUTTU (YouTube blog, Wikipedia, Tubefilter özetleri; 11–11,65M).
- Fruit Love Island hesabı 13 Mart 2026'da açıldı, ~9 günde ~300 milyon izlenme; hesap sonra silindi: TUTTU (Star, RTÉ, Designrush, Gizmodo özetleri; takipçi 3,2–3,3M).
NOTLAR: Doğrulayamadığım ama dosyanın zaten "doğrulanmadı" etiketlediği kalemler (MrBeast el kitabı dakika çizelgesi, Paddy Galloway "40 kat", Duolingo Meltwater sayıları) bu ONAY'ın dışındadır; G-0015 kontrol listesi bunları kapsıyor. Hayatta kalma yanlılığı bölümü kısmi: karşı örnekler var (Viewstats AI küçük resim aracının geri çekilmesi, Kamonegi Ahiru, Khaby anlaşması) ama her creator için başarısız taklitçi örneği yok; KALITE madde 3'ün "bulunamadıysa yazılır" şartı genel olarak karşılanıyor.
DÜZELTME İÇİN: Gerekmiyor.
```

---

```
KARAR: DÜZELTME GEREKLİ
GÖREV: G-0006   TAKIM: pazar-istihbarati   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- 14 / KALITE-STANDARTLARI 2, 13 / Anayasa 9: istihbarat/rakip-analizleri/2026-11-27-ilk-tarama.md Kart 19 (satır 465) "Gelir modeli: sektör düzeyinde doğrulanmış uygulama içi gelir" yazıyor, ama aynı satır 150 milyar $ / 4 milyar $ rakamlarını "tahmin" ve "AI satıcısı kaynaklı tahminler" diye tanımlıyor. Tahmin "doğrulanmış" etiketiyle sunulmuş; şablon (ARASTIRMA-KARTI) "doğrulanmış / iddia / bilinmiyor" ayrımı için doğru etiket "iddia"/"tahmin".
- 14 / KALITE 1: aynı dosya Kart 20 (Maverick Maltin, satır 489) "iddia, kısmen doğrulanmış": kaynak yaratıcının birinci şahıs Business Insider yazısı; "BI belgelerle doğruladı" bilgisi ikincil bir siteden ve kendileri teyit edemediklerini yazıyor. Doğrulama yapılmadığı için etiket "iddia" olmalı. istihbarat/pazar-firsatlari/2026-11-27-ilk-firsatlar.md satır 12 ve 111 "doğrulanmaya en yakın gelirler: Maltin, Meow Ziqi" diyor; Meow Ziqi için sponsorluk tutarı hiç yok, Maltin yalnızca beyan.
- 14: Kart 13 (Basin Creek, satır 323) "Gelir modeli: doğrulanmış (mağaza var)": doğrulanan şey bir mağaza bağlantısının varlığı; satış hacmi bilinmiyor. Gelir modeli "doğrulanmış" değil "iddia/bilinmiyor (mağaza bağlantısı görüldü)".
- 8 / pazar-istihbarati takim.md adım 4 ("veri yetmiyorsa sınıflandırma yapma"): istihbarat/trend-radari/2026-11-27-trend-radari.md ana tablo #10 "What if alternatif tarih: Saturated, güven düşük" ve kanıt sütunu "(doğrulanmadı)"; kanıt olmadan evre atanmış. Benzer şekilde #12 "Emerging/düşük" kabul edilebilir, #10 değil.
- 11: tutarsız sayılar: Fruit Love Island rakip-analizleri Kart 2 ve trend radarı "20 bölüm ~300M", Kart B1 "22 bölümden 12'si kaldırıldı", pazar-firsatlari "9 günde 3,1 milyon takipçi" (kaynak kloss_xyz X paylaşımı; haberlerde 3,2–3,3M). Küçük farklar, açıklanmamış.
ÖRNEKLEM DOĞRULAMASI (6 iddia, hepsi tuttu):
- Fruit Love Island: 13 Mart 2026 açılış, ~9 günde ~300M izlenme, hesap silindi: TUTTU (3,2–3,3M takipçi haberleri; dosyanın 3,1M'i X paylaşımına dayanıyor, kaynağıyla tutarlı).
- Bandar Apna Dost: 2,76M abone, 2,07 milyar izlenme (Business Standard, 31 Aralık 2025, Kapwing/SocialBlade tabanlı); Kapwing'in 4,25M $ yıllık gelir tahmini kullanılmamış: TUTTU. Dosyanın "gelir verisi olarak kullanılmamalı" yaklaşımı doğru.
- YouTube Ocak 2026'da 16 AI kanalı (35M+ abone, 4,7 milyar izlenme) sildi/boşalttı: TUTTU (Tubefilter, Kapwing güncellemesi; kaynaklarda 11 silindi 5 boşaltıldı).
- Veo 3.1 Lite 31 Mart 2026, 720p'de saniyesi 0,05 $: TUTTU (Google blog ve Decoder; Vertex'te farklı fiyat ve bir forum faturalama uyarısı var, dosya Gemini API fiyatını veriyor).
- OpenAI Sora uygulamasının kapatılması 24 Mart 2026'da duyuruldu: TUTTU (Axios, CBS, OpenAI yardım sayfası; web/uygulama 26 Nisan'da, API 24 Eylül 2026'da kapanacak şeklinde duyurulmuş; dosya yalnızca "kapatacağını açıkladı" diyor, doğru).
- Meow Ziqi 1,76M takipçi, 500M+ görüntüleme, marka sponsorlukları (SCMP): TUTTU (başlık ve açılış özeti; sponsor ayrıntıları özette yoktu).
NOTLAR: Genel yöntem iyi: Bölüm B (başarısız/kapanan örnekler, hayatta kalma yanlılığı) ve Bölüm C ("kullanmayın" listesi: Revid iddiaları, Kapwing gelir tahminleri) örnek niteliğinde; Hipotez dosyası açıkça "Hipotez" ve "karar değil" etiketli, ücretli üretim yok, gerçek marka parodisi önerilmiyor (Hipotez 3 telif riskini yazıyor), çocuk hedeflemesinden kaçınıyor. Araştırma kısıtları 10 madde. Radar'daki Kolsquare "-%21,2" etkileşim cezası ve Gemini Omni fiyatı bu denetimde sınanmadı. Ülke kısıtı: Çin verileri ikincil aktarım, dosya bunu söylüyor.
DÜZELTME İÇİN: Kart 19, 20, 13'teki "doğrulanmış/kısmen doğrulanmış" etiketlerini "iddia/tahmin" yap, fırsatlar dosyasındaki "doğrulanmaya en yakın gelirler" cümlesini buna göre yumuşat, radar #10'dan evre sınıflandırmasını kaldır (veya "sınıflandırılamadı" yaz) ve bölüm sayısı farkını açıkla.
```

---

```
KARAR: DÜZELTME GEREKLİ
GÖREV: G-0007   TAKIM: chief-of-staff (üretim/maliyet keşfi)   SHA: d7d85176c825978b98b8777e9c582a6ddf590848
GEREKÇELER:
- 11 / 14 (Anayasa 1, KALITE 14): produksiyon/model-testleri/2026-11-27-maliyet-kesfi.md "Çıkarımlar" 1: "En pahalı ile en ucuz arasında ~14 kat fark var … aynı süre bütçe modellerinde 4–8 kredi." 14 = 56/4, yani 8 sn · 720p · sesli Seedance 2.5 varsayılan ile 6 sn · 768p Hailuo 2.3-fast klibinin klip başı kredisi. "Aynı süre" doğru değil (4 kredilik klip 6 sn). Saniye başına tablonun kendi sütunuyla oran 7,0 / 0,67 ≈ 10,5 kat. Ses, süre ve çözünürlük de farklı. Aynı yanlış oran vardiyalar/DEVIR-TESLIM.md "Öğrenildi" satırında ("14 kat") tekrarlanıyor.
ARITMETIK KONTROL (yeniden çağrı yapmadan, dosya içi): saniye başı sütunu tüm satırlarda doğru (4/6=0,67; 7,5/5=1,5; 8/8=1; 20/8=2,5; 24/8=3; 40/8=5; 56/8=7); 1.935/56 ≈ 34, 1.935/8 ≈ 242 (≈240); benchmark 4+8+56 = 68. Hepsi tutuyor.
KREDİ ≠ PARA: dosyada kredi hiçbir yerde € veya $ ile çarpılmıyor; plan ücreti ve kredi yenilenmesi "açık soru (Bora)" olarak bırakılmış; "unlim.available=false" ve manifestodaki 3 ücretsiz hak doğrulanamadı diye yazılmış (KALITE 14, finans/BUTCE.md ile tutarlı): UYUMLU.
Harcanan kredi 0, finans/kredi-kayitlari.csv ve benchmark.csv yalnızca başlık satırı: dosyayla tutarlı. A2 gerektiren hiçbir üretim yok; yalnızca okuma sorguları (matris kural 4 yorumu için G-0001 notuna bak).
ÖRNEKLEM DOĞRULAMASI: Kredi tahminlerini yeniden çağırmam istenmedi; fiyatları bağımsız doğrulayamadım (Higgsfield araç yanıtları web'de yok). Yalnızca dosya içi tutarlılık ve manifesto/BUTCE ile karşılaştırma yapıldı. Doğrulanamadı: tablo değerleri.
NOTLAR: Tahminler "tahmini kredi" ve "hipotez — kalite test edilmedi" diye etiketli, "kanıtlanmadı" ifadesi var (iyi). Karşılaştırma tablosunda modeller farklı süre/çözünürlük/ses ayarlarında; "bütçe modeli" karşılaştırmasını aynı ayara getiren ikinci bir tablo benchmark öncesi faydalı olur. Kling fiyatları okunmadı (dosya söylüyor).
DÜZELTME İÇİN: "~14 kat"ı saniye başına kredi üzerinden (~10,5 kat) ve ayar farklarını belirterek yeniden yaz, "aynı süre" ifadesini düzelt ve DEVIR-TESLIM.md'deki aynı rakamı güncelle.
```
