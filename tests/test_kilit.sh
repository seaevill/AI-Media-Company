#!/usr/bin/env bash
# Kilit testi: yerel çıplak (bare) uzak depo ile iki koşucu yarışı. Çalıştır: bash tests/test_kilit.sh
set -uo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
git init -q --bare "$TMP/uzak.git"
kopya() { git clone -q "$TMP/uzak.git" "$TMP/$1" 2>/dev/null; mkdir -p "$TMP/$1/scripts" "$TMP/$1/vardiyalar"; cp "$KOK/scripts/kilit.sh" "$TMP/$1/scripts/"; cp "$KOK/vardiyalar/CONFIG.json" "$TMP/$1/vardiyalar/"; git -C "$TMP/$1" config user.email t@example.invalid; git -C "$TMP/$1" config user.name test; }
kopya A; kopya B
gecti=0; kaldi=0
kontrol() { if [ "$2" = "$3" ]; then echo "GEÇTİ $1"; gecti=$((gecti+1)); else echo "KALDI $1 (beklenen $3, gelen $2)"; kaldi=$((kaldi+1)); fi; }

( cd "$TMP/A" && bash scripts/kilit.sh al RUN-A >/dev/null ); kontrol "A kilidi alır" $? 0
( cd "$TMP/B" && bash scripts/kilit.sh al RUN-B >/dev/null ); kontrol "B taze kilidi görünce durur" $? 10
( cd "$TMP/B" && bash scripts/kilit.sh birak RUN-B >/dev/null ); kontrol "B başkasının kilidini bırakamaz" $? 12
( cd "$TMP/A" && bash scripts/kilit.sh birak RUN-A >/dev/null ); kontrol "A kendi kilidini bırakır" $? 0

# Yarış: ikisi de FREE görüp aynı anda almaya çalışsın -> biri kazanır, diğeri lease ile reddedilir.
( cd "$TMP/A" && git fetch -q origin +refs/heads/lock/medya:refs/remotes/origin/lock/medya )
( cd "$TMP/B" && git fetch -q origin +refs/heads/lock/medya:refs/remotes/origin/lock/medya )
S=$(git -C "$TMP/A" rev-parse refs/remotes/origin/lock/medya); T=$(git -C "$TMP/A" rev-parse "$S^{tree}")
LA=$(git -C "$TMP/A" commit-tree "$T" -p "$S" -m "LOCK run=RA at=$(date -u +%FT%TZ)")
LB=$(git -C "$TMP/B" commit-tree "$T" -p "$S" -m "LOCK run=RB at=$(date -u +%FT%TZ)")
git -C "$TMP/A" push -q --force-with-lease=refs/heads/lock/medya:$S origin $LA:refs/heads/lock/medya 2>/dev/null; kontrol "yarış: ilk gelen alır" $? 0
git -C "$TMP/B" push -q --force-with-lease=refs/heads/lock/medya:$S origin $LB:refs/heads/lock/medya 2>/dev/null; r=$?; [ $r -ne 0 ] && r=1; kontrol "yarış: eski görünümle ikinci alma reddedilir" $r 1

# Bayat kilit devralma
CIKTI=$(cd "$TMP/B" && KILIT_BAYAT_DK=0 bash scripts/kilit.sh al RUN-B2); r=$?
case "$CIKTI" in *BAYAT_KILIT_DEVRALINIYOR*ALINDI*) [ $r -eq 0 ] && r=0 || r=1;; *) r=1;; esac; kontrol "bayat kilit devralınır, raporlanır ve alınır" $r 0
echo "$gecti geçti, $kaldi kaldı"; [ $kaldi -eq 0 ]
