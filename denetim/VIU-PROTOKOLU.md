# Video Intelligence Unit (VIU) — gerçek video denetim protokolü

Kaynak: K-027 (Bora, 2026-11-27). **VIU onayı olmadan hiçbir animasyon "yayın kalitesinde" sayılmaz.** Bekçi'nin genel denetiminden ayrıdır; video çıktısı için zorunlu ek kapıdır.

## Neden üç katman
2026-11-27 kalibrasyonu: "Kapı" v1'deki iç içe geçmeyi (a) Chief of Staff 2 kare/sn döşemede, (b) Bekçi aynı döşemede, (c) `video_qc.py` sayısal sıçrama ölçümüyle **kaçırdı**; Bora izleyerek yakaladı. Hata kademeli olduğu için sayısal ölçüm yakalayamaz; küçük döşeme göz yanıltır. Bu yüzden:

| Katman | Ne | Kim | Geçme şartı |
|---|---|---|---|
| **VIU-1 Otomatik** | `python3 -I scripts/video_qc.py <video> --cikti <scratch>/viu --fps 8` — çözünürlük, 9:16, süre, ses kanalı/düzeyi, sessiz/donma bölümleri, ani değişim (kesme/ışınlanma) anları, karanlık sahne; tam video 8 kare/sn kontak tabloları + şüpheli anlar 12 kare/sn büyük boy | betik | Teknik uyarı yok ya da gerekçeli |
| **VIU-2 Görsel** | **İki bağımsız** denetçi (`.claude/agents/viu-denetci.md`), birbirini ve üretenin notlarını görmeden, tüm kontak tablolarını ve şüpheli an tablolarını açar; aşağıdaki 4 uzman merceğiyle kare kare kontrol | 2 ayrı ajan bağlamı | İkisi de "yayın engeli yok"; ayrışırsa engel varsayılır |
| **VIU-3 İnsan** | Bora (ileride: gerçek izleyici paneli) videoyu sesli ve tam hızda izler | Bora | Bora "olur" der |

Üreten (produksiyon/Chief of Staff) kendi videosu için VIU-2 denetçisi olamaz.

## Dört uzman merceği (VIU-2 kontrol listesi)
**Physics QA** — iç içe geçme (karakter–karakter, karakter–nesne, nesne–duvar) · kaybolma–yeniden belirme · nesne çoğalması/yok olması · menteşe/dönme ekseni tutarlılığı · yerçekimi/ağırlık (havada asılı kalma) · uzuv sayısı, kopması, eriyen eller/kanatlar · zemin teması (ayak kayması).
**Continuity Supervisor** — karakter çapaları kare boyunca sabit mi (renk, kıyafet, aksesuar sayısı, oran) · prop sürekliliği (çanta sayısı, anahtar, kapı kolu tarafı) · ışık/saat/arka plan sabit mi · iki çekim arası kesmede konum ve poz uyumu · istenmeyen yazı/rakam/logo.
**Animation Director** — okunurluk (ana eylem kadrajda büyük ve net mi, karanlıkta kalıyor mu) · sahneleme (izleyicinin gözü doğru yere gidiyor mu) · hareket kalitesi (robotik, kayan, titreyen) · karakter sayısı ve olay yoğunluğu süreye uygun mu · ifade/mimik okunuyor mu.
**Comedy Editor** — ilk 2 sn'de kurulum anlaşılıyor mu · tek sürpriz anı var mı, hangi karede · tepki/duraklama (beat) var mı, süresi · zamanlama modele mi bırakılmış, montajla düzeltilebilir mi (kırpma, dondurma, ses vurgusu) · ses olmadan da okunuyor mu.

## Karar biçimi (her denetçi, her video)
```
VİDEO: <ad>   KARAR: YAYIN ENGELİ YOK | YAYIN ENGELİ VAR | BELİRSİZ
PHYSICS QA:      [zaman] bulgu (kare no)…
CONTINUITY:      …
ANIMATION DIR.:  …
COMEDY EDITOR:   …
MONTAJLA ÇÖZÜLEBİLİR: …
MODEL KAPASİTESİ ÜSTÜNDE: …
```
Her bulgu zaman damgası ve kontak tablosu adıyla yazılır. "Görmedim" ≠ "yok": bakılamayan an "kontrol edilemedi" yazılır.

## Kalibrasyon
VIU-2 denetçilerinin bulguları Bora'nın (VIU-3) bulgularıyla `denetim/viu/kalibrasyon.csv`'de karşılaştırılır; kaçırılan hata türleri kontrol listesine eklenir.
