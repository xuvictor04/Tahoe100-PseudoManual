"""tlib - the shared library part of the old tahoe_mtap_gankyrin.py that the build and the effects need.

Ported verbatim (function by function, by syntax tree) from tahoe_mtap_gankyrin.py at commit 28cd834 of
xuvictor04/Tahoe100-PseudoManual (branch claude/tahoe100m-gene-pipeline-lodlx7). Do not edit the copied bodies by
hand: tests/test_port.py checks that they still match the method they came from. New code goes in other modules.
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

DMSO_PREFIX = "DMSO"            # DMSO_TF marks vehicle controls


MIN_CELLS = 30                  # min cells of one cell line in one well to use its expression


LFC_MIN = math.log2(1.2)        # min log2 fold change to count a cell line or call a drug (1.2x)


NULL_FRAC = 0.30                # MTAP-null fallback cut (fraction of the median line, all wells); see null_threshold


MIN_LINE_CELLS = 200            # lines with fewer cells in total are not classified


MIN_SLOT_WELLS = 3              # need >= this many other-drug wells to estimate a position effect


MIN_LINES = 5                   # a well's effect on a gene needs >= this many measured lines (as tahoe_atlas.py; a


METHOD_VERSION = 3              # results/run_info.json; tahoe_gene_panel.py needs >= 3, tahoe_status.py reads it


UNRELIABLE_PLATES = ("plate13",)  # default --unreliable-plates (when present): its wells stay in the per-well


POS_CLEAN_Z = 3.0               # position correction, pass 2: donor wells only with |first-pass z| < this (per gene)


PLATE_SCALE_MIN_WELLS = 20      # a (plate, dose) group with fewer drug wells joins its plate's largest group


NOISY_PLATE = 1.2               # flag 'noisy plate (z scaled)' above this plate factor


PLATE_SCALE_BAND = 1.3          # a gene whose own spread ratio on a plate group exceeds the group factor x this (about


ROW_SHIFT = 0.8                 # a plate row whose other drug wells moved by more (log2 cells) is itself shifted


TOXIC_BEST_WELL = -0.5          # 'toxic' of a drug-dose with several used wells: its best well lost cells too (log2)


COMPOSITION_FLAG = 0.2          # flag 'composition shift' at |drug-dose composition shift| >= this (log2)


S_GENES = """MCM5 PCNA TYMS FEN1 MCM2 MCM4 RRM1 UNG GINS2 MCM6 CDCA7 DTL PRIM1 UHRF1 MLF1IP CENPU
HELLS RFC2 RPA2 NASP RAD51AP1 GMNN WDR76 SLBP CCNE2 UBR7 POLD3 MSH2 ATAD2 RAD51 RRM2 CDC45 CDC6
EXO1 TIPIN DSCC1 BLM CASP8AP2 USP1 CLSPN POLA1 CHAF1B BRIP1 E2F8""".split()


G2M_GENES = """HMGB2 CDK1 NUSAP1 UBE2C BIRC5 TPX2 TOP2A NDC80 CKS2 NUF2 CKS1B MKI67 TMPO CENPF TACC3
FAM64A PIMREG SMC4 CCNB2 CKAP2L CKAP2 AURKB BUB1 KIF11 ANP32E TUBB4B GTSE1 KIF20B HJURP CDCA3 HN1
JPT1 CDC20 TTK CDC25C KIF2C RANGAP1 NCAPD2 DLGAP5 CDCA2 CDCA8 ECT2 KIF23 HMMR AURKA PSRC1 ANLN LBR
CKAP5 CENPE CTCF NEK2 G2E3 GAS2L3 CBX5 CENPA""".split()


PROTEASOME_RE = re.compile(r"^(PSMA[1-7]|PSMB[1-7]|PSMC[1-6]|PSMD[1-9]|PSMD1[0-4])$")


PROTEASOME_EXCLUDE = {"PSMD5", "PSMD9", "PSMD10"}  # assembly chaperones; PSMD10 is Gankyrin itself


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


REINDEX_HINT = " (if the download finished after an earlier run, add --reindex)"


def data_parquets(data_abs, out_dir):
    """Every parquet file under data_abs except the outputs of these scripts: out_dir and every folder below
    data_abs that holds a file_index.json (mtap_gankyrin/, gene_panel/, atlas/, trial folders) or a .not_tahoe_input
    marker (mg53_p53/run_mg53_p53.py's output folder)."""
    def norm(p):
        return os.path.normcase(os.path.abspath(p))

    skip = [norm(out_dir) + os.sep]
    for f in (glob.glob(os.path.join(data_abs, "**", "file_index.json"), recursive=True)
              + glob.glob(os.path.join(data_abs, "**", ".not_tahoe_input"), recursive=True)):
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


def dose_text(v):
    """A dose as dose_key writes it ('0.05', '5'); other labels unchanged."""
    try:
        return f"{float(v):.6g}"
    except (TypeError, ValueError):
        return str(v)


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


def salt_base(name):
    """A drug name without its trailing salt / form in brackets ('Topotecan (hydrochloride)' -> 'Topotecan';
    one level of nested brackets, '(R)-Verapamil (hydrochloride)' -> '(R)-Verapamil'): the drugs listed twice as
    salt forms share it."""
    return re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)\s*$", "", str(name)).strip()


def dose_key(sm):
    """String key for a dose; falls back to the plate when the dose is unknown."""
    return pd.Series([f"{c:.6g}" if np.isfinite(c) else f"plate:{p}"
                      for c, p in zip(sm["conc"].astype(float), sm["plate"])], index=sm.index)


def fmt_list(vals, fmt="{:.2f}"):
    return " / ".join("NA" if not np.isfinite(v) else fmt.format(v) for v in vals)


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


def is_toxic(cells, row, best_well=float("nan"), higher_keeps=False):
    """'toxic' (method v3, one definition with tahoe_atlas.flags_for): the drug-dose's mean cell count is < -1 log2
    vs the plate, also beyond its plate row where that row is itself shifted (cells_beyond_row), its best used well
    lost cells too (best_well = the largest cells_beyond_row of the used wells < TOXIC_BEST_WELL: a well of several
    that kept its cells means the loss did not replicate; NaN: not known), and no higher dose of the drug keeps
    >= half the plate's cells. For a drug-dose of one well this is: its loss beyond a shifted row < -1."""
    if not cells < -1 or not float(cells_beyond_row(cells, row)) < -1 or higher_keeps:
        return False
    return not (math.isfinite(best_well) and best_well >= TOXIC_BEST_WELL)


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
