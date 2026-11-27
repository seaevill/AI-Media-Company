#!/usr/bin/env bash
# Tek koşucu kilidi. ALONI'deki lock/aloni mantığından uyarlandı (ileri-yönlü dal, force-with-lease).
# Kullanım:
#   scripts/kilit.sh al    <RUN>   -> 0: alındı, 10: başka koşu sürüyor, 11: yarışı kaybetti
#   scripts/kilit.sh birak <RUN>   -> 0: bırakıldı, 12: kilit bu koşunun değil
#   scripts/kilit.sh durum         -> kilidin son mesajını yazar
#   13: kilit dalı okunamadı. 0 dışındaki HER kod = DUR.
# Ortam: KILIT_REMOTE (varsayılan origin), KILIT_DAL (varsayılan lock/medya),
#        KILIT_BAYAT_DK (varsayılan CONFIG.json > limitler.kilit_bayatlama_dakika)
set -euo pipefail
REMOTE="${KILIT_REMOTE:-origin}"
DAL="${KILIT_DAL:-lock/medya}"
KOK="$(cd "$(dirname "$0")/.." && pwd)"
BAYAT="${KILIT_BAYAT_DK:-$(python3 -I -c "import json;print(json.load(open('$KOK/vardiyalar/CONFIG.json'))['limitler']['kilit_bayatlama_dakika'])")}"
REF="refs/remotes/$REMOTE/$DAL"
simdi_iso() { date -u +%FT%TZ; }

getir() {
  git fetch -q "$REMOTE" "+refs/heads/$DAL:$REF" 2>/dev/null || return 1
}

ilk_kurulum() {
  # Dal yoksa boş ağaçlı ilk FREE commit'i oluştur.
  local T; T=$(git hash-object -t tree /dev/null -w)
  local C; C=$(git commit-tree "$T" -m "FREE run=init at=$(simdi_iso) [skip ci]")
  if ! git push -q "$REMOTE" "$C:refs/heads/$DAL" 2>/tmp/kilit-init.$$; then
    echo "ILK_KURULUM_PUSH_BASARISIZ (başka koşucu aynı anda kurmuş olabilir): $(cat /tmp/kilit-init.$$)" >&2
  fi
  rm -f /tmp/kilit-init.$$
  getir || { echo "KILIT_DALI_OKUNAMADI" >&2; exit 13; }
}

komut="${1:-durum}"; RUN="${2:-}"
cd "$KOK"
getir || ilk_kurulum
S=$(git rev-parse "$REF"); MSG=$(git log -1 --format=%s "$S"); T=$(git rev-parse "$S^{tree}")

case "$komut" in
  durum) echo "$MSG";;
  al)
    [ -n "$RUN" ] || { echo "RUN gerekli" >&2; exit 2; }
    if [[ "$MSG" == LOCK* ]]; then
      AT=$(sed -n 's/.* at=\([^ ]*\).*/\1/p' <<<"$MSG")
      YAS=$(( ( $(date -u +%s) - $(date -u -d "$AT" +%s) ) / 60 ))
      if [ "$YAS" -lt "$BAYAT" ]; then echo "BASKA_KOSU_SURUYOR $MSG (yaş ${YAS} dk)"; exit 10; fi
      echo "BAYAT_KILIT_DEVRALINIYOR $MSG (yaş ${YAS} dk)"
    fi
    L=$(git commit-tree "$T" -p "$S" -m "LOCK run=$RUN at=$(simdi_iso) [skip ci]")
    if git push --porcelain --force-with-lease="refs/heads/$DAL:$S" "$REMOTE" "$L:refs/heads/$DAL" >/tmp/kilit.$$ 2>&1; then
      rm -f /tmp/kilit.$$; echo "ALINDI $L"
    else
      cat /tmp/kilit.$$ >&2; rm -f /tmp/kilit.$$; echo "YARIS_KAYBEDILDI"; exit 11
    fi;;
  birak)
    [ -n "$RUN" ] || { echo "RUN gerekli" >&2; exit 2; }
    [[ "$MSG" == "LOCK run=$RUN "* ]] || { echo "KILIT_BU_KOSUNUN_DEGIL $MSG"; exit 12; }
    F=$(git commit-tree "$T" -p "$S" -m "FREE run=$RUN at=$(simdi_iso) [skip ci]")
    git push -q --force-with-lease="refs/heads/$DAL:$S" "$REMOTE" "$F:refs/heads/$DAL"
    echo "BIRAKILDI $F";;
  *) echo "bilinmeyen komut: $komut" >&2; exit 2;;
esac
