#!/usr/bin/env python3
r"""
tahoe_mtap_gankyrin.py
MTAP and Gankyrin (PSMD10) in Tahoe-100M, rebuilt from the single-cell data with
corrections for the technical artifacts found in the published pseudobulk table.

Run it from the folder you downloaded Tahoe-100M into:

    python3 tahoe_mtap_gankyrin.py all        # extract + analyze (start here)
    python3 tahoe_mtap_gankyrin.py extract    # one pass over the ~95M cells (resumable)
    python3 tahoe_mtap_gankyrin.py analyze    # corrected analyses from the extracted tables (minutes)
    python3 tahoe_mtap_gankyrin.py coreg      # optional, heavy: genome-wide co-regulation (pseudobulk table)

Quick trial on a few files first:   python3 tahoe_mtap_gankyrin.py all --limit-files 30
Long run that survives logout:      nohup python3 tahoe_mtap_gankyrin.py all > /dev/null 2>&1 &
On Windows (PowerShell):            C:\tahoe\.venv\Scripts\python.exe tahoe_mtap_gankyrin.py all  (keep window open)
Every run appends its log to mtap_gankyrin/mtap_gankyrin.log (tail -f mtap_gankyrin/mtap_gankyrin.log;
Windows: Get-Content mtap_gankyrin\mtap_gankyrin.log -Wait) and keeps the computer from sleeping while it runs.

Corrections built in (each one targets a problem found in the published DE table):
  1. Plate baseline: every well is compared with the median of all drug wells on the same plate
     for the same cell line, not with the plate's DMSO wells (one bad DMSO well shifted a whole plate).
  2. Well position: the effect of each well position is estimated from the OTHER drugs that sat in
     the same position on other plates (leave-drug-out median) and subtracted.
  3. Calibrated statistics: each well's effect is scored against the spread of all other wells
     (robust z), so well-to-well noise is part of the null. Cell lines in one well are not treated
     as independent replicates.
  4. Counting: cell lines are counted once per drug and dose, even if it was tested on two plates.
Method v3 (found on the full real run; numbers differ from earlier runs, see README 'Method v3'):
  5. Composition: when the atlas (<data>/atlas, --atlas) exported it, each profile's library-composition shift
     (median-of-ratios over the line's well-expressed genes) is subtracted, so a few hugely induced genes cannot
     make every other gene look lower.
  6. Plate dispersion: each (plate, dose) group's spread is compared with the same dose on the other plates; a
     noisier group gets its z divided by that factor (only ever widened, never narrowed).
  7. Unreliable plates (--unreliable-plates; default plate13): kept per well, left out of the pooled drug-doses
     that have a well elsewhere, of the reference spread and of the plate-factor peers.
  8. Position correction in two passes: donors whose own first-pass |z| >= 3 for the gene are left out, so a strong
     drug at the same well position cannot create a mirror-image effect; wells without enough clean donors are not
     corrected and flagged ('position correction uncertain' / 'position not correctable').

Requires numpy, pandas, pyarrow (and duckdb for 'coreg').
"""

import argparse
import contextlib
import glob
import json
import math
import multiprocessing as mp
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import time
import traceback
from collections import defaultdict

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

# ----------------------------------------------------------------------------- settings
TARGET_GENES = ["MTAP", "PSMD10", "CDKN2A", "CDKN2B"]  # PSMD10 = Gankyrin; CDKN2A/B = 9p21 neighbours of MTAP
EFFECT_GENES = ["MTAP", "PSMD10", "PROTEASOME"]          # get full drug-effect tables
DMSO_PREFIX = "DMSO"            # DMSO_TF marks vehicle controls
MIN_CELLS = 30                  # min cells of one cell line in one well to use its expression
LFC_MIN = math.log2(1.2)        # min log2 fold change to count a cell line or call a drug (1.2x)
Z_LINE = 2.0                    # per-cell-line z cutoff for counting a line as changed
FDR_CUT = 0.10                  # FDR cutoff for calling a drug
NULL_FRAC = 0.30                # MTAP-null fallback cut (fraction of the median line, all wells); see null_threshold
MIN_LINE_CELLS = 200            # lines with fewer cells in total are not classified
MIN_SLOT_WELLS = 3              # need >= this many other-drug wells to estimate a position effect
MIN_LINES = 5                   # a well's effect on a gene needs >= this many measured lines (as tahoe_atlas.py; a
                                # gene measured in fewer lines in a typical well: any well with a measured line counts)
# method v3 (README 'Method v3'): numbers differ from the earlier runs (v2)
METHOD_VERSION = 3              # results/run_info.json; tahoe_gene_panel.py needs >= 3, tahoe_status.py reads it
UNRELIABLE_PLATES = ("plate13",)  # default --unreliable-plates (when present): its wells stay in the per-well
                                # tables but leave the reference spread, the plate-factor peers and every drug-dose
                                # that also has a well on another plate (plate 13 of the real data does not reproduce)
POS_CLEAN_Z = 3.0               # position correction, pass 2: donor wells only with |first-pass z| < this (per gene)
PLATE_SCALE_MIN_WELLS = 20      # a (plate, dose) group with fewer drug wells joins its plate's largest group
NOISY_PLATE = 1.2               # flag 'noisy plate (z scaled)' above this plate factor
PLATE_SCALE_BAND = 1.3          # a gene whose own spread ratio on a plate group exceeds the group factor x this (about
                                # the upper sampling band of a MAD ratio over ~90 wells) gets ratio / this instead
ROW_SHIFT = 0.8                 # a plate row whose other drug wells moved by more (log2 cells) is itself shifted
TOXIC_BEST_WELL = -0.5          # 'toxic' of a drug-dose with several used wells: its best well lost cells too (log2)
COMPOSITION_FLAG = 0.2          # flag 'composition shift' at |drug-dose composition shift| >= this (log2)
WELL_COLS = ["plate", "drug", "conc", "slot", "well", "is_dmso", "unreliable_plate"]   # every per-well table
REDUCE_EVERY = 50               # extract: merge the per-file tables every this many files (main process stays ~1 GB)
MIN_BASEMEAN = 5                # coreg: ignore genes with lower baseMean in a test
N_PCS = 3                       # coreg: broad shared responses (principal components) removed before correlating;
                                # more can also remove real modules, so both raw and adjusted r are reported

# Tirosh et al. 2016 cell-cycle genes (old and current HGNC names both listed)
S_GENES = """MCM5 PCNA TYMS FEN1 MCM2 MCM4 RRM1 UNG GINS2 MCM6 CDCA7 DTL PRIM1 UHRF1 MLF1IP CENPU
HELLS RFC2 RPA2 NASP RAD51AP1 GMNN WDR76 SLBP CCNE2 UBR7 POLD3 MSH2 ATAD2 RAD51 RRM2 CDC45 CDC6
EXO1 TIPIN DSCC1 BLM CASP8AP2 USP1 CLSPN POLA1 CHAF1B BRIP1 E2F8""".split()
G2M_GENES = """HMGB2 CDK1 NUSAP1 UBE2C BIRC5 TPX2 TOP2A NDC80 CKS2 NUF2 CKS1B MKI67 TMPO CENPF TACC3
FAM64A PIMREG SMC4 CCNB2 CKAP2L CKAP2 AURKB BUB1 KIF11 ANP32E TUBB4B GTSE1 KIF20B HJURP CDCA3 HN1
JPT1 CDC20 TTK CDC25C KIF2C RANGAP1 NCAPD2 DLGAP5 CDCA2 CDCA8 ECT2 KIF23 HMMR AURKA PSRC1 ANLN LBR
CKAP5 CENPE CTCF NEK2 G2E3 GAS2L3 CBX5 CENPA""".split()
PROTEASOME_RE = re.compile(r"^(PSMA[1-7]|PSMB[1-7]|PSMC[1-6]|PSMD[1-9]|PSMD1[0-4])$")
PROTEASOME_EXCLUDE = {"PSMD5", "PSMD9", "PSMD10"}  # assembly chaperones; PSMD10 is Gankyrin itself

# drugs named in the earlier analyses, printed side by side in the summary
WATCH = ["Pyridoxine", "HI-TOPK-032", "Docetaxel", "Calcium lactate", "Daptomycin", "XRK3F2",
         "Lenalidomide", "Simotinib", "Ranolazine", "Afatinib", "Bentamapimod", "NG25",
         "Darinaparsin", "Dinaciclib", "Harringtonine"]

META_COLS = ["BARCODE_SUB_LIB_ID", "sample", "plate", "drug", "cell_line_id"]
INDEX_VERSION = 2
ROWS = "ABCDEFGH"


def _to_log_file(text):
    """Append to the run log named by TAHOE_LOG_FILE (set by start_run_log; worker processes inherit it)."""
    path = os.environ.get("TAHOE_LOG_FILE")
    if path:
        try:
            with open(path, "a", encoding="utf-8") as fh:
                fh.write(text + "\n")
        except Exception:  # noqa: BLE001  (logging must never stop a run)
            pass


def log(msg):
    line = time.strftime("[%H:%M:%S] ") + str(msg)
    try:
        print(line, flush=True)
    except UnicodeEncodeError:                  # console code page without these characters (Windows)
        enc = getattr(sys.stdout, "encoding", None) or "ascii"
        try:
            print(line.encode(enc, "replace").decode(enc), flush=True)
        except Exception:  # noqa: BLE001
            pass
    except OSError:                             # console gone (closed pipe): the run log still gets the line
        if not os.environ.get("TAHOE_LOG_FILE"):
            raise
    _to_log_file(line)


# ============================================================================= platform helpers
def safe_console():
    """Characters the console cannot show (Windows code pages) are printed as escapes instead of crashing."""
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="backslashreplace")
        except Exception:  # noqa: BLE001  (not a text stream)
            pass


def start_run_log(path, title):
    """From now on every log() line, also from worker processes (they inherit the environment), is appended to
    `path`, and so is the traceback of a crash (sys.exit messages: log_exit). Returns the absolute path."""
    path = os.path.abspath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    os.environ["TAHOE_LOG_FILE"] = path
    safe_console()
    try:
        plat = platform.platform()
    except Exception:  # noqa: BLE001
        plat = sys.platform
    v = sys.version_info
    _to_log_file(("\n" if os.path.exists(path) and os.path.getsize(path) else "")
                 + f"===== {title} started {time.strftime('%Y-%m-%d %H:%M:%S')} | Python {v.major}.{v.minor}.{v.micro}"
                 f" | {plat} =====")
    prev = sys.excepthook
    if not getattr(prev, "_tahoe", False):
        def hook(et, ev, tb):                   # the file gets the traceback; the console gets it from prev
            what = "STOPPED by Ctrl-C" if issubclass(et, KeyboardInterrupt) else \
                "CRASHED:\n" + "".join(traceback.format_exception(et, ev, tb)).rstrip()
            _to_log_file(time.strftime("[%H:%M:%S] ") + what)
            prev(et, ev, tb)
        hook._tahoe = True
        sys.excepthook = hook
    return path


def log_exit(e):
    """Write why a run stopped through sys.exit (which bypasses the excepthook) to the run log."""
    code = getattr(e, "code", None)
    if code not in (None, 0):
        _to_log_file(time.strftime("[%H:%M:%S] ") + (f"STOPPED: {code}" if isinstance(code, str)
                                                     else f"STOPPED with exit code {code}"))


@contextlib.contextmanager
def keep_awake(reason="the computation"):
    """Keep the computer from sleeping while the block runs (Windows; macOS caffeinate; Linux systemd-inhibit).
    Never raises; does nothing where it cannot. A laptop still sleeps when its lid is closed."""
    stop, how = None, ""
    try:
        if sys.platform == "win32":
            import ctypes
            f = ctypes.windll.kernel32.SetThreadExecutionState
            f.argtypes, f.restype = [ctypes.c_uint], ctypes.c_uint
            ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
            if f(ES_CONTINUOUS | ES_SYSTEM_REQUIRED):
                stop, how = (lambda: f(ES_CONTINUOUS)), "Windows"
        else:
            cmd = None
            if sys.platform == "darwin":
                if shutil.which("caffeinate"):
                    cmd = ["caffeinate", "-i", "-w", str(os.getpid())]
            elif shutil.which("systemd-inhibit"):
                # the inhibited command watches this process, so the lock goes away even if this one is killed
                cmd = ["systemd-inhibit", "--what=sleep:idle", "--who=tahoe", "--why=" + reason, "--mode=block",
                       "sh", "-c", f"while kill -0 {os.getpid()} 2>/dev/null; do sleep 15; done"]
            if cmd:
                p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
                time.sleep(0.5)
                if p.poll() is None:            # still running = the lock is held (it fails fast without a bus)
                    stop, how = (lambda: (p.terminate(), p.wait(5))), cmd[0]
    except Exception:  # noqa: BLE001
        stop = None
    if stop:
        log(f"Keeping the computer awake while {reason} runs ({how})")
    try:
        yield
    finally:
        if stop:
            try:
                stop()
            except Exception:  # noqa: BLE001
                pass


def _linux_disk_kind(dev, depth=0):
    """dev: a /sys/class/block or /sys/dev/block entry. Partitions -> their disk; dm-/md- devices -> slaves/."""
    dev = os.path.realpath(dev)
    if os.path.exists(os.path.join(dev, "partition")):
        dev = os.path.dirname(dev)
    if os.path.basename(dev).startswith("nvme"):
        return "ssd"
    slaves = os.path.join(dev, "slaves")
    under = sorted(os.listdir(slaves)) if os.path.isdir(slaves) and depth < 5 else []
    if under:
        kinds = {_linux_disk_kind(os.path.join(slaves, s), depth + 1) for s in under}
        return "hdd" if "hdd" in kinds else ("ssd" if kinds == {"ssd"} else None)
    with open(os.path.join(dev, "queue", "rotational"), encoding="utf-8") as fh:
        return {"0": "ssd", "1": "hdd"}.get(fh.read().strip())


def disk_kind(path):
    """'ssd', 'hdd' or None (unknown) for the drive holding `path`. Never raises; at most ~20 s. Only for hints:
    many cloud VMs report their SSDs as rotational."""
    try:
        if sys.platform == "win32":
            drive = os.path.splitdrive(os.path.abspath(path))[0]
            if len(drive) != 2 or drive[1] != ":":
                return None
            ps = (f"$n = (Get-Partition -DriveLetter {drive[0]} -ErrorAction Stop).DiskNumber; "
                  "$p = Get-PhysicalDisk | Where-Object { $_.DeviceId -eq \"$n\" }; "
                  "if (-not $p) { $p = Get-Disk -Number $n | Get-PhysicalDisk -ErrorAction SilentlyContinue }; "
                  "$p.MediaType")
            out = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
                                 capture_output=True, text=True, timeout=20).stdout
            kinds = {w.upper() for w in out.split()}
            if kinds & {"HDD", "3"}:
                return "hdd"
            return "ssd" if kinds and kinds <= {"SSD", "4", "SCM", "5"} else None
        if sys.platform == "darwin":
            mnt = os.path.abspath(path)
            while not os.path.ismount(mnt) and os.path.dirname(mnt) != mnt:
                mnt = os.path.dirname(mnt)
            out = subprocess.run(["diskutil", "info", mnt], capture_output=True, text=True, timeout=20).stdout
            m = re.search(r"Solid State:\s*(Yes|No)", out)
            return None if not m else ("ssd" if m.group(1) == "Yes" else "hdd")
        st = os.stat(path).st_dev
        return _linux_disk_kind(f"/sys/dev/block/{os.major(st)}:{os.minor(st)}")
    except Exception:  # noqa: BLE001
        return None


def py_cmd():
    """What a user types to run this Python: on Windows its path (PowerShell needs & "..." when the path has
    spaces); elsewhere 'python3' when that is this very interpreter (same folder, same file), else the full path."""
    exe = sys.executable or "python3"
    if sys.platform == "win32":
        return f'& "{exe}"' if " " in exe else exe
    p3 = shutil.which("python3")
    if p3 and os.path.realpath(p3) == os.path.realpath(exe) \
            and os.path.dirname(os.path.abspath(p3)) == os.path.dirname(os.path.abspath(exe)):
        return "python3"
    return shlex.quote(exe)


# ============================================================================= file discovery
REINDEX_HINT = " (if the download finished after an earlier run, add --reindex)"


def data_parquets(data_abs, out_dir):
    """Every parquet file under data_abs except the outputs of these scripts: out_dir and every folder below
    data_abs that holds a file_index.json (mtap_gankyrin/, gene_panel/, atlas/, trial folders)."""
    def norm(p):
        return os.path.normcase(os.path.abspath(p))

    skip = [norm(out_dir) + os.sep]
    for f in glob.glob(os.path.join(data_abs, "**", "file_index.json"), recursive=True):
        d = norm(os.path.dirname(f))
        if d != norm(data_abs):
            skip.append(d + os.sep)
    return [f for f in sorted(glob.glob(os.path.join(data_abs, "**", "*.parquet"), recursive=True))
            if not norm(f).startswith(tuple(skip))]


def discover(data_dir, out_dir, refresh=False):
    """Find every Tahoe table by its columns, not its file name. Cached in out_dir/file_index.json; indexed again
    when parquet files appeared or vanished since (e.g. the download finished after an earlier run)."""
    os.makedirs(out_dir, exist_ok=True)
    cache = os.path.join(out_dir, "file_index.json")
    data_abs = os.path.abspath(data_dir)
    files = data_parquets(data_abs, out_dir)
    if os.path.exists(cache) and not refresh:
        with open(cache, encoding="utf-8") as fh:
            idx = json.load(fh)
        if idx.get("data_dir") == data_abs and idx.get("expression") and idx.get("version") == INDEX_VERSION:
            known = {f for v in idx.values() if isinstance(v, list) for f in v}
            new, gone = len(set(files) - known), len(known - set(files))
            if not new and not gone:
                return idx
            log(f"{new} new and {gone} missing parquet files since the last index: indexing again")
    log("Indexing parquet files (one-time, reads only file footers) ...")
    idx = {"version": INDEX_VERSION, "data_dir": data_abs, "expression": [], "pseudobulk": [], "gene": [],
           "sample": [], "cell_line": [], "drug": [], "per_cell_metadata": [], "other": [], "unreadable": []}
    for f in files:
        try:
            names = set(pq.read_schema(f).names)
        except Exception as e:  # noqa: BLE001
            log(f"  skipping unreadable file {f}: {e}")
            idx["unreadable"].append(f)         # listed, so it does not trigger a new index on every run
            continue
        if {"genes", "expressions", "sample", "cell_line_id"} <= names:
            idx["expression"].append(f)
        elif {"gene_name", "log2FoldChange", "drug", "plate"} <= names:
            idx["pseudobulk"].append(f)
        elif {"token_id", "gene_symbol"} <= names:
            idx["gene"].append(f)
        elif "BARCODE_SUB_LIB_ID" in names:          # obs_metadata: one row per cell, not per sample
            idx["per_cell_metadata"].append(f)
        elif {"sample", "drugname_drugconc"} <= names:
            idx["sample"].append(f)
        elif {"Cell_ID_Cellosaur", "Organ"} <= names:
            idx["cell_line"].append(f)
        elif "drug" in names and "targets" in names:
            idx["drug"].append(f)
        else:
            idx["other"].append(f)
    with open(cache, "w", encoding="utf-8") as fh:
        json.dump(idx, fh, indent=1)
    log("  found: " + ", ".join(f"{k}={len(v)}" for k, v in idx.items() if isinstance(v, list)))
    return idx


def read_tables(files, columns=None):
    if not files:
        return None
    dfs = []
    for f in files:
        cols = None
        if columns is not None:
            have = set(pq.read_schema(f).names)
            cols = [c for c in columns if c in have]
        dfs.append(pq.read_table(f, columns=cols).to_pandas())
    return pd.concat(dfs, ignore_index=True)


def to_text(v):
    """Turn list-like / null metadata values into a plain string."""
    if v is None:
        return ""
    if isinstance(v, float) and math.isnan(v):
        return ""
    if isinstance(v, (list, tuple, np.ndarray)):
        return ", ".join(str(x) for x in v)
    return str(v)


# ============================================================================= extract
def build_columns(gene_meta, extra_genes):
    """Columns to extract per cell: target genes, then summed modules. Returns names, LUT, report."""
    gm = gene_meta.dropna(subset=["token_id", "gene_symbol"]).copy()
    gm["token_id"] = gm["token_id"].astype(np.int64)
    gm["gene_symbol"] = gm["gene_symbol"].astype(str)
    targets = []
    for g in TARGET_GENES + list(extra_genes):
        if g in targets:
            continue
        if (gm.gene_symbol == g).any():
            targets.append(g)
        else:
            log(f"  WARNING: gene {g} not found in gene metadata, skipped")
    target_set = set(targets)
    syms = set(gm.gene_symbol)
    modules = {
        "PROTEASOME": sorted(s for s in syms if PROTEASOME_RE.match(s) and s not in PROTEASOME_EXCLUDE
                             and s not in target_set),
        "S_PHASE": sorted(s for s in set(S_GENES) & syms if s not in target_set),
        "G2M_PHASE": sorted(s for s in set(G2M_GENES) & syms if s not in target_set),
    }
    cols = targets + [m for m in modules if modules[m]]
    lut = np.full(int(gm.token_id.max()) + 2, -1, dtype=np.int16)
    for k, name in enumerate(cols):
        members = [name] if name in target_set else modules[name]
        lut[gm.token_id[gm.gene_symbol.isin(members)].values] = k
    lut[0] = -1
    lut[-1] = -1  # sentinel for out-of-range tokens (np.take mode="clip")
    report = {"targets": targets, "modules": modules}
    return targets, cols, lut, report


_W = {}


def _init_worker(lut, cols, targets, batch_size):
    _W.update(lut=lut, cols=cols, targets=targets, batch=batch_size)
    try:
        pa.set_cpu_count(1)
    except Exception:  # noqa: BLE001
        pass


def _process_batch(batch):
    lut, cols = _W["lut"], _W["cols"]
    n = batch.num_rows

    def col(name):
        return batch.column(batch.schema.get_field_index(name))

    genes, expr = col("genes"), col("expressions")
    lens = pc.fill_null(pc.list_value_length(genes), 0).to_numpy(zero_copy_only=False).astype(np.int64)
    elens = pc.fill_null(pc.list_value_length(expr), 0).to_numpy(zero_copy_only=False).astype(np.int64)
    if not np.array_equal(lens, elens):
        raise ValueError("genes and expressions lists have different lengths")
    vals = np.asarray(genes.flatten().to_numpy(zero_copy_only=False)).astype(np.int64, copy=False)
    ex = np.array(expr.flatten().to_numpy(zero_copy_only=False), dtype=np.float32)  # writable copy
    offsets = np.zeros(n + 1, dtype=np.int64)
    np.cumsum(lens, out=offsets[1:])
    first = offsets[:-1][lens > 0]          # first entry of each row is a marker token: ignore it
    ex[first] = 0.0
    csum = np.zeros(ex.size + 1, dtype=np.float64)
    np.cumsum(ex, dtype=np.float64, out=csum[1:])
    total = (csum[offsets[1:]] - csum[offsets[:-1]]).astype(np.float32)
    idx = np.take(lut, vals, mode="clip")
    idx[first] = -1
    hit = np.flatnonzero(idx >= 0)
    k = len(cols)
    if hit.size:
        rows = np.searchsorted(offsets, hit, side="right") - 1
        acc = np.bincount(rows * k + idx[hit].astype(np.int64), weights=ex[hit], minlength=n * k)
        acc = acc.reshape(n, k).astype(np.float32)
    else:
        acc = np.zeros((n, k), dtype=np.float32)
    data = {
        "barcode": pc.cast(col("BARCODE_SUB_LIB_ID"), pa.string()),
        "sample": pc.cast(col("sample"), pa.string()),
        "plate": pc.cast(col("plate"), pa.string()),
        "drug": pc.cast(col("drug"), pa.string()),
        "cell_line_id": pc.cast(col("cell_line_id"), pa.string()),
        "n_genes": pa.array(np.maximum(lens - 1, 0).astype(np.int32)),
        "total_counts": pa.array(total),
    }
    for j, name in enumerate(cols):
        data[name] = pa.array(acc[:, j])
    return pa.table(data)


def _aggregate_part(path):
    cols, targets = _W["cols"], _W["targets"]
    df = pq.read_table(path, columns=["barcode", "sample", "plate", "drug", "cell_line_id", "n_genes",
                                      "total_counts"] + cols).to_pandas()
    for c in ["barcode", "sample", "plate", "drug", "cell_line_id"]:
        df[c] = df[c].astype(str)
    keys = [df["sample"], df["cell_line_id"]]
    agg = df.groupby(keys, sort=False)[["total_counts", "n_genes"] + cols].sum()
    agg.insert(0, "n_cells", df.groupby(keys, sort=False).size())
    det = (df[targets] > 0).groupby(keys, sort=False).sum()
    det.columns = ["det_" + c for c in targets]
    wl = agg.join(det)
    wl.index.names = ["sample", "cell_line_id"]
    wl = wl.reset_index()
    # barcode fields (e.g. 01_001_052-lib_1105): one of them identifies the sample well
    fields = df["barcode"].str.split("-", n=1).str[0].str.split("_", expand=True)
    bcs = []
    for i in range(min(3, fields.shape[1])):
        v = pd.to_numeric(fields[i], errors="coerce")
        t = pd.DataFrame({"sample": df["sample"].values, "field": i, "value": v.values}).dropna()
        if len(t):
            bcs.append(t.groupby(["sample", "field", "value"], sort=False).size().rename("n").reset_index())
    bcf = pd.concat(bcs, ignore_index=True) if bcs else pd.DataFrame(columns=["sample", "field", "value", "n"])
    smeta = df.groupby("sample", sort=False)[["plate", "drug"]].first().reset_index()
    return wl, bcf, smeta


def _extract_one(job):
    src, dst = job[:2]
    t0 = time.time()
    if not os.path.exists(dst):
        pf = pq.ParquetFile(src)
        pieces = [_process_batch(b) for b in
                  pf.iter_batches(batch_size=_W["batch"], columns=["genes", "expressions"] + META_COLS,
                                  use_threads=False)]
        pieces = [p for p in pieces if p.num_rows]
        if not pieces:
            return None, time.time() - t0, 0
        tbl = pa.concat_tables(pieces)
        tmp = dst + ".tmp"
        pq.write_table(tbl, tmp, compression="zstd")
        os.replace(tmp, dst)
    try:
        wl, bcf, smeta = _aggregate_part(dst)
    except Exception as e:  # noqa: BLE001  (damaged per-cell file: power loss, disk error): extract it again once
        if len(job) > 2:
            raise
        log(f"  {os.path.basename(dst)} is damaged ({type(e).__name__}): extracting that file again")
        os.remove(dst)
        return _extract_one((src, dst, "retry"))
    return (wl, bcf, smeta), time.time() - t0, int(wl["n_cells"].sum())


def _merge_parts(wls, bcfs, smetas):
    """Running reduction in extract: many files' partial tables -> one each. The sums are of whole counts, so the
    result is the same as summing everything at the end, while the main process stays small (~1 GB, not tens)."""
    keys = ["sample", "cell_line_id"]
    wl = pd.concat(wls, ignore_index=True).groupby(keys, sort=False).sum(numeric_only=True).reset_index()
    bcf = pd.concat(bcfs, ignore_index=True).groupby(["sample", "field", "value"], sort=False)["n"].sum().reset_index()
    smeta = pd.concat(smetas, ignore_index=True).drop_duplicates("sample")
    return [wl], [bcf], [smeta]


def mem_available_gb():
    """Free memory in GB on Linux, Windows or macOS (None if it cannot be read)."""
    try:
        import psutil
        return psutil.virtual_memory().available / 1e9
    except Exception:  # noqa: BLE001
        pass
    if sys.platform == "win32":
        try:
            import ctypes

            class MEMSTAT(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                            ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                            ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                            ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                            ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
            st = MEMSTAT()
            st.dwLength = ctypes.sizeof(MEMSTAT)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(st)):
                return st.ullAvailPhys / 1e9
        except Exception:  # noqa: BLE001
            return None
        return None
    try:
        with open("/proc/meminfo", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) / 1e6
    except OSError:
        pass
    try:                                                    # macOS and other Unix: total physical memory / 2
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2e9
    except (ValueError, OSError, AttributeError):
        return None


def auto_workers():
    cpus = os.cpu_count() or 2
    mem_gb = mem_available_gb()
    w = max(1, cpus - 1)
    if mem_gb:
        w = min(w, max(1, int(mem_gb / 3)))  # ~3 GB per worker is generous
    return min(w, 48)


def parse_conc(s):
    """"[('8-Hydroxyquinoline',0.05,'uM')]" -> (0.05, 'uM')"""
    if s is None or (isinstance(s, float) and math.isnan(s)):
        return np.nan, ""
    m = re.search(r",\s*([-+0-9.eE]+)\s*,\s*['\"]([^'\"]*)['\"]", str(s))
    if m:
        try:
            return float(m.group(1)), m.group(2)
        except ValueError:
            pass
    return np.nan, ""


def well_name(slot):
    if slot is None or not np.isfinite(slot):
        return ""
    s = int(slot)
    if 1 <= s <= 96:
        return f"{ROWS[(s - 1) // 12]}{(s - 1) % 12 + 1}"
    return f"slot{s}"


def slot_from_well(w):
    m = re.match(r"^\s*([A-Ha-h])\s*0*([0-9]{1,2})\s*$", str(w))
    if not m:
        return np.nan
    r, c = ROWS.index(m.group(1).upper()), int(m.group(2))
    return r * 12 + c if 1 <= c <= 12 else np.nan


def build_sample_map(smeta, bcf, wl, idx, layout_file):
    sm = smeta.drop_duplicates("sample").set_index("sample")
    sm["n_cells"] = wl.groupby("sample")["n_cells"].sum()
    sm["is_dmso"] = sm["drug"].str.upper().str.startswith(DMSO_PREFIX)
    sm["plate_num"] = sm["plate"].str.extract(r"(\d+)", expand=False)
    # dose from sample metadata
    smd = read_tables(idx["sample"])
    sm["conc"], sm["unit"] = np.nan, ""
    if smd is not None and "drugname_drugconc" in smd:
        smd = smd.drop_duplicates("sample").set_index("sample")
        cu = smd["drugname_drugconc"].map(parse_conc)
        sm["conc"] = cu.map(lambda t: t[0]).reindex(sm.index)
        sm["unit"] = cu.map(lambda t: t[1]).reindex(sm.index).fillna("")
        for c in ["mean_gene_count", "mean_tscp_count", "mean_pcnt_mito"]:
            if c in smd:
                sm[c] = smd[c].reindex(sm.index)
    else:
        log("  WARNING: sample metadata not found; doses unknown (plates will be used as dose labels)")
    sm.loc[sm.is_dmso, "conc"] = 0.0
    # well position
    checks = []
    if layout_file:
        lay = pd.read_csv(layout_file)
        lay.columns = [c.strip().lower() for c in lay.columns]
        if "slot" not in lay:
            lay["slot"] = lay["well"].map(slot_from_well)
        sm["slot"] = lay.drop_duplicates("sample").set_index("sample")["slot"].reindex(sm.index)
        sm["slot_purity"] = 1.0
        source = f"layout file {layout_file}"
    else:
        bc = bcf.groupby(["sample", "field", "value"])["n"].sum().reset_index()
        best = None
        for f, g in bc.groupby("field"):
            tot = g.groupby("sample")["n"].sum()
            top = g.sort_values("n", ascending=False).drop_duplicates("sample").set_index("sample")
            purity = (top["n"] / tot.reindex(top.index)).reindex(sm.index)
            slot = top["value"].reindex(sm.index)
            dup = (pd.DataFrame({"plate": sm["plate"], "slot": slot}).dropna()
                   .duplicated(["plate", "slot"]).sum())
            checks.append({"barcode_field": int(f) + 1, "median_purity": float(purity.median()),
                           "min_purity": float(purity.min()), "distinct_values": int(slot.nunique()),
                           "max_value": float(slot.max()), "duplicate_positions_within_plate": int(dup)})
            score = float(purity.median()) - 0.01 * dup
            if best is None or score > best[0]:
                best = (score, int(f), slot, purity)
        if best is None:
            sm["slot"], sm["slot_purity"] = np.nan, np.nan
            source = "none (barcodes could not be parsed)"
        else:
            _, f, slot, purity = best
            if slot.min() == 0:
                slot = slot + 1
            sm["slot"], sm["slot_purity"] = slot, purity
            source = f"barcode field {f + 1} (Parse round-1 well; numbered row-major A1=1 ... H12=96)"
            if purity.median() < 0.9:
                log("  WARNING: no barcode field identifies the sample well cleanly; consider --layout")
    sm["well"] = sm["slot"].map(well_name)
    return sm.reset_index(), source, pd.DataFrame(checks)


def cmd_extract(args):
    out = args.out
    idx = discover(args.data, out, refresh=args.reindex)
    exprs = idx["expression"]
    if not exprs:
        sys.exit("No expression parquet files found under " + os.path.abspath(args.data) + REINDEX_HINT)
    if args.limit_files:
        exprs = exprs[:args.limit_files]
    gene_meta = read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    if gene_meta is None:
        sys.exit("Gene metadata (token_id -> gene_symbol) not found" + REINDEX_HINT)
    targets, cols, lut, report = build_columns(gene_meta, args.extra_genes)
    log(f"Extracting per cell: {', '.join(targets)} + modules "
        + ", ".join(f"{m} ({len(v)} genes)" for m, v in report["modules"].items() if v))
    with open(os.path.join(out, "extracted_columns.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1)
    cells_dir = os.path.join(out, "cells")
    os.makedirs(cells_dir, exist_ok=True)
    root = os.path.abspath(args.data)
    jobs = []
    for src in exprs:
        rel = os.path.relpath(os.path.abspath(src), root)
        jobs.append((src, os.path.join(cells_dir, re.sub(r"[^\w.-]+", "__", rel))))
    done_before = sum(os.path.exists(d) for _, d in jobs)
    workers = args.workers or auto_workers()
    log(f"{len(jobs)} expression files ({done_before} already done), {workers} workers")
    wls, bcfs, smetas = [], [], []
    n_cells, t0, last, merges = 0, time.time(), 0.0, 0
    ctx = mp.get_context("spawn")
    with ctx.Pool(workers, initializer=_init_worker, initargs=(lut, cols, targets, args.batch_size)) as pool:
        for i, (res, _dt, nc) in enumerate(pool.imap_unordered(_extract_one, jobs, chunksize=1), 1):
            if res is not None:
                wls.append(res[0])
                bcfs.append(res[1])
                smetas.append(res[2])
                if len(wls) >= REDUCE_EVERY:
                    wls, bcfs, smetas = _merge_parts(wls, bcfs, smetas)
                    merges += 1
            n_cells += nc
            now = time.time()
            if now - last > 60 or i == len(jobs):
                rate = i / max(now - t0, 1e-9)
                eta = (len(jobs) - i) / rate if rate > 0 else 0
                log(f"  {i}/{len(jobs)} files, {n_cells:,} cells, ETA {eta / 60:.0f} min")
                last = now
    log("Combining ..." + (f" (partial tables already merged {merges} times on the way)" if merges else ""))
    keys = ["sample", "cell_line_id"]
    wl = pd.concat(wls, ignore_index=True).groupby(keys, sort=True).sum(numeric_only=True).reset_index()
    bcf = pd.concat(bcfs, ignore_index=True)
    smeta = pd.concat(smetas, ignore_index=True)
    sm, source, checks = build_sample_map(smeta, bcf, wl, idx, args.layout)
    wl.to_parquet(os.path.join(out, "well_line.parquet"), index=False)
    wl.to_csv(os.path.join(out, "well_line.csv"), index=False)
    sm.to_csv(os.path.join(out, "sample_map.csv"), index=False)
    checks.to_csv(os.path.join(out, "well_position_check.csv"), index=False)
    with open(os.path.join(out, "extract_info.json"), "w", encoding="utf-8") as fh:
        json.dump({"well_position_source": source, "targets": targets, "columns": cols,
                   "n_files": len(jobs), "n_cells": int(wl["n_cells"].sum()),
                   "limit_files": args.limit_files}, fh, indent=1)
    dup = sm.dropna(subset=["slot"]).duplicated(["plate", "slot"]).sum()
    log(f"Done: {int(wl['n_cells'].sum()):,} cells, {sm['sample'].nunique()} wells, "
        f"{wl['cell_line_id'].nunique()} cell lines, {sm['plate'].nunique()} plates")
    log(f"Well position from {source}; median purity {sm['slot_purity'].median():.3f}, "
        f"duplicate positions within a plate: {dup}")


# ============================================================================= analysis helpers
def norm_sf(z):
    z = np.asarray(z, dtype=float)
    out = np.full(z.shape, np.nan)
    ok = np.isfinite(z)
    out[ok] = [0.5 * math.erfc(v / math.sqrt(2.0)) for v in z[ok]]
    return out


def bh(p):
    p = np.asarray(p, dtype=float)
    out = np.full(p.shape, np.nan)
    ok = np.isfinite(p)
    n = int(ok.sum())
    if n == 0:
        return out
    ps = p[ok]
    order = np.argsort(ps)
    ranked = ps[order] * n / np.arange(1, n + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    tmp = np.empty(n)
    tmp[order] = np.minimum(ranked, 1.0)
    out[ok] = tmp
    return out


def robust_center_scale(v):
    v = np.asarray(v, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return 0.0, 1.0
    c = float(np.median(v))
    s = 1.4826 * float(np.median(np.abs(v - c)))
    if not s > 0:
        s = float(np.std(v)) or 1.0
    return c, s


def loo_slot(values, slot, drug, use):
    """Leave-drug-out position effect: for each well, the median value of wells in the same position
    (on any plate) that hold a DIFFERENT drug. Returns effect and number of wells used."""
    v = np.asarray(values, dtype=float)
    slot = np.asarray(slot, dtype=float)
    drug = np.asarray(drug, dtype=object)
    use = np.asarray(use, dtype=bool) & np.isfinite(v)
    eff = np.zeros(v.size)
    n_used = np.zeros(v.size, dtype=int)
    groups = defaultdict(list)
    for i, s in enumerate(slot):
        if np.isfinite(s):
            groups[s].append(i)
    for ii in groups.values():
        ii = np.asarray(ii)
        for i in ii:
            m = ii[use[ii] & (drug[ii] != drug[i])]
            n_used[i] = m.size
            if m.size >= MIN_SLOT_WELLS:
                eff[i] = float(np.median(v[m]))
    return eff, n_used


def loo_slot_clean(values, slot, drug, use, clean):
    """Second pass of the leave-drug-out position effect (method v3): for each well, the median of the wells in the
    same position (any plate) that hold a DIFFERENT drug and are clean for this gene (clean: first-pass |z| <
    POS_CLEAN_Z), so a strong drug sharing the position cannot pass its own effect on as a 'position effect'.
    >= MIN_SLOT_WELLS clean donors: their median. Fewer, but >= MIN_SLOT_WELLS donors in total: 0, state 1
    ('position correction uncertain'). < MIN_SLOT_WELLS donors in total: 0, state 2 ('position not correctable').
    Donors in total count every other-drug `use` well at the position (as tahoe_atlas.py: per well, whatever their
    values); clean donors need a value. Returns effect, donors in total, clean donors, state."""
    v = np.asarray(values, dtype=float)
    slot = np.asarray(slot, dtype=float)
    drug = np.asarray(drug, dtype=object)
    usew = np.asarray(use, dtype=bool)
    ok = usew & np.isfinite(v) & np.asarray(clean, dtype=bool)
    eff = np.zeros(v.size)
    n_tot = np.zeros(v.size, dtype=int)
    n_cl = np.zeros(v.size, dtype=int)
    state = np.full(v.size, 2, dtype=int)                  # wells without a known position: not correctable
    groups = defaultdict(list)
    for i, s in enumerate(slot):
        if np.isfinite(s):
            groups[s].append(i)
    for ii in groups.values():
        ii = np.asarray(ii)
        for i in ii:
            other = drug[ii] != drug[i]
            n_tot[i] = int((usew[ii] & other).sum())
            m = ii[ok[ii] & other]
            n_cl[i] = m.size
            if m.size >= MIN_SLOT_WELLS:
                eff[i], state[i] = float(np.median(v[m])), 0
            else:
                state[i] = 1 if n_tot[i] >= MIN_SLOT_WELLS else 2
    return eff, n_tot, n_cl, state


def plate_line_residual(d, col):
    """value minus the median over drug wells on the same plate, same cell line"""
    ref = d.loc[~d["is_dmso"]].groupby(["plate", "cell_line_id"])[col].median()
    key = pd.MultiIndex.from_arrays([d["plate"], d["cell_line_id"]])
    return d[col].values - ref.reindex(key).values


def unreliable_plates(sm, spec=None):
    """Plates whose wells are computed (the per-well tables keep them) but left out of the reference spread, the
    plate-factor peers and every drug-dose that also has a well on another plate. spec: --unreliable-plates
    ('plate13,plate5', any case; plate numbers also work; 'none' or 'no'); default (no option, or an empty one):
    UNRELIABLE_PLATES that are in the data. The one definition: tahoe_atlas.py calls this too."""
    plates = sorted(set(sm["plate"].astype(str)), key=lambda p: (len(p), p))
    txt = "" if spec is None else str(spec).strip()
    if txt.lower() in ("none", "no"):
        return []
    want = [x.strip() for x in txt.split(",") if x.strip()] if txt else list(UNRELIABLE_PLATES)
    num = {re.sub(r"\D", "", p): p for p in plates}
    out = []
    for w in want:
        hit = next((p for p in plates if p.lower() == w.lower()), None) or \
            (num.get(w) if w.isdigit() else None)
        if hit:
            out.append(hit)
        elif txt:
            log(f"  WARNING: --unreliable-plates: no plate called {w} (plates: {', '.join(plates)})")
    return sorted(set(out), key=lambda p: (len(p), p))


def mark_unreliable(sm, plates):
    sm = sm.copy()
    sm["unreliable_plate"] = sm["plate"].astype(str).isin(set(plates))
    return sm


def wells_of(sm):
    """One row per well (index: sample) with the columns every per-well table carries (WELL_COLS)."""
    w = sm.set_index("sample")
    if "unreliable_plate" not in w:
        w = w.assign(unreliable_plate=False)
    w = w[WELL_COLS].copy()
    w["unreliable_plate"] = w["unreliable_plate"].fillna(False).astype(bool)
    return w


def reference_wells(W):
    """Drug wells on reliable plates: the reference for robust centres / scales (all drug wells when every plate
    is marked unreliable)."""
    drug = ~W["is_dmso"].astype(bool)
    rel = drug & ~W["unreliable_plate"].astype(bool) if "unreliable_plate" in W else drug
    return rel if rel.any() else drug


def used_wells(Wd):
    """The drug wells that enter their drug-dose (Wd: drug wells with a 'dose' column): the wells on reliable
    plates, or every well when the drug-dose has none there ('unreliable plate only')."""
    if "unreliable_plate" not in Wd:
        return pd.Series(True, index=Wd.index)
    unrel = Wd["unreliable_plate"].astype(bool)
    has_rel = (~unrel).groupby([Wd["drug"], Wd["dose"]]).transform("any")
    return ~unrel | ~has_rel


def dose_text(v):
    """A dose as dose_key writes it ('0.05', '5'); other labels unchanged."""
    try:
        return f"{float(v):.6g}"
    except (TypeError, ValueError):
        return str(v)


def plate_groups(W):
    """Plate dispersion group of every well (index of W) as 'plate|dose': (plate, dose) groups with fewer than
    PLATE_SCALE_MIN_WELLS drug wells (a lone control well of another dose, the DMSO wells) join their plate's largest
    group. Plate 13 of the real data (all three doses) gives three groups."""
    dose = dose_key(W)
    drug = ~W["is_dmso"].astype(bool)
    n = pd.Series(1, index=W.index)[drug].groupby([W["plate"][drug], dose[drug]]).sum()
    largest = {}
    for (p, d_), k in n.items():
        if p not in largest or k > n[(p, largest[p])]:
            largest[p] = d_
    out = [f"{p}|{d_}" if n.get((p, d_), 0) >= PLATE_SCALE_MIN_WELLS or p not in largest else f"{p}|{largest[p]}"
           for p, d_ in zip(W["plate"], dose)]
    return pd.Series(out, index=W.index)


def spread_ratios(mads, info):
    """Per group and feature (mads: groups x features, each feature's 1.4826 x median |W2 - c| over the group's drug
    wells; info: per group plate, dose, reliable): the group's spread over the median spread of the same dose on the
    OTHER reliable plates (its peers). NaN without peers. Returns (ratios, number of peers per group)."""
    R = pd.DataFrame(np.nan, index=mads.index, columns=mads.columns)
    npeer = {}
    for G in mads.index:
        p, d_ = info.at[G, "plate"], info.at[G, "dose"]
        peers = [P for P in mads.index if info.at[P, "dose"] == d_ and info.at[P, "plate"] != p
                 and bool(info.at[P, "reliable"])]
        npeer[G] = len(peers)
        if peers:
            ref = mads.loc[peers].median(axis=0)
            R.loc[G] = (mads.loc[G] / ref.where(ref > 0)).to_numpy(dtype=float)
    return R, npeer


def fit_plate_factors(mads, info):
    """Plate factors (method v3) from mads and info (see spread_ratios): factor_raw = median spread ratio over the
    features; factor = max(1, factor_raw): a noisy group is widened, a quiet one never narrowed (part of a noisy
    plate's spread may be real activity); no peers -> 1. A feature's own z uses feature_factors on top."""
    R, npeer = spread_ratios(mads, info)
    rows = []
    for G in mads.index:
        ratio = R.loc[G].to_numpy(dtype=float)
        fr = float(np.nanmedian(ratio)) if np.isfinite(ratio).any() else np.nan
        rows.append({"group": G, "n_peers": npeer[G], "n_features": int(mads.loc[G].notna().sum()),
                     "factor_raw": fr, "factor": max(1.0, fr) if np.isfinite(fr) else 1.0})
    return pd.DataFrame(rows).set_index("group")


def feature_factors(group_factor, ratio):
    """The z divisor of one feature per group: the group's factor, raised to the feature's own spread ratio /
    PLATE_SCALE_BAND where that is larger (a gene over-dispersed on a plate beyond the group's median gene; only
    ever widens). group_factor, ratio: aligned arrays (ratio NaN: the group's factor)."""
    f = np.asarray(group_factor, dtype=float)
    r = np.asarray(ratio, dtype=float) / PLATE_SCALE_BAND
    return np.where(np.isfinite(r), np.maximum(f, r), f)


def cells_beyond_row(cells, row):
    """A well's cell loss that its plate row does not explain (log2 vs the plate): where the row's other drug wells
    are themselves shifted (|row| > ROW_SHIFT), the smaller loss of the two readings (vs the plate, vs the row);
    otherwise the plain value (a row of toxic neighbours at a high dose is no reason to subtract their loss). NaN
    row: the plain value. 'toxic' needs this < -1 in the drug-dose's best used well."""
    c = np.asarray(cells, dtype=float)
    r = np.nan_to_num(np.asarray(row, dtype=float))
    return np.where(np.abs(r) > ROW_SHIFT, np.maximum(c, c - r), c)


POSITION_PAIR_TYPES = ("same position, other plate", "different position")


def replicate_summary(pairs, active=None):
    """Replicate agreement per pair type with every drug-dose counted ONCE (its mean r over its well pairs of that
    type), so a drug-dose with many wells cannot dominate. pairs: one row per well pair with drug, dose (or conc),
    pair_type, r and optionally position_not_correctable (either well had no position correction: such pairs stay out
    of the two position types and are reported as their own row 'position not correctable (either well)').
    active: set of (drug, dose text) for a second median over the active drug-doses. One row per type: n_pairs,
    n_drug_doses, n_drugs, median_r, drugs (named when <= 5), n_active, median_r_active."""
    cols = ["pair_type", "n_pairs", "n_drug_doses", "n_drugs", "median_r", "drugs", "n_active", "median_r_active"]
    if pairs is None or not len(pairs):
        return pd.DataFrame(columns=cols)
    p = pairs.copy()
    p["dose_"] = (p["dose"] if "dose" in p else p["conc"]).map(dose_text)
    if "position_not_correctable" in p:
        nc = p["position_not_correctable"].fillna(False).astype(bool) & p["pair_type"].isin(POSITION_PAIR_TYPES)
        p.loc[nc, "pair_type"] = "position not correctable (either well)"
    d = p.groupby(["pair_type", "drug", "dose_"]).agg(r=("r", "mean"), n=("r", "size")).reset_index()
    rows = []
    for t, g in d.groupby("pair_type", sort=False):
        drugs = sorted(set(g["drug"]))
        act = g[[(a, b) in active for a, b in zip(g["drug"], g["dose_"])]] if active is not None else g.iloc[:0]
        rows.append({"pair_type": t, "n_pairs": int(g["n"].sum()), "n_drug_doses": len(g), "n_drugs": len(drugs),
                     "median_r": float(g["r"].median()), "drugs": ", ".join(drugs) if len(drugs) <= 5 else "",
                     "n_active": len(act), "median_r_active": float(act["r"].median()) if len(act) else np.nan})
    order = {t: i for i, t in enumerate(("same position, other plate", "different position", "same plate",
                                         "unreliable plate", "position not correctable (either well)"))}
    return pd.DataFrame(rows, columns=cols).sort_values("pair_type", key=lambda s: s.map(order).fillna(9))


def replicate_text(tab, active_label="active"):
    """'different position: median r 0.58 over 10 drug-doses of 4 drugs (Afatinib, ...)' per row of
    replicate_summary."""
    out = []
    for r in tab.itertuples():
        x = (f"{r.pair_type}: median r {r.median_r:.2f} over {r.n_drug_doses} drug-dose"
             f"{'s' if r.n_drug_doses != 1 else ''} of {r.n_drugs} drug{'s' if r.n_drugs != 1 else ''}"
             + (f" ({r.drugs})" if r.drugs else "") + f", {r.n_pairs} well pair{'s' if r.n_pairs != 1 else ''}")
        if r.n_active and np.isfinite(r.median_r_active):
            x += f"; {active_label} drug-doses {r.median_r_active:.2f} ({r.n_active})"
        out.append(x)
    return "; ".join(out)


def salt_base(name):
    """A drug name without its trailing salt / form in brackets ('Topotecan (hydrochloride)' -> 'Topotecan';
    one level of nested brackets, '(R)-Verapamil (hydrochloride)' -> '(R)-Verapamil'): the drugs listed twice as
    salt forms share it."""
    return re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)\s*$", "", str(name)).strip()


class Method:
    """The drug-effect method (v3) on one set of wells: what every gene, module and score of one analysis shares -
    the unreliable plates (sm column unreliable_plate), the composition shift per (well, line) (optional: the
    atlas's composition_shift.parquet), the plate dispersion groups and factors (imported from the atlas's
    plate_scale.csv, or fitted over the features added here), the drug-dose columns imported from the atlas
    ('wells disagree'), and each feature's two position passes (cached).
    Use: add(wl, gene, excluded_lines) for every feature, complete(fit_on), then expression_effects(..., method=M)
    and well_context(..., method=M); a feature not added before is computed on demand with the factors fitted so
    far (or, when nothing was fitted, with factors fitted on that feature alone)."""

    def __init__(self, sm, shift=None, plate_scale=None, dd_extra=None):
        self.sm = sm
        self.W = wells_of(sm)
        self.group = plate_groups(self.W)
        self.shift = None
        if shift is not None and len(shift):
            s = shift.assign(sample=shift["sample"].astype(str), cell_line_id=shift["cell_line_id"].astype(str))
            s = s.drop_duplicates(["sample", "cell_line_id"]).set_index(["sample", "cell_line_id"])["shift_log2"]
            self.shift = s.astype(float)
        self.dd_extra = dd_extra
        self.factors = {1: None, 2: None}        # dict group -> factor, per pass
        self.factor_table = None
        self.factor_source = ""
        self.cache = {}                          # (feature, excluded lines) -> well-level passes
        self.pending = []                        # added, second pass not yet done
        self.feature_table = {}                  # feature -> per group: its spread ratio and z divisor (finish)
        if plate_scale is not None and len(plate_scale):
            try:
                self._import_factors(plate_scale)
            except (KeyError, ValueError, TypeError) as e:     # an unexpected table: fit our own, say so
                log(f"  WARNING: the atlas's plate_scale.csv could not be used ({e!r}): plate factors fitted here")
                self.factors, self.factor_table, self.factor_source = {1: None, 2: None}, None, ""

    # ---- plate factors
    def group_info(self):
        g = pd.DataFrame({"group": self.group, "plate": self.W["plate"].astype(str),
                          "unreliable": self.W["unreliable_plate"], "drug": ~self.W["is_dmso"]})
        info = g.groupby("group").agg(plate=("plate", "first"), n_wells=("drug", "sum"),
                                      unreliable=("unreliable", "all"))
        info["dose"] = [x.split("|", 1)[1] for x in info.index]
        info["reliable"] = ~info["unreliable"]
        return info[["plate", "dose", "n_wells", "reliable"]]

    def _import_factors(self, ps):
        ps = ps.copy()
        if not {"plate", "dose"} <= set(ps.columns) and "group" in ps:
            sp = ps["group"].astype(str).str.split("|", n=1, expand=True)
            ps["plate"], ps["dose"] = sp[0], sp[1]
        if not {"plate", "dose", "factor"} <= set(ps.columns):
            raise KeyError("plate_scale.csv needs the columns plate, dose and factor")
        ps["plate"] = ps["plate"].astype(str)
        ps["dose"] = ps["dose"].map(dose_text)
        key = {f"{p}|{d_}": r for p, d_, r in zip(ps["plate"], ps["dose"], ps.to_dict("records"))}
        big = ps.sort_values("n_wells", ascending=False) if "n_wells" in ps else ps
        bigk = {}                                # a group the atlas does not list: its plate's largest group
        for p, r in zip(big["plate"], big.to_dict("records")):
            bigk.setdefault(p, r)
        info = self.group_info()
        f1, f2 = {}, {}
        for G in info.index:
            r = key.get(G) or bigk.get(info.at[G, "plate"])
            v = float(r.get("factor", np.nan)) if r is not None else np.nan
            f2[G] = v if np.isfinite(v) and v > 0 else 1.0
            v1 = float(r.get("factor_pass1", np.nan)) if r is not None else np.nan
            f1[G] = v1 if np.isfinite(v1) and v1 > 0 else f2[G]
        self.factors = {1: f1, 2: f2}
        t = info.copy()
        t["factor"] = pd.Series(f2)
        t["factor_raw"] = [float(key[G].get("factor_raw", np.nan)) if G in key else np.nan for G in t.index]
        self.factor_table = t
        self.factor_source = "imported from the atlas (plate_scale.csv)"

    def well_factor(self, k, index):
        f = self.factors.get(k) or {}
        return pd.Series([f.get(g, 1.0) for g in self.group.reindex(index)], index=index, dtype=float)

    def factor_for(self, values, center, feature=None):
        """Per well (index of values): the z divisor of one feature (a gene, module, score or contrast; method v3):
        its plate group's factor (pass 2, imported or fitted), raised where the feature's own spread ratio on that
        group (from these values, the same wells and peers as the factors) exceeds it x PLATE_SCALE_BAND
        (feature_factors). With `feature`, the per-group table is kept for plate_scale_by_gene.csv."""
        info = self.group_info()
        v = pd.Series(values, dtype=float)
        dw = ~self.W["is_dmso"].reindex(v.index).fillna(True).astype(bool) & np.isfinite(v)
        dev = (v[dw] - center).abs()
        mad = 1.4826 * dev.groupby(self.group.reindex(dev.index)).median()
        R, _ = spread_ratios(pd.DataFrame({0: mad}).reindex(info.index), info)
        f2 = self.factors.get(2) or {}
        fg = pd.Series([f2.get(G, 1.0) for G in info.index], index=info.index, dtype=float)
        ff = pd.Series(feature_factors(fg, R[0]), index=info.index)
        if feature is not None:
            self.feature_table[feature] = pd.DataFrame({"plate": info["plate"], "dose": info["dose"],
                                                        "n_wells": info["n_wells"], "spread_ratio": R[0],
                                                        "group_factor": fg, "factor": ff})
        return pd.Series(ff.reindex(self.group.reindex(v.index)).fillna(1.0).to_numpy(), index=v.index)

    def _fit(self, k, cores, col, ccol):
        info = self.group_info()
        mads = {}
        for i, core in enumerate(cores):
            W = core["W"]
            dw = ~W["is_dmso"] & np.isfinite(W[col])
            v = (W.loc[dw, col] - core[ccol]).abs()
            mads[i] = 1.4826 * v.groupby(self.group.reindex(v.index)).median()
        M = pd.DataFrame(mads).reindex(info.index)
        t = fit_plate_factors(M, info)
        self.factors[k] = t["factor"].to_dict()
        if k == 2:
            self.factor_table = info.join(t)
            self.factor_table["factor_pass1"] = pd.Series(self.factors[1])

    # ---- the passes
    def shift_of(self, d):
        if self.shift is None:
            return np.zeros(len(d))
        key = pd.MultiIndex.from_arrays([d["sample"].astype(str), d["cell_line_id"].astype(str)])
        return self.shift.reindex(key).fillna(0.0).to_numpy(dtype=float)

    def well_shift(self):
        """Per well: median composition shift over its lines (NaN without a shift table)."""
        if self.shift is None:
            return pd.Series(np.nan, index=self.W.index)
        s = self.shift.groupby(level=0).median()
        return s.reindex(self.W.index)

    def profiles(self, wl, gene, exclude_lines):
        """Per (well, line) profile of one gene or module: log2 CPM y; r1 = y minus the plate x line median of the
        plate's drug wells; r1c = r1 minus the profile's composition shift (0 without the atlas's table)."""
        keep = ["sample", "cell_line_id", "n_cells", "total_counts", gene]
        if f"det_{gene}" in wl:
            keep.append(f"det_{gene}")
        d = wl.loc[(wl["n_cells"] >= MIN_CELLS) & ~wl["cell_line_id"].isin(exclude_lines), keep]
        d = d.merge(self.sm[["sample", "plate", "drug", "slot", "is_dmso"]], on="sample").reset_index(drop=True)
        d["y"] = np.log2((d[gene] + 0.5) / (d["total_counts"] + 1.0) * 1e6)
        d["r1"] = plate_line_residual(d, "y")
        d["r1c"] = d["r1"] - self.shift_of(d)
        return d

    def _pass1(self, W1):
        W = self.W.reindex(W1.index).copy()
        W["W1"] = W1.to_numpy(dtype=float)
        eff, _n = loo_slot(W["W1"].values, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
        W["position_effect_pass1"] = eff
        W["W2a"] = W["W1"] - eff
        c, s = robust_center_scale(W.loc[reference_wells(W), "W2a"])
        return {"W": W, "c1": c, "s1": s}

    def _pass2(self, core):
        W = core["W"]
        za = (W["W2a"] - core["c1"]) / (core["s1"] * self.well_factor(1, W.index))
        eff, n_tot, n_cl, state = loo_slot_clean(W["W1"].values, W["slot"].values, W["drug"].values,
                                                 ~W["is_dmso"].values, (za.abs() < POS_CLEAN_Z).to_numpy())
        W["slot_effect"], W["slot_n"], W["slot_clean_n"], W["pos_state"] = eff, n_tot, n_cl, state
        W["W2"] = W["W1"] - W["slot_effect"]
        core["c"], core["s"] = robust_center_scale(W.loc[reference_wells(W), "W2"])
        core["done"] = True

    def add(self, wl, gene, exclude_lines, min_lines=None):
        """First pass of one feature (cached; the second pass needs the first-pass plate factors: complete()).
        min_lines: measured lines a well needs (default MIN_LINES, as tahoe_atlas.py, or 1 for a gene measured in
        fewer lines in a typical well (the median over wells): CASP5 of the real data, 6 expressing lines of which
        2 are usable in few wells, keeps its 4 colorectal lines in nearly every well; 1 for effects within a chosen
        subset of lines, e.g. the lines that lost a gene)."""
        k = (gene, frozenset(exclude_lines), min_lines)
        if k not in self.cache:
            d = self.profiles(wl, gene, exclude_lines)
            g = d.groupby("sample")["r1c"]
            W1 = g.median()
            n = g.count()                                  # lines measured per well; a gene measured in a typical
            need = min_lines or (MIN_LINES if len(n) and n.median() >= MIN_LINES else 1)   # well in fewer: 1
            W1[n < need] = np.nan                          # too few lines measured in the well
            self.cache[k] = self._pass1(W1)
            self.cache[k]["feature"] = gene if min_lines is None else None   # None: a subset (plate_scale_by_gene)
            self.pending.append(k)
        return k

    def complete(self, fit_on=None):
        """Plate factors of the first pass (unless imported or fitted before), the clean-donor second pass of every
        pending feature, then the final plate factors over the features in fit_on (default: all pending)."""
        todo, self.pending = self.pending, []
        fit = [self.cache[k] for k in todo if fit_on is None or k[0] in set(fit_on)] or [self.cache[k] for k in todo]
        own = self.factors[2] is None
        if own and fit:
            self._fit(1, fit, "W2a", "c1")
        for k in todo:
            self._pass2(self.cache[k])
        if own and fit:
            self._fit(2, fit, "W2", "c")
            n = len(fit)
            self.factor_source = f"fitted over {n} gene{'s' if n != 1 else ''} / modules of this analysis"

    def core(self, wl, gene, exclude_lines, min_lines=None):
        k = self.add(wl, gene, exclude_lines, min_lines)
        if not self.cache[k].get("done"):
            self.complete()
        return self.cache[k]

    def finish(self, core):
        """The well-level table of one feature: W1, both position passes, W2 and z = (W2 - c) / (s x the feature's
        plate factor). plate_scale = its group's factor, plate_scale_gene = the divisor used (factor_for)."""
        W = core["W"].copy()
        W["plate_scale"] = self.well_factor(2, W.index)
        W["plate_scale_gene"] = self.factor_for(W["W2"], core["c"], core.get("feature"))
        W["z"] = (W["W2"] - core["c"]) / (core["s"] * W["plate_scale_gene"])
        t = self.feature_table.get(core.get("feature"))
        if t is not None:                          # calibration per group: group factor only vs the divisor used
            dw = ~W["is_dmso"].astype(bool) & W["z"].notna()
            grp = self.group.reindex(W.index)[dw]
            t["pct_drug_wells_abs_z_gt_1.96_group_factor"] = 100 * (
                (W["z"] * W["plate_scale_gene"] / W["plate_scale"])[dw].abs() > 1.96).groupby(grp).mean()
            t["pct_drug_wells_abs_z_gt_1.96"] = 100 * (W.loc[dw, "z"].abs() > 1.96).groupby(grp).mean()
        W["position_correction_uncertain"] = (W["pos_state"] == 1) & W["W1"].notna()
        W["position_not_correctable"] = W["pos_state"] == 2
        return W

    def well_pass(self, W1):
        """Both passes and z for a per-well series with the factors fitted so far (not cached), e.g. the
        single-cell detail columns. Returns the finished well table and (c, s)."""
        core = self._pass1(W1)
        if self.factors[2] is None:
            self._fit(1, [core], "W2a", "c1")
            self._pass2(core)
            self._fit(2, [core], "W2", "c")
            self.factor_source = "fitted on a single feature"
        else:
            self._pass2(core)
        return self.finish(core), (core["c"], core["s"])

    def not_correctable(self):
        """Per well: fewer than MIN_SLOT_WELLS other-drug wells at its position (on any plate): no correction."""
        W = self.W
        _e, _n, _c, state = loo_slot_clean(np.zeros(len(W)), W["slot"].values, W["drug"].values,
                                           ~W["is_dmso"].values, np.ones(len(W), dtype=bool))
        return pd.Series(state == 2, index=W.index)

    def add_dd_columns(self, res):
        """The drug-dose columns imported from the atlas (wells_disagree, replicate_r), joined on drug + dose."""
        if self.dd_extra is None or not len(res) or "drug" not in res:
            return res
        e = self.dd_extra
        m = {(str(d_), str(k)): (bool(w), r) for d_, k, w, r in zip(e["drug"], e["dose"], e["wells_disagree"],
                                                                     e["replicate_r"])}
        keys = [(str(d_), dose_text(c)) for d_, c in zip(res["drug"], res["conc"])]
        res = res.copy()
        res["wells_disagree"] = [m.get(k, (False, np.nan))[0] for k in keys]
        res["replicate_r"] = [m.get(k, (False, np.nan))[1] for k in keys]
        return res


def correct_wells(d, resid, wells, method=None):
    """Per-well median over cell lines -> two-pass leave-drug-out position correction -> robust z (method v3; with
    `method`, its plate factors)."""
    w1 = pd.Series(resid, index=d.index).groupby(d["sample"].values).median()
    M = method if method is not None else Method(wells.rename_axis("sample").reset_index())
    return M.well_pass(w1)


def dose_key(sm):
    """String key for a dose; falls back to the plate when the dose is unknown."""
    return pd.Series([f"{c:.6g}" if np.isfinite(c) else f"plate:{p}"
                      for c, p in zip(sm["conc"].astype(float), sm["plate"])], index=sm.index)


def pattern(zs, thr=2.0):
    """Classify how an effect behaves across ascending doses."""
    zs = [z for z in zs if np.isfinite(z)]
    if not zs or max(zs) < thr:
        return "none"
    if len(zs) == 1:
        return "single dose"
    if min(zs) >= thr:
        return "all doses, stronger at high dose" if zs[-1] - zs[0] >= 1.0 else "all doses, flat"
    if zs[-1] >= thr and max(zs[:-1]) < thr * 0.75:
        return "top dose only"
    if zs[-1] >= thr and all(b >= a - 0.5 for a, b in zip(zs, zs[1:])):
        return "rises with dose"
    return "inconsistent across doses"


def fmt_list(vals, fmt="{:.2f}"):
    return " / ".join("NA" if not np.isfinite(v) else fmt.format(v) for v in vals)


# ============================================================================= analyses
def baseline_by_line(wl, sm, cl, targets, null_override):
    d = wl.merge(sm[["sample", "is_dmso"]], on="sample")
    dm = d[d["is_dmso"]].groupby("cell_line_id").sum(numeric_only=True)
    al = d.groupby("cell_line_id").sum(numeric_only=True)
    out = pd.DataFrame(index=al.index)
    out["n_cells_total"] = al["n_cells"]
    out["n_cells_dmso"] = dm["n_cells"].reindex(out.index).fillna(0).astype(int)
    for g in targets:
        out[f"{g}_cpm_dmso"] = 1e6 * dm[g] / dm["total_counts"]
        out[f"{g}_pct_cells_dmso"] = 100 * dm[f"det_{g}"] / dm["n_cells"]
        out[f"{g}_cpm_all_wells"] = 1e6 * al[g] / al["total_counts"]
    for m in ["PROTEASOME", "S_PHASE", "G2M_PHASE"]:
        if m in dm:
            out[f"{m}_cpm_dmso"] = 1e6 * dm[m] / dm["total_counts"]
    out["umi_per_cell_dmso"] = dm["total_counts"] / dm["n_cells"]
    out["MTAP_vs_median_line"] = out["MTAP_cpm_dmso"] / out["MTAP_cpm_dmso"].median()
    # classify on all wells (many more cells than DMSO alone; few drugs move MTAP much)
    allw = out["MTAP_cpm_all_wells"] / out["MTAP_cpm_all_wells"].median()
    out["MTAP_all_wells_vs_median_line"] = allw
    enough = out["n_cells_total"] >= MIN_LINE_CELLS
    thr, gap = null_threshold(allw[enough])
    out["MTAP_null"] = enough & (allw < thr)
    if "CDKN2A_cpm_dmso" in out:
        out["CDKN2A_vs_median_line"] = out["CDKN2A_cpm_all_wells"] / out["CDKN2A_cpm_all_wells"].median()
    if cl is not None:
        out = out.join(cl, how="left")
    source = f"MTAP across all wells below {thr:.0%} of the median line" + \
        (f" (largest gap in the data, {2 ** gap:.1f}x)" if np.isfinite(gap) else " (default cut; no clear gap)")
    if null_override:
        want = {x.strip().upper() for x in null_override.split(",") if x.strip()}
        names = out.get("cell_name", pd.Series("", index=out.index)).fillna("").str.upper()
        out["MTAP_null"] = [i.upper() in want or n in want for i, n in zip(out.index, names)]
        source = "set by --mtap-null"
    out.index.name = "cell_line_id"
    return out.sort_values("MTAP_all_wells_vs_median_line"), source


def null_threshold(ratio):
    """MTAP-deleted lines keep only background RNA from the other lines pooled in the well (roughly 10-25% of
    the median line). Cut at the largest gap between 15% and 50% of the median; else fall back to NULL_FRAC."""
    v = np.sort(np.asarray(ratio.dropna(), dtype=float))
    v = v[v > 0]
    best = None
    for a, b in zip(v[:-1], v[1:]):
        mid, gap = math.sqrt(a * b), math.log2(b / a)
        if 0.15 <= mid <= 0.5 and gap >= 0.4 and (best is None or gap > best[1]):
            best = (mid, gap)
    return best if best else (NULL_FRAC, float("nan"))


def load_cell_lines(idx):
    cl = read_tables(idx["cell_line"])
    if cl is None or "Cell_ID_Cellosaur" not in cl:
        return None
    rows = []
    for cid, g in cl.groupby("Cell_ID_Cellosaur"):
        drivers = []
        if "Driver_Gene_Symbol" in g:
            for _, r in g.iterrows():
                sym = to_text(r.get("Driver_Gene_Symbol"))
                if sym:
                    vt = to_text(r.get("Driver_VarType", ""))
                    drivers.append(f"{sym}({vt})" if vt else sym)
        first = g.iloc[0]
        rows.append({"cell_line_id": cid, "cell_name": to_text(first.get("cell_name", "")),
                     "Cell_ID_DepMap": to_text(first.get("Cell_ID_DepMap", "")),
                     "Organ": to_text(first.get("Organ", "")),
                     "drivers": "; ".join(sorted(set(drivers)))})
    return pd.DataFrame(rows).set_index("cell_line_id")


def load_drugs(idx):
    dm = read_tables(idx["drug"])
    if dm is None:
        return pd.DataFrame(columns=["targets", "moa_fine"])
    dm = dm.drop_duplicates("drug").set_index("drug")
    out = pd.DataFrame(index=dm.index)
    out["targets"] = dm["targets"].map(to_text) if "targets" in dm else ""
    out["moa_fine"] = dm["moa-fine"].map(to_text) if "moa-fine" in dm else ""
    out["moa_broad"] = dm["moa-broad"].map(to_text) if "moa-broad" in dm else ""
    if "human-approved" in dm:
        out["approved"] = dm["human-approved"].map(to_text)
    return out


def row_medians_of_others(W, col):
    """Per well: the median of `col` over the OTHER drug wells in the same plate row (A-H) of its plate; NaN when
    there are none. Tells a drug's own cell loss from a technical loss of the whole row."""
    row = W["well"].astype(str).str.extract(r"^([A-Ha-h])", expand=False).str.upper().fillna("").to_numpy()
    v = W[col].to_numpy(dtype=float)
    drug = ~W["is_dmso"].astype(bool).to_numpy()
    out = np.full(len(W), np.nan)
    for (_p, r), ii in pd.Series(np.arange(len(W))).groupby([W["plate"].to_numpy(), row]).groups.items():
        if not r:
            continue
        ii = np.asarray(list(ii))
        for i in ii:
            m = ii[(ii != i) & drug[ii] & np.isfinite(v[ii])]
            if m.size:
                out[i] = float(np.median(v[m]))
    return out


def well_context(wl, sm, cols_present, method=None):
    """Per-well covariates: cells, genes and UMIs per cell vs the plate's drug wells, the same for the other drug
    wells of the well's plate row (row_*: a technical loss of a whole row), the cell loss the row does not explain
    (cells_log2_beyond_row; a drug-dose keeps its best used well's: cells_log2_best_well), the composition shift
    (median over the
    well's lines), the plate factor, whether the position could be corrected at all, and the cell-cycle modules
    (corrected like every gene: shift_log2 and z)."""
    M = method if method is not None else Method(sm)
    d = wl.merge(sm[["sample"]], on="sample")
    tot = d.groupby("sample")[["n_cells", "n_genes", "total_counts"]].sum()
    W = M.W.reindex(tot.index).copy()
    W["cells"] = tot["n_cells"]
    W["genes_per_cell"] = tot["n_genes"] / tot["n_cells"]
    W["umi_per_cell"] = tot["total_counts"] / tot["n_cells"]
    for c in ["cells", "genes_per_cell", "umi_per_cell"]:
        ref = W.loc[~W["is_dmso"]].groupby("plate")[c].median()
        W[f"{c}_log2_vs_plate"] = np.log2(W[c] / W["plate"].map(ref))
    for c, name in (("cells_log2_vs_plate", "row_cells_log2"), ("umi_per_cell_log2_vs_plate", "row_umi_per_cell_log2"),
                    ("genes_per_cell_log2_vs_plate", "row_genes_per_cell_log2")):
        W[name] = row_medians_of_others(W, c)
    W["cells_log2_beyond_row"] = cells_beyond_row(W["cells_log2_vs_plate"], W["row_cells_log2"])
    ctx = W[["cells", "cells_log2_vs_plate", "genes_per_cell_log2_vs_plate", "umi_per_cell_log2_vs_plate",
             "row_cells_log2", "row_umi_per_cell_log2", "row_genes_per_cell_log2", "cells_log2_beyond_row"]].copy()
    if M.shift is not None:
        ctx["composition_shift_log2"] = M.well_shift().reindex(ctx.index)
    ctx["plate_scale"] = M.well_factor(2, ctx.index)
    ctx["position_not_correctable"] = M.not_correctable().reindex(ctx.index).fillna(True).astype(bool)
    for m in ["S_PHASE", "G2M_PHASE"]:
        if m in cols_present:
            Wm = M.finish(M.core(wl, m, []))
            ctx[f"{m}_shift_log2"] = Wm["W2"].reindex(ctx.index)
            ctx[f"{m}_z"] = Wm["z"].reindex(ctx.index)
    return ctx


def best_well_columns(g, res):
    """Drug-dose columns taken from the best used well instead of the mean (g: the used wells grouped by drug-dose;
    res: their means): cells_log2_best_well = the largest cells_log2_beyond_row, so one well's cell count never
    makes a replicated drug-dose 'toxic' (duplicate wells of the real data do not agree on cell loss)."""
    if "cells_log2_beyond_row" in res:
        res = res.drop(columns=["cells_log2_beyond_row"])
        res["cells_log2_best_well"] = g["cells_log2_beyond_row"].max()
    return res


def stouffer(g, col):
    """Stouffer's z over the rows of each group (NaN skipped)."""
    return g[col].sum() / np.sqrt(g[col].count())


def expression_effects(wl, sm, gene, exclude_lines, ctx, drugs, extra_cols=None, method=None, min_lines=None):
    """Corrected effect of every drug and dose on one gene (or module), method v3 (Method): plate baseline ->
    composition shift -> median over lines (min_lines: see Method.add) -> two-pass leave-drug-out position
    correction -> z against the drug wells of the reliable plates, scaled by the plate factor -> per drug-dose over
    its used wells."""
    M = method if method is not None else Method(sm)
    core = M.core(wl, gene, exclude_lines, min_lines)
    c0, s0 = core["c"], core["s"]
    W = M.finish(core)
    d = M.profiles(wl, gene, exclude_lines)
    has_det = f"det_{gene}" in d
    d["r2"] = d["r1c"] - d["sample"].map(W["slot_effect"])
    ref = d.loc[d["sample"].map(reference_wells(W)).fillna(False).astype(bool)]
    lc = ref.groupby("cell_line_id")["r2"].median()
    ls = 1.4826 * (ref["r2"] - ref["cell_line_id"].map(lc)).abs().groupby(ref["cell_line_id"]).median()
    d["z_line"] = (d["r2"] - d["cell_line_id"].map(lc)) / d["cell_line_id"].map(ls)

    # the old way, for comparison: fold change against the plate's pooled DMSO wells (no composition, no position)
    dm = d[d["is_dmso"]].groupby(["plate", "cell_line_id"])[[gene, "total_counts"]].sum()
    dmso_y = np.log2((dm[gene] + 0.5) / (dm["total_counts"] + 1.0) * 1e6)
    key = pd.MultiIndex.from_arrays([d["plate"], d["cell_line_id"]])
    d["lfc_dmso"] = d["y"].values - dmso_y.reindex(key).values
    W["lfc_vs_dmso"] = d.groupby("sample")["lfc_dmso"].median().reindex(W.index)
    W["lines_in_well"] = d.groupby("sample").size().reindex(W.index)

    # single-cell detail: more cells expressing, or more per expressing cell?
    if has_det:
        d["pct"] = 100.0 * d[f"det_{gene}"] / d["n_cells"]
        d["lvl"] = np.log2(((d[gene] + 0.5) / (d[f"det_{gene}"] + 0.5)) / (d["total_counts"] / d["n_cells"]))
        Wp, _ = M.well_pass(pd.Series(plate_line_residual(d, "pct"), index=d.index).groupby(d["sample"]).median())
        Wl, _ = M.well_pass(pd.Series(plate_line_residual(d, "lvl") - M.shift_of(d), index=d.index)
                            .groupby(d["sample"]).median())
        W["pct_cells_expressing_change"] = Wp["W2"].reindex(W.index)
        W["level_in_expressing_cells_log2"] = Wl["W2"].reindex(W.index)

    # plate DMSO offset: >0 means the plate's DMSO wells read low, inflating DMSO-based fold changes
    pl = pd.DataFrame({"plate": d["plate"], "off": d["lfc_dmso"] - d["r1"]}).dropna()
    plate_off = pl.groupby("plate")["off"].median()
    W["plate_dmso_offset"] = W["plate"].map(plate_off)
    zctx = []
    if ctx is not None:
        zctx = [c for c in ctx.columns if c.endswith("_z")]
        W = W.join(ctx.drop(columns=[c for c in ctx.columns if c in W]), how="left")
    if extra_cols is not None:
        W = W.join(extra_cols.drop(columns=[c for c in extra_cols.columns if c in W]), how="left")

    # ---- per drug and dose (plates averaged; cell lines counted once); the wells of unreliable plates only when
    # the drug-dose has no other well
    Wd = W.loc[~W["is_dmso"]].copy()
    Wd["dose"] = dose_key(Wd)
    Wd["_used"] = used_wells(Wd)
    left = (~Wd["_used"]).groupby([Wd["drug"], Wd["dose"]]).sum()
    Wu = Wd.loc[Wd["_used"]]
    d2 = d.loc[d["sample"].isin(Wu.index)].copy()
    d2["dose"] = d2["sample"].map(Wu["dose"])
    per_line = d2.groupby(["drug", "dose", "cell_line_id"])[["r2", "z_line"]].mean().reset_index()
    per_line["up"] = (per_line["z_line"] > Z_LINE) & (per_line["r2"] > LFC_MIN)
    per_line["down"] = (per_line["z_line"] < -Z_LINE) & (per_line["r2"] < -LFC_MIN)
    per_line["pos"] = per_line["r2"] > 0
    per_line["neg"] = per_line["r2"] < 0
    lines = per_line.groupby(["drug", "dose"]).agg(n_lines=("up", "size"), n_lines_up=("up", "sum"),
                                                   n_lines_down=("down", "sum"), n_pos=("pos", "sum"),
                                                   n_neg=("neg", "sum"))
    flagcols = ["position_correction_uncertain", "position_not_correctable", "unreliable_plate"]
    skip = {"plate", "drug", "conc", "slot", "well", "is_dmso", "dose", "z", "_used", "pos_state", "W2a"} | \
        set(flagcols) | set(zctx)
    num = [c for c in Wu.columns if c not in skip and pd.api.types.is_numeric_dtype(Wu[c])]
    g = Wu.groupby(["drug", "dose"])
    res = best_well_columns(g, g[num].mean())
    res["z"] = stouffer(g, "z")                            # Stouffer across plates
    for c in zctx:
        res[c] = stouffer(g, c)
    res["position_correction_uncertain"] = g["position_correction_uncertain"].any()
    res["position_not_correctable"] = g["position_not_correctable"].any()
    res["unreliable_plate_only"] = g["unreliable_plate"].all()
    res["n_wells_left_out_unreliable"] = left.reindex(res.index).fillna(0).astype(int)
    res["n_plates"] = g.size()
    res["plates"] = g["plate"].agg(lambda s: ",".join(sorted(set(map(str, s)))))
    res["wells"] = g["well"].agg(lambda s: ",".join(sorted(set(map(str, s)))))
    res["conc"] = g["conc"].first()
    res = res.join(lines)
    res["frac_lines_up"] = res["n_lines_up"] / res["n_lines"]
    res["frac_lines_down"] = res["n_lines_down"] / res["n_lines"]
    res["frac_lines_positive"] = res.pop("n_pos") / res["n_lines"]
    res["frac_lines_negative"] = res.pop("n_neg") / res["n_lines"]
    res["p_up"] = norm_sf(res["z"].values)
    res["p_down"] = norm_sf(-res["z"].values)
    res["fdr_up"] = bh(res["p_up"].values)
    res["fdr_down"] = bh(res["p_down"].values)
    res["fold_change"] = 2.0 ** res["W2"]
    res = res.reset_index().drop(columns=["dose"])
    res = res.join(drugs, on="drug")
    res = M.add_dd_columns(res)
    res = res.rename(columns={"W2": "log2FC_corrected", "z": "z_corrected",
                              "lfc_vs_dmso": "log2FC_vs_DMSO_uncorrected", "slot_effect": "position_effect_removed",
                              "W1": "log2FC_plate_corrected_only", "slot_n": "position_wells_used",
                              "slot_clean_n": "position_clean_donors"})
    res["flags"] = flag_rows(res, gene)
    res["call"] = [call_row(r) for _, r in res.iterrows()]
    lead = ["drug", "conc", "call", "fold_change", "log2FC_corrected", "z_corrected", "fdr_up", "fdr_down",
            "n_lines", "n_lines_up", "n_lines_down", "frac_lines_positive", "flags", "log2FC_vs_DMSO_uncorrected",
            "position_effect_removed", "plate_dmso_offset", "wells", "plates", "n_plates", "plate_scale",
            "composition_shift_log2"]
    res = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]]
    dw, rel = ~W["is_dmso"] & W["z"].notna(), reference_wells(W) & W["z"].notna()   # shares of the measured z
    zu = (W["W2"] - c0) / s0
    calib = {
        "drug_wells": int((~W["is_dmso"]).sum()), "drug_wells_with_z": int(dw.sum()),
        "pct_drug_wells_abs_z_gt_1.96": float(100 * (W.loc[dw, "z"].abs() > 1.96).mean()),
        "pct_dmso_wells_abs_z_gt_1.96": float(100 * (W.loc[W["is_dmso"], "z"].dropna().abs() > 1.96).mean())
        if W["is_dmso"].any() else float("nan"),
        "pct_drug_wells_abs_z_gt_3": float(100 * (W.loc[dw, "z"].abs() > 3).mean()),
        "pct_drug_wells_abs_z_gt_1.96_unscaled": float(100 * (zu[dw].abs() > 1.96).mean()),
        "pct_reliable_drug_wells_abs_z_gt_1.96": float(100 * (W.loc[rel, "z"].abs() > 1.96).mean()),
        "wells_position_uncertain": int(W.loc[~W["is_dmso"], "position_correction_uncertain"].sum()),
        "wells_position_not_correctable": int(W.loc[~W["is_dmso"], "position_not_correctable"].sum()),
        "null_center": c0, "null_scale": s0,
    }
    return res, W, d, calib


def _num(r, k, default=0.0):
    """r[k] as a float; default when missing or not finite (a NaN never triggers a flag)."""
    v = r.get(k, default)
    try:
        v = float(v)
    except (TypeError, ValueError):
        return default
    return v if math.isfinite(v) else default


def is_toxic(cells, row, best_well=float("nan"), higher_keeps=False):
    """'toxic' (method v3, one definition with tahoe_atlas.flags_for): the drug-dose's mean cell count is < -1 log2
    vs the plate, also beyond its plate row where that row is itself shifted (cells_beyond_row), its best used well
    lost cells too (best_well = the largest cells_beyond_row of the used wells < TOXIC_BEST_WELL: a well of several
    that kept its cells means the loss did not replicate; NaN: not known), and no higher dose of the drug keeps
    >= half the plate's cells. For a drug-dose of one well this is: its loss beyond a shifted row < -1."""
    if not cells < -1 or not float(cells_beyond_row(cells, row)) < -1 or higher_keeps:
        return False
    return not (math.isfinite(best_well) and best_well >= TOXIC_BEST_WELL)


def cell_loss_replication(W):
    """How well two wells of one drug-dose agree on cell loss: Spearman r of cells_log2_beyond_row between the two
    used wells of every drug-dose with exactly two on reliable plates (W: per-well table with drug, dose or conc,
    unreliable_plate, cells_log2_beyond_row, is_dmso). Returns (r, number of drug-doses); (nan, n) below 10.
    In the first real run duplicate wells did not agree (r ~ -0.2): a one-well 'toxic' is weak evidence."""
    W = W[~W["is_dmso"].astype(bool)]
    if "unreliable_plate" in W:
        W = W[~W["unreliable_plate"].fillna(False).astype(bool)]
    key = W["dose"] if "dose" in W else W["conc"].map(dose_text)
    g = W.assign(_k=key).groupby(["drug", "_k"])["cells_log2_beyond_row"]
    two = [v.to_numpy(dtype=float) for _, v in g if len(v) == 2 and np.isfinite(v.to_numpy(dtype=float)).all()]
    if len(two) < 10:
        return float("nan"), len(two)
    a, b = (pd.Series([t[i] for t in two]).rank() for i in (0, 1))
    return float(np.corrcoef(a, b)[0, 1]), len(two)


def cell_loss_replication_text(r, n):
    """The sentence the briefs state about 'toxic' at the top dose, from cell_loss_replication."""
    if not np.isfinite(r):
        return (f"too few two-well drug-doses ({n}) to say how well wells agree on cell loss: treat a one-well "
                "'toxic' as weak evidence alone")
    how = "poorly, so a one-well 'toxic' is weak evidence alone" if r < 0.5 else \
        "well, but a one-well 'toxic' is still a single measurement"
    return f"two wells of one drug-dose agree on cell loss at Spearman r {r:.2f} ({n} drug-doses): {how}"


def higher_dose_keeps_cells(res):
    """Per drug-dose row: does a HIGHER dose of the same drug keep >= half the plate's usual cells (its mean
    cells_log2_vs_plate >= -1)? Then this dose's cell loss is not dose-consistent: 'low cells (technical?)'."""
    if not len(res) or "cells_log2_vs_plate" not in res:
        return np.zeros(len(res), dtype=bool)
    c = pd.to_numeric(res["cells_log2_vs_plate"], errors="coerce").to_numpy(dtype=float)
    conc = pd.to_numeric(res["conc"], errors="coerce").to_numpy(dtype=float)
    out = np.zeros(len(res), dtype=bool)
    for ii in pd.Series(np.arange(len(res))).groupby(res["drug"].astype(str).to_numpy()).groups.values():
        ii = np.asarray(list(ii))
        for i in ii:
            out[i] = bool(((conc[ii] > conc[i]) & (c[ii] >= -1)).any())
    return out


def flag_rows(res, gene=""):
    """flag_row for every row of a drug-dose table (adds the dose-consistency input of 'toxic')."""
    keep = higher_dose_keeps_cells(res)
    return [flag_row({**r, "higher_dose_keeps_cells": k}, gene) for r, k in zip(res.to_dict("records"), keep)]


def flag_row(r, gene):
    """Artifact flags of one drug-dose (method v3; the same definitions as tahoe_atlas.py). The values are the
    drug-dose's means over its used wells; row_* = the median of the other drug wells in the same plate row;
    cells_log2_best_well = the best used well's cell loss beyond a shifted row (cells_beyond_row). Use flag_rows on
    a whole table: 'toxic' needs the drug's other doses."""
    f = []
    cells, row = _num(r, "cells_log2_vs_plate"), _num(r, "row_cells_log2")
    if cells < -1:
        f.append("toxic" if is_toxic(cells, row, _num(r, "cells_log2_best_well", float("nan")),
                                     bool(_num(r, "higher_dose_keeps_cells"))) else "low cells (technical?)")
    if abs(row) > ROW_SHIFT or _num(r, "row_umi_per_cell_log2") < -0.4:
        f.append("plate-row cell shift")
    g, u = _num(r, "genes_per_cell_log2_vs_plate"), _num(r, "umi_per_cell_log2_vs_plate")
    if (g < -0.3 and g - _num(r, "row_genes_per_cell_log2") < -0.3) or \
            (u < -0.5 and u - _num(r, "row_umi_per_cell_log2") < -0.5):
        f.append("transcription drop")
    cyc = [(abs(_num(r, f"{m}_shift_log2")), abs(_num(r, f"{m}_z"))) for m in ("S_PHASE", "G2M_PHASE")]
    if any(s > 0.5 or (s > 0.25 and z >= 4) for s, z in cyc):
        f.append("cell-cycle shift")
    if abs(_num(r, "composition_shift_log2")) >= COMPOSITION_FLAG:
        f.append("composition shift")
    if max(_num(r, "plate_scale", 1.0), _num(r, "plate_scale_gene", 1.0)) > NOISY_PLATE:
        f.append("noisy plate (z scaled)")
    if _num(r, "unreliable_plate_only"):
        f.append("unreliable plate only")
    if gene == "PSMD10" and math.isfinite(_num(r, "PROTEASOME_z", float("nan"))):
        if _num(r, "z_corrected") > 2 and _num(r, "PROTEASOME_z") > 2:
            f.append("whole proteasome up")
        if _num(r, "z_corrected") < -2 and _num(r, "PROTEASOME_z") < -2:
            f.append("whole proteasome down")
    if _num(r, "position_not_correctable"):
        f.append("position not correctable")
    if _num(r, "position_correction_uncertain"):
        f.append("position correction uncertain")
    if abs(_num(r, "position_effect_removed")) > 0.2:
        f.append("position effect removed")
    if _num(r, "wells_disagree"):
        f.append("wells disagree")
    return "; ".join(f)


def call_row(r):
    if r["fdr_up"] < FDR_CUT and r["log2FC_corrected"] >= LFC_MIN and r["frac_lines_positive"] >= 0.6:
        return "up"
    if r["fdr_down"] < FDR_CUT and r["log2FC_corrected"] <= -LFC_MIN and r["frac_lines_negative"] >= 0.6:
        return "down"
    return ""


def drug_summary(res):
    rows = []
    for drug, g in res.groupby("drug"):
        g = g.sort_values("conc")
        zs = g["z_corrected"].tolist()
        best_up = g.loc[g["z_corrected"].fillna(-np.inf).idxmax()]
        best_dn = g.loc[g["z_corrected"].fillna(np.inf).idxmin()]
        k = len(g)
        p_up = min(1.0, k * float(g["p_up"].min()))
        p_dn = min(1.0, k * float(g["p_down"].min()))
        rows.append({
            "drug": drug, "moa_fine": best_up.get("moa_fine", ""), "targets": best_up.get("targets", ""),
            "doses": fmt_list(g["conc"].tolist(), "{:g}"),
            "z_by_dose": fmt_list(zs), "log2FC_by_dose": fmt_list(g["log2FC_corrected"].tolist()),
            "best_up_dose": best_up["conc"], "best_up_fold_change": best_up["fold_change"],
            "best_up_z": best_up["z_corrected"], "p_up_drug": p_up,
            "up_lines": f"{int(best_up['n_lines_up'])}/{int(best_up['n_lines'])}",
            "pct_lines_positive_at_best_up": round(100 * best_up["frac_lines_positive"]),
            "up_pattern": pattern(zs), "up_call": best_up["call"] if best_up["call"] == "up" else "",
            "up_flags": best_up["flags"],
            "best_down_dose": best_dn["conc"], "best_down_fold_change": best_dn["fold_change"],
            "best_down_z": best_dn["z_corrected"], "p_down_drug": p_dn,
            "down_lines": f"{int(best_dn['n_lines_down'])}/{int(best_dn['n_lines'])}",
            "pct_lines_negative_at_best_down": round(100 * best_dn["frac_lines_negative"]),
            "down_pattern": pattern([-z for z in zs]),
            "down_call": best_dn["call"] if best_dn["call"] == "down" else "",
            "down_flags": best_dn["flags"],
            "uncorrected_log2FC_vs_DMSO_at_best_up": best_up["log2FC_vs_DMSO_uncorrected"],
            "wells": ",".join(sorted(set(",".join(g["wells"].astype(str)).split(",")))),
        })
    s = pd.DataFrame(rows)
    s["fdr_up_drug"] = bh(s["p_up_drug"].values)
    s["fdr_down_drug"] = bh(s["p_down_drug"].values)
    return s.sort_values("best_up_z", ascending=False)


def abundance(wl, sm, base):
    """Relative abundance of each cell line in each well vs the plate's drug-well median. Lines with very few cells
    are left out (counting noise is propagated into the scores, so moderately rare lines are fine)."""
    lines = base.index[base["n_cells_total"] >= 0.02 * base["n_cells_total"].median()]
    d = wl.loc[wl["cell_line_id"].isin(lines), ["sample", "cell_line_id", "n_cells"]]
    grid = pd.MultiIndex.from_product([sm["sample"], lines], names=["sample", "cell_line_id"])
    n = d.set_index(["sample", "cell_line_id"])["n_cells"].reindex(grid, fill_value=0).reset_index()
    n = n.merge(sm[["sample", "plate", "drug", "conc", "slot", "well", "is_dmso"]], on="sample")
    N = n.groupby("sample")["n_cells"].transform("sum")
    n["frac"] = n["n_cells"] / N
    eps = 0.5 / float(n.groupby("sample")["n_cells"].sum().median())
    ref = n.loc[~n["is_dmso"]].groupby(["plate", "cell_line_id"])["frac"].median()
    key = pd.MultiIndex.from_arrays([n["plate"], n["cell_line_id"]])
    n["A"] = np.log2((n["frac"].values + eps) / (ref.reindex(key).values + eps))
    n["varA"] = 1.0 / ((n["n_cells"] + 0.5) * math.log(2) ** 2)   # counting noise of A (Poisson)
    return n


def find_failed_wells(sm):
    """Wells that recovered < 1/8 of the plate's typical cell count while the same drug recovered at least half
    at the same or a higher dose elsewhere. Treated as technical failures and excluded from every analysis."""
    s = sm.copy()
    med = s.loc[~s["is_dmso"]].groupby("plate")["n_cells"].median()
    s["cells_log2_vs_plate"] = np.log2(s["n_cells"] / s["plate"].map(med))
    failed = []
    for _, r in s[s["cells_log2_vs_plate"] < -3].iterrows():
        other = s[(s["drug"] == r["drug"]) & (s["sample"] != r["sample"]) & (s["conc"] >= r["conc"])]
        if (other["cells_log2_vs_plate"] > -1).any():
            failed.append(r["sample"])
    return s[s["sample"].isin(failed)]


def add_dose_columns(res, zcol, pcol, direction):
    """Add the drug's z at every dose, a dose pattern, and a drug-level FDR (best dose, Bonferroni over doses)."""
    zs_map, doses_map, pat_map, p_map = {}, {}, {}, {}
    for drug, g in res.groupby("drug"):
        g = g.sort_values("conc")
        zs = g[zcol].tolist()
        zs_map[drug] = fmt_list(zs)
        doses_map[drug] = fmt_list(g["conc"].tolist(), "{:g}")
        pat_map[drug] = pattern([-z for z in zs] if direction == "down" else zs)
        p_map[drug] = min(1.0, len(g) * float(np.nanmin(g[pcol].values)))
    drugs = list(p_map)
    fdr = dict(zip(drugs, bh(np.array([p_map[d] for d in drugs]))))
    res = res.copy()
    res["doses"] = res["drug"].map(doses_map)
    res["z_by_dose"] = res["drug"].map(zs_map)
    res["dose_pattern"] = res["drug"].map(pat_map)
    res["fdr_drug"] = res["drug"].map(fdr)
    return res


def per_dose_table(W, value_cols, zcol="z"):
    """Per drug-dose over its used wells (used_wells): means of value_cols, Stouffer of zcol and of every value
    column ending in '_z', any() of boolean columns; unreliable_plate_only and n_wells_left_out_unreliable when W
    carries unreliable_plate."""
    Wd = W.loc[~W["is_dmso"]].copy()
    Wd["dose"] = dose_key(Wd)
    used = used_wells(Wd)
    left = (~used).groupby([Wd["drug"], Wd["dose"]]).sum()
    Wd = Wd.loc[used]
    g = Wd.groupby(["drug", "dose"])
    zc = [c for c in value_cols if c.endswith("_z") and c != zcol]
    bc = [c for c in value_cols if c not in zc and (pd.api.types.is_bool_dtype(Wd[c]) or (
        Wd[c].dtype == object and len(Wd[c].dropna()) and Wd[c].dropna().map(type).eq(bool).all()))]
    for c in bc:
        Wd[c] = Wd[c].fillna(False).astype(bool)
    res = g[[c for c in value_cols if c not in zc and c not in bc]].mean()
    for c in value_cols:
        if c in zc:
            res[c] = stouffer(g, c)
        elif c in bc:
            res[c] = g[c].any()
    res = best_well_columns(g, res[[c for c in value_cols]])
    res["z"] = stouffer(g, zcol)
    res["conc"] = g["conc"].first()
    res["wells"] = g["well"].agg(lambda s: ",".join(sorted(set(map(str, s)))))
    res["plates"] = g["plate"].agg(lambda s: ",".join(sorted(set(map(str, s)))))
    if "unreliable_plate" in Wd:
        res["unreliable_plate_only"] = g["unreliable_plate"].all()
        res["n_wells_left_out_unreliable"] = left.reindex(res.index).fillna(0).astype(int)
    return res.reset_index().drop(columns=["dose"])


def mtap_null_screen(n, base, sm, drugs, ctx):
    wells = wells_of(sm)
    null = set(base.index[base["MTAP_null"]])
    intact = set(base.index[~base["MTAP_null"]])
    n = n.copy()
    n["grp"] = np.where(n["cell_line_id"].isin(null), "null", np.where(n["cell_line_id"].isin(intact), "intact", ""))
    A = n.pivot_table(index="sample", columns="cell_line_id", values="A")
    V = n.pivot_table(index="sample", columns="cell_line_id", values="varA")
    nl = [c for c in A.columns if c in null]
    il = [c for c in A.columns if c in intact]
    W = wells.reindex(A.index).copy()
    W["null_mean_log2"] = A[nl].mean(axis=1)
    W["intact_median_log2"] = A[il].median(axis=1)
    W["delta"] = W["null_mean_log2"] - W["intact_median_log2"]
    # counting noise of delta (mean of the null lines minus median of the intact lines)
    k, m = max(len(nl), 1), max(len(il), 1)
    W["delta_counting_var"] = V[nl].sum(axis=1) / k ** 2 + (math.pi / 2) * V[il].sum(axis=1) / m ** 2
    # tissue-matched: MTAP-null lines vs MTAP-intact lines of the same organ
    organ = base.get("Organ", pd.Series("", index=base.index)).fillna("")
    parts, wts = [], []
    for o in sorted(set(organ[list(null)])):
        if not o:
            continue
        on = [c for c in nl if organ.get(c, "") == o]
        oi = [c for c in il if organ.get(c, "") == o]
        if on and len(oi) >= 2:
            parts.append(A[on].mean(axis=1) - A[oi].median(axis=1))
            wts.append(len(on))
    if parts:
        W["delta_tissue_matched"] = sum(p * w for p, w in zip(parts, wts)) / sum(wts)
    eff, n_used = loo_slot(W["delta"].values, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
    W["position_effect_removed"] = eff
    W["delta_corrected"] = W["delta"] - eff
    # spread across wells = biological/technical well noise + counting noise; wells with few cells get the
    # counting part on top, so a handful of surviving cells cannot produce an extreme score (reliable plates)
    drug_w = reference_wells(W)
    c, s = robust_center_scale(W.loc[drug_w, "delta_corrected"])
    typical_count_var = float(np.nanmedian(W.loc[drug_w, "delta_counting_var"]))
    well_var = max(s ** 2 - typical_count_var, (0.25 * s) ** 2)
    W["z"] = (W["delta_corrected"] - c) / np.sqrt(well_var + W["delta_counting_var"])
    W = W.join(ctx[["cells_log2_vs_plate"]], how="left")
    names = base.get("cell_name", pd.Series(index=base.index, dtype=object)).fillna("")
    for cid in nl:
        W[f"{names.get(cid) or cid}_log2"] = A[cid]
    vals = ["delta_corrected", "delta", "null_mean_log2", "intact_median_log2", "position_effect_removed",
            "cells_log2_vs_plate"] + (["delta_tissue_matched"] if "delta_tissue_matched" in W else []) + \
           [f"{names.get(cid) or cid}_log2" for cid in nl]
    res = per_dose_table(W, vals)
    res["p_selective"] = norm_sf(-res["z"].values)
    res["fdr_selective"] = bh(res["p_selective"].values)
    res = res.join(drugs, on="drug")
    tgt = res.get("targets", pd.Series("", index=res.index)).fillna("").str.upper()
    moa = res.get("moa_fine", pd.Series("", index=res.index)).fillna("").str.upper()
    res["PRMT5_or_MAT2A_drug"] = tgt.str.contains("PRMT5|MAT2A") | moa.str.contains("PRMT5|MAT2A")
    res = res.rename(columns={"z": "z_selective", "delta_corrected": "extra_log2_depletion_of_MTAP_null",
                              "cells_log2_vs_plate": "all_cells_log2_vs_plate"})
    res = add_dose_columns(res, "z_selective", "p_selective", "down")
    lead = ["drug", "conc", "extra_log2_depletion_of_MTAP_null", "z_selective", "fdr_selective", "fdr_drug",
            "z_by_dose", "dose_pattern", "PRMT5_or_MAT2A_drug", "delta_tissue_matched", "intact_median_log2",
            "all_cells_log2_vs_plate"]
    res = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]]
    return res.sort_values("z_selective"), W, sorted(nl), sorted(il)


def gankyrin_level_screen(n, base, sm, drugs):
    """Does a cell line's untreated Gankyrin level predict how a drug affects its abundance?"""
    wells = wells_of(sm)
    A = n.pivot_table(index="sample", columns="cell_line_id", values="A")
    lines = [c for c in A.columns if np.isfinite(base.loc[c, "PSMD10_cpm_dmso"])]
    A = A[lines]
    x = np.log2(base.loc[lines, "PSMD10_cpm_dmso"].values)
    gcol = "G2M_PHASE_cpm_dmso" if "G2M_PHASE_cpm_dmso" in base else None
    rA = A.rank(axis=1).values
    rx = pd.Series(x).rank().values

    def rowcorr(M, v):
        Mc = M - M.mean(axis=1, keepdims=True)
        vc = v - v.mean()
        den = np.sqrt((Mc ** 2).sum(axis=1) * (vc ** 2).sum())
        with np.errstate(invalid="ignore", divide="ignore"):
            return (Mc @ vc) / den

    W = wells.reindex(A.index).copy()
    W["rho"] = rowcorr(rA, rx)
    if gcol:
        rg = pd.Series(np.log2(base.loc[lines, gcol].values)).rank().values
        G = np.column_stack([np.ones_like(rg), rg])
        P = G @ np.linalg.pinv(G)
        W["rho_partial_G2M"] = rowcorr(rA - rA @ P.T, rx - P @ rx)
    fz = np.arctanh(np.clip(W["rho"].values, -0.999, 0.999))
    eff, _ = loo_slot(fz, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
    W["fisher_corrected"] = fz - eff
    c, s = robust_center_scale(W.loc[reference_wells(W), "fisher_corrected"])
    W["z"] = (W["fisher_corrected"] - c) / s
    vals = ["rho"] + (["rho_partial_G2M"] if gcol else [])
    res = per_dose_table(W, vals)
    res["p"] = 2 * norm_sf(np.abs(res["z"].values))
    res["fdr"] = bh(res["p"].values)
    res = res.join(drugs, on="drug").rename(columns={"z": "z_corrected"})
    res["reading"] = np.where(res["z_corrected"] < 0, "high-Gankyrin lines depleted more",
                              "high-Gankyrin lines spared")
    res = add_dose_columns(res, "z_corrected", "p", "down")
    res = res.rename(columns={"dose_pattern": "dose_pattern_depleted_more"})
    lead = ["drug", "conc", "rho", "rho_partial_G2M", "z_corrected", "fdr", "fdr_drug", "z_by_dose",
            "dose_pattern_depleted_more", "reading"]
    res = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]]
    return res.sort_values("z_corrected"), len(lines)


def cell_cycle_by_line(out, base, cols_present):
    need = {"PSMD10", "MTAP", "S_PHASE", "G2M_PHASE"}
    if not need <= set(cols_present):
        return None
    cells_dir = os.path.join(out, "cells")
    files = sorted(glob.glob(os.path.join(cells_dir, "*.parquet")))
    parts = []
    for f in files:
        t = pq.read_table(f, columns=["drug", "cell_line_id", "total_counts", "MTAP", "PSMD10", "S_PHASE", "G2M_PHASE"])
        mask = pc.starts_with(pc.utf8_upper(t["drug"]), DMSO_PREFIX)
        t = t.filter(mask)
        if t.num_rows:
            parts.append(t.select(["cell_line_id", "total_counts", "MTAP", "PSMD10", "S_PHASE",
                                   "G2M_PHASE"]).to_pandas())
    if not parts:
        return None
    df = pd.concat(parts, ignore_index=True)
    # normalise by counts outside the cell-cycle genes, so their own rise in cycling cells does not dilute others
    df["den"] = df["total_counts"] - df["S_PHASE"] - df["G2M_PHASE"]
    df = df[df["den"] > 0]
    df["cell_line_id"] = df["cell_line_id"].astype(str)
    rows = []
    for cid, x in df.groupby("cell_line_id"):
        if len(x) < 100:
            continue
        r = {"cell_line_id": cid, "n_dmso_cells": len(x)}
        for score in ["G2M_PHASE", "S_PHASE"]:
            sc = x[score] / x["den"]
            lo, hi = sc.quantile(0.25), sc.quantile(0.75)
            top, bot = x[sc >= hi], x[sc <= lo]
            for g in ["PSMD10", "MTAP"]:
                a = top[g].sum() / top["den"].sum()
                b = bot[g].sum() / bot["den"].sum()
                r[f"{g}_log2_top_vs_bottom_{score}_quartile"] = np.log2(a / b) if a > 0 and b > 0 else np.nan
                r[f"{g}_cell_spearman_vs_{score}"] = (x[g] / x["den"]).rank().corr(sc.rank())
        rows.append(r)
    if not rows:
        return None
    res = pd.DataFrame(rows).set_index("cell_line_id")
    if "cell_name" in base:
        res.insert(0, "cell_name", base["cell_name"].reindex(res.index))
    return res


def slot_table(W, label):
    Wd = W.loc[~W["is_dmso"]]
    g = Wd.groupby("well")
    t = pd.DataFrame({"median_effect_plate_corrected": g["W1"].median(), "n_wells": g.size(),
                      "drugs": g["drug"].agg(lambda s: ", ".join(sorted(set(s))))})
    c, s = robust_center_scale(t["median_effect_plate_corrected"])
    t["z_vs_other_positions"] = (t["median_effect_plate_corrected"] - c) / s
    t.insert(0, "gene", label)
    return t.sort_values("z_vs_other_positions", ascending=False)


def plate_table(W, label):
    t = W.groupby("plate").agg(dmso_offset=("plate_dmso_offset", "first"),
                               n_dmso_wells=("is_dmso", "sum"))
    t["dmso_wells"] = W.loc[W["is_dmso"]].groupby("plate")["well"].agg(lambda s: ",".join(map(str, s)))
    t.insert(0, "gene", label)
    return t.sort_values("dmso_offset", ascending=False)


def atlas_effects_version(atl):
    """The version stamped in <atl>/effects/complete.json (0 when missing or unreadable)."""
    try:
        with open(os.path.join(atl, "effects", "complete.json"), encoding="utf-8") as fh:
            return int(json.load(fh).get("version") or 0)
    except (OSError, ValueError, TypeError, AttributeError):
        return 0


def atlas_dir(args):
    """--atlas DIR (default <data>/atlas); None for --atlas none (load_atlas_inputs(..., why='--atlas none'))."""
    a = getattr(args, "atlas", None)
    if a and str(a).strip().lower() == "none":
        return None
    return a or os.path.join(args.data, "atlas")


def atlas_build_info(atl):
    """(unreliable plates of its effects or None, limit_files of its build): from effects/complete.json and
    build_info.json of a computed atlas."""
    def rd(*parts):
        try:
            with open(os.path.join(atl, *parts), encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return {}
    cj, bi = rd("effects", "complete.json"), rd("build_info.json")
    unrel = cj.get("unreliable_plates") if isinstance(cj, dict) else None
    lim = bi.get("limit_files") if isinstance(bi, dict) else 0
    return (sorted(map(str, unrel), key=lambda p: (len(p), p)) if isinstance(unrel, list) else None), int(lim or 0)


def load_atlas_inputs(atl, unreliable=None, why=""):
    """What a method-v3 atlas ('tahoe_atlas.py effects') exports for the gene-level analyses, read by path:
    effects/composition_shift.parquet (sample, cell_line_id, shift_log2), effects/plate_scale.csv (plate, dose,
    n_wells, factor_raw, factor; factor_pass1 if present) and effects/drugdose.csv ('wells disagree' in flags,
    replicate_r, n_sig_genes). Returns {dir, version, shift, plate_scale, drugdose, dd_extra, notes, warnings,
    why, unreliable_plates, limit_files}; the tables are None when absent, or when the atlas effects are missing or
    older than method v3. Nothing is imported from a --limit-files trial build (its tables cover a few plates
    only). unreliable: this run's unreliable plates; when the atlas's differ, its plate factors and 'wells
    disagree' (fitted on other wells) are not imported and a warning says so (the composition shift is per
    profile and still holds). why: the reason when atl is None (e.g. '--atlas none')."""
    out = {"dir": os.path.abspath(atl) if atl else "", "version": atlas_effects_version(atl) if atl else 0,
           "shift": None, "plate_scale": None, "drugdose": None, "dd_extra": None, "notes": [], "warnings": [],
           "why": why if not atl else "", "unreliable_plates": None, "limit_files": 0}
    if not atl or out["version"] < METHOD_VERSION:
        return out
    out["unreliable_plates"], out["limit_files"] = atlas_build_info(atl)
    if out["limit_files"]:
        out["why"] = f"the atlas is a --limit-files {out['limit_files']} trial: nothing imported"
        out["warnings"].append(f"{atl} is a --limit-files {out['limit_files']} trial build: its composition "
                               "shifts, plate factors and 'wells disagree' are not imported")
        return out
    differ = unreliable is not None and out["unreliable_plates"] is not None and \
        sorted(map(str, unreliable)) != sorted(out["unreliable_plates"])
    if differ:
        out["warnings"].append(
            f"the atlas's unreliable plates ({', '.join(out['unreliable_plates']) or 'none'}) differ from this "
            f"run's ({', '.join(unreliable) or 'none'}): its plate factors and 'wells disagree' are not imported "
            "(fitted here instead), so MTAP / PSMD10 differ from the atlas's; run both with the same "
            "--unreliable-plates")
    fx = os.path.join(atl, "effects")

    def rd(name, fn):
        p = os.path.join(fx, name)
        if not os.path.exists(p):
            out["notes"].append(f"{name} missing")
            return None
        try:
            return fn(p)
        except Exception as e:  # noqa: BLE001
            out["notes"].append(f"{name} unreadable ({type(e).__name__}: {e})")
            return None
    out["shift"] = rd("composition_shift.parquet",
                      lambda p: pd.read_parquet(p, columns=["sample", "cell_line_id", "shift_log2"]))
    if not differ:
        out["plate_scale"] = rd("plate_scale.csv", lambda p: pd.read_csv(p, dtype={"plate": str, "dose": str}))
    dd = rd("drugdose.csv", lambda p: pd.read_csv(p, dtype={"drug": str}))
    if dd is not None and "drug" in dd:
        out["drugdose"] = dd
        flags = dd["flags"].fillna("").astype(str) if "flags" in dd else pd.Series("", index=dd.index)
        out["dd_extra"] = pd.DataFrame({
            "drug": dd["drug"].astype(str),
            "dose": (dd["dose"] if "dose" in dd else dd["conc"]).map(dose_text),
            "wells_disagree": flags.str.contains("wells disagree", regex=False),
            "replicate_r": pd.to_numeric(dd["replicate_r"], errors="coerce") if "replicate_r" in dd else np.nan})
        if differ:
            out["dd_extra"] = None
    return out


def composition_note(ax):
    """One line on the composition normalisation of this run (summary.txt, briefs, run_info.json)."""
    if ax.get("shift") is not None:
        return f"applied (median-of-ratios shift per well x line from {os.path.join(ax['dir'], 'effects')})"
    if ax.get("why"):
        why = ax["why"]
    elif not ax.get("version"):
        why = "atlas not computed"
    elif ax["version"] < METHOD_VERSION:
        why = f"atlas not computed with method v{METHOD_VERSION}: its effects are v{ax['version']}"
    else:
        why = "; ".join(ax.get("notes", [])) or "no composition table in the atlas"
    return f"composition normalisation not applied ({why})"


def plate_factor_text(M, cut=NOISY_PLATE):
    """'plate3 5 x2.04, plate2 0.5 x1.38' for the plate groups with a factor > cut."""
    t = M.factor_table
    if t is None or not len(t):
        return "none"
    hi = t[t["factor"] > cut].sort_values("factor", ascending=False)
    return ", ".join(f"{g.split('|')[0]} {g.split('|')[1]} uM x{f:.2f}" for g, f in zip(hi.index, hi["factor"])) \
        or f"none above {cut:g}"


def write_plate_scale(M, path):
    t = M.factor_table.copy() if M.factor_table is not None else pd.DataFrame()
    if len(t):
        t = t.rename_axis("group").reset_index()
        t["source"] = M.factor_source
    t.to_csv(path, index=False)
    return t


def write_plate_scale_by_gene(M, path):
    """results/plate_scale_by_gene.csv: per feature and plate group, the feature's own spread ratio, the group's
    factor and the z divisor it got (Method.factor_for), with the share of drug wells beyond |z| 1.96 before (group
    factor only) and after; a gene widened beyond its group shows where one plate is noisier for it alone."""
    rows = []
    for feat, t in M.feature_table.items():
        t = t.rename_axis("group").reset_index()
        t.insert(0, "feature", feat)
        rows.append(t)
    t = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    t.to_csv(path, index=False)
    return t


def write_run_info(path, **kw):
    """results/run_info.json: method version and the run's settings (tahoe_status.py reads method_version)."""
    info = {"method_version": METHOD_VERSION, "written": time.strftime("%Y-%m-%d %H:%M:%S"),
            "python": sys.version.split()[0]}
    info.update(kw)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(info, fh, indent=1, default=str)


def cmd_analyze(args):
    out = args.out
    res_dir = os.path.join(out, "results")
    os.makedirs(res_dir, exist_ok=True)
    for f in ("run_info.json", "summary.txt"):     # written last: a failed rerun never looks finished
        try:
            os.remove(os.path.join(res_dir, f))
        except FileNotFoundError:
            pass
    for f in ["well_line.parquet", "sample_map.csv"]:
        if not os.path.exists(os.path.join(out, f)):
            sys.exit(f"{f} not found in {out}; run the 'extract' step first")
    idx = discover(args.data, out)
    with open(os.path.join(out, "extract_info.json"), encoding="utf-8") as fh:
        info = json.load(fh)
    wl = pd.read_parquet(os.path.join(out, "well_line.parquet"))
    wl["sample"] = wl["sample"].astype(str)
    wl["cell_line_id"] = wl["cell_line_id"].astype(str)
    sm = pd.read_csv(os.path.join(out, "sample_map.csv"), dtype={"sample": str, "plate": str, "drug": str,
                                                                  "plate_num": str})
    sm["is_dmso"] = sm["is_dmso"].astype(bool)
    sm["well"] = sm["well"].fillna("")
    targets = info["targets"]
    cols_present = info["columns"]
    cl = load_cell_lines(idx)
    drugs = load_drugs(idx)
    S = []  # summary lines

    def say(s=""):
        S.append(s)

    failed = find_failed_wells(sm)
    failed[["sample", "plate", "well", "drug", "conc", "n_cells", "cells_log2_vs_plate"]].to_csv(
        os.path.join(res_dir, "excluded_failed_wells.csv"), index=False)
    if len(failed):
        log(f"Excluding {len(failed)} failed wells (almost no cells recovered; same drug fine elsewhere)")
        sm = sm[~sm["sample"].isin(failed["sample"])].reset_index(drop=True)
        wl = wl[wl["sample"].isin(sm["sample"])].reset_index(drop=True)
    unrel = unreliable_plates(sm, getattr(args, "unreliable_plates", None))
    sm = mark_unreliable(sm, unrel)
    if unrel:
        log(f"Unreliable plates (kept per well; left out of the reference spread, the plate-factor peers and the "
            f"drug-doses that also have a well elsewhere): {', '.join(unrel)}")
    atl = atlas_dir(args)
    ax = load_atlas_inputs(atl, unrel, "--atlas none" if atl is None else "")
    for w in ax["warnings"]:
        log(f"  WARNING: {w}")
    M = Method(sm, ax["shift"], ax["plate_scale"], ax["dd_extra"])
    comp_note = composition_note(ax)
    log(f"  composition: {comp_note}")

    log("Baseline by cell line ...")
    base, null_source = baseline_by_line(wl, sm, cl, targets, args.mtap_null)
    base.to_csv(os.path.join(res_dir, "baseline_by_cell_line.csv"))
    null_lines = list(base.index[base["MTAP_null"]])
    label = base.get("cell_name", pd.Series(base.index, index=base.index)).fillna("")
    label = pd.Series([n if n else i for i, n in zip(base.index, label)], index=base.index)

    log("Position passes and plate factors (method v3) ...")
    order = [g for g in ["PROTEASOME", "MTAP", "PSMD10"] if g in cols_present]
    for gene in order + [m for m in ("S_PHASE", "G2M_PHASE") if m in cols_present]:
        M.add(wl, gene, null_lines if gene == "MTAP" else [])
    M.complete()
    log(f"  plate factors {M.factor_source}; > {NOISY_PLATE:g}: {plate_factor_text(M)}")
    write_plate_scale(M, os.path.join(res_dir, "plate_scale.csv"))

    log("Well covariates ...")
    ctx = well_context(wl, sm, cols_present, M)

    log("Drug effects (corrected) ...")
    results, Ws, calibs = {}, {}, {}
    for gene in order:
        excl = null_lines if gene == "MTAP" else []
        extra = None
        if gene == "PSMD10" and "PROTEASOME" in Ws:
            extra = Ws["PROTEASOME"][["W2", "z"]].rename(columns={"W2": "PROTEASOME_log2FC", "z": "PROTEASOME_z"})
        res, W, _d, calib = expression_effects(wl, sm, gene, excl, ctx, drugs, extra, method=M)
        results[gene], Ws[gene], calibs[gene] = res, W, calib
        name = "Gankyrin_PSMD10" if gene == "PSMD10" else gene
        if gene in ("MTAP", "PSMD10"):
            res.sort_values("z_corrected", ascending=False).to_csv(
                os.path.join(res_dir, f"{name}_drug_effects_by_dose.csv"), index=False)
            drug_summary(res).to_csv(os.path.join(res_dir, f"{name}_drug_summary.csv"), index=False)
        else:
            res.sort_values("z_corrected", ascending=False).to_csv(
                os.path.join(res_dir, f"{name}_module_drug_effects_by_dose.csv"), index=False)
    write_plate_scale_by_gene(M, os.path.join(res_dir, "plate_scale_by_gene.csv"))
    pos = pd.concat([slot_table(Ws[g], g) for g in ["MTAP", "PSMD10"] if g in Ws])
    pos.to_csv(os.path.join(res_dir, "well_position_effects.csv"))
    plates = pd.concat([plate_table(Ws[g], g) for g in ["MTAP", "PSMD10"] if g in Ws])
    plates.to_csv(os.path.join(res_dir, "plate_dmso_offsets.csv"))

    failures = {}

    def attempt(label, fn):
        """Run one analysis; if it fails, log it and carry on with the others."""
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            log(f"  WARNING: {label} failed: {e!r}")
            failures[label] = repr(e)
            return None

    log("MTAP-null selective killing ...")
    n = attempt("abundance table", lambda: abundance(wl, sm, base))
    out_m = attempt("MTAP-null screen", lambda: mtap_null_screen(n, base, sm, drugs, ctx)) if n is not None else None
    mres, nl, il = (out_m[0], out_m[2], out_m[3]) if out_m else (None, [], [])
    if mres is not None:
        mres.to_csv(os.path.join(res_dir, "MTAP_null_selective_drugs.csv"), index=False)

    log("Gankyrin level vs drug response ...")
    out_g = attempt("Gankyrin level screen", lambda: gankyrin_level_screen(n, base, sm, drugs)) \
        if n is not None else None
    gres, n_g_lines = out_g if out_g else (None, 0)
    if gres is not None:
        gres.to_csv(os.path.join(res_dir, "Gankyrin_level_vs_drug_response.csv"), index=False)

    log("Cell cycle (DMSO cells) ...")
    cc = attempt("cell cycle", lambda: cell_cycle_by_line(out, base, cols_present))
    if cc is not None:
        cc.to_csv(os.path.join(res_dir, "cell_cycle_by_cell_line.csv"))

    # ------------------------------------------------------------------ summary
    log("Writing summary ...")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    pd.set_option("display.max_colwidth", 60)
    say("Tahoe-100M: MTAP and Gankyrin (PSMD10), artifact-corrected rebuild")
    say("=" * 72)
    say(f"Cells: {int(wl['n_cells'].sum()):,}   wells: {sm['sample'].nunique()}   plates: {sm['plate'].nunique()}"
        f"   cell lines: {wl['cell_line_id'].nunique()}   (files used: {info['n_files']}"
        + (f", TRIAL limited to {info['limit_files']} files" if info.get("limit_files") else "") + ")")
    say(f"Well position source: {info['well_position_source']}")
    say(f"Min cells per cell line per well: {MIN_CELLS}.  Drug call: FDR < {FDR_CUT}, >= {2 ** LFC_MIN:.1f}x "
        f"(median over cell lines), >= 60% of cell lines moving the same way.")
    say(f"Failed wells excluded (< 1/8 of the plate's usual cells while the same drug was fine elsewhere): "
        f"{len(failed)}" + (" -> " + ", ".join(f"{r.drug} {r.conc:g} ({r.plate} {r.well}, {int(r.n_cells)} cells)"
                                                for r in failed.itertuples()) if len(failed) else ""))
    say()
    say("1. CHECKS: do the known artifacts show up where they should?")
    say("-" * 72)
    for g in ["MTAP", "PSMD10"]:
        if g in Ws:
            t = pos[pos["gene"] == g].head(5)
            say(f"Top well positions for {g} (median plate-corrected log2 shift of all drugs at that position):")
            say(t[["median_effect_plate_corrected", "z_vs_other_positions", "n_wells", "drugs"]]
                .round(3).to_string())
            say()
    say("Earlier finding: MTAP artifact at H1, Gankyrin artifact at D10. If those wells are on top above,")
    say("the well positions are mapped correctly. If not, rerun with --layout pointing to the plate layout.")
    say()
    for g in ["MTAP", "PSMD10"]:
        if g in Ws:
            t = plates[plates["gene"] == g].head(4)
            say(f"Plates whose DMSO wells read lowest for {g} (offset > 0 inflated every DMSO-based fold change):")
            say(t[["dmso_offset", "n_dmso_wells", "dmso_wells"]].round(3).to_string())
            say()
    say("Calibration: share of wells with |z| > 1.96 (~5% expected if most drugs do nothing; the original")
    say("DE table had 32% of MTAP tests at p < 0.05) and |z| > 3 (0.3% expected; much more = heavy tails):")
    for g, c in calibs.items():
        say(f"  {g:11s} drug wells {c['pct_drug_wells_abs_z_gt_1.96']:.1f}% "
            f"({c['pct_drug_wells_abs_z_gt_1.96_unscaled']:.1f}% before the plate factors)   DMSO wells {c['pct_dmso_wells_abs_z_gt_1.96']:.1f}%   |z| > 3: "
            f"{c['pct_drug_wells_abs_z_gt_3']:.1f}%   (null spread {c['null_scale']:.3f} log2)")
    say()
    say(f"Method v{METHOD_VERSION} (README 'Method v3'):")
    say(f"  Unreliable plates: {', '.join(unrel) if unrel else 'none'} (--unreliable-plates; kept per well, left out "
        "of the reference spread, the plate-factor peers and every drug-dose that also has a well elsewhere; "
        "drug-doses only there are flagged 'unreliable plate only').")
    say(f"  Composition: {comp_note}.")
    for w in ax["warnings"]:
        say(f"  WARNING: {w}.")
    say(f"  Plate factors ({M.factor_source}; z divided by the factor, never below 1): > {NOISY_PLATE:g}: "
        f"{plate_factor_text(M)} (results/plate_scale.csv).")
    nc = ctx.loc[~sm.set_index("sample").reindex(ctx.index)["is_dmso"].astype(bool), "position_not_correctable"]
    ncw = sm.set_index("sample").reindex(nc.index[nc.astype(bool)])
    say(f"  Position correction: {int(nc.sum())} drug wells could not be corrected (< {MIN_SLOT_WELLS} other-drug "
        "wells at their position)" + (": " + ", ".join(sorted({f"{r.drug} {r.conc:g} ({r.well})" for r in
                                                                 ncw.itertuples()})[:8]) if len(ncw) else "")
        + "; per gene, wells left uncorrected because too few donors were clean (|z| < 3): "
        + ", ".join(f"{g} {c['wells_position_uncertain']}" for g, c in calibs.items()) + ".")
    say()
    say(f"2. BASELINE: MTAP-null cell lines ({null_source})")
    say("-" * 72)
    cols = [c for c in ["cell_name", "Organ", "n_cells_total", "MTAP_all_wells_vs_median_line",
                        "MTAP_cpm_all_wells", "MTAP_pct_cells_dmso", "CDKN2A_vs_median_line", "drivers"] if c in base]
    say(base.loc[base["MTAP_null"], cols].round(3).to_string() if null_lines else "  none called")
    say("Next-lowest MTAP lines:")
    say(base.loc[~base["MTAP_null"], cols].head(4).round(3).to_string())
    say()
    for g, title in [("MTAP", "3. DRUGS THAT CHANGE MTAP"), ("PSMD10", "4. DRUGS THAT CHANGE GANKYRIN (PSMD10)")]:
        if g not in results:
            continue
        say(title + (" (corrected; MTAP-null lines excluded)" if g == "MTAP" else " (corrected)"))
        say("-" * 72)
        sm_ = drug_summary(results[g])
        show = ["drug", "doses", "z_by_dose", "best_up_fold_change", "fdr_up_drug", "pct_lines_positive_at_best_up",
                "up_pattern", "up_flags"]
        say("Top 15 increases:")
        say(sm_.head(15)[show].round(3).to_string(index=False))
        say()
        dn = sm_.sort_values("best_down_z")
        show = ["drug", "doses", "z_by_dose", "best_down_fold_change", "fdr_down_drug",
                "pct_lines_negative_at_best_down", "down_pattern", "down_flags"]
        say("Top 10 decreases:")
        say(dn.head(10)[show].round(3).to_string(index=False))
        say()
        called_up = (results[g]["call"] == "up").sum()
        called_dn = (results[g]["call"] == "down").sum()
        say(f"Drug-dose combinations called: {called_up} up, {called_dn} down.")
        say("(pct_lines_* = % of cell lines moving in that direction at that dose; fold change = median line)")
        say()
    say("5. DRUGS NAMED EARLIER, before vs after correction (best dose for each)")
    say("-" * 72)
    for g in ["MTAP", "PSMD10"]:
        if g not in results:
            continue
        r = results[g]
        hit = r[r["drug"].str.lower().apply(lambda s: any(w.lower() in s for w in WATCH))]
        if hit.empty:
            continue
        best = hit.loc[hit["z_corrected"].fillna(-np.inf).groupby(hit["drug"]).idxmax()]
        say(f"{g}:")
        say(best[["drug", "conc", "log2FC_vs_DMSO_uncorrected", "log2FC_corrected", "z_corrected", "fdr_up",
                  "n_lines_up", "n_lines", "position_effect_removed", "plate_dmso_offset", "wells"]]
            .sort_values("z_corrected", ascending=False).round(3).to_string(index=False))
        say()
    say("6. DRUGS THAT SELECTIVELY DEPLETE MTAP-NULL LINES")
    say("-" * 72)
    if mres is not None:
        say(f"MTAP-null lines: {', '.join(label[c] for c in nl) or 'none'}; compared with {len(il)} "
            "MTAP-intact lines")
        say("in the same wells (log2 relative abundance vs the plate median; negative = null lines lost more).")
        show = [c for c in ["drug", "conc", "extra_log2_depletion_of_MTAP_null", "z_selective", "fdr_drug",
                            "z_by_dose", "dose_pattern", "delta_tissue_matched", "all_cells_log2_vs_plate",
                            "PRMT5_or_MAT2A_drug", "moa_fine"] if c in mres]
        say(mres.head(15)[show].round(3).to_string(index=False))
        pc_rows = mres[mres["PRMT5_or_MAT2A_drug"]]
        say("PRMT5/MAT2A drugs in the dataset (expected positive controls): "
            + (", ".join(sorted(set(pc_rows["drug"]))) if len(pc_rows) else "none found"))
    else:
        say("  failed: " + failures.get("MTAP-null screen", failures.get("abundance table", "")))
    say()
    say("7. DOES A LINE'S GANKYRIN LEVEL PREDICT DRUG RESPONSE?")
    say("-" * 72)
    if gres is not None:
        say(f"Spearman correlation across {n_g_lines} lines between untreated PSMD10 level and relative abundance")
        say("after the drug (partial = controlling for proliferation via the G2M score).")
        show = [c for c in ["drug", "conc", "rho", "rho_partial_G2M", "z_corrected", "fdr_drug", "z_by_dose",
                            "moa_fine"] if c in gres]
        say("Strongest 'high-Gankyrin lines depleted more':")
        say(gres.head(10)[show].round(3).to_string(index=False))
        say("Strongest 'high-Gankyrin lines spared':")
        say(gres.sort_values("z_corrected", ascending=False).head(5)[show].round(3).to_string(index=False))
    else:
        say("  failed: " + failures.get("Gankyrin level screen", failures.get("abundance table", "")))
    say()
    say("8. CO-REGULATION")
    say("-" * 72)
    if "PSMD10" in Ws and "PROTEASOME" in Ws:
        a = Ws["PSMD10"].loc[~Ws["PSMD10"]["is_dmso"], "W2"]
        b = Ws["PROTEASOME"]["W2"].reindex(a.index)
        say(f"Across all drug wells, Gankyrin vs rest-of-proteasome corrected shifts: Pearson r = {a.corr(b):.2f}, "
            f"Spearman = {a.rank().corr(b.rank()):.2f}")
    if "PSMD10" in Ws and "MTAP" in Ws:
        a = Ws["PSMD10"].loc[~Ws["PSMD10"]["is_dmso"], "W2"]
        b = Ws["MTAP"]["W2"].reindex(a.index)
        say(f"MTAP vs Gankyrin corrected shifts: Pearson r = {a.corr(b):.2f}")
    say("Genome-wide co-regulation: run the 'coreg' step (heavy, optional).")
    say()
    say("9. CELL CYCLE (untreated cells)")
    say("-" * 72)
    if cc is not None and len(cc):
        for g in ["PSMD10", "MTAP"]:
            col = f"{g}_log2_top_vs_bottom_G2M_PHASE_quartile"
            col2 = f"{g}_log2_top_vs_bottom_S_PHASE_quartile"
            say(f"{g}: G2M-high vs G2M-low cells, median log2 ratio across lines {cc[col].median():.2f} "
                f"(positive in {int((cc[col] > 0).sum())}/{cc[col].notna().sum()} lines); "
                f"S-high vs S-low {cc[col2].median():.2f}")
    else:
        say("  not available")
    say()
    say("Files in results/: see README_columns.txt")
    with open(os.path.join(res_dir, "summary.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(S) + "\n")
    with open(os.path.join(res_dir, "README_columns.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    write_run_info(os.path.join(res_dir, "run_info.json"), script=os.path.abspath(__file__),
                   data=os.path.abspath(args.data), out=os.path.abspath(out), min_cells=MIN_CELLS,
                   n_files=info.get("n_files"), limit_files=info.get("limit_files") or 0, unreliable_plates=unrel,
                   composition_normalisation=comp_note, plate_scale_source=M.factor_source,
                   plate_factors_above_1={g: round(float(f), 4) for g, f in (M.factors[2] or {}).items() if f > 1},
                   atlas=ax["dir"] or None, atlas_effects_version=ax["version"], failed_steps=failures)
    log(f"Done. Start with {os.path.join(res_dir, 'summary.txt')}")


README = """Extracted data (one folder up)
=============================
cells/*.parquet          One row per cell (~95M): barcode, sample (well), plate, drug, cell_line_id, n_genes,
                         total_counts, raw counts of MTAP, PSMD10, CDKN2A, CDKN2B, and summed counts of the
                         PROTEASOME, S_PHASE and G2M_PHASE gene sets. Query with duckdb or pyarrow.
well_line.csv / .parquet One row per well x cell line: cell count, summed counts, cells with >= 1 count (det_*).
sample_map.csv           One row per well: plate, drug, dose, well position, cells.
well_position_check.csv  Which barcode field gave the well position and how cleanly.
extracted_columns.json   Genes in each summed gene set.

Files in results/
=================
summary.txt                          Key checks and top results. Start here.
MTAP_drug_summary.csv                One row per drug: corrected MTAP effect at every dose.
MTAP_drug_effects_by_dose.csv        One row per drug and dose, all columns.
Gankyrin_PSMD10_drug_summary.csv     Same for Gankyrin.
Gankyrin_PSMD10_drug_effects_by_dose.csv
PROTEASOME_module_drug_effects_by_dose.csv   Same for the rest of the proteasome (sum of PSMA/PSMB/PSMC/PSMD
                                     subunits, excluding PSMD10 and chaperones); used to tell Gankyrin-specific
                                     changes from whole-proteasome changes.
MTAP_null_selective_drugs.csv        Drugs that deplete MTAP-null lines more than MTAP-intact lines in the same wells.
Gankyrin_level_vs_drug_response.csv  Drugs whose effect on a line's abundance tracks the line's Gankyrin level.
baseline_by_cell_line.csv            Untreated (DMSO) MTAP, PSMD10, CDKN2A, CDKN2B levels, % of cells expressing,
                                     MTAP-null call, organ, driver mutations.
cell_cycle_by_cell_line.csv          In untreated cells: Gankyrin and MTAP in G2M-/S-high vs -low cells.
well_position_effects.csv            Median shift of all drugs in each well position (the artifact being removed).
plate_dmso_offsets.csv               How far each plate's DMSO wells sit from the plate's drug-well median.
plate_scale.csv                      Plate dispersion groups (plate|dose): drug wells, peers (the same dose on other
                                     reliable plates), factor_raw (median over the genes/modules of the group's spread
                                     / its peers' median spread), factor = max(1, factor_raw), source (fitted here, or
                                     imported from the atlas).
plate_scale_by_gene.csv              Per gene / module and group: its own spread ratio, the group factor and the z
                                     divisor it got (factor = max(group factor, spread_ratio / 1.3): a gene noisier on
                                     a plate than the group's median gene is widened further, never narrowed), and
                                     the % of drug wells beyond |z| 1.96 with the group factor only and with its own.
run_info.json                        Method version (3) and the run's settings: unreliable plates, composition
                                     normalisation, plate-factor source.
excluded_failed_wells.csv            Wells that recovered < 1/8 of the plate's usual cells while the same drug was
                                     fine at the same or higher dose elsewhere: technical failures, left out of
                                     every analysis.
coregulation_summary.txt, coregulated_with_*.csv   (from the 'coreg' step) Genes whose drug responses track MTAP
                                     or Gankyrin across all drug wells. r_adjusted removes the top principal
                                     components first (broad responses such as transcription shutdown that move
                                     thousands of genes together; 3 by default, set with --pcs); r is before that
                                     adjustment. Strong real modules can also become components, so compare both.

Main columns (drug effect tables)
---------------------------------
log2FC_corrected       Effect after (method v3): plate baseline = median of the plate's drug wells for the same cell
                       line; minus the profile's composition shift (when the atlas exported it); median over cell
                       lines (a well needs >= 5 measured lines, as in the atlas; a gene measured in fewer lines in a
                       typical well, e.g. one carried by 4 lines in most wells: one); minus the leave-drug-out
                       well-position effect (second pass: only donor wells whose own first-pass |z| < 3 for this
                       gene). Mean over the drug-dose's used wells (below).
fold_change            2 ** log2FC_corrected.
z_corrected            log2FC_corrected scored against the spread of the drug wells on reliable plates (robust z;
                       median/MAD), divided by the gene's plate factor of the well's plate x dose group
                       (plate_scale_gene: the group's factor, plate_scale, or more where this gene alone is noisier
                       on that plate; results/plate_scale_by_gene.csv).
                       Combined across plates (Stouffer) when a drug and dose was on several plates.
used wells             A drug-dose with a well on a reliable plate uses only those wells (means, Stouffer, counts);
                       one with wells only on unreliable plates (--unreliable-plates; default plate13) keeps them and
                       is flagged 'unreliable plate only'. n_wells_left_out_unreliable counts the wells left out.
fdr_up, fdr_down       Benjamini-Hochberg over all drug-dose combinations, one-sided.
n_lines_up             Cell lines (counted once) with a per-line z > 2 and > 1.2x. n_lines = lines measured.
frac_lines_positive    Share of cell lines whose corrected change is above zero (frac_lines_negative: below).
call                   up/down when FDR < 0.10, median change >= 1.2x, and >= 60% of lines move that way.
flags                  toxic: the drug-dose kept < half the plate's typical cells, also < half of its plate row's
                         where that row is itself shifted (|row_cells_log2| > 0.8); with several used wells, its BEST
                         one lost cells too (cells_log2_best_well < -0.5); and no higher dose of the drug kept
                         >= half: dose-consistent cell loss. Otherwise < half the cells = 'low cells (technical?)':
                         not confirmed (a row that lost cells, a lower dose killing more than a higher one, as
                         antimitotics do, or one well of several). At the top dose 'toxic' rests on one well's cell
                         count when the drug-dose has one well, and duplicate wells of the real data do not agree on
                         cell loss: weak evidence alone.
                       plate-row cell shift: the plate row itself lost or gained cells (|row_cells_log2| > 0.8) or
                         UMIs per cell (row_umi_per_cell_log2 < -0.4): a technical row effect.
                       transcription drop: genes per cell -0.3 log2 or UMIs per cell -0.5 log2 vs the plate, and also
                         vs the plate row; relative mRNA levels can rise artificially.
                       cell-cycle shift: S_PHASE or G2M_PHASE module changed > 1.41x (> 1.19x with |z| >= 4).
                       composition shift: |composition_shift_log2| >= 0.2: a few genes took a large share of the
                         reads; the effects are relative to the median gene (the raw CPM view would differ).
                       noisy plate (z scaled): plate_scale (or plate_scale_gene) > 1.2: the z was divided by it.
                       unreliable plate only: every well of the drug-dose sits on an unreliable plate.
                       whole proteasome up/down: rest of the proteasome moved the same way (Gankyrin not specific).
                       position not correctable: a used well had < 3 other-drug wells at its position (no correction).
                       position correction uncertain: a used well had < 3 clean donor wells for this gene (left
                         uncorrected): a strong drug may share the position; check sample_map.csv.
                       position effect removed: the correction moved the estimate by > 0.2 log2.
                       wells disagree: imported from the atlas (its wells' genome-wide signatures do not agree).
log2FC_vs_DMSO_uncorrected   The old-style estimate (against the plate's DMSO wells, no position correction).
position_effect_removed      Leave-drug-out median of other drugs in the same well position (second pass).
position_effect_pass1  The same from every other-drug well (first pass, before the clean-donor rule).
position_wells_used, position_clean_donors   Other-drug wells at the position in total, and those clean for the gene.
plate_dmso_offset      > 0: this plate's DMSO wells read low, which inflated every DMSO-based fold change on it
                       (a column only: it never changes the corrected values).
plate_scale            Mean plate factor of the used wells (results/plate_scale.csv); plate_scale_gene: the mean z
                       divisor of this gene (results/plate_scale_by_gene.csv).
composition_shift_log2 Mean over the used wells of the well's median composition shift over its lines.
row_cells_log2, row_umi_per_cell_log2, row_genes_per_cell_log2   The plate row's other drug wells (median).
pct_cells_expressing_change  Change in % of cells with >= 1 count (corrected). With level_in_expressing_cells_log2
                       this tells a shift in every cell from a change in the fraction of expressing cells.
PROTEASOME_log2FC, PROTEASOME_z   Rest-of-proteasome change in the same wells (Gankyrin tables).
S_PHASE_shift_log2, G2M_PHASE_shift_log2   Corrected change of the cell-cycle modules.
cells_log2_vs_plate    log2 cells recovered in the well vs the plate's typical drug well (mean over used wells).
cells_log2_best_well   The used well with the least cell loss, after subtracting its plate row's median where that
                       row is shifted by > 0.8 log2 (else the plain value): 'toxic' needs it < -0.5 (a used well
                       that kept its cells: the loss did not replicate).
Drug summary: z_by_dose / log2FC_by_dose list doses in ascending order; up_pattern describes the dose behaviour
                       ('top dose only', 'rises with dose', 'all doses, stronger at high dose', 'all doses, flat',
                       'inconsistent across doses'). A real effect usually grows with dose; a significant result
                       at one low dose only deserves suspicion.
                       p/fdr_*_drug: best dose, Bonferroni over doses, then Benjamini-Hochberg over drugs.

MTAP_null_selective_drugs.csv
-----------------------------
extra_log2_depletion_of_MTAP_null   Mean log2 relative abundance of MTAP-null lines minus the median of
                       MTAP-intact lines in the same well, after position correction. Negative = selective.
z_selective            Scored against the spread across wells (reliable plates) plus each well's own counting noise,
                       so wells with few surviving cells cannot produce extreme scores. Per drug-dose over its used
                       wells (unreliable_plate_only, n_wells_left_out_unreliable as in the drug-effect tables).
delta_tissue_matched   Same, comparing only with intact lines of the same organ.
intact_median_log2     Typical intact-line change (relative to the well), all_cells_log2_vs_plate = overall kill.
<line>_log2            Each MTAP-null line separately.
PRMT5_or_MAT2A_drug    Positive controls if present (MTAP loss makes cells depend on PRMT5/MAT2A).
z_by_dose, dose_pattern, fdr_drug   The drug's z at every dose (ascending), how depletion behaves with dose,
                       and a drug-level FDR (best dose, Bonferroni over doses, Benjamini-Hochberg over drugs).

Gankyrin_level_vs_drug_response.csv
-----------------------------------
rho                    Spearman correlation across lines: untreated PSMD10 level vs relative abundance after drug.
rho_partial_G2M        Same, controlling for proliferation (G2M score), since fast-growing lines differ in both.
z_corrected            Fisher-transformed rho, position-corrected, scored against all drug wells.
z_by_dose, fdr_drug    As above. Lineage is a confounder here: check whether a hit is driven by one tissue.
"""


# ============================================================================= coreg
def cmd_coreg(args):
    try:
        import duckdb
    except ImportError:
        sys.exit("coreg needs duckdb:  pip install duckdb")
    out = args.out
    res_dir = os.path.join(out, "results")
    os.makedirs(res_dir, exist_ok=True)
    cache = os.path.join(out, "coreg_matrix.npz")
    if os.path.exists(cache) and not args.reindex:
        log("Using the saved well x gene matrix (coreg_matrix.npz); add --reindex to rebuild it")
        z = np.load(cache, allow_pickle=False)
        wk = pd.DataFrame({"drug": z["drug"], "conc": z["conc"], "plate_num": z["plate_num"]})
        coreg_from_matrix(z["X"], z["genes"], wk, res_dir, failed_well_keys(out))
        return
    idx = discover(args.data, out)
    files = idx["pseudobulk"]
    if not files:
        sys.exit("No pseudobulk differential expression files found")
    smp = os.path.join(out, "sample_map.csv")
    if not os.path.exists(smp):
        sys.exit("sample_map.csv not found; run 'extract' first (it provides the well positions)")
    sm = pd.read_csv(smp, dtype={"plate_num": str, "drug": str})
    sm = sm[~sm["is_dmso"].astype(bool) & sm["slot"].notna()]
    wells = pd.DataFrame({"drug": sm["drug"], "conc": sm["conc"].round(4),
                          "plate_num": sm["plate_num"].astype(str), "slot": sm["slot"].astype(int)})
    mem = mem_available_gb()
    con = duckdb.connect()
    tmp = os.path.join(out, "duckdb_tmp")
    os.makedirs(tmp, exist_ok=True)
    con.execute(f"SET temp_directory='{tmp}'")
    if mem:
        con.execute(f"SET memory_limit='{max(2, int(mem * 0.6))}GB'")
    con.register("wells_df", wells)
    con.execute("CREATE TABLE wells AS SELECT * FROM wells_df")
    log(f"Averaging log2 fold changes per gene and well across cell lines ({len(files)} files; slow) ...")
    flist = "[" + ",".join("'" + f.replace("'", "''") + "'" for f in files) + "]"
    con.execute(f"""
        CREATE TABLE wg AS
        SELECT gene_name, drug, round(CAST(concentration AS DOUBLE), 4) AS conc,
               regexp_extract(plate, '([0-9]+)', 1) AS plate_num,
               avg(greatest(least(log2FoldChange, 5), -5)) AS lfc
        FROM read_parquet({flist})
        WHERE log2FoldChange IS NOT NULL AND isfinite(log2FoldChange) AND baseMean >= {MIN_BASEMEAN}
        GROUP BY 1, 2, 3, 4
    """)
    log("Correcting for plate and well position ...")
    con.execute("""
        CREATE TABLE r1 AS
        SELECT wg.gene_name, wg.drug, wg.conc, wg.plate_num, w.slot,
               wg.lfc - median(wg.lfc) OVER (PARTITION BY wg.gene_name, wg.plate_num) AS r1
        FROM wg JOIN wells w ON wg.drug = w.drug AND wg.conc = w.conc AND wg.plate_num = w.plate_num
    """)
    con.execute("""
        CREATE TABLE res AS
        SELECT gene_name, drug, conc, plate_num,
               r1 - median(r1) OVER (PARTITION BY gene_name, slot) AS res
        FROM r1
    """)
    n_matched = con.execute("SELECT count(*) FROM (SELECT DISTINCT drug, conc, plate_num FROM res)").fetchone()[0]
    log(f"  {n_matched} drug wells matched to well positions")
    log("Building the well x gene matrix ...")
    con.execute("""CREATE TABLE wid AS SELECT (row_number() OVER (ORDER BY drug, conc, plate_num)) - 1 AS wid,
                   drug, conc, plate_num FROM (SELECT DISTINCT drug, conc, plate_num FROM res)""")
    con.execute("""CREATE TABLE gid AS SELECT (row_number() OVER (ORDER BY gene_name)) - 1 AS gid, gene_name
                   FROM (SELECT DISTINCT gene_name FROM res)""")
    arr = con.execute("""SELECT g.gid, w.wid, r.res FROM res r
                         JOIN gid g ON r.gene_name = g.gene_name
                         JOIN wid w ON r.drug = w.drug AND r.conc = w.conc AND r.plate_num = w.plate_num""").fetchnumpy()
    genes = np.array([str(x) for x in con.execute("SELECT gene_name FROM gid ORDER BY gid").fetchnumpy()["gene_name"]])
    wk = con.execute("SELECT drug, conc, plate_num FROM wid ORDER BY wid").fetchdf()
    X = np.full((len(genes), len(wk)), np.nan, dtype=np.float32)
    X[np.asarray(arr["gid"], dtype=np.int64), np.asarray(arr["wid"], dtype=np.int64)] = np.asarray(arr["res"])
    con.close()
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    np.savez_compressed(cache, X=X, genes=np.array([str(g) for g in genes], dtype=str),
                        drug=np.array([str(d) for d in wk["drug"]], dtype=str),
                        conc=wk["conc"].to_numpy(dtype=float),
                        plate_num=np.array([str(p) for p in wk["plate_num"]], dtype=str))
    coreg_from_matrix(X, genes, wk, res_dir, failed_well_keys(out))


def failed_well_keys(out):
    """(drug, dose, plate number) of the failed wells, so co-regulation leaves them out too."""
    smp = os.path.join(out, "sample_map.csv")
    if not os.path.exists(smp):
        return set()
    sm = pd.read_csv(smp, dtype={"sample": str, "plate": str, "drug": str})
    sm["is_dmso"] = sm["is_dmso"].astype(bool)
    fw = find_failed_wells(sm)
    nums = fw["plate"].astype(str).str.extract(r"(\d+)", expand=False)
    return {(str(d), round(float(c), 4), str(p)) for d, c, p in zip(fw["drug"], fw["conc"], nums)}


def coreg_from_matrix(X, genes, wk, res_dir, drop=frozenset()):
    """Correlate every gene with MTAP and PSMD10 across drug wells, before and after removing the broad
    responses shared by thousands of genes (top principal components: e.g. transcription shutdown)."""
    wk = wk.reset_index(drop=True)
    use = np.array([(str(d), round(float(c), 4), str(p)) not in drop
                    for d, c, p in zip(wk["drug"], wk["conc"], wk["plate_num"])])
    if (~use).any():
        log(f"Leaving out {int((~use).sum())} failed wells")
    X = X[:, use]
    wk = wk[use].reset_index(drop=True)
    keep = np.isfinite(X).mean(axis=1) >= 0.9
    genes = np.asarray(genes)[keep]
    Z = np.where(np.isfinite(X[keep]), X[keep], 0).astype(np.float32)
    Z -= Z.mean(axis=1, keepdims=True)
    sd = Z.std(axis=1, keepdims=True)
    sd[sd == 0] = 1
    Z /= sd
    log(f"Principal components of {Z.shape[0]:,} genes x {Z.shape[1]:,} drug wells ...")
    U, Sv, Vt = np.linalg.svd(Z, full_matrices=False)
    k = min(N_PCS, len(Sv) - 1)
    Zr = Z - (U[:, :k] * Sv[:k]) @ Vt[:k]
    k10 = min(10, len(Sv) - 1)
    Zr10 = Z - (U[:, :k10] * Sv[:k10]) @ Vt[:k10]     # stricter version, as a sensitivity check
    var = Sv ** 2 / (Sv ** 2).sum()
    labels = [f"{d} {c:g} (plate {p})" for d, c, p in zip(wk["drug"], wk["conc"], wk["plate_num"])]

    def corr_with(M, v):
        nv = np.linalg.norm(v)
        nm = np.linalg.norm(M, axis=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            return (M @ v) / (nm * nv)

    S = ["Genome-wide co-regulation",
         "Per drug well: published pseudobulk log2FC averaged over cell lines, corrected for plate and well position.",
         f"r = Pearson correlation across {Z.shape[1]:,} drug wells. r_adjusted = the same after removing the top {k}",
         "principal components, i.e. broad responses shared by thousands of genes (e.g. transcription or",
         "translation shutdown, proliferation), which otherwise dominate every gene's partner list.", "=" * 72,
         "\nTop components removed (share of variance): " + ", ".join(f"PC{i + 1} {100 * var[i]:.1f}%" for i in range(k))]
    for j in range(3):
        order = np.argsort(Vt[j])
        S.append(f"PC{j + 1} ({100 * var[j]:.1f}%): drug wells at one end: "
                 + "; ".join(labels[i] for i in order[:5]))
        S.append("      other end: " + "; ".join(labels[i] for i in order[::-1][:5]))
        go = np.argsort(U[:, j])
        S.append("      genes: " + ", ".join(genes[go[:8]]) + "  <->  " + ", ".join(genes[go[::-1][:8]]))
    for target in ["MTAP", "PSMD10"]:
        hit = np.flatnonzero(genes == target)
        if not hit.size:
            S.append(f"\n{target}: not measured in enough wells")
            continue
        i = int(hit[0])
        df = pd.DataFrame({"gene_name": genes, "r_adjusted": corr_with(Zr, Zr[i]), "r": corr_with(Z, Z[i]),
                           "r_adjusted_10pcs": corr_with(Zr10, Zr10[i])})
        df = df[df["gene_name"] != target].sort_values("r_adjusted", ascending=False).reset_index(drop=True)
        df["rank_pct_adjusted"] = (np.arange(len(df)) + 1) / len(df) * 100
        df["rank_pct_10pcs"] = df["r_adjusted_10pcs"].rank(ascending=False, pct=True) * 100
        df["proteasome_gene"] = df["gene_name"].str.match(PROTEASOME_RE.pattern)
        name = "Gankyrin_PSMD10" if target == "PSMD10" else target
        df.to_csv(os.path.join(res_dir, f"coregulated_with_{name}.csv"), index=False)
        S.append(f"\n{target}: {len(df):,} genes")
        S.append("Most positively co-regulated (after removing broad responses):")
        S.append(df.head(25)[["gene_name", "r_adjusted", "r"]].round(3).to_string(index=False))
        S.append("Most negatively co-regulated:")
        S.append(df.tail(10)[["gene_name", "r_adjusted", "r"]].round(3).to_string(index=False))
        raw = df.sort_values("r", ascending=False)
        S.append("Before removing broad responses, the top partners were: " + ", ".join(raw["gene_name"].head(10)))
        strict = df.sort_values("r_adjusted_10pcs", ascending=False)
        S.append(f"With {k10} components removed (stricter check), the top partners are: "
                 + ", ".join(strict["gene_name"].head(15)))
        p = df[df["proteasome_gene"]]
        if len(p):
            rr = raw["r"].rank(ascending=False, pct=True) * 100
            S.append(f"Proteasome subunits ({len(p)} genes): median rank percentile {p['rank_pct_adjusted'].median():.1f} "
                     f"after adjustment, {rr[p.index].median():.1f} before, {p['rank_pct_10pcs'].median():.1f} with "
                     f"{k10} components removed (near 0 = move together with {target})")
    with open(os.path.join(res_dir, "coregulation_summary.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(S) + "\n")
    log("Done: results/coregulation_summary.txt and results/coregulated_with_*.csv")


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["extract", "analyze", "all", "coreg"])
    ap.add_argument("--data", default=".", help="Tahoe-100M download folder (default: current folder)")
    ap.add_argument("--out", default=None, help="output folder (default: <data>/mtap_gankyrin)")
    ap.add_argument("--workers", type=int, default=0, help="parallel processes for extract (default: auto)")
    ap.add_argument("--batch-size", type=int, default=20000, help="cells per batch per worker")
    ap.add_argument("--limit-files", type=int, default=0, help="trial run on the first N expression files")
    ap.add_argument("--layout", default=None, help="CSV with columns sample,well to override well positions")
    ap.add_argument("--mtap-null", default=None, help="comma-separated cell lines to treat as MTAP-null")
    ap.add_argument("--extra-genes", default="", help="comma-separated extra genes to extract per cell")
    ap.add_argument("--min-cells", type=int, default=MIN_CELLS, help="min cells per line per well")
    ap.add_argument("--unreliable-plates", default=None,
                    help="plates kept per well but left out of pooled drug-doses, comma-separated, or 'none' "
                         f"(default: {', '.join(UNRELIABLE_PLATES)} when present)")
    ap.add_argument("--atlas", default=None, help="computed atlas (method v3) whose composition shift and plate "
                                                  "factors to use (default: <data>/atlas when there; 'none')")
    ap.add_argument("--reindex", action="store_true", help="rescan the download folder (coreg: rebuild its matrix)")
    ap.add_argument("--pcs", type=int, default=N_PCS, help="coreg: broad components to remove (default 3)")
    args = ap.parse_args()
    args.out = args.out or os.path.join(args.data, "mtap_gankyrin")
    args.extra_genes = [g.strip() for g in args.extra_genes.split(",") if g.strip()]
    globals()["MIN_CELLS"] = args.min_cells
    globals()["N_PCS"] = args.pcs
    start_run_log(os.path.join(args.out, "mtap_gankyrin.log"), "tahoe_mtap_gankyrin.py " + " ".join(sys.argv[1:]))
    try:
        with keep_awake(f"tahoe_mtap_gankyrin.py {args.command}"):
            if args.command in ("extract", "all"):
                cmd_extract(args)
            if args.command in ("analyze", "all"):
                cmd_analyze(args)
            if args.command == "coreg":
                cmd_coreg(args)
    except SystemExit as e:
        log_exit(e)
        raise


if __name__ == "__main__":
    main()
