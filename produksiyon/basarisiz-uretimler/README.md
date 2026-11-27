# Başarısız üretim arşivi (K-027: silinmez)

Her başarısız ya da kurucu tarafından reddedilen üretim burada kalır. Medya dosyaları repoda değil: Higgsfield hesabında (iş kimliğiyle) ve oturum scratch klasöründe. Toplam harcama ve satırlar: `finans/kredi-kayitlari.csv`.

| # | Ad | Görev | Model | Süre / çözünürlük | Kredi | Girdi | Amaç | Sonuç | Bora | Bilinen hatalar | Neden (hipotez) |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| 1 | mini | G-0012 | Seedance 2.0 Mini | 8 sn / 720×1280 | 8 | 3 karakter referansı | 3 karakterli merdiven sahnesi (benchmark) | Kimlikler sabit; kamera talimatı uygulanmadı; flamingo küçük; vombat ayı/kediye kaydı | "hiç komik değil, animasyon güzel, ses yerinde" (ortak değerlendirme) | Bekçi/CoS eşik altı | 3 karakter + ince nesne (metre) + kamera talimatı tek 8 sn'de; şaka değil teknik test |
| 2 | flash | G-0012 | Seedance 2.5 Flash | 8 sn / 720×1280 | 40 | aynı | aynı | Mini'den üstün değil, 5× pahalı | aynı | VIU-1: 6,0–7,0 sn ani değişimler | aynı |
| 3 | hailuo | G-0012 | Minimax Hailuo 2.3-fast | 6 sn / 768×1376, **sessiz** | 4 (+1,5 başlangıç karesi) | başlangıç karesi | aynı | Kullanılamaz | aynı | koli çoğalması, flamingo deformasyonu/uçma, ses yok; VIU-1: 4,6–5,5 sn | Ucuz model + karmaşık fizik |
| 4 | tikirti | G-0026 | Seedance 2.0 Mini | 8 sn / 720×1280 | 8 (+1,5 kare) | başlangıç karesi + referans | Y3 tekrar–kırılma şakası | Sıra doğru, kilit an okunmuyor | "Rezalet" (genel) | karanlık (parlaklık 40/255), ayak küçük, saatte rakam | Şaka sese ve küçük bir ayrıntıya dayanıyor; ışık seçimi |
| 5 | kapi_v1 | G-0026 | Seedance 2.0 Mini | 8 sn / 720×1280 | 8 (+1,5 kare) | başlangıç karesi + 2 referans | Y4 tepki şakası | **İç içe geçme** (vombat kazın içinden geçer, 3–5 sn) | Bora buldu | CoS, Bekçi ve video_qc kaçırdı | İki karakterin yolları kesişiyor; kapı etkileşimi |
| 6 | kapiA | G-0026 | Seedance 2.0 Mini | 4 sn | 4 | başlangıç karesi + referans | Kapı v2 çekim A | Kaz duvara değil kapıya çekildi → kırpıldı | "Rezalet" (v2) | süreklilik | Model sahne yönünü (sola/duvara) izlemedi |
| 7 | kapiB | G-0026 | Seedance 2.0 Mini | 5 sn | 5 (+1,5 kare) | başlangıç karesi + 2 referans | Kapı v2 çekim B | Karakterler arası iç içe geçme yok; **menteşe yönü tutarsız** | "Rezalet" (v2) | kapı ortadan menteşeli gibi döner | Menteşeli nesne fiziği model kapasitesinin üstünde |
Yan üretimler (görseller): 3 karakter referansı (G-0012), Tomruk yeniden çizimi ×2, başlangıç kareleri ×4 — hepsi kredi CSV'sinde.

**Toplam görsel+video harcaması: 90,5 kredi** (G-0012: 58; G-0026: 32,5). ≈ 145 TL (Bora beyanı ~1,6 TL/kredi).

## Kök neden özeti (Chief of Staff, hipotez; VIU-2 ve konsey toplantısı ile doğrulanacak)
1. Kısa süreye çok olay ve çok karakter (ChatGPT teşhisi 1, 3 ile uyumlu).
2. Fiziksel etkileşimler (kapı, koli, metre, battaniye) — modelin en zayıf alanı (teşhis 2).
3. Komedi zamanlaması tek prompt içinde modele bırakıldı; montaj neredeyse kullanılmadı (teşhis 5).
4. Uzun, saniye saniye kısıtlayıcı promptlar (teşhis 4) — model bunları seçici uyguladı.
5. Görsel stil (mat 3D, soluk renk) pazar kanıtı olmadan, mahkemede "yetişkin kodlu" görünsün diye seçildi (teşhis 6) — doğrulandı: araştırma dosyalarında bu estetiğe ait başarı kanıtı yok.
6. Aynı konsepte art arda üretim (teşhis 7): Kapı üç kez üretildi.
7. Kalite çıtası kurucuya önceden onaylatılmadı; "çalıştı" kararı zayıf denetimle verildi (bizim ek teşhisimiz).
