#!/usr/bin/env bash
# Download Tahoe-100M (about 429 GB, 4,427 files) from Hugging Face.
# Safe to rerun: files that already finished are skipped.
#
#   bash 00_download_tahoe.sh                 # downloads into ~/Tahoe-100M
#   bash 00_download_tahoe.sh /data/Tahoe-100M
#
# Optional, for higher rate limits: create a free read token at huggingface.co/settings/tokens and run
#   export HF_TOKEN=hf_xxx
# before this script.
set -uo pipefail

DEST="${1:-$HOME/Tahoe-100M}"
LOG="$(mktemp)"
mkdir -p "$DEST"

echo "Installing tools (huggingface_hub, hf_xet, brotli, pyarrow, pandas, numpy, duckdb) ..."
pip install -q -U huggingface_hub hf_xet "brotli>=1.2.0" pyarrow pandas numpy duckdb
# An old brotlicffi also triggers the "process() takes no keyword arguments" crash
if pip show brotlicffi >/dev/null 2>&1; then pip install -q -U brotlicffi; fi

df -hP "$DEST" | tail -1 | awk '{print "Free space at destination: " $4 " (need about 430G for everything)"}'

for attempt in 1 2 3; do
  echo "Download attempt $attempt into $DEST ..."
  if hf download tahoebio/Tahoe-100M --repo-type dataset --local-dir "$DEST" 2>&1 | tee "$LOG"; then
    echo "Download complete: $DEST"
    exit 0
  fi
  if grep -q "takes no keyword arguments" "$LOG"; then
    echo "Brotli version conflict detected: removing brotli packages, then retrying."
    pip uninstall -y brotli brotlicffi || true
  fi
  echo "Attempt $attempt failed; retrying (finished files are kept)."
  sleep 5
done
echo "Download did not finish after 3 attempts. The last error is above."
exit 1
