#!/usr/bin/env bash
# mg53_setup.sh - from an empty Linux machine to the MG53 (TRIM72) upstream / downstream tables, Tahoe-100M data only.
#
#   bash mg53_p53/setup/mg53_setup.sh            start (or resume) every step in the background; safe to log out
#   bash mg53_p53/setup/mg53_setup.sh status     what is done, what is running, the end of the log
#   bash mg53_p53/setup/mg53_setup.sh stop       stop the background run (the first command resumes it)
#   bash mg53_p53/setup/mg53_setup.sh run        the same steps in this terminal (what the background run does)
#
# Options: --data DIR    data folder (default $TAHOE_DATA, else ~/Tahoe-100M)
#          --mode MODE   how Tahoe-100M gets here (default: what this data folder already uses, else full):
#                          full    download the whole dataset and keep it (429 GB, as 'tahoe download'; ~430 GB free)
#                          needed  download only what the analysis reads: the 3,388 expression files and the four
#                                  metadata tables (338 GB; ~345 GB free)
#                          stream  download each file, process it, delete it: only ~23 GB kept (~28 GB free)
#          --venv DIR    Python environment (default: the one this folder used, else $TAHOE_VENV, else ~/tahoe-venv;
#                        made if missing)
#          --workers N   plates read at once (default: from CPUs and free memory)
#          --redo STEP   forget STEP and every step after it, then run (e.g. --redo mg53_two_way)
# Optional: export HF_TOKEN=<your Hugging Face read token> before starting, for higher download rate limits.
#
# Steps, in order; each is marked done in <data>/.mg53_setup/ and skipped on a rerun, and an interrupted step resumes
# (a machine check runs first every time: python3 3.9+ with venv, curl, disk for the mode, memory, Hugging Face):
#   env            the Python environment: numpy pandas pyarrow scipy psutil fsspec aiohttp requests huggingface_hub
#   download       (full, needed) hf download tahoebio/Tahoe-100M into <data>, resumable, then every file checked
#   metadata       (stream) the four metadata tables
#   plates         (stream) which of the 3,388 expression files is on which plate
#   stream         (stream) each file downloaded once, read by the atlas build and the gene-panel extract, then
#                  replaced by an empty stub (setup/stream_build.py)
#   atlas_build    tahoe_atlas.py build: pseudobulk per well x cell line (~20 GB; stream: reuses the streamed plates)
#   atlas_effects  tahoe_atlas.py effects: method-v3 corrected effects (~30 min)
#   panel_extract  tahoe_gene_panel.py extract: per-cell gene panel (~2.6 GB; stream: reuses the streamed files)
#   panel_analyze  tahoe_gene_panel.py analyze: the gene panel with the atlas's corrections (~10 min)
#   ida            TRIM72 x idarubicin per cell line, corrected (trim72_idarubicin/corrected/trim72_ida_per_line.py)
#   mg53_<step>    mg53_p53/run_mg53_p53.py, one step at a time: perturbations coregulation p53_dependence downstream
#                  two_way single_cell_all upstream_tf summary (1-2 h; coregulation and upstream_tf download a TF
#                  list, HGNC / Ensembl coordinates and the CollecTRI / DoRothEA regulons once)
#   compare        your tables against the ones committed in this repository (<data>/mg53_p53/compare_with_repo.txt)
# Results: <data>/mg53_p53/SUMMARY.md and <data>/mg53_p53/summary/*.csv; idarubicin per line in
# <data>/mg53_p53/trim72_idarubicin/. Log: <data>/.mg53_setup/setup.log.
set -u

SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
HERE="$(dirname "$SELF")"
MG53="$(dirname "$HERE")"
REPO="$(dirname "$MG53")"
HF_REPO="tahoebio/Tahoe-100M"
N_FILES=3388
META_TABLES="cell_line_metadata drug_metadata gene_metadata sample_metadata"
MG53_STEPS="perturbations coregulation p53_dependence downstream two_way single_cell_all upstream_tf summary"
PKGS="numpy pandas pyarrow scipy psutil fsspec aiohttp requests huggingface_hub hf_xet brotli>=1.2.0"

absolute() {
  local p="$1"
  # shellcheck disable=SC2088
  case "$p" in "~") p="$HOME" ;; "~/"*) p="$HOME/${p#"~/"}" ;; /*) ;; *) p="$PWD/$p" ;; esac
  [ "$p" = / ] || p="${p%/}"
  printf '%s\n' "$p"
}

CMD="start"
DATA="${TAHOE_DATA:-$HOME/Tahoe-100M}"
VENV=""
MODE_ARG=""
WORKERS=""
REDO=""
while [ $# -gt 0 ]; do
  case "$1" in
    start|run|status|stop) CMD="$1" ;;
    --data) DATA="${2:?--data needs a folder}"; shift ;;
    --data=*) DATA="${1#--data=}" ;;
    --mode) MODE_ARG="${2:?--mode needs full, needed or stream}"; shift ;;
    --mode=*) MODE_ARG="${1#--mode=}" ;;
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
case "$MODE_ARG" in ""|full|needed|stream) ;; *) echo "--mode: full, needed or stream (not '$MODE_ARG')" >&2; exit 2 ;; esac
case "$WORKERS" in ""|[1-9]|[1-9][0-9]) ;; *) echo "--workers: a number from 1 to 99 (not '$WORKERS')" >&2; exit 2 ;; esac
DATA="$(absolute "$DATA")"
STATE="$DATA/.mg53_setup"
LOG="$STATE/setup.log"
OUT="$DATA/mg53_p53"
mkdir -p "$STATE" || exit 1
[ -z "$VENV" ] && [ -s "$STATE/venv" ] && VENV="$(cat "$STATE/venv")"   # the environment this folder was set up with
VENV="$(absolute "${VENV:-${TAHOE_VENV:-$HOME/tahoe-venv}}")"
PY="$VENV/bin/python"

# the mode: --mode, else the one this folder already uses, else full
if [ -n "$MODE_ARG" ]; then MODE="$MODE_ARG"
elif [ -f "$STATE/mode" ]; then MODE="$(cat "$STATE/mode")"
elif [ -f "$DATA/data/.streamed" ]; then MODE=stream
else MODE=full
fi
case "$MODE" in full|needed|stream) ;; *) MODE=full ;; esac       # an older run's 'local' = a full download
if [ "$MODE" = stream ]; then
  DATA_STEPS="metadata plates stream"
else
  DATA_STEPS="download"
fi
STEPS="env $DATA_STEPS atlas_build atlas_effects panel_extract panel_analyze ida"
for s in $MG53_STEPS; do STEPS="$STEPS mg53_$s"; done
STEPS="$STEPS compare"
if [ -n "$REDO" ]; then
  case " $STEPS " in *" $REDO "*) ;; *) echo "--redo: '$REDO' is not a step of mode $MODE; steps: $STEPS" >&2; exit 2 ;; esac
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
used_gb() { du -sk "$1" 2>/dev/null | awk '{ printf "%d\n", $1 / 1048576 }'; }
full_files() {      # expression files with cells in <data>/data (stubs of a stream are ~3 KB)
  find "$DATA/data" -maxdepth 1 -name '*.parquet' -size +1024k 2>/dev/null | wc -l | tr -d ' '
}
need_gb() {         # free disk the whole run needs in this mode (df -h units), counting what is here already
  local total
  case "$MODE" in full) total=430 ;; needed) total=345 ;; *) total=28 ;; esac
  echo $(( total - $(used_gb "$DATA") ))
}

# ----------------------------------------------------------------------------- status / stop / start
if [ "$CMD" = status ]; then
  pid="$(running_pid)"
  echo "data folder: $DATA    mode: $MODE    python: $PY"
  if [ -n "$pid" ]; then echo "running (pid $pid)"; else echo "not running"; fi
  for s in $STEPS; do
    if done_mark "$s"; then printf '  done     %-26s %s\n' "$s" "$(cat "$STATE/$s.done")"; else printf '  pending  %s\n' "$s"; fi
  done
  [ -d "$DATA/data" ] && echo "expression files with cells in $DATA/data: $(full_files) of $N_FILES ($(used_gb "$DATA") GB in the data folder)"
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
  args=(run --data "$DATA" --venv "$VENV" --mode "$MODE")
  [ -n "$WORKERS" ] && args+=(--workers "$WORKERS")
  [ -n "$REDO" ] && args+=(--redo "$REDO")
  if command -v setsid >/dev/null 2>&1; then
    setsid nohup bash "$SELF" "${args[@]}" </dev/null >>"$LOG" 2>&1 &
  else
    nohup bash "$SELF" "${args[@]}" </dev/null >>"$LOG" 2>&1 &
  fi
  echo "started in the background (pid $!; mode $MODE); safe to log out."
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
  for s in $STEPS; do [ "$s" = "$REDO" ] && hit=1; [ "$hit" = 1 ] && rm -f "$STATE/$s.done"; done
  say "redo: '$REDO' and every later step will run again"
fi
say "setup: data $DATA; mode $MODE; python $PY; repository $REPO ($(git -C "$REPO" rev-parse --short HEAD 2>/dev/null || echo 'no git'))"
T_ALL=$(date +%s)

step() {            # step NAME COMMAND...: run unless done; mark when it succeeds
  local name="$1" rc; shift
  if done_mark "$name"; then say "$name: done earlier"; return 0; fi
  say "$name: start"
  local t0; t0=$(date +%s)
  "$@"; rc=$?
  [ "$rc" = 0 ] || die "$name failed (exit $rc); the lines above have the error. Fix it, then rerun the same command (finished work is kept)."
  mark "$name"
  say "$name: done in $(( ($(date +%s) - t0 + 30) / 60 )) min"
}

# the machine check (every run) -----------------------------------------------
check() {
  local py3 have_data=0
  command -v curl >/dev/null 2>&1 || die "curl not found. Ubuntu/Debian: sudo apt-get install -y curl"
  if [ ! -x "$PY" ]; then
    py3="$(command -v python3 2>/dev/null)" || die "python3 not found. Ubuntu/Debian: sudo apt-get install -y python3 python3-venv"
    "$py3" -c 'import sys; sys.exit(sys.version_info < (3, 9))' \
      || die "python3 is $("$py3" -V 2>&1); 3.9 or newer is needed"
    "$py3" -c 'import venv, ensurepip' 2>/dev/null \
      || die "python3 has no venv/ensurepip. Ubuntu/Debian: sudo apt-get install -y python3-venv (or python3.X-venv for your python3 -V)"
  fi
  if [ "$MODE" = stream ] && [ ! -f "$DATA/data/.streamed" ] && [ "$(full_files)" -gt 0 ]; then
    die "$DATA/data holds $(full_files) expression files with cells (a download?); stream mode would replace them by empty stubs. Use --mode full (it finishes and checks the download) or another --data folder."
  fi
  done_mark stream && have_data=1
  done_mark download && have_data=1
  if [ "$have_data" = 0 ]; then
    local need; need="$(need_gb)"
    [ "$(free_gb)" -ge "$need" ] || die "$(free_gb) GB free in $DATA; mode $MODE needs ~$need GB more. Free space, use --data on a larger disk, or a smaller --mode (needed: 345 GB, stream: 28 GB)."
    curl -sSfI --retry 3 "https://huggingface.co/api/datasets/$HF_REPO" >/dev/null \
      || die "cannot reach huggingface.co (the data come from https://huggingface.co/datasets/$HF_REPO)"
  fi
  local memkb
  memkb="$(awk '/MemAvailable/ { print $2 }' /proc/meminfo 2>/dev/null)"
  if [ -n "$memkb" ] && [ "$memkb" -lt 4000000 ]; then
    say "warning: $(( memkb / 1048576 )) GB of free memory; ~3 GB per plate read at once and up to ~4 GB per MG53 step are needed"
  fi
  echo "$MODE" > "$STATE/mode"
  echo "$VENV" > "$STATE/venv"
  say "check: $(getconf _NPROCESSORS_ONLN 2>/dev/null || echo '?') CPUs; ${memkb:+$(( memkb / 1048576 )) GB free memory; }$(free_gb) GB free disk"
}

# env --------------------------------------------------------------------------
do_env() {
  if [ ! -x "$PY" ]; then
    python3 -m venv "$VENV" || die "could not make $VENV"
  fi
  "$PY" -m pip install --quiet --upgrade pip || return 1
  # shellcheck disable=SC2086
  "$PY" -m pip install --quiet $PKGS || return 1
  if "$PY" -m pip show brotlicffi >/dev/null 2>&1; then "$PY" -m pip install --quiet -U brotlicffi; fi  # an old one crashes hf
  "$PY" - <<'EOF'
import importlib
for m in ["numpy", "pandas", "pyarrow", "scipy", "psutil", "fsspec", "aiohttp", "requests", "huggingface_hub"]:
    print(f"  {m} {importlib.import_module(m).__version__}")
EOF
}

# download (full, needed) --------------------------------------------------------
download_complete() {       # every expression file with cells and the four metadata tables (hf checked each file)
  local t
  [ "$(full_files)" -ge "$N_FILES" ] || return 1
  for t in $META_TABLES; do [ -s "$DATA/metadata/$t.parquet" ] || return 1; done
}
download() {
  local hf="$VENV/bin/hf" a rc hfpid t inc=() n
  [ -x "$hf" ] || "$PY" -m pip install --quiet huggingface_hub hf_xet "brotli>=1.2.0" || return 1
  [ -x "$hf" ] || { say "download: no 'hf' command in $VENV/bin after installing huggingface_hub"; return 1; }
  if [ "$MODE" = needed ]; then
    inc=(--include "data/*.parquet")
    for t in $META_TABLES; do inc+=(--include "metadata/$t.parquet"); done
  fi
  say "download: $HF_REPO into $DATA ($([ "$MODE" = needed ] && echo '338 GB: expression files and metadata tables' || echo '429 GB: the whole dataset'));" \
      "files already complete are skipped, so a rerun resumes"
  for a in 1 2 3 4 5; do
    # parts left by an interrupted attempt are not resumed (each attempt names its own): delete them, they hold disk
    find "$DATA/.cache/huggingface/download" -name '*.incomplete' -type f -delete 2>/dev/null
    # no chunk cache (one pass over each file), no progress bars in the log: this loop reports progress instead
    HF_XET_CHUNK_CACHE_SIZE_BYTES=0 HF_HUB_DISABLE_PROGRESS_BARS=1 \
      "$hf" download "$HF_REPO" --repo-type dataset --local-dir "$DATA" ${inc[@]+"${inc[@]}"} > "$STATE/download.console" 2>&1 &
    hfpid=$!
    n=0
    while kill -0 "$hfpid" 2>/dev/null; do
      sleep 10; n=$((n + 1))
      [ $((n % 60)) = 0 ] && say "download: $(full_files) of $N_FILES expression files, $(used_gb "$DATA") GB in $DATA"
    done
    wait "$hfpid"; rc=$?
    if [ "$rc" = 0 ] && download_complete; then
      say "download: complete and checked ($(full_files) expression files, the metadata tables; $(used_gb "$DATA") GB)"
      return 0
    fi
    tail -n 5 "$STATE/download.console"
    if grep -q "takes no keyword arguments" "$STATE/download.console"; then      # the Brotli crash: drop Brotli
      say "download: Brotli version conflict; removing brotli/brotlicffi"
      "$PY" -m pip uninstall -y brotli brotlicffi >/dev/null 2>&1
    fi
    [ "$a" -lt 5 ] && { say "download: attempt $a stopped (exit $rc; $(full_files) of $N_FILES files); retrying in 60 s (finished files are kept)"; sleep 60; }
  done
  say "download: not complete after 5 attempts ($(full_files) of $N_FILES expression files); the error is above and in $STATE/download.console"
  return 1
}

# the other data steps -----------------------------------------------------------
stream_with_retries() {     # a dropped connection costs a rerun, not the night: up to 3 automatic reruns
  local a
  for a in 1 2 3 4; do
    "$PY" "$HERE/stream_build.py" stream --data "$DATA" ${WORKERS:+--workers "$WORKERS"} && return 0
    [ "$a" -lt 4 ] && { say "stream: incomplete; rerun $a of 3 in 60 s (finished plates and files are kept)"; sleep 60; }
  done
  return 1
}
atlas_build() {
  if [ "$MODE" = stream ]; then
    "$PY" "$HERE/stream_build.py" finish --data "$DATA"
  else
    "$PY" "$REPO/tahoe_atlas.py" build --data "$DATA" ${WORKERS:+--workers "$WORKERS"}
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

check
[ -x "$PY" ] || rm -f "$STATE/env.done"        # the environment was removed since: make it again
step env do_env
if [ "$MODE" = stream ]; then
  step metadata "$PY" "$HERE/stream_build.py" metadata --data "$DATA"
  step plates "$PY" "$HERE/stream_build.py" plates --data "$DATA"
  step stream stream_with_retries
else
  step download download
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
