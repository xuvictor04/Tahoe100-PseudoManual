#!/usr/bin/env bash
# mg53_setup.sh - from an empty Linux machine to the MG53 (TRIM72) upstream / downstream tables, Tahoe-100M data only.
#
#   bash mg53_p53/setup/mg53_setup.sh            start (or resume) every step in the background; safe to log out
#   bash mg53_p53/setup/mg53_setup.sh status     what is done, what is running, the end of the log
#   bash mg53_p53/setup/mg53_setup.sh stop       stop the background run (the first command resumes it)
#   bash mg53_p53/setup/mg53_setup.sh run        the same steps in this terminal (what the background run does)
#
# Options: --data DIR    data folder (default $TAHOE_DATA, else ~/Tahoe-100M)
#          --venv DIR    Python environment (default $TAHOE_VENV, else ~/tahoe-venv; made if missing)
#          --workers N   plates streamed at once (default: one per CPU, at most one per ~3 GB of free memory)
#          --redo STEP   forget STEP and every step after it, then run (e.g. --redo mg53)
#
# Steps, in order; each is marked done in <data>/.mg53_setup/ and skipped on a rerun, and an interrupted step resumes:
#   check          python3 (3.9+, with venv) and curl present, disk and memory enough, Hugging Face reachable
#   env            the Python environment: numpy pandas pyarrow scipy psutil fsspec aiohttp requests
#   metadata       the four Tahoe-100M metadata tables (~50 MB)
#   plates         which of the 3,388 expression files is on which plate (reads one column chunk per file)
#   stream         each expression file downloaded once, read by the atlas pseudobulk build and the per-cell gene
#                  panel extract, then replaced by an empty stub: 340 GB downloaded, ~23 GB kept (hours)
#   atlas_build    tahoe_atlas.py build: the streamed plates indexed and reused (minutes)
#   atlas_effects  tahoe_atlas.py effects: method-v3 corrected effects (~30 min)
#   panel_extract  tahoe_gene_panel.py extract: the per-cell files reused, well tables built (~10 min)
#   panel_analyze  tahoe_gene_panel.py analyze: the gene panel with the atlas's corrections (~10 min)
#   ida            TRIM72 x idarubicin per cell line, corrected (trim72_idarubicin/corrected/trim72_ida_per_line.py)
#   mg53_<step>    mg53_p53/run_mg53_p53.py, one step at a time: perturbations coregulation p53_dependence downstream
#                  two_way single_cell_all upstream_tf summary (1-2 h; the coregulation and upstream_tf steps download
#                  a TF list, HGNC / Ensembl coordinates and the CollecTRI / DoRothEA regulons once)
#   compare        your tables against the ones committed in this repository (<data>/mg53_p53/compare_with_repo.txt)
# A folder that already holds the full download (3,388 files with cells in <data>/data) is used as it is: plates and
# stream are skipped and atlas_build / panel_extract read the files (the download is never modified).
# Results: <data>/mg53_p53/SUMMARY.md and <data>/mg53_p53/summary/*.csv; idarubicin per line in
# <data>/mg53_p53/trim72_idarubicin/. Log: <data>/.mg53_setup/setup.log.
set -u

SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
HERE="$(dirname "$SELF")"
MG53="$(dirname "$HERE")"
REPO="$(dirname "$MG53")"
MG53_STEPS="perturbations coregulation p53_dependence downstream two_way single_cell_all upstream_tf summary"
ALL_STEPS="check env metadata plates stream atlas_build atlas_effects panel_extract panel_analyze ida"
for s in $MG53_STEPS; do ALL_STEPS="$ALL_STEPS mg53_$s"; done
ALL_STEPS="$ALL_STEPS compare"
PKGS="numpy pandas pyarrow scipy psutil fsspec aiohttp requests"
NEED_GB=28          # free disk for a stream from nothing: ~23 GB kept, files in flight, the MG53 outputs and caches

absolute() {
  local p="$1"
  # shellcheck disable=SC2088
  case "$p" in "~") p="$HOME" ;; "~/"*) p="$HOME/${p#"~/"}" ;; /*) ;; *) p="$PWD/$p" ;; esac
  [ "$p" = / ] || p="${p%/}"
  printf '%s\n' "$p"
}

CMD="start"
DATA="${TAHOE_DATA:-$HOME/Tahoe-100M}"
VENV="${TAHOE_VENV:-$HOME/tahoe-venv}"
WORKERS=""
REDO=""
while [ $# -gt 0 ]; do
  case "$1" in
    start|run|status|stop) CMD="$1" ;;
    --data) DATA="${2:?--data needs a folder}"; shift ;;
    --data=*) DATA="${1#--data=}" ;;
    --venv) VENV="${2:?--venv needs a folder}"; shift ;;
    --venv=*) VENV="${1#--venv=}" ;;
    --workers) WORKERS="${2:?--workers needs a number}"; shift ;;
    --workers=*) WORKERS="${1#--workers=}" ;;
    --redo) REDO="${2:?--redo needs a step}"; shift ;;
    --redo=*) REDO="${1#--redo=}" ;;
    -h|--help|help) sed -n '2,/^set -u/p' "$SELF" | sed '$d; s/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown argument: $1 (see: bash $0 --help)" >&2; exit 2 ;;
  esac
  shift
done
DATA="$(absolute "$DATA")"
VENV="$(absolute "$VENV")"
STATE="$DATA/.mg53_setup"
LOG="$STATE/setup.log"
PY="$VENV/bin/python"
OUT="$DATA/mg53_p53"
mkdir -p "$STATE" || exit 1
if [ -n "$REDO" ]; then
  case " $ALL_STEPS " in *" $REDO "*) ;; *) echo "--redo: unknown step '$REDO'; steps: $ALL_STEPS" >&2; exit 2 ;; esac
fi

say() { printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"; }
die() { say "STOPPED: $*"; exit 1; }
running_pid() {     # the pid of a live background run, if any
  local pid
  pid="$(cat "$STATE/pid" 2>/dev/null)" || return 1
  [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && ps -o args= -p "$pid" 2>/dev/null | grep -q "mg53_setup.sh" \
    && printf '%s\n' "$pid"
}
done_mark() { [ -f "$STATE/$1.done" ]; }
mark() { date '+%Y-%m-%d %H:%M:%S' > "$STATE/$1.done"; }
free_gb() { df -Pk "$DATA" | awk 'NR == 2 { printf "%d\n", $4 / 1048576 }'; }
used_gb() { du -sk "$@" 2>/dev/null | awk '{ s += $1 } END { printf "%d\n", s / 1048576 }'; }

mode() {            # stream (the default) or local (a full download is already in <data>/data)
  if [ -f "$STATE/mode" ]; then cat "$STATE/mode"; return; fi
  local n=0
  if [ -d "$DATA/data" ] && [ ! -f "$DATA/data/.streamed" ]; then
    n="$(find "$DATA/data" -maxdepth 1 -name '*.parquet' -size +1024k 2>/dev/null | wc -l | tr -d ' ')"
  fi
  if [ "$n" -ge 3388 ]; then echo local
  elif [ "$n" -gt 0 ]; then echo "partial:$n"
  else echo stream
  fi
}

# ----------------------------------------------------------------------------- status / stop / start
if [ "$CMD" = status ]; then
  pid="$(running_pid)"
  echo "data folder: $DATA    python: $PY    mode: $(mode)"
  if [ -n "$pid" ]; then echo "running (pid $pid)"; else echo "not running"; fi
  for s in $ALL_STEPS; do
    if done_mark "$s"; then printf '  done     %-26s %s\n' "$s" "$(cat "$STATE/$s.done")"; else printf '  pending  %s\n' "$s"; fi
  done
  [ -f "$OUT/SUMMARY.md" ] && echo "results: $OUT/SUMMARY.md"
  [ -f "$LOG" ] && { echo "--- end of $LOG"; tail -n 15 "$LOG"; }
  exit 0
fi
if [ "$CMD" = stop ]; then
  pid="$(running_pid)" || true
  [ -z "$pid" ] && { echo "not running"; exit 0; }
  kill -TERM -- "-$pid" 2>/dev/null || kill -TERM "$pid"
  for _ in $(seq 1 50); do kill -0 "$pid" 2>/dev/null || break; sleep 0.2; done
  kill -KILL -- "-$pid" 2>/dev/null || true
  rm -f "$STATE/pid"
  echo "stopped; rerun 'bash $SELF --data $DATA' to resume"
  exit 0
fi
if [ "$CMD" = start ]; then
  pid="$(running_pid)" && { echo "already running (pid $pid); follow it: tail -f $LOG"; exit 0; }
  args=(run --data "$DATA" --venv "$VENV")
  [ -n "$WORKERS" ] && args+=(--workers "$WORKERS")
  [ -n "$REDO" ] && args+=(--redo "$REDO")
  if command -v setsid >/dev/null 2>&1; then
    setsid nohup bash "$SELF" "${args[@]}" </dev/null >>"$LOG" 2>&1 &
  else
    nohup bash "$SELF" "${args[@]}" </dev/null >>"$LOG" 2>&1 &
  fi
  echo "started in the background (pid $!); safe to log out."
  echo "  follow it:   tail -f $LOG"
  echo "  where it is: bash $SELF status --data $DATA"
  echo "  results:     $OUT/SUMMARY.md (at the end)"
  exit 0
fi

# ----------------------------------------------------------------------------- run
other="$(running_pid)" && [ "$other" != "$$" ] && die "another run is going (pid $other); 'stop' it first"
echo "$$" > "$STATE/pid"
trap 'rm -f "$STATE/pid"' EXIT
[ -t 1 ] && exec > >(tee -a "$LOG") 2>&1
if [ -n "$REDO" ]; then
  hit=0
  for s in $ALL_STEPS; do [ "$s" = "$REDO" ] && hit=1; [ "$hit" = 1 ] && rm -f "$STATE/$s.done"; done
  say "redo: '$REDO' and every later step will run again"
fi
say "setup: data $DATA; python $PY; repository $REPO ($(git -C "$REPO" rev-parse --short HEAD 2>/dev/null || echo 'no git'))"
T_ALL=$(date +%s)

step() {            # step NAME COMMAND...: run unless done; mark when it succeeds
  local name="$1"; shift
  if done_mark "$name"; then say "$name: done earlier"; return 0; fi
  say "$name: start"
  local t0; t0=$(date +%s)
  "$@" || die "$name failed (exit $?); the lines above have the error. Fix it, then rerun the same command (finished work is kept)."
  mark "$name"
  say "$name: done in $(( ($(date +%s) - t0 + 30) / 60 )) min"
}

# check ------------------------------------------------------------------------
do_check() {
  local py3 m
  command -v curl >/dev/null 2>&1 || die "curl not found. Ubuntu/Debian: sudo apt-get install -y curl"
  if [ ! -x "$PY" ]; then
    py3="$(command -v python3 2>/dev/null)" || die "python3 not found. Ubuntu/Debian: sudo apt-get install -y python3 python3-venv"
    "$py3" -c 'import sys; sys.exit(sys.version_info < (3, 9))' \
      || die "python3 is $("$py3" -V 2>&1); 3.9 or newer is needed"
    "$py3" -c 'import venv, ensurepip' 2>/dev/null \
      || die "python3 has no venv/ensurepip. Ubuntu/Debian: sudo apt-get install -y python3-venv (or python3.X-venv)"
  fi
  m="$(mode)"
  case "$m" in
    partial:*) die "$DATA/data holds ${m#partial:} of the 3,388 expression files with cells (an unfinished download?). Finish it (tahoe download), or move it away to stream instead." ;;
  esac
  if [ "$m" = stream ] && ! done_mark stream; then
    local have need
    have="$(used_gb "$DATA/atlas/pseudobulk" "$DATA/gene_panel/cells")"
    need=$(( NEED_GB - have ))
    [ "$(free_gb)" -ge "$need" ] || die "$(free_gb) GB free in $DATA; the stream needs ~$need GB more (~$NEED_GB GB in all). Free some space or use --data on a larger disk."
  fi
  local memkb
  memkb="$(awk '/MemAvailable/ { print $2 }' /proc/meminfo 2>/dev/null)"
  if [ -n "$memkb" ] && [ "$memkb" -lt 4000000 ]; then
    say "warning: $(( memkb / 1048576 )) GB of free memory; ~3 GB per streamed plate and up to ~4 GB per MG53 step are needed"
  fi
  if [ "$m" = stream ] && ! done_mark stream; then
    curl -sSfI --retry 3 "https://huggingface.co/api/datasets/tahoebio/Tahoe-100M" >/dev/null \
      || die "cannot reach huggingface.co (the data come from https://huggingface.co/datasets/tahoebio/Tahoe-100M)"
  fi
  [ -f "$STATE/mode" ] || echo "$m" > "$STATE/mode"
  say "check: mode $m; $(getconf _NPROCESSORS_ONLN 2>/dev/null || echo '?') CPUs; ${memkb:+$(( memkb / 1048576 )) GB free memory; }$(free_gb) GB free disk"
}

# env --------------------------------------------------------------------------
do_env() {
  if [ ! -x "$PY" ]; then
    python3 -m venv "$VENV" || die "could not make $VENV"
  fi
  "$PY" -m pip install --quiet --upgrade pip || return 1
  # shellcheck disable=SC2086
  "$PY" -m pip install --quiet $PKGS || return 1
  "$PY" - <<'EOF'
import importlib
for m in ["numpy", "pandas", "pyarrow", "scipy", "psutil", "fsspec", "aiohttp", "requests"]:
    print(f"  {m} {importlib.import_module(m).__version__}")
EOF
}

# the data steps ---------------------------------------------------------------
stream_with_retries() {     # a dropped connection costs a rerun, not the night: up to 3 automatic reruns
  local a
  for a in 1 2 3 4; do
    "$PY" "$HERE/stream_build.py" stream --data "$DATA" ${WORKERS:+--workers "$WORKERS"} && return 0
    [ "$a" -lt 4 ] && { say "stream: incomplete; rerun $a of 3 in 60 s (finished plates and files are kept)"; sleep 60; }
  done
  return 1
}
atlas_build() {
  if [ "$(mode)" = local ]; then
    "$PY" "$REPO/tahoe_atlas.py" build --data "$DATA" ${WORKERS:+--workers "$WORKERS"}
  else
    "$PY" "$HERE/stream_build.py" finish --data "$DATA"
  fi
}
ida() {
  "$PY" "$REPO/trim72_idarubicin/corrected/trim72_ida_per_line.py" --data "$DATA" --outdir "$OUT/trim72_idarubicin" \
    > "$STATE/ida.console" 2>&1 || { tail -n 30 "$STATE/ida.console"; return 1; }
  say "ida: tables in $OUT/trim72_idarubicin"
}
mg53() {
  "$PY" "$MG53/run_mg53_p53.py" --data "$DATA" --out "$OUT" --steps "$1"
}
metadata() {
  if [ "$(mode)" = local ] && ls "$DATA"/metadata/*.parquet >/dev/null 2>&1; then
    say "metadata: from the download"
    return 0
  fi
  "$PY" "$HERE/stream_build.py" metadata --data "$DATA"
}

[ -x "$PY" ] || rm -f "$STATE/env.done"        # the environment was removed since: make it again
step check do_check
step env do_env
step metadata metadata
if [ "$(mode)" = stream ]; then
  step plates "$PY" "$HERE/stream_build.py" plates --data "$DATA"
  step stream stream_with_retries
else
  say "plates, stream: not needed (the full download is in $DATA/data)"
  mark plates; mark stream
fi
step atlas_build atlas_build
step atlas_effects "$PY" "$REPO/tahoe_atlas.py" effects --data "$DATA"
step panel_extract "$PY" "$REPO/tahoe_gene_panel.py" extract --data "$DATA" ${WORKERS:+--workers "$WORKERS"}
step panel_analyze "$PY" "$REPO/tahoe_gene_panel.py" analyze --data "$DATA"
step ida ida
for s in $MG53_STEPS; do step "mg53_$s" mg53 "$s"; done
step compare "$PY" "$HERE/compare_with_repo.py" --out "$OUT"
say "all done in $(( ($(date +%s) - T_ALL + 30) / 60 )) min. Start with $OUT/SUMMARY.md (tables in $OUT/summary/);"
say "idarubicin per line: $OUT/trim72_idarubicin/; against the repository: $OUT/compare_with_repo.txt"
