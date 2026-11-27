# Engeller (otonom sistemin dışında bir eylem gerektirenler)

| Tarih | Engel | Kimden | Alternatif | Kanıt |
|---|---|---|---|---|
| ~~2026-11-27~~ ÇÖZÜLDÜ 2026-11-27 (K-011) | `AI-Media-Company` uzak reposu yok; bu ortamdaki `gh` tokeni geçersiz, yeni repo oluşturamıyorum | Bora: github.com'da private repo aç (ad: AI-Media-Company), bu oturuma/ortama ekle | Yerel git + sohbete eklenen arşiv dosyası (geçici; konteyner silinirse kaybolur) | `gh auth status`: token invalid; list_repos: yalnızca Aloni, twoislandsdallas |
| 2026-11-27 | youtube.com, tiktok.com, trends.google.com proxy 403; support.google.com, support.tiktok.com, tubefilter.com WebFetch ENOTFOUND | Bora: ortamın ağ ayarlarında bu hostlara izin | WebSearch özetleri (düşük/orta güven); Bora'nın tarayıcısından başlık/açıklama/transkript kopyası | curl 403, alt ajan raporları |
| 2026-11-27 | Referans videoların içeriği doğrulanamadı | Bora: üç videonun başlığı + açıklaması (veya transkripti) | Ağ izni açılınca yeniden çalıştır (G-0009) | istihbarat/kaynaklar/REFERANS-VIDEOLAR.md |
| 2026-11-27 | Zamanlayıcı repo kaynağı olmadan çalışmaz (ALONI dersi: 403) | Uzak repo → tetikleyiciye kaynak olarak ekle | Bora oturum açtığında `/vardiya` elle | ALONI docs/autopilot/BLOCKERS.md 2026-11-24 |
| 2026-11-27 | Rakip hesapların gerçek takipçi/izlenme verisi platformdan okunamıyor | Ağ izni veya resmi araç (TikTok Creative Center vb.) | Basın/rapor kaynaklı rakamlar, düşük güven etiketiyle | — |
