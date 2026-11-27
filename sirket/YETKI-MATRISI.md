# YETKİ MATRİSİ

Salt okunur. Yalnızca Bora değiştirir. Kaynak: manifesto §09 madde 10/19, §30, §36, §37 "Kuruluş emri".
Durum (2026-11-27): **Ücretli üretim, gerçek yayın, dış iletişim veya yeni harcama için genel yetki YOKTUR.**

## Onay seviyeleri

| Seviye | Ne kapsar | Kim onaylar | Görevde nasıl yazılır |
|---|---|---|---|
| **A0 — Önceden yetkili** | Ücretsiz web araştırması, iç dokümantasyon, fikir/senaryo/storyboard/prompt yazımı, konsey ve mahkeme toplantıları, kuru koşular, analiz, şablon, repo içi düzenleme (Anayasa/sirket/kurallar hariç) | Kuruluş emriyle Bora (2026-11-27) | `"onay": "A0"` |
| **A1 — Kaynak sınırlı** | Claude kullanımı: vardiya başına en fazla `CONFIG.json > limitler.alt_ajan_kosu_basina` alt ajan; günlük koşu sınırı | CONFIG.json'daki sınırlar | otomatik, sınır aşılırsa dur |
| **A2 — Ücretli üretim** | Higgsfield/Kling/diğer kredi harcayan her üretim; ücretli araç denemesi | **Bora, deney bazında, azami kredi tutarıyla** | `"onay": "Bora, <tarih>, max <N> kredi"` |
| **A3 — Dış dünya** | Gerçek yayın, sosyal medya hesabı açma, platforma bağlanma, müşteri/marka/insan ile iletişim, fiyat teklifi, sözleşme, ödeme, ürün yayına alma (Gumroad vb.), uzak repo oluşturma, zamanlayıcı etkinleştirme | **Yalnızca Bora, iş bazında** | `"onay": "Bora, <tarih>, <kapsam>"` |
| **A4 — Değiştirilemez** | ANAYASA.md, sirket/, takimlar/*/kurallar.md, bütçe sınırları, güvenlik kuralları | Yalnızca Bora, elle | Ajanlar dokunmaz |

## Kurallar

1. Onay alanı boş görev alınmaz. A0 olarak işaretlenemeyecek bir işi ajan A0 diye işaretleyemez.
2. A2 onayı **azami kredi** içerir. Tahmin onaylı sınırı aşarsa üretim başlamaz; aşım üretim sırasında anlaşılırsa durur ve `finans/kredi-kayitlari.csv`'ye yazılır.
3. Başarısız üretimler de krediye sayılır.
4. Bir bağlantının (MCP) var olması yetki değildir. Higgsfield, Kling, Gumroad, Canva, Gmail, Notion, Supabase, Cloudflare, TikTok bağlantıları A2/A3 kapsamındadır; yalnızca **okuma** amaçlı bakiye/model/fiyat sorguları A0'dır.
5. **Kalıcı yetki** (ör. otomatik yayın) ancak aşağıdaki tabloda bir satır olarak yazılıysa geçerlidir: hesap, platform, içerik kategorisi, Bekçi şartı, sıklık, bütçe, süre, durdurma yolu.

## Kalıcı yetkiler

| # | Kapsam | Platform/hesap | Bütçe | Başlangıç–bitiş | Bekçi şartı | Durdurma | Veren |
|---|---|---|---|---|---|---|---|
| 1 | A2 üretim: Higgsfield (ve Kling) **plan içi kredileri**; görsel, video, ses üretimi ve testler | Higgsfield/Kling hesabı (yayın yok) | Sınırsız plan kredisi. Ek kredi/paket satın alma, otomatik yükleme, yeni abonelik **dahil değil** (nakit = A3). Bakiye 300 kredinin altına düşünce Bora'ya bildirim (durdurmaz). Plan dışı tek iş > 100 kredi ise önce Bora'ya bilgi | 2026-11-27 – Bora iptal edene kadar | Her üretim `finans/kredi-kayitlari.csv`'ye (başarısızlar dahil); her deney/üretim partisi Bekçi denetiminden geçer; gerçek yayın yine A3 | Bora: "kredi yetkisi iptal" ya da bu satırı silmesi | Bora, sohbet, 2026-11-27 (K-019) |

## Asla (hiçbir onayla değil)

Sahte hesap/bot/satın alınmış etkileşim · sahte yorum veya müşteri · gerçek kişinin yüzü/sesi izinsiz · platform kısıtını, CAPTCHA'yı veya girişi aşma · ALONI veya Two Islands Dallas'a yazma · bu projelerin özel verilerini taşıma · sır/kimlik bilgisini dosyaya yazma.
