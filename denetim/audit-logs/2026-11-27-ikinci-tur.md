# İkinci tur denetimi — 2026-11-27

Denetçi: Bekçi (`.claude/agents/bekci.md`). Denetlenen SHA: `f75fff6eecc2f05831ab00bc19b855aa484f5b9b` (`git rev-parse HEAD` ile doğrulandı).
Kapsam: (1) G-0004, G-0006, G-0007 düzeltme turu 1/2 (düzeltmeler `d7d8517..5f1d4ba`); (2) G-0008 ilk denetim.
`git diff 5f1d4ba f75fff6` yalnızca `konseyler/kalibrasyon.csv`, `scripts/mahkeme_skor.py`, tutanak, muhalefet konsey dosyası ve `DURUM.json` dosyalarına dokunuyor; G-0004/6/7 dosyaları 5f1d4ba ile HEAD arasında değişmedi, yani onay HEAD için de geçerli.
Üreticiler: pazar-istihbarati (G-0004, G-0006), Chief of Staff (G-0007 düzeltmesi, G-0008 tutanağı/sentez), kreatif-direktor (gündem dosyaları, Tomruk). Bekçi bu işleri üretmedi.

## Çalıştırılan mekanik kontroller (kendim)
- `python3 -I scripts/dogrula.py --degisen $(git diff --name-only d7d8517 5f1d4ba)` → **2 BULGU, ikisi KORUNAN:** `ANAYASA.md`, `scripts/dogrula.py` (aşağıda "Korunan dosya" bloğu).
- `python3 -I scripts/dogrula.py --degisen $(git diff --name-only 5f1d4ba f75fff6)` → TEMİZ.
- `python3 -I tests/test_gorev_sec.py` → 14/14 geçti.
- `python3 -I scripts/mahkeme_skor.py <4 konsey dosyası> --ek "Üçüncü Kat:maliyet=5" "Dağ Kileri:maliyet=6" "Kayıp Eşya Bürosu:maliyet=7"` → **60,9 / 50,4 / 57,6**; tutanaktaki skor tablosunun 24 hücresi ve 3 toplamı birebir tutuyor.

## Araştırma kısıtı
Yalnızca WebSearch; hiçbir kaynak sayfası tam metin açılmadı. "Tuttu" = arama özetlerinde aynı değer/tarih görüldü.

---

```
KARAR: ONAY
GÖREV: G-0004   TAKIM: pazar-istihbarati   SHA: f75fff6eecc2f05831ab00bc19b855aa484f5b9b
GEREKÇELER (önceki üç gerekçe tek tek):
- "Doğrulanmış gelir" abartısı: GİDERİLDİ. gelir-modelleri.md §4 madde 4 artık "Küçük gelir; programın Yunanistan'da varlığı kaynaklı, bizim için gelir tutarı bilinmiyor" diyor; tablo satır 8 ile tutarlı.
- 31 Ocak 2027 / gerçekçilik: GİDERİLDİ. gelir-modelleri.md §4 madde 2 ve platform-kurallari.md §6 madde 8 + "Bizim için anlamı" (satır 45): 31 Ocak = mevcut üyelerin kabul son günü, eşik tarihi 1 Şubat; "~65 günde 1.000 abone + 10M Shorts gerçekçi varsayılmamalı". Kaynak metin (platform-kurallari satır 42) ile çelişki kalmadı.
- TikTok Shop çelişkisi: GİDERİLDİ. gelir-modelleri.md tablo satır 10 "açılışı teyit edilmedi (kaynaklar çelişkili)"; platform-kurallari.md satır 90 ve 222 ile aynı.
ÖRNEKLEM DOĞRULAMASI: İlk denetimdeki YPP 1 Şubat 2027 eşikleri ve 31 Ocak kabul tarihi örneklemi geçerli (düzeltilmiş metin ona uyuyor); bu turda yeni kaynaklı iddia eklenmedi.
NOTLAR (RED sebebi değil):
- Üretici dosyalara "Bekçi düzeltmesi" / "Bekçi örneklemle doğruladı" ibareleri yazılmış (gelir-modelleri §4 madde 2, platform-kurallari satır 45). Doğrulama gücü arama özetidir; ibare, resmi sayfa açılana kadar (G-0014) "kesin" okunmamalı.
- gelir-modelleri §4 madde 2 hâlâ "Yunanistan'da doğrulanmış tek güçlü yol" diyor; bu erişim uygunluğu (arama özeti, orta güven), gelir değil. Bir sonraki tarama turunda "uygun olduğu görüldü (orta güven)" yap.
DÜZELTME İÇİN: Gerekmiyor.
```

---

```
KARAR: ONAY
GÖREV: G-0006   TAKIM: pazar-istihbarati   SHA: f75fff6eecc2f05831ab00bc19b855aa484f5b9b
GEREKÇELER (önceki beş gerekçe tek tek):
- Kart 19 "doğrulanmış" etiketi: GİDERİLDİ (ilk-tarama.md Kart 19: "sektör tahmini (satıcı kaynaklı, doğrulanmamış)").
- Kart 20 Maltin: GİDERİLDİ ("iddia (yaratıcının kendi beyanı; bağımsız doğrulama bizce yapılamadı)").
- Kart 13 Basin Creek: GİDERİLDİ ("iddia/bilinmiyor; yalnızca mağaza bağlantısı görüldü"). Davis kartı da "iddia, üçüncü tarafça incelenmiş" olarak sıkılaştırılmış.
- ilk-firsatlar.md madde 4 "doğrulanmaya en yakın gelirler": GİDERİLDİ ("bağımsız doğrulanmış gelir yok; en güçlü beyanlar ...").
- Trend radarı #10: GİDERİLDİ ("sınıflandırılamadı (veri yetersiz; Saturated şüphesi)").
- Fruit Love Island bölüm sayısı: KISMEN giderildi, kabul edilebilir. Kart 2 artık "~20 (kaynaklar 20-22 arası çelişiyor)"; Kart B1 3,1M/3,3M ve 22 bölüm/12 kaldırıldı farklarını kendi içinde veriyor.
KAPSAM DIŞI YENİ HATA: yok.
ÖRNEKLEM DOĞRULAMASI: İlk turdaki 6 iddia geçerli; bu turda yeni kaynaklı iddia eklenmedi.
NOTLAR (RED sebebi değil):
- ilk-firsatlar.md satır 111 (madde 8) "Doğrulanmış gelir neredeyse yok. Davis ... ve Maltin ... dışındaki rakamlar beyan" diyor; satır 12 ise "bağımsız doğrulanmış gelir yok" diyor. İki cümle birbirinden hafif farklı sertlikte; satır 111'i satır 12 ile aynı yap.
- ilk-firsatlar.md satır 39 "9 günde 3,1M takipçi" tek rakamı veriyor; B1 3,1–3,3M aralığını taşıyor.
DÜZELTME İÇİN: Gerekmiyor.
```

---

```
KARAR: ONAY
GÖREV: G-0007   TAKIM: chief-of-staff (üretim/maliyet keşfi)   SHA: f75fff6eecc2f05831ab00bc19b855aa484f5b9b
GEREKÇELER (önceki gerekçe):
- "~14 kat / aynı süre": GİDERİLDİ. maliyet-kesfi.md Çıkarımlar 1: "saniye başına 7,0 ile 0,67 arasında ~10,5 kat (8 sn klipte 56 vs 8 kredi = 7 kat)"; tablo satırlarıyla yeniden hesapladım: 7,0/0,67 = 10,4-10,5; 56/8 = 7 ✓. "Aynı süre" ifadesi kalmadı. vardiyalar/DEVIR-TESLIM.md "Öğrenildi" satırı aynı rakamlara güncellenmiş. Depoda kalan "14 kat" yalnızca denetim kayıtlarında/defterde (alıntı olarak).
KAPSAM DIŞI YENİ HATA: yok. Yeni dış denetim paketi (`denetim/dis-denetim/2026-11-27-kurulus-paketi.md`) düzeltilmiş rakamları doğru kullanıyor.
ÖRNEKLEM DOĞRULAMASI: Fiyatlar dosya içi tutarlılıkla kontrol edildi, bağımsız doğrulanamadı (önceki turdaki durum).
NOTLAR: Karşılaştırma tablosunda modeller hâlâ farklı süre/çözünürlük/ses ayarında; benchmark (G-0012) öncesi aynı ayara getiren tablo faydalı olur.
DÜZELTME İÇİN: Gerekmiyor.
```

---

```
KARAR: İNSAN ONAYI GEREKLİ
GÖREV: G-0001 (ek: korunan dosya değişiklikleri)   TAKIM: chief-of-staff   SHA: f75fff6eecc2f05831ab00bc19b855aa484f5b9b
GEREKÇELER:
- 3 (1. katman): `ANAYASA.md` madde 11 metni 5f1d4ba'da manifesto §09 Madde 11 metnine geri döndürüldü ("Organik tartışma, absürt mizah, parodi ve yaratıcı provokasyon değerlendirilebilir"). Manifestoyla karşılaştırdım: birebir uyuyor, ilk denetimdeki "serbesttir" farkı kapandı. Ama dosya korunan; yalnızca Bora birleştirebilir. Madde 1'deki "Kaynağı gösterilemeyen sayı çıktıya girmez" eklemesi ve madde 10 eklemeleri hâlâ yerinde ve K-B1 (DURUM.json bekleyen_kararlar) hâlâ cevapsız.
- 3 (1. katman): `scripts/dogrula.py` KORUNAN listesi genişletildi (CONFIG.json, .claude/agents/bekci.md, scripts/dogrula.py, denetim/ONAY-PROTOKOLU.md). Bu, ilk denetimin tavsiyesini uyguluyor ve ONAY-PROTOKOLU.md gerçekten var; ama koruma listesinin kendisi korunan bir dosyada ve kendi kendini kapsıyor. Değişikliği Bora görmeli. Hâlâ korumasız: `scripts/gorev_sec.py`, `scripts/kilit.sh`, `scripts/mahkeme_skor.py`, `tests/`, `.claude/commands/`. (Silinmiş test kuralı testleri kısmen korur; skor betiği mahkeme sonucunu belirliyor.)
NOTLAR: G-0001 DURUM.json'da "A4, onay: null, waiting_owner" olarak düzeltilmiş (ilk denetimdeki A0 etiketi sorunu kapandı). Bu blok G-0004/6/7 ONAY'larını engellemez; kuruluş dosyalarının onayı Bora'dadır.
DÜZELTME İÇİN: Bora ANAYASA.md (madde 1, 10, 11) ve dogrula.py KORUNAN listesini onaylar; K-B1 cevabı `KARARLAR.md`'ye yazılır, G-0001 onayı "Bora, <tarih>, kuruluş dosyaları" olarak kayda geçer.
```

---

```
KARAR: DÜZELTME GEREKLİ
GÖREV: G-0008   TAKIM: kreatif (gündem, Tomruk) + konsey (Mahkeme #1, Chief of Staff sentezi)   SHA: f75fff6eecc2f05831ab00bc19b855aa484f5b9b
GEREKÇELER:
- 14 / Anayasa 1, 6 / MAHKEME.md akış 4 (azınlık görüşü kaydı): tutanak satır 42 "Uzman (özgünlük 8): Kayıp Eşya Bürosu en savunulabilir uzun vadeli IP" diyor. Uzman dosyasında bu cümle yok (`savunulabilir` yalnızca gündem dosyasında geçiyor, başka anlamda). Uzman Kayıp azınlık görüşü (uzman-konseyi.md ~satır 236): Visual Director ve Consumer/Marketing fikri "sanatsal ama ölçeksiz" buluyor; Sociologist/Behavioral küçük ama bağlı kitle ve ucuzluk nedeniyle riski kabul edilebilir buluyor. Özgünlük 8 puanı gerçek (Sociologist, Visual), "IP" yorumu tutanağın eklemesi. Aynı bölümde satır 41 Creator'a "gelire dönüşme 5,3" atfediyor; 5,3 üç konseyin ortalaması, Creator'ın kendi puanı 6 (creator-konseyi.md satır 68; azınlık metni satır 84), Trahan profili gelir puanı vermemiş.
- 14 / MAHKEME.md akış 4: tutanağın azınlık bölümünde Muhalefet Konseyi yok. Muhalefet dosyasında güçlü bir azınlık görüşü var: Chaos Director ve Anti-Trend Analyst Kayıp Eşya Bürosu'nun "üçü içinde tek gerçek deney adayı" olduğunu savunuyor (muhalefet-konseyi.md satır 306); Anti-Trend, ses testi geçerse Dağ Kileri'nin "en uzun ömürlü kategori" olup "ilk sırada olabileceğini" söylüyor (satır 211). Her ikisi de tutanağın Kayıp Eşya = %10 kova/Dağ Kileri = arşiv kararıyla gerilimli; kayda girmesi gerekir.
- 14 / Anayasa 1, KALITE 5: tutanak "Ortak bulgular" satır 49 "Bandar Apna Dost kitlesi çocuk/genç ağırlıklı" kesin yazıyor. Kaynak ilk-tarama.md Kart 8 satır 202'de "Paylaşılma/yorumlanma hipotezi" alanında (hipotez). Kendi WebSearch'üm kitle dökümü bulamadı. "Hipotez" olarak yazılmalı. (Sonuç yönü, yani Üçüncü Kat'ın kanıt aktarımı zayıf, yine geçerli.)
- 13/15 (yöntem şeffaflığı, MAHKEME.md puanlama tablosu): skor betiği tablo satırlarını kaçırmıyor (4 dosyada sayısal puanlı her satırı taradım; kaçan yok, bölüm başlığı sızması yok), Üçüncü Kat tüketici ve Uzman satırlarını elle toplayıp doğruladım. Ama (a) **Yorum kriteri kapsamı eşit değil:** Üçüncü Kat ve Dağ Kileri için yalnızca Muhalefet (n=2) puan vermiş, Kayıp Eşya için ayrıca Tüketici Comment Warrior 7 var; Kayıp'ın yorum ortalaması 6,25, yalnız-Muhalefet olsaydı 5,5 (~0,75 skor puanı lehine). (b) **Etiket sezgisi tutarsız:** "Platform yerliliği / dikkat arbitrajı" (Creator, Dağ ve Kayıp) "dikkat" sayılıyor, ama Üçüncü Kat'taki aynı profil "Platform yerliliği / özgünlük" "özgünlük" sayılıyor; "İlk 2 sn / paylaşılma" (Khaby 8) yalnız paylaşılmaya, "İlk 2 sn / tekrar izleme" (Zach King) hiçbir yere gitmiyor; Duolingo/Hormozi-çaba satırları sessizce düşüyor. Duyarlılık: toplam etki ≤1 puan, sıralama (60,9 > 57,6 > 50,4) değişmiyor; ama Dağ Kileri 50,4'ten ~50,1'e iner, yani 50 bandının hemen üstünde. Tutanak yöntem sınırını yazmıyor; "kriter başına kapsayan konsey sayısı" ve bu sınır tutanağa girmeli.
ÖRNEKLEM DOĞRULAMASI (3 sınama + tutanak aktarımı):
- Gossip Goblin AI filmi "Gods Don't Give Gifts" 30 Ekim sinema gösterimi planı (Variety, IndieWire): TUTTU. Not: gündem 27 Kasım'da yazılmış, tarih geçmiş; "plan" ifadesi eskimiş, sonuç doğrulanmadı.
- Neural Viz / WIRED (2025-10-07): senaryo ve storyboard'u geleneksel yöntemle yazan tek kişi, Runway Act-One: TUTTU (WIRED sayfası açılamadı, ikincil kaynaklar).
- Bandar Apna Dost 2,07 milyar izlenme (Kapwing); kitlenin çocuk/genç olması: izlenme TUTTU, kitle iddiası DOĞRULANAMADI.
- Tutanak ↔ konsey dosyaları (rastgele): Üçüncü Kat "iki konsey deney adayı" (Creator koşullu, Tüketici): tuttu. Finans kredi aralıkları 90/252/400, 84/240/400, 56/159/255: finans dosyasıyla tuttu. Kalibrasyon: 12 tahminin 12'si dosyalar ve `konseyler/kalibrasyon.csv` ile tuttu. "Dağ Kileri talep kanıtı tek tarihsiz haber" ve "Bölüm 2 sonucu varsayıyordu" (Muhalefet): tuttu. Uzman IP cümlesi ve Creator 5,3: tutmadı (yukarıda).
KONTROL ÖZETİ (sorunsuz):
- "Simülasyon" uyarısı: tutanak satır 3 ve gündemlerde var; puanlar "hipotez" olarak etiketli (Anayasa 7).
- Kreatif içerik: gerçek marka/kişi yok (Tomruk yeleğinde logo yok); Gossip Goblin/Neural Viz/Khaby/Li Ziqi yalnızca yöntem veya risk referansı, prompt'ta "X tarzı" yok; Meow Ziqi/Li Ziqi yakınlık riski gündemde ve tutanakta kayıtlı; çakışma taraması "yapılmadı" diye dürüst yazılmış (G-0019). Çocuk hedefleme: üç gündem de "çocuklara özel değil" ve yetişkin ton, şartlar tutanakta; Üçüncü Kat için çocuksu algı şartı var. Platform: oylama CTA'sı (engagement bait riski) tutanakta kaldırıldı; YPP 2027 rakamları gündemlerde "doğrulanmadı" etiketli ve karar rakamlara dayanmıyor.
- DURUM.json: G-0019/G-0020 (A0, queued, bağımlılık G-0008) tutanaktaki şartlarla tutarlı; G-0012 `proposed`, onay null, "önerilen max 80 kredi"; K-B4 Bora'ya soruyor. **A2 önerisi onaylı gibi sunulmamış.** 80 = ~68 + %15 pay (tutarlı). G-0008 bekci_karari null (doğru).
- `bekleyen_kararlar` K-B1..K-B5 tutanakla çelişmiyor.
NOTLAR (RED sebebi değil):
- Tutanak "Engel yok" cümlesi Finans+Bekçi ÖN kontrolüne dayanıyor; ön kontrol kendi başlığında bağımsız Bekçi denetiminin yerine geçmediğini söylüyor. Tutanağa "bağımsız Bekçi denetimi bekliyor/yapıldı (bu kayıt)" satırı eklenmeli.
- Üçüncü Kat Bölüm 1 "TESLİM ALINDI" damgası Türkçe metin; "sözsüz/dil bağımsız" iddiasıyla çelişiyor (Tüketici Global Viewer işaretlemiş) ve tutanak şartları arasında değil. Koli üstünde üç kat kayma sahnesi (finans: taklit edilebilir davranış) revizyonda yeniden okunmalı.
- Dağ Kileri bandı "geliştirilmeli" (50,4) ama karar "düşük öncelik/arşiv": MAHKEME.md çoğunluk/puan otomatik değildir diyor, gerekçe yazılmış; yine de band ile karar farkı tek cümleyle belirtilmeli.
- Kayıp Eşya skoru uzman maliyet puanlarında (taban ~44) düzeltilmemiş kapsamı (4 klip/bölüm, 56/159/255) kullanıyor; finans puanı 7 düzeltmeye dayanıyor. Fark küçük.
- Dış denetim paketi (`denetim/dis-denetim/2026-11-27-kurulus-paketi.md`, yeni) kurucunun ikamet ve uyruğunu içeriyor; Bora paketi ChatGPT'ye yapıştırmadan önce bu satırı çıkarmayı düşünebilir (Anayasa 15 özel kişisel veri).
DÜZELTME İÇİN: Tutanakta azınlık bölümünü konsey dosyalarındaki cümlelere göre yeniden yaz (Uzman IP cümlesini ve Creator 5,3'ü düzelt, Muhalefet azınlığını ekle), "Bandar kitlesi" ifadesini hipotez yap, skor tablosunun altına kriter başına kapsayan konsey sayısı ve betik/etiket sınırı notunu ekle.
```
