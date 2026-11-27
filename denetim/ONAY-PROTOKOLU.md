# ONAY PROTOKOLÜ — Bora'dan onay nasıl istenir, nasıl kaydedilir

1. Onay isteği `vardiyalar/DURUM.json > bekleyen_kararlar` içine yazılır: `{id, soru, secenekler, oneri, gerekce, maliyet, geri_alinabilir_mi, ilgili_gorev}`.
2. Patron özeti (`raporlar/patron-ozeti/`) yalnızca gerçekten gereken kararları, önerisiyle sorar. Daha önce cevaplanmış soru (`KARARLAR.md`) tekrar sorulmaz.
3. Bora'nın cevabı geldiğinde: `KARARLAR.md`'ye tarihli satır, ilgili görevin `onay` alanı ("Bora, 2026-11-28, <kapsam>[, max N kredi]"), görev `approved`.
4. Sohbette verilen onay dosyaya yazılmadan geçerli değildir (bir sonraki oturum bilemez).
5. Onay kapsamı dar yorumlanır: "EXP-0001 için 120 kredi" başka deneye veya ikinci tura geçmez.
6. Kalıcı yetki yalnızca `sirket/YETKI-MATRISI.md` tablosuna Bora'nın kendi eklediği satırla doğar.
