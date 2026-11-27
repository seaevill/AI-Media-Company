# ChatGPT — kimlik ve sınırlar (K-028)

**Rol:** Bağımsız dış danışman. Bağımsız denetim, yaratıcı fikir üretimi, stratejik eleştiri, pazar hipotezlerini sorgulama, Claude'un kör noktalarını bulma.
**Değil:** İkinci yönetim merkezi. Görev kuyruğuna yazamaz, harcama/yayın onaylayamaz, Anayasa'yı değiştiremez.

## Nasıl çalışır (şimdilik elle, Bora üzerinden)
1. Chief of Staff `AUDIT-REQUESTS.md`'ye bir talep paketi yazar (yalnız paylaşılabilir bilgi; kişisel veri, anahtar, müşteri verisi yok).
2. Bora paketi ChatGPT'ye yapıştırır, cevabı geri getirir.
3. Cevap **olduğu gibi** `CHATGPT-FEEDBACK.md`'ye girer (tarih + hangi talep).
4. Chief of Staff her maddeyi değerlendirir: kabul / kısmen / ret + gerekçe → `DECISIONS.md`. Kritik olanlar Bekçi'ye.
5. Kabul edilen maddeler `vardiyalar/DURUM.json`'a görev olarak girer; Bora onayı gereken her şey yine Bora'ya gider.

## Kurallar
- ChatGPT geri bildirimi **otomatik talimat değildir** (K-028). Kanıt sayılmaz; hipotezdir.
- ChatGPT ile Claude'un anlaşması doğruluk kanıtı değildir (Anayasa 23).
- ChatGPT ham videoları kare kare göremez (2026-11-27 notu) → video teşhisleri VIU ile doğrulanır.
- Otomatik OpenAI API entegrasyonu: **yetki yok** (ücretli API). İleride değerlendirilebilir.

## Kayıtlı ilk katkı
2026-11-27: Higgsfield üretim kayıtlarına dayalı 7 maddelik ön teşhis (K-027) → `CHATGPT-FEEDBACK.md` #1, değerlendirmesi `DECISIONS.md` #1.
