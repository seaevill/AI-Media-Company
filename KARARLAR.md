# KARARLAR

Her satır: tarih · karar · kaynak · onaylayan. Geçmiş silinmez; değişen karar `hafiza/DEGISTIRILEN-KARARLAR.md`'ye taşınır ve buraya yeni satır yazılır. **Bora'nın burada cevapladığı soru tekrar sorulmaz.**

## Bora'nın kuruluşta verdiği kararlar (manifesto v1.0, 2026-11-27)
| # | Karar | Kaynak |
|---|---|---|
| K-001 | Şirketin hafızası bağımsız, **private** bir GitHub reposu (`AI-Media-Company`, geçici ad); Markdown + JSON + CSV. GitHub Wiki ve Notion ana hafıza değil | §06, §08 |
| K-002 | Öncelik sırası: 1 AI Media/Influencer → 2 kitleyi gelire dönüştürme → 3 AI Commercial Studio → 4 Micro-SaaS | §04 |
| K-003 | Bora'nın kişisel ilgi alanları içerik kategorisi seçiminde ölçüt değildir | §02 |
| K-004 | Ücretli üretim, gerçek yayın, dış iletişim ve yeni harcama için genel yetki yok | Kuruluş emri |
| K-005 | ALONI ve Two Islands Dallas'a dokunulmaz; özel verileri taşınmaz | §07 |
| K-006 | Tek zamanlanmış yönetici; başlangıç önerisi 3 saatte bir; ALONI kilit mantığı uyarlanır | §28 |
| K-007 | Gerçek yayın yetkisi başlangıçta Bora'dadır | §36 |
| K-008 | ChatGPT bağımsız dış denetçidir; bağlantı Bora üzerinden | §32 |
| K-009 | Supabase, Cloudflare, Notion şimdilik zorunlu değil | §06 |
| K-010 | Raporlar Türkçe, kısa, jargonsuz | §33 |

## Chief of Staff'ın kuruluşta aldığı mimari kararlar (Bora'nın itiraz hakkı açık)
| # | Karar | Gerekçe | Tarih |
|---|---|---|---|
| M-001 | Sıklık/sınır/bütçe tek kaynağı `vardiyalar/CONFIG.json`; `dogrula.py` başka dosyada sıklık sayısını yakalar | ALONI'de 3 saat / yoğun mod çelişkisi | 2026-11-27 |
| M-002 | Tek kuyruk `vardiyalar/DURUM.json` (takım başına ayrı kuyruk yok); takımlar yalnızca kendi `defter.md`'sine yazar | Anayasa 17; ALONI'nin tek-liste geçişi | 2026-11-27 |
| M-003 | Onay seviyeleri A0–A4 (`sirket/YETKI-MATRISI.md`); araştırma/dokümantasyon A0 önceden yetkili | Kuruluş emri + §30 | 2026-11-27 |
| M-004 | 7 çekirdek rol (Chief of Staff + 6 ajan); diğer 30+ rol çağrılabilir profil | Maliyet (§10) | 2026-11-27 |
| M-005 | Konseyler her mahkemede ayrı alt ajan bağlamında; profiller konsey içinde bölüm | Bağımsızlık ↔ maliyet dengesi | 2026-11-27 |
| M-006 | Kilit: ileri-yönlü `lock/medya` dalı, `--force-with-lease`; bayatlama süresi CONFIG'de | ALONI'de kanıtlanmış mekanizma | 2026-11-27 |
| M-007 | Manifestodaki klasör ağacının yalnızca aktif bölümleri açıldı; kalanlar ROADMAP'te | "Yüzlerce boş dosya yaratma" (§08) | 2026-11-27 |
| M-008 | Bekçi kararları `denetim/audit-logs/`'a SHA ile yazılır (uzak repo olunca PR yorumu da) | Madde 18, §31 | 2026-11-27 |
| M-009 | Medya dosyaları repoya girmez (`.gitignore` + `dogrula.py`) | §08 | 2026-11-27 |

## Bora'nın 2026-11-27 (kuruluş raporu sonrası) kararları
| # | Karar | Kaynak |
|---|---|---|
| K-011 | Uzak repo: https://github.com/seaevill/AI-Media-Company (private, Bora açtı) | Bora, sohbet, 2026-11-27 (K-B2) |
| K-012 | Kuruluş belgeleri **onaylandı**: ANAYASA (madde 1 ve 10'daki eklemeler dahil), sirket/, takımların kurallar.md dosyaları, BEKCI-KURALLARI, ONAY-PROTOKOLU ve dogrula.py koruma listesinin genişletilmesi | Bora, "2-Onaylıyorum", 2026-11-27 (K-B1) |
| K-013 | Ağ izinleri onaylandı: youtube.com, tiktok.com, trends.google.com, support.google.com, support.tiktok.com, help.instagram.com | Bora, "3-Onaylıyorum", 2026-11-27 (K-B3) |
| K-014 | G-0012 karakter tutarlılığı benchmark'ı: **en fazla 80 Higgsfield kredisi** (A2) | Bora, "4-Onaylıyorum", 2026-11-27 (K-B4) |
| K-015 | Higgsfield Ultra: aylık ~4.800 TL, 3.000 kredi (Bora beyanı, "galiba" — kesin değil) → yaklaşık 1,6 TL/kredi. Bora'nın gördüğü bakiye 1.938; araç 1.935,39 okudu | Bora, 2026-11-27 (K-B5) |
| K-016 | G-0012 test videolarına Bora'nın tepkisi: **"hiç komik değil ama animasyon fikri güzel, ses yerinde."** İlk gerçek insan geri bildirimi (tek kişi, kurucu; izleyici verisi değil) | Bora, sohbet, 2026-11-27 |
| K-017 | Harcanan kredi ve güncel bakiye CONFIG.json'dan çıkarılır; tek kaynak `finans/kredi-kayitlari.csv`. CONFIG yalnızca sınır/onay tutar | Bora, "3-evet", 2026-11-27 (K-B9) |
| K-018 | Dizi/hesap adı kararı ekibe devredildi ("uluslararası olunca gözlem ve veri sizin elinizde"). Ekip veriyle seçer, Bora'ya bilgi verir; hesap açma yine A3 | Bora, "4-…ekibe bırakıyorum", 2026-11-27 |
| K-019 | **Kalıcı kredi yetkisi:** "Kredi sıkıntım yok, sınırsız kullan." Higgsfield (ve bağlıysa Kling) plan kredileriyle üretim artık deney bazında ayrı onay gerektirmez. Kapsam ve güvenlik çizgileri `sirket/YETKI-MATRISI.md` kalıcı yetki #1. Ek kredi/paket satın alma ve yeni ücretli abonelik (nakit) bu yetkiye dahil değil | Bora, sohbet, 2026-11-27 |
| K-020 | Bora'nın yönlendirmesi: Üçüncü Kat dünyası **hesaptan çok film/hikâye için** güçlü olabilir ("güzel bir hikâyeyle tutabilir"); **3D her zaman daha iyi**. Stratejik sıra (K-002) değişmedi; hikâye odaklı format test edilecek (G-0025) | Bora, sohbet, 2026-11-27 |
| K-021 | **Çalışma adı: "Unit 3C"** (ekip kararı, K-018 yetkisiyle). Gerekçe: dizinin bağlayıcı gizemi (var olmayan 3/C dairesi), dilden bağımsız, film/hikâye yönüne uygun, @unit3c TikTok ve YouTube'da boş görünüyor; çakışma bulunamadı (arama özeti). Yedek: "Landing 3" (@landingthree). Elenenler: Floor Three (handle'lar dolu, Third Floor tescilleri), The Third Floor, Yunanca ad. Marka tescili araştırması gerçek hukukçu işi | Chief of Staff, 2026-11-27, `istihbarat/pazar-firsatlari/2026-11-27-isim-secimi.md` |
| K-022 | **K-019 DÜZELTMESİ:** "Kredi Higgsfield için değil Claude için; Higgsfield'da temkinli git, amaç ilk başta içerik üretmek." → K-019'daki kalıcı Higgsfield kredi yetkisi geri alındı (hiç kullanılmadı, 0 kredi harcandı). Higgsfield üretimi yine deney/parti bazında Bora onayı + azami kredi (A2). **Claude kullanımı sınırsız** (A1). Öncelik: içerik üretimi | Bora, sohbet, 2026-11-27 |
| K-023 | G-0026 ilk içerik üretimi onaylandı: 'Tıkırtı' + 'Kapı' + Tomruk/Cetvel referans yeniden çizimi, **max 35 Higgsfield kredisi** (A2) | Bora, "onaylıyorum", 2026-11-27 (K-B11) |
| K-024 | Bora geri bildirimi: "Kapı" videosunda vombat kazın içinden geçiyor (görüntü hatası). Klip kullanılamaz kabul edildi; kalite kontrol yöntemi sıklaştırıldı | Bora, sohbet, 2026-11-27 |
| K-025 | "Kapı" yeniden üretimi onaylandı ("Üret fakat lütfen aynı hataları istemiyorum"); K-023 bütçesi içinde, iki çekim + kurgu | Bora, sohbet, 2026-11-27 (K-B13) |
| K-026 | Bora'nın "Kapı" v2 değerlendirmesi: **"Rezalet."** G-0026 başarısız kabul edildi. Bora yeni bir üretim planını onaylayana kadar Higgsfield üretimi durduruldu | Bora, sohbet, 2026-11-27 |
| K-027 | **ACİL PRODÜKSİYON VE KREATİF DENETİM (Bora):** yeni ücretli video üretimi ve yayın geçici olarak durduruldu; 4 konsey 10 soruyla toplanacak; mevcut karakter/konsept/stil savunulmak zorunda değil, gerekirse tamamı iptal; Animation Director, Continuity Supervisor, Physics QA, Comedy Editor uzmanlıkları eklenecek; Video Intelligence Unit (gerçek kare kare video denetimi) kurulmadan hiçbir animasyon yayın kalitesinde kabul edilmez; başarısız üretimler silinmez, nedenleri/modeli/maliyeti/dersleri kaydedilir; önce araştırma ve gerçek pazar örnekleri, sonra alternatif kreatif yönler Bora'ya sunulur. Dış girdi: ChatGPT'nin üretim kayıtlarına dayalı ön teşhisi (7 risk; kare kare doğrulanmamış) | Bora, 2026-11-27 |
| K-028 | **MULTI-AI INTELLIGENCE EXPANSION (Bora):** Claude Code Chief of Staff olarak kalır; **Google Gemini** video/ses analizi istihbarat servisi; **ChatGPT** bağımsız stratejik danışman, kreatif ortak ve dış denetçi (ikinci yönetim merkezi değil; geri bildirimi otomatik talimat değildir, Chief of Staff değerlendirir, gerekirse Bekçi'ye sunar). Görevler: 4 açık kaynak video-MCP projesi + resmî Gemini API karşılaştırması (incelenmemiş kod çalıştırılmaz); video analiz metodolojisi; `external-advisory/` klasörü; VIU'nun vardiyaya bağlanması (her video bir kez analiz, önbellek, yerel/bulut erişimi ayrı doğrulanır, anahtar dosyaya yazılmaz); 3 referans video için benchmark planı + ikinci benchmark planı. **Ücretli API aboneliği, kredi harcama, yayın yok**; önce araştırma ve en ekonomik/güvenli/sürdürülebilir entegrasyon önerisi | Bora, 2026-11-27 |
| K-029 | **PROFESSIONAL KNOWLEDGE ACQUISITION & AGENT QUALIFICATION (Bora):** rol tanımı ≠ beceri; kaynaklı mesleki bilgi + `.claude/skills/` + L0–L4 yeterlilik; eğitim öncesi (A) / sonrası (B) kör karşılaştırma; ilk 3 pilot: Market Intelligence, Viral Content Analysis, Animation QC; gerçek videoya erişemeyen ajan video analizi için yeterli sayılmaz; ücretli üretim/API yok; 'NO KNOWLEDGE WITHOUT SOURCES / NO SKILL WITHOUT EXECUTION / NO QUALIFICATION WITHOUT EVIDENCE'. Görev dağılımı notu: **video üretim sorumluluğu ChatGPT'ye devrediliyor**; Claude kreatif araştırma, brief, bağımsız eleştiri ve doğrulamada kalır | Bora, 2026-11-27 |
