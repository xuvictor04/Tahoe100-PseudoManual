#!/usr/bin/env python3
"""The data behind the MG53 (TRIM72) analysis as plain tables: cell lines, drugs, wells, doses, and per (plate, well,
drug, concentration, cell line) the raw counts, the uncorrected log2 changes and the method-v3 corrected effect of
TRIM72, of the genes the data tie to it upstream and downstream, and (by default) of every expressed atlas gene.
Tahoe-100M only (no new data); nothing is downloaded. mRNA 24 h after treatment.

Every value comes from <data>/atlas (the pseudobulk counts and the method-v3 effects); nothing is re-estimated:
  raw          n_cells, the gene's UMI count and the profile's total UMIs (summed over that line's cells in that well),
               CPM, log2 CPM with the atlas's pseudocount: log2((count + 0.5) / (total + 1) x 1e6)
  uncorrected  u_dmso       = log2 CPM - the same line's pooled DMSO wells on the same plate (Tahoe's own reference;
                              the atlas found DMSO wells offset from the plate's drug median: plate_offset)
               u_drugmedian = log2 CPM - the same line's median over the plate's drug wells (the method's r1, before the
                              composition and position corrections)
  corrections  composition_shift (per profile, atlas composition_shift.parquet), position_effect (the atlas's W1 - W2
               of the gene in that well), posunc (atlas: position correction uncertain)
  corrected    r2 = u_drugmedian - composition_shift - position_effect (wells whose W1 has < MIN_LINES lines: none),
               as upstream_tf.plate_r2 computes it: the same value as genome_wide's per (well x line) tensor
Per (plate, line), u_dmso - u_drugmedian = drug_median_log2cpm - dmso_log2cpm (all_genes/plate_baselines), the same in
every well of the plate; the atlas's plate_offset is the median over lines of that difference.
Checked inside the step (checks.csv): the median over lines of u_drugmedian - composition_shift = atlas W1 per plate,
the median over lines of r2 = atlas W2, its drug-dose mean = DD_lfc, the median over lines of (drug-well median -
pooled DMSO level) = atlas plate_offset, r2 = genome_wide's tensor when that cache is present and valid.

What is exported and why (curated lists never decide it; they appear only as labelled overlays):
  metadata/    cell_lines.csv, drugs.csv, wells.csv (used or excluded, and why), drug_doses.csv, plates.csv
  <GENE>/      the exposure (TRIM72; $MG53_GW_EXPOSURE overrides it, as genome_wide): every profile (CSV), per well,
               per (drug-dose, line), per drug-dose, and drug-dose x line matrices (corrected and uncorrected)
  upstream/    TRIM72 per drug-dose (with the drug metadata and the upstream_coregulation readthrough index when that
               step's tables exist), per (drug-dose, line), line traits; the genes the data tie to TRIM72: genome_wide's
               common-slope screen (q < 0.1, and the top 200 by |t|), the co-regulation partners of
               upstream_coregulation
               (a_top_partners), and the locus genes chosen by genomic geometry (FUS, PYCARD-AS1 through the extra-gene
               path, ITGAM), each with its per-profile values and the reason it is there
  downstream/  genome_wide's Tahoe p53 program (P, P-down, with their FALLBACK flags) and screen hits (q < 0.1 for the
               common slope or WT minus altered), each with its values and reason; per-profile program scores;
               overlay/: the curated sets (panel P53_ACTIVITY, gene_modules.csv, CollecTRI if cached), labelled overlay
  all_genes/   every expressed atlas gene at the per-profile level (Parquet, gene chunks, an index gene -> file), with
               per drug-dose and per (plate, line) baseline tables; on by default (--no-all-genes or
               MG53_EXPORT_ALL_GENES=0 turns it off: ~21 GB on the real data)
  tahoe_deseq2/ Tahoe's own pseudobulk DESeq2 rows (drug vs the plate's DMSO) for TRIM72 and the genes above, when
               <data>/metadata/pseudobulk_differential_expression is present (setup --mode full); else a note
  README.md (every file and column, with units), checks.csv, export_info.json, run_info.json (timings; not compared)

    python3 export_data.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--gene TRIM72]
                           [--no-all-genes] [--chunk 256] [--locus-genes FUS,PYCARD-AS1,ITGAM] [--coreg-dir DIR]
                           [--gw-dir DIR] [--redo]
    python3 export_genes.py --export <out> --genes TRIM72,FUS --out x.csv     (any genes' rows as CSV, from all_genes)

Output: $MG53_OUT (run_mg53_p53.py sets <out>/export), else <data>/mg53_p53/export. Inputs: <data>/atlas (effects and
pseudobulk: one streamed pass of ~20 GB), <data>/metadata, <data>/gene_panel/results (TP53 groups), and the sibling
steps' tables next to the output folder (genome_wide, upstream_coregulation) when present. Nothing is written under
<data>/atlas or <data>/gene_panel. Resumable: each part is marked done in <out>/.state keyed to the data folder and its
inputs and to its files (a part whose files were deleted is rebuilt); all_genes chunks are written one by one through
temporary files; the pass's counts cache (<out>/.cache) is deleted when the gene store is complete. When genome_wide has
not finished (or finished for another exposure, or its tables name other genes than this atlas), everything that does
not need it is written, README.md says what is missing, and the step still succeeds. Disk on the real data (measured
with the step's own writers on simulated real-size arrays: 17.1 bytes per per-profile row): all_genes ~21 GB (per
profile ~19, per drug-dose 1.4, plate baselines 0.2), ~4.6 GB of temporary counts during the build (+4.6 GB when
genome_wide's tensor is absent), ~3.9 MB per selected gene and folder in upstream/ and downstream/, ~3.2 MB per gene of
DESeq2 rows. The free disk is checked before anything is written, for the peak of what this run still writes (a resumed
run counts only the missing chunks; what it deletes first is credited): ~27-29 GB for ~1,000 selected-gene entries.
Memory: ~2-3 GB in the pass (one or two plates of counts: 2.0-2.2 GB measured for one plate), ~1-2.4 GB while writing.
Time (4 CPUs; kernels timed at the real dimensions): the pass ~8-15 min (3-4 min of compute, +1.5 min without
genome_wide's tensor, the rest reading 20 GB), the all_genes Parquet ~16-18 min, the gene tables ~3-5 min per 1,000
selected genes; the DESeq2 scan ~15-40 min (1.2-2.3 s per file for 1,026 files, plus reading 92 GB; the worst case,
when no row group can be skipped).
"""
import argparse
import glob
import hashlib
import json
import os
import shutil
import sys
import time
import traceback

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import pyarrow as pa  # noqa: E402
import pyarrow.compute as pc  # noqa: E402
import pyarrow.parquet as pq  # noqa: E402

sys.dont_write_bytecode = True        # no __pycache__ written into the repo folders imported below
HERE = os.path.dirname(os.path.abspath(__file__))
MGDIR = os.path.dirname(HERE)
REPO = os.path.dirname(MGDIR)
for _p in (REPO, os.path.join(MGDIR, "two_way"), os.path.join(MGDIR, "upstream_tf"),
           os.path.join(MGDIR, "genome_wide")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import tahoe_atlas as A     # noqa: E402  (FX, composition_matrix, genotype_features, gene_flag_col, MIN_CELLS/LINES)
import upstream_tf as UT    # noqa: E402  (load_profiles, stream_plates, plate_r2, corrected_effects, peak_gb)
import two_way as TW        # noqa: E402  (Grid, cache_manifest, npy_layout)
import genome_wide as GW    # noqa: E402  (gw_manifest, Tensor, overlay_sets, Q_REP)

import export_doc as DOC    # noqa: E402  (README text: every file and column)

EXPORT_VERSION = 2
GENE = "TRIM72"
LOCUS_DEFAULTS = {"TRIM72": ["FUS", "PYCARD-AS1", "ITGAM"]}
Q_SCREEN = GW.Q_REP          # 0.10: genome_wide's reporting threshold
TOP_T = 200                  # plus the top 200 genes by |t_common|
GZ = {"method": "gzip", "mtime": 0}
PQ = {"compression": "zstd", "compression_level": 3}
# disk per row, measured with the step's own writers on simulated arrays at the real dimensions (16,643 genes, 1,400
# wells, 50 lines, 1,132 drug-doses), plus ~5-10% margin:
EST_BYTES_ROW = 18.5         # all_genes per_profile, per (gene, profile) row (17.07 measured)
SET_BYTES_PROFILE = 18.0     # upstream / downstream genes_per_profile.parquet, per (gene, profile) (17.1)
SET_BYTES_DDLINE = 45.0      # genes_per_drugdose_line.parquet, per (gene, drug-dose, line) (41.7)
SET_BYTES_DD = 170.0         # genes_per_drugdose .parquet + .csv.gz, per (gene, drug-dose) (160)
DESEQ_BYTES_ROW = 52.0       # tahoe_deseq2/genes.parquet, per row; ~one row per (drug well, line) and gene (49.7)
DESEQ_COLS = ["gene_name", "baseMean", "log2FoldChange", "lfcSE", "stat", "pvalue", "padj", "plate", "n_cells_trt",
              "n_cells_ctrl", "Cell_ID_Cellosaur", "Cell_ID_DepMap", "drug", "concentration", "concentration_unit",
              "Cell_Name_Vevo"]
DESEQ_NEED = ["gene_name", "log2FoldChange", "plate", "drug", "concentration"]
log, quiet = UT.log, UT.quiet


# ============================================================================= small helpers
def stat_of(p):
    try:
        s = os.stat(p)
        return [int(s.st_size), int(s.st_mtime_ns)]
    except OSError:
        return None


def sha(obj):
    return hashlib.sha1(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]


def write_csv(df, path, gz=False):
    """CSV through path.tmp: floats as their shortest exact text (float32 values round-trip), .gz byte-identical
    across runs."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_csv(tmp, index=False, compression=GZ if gz else None, lineterminator="\n")
    os.replace(tmp, path)


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + ".tmp", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(path + ".tmp", path)


def write_json(path, obj):
    write_text(path, json.dumps(obj, indent=1, sort_keys=True, default=str) + "\n")


def write_parquet(table, path, **kw):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pq.write_table(table, path + ".tmp", **(PQ | kw))
    os.replace(path + ".tmp", path)


def free_gb(path):
    p = path
    while not os.path.exists(p):
        p = os.path.dirname(p) or "."
    return shutil.disk_usage(p).free / 1e9


def dir_gb(path):
    """Size of a file or folder (GB; 0 when absent)."""
    if os.path.isfile(path):
        return os.path.getsize(path) / 1e9
    n = 0
    for root, _d, fs in os.walk(path):
        for f in fs:
            try:
                n += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return n / 1e9


def need_disk(path, gb, what, credit=0.0):
    """Stop before writing when the free disk at path (plus credit: what this run deletes before it writes, GB) is below
    gb (exit 3, nothing written by this call)."""
    f = free_gb(path)
    if f + credit < gb:
        print(f"export: {what} needs ~{gb:.1f} GB free in {path}; {f:.1f} GB free"
              + (f" (+{credit:.1f} GB this run would delete first)" if credit > 0.05 else "")
              + ". Free some disk (or run with --no-all-genes / MG53_EXPORT_ALL_GENES=0, which leaves out the ~21 GB "
              "all_genes tables), then rerun.", file=sys.stderr, flush=True)
        sys.exit(3)


def maxabs(a, b):
    a, b = np.asarray(a, np.float64), np.asarray(b, np.float64)
    m = np.isfinite(a) & np.isfinite(b)
    return (float(np.max(np.abs(a[m] - b[m]))) if m.any() else float("nan"), int(m.sum()),
            int((np.isfinite(a) != np.isfinite(b)).sum()))


def dict_col(values, idx):
    """A dictionary-encoded string column of len(idx) rows: row i holds values[idx[i]]. The dictionary is made unique
    and sorted (a dictionary with repeated values makes the Parquet bytes differ between identical runs)."""
    u, inv = np.unique(np.array([str(v) for v in values], dtype=object).astype(str), return_inverse=True)
    return pa.DictionaryArray.from_arrays(pa.array(inv[np.asarray(idx, dtype=np.int64)].astype(np.int32)),
                                          pa.array(u.tolist(), pa.string()))


def farr(x, dtype=np.float32):
    """float array with NaN -> null (nulls cost almost nothing in Parquet; pandas reads them as NaN)."""
    x = np.asarray(x, dtype=dtype)
    m = np.isnan(x)
    return pa.array(x, mask=m) if m.any() else pa.array(x)


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, check, value, n=np.nan, note=""):
        py = (lambda v: v.item() if isinstance(v, np.generic) else v)     # plain Python: JSON round-trips exactly
        self.rows.append({"check": check, "value": py(value), "n": py(n), "note": note})

    def frame(self):
        f = pd.DataFrame(self.rows, columns=["check", "value", "n", "note"])
        f["n"] = pd.to_numeric(f["n"], errors="coerce").astype("Int64")
        return f


class State:
    """<out>/.state/<part>.json = {"key": ..., "info": ...}: a part is done when its key matches."""

    def __init__(self, out):
        self.d = os.path.join(out, ".state")
        os.makedirs(self.d, exist_ok=True)

    def get(self, part):
        try:
            with open(os.path.join(self.d, f"{part}.json"), encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return None

    def done(self, part, key):
        g = self.get(part)
        return g is not None and g.get("key") == key

    def mark(self, part, key, info=None):
        write_json(os.path.join(self.d, f"{part}.json"), {"key": key, "info": info or {}})

    def clear(self, part):
        for f in glob.glob(os.path.join(self.d, f"{part}*.json")):
            os.remove(f)

    def run(self, part, key, ck, fn, need=()):
        """Runs fn() unless the part is done for this key and its outputs (need: paths) are still there; either way the
        checks the part added (saved with it) end up in ck, so a rerun writes the same checks.csv. Returns fn's result
        (also saved)."""
        g = self.get(part)
        if g is not None and g.get("key") == key and not all(os.path.exists(p) for p in need):
            log(f"{part}: marked done but its files are missing: rebuilt")
            g = None
        if g is not None and g.get("key") == key:
            for r in g.get("info", {}).get("checks", []):
                ck.add(r["check"], r["value"], r["n"], r["note"])
            log(f"{part}: done earlier")
            return g.get("info", {}).get("result", {})
        n0 = len(ck.rows)
        res = fn()
        self.mark(part, key, {"checks": ck.rows[n0:], "result": res})
        return res


# ============================================================================= the atlas context
class Ctx:
    def __init__(self, data, out, sib, args):
        self.data, self.out, self.sib = data, out, sib
        fx = A.FX(os.path.join(data, "atlas"))            # sets tahoe_atlas.MIN_CELLS from effects/info.json
        self.fx = fx
        self.grid = TW.Grid(data)
        if list(self.grid.w["sample"].astype(str)) != list(fx.wells["sample"].astype(str)):
            sys.exit("atlas wells.csv read twice gives different well orders")
        w = fx.wells
        self.w = w
        self.NW, self.L = len(w), len(fx.lines)
        self.lines = fx.lines["cell_line_id"].astype(str).tolist()
        self.line_name = np.asarray(fx.line_name, dtype=object)
        self.plates = list(fx.plates)
        self.plate_w = w["plate"].astype(str).to_numpy()
        pix = {p: i for i, p in enumerate(self.plates)}
        self.pidx = np.array([pix[p] for p in self.plate_w], dtype=np.int64)
        self.drug_w = np.asarray(fx.drug_w, bool)
        self.used = np.asarray(self.grid.used, bool)
        self.ddr = w["drugdose_row"].to_numpy(dtype=np.int64) if "drugdose_row" in w else np.full(self.NW, -1)
        self.B = self.grid.B
        gi = fx.gi
        g = fx.genes.iloc[gi].reset_index(drop=True)
        self.gi = gi
        self.G = len(gi)
        self.gsym = g["symbol"].astype(str).to_numpy()
        self.glabel = g["label"].astype(str).to_numpy()
        self.gtok = g["token"].astype(int).to_numpy()
        self.gpooled = g["pooled_cpm"].to_numpy(float)
        self.gmed = g["median_line_cpm"].to_numpy(float)
        self.gnexp = g["n_lines_expressing"].to_numpy(int)
        self.sym2idx, self.label2idx = {}, {}
        for i, (s, lb) in enumerate(zip(self.gsym, self.glabel)):
            self.sym2idx.setdefault(s, i)
            self.label2idx.setdefault(lb, i)
        self.em = np.asarray(fx.expr_mask, bool)[:, gi]       # lines x genes
        self.comp = A.composition_matrix(fx)                  # wells x lines, float32
        gm = pd.read_parquet(os.path.join(data, "metadata", "gene_metadata.parquet"),
                             columns=["gene_symbol", "token_id"])
        self.tok_of = {}
        for s, t in zip(gm["gene_symbol"].astype(str), gm["token_id"].astype(int)):
            self.tok_of.setdefault(s, int(t))
        self.tp53 = self.tp53_table()

    def tp53_table(self):
        p = os.path.join(self.data, "gene_panel", "results", "baseline_by_cell_line.csv")
        cols = ["tp53_group", "tp53_status", "tp53_changes"]
        if not os.path.exists(p):
            t = pd.DataFrame(index=self.lines, columns=cols).fillna("")
            t["tp53_source"] = "not available (gene_panel/results/baseline_by_cell_line.csv missing)"
            return t
        b = pd.read_csv(p, dtype={"cell_line_id": str}).drop_duplicates("cell_line_id").set_index("cell_line_id")
        t = pd.DataFrame(index=self.lines)
        for c in cols:
            t[c] = b[c].reindex(self.lines).fillna("").astype(str).to_numpy() if c in b else ""
        t["tp53_source"] = ("gene_panel/results/baseline_by_cell_line.csv (tahoe_gene_panel.genotypes: a TP53 driver "
                            "row in Tahoe's cell_line_metadata = altered, none = wild type)")
        return t


def data_manifest(data):
    """What the export is built from: two_way's manifest (data folder, atlas wells, pseudobulk files, gene panel) plus
    the atlas effects files, the metadata tables and the panel's line table this step reads."""
    man = TW.cache_manifest(data)
    fxd = os.path.join(data, "atlas", "effects")
    man["atlas_effects"] = {f: stat_of(os.path.join(fxd, f)) for f in (
        "genes.csv", "lines.csv", "wells.csv", "drugdose.csv", "plates.csv", "failed_wells.csv", "info.json",
        "complete.json", "W1.npy", "W2.npy", "Z.npy", "expr_mask.npy", "line_cpm.npy", "posunc.npy", "DD_lfc.npy",
        "DD_z.npy", "DD_qup.npy", "DD_qdn.npy", "DD_poseff.npy", "DD_posunc.npy", "plate_offset.npy",
        "composition_shift.parquet")}
    man["metadata"] = {f: stat_of(os.path.join(data, "metadata", f)) for f in (
        "gene_metadata.parquet", "drug_metadata.parquet", "cell_line_metadata.parquet", "sample_metadata.parquet")}
    man["panel_lines"] = stat_of(os.path.join(data, "gene_panel", "results", "baseline_by_cell_line.csv"))
    man["export_version"] = EXPORT_VERSION
    return man


# ============================================================================= sibling tables (never computed here)
def read_screen(gwtab):
    p = os.path.join(gwtab, "c_screen_genes.csv.gz")
    if not os.path.exists(p):
        return None
    return pd.read_csv(p)


def read_programs(gwtab):
    p = os.path.join(gwtab, "b_p53_program.csv")
    if not os.path.exists(p):
        return None
    return pd.read_csv(p)


def gw_status(gwdir):
    """genome_wide is finished when its run_info.json and the screen / program tables exist. Returns (finished, file
    stats, exposure, run_info)."""
    tab = os.path.join(gwdir, "tables")
    need = ["run_info.json", "c_screen_genes.csv.gz", "b_p53_program.csv"]
    have = {f: stat_of(os.path.join(tab, f)) for f in need + ["checks.csv", "key_results.csv"]}
    exposure, ri = None, {}
    try:
        with open(os.path.join(tab, "run_info.json"), encoding="utf-8") as fh:
            ri = json.load(fh)
        exposure = ri.get("exposure")
    except (OSError, ValueError):
        pass
    return all(have[f] for f in need), have, exposure, ri


def gw_tables_mismatch(ctx, *tabs):
    """genome_wide's tables name genes by idx (the position in the atlas's expressed genes) and symbol: rows whose idx
    is out of range or whose symbol is not the atlas's symbol at that idx (tables of another atlas build). Returns
    (mismatching rows, rows checked, an example)."""
    bad, n, ex = 0, 0, ""
    for t in tabs:
        if t is None or not len(t):
            continue
        idx = pd.to_numeric(t["idx"], errors="coerce").fillna(-1).astype(np.int64).to_numpy()
        sym = t["symbol"].astype(str).to_numpy()
        ok = (idx >= 0) & (idx < ctx.G)
        m = np.zeros(len(t), bool)
        m[ok] = ctx.gsym[idx[ok]] == sym[ok]
        if not ex and (~m).any():
            i = int(np.flatnonzero(~m)[0])
            ex = (f"idx {idx[i]}: table symbol {sym[i]}, atlas "
                  f"{ctx.gsym[idx[i]] if 0 <= idx[i] < ctx.G else 'out of range'}")
        bad += int((~m).sum())
        n += len(t)
    return bad, n, ex


def rel(p, ctx):
    """A path as the checks and README show it: relative to the folder that holds the export folder (the run's <out>),
    so that two identical runs into different folders write identical files."""
    return os.path.relpath(p, ctx.sib)


def valid_tensor(ctx, gwdir):
    """genome_wide's per (well x line) tensor when its cache is complete and keyed to this data folder (its own
    manifest, recomputed here the way genome_wide.gw_manifest makes it), else None. Returns (tensor or None, the check
    row's note); the caller records the check with the gene store it builds (so a later run reports the r2 source the
    store was actually built from)."""
    cdir = os.path.join(gwdir, "cache")
    mp_ = os.path.join(cdir, "manifest.json")
    need = [os.path.join(cdir, f) for f in ("r2_wl.npy", "side_wl.npz", "r2_genes.csv", "r2_wells.csv",
                                            "r2_lines.csv")]
    why = None
    if not all(os.path.exists(p) for p in need + [mp_]):
        why = "not present (genome_wide has not written its tensor)"
    else:
        try:
            with open(mp_, encoding="utf-8") as fh:
                have = json.load(fh)
            extra = list(have.get("genome_wide", {}).get("extra_genes", []))
            pmin = have.get("genome_wide", {}).get("panel_min_cells")
            want = GW.gw_manifest(ctx.data, extra, pmin)
            if have != want:
                why = "keyed to other inputs (cache/manifest.json differs from this data folder)"
        except (OSError, ValueError, KeyError) as err:
            why = f"unreadable manifest ({type(err).__name__})"
    if why is None:
        try:
            T = GW.Tensor(cdir)
            gw = pd.read_csv(os.path.join(cdir, "r2_genes.csv"))
            ww = pd.read_csv(os.path.join(cdir, "r2_wells.csv"), dtype={"sample": str})
            ll = pd.read_csv(os.path.join(cdir, "r2_lines.csv"), dtype={"cell_line_id": str})
            if not (T.G == ctx.G and T.NW == ctx.NW and T.L == ctx.L
                    and list(gw["col"].astype(int)) == list(ctx.gi)
                    and list(ww["sample"].astype(str)) == list(ctx.w["sample"].astype(str))
                    and list(ll["cell_line_id"].astype(str)) == ctx.lines):
                why = "shape or order differs from the atlas"
        except (OSError, ValueError, KeyError) as err:
            why = f"unreadable ({type(err).__name__})"
    if why:
        return None, (f"{rel(os.path.join(cdir, 'r2_wl.npy'), ctx)}: {why}; r2 computed here by upstream_tf.plate_r2 "
                      "(the function that builds the tensor)")
    return T, rel(os.path.join(cdir, "r2_wl.npy"), ctx)


def coreg_tables(ctx, coreg_dir, explicit, exposure, ck):
    """upstream_coregulation's tables (TRIM72-specific): used from the sibling folder only when the exposure is TRIM72,
    from --coreg-dir always. Returns {name: DataFrame} of the tables present."""
    if not os.path.isdir(coreg_dir):
        ck.add("upstream_coregulation tables", 0, note=f"{rel(coreg_dir, ctx)} not present (that step has not run): no "
               "co-regulation partners, readthrough index or DoG classes")
        return {}
    if exposure != "TRIM72" and not explicit:
        ck.add("upstream_coregulation tables", 0, note=f"not used: they describe TRIM72 and the exposure is {exposure} "
               "(pass --coreg-dir to use them anyway)")
        return {}
    out = {}
    for name, f in (("partners", "a_top_partners.csv"), ("coreg", "a_coreg_genomewide.csv"),
                    ("dog_index", "c_DoG_index_by_drugdose.csv"), ("dog_class", "c_DoG_gene_exposure_classes.csv"),
                    ("locus", "c_locus_neighbours_effects.csv"), ("baseline", "b_TRIM72_baseline_per_line.csv")):
        p = os.path.join(coreg_dir, f)
        if os.path.exists(p):
            try:
                out[name] = pd.read_csv(p, low_memory=False)
            except (OSError, ValueError) as err:
                ck.add(f"upstream_coregulation table unreadable: {f}", 0, note=f"{type(err).__name__}: {err}"[:300])
    ck.add("upstream_coregulation tables", len(out), note=f"{rel(coreg_dir, ctx)}: {', '.join(sorted(out)) or 'none'}")
    return out


# ============================================================================= gene selection (data-defined)
def add_reason(sel, key, reason, **cols):
    r = sel.setdefault(key, {"reasons": []})
    if reason not in r["reasons"]:
        r["reasons"].append(reason)
    for k, v in cols.items():
        r.setdefault(k, v)


def locus_genes(ctx, syms, ck):
    """Locus genes: atlas genes -> ('atlas', idx); non-atlas genes with a token -> ('extra', symbol); else skipped."""
    out = []
    for s in syms:
        if s in ctx.sym2idx:
            out.append(("atlas", ctx.sym2idx[s], s))
        elif s in ctx.tok_of:
            out.append(("extra", s, s))
        else:
            ck.add(f"locus gene not found: {s}", 0, note="neither an atlas gene nor in metadata/gene_metadata.parquet")
    return out


def upstream_selection(ctx, screen, co, locus, xi):
    """{key: {reasons, ...}}: genome_wide's common-slope screen (q < 0.1 and the top 200 by |t|), the co-regulation
    partners (a_top_partners: every variant, both directions), the locus genes (geometry). Keys: atlas index or
    ('extra', symbol)."""
    sel = {}
    if screen is not None:
        s = screen[screen["tested"].astype(str).str.lower().eq("true")].copy()
        s = s[s["idx"].astype(int) != xi]
        s["abs_t"] = s["t_common"].abs()
        s["rank_abs_t_common"] = s["abs_t"].rank(ascending=False, method="first")
        for r in s[s["q_common"] < Q_SCREEN].itertuples():
            add_reason(sel, int(r.idx), f"genome_wide screen: common slope q < {Q_SCREEN:g}")
        for r in s[s["rank_abs_t_common"] <= TOP_T].itertuples():
            ns = "" if r.q_common < Q_SCREEN else f"; q_common {r.q_common:.2g} >= {Q_SCREEN:g}: not significant"
            add_reason(sel, int(r.idx),
                       f"genome_wide screen: top {TOP_T} by |t_common| (rank {int(r.rank_abs_t_common)}{ns})")
    if "partners" in co:
        for r in co["partners"].itertuples():
            g = str(r.gene)
            i = ctx.label2idx.get(g, ctx.sym2idx.get(g))
            if i is None or i == xi:
                continue
            add_reason(sel, int(i), f"upstream_coregulation partner ({r.variant}, {r.direction}, rank {int(r.rank)})")
    for kind, k, s in locus:
        if kind == "atlas" and k == xi:
            continue
        add_reason(sel, k if kind == "atlas" else ("extra", k), "locus geometry: TRIM72 neighbourhood (16p11.2), "
                   "chosen by genomic position, not by pathway")
    return sel


def downstream_selection(ctx, screen, prog, xi):
    sel = {}
    if prog is not None:
        for r in prog.itertuples():
            nm = "P" if str(r.program).startswith("P (") else "P-down"
            fb = str(r.program_is_fallback).lower() == "true"
            add_reason(sel, int(r.idx), f"Tahoe p53 program {nm}" + (" (FALLBACK: fewer than 10 genes passed; the top "
                                                                     "25 by z, exploratory)" if fb else ""))
    if screen is not None:
        s = screen[screen["tested"].astype(str).str.lower().eq("true")]
        s = s[s["idx"].astype(int) != xi]
        for r in s[s["q_common"] < Q_SCREEN].itertuples():
            add_reason(sel, int(r.idx), f"genome_wide screen: common slope q < {Q_SCREEN:g}")
        for r in s[s["q_diff"] < Q_SCREEN].itertuples():
            add_reason(sel, int(r.idx), f"genome_wide screen: WT minus altered q < {Q_SCREEN:g}")
    return sel


# ============================================================================= the pass over atlas/pseudobulk
def logcpm(C, tot, nc, em=None):
    """log2((count + 0.5) / (total + 1) x 1e6) as float32, elementwise exactly as tahoe_atlas.log_cpm and
    upstream_tf.plate_r2; NaN where the profile has < MIN_CELLS cells and (em: lines x genes) where the line does not
    express the gene. C (..., L, G) float32; tot, nc (..., L)."""
    Y = np.full(C.shape, np.nan, dtype=np.float32)
    ok = nc >= A.MIN_CELLS
    Y[ok] = np.log2((C[ok] + 0.5) / (tot[ok][:, None] + 1.0) * 1e6)
    if em is not None:
        Y[..., ~em] = np.nan
    return Y


def dmso_level(C, tot, nc, drug, em):
    """The atlas's pooled DMSO level of one plate (tahoe_atlas cmd_effects, plate_offset): per line, the DMSO wells'
    counts summed, one pseudocount per DMSO well with the line: log2((sum + 0.5 k) / (total + k) x 1e6); NaN when the
    pooled DMSO cells < MIN_CELLS or the line does not express the gene. Returns (level float64 L x G, sums of counts
    float32 L x G, totals L, cells L, k L)."""
    dm = ~drug
    L, G = C.shape[1], C.shape[2]
    if not dm.any():
        return (np.full((L, G), np.nan), np.zeros((L, G), np.float32), np.zeros(L), np.zeros(L), np.zeros(L, int))
    dc = C[dm].sum(axis=0)
    dt = tot[dm].sum(axis=0)
    dn = nc[dm].sum(axis=0)
    k = np.maximum((tot[dm] > 0).sum(axis=0), 1)
    dy = np.where((dn >= A.MIN_CELLS)[:, None], np.log2((dc + 0.5 * k[:, None]) / (dt[:, None] + k[:, None]) * 1e6),
                  np.nan)
    if em is not None:
        dy[~em] = np.nan
    return dy, dc, dt, dn, k


class Pass:
    """The pass cache in <out>/.cache/pass: counts_wl.npy (genes x wells x lines, float32, gene-major), r2_wl.npy when
    genome_wide's tensor is not reused, side.npz (written last: it marks a finished pass)."""

    def __init__(self, pdir):
        self.d = pdir
        self.counts_p = os.path.join(pdir, "counts_wl.npy")
        self.r2_p = os.path.join(pdir, "r2_wl.npy")
        self.side_p = os.path.join(pdir, "side.npz")

    def ready(self, key, need_r2):
        try:
            with open(os.path.join(self.d, "key.json"), encoding="utf-8") as fh:
                k = json.load(fh)["key"]
        except (OSError, ValueError, KeyError):
            return False
        need = [self.counts_p, self.side_p] + ([self.r2_p] if need_r2 else [])
        return k == key and all(os.path.exists(p) for p in need)

    def side(self):
        with np.load(self.side_p, allow_pickle=False) as z:
            return {k: z[k] for k in z.files}

    def read(self, path, a, b):
        off, shape, _ = TW.npy_layout(path)
        _, NW, L = shape
        mm = np.memmap(path, np.float32, "r", offset=off + a * NW * L * 4, shape=(b - a, NW, L))
        out = np.array(mm)
        del mm
        return out

    def clear(self):
        shutil.rmtree(self.d, ignore_errors=True)


def run_pass(ctx, cols, extra, P_, key, need_r2, ck):
    """One streamed pass over <data>/atlas/pseudobulk (upstream_tf.stream_plates: each file read once). Per plate, as
    soon as its profiles are read: the counts of the atlas genes cols (positions in the atlas gene order) and of the
    extra genes, written gene-major; the plate's drug-well median log2 CPM per line (the method's baseline), the pooled
    DMSO level per line, the W1 and plate_offset checks against the atlas; r2 by upstream_tf.plate_r2 when genome_wide's
    tensor is not reused."""
    if P_.ready(key, need_r2):
        log(f"pass: cache {P_.d}")
        return P_.side()
    P_.clear()
    os.makedirs(P_.d, exist_ok=True)
    t0 = time.time()
    fx = ctx.fx
    cols = np.asarray(cols, dtype=np.int64)
    G, NW, L = len(cols), ctx.NW, ctx.L
    toks = ctx.gtok[cols]
    etoks = np.array([ctx.tok_of[s] for s in extra], dtype=int)
    em = ctx.em[:, cols]
    gcol = ctx.gi[cols]
    prof = UT.load_profiles(os.path.join(ctx.data, "atlas", "pseudobulk"))
    wi = {s: i for i, s in enumerate(ctx.w["sample"].astype(str))}
    li = {s: i for i, s in enumerate(ctx.lines)}
    prof = prof[prof["sample"].isin(wi) & prof["cell_line_id"].isin(li)].copy()
    prof["wi"] = prof["sample"].map(wi).astype(int)
    prof["li"] = prof["cell_line_id"].map(li).astype(int)
    prof["plate"] = ctx.plate_w[prof["wi"].to_numpy()]
    rows_of = {p: np.flatnonzero(ctx.plate_w == p) for p in ctx.plates}
    prof = prof[prof["plate"].isin(ctx.plates)]
    tot = np.zeros((NW, L))
    nc = np.zeros((NW, L))
    np.add.at(tot, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["total_counts"].to_numpy(float))
    np.add.at(nc, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["n_cells"].to_numpy(float))
    nP = len(ctx.plates)
    paths = [P_.counts_p] + ([P_.r2_p] if need_r2 else [])
    fhs, offs = [], []
    for p in paths:
        mm = np.lib.format.open_memmap(p + ".tmp", mode="w+", dtype=np.float32, shape=(G, NW, L))
        del mm
        offs.append(TW.npy_layout(p + ".tmp")[0])
        fhs.append(open(p + ".tmp", "r+b"))
    rowb = NW * L * 4
    base = np.full((nP, L, G), np.nan, np.float32)
    dy = np.full((nP, L, G), np.nan, np.float64)
    dmc = np.zeros((nP, L, G), np.float32)
    dmt, dmn = np.zeros((nP, L)), np.zeros((nP, L))
    dmk = np.zeros((nP, L), np.int64)
    exw = np.zeros((NW, L, len(etoks)), np.float32)
    written = np.zeros(NW, bool)
    val = []
    nonint = [0]
    po_atlas = np.asarray(fx.plate_offset)
    W1all, W2all = fx.W1, fx.W2
    log(f"pass: {G} atlas genes{' and ' + ', '.join(extra) if extra else ''} x {NW} wells x {L} lines "
        f"({G * rowb / 1e9:.2f} GB of counts{' + the same of r2' if need_r2 else ''}) from "
        f"{prof['file'].nunique()} pseudobulk files")

    def write_rows(fh, off, rows, Yt):
        for i0, i1 in GW.runs_of(rows):
            r0 = int(rows[i0])
            for g in range(G):
                fh.seek(off + g * rowb + r0 * L * 4)
                fh.write(np.ascontiguousarray(Yt[g, i0:i1]).tobytes())

    def on_plate(p, C, Ex):
        tp = time.time()
        rows = rows_of[p]
        pi = ctx.plates.index(p)
        nonint[0] += int(np.count_nonzero(np.rint(C) != C))
        write_rows(fhs[0], offs[0], rows, C.transpose(2, 0, 1))
        exw[rows] = Ex
        t_, n_ = tot[rows], nc[rows]
        drug = ctx.drug_w[rows]
        comp = ctx.comp[rows]
        dy[pi], dmc[pi], dmt[pi], dmn[pi], dmk[pi] = dmso_level(C, t_, n_, drug, em)
        Y = logcpm(C, t_, n_, em)
        with quiet():
            for l_ in range(L):                               # as upstream_tf.plate_r2: the baseline, then the shift
                base[pi, l_] = np.nanmedian(Y[drug, l_, :], axis=0)
                Y[:, l_, :] -= base[pi, l_][None, :]
                Y[:, l_, :] -= comp[:, l_][:, None]
            W1m = np.full((len(rows), G), np.nan, np.float32)
            for i in range(len(rows)):
                v = np.nanmedian(Y[i], axis=0)
                v[np.isfinite(Y[i]).sum(axis=0) < A.MIN_LINES] = np.nan
                W1m[i] = v
            off_here = np.nanmedian(base[pi].astype(np.float64) - dy[pi], axis=0).astype(np.float32)
        del Y
        W1a = np.asarray(W1all[rows])[:, gcol]
        d1, n1, m1 = maxabs(W1m, W1a)
        d2, n2, m2 = maxabs(off_here, po_atlas[pi, gcol]) if (~drug).any() else (np.nan, 0, 0)
        v = {"plate": p, "wells": len(rows), "W1_max_abs_diff_vs_atlas": d1, "W1_cells_both_finite": n1,
             "W1_finite_pattern_mismatch": m1, "plate_offset_max_abs_diff_vs_atlas": d2, "plate_offset_genes": n2,
             "plate_offset_finite_pattern_mismatch": m2}
        if need_r2:
            W2a = np.asarray(W2all[rows])[:, gcol]
            R, _w, _v = UT.plate_r2(C, t_, n_, em, drug, comp, W1a, W2a)      # in place on C (counts already written)
            write_rows(fhs[1], offs[1], rows, R.transpose(2, 0, 1))
        written[rows] = True
        val.append(v)
        log(f"  plate {p}: {len(rows)} wells ({time.time() - tp:.0f} s; W1 max |diff| vs atlas {d1:.2g}; "
            f"plate_offset {d2:.2g}; peak RSS {UT.peak_gb():.2f} GB)")

    UT.stream_plates(prof, rows_of, ctx.plates, NW, L, toks, etoks, on_plate)
    nowrite = np.flatnonzero(~written)
    if len(nowrite) and need_r2:                               # no profiles: r2 NaN (a new file reads as zeros)
        write_rows(fhs[1], offs[1], nowrite, np.broadcast_to(np.full((1, len(nowrite), L), np.nan, np.float32),
                                                             (G, len(nowrite), L)))
    for fh in fhs:
        fh.close()
    for p in paths:
        os.replace(p + ".tmp", p)
    side = {"tot": tot, "nc": nc, "base": base, "dy": dy, "dmc": dmc, "dmt": dmt, "dmn": dmn, "dmk": dmk, "exw": exw,
            "cols": cols, "extra": np.array(extra, dtype=str), "validation": np.array(json.dumps(val)),
            "nonint": np.int64(nonint[0]), "tot_nonint": np.int64(np.count_nonzero(np.rint(tot) != tot)),
            "wells_without_profiles": nowrite}
    GW.save_npz(P_.side_p, **side)
    write_json(os.path.join(P_.d, "key.json"), {"key": key})
    log(f"pass done ({time.time() - t0:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")
    return side


def pass_checks(side, ck):
    V = pd.DataFrame(json.loads(str(side["validation"])))
    for r in V.itertuples():
        ck.add(f"median over lines of u_drugmedian - composition_shift vs atlas W1, plate {r.plate}: max |diff|",
               r.W1_max_abs_diff_vs_atlas, r.W1_cells_both_finite,
               f"finite-pattern mismatches {r.W1_finite_pattern_mismatch}")
    ck.add("median over lines of (drug-median baseline - pooled DMSO level) vs atlas plate_offset, all plates: max "
           "|diff|", float(V["plate_offset_max_abs_diff_vs_atlas"].max()), int(V["plate_offset_genes"].sum()),
           f"finite-pattern mismatches {int(V['plate_offset_finite_pattern_mismatch'].sum())}")
    ck.add("non-integer UMI counts in the pseudobulk (stored as float32 when > 0)", int(side["nonint"]))
    ck.add("wells without any profile in the pseudobulk", len(side["wells_without_profiles"]))
    return V


def extra_effects(ctx, side, extra):
    """Non-atlas genes (e.g. PYCARD-AS1): upstream_tf.corrected_effects (the atlas's per_line_columns steps with the
    gene's own two-pass position correction), kept in every line (as two_way does for PYCARD-AS1). Returns per gene a
    dict of (wells x lines) arrays and per drug-dose values, in the same terms as the atlas genes."""
    if not len(extra):
        return {}
    fx = ctx.fx
    cnt = side["exw"].astype(np.float64)
    tot, nc = side["tot"], side["nc"]
    expressed = np.ones((ctx.L, len(extra)), bool)
    with quiet():
        r1, r2, W2, zw, per, ddl, ddz = UT.corrected_effects(fx, cnt, tot, nc, expressed)
        W1 = np.nanmedian(r1, axis=1)
    W1[np.isfinite(r1).sum(axis=1) < A.MIN_LINES] = np.nan
    out = {}
    for j, s in enumerate(extra):
        C = side["exw"][:, :, j][:, :, None]
        Y = logcpm(C, tot, nc)[:, :, 0]
        base = np.full((len(ctx.plates), ctx.L), np.nan, np.float32)
        dyp = np.full((len(ctx.plates), ctx.L), np.nan)
        dmc = np.zeros((len(ctx.plates), ctx.L), np.float32)
        with quiet():
            for pi, p in enumerate(ctx.plates):
                rows = np.flatnonzero(ctx.pidx == pi)
                base[pi] = np.nanmedian(Y[rows[ctx.drug_w[rows]]], axis=0)
                d_, c_, _t, _n, _k = dmso_level(C[rows], tot[rows], nc[rows], ctx.drug_w[rows], None)
                dyp[pi], dmc[pi] = d_[:, 0], c_[:, 0]
        eff = (W1[:, j] - W2[:, j]).astype(np.float32)
        out[s] = {"counts": side["exw"][:, :, j], "u_dm": (Y - base[ctx.pidx]).astype(np.float32),
                  "u_dmso": (Y.astype(np.float64) - dyp[ctx.pidx]).astype(np.float32),
                  "r2": r2[:, :, j].astype(np.float32),
                  "eff": np.where(np.isfinite(W1[:, j]), eff, np.nan).astype(np.float32), "W1": W1[:, j],
                  "W2": W2[:, j],
                  "Z": zw[:, j], "ddl": ddl[:, j], "ddz": ddz[:, j], "base": base, "dy": dyp, "dmc": dmc,
                  "expressed": expressed[:, j], "token": ctx.tok_of[s]}
    return out


# ============================================================================= the gene store (all_genes or selected)
PROFILE_KEYS = ["plate", "well", "drug", "concentration_uM", "is_dmso", "cell_line_id"]
ROW_SCHEMA = pa.schema([
    ("gene", pa.dictionary(pa.int32(), pa.string())), ("plate", pa.dictionary(pa.int32(), pa.string())),
    ("well", pa.dictionary(pa.int32(), pa.string())), ("drug", pa.dictionary(pa.int32(), pa.string())),
    ("concentration_uM", pa.float64()), ("is_dmso", pa.bool_()),
    ("cell_line_id", pa.dictionary(pa.int32(), pa.string())), ("n_cells", pa.int32()), ("total_umi", pa.int64()),
    ("umi_count", pa.int32()), ("usable", pa.bool_()), ("expressed", pa.bool_()), ("well_used", pa.bool_()),
    ("u_dmso", pa.float32()), ("u_drugmedian", pa.float32()), ("position_effect", pa.float32()),
    ("posunc", pa.bool_()), ("r2", pa.float32())])
FLOAT_COLS = ["u_dmso", "u_drugmedian", "position_effect", "r2"]


def row_schema(int_counts):
    if int_counts:
        return ROW_SCHEMA
    return ROW_SCHEMA.set(ROW_SCHEMA.get_field_index("umi_count"), pa.field("umi_count", pa.float32()))


def row_writer(path, schema):
    """Parquet writer of per-profile rows: zstd, byte-stream-split floats, dictionary pages for the text columns and
    concentration_uM only (17.4 bytes per row on simulated real-size data vs 18.9 with dictionaries on every column,
    and faster). concentration_uM is float64 (0.05 exactly as written in every table; a float32 0.05 does not equal
    the literal 0.05 in pyarrow / R arrow filters); with its 4 values in a dictionary it costs ~0 bytes per row."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return pq.ParquetWriter(path, schema, **PQ, use_byte_stream_split=[c for c in FLOAT_COLS if c in schema.names],
                            use_dictionary=[f.name for f in schema if pa.types.is_dictionary(f.type)
                                            or f.name == "concentration_uM"])


class Profiles:
    """The profiles (well x line with cells or UMIs) in store order: wells in atlas order, lines in atlas order."""

    def __init__(self, ctx, side):
        tot, nc = side["tot"], side["nc"]
        self.exists = (nc > 0) | (tot > 0)
        self.pw, self.pl = np.nonzero(self.exists)
        self.P = len(self.pw)
        self.tot, self.nc = tot, nc
        w = ctx.w
        self.keys = {
            "plate": dict_col(ctx.plates, ctx.pidx[self.pw]),
            "well": None, "drug": None, "cell_line_id": dict_col(ctx.lines, self.pl)}
        wells = w["well"].fillna("").astype(str).to_numpy()
        uw, iw = np.unique(wells, return_inverse=True)
        self.keys["well"] = dict_col(uw, iw[self.pw])
        drugs = w["drug"].astype(str).to_numpy()
        ud, idr = np.unique(drugs, return_inverse=True)
        self.keys["drug"] = dict_col(ud, idr[self.pw])
        self.keys["concentration_uM"] = pa.array(w["conc"].to_numpy(np.float64)[self.pw])
        self.keys["is_dmso"] = pa.array(~ctx.drug_w[self.pw])
        self.n_cells = nc[self.pw, self.pl]
        self.total = tot[self.pw, self.pl]
        self.usable = self.n_cells >= A.MIN_CELLS
        self.well_used = ctx.used[self.pw]

    def table(self, ctx):
        w = ctx.w
        cs = ctx.comp[self.pw, self.pl]
        return pa.table({
            "profile_id": pa.array(np.arange(self.P, dtype=np.int32)), "plate": self.keys["plate"],
            "well": self.keys["well"], "slot": pa.array(w["slot"].to_numpy(np.float64)[self.pw]),
            "sample": dict_col(w["sample"].astype(str).to_numpy(), self.pw), "drug": self.keys["drug"],
            "concentration_uM": self.keys["concentration_uM"], "is_dmso": self.keys["is_dmso"],
            "well_used": pa.array(self.well_used), "drug_dose_row": pa.array(ctx.ddr[self.pw].astype(np.int32)),
            "unreliable_plate": pa.array(~ctx.fx.reliable_w[self.pw]),
            "cell_line_id": self.keys["cell_line_id"], "cell_name": dict_col(ctx.line_name, self.pl),
            "tp53_group": dict_col(ctx.tp53["tp53_group"].astype(str).to_numpy(), self.pl),
            "n_cells": pa.array(np.rint(self.n_cells).astype(np.int32)),
            "total_umi": pa.array(np.rint(self.total).astype(np.int64)), "usable": pa.array(self.usable),
            "composition_shift": pa.array(cs.astype(np.float32))})


def gene_rows(prof, label, vals, int_counts, path_tag=None):
    """One gene's rows (pa.Table): vals = dict of (wells x lines) arrays counts, expressed (lines), u_dmso, u_dm,
    eff (wells), posunc (wells or None), r2."""
    pw, pl = prof.pw, prof.pl
    cnt = vals["counts"][pw, pl]
    cols = {"gene": dict_col([label], np.zeros(prof.P, np.int32)), **{k: prof.keys[k] for k in PROFILE_KEYS},
            "n_cells": pa.array(np.rint(prof.n_cells).astype(np.int32)),
            "total_umi": pa.array(np.rint(prof.total).astype(np.int64)),
            "umi_count": pa.array(np.rint(cnt).astype(np.int32)) if int_counts else pa.array(cnt.astype(np.float32)),
            "usable": pa.array(prof.usable), "expressed": pa.array(np.asarray(vals["expressed"], bool)[pl]),
            "well_used": pa.array(prof.well_used), "u_dmso": farr(vals["u_dmso"][pw, pl]),
            "u_drugmedian": farr(vals["u_dm"][pw, pl]), "position_effect": farr(vals["eff"][pw]),
            "posunc": (pa.array(np.asarray(vals["posunc"], bool)[pw]) if vals.get("posunc") is not None
                       else pa.nulls(prof.P, pa.bool_())),
            "r2": farr(vals["r2"][pw, pl])}
    return pa.table(cols)


def drugdose_rows(ctx, label, vals, dd):
    """Per (gene, drug-dose): the atlas's drug-dose values (dd: dict of nd arrays) and the uncorrected medians over
    lines, as means over the drug-dose's used wells."""
    B = ctx.B
    nd = B.shape[0]
    with quiet():
        um = vals["um"] if "um" in vals else np.nanmedian(vals["u_dm"], axis=1)
        uo = vals["uo"] if "uo" in vals else np.nanmedian(vals["u_dmso"], axis=1)
        rm = vals["rm"] if "rm" in vals else np.nanmedian(vals["r2"], axis=1)
    cnt = np.nansum(vals["counts"], axis=1)
    tot = ctx._tot_w
    r2f = np.isfinite(vals["r2"])                               # wells x lines
    nl = r2f.sum(axis=1).astype(np.float64)
    D = {"gene": dict_col([label], np.zeros(nd, np.int32)),
         "drug_dose_row": pa.array(np.arange(nd, dtype=np.int32)),
         "drug": dict_col(ctx.fx.dd["drug"].astype(str).to_numpy(), np.arange(nd)),
         "concentration_uM": pa.array(ctx.fx.dd["conc"].to_numpy(np.float64)),
         "n_wells_used": pa.array(np.asarray(B.sum(axis=1)).ravel().astype(np.int32)),
         "n_lines_r2_mean": farr(TW.Grid.dd_mean(B, nl[:, None])[:, 0]),
         "n_lines_r2_any": pa.array((np.asarray(B @ r2f.astype(np.float64)) > 0).sum(axis=1).astype(np.int32))}
    for k in ("DD_lfc", "DD_z", "DD_qup", "DD_qdn", "DD_poseff"):
        D[k] = farr(dd[k])
    D["DD_posunc"] = pa.array(dd["DD_posunc"]) if dd.get("DD_posunc") is not None else pa.nulls(nd, pa.bool_())
    D["W1_mean_used_wells"] = farr(TW.Grid.dd_mean(B, vals["W1"][:, None])[:, 0])
    D["r2_median_lines_mean"] = farr(TW.Grid.dd_mean(B, rm[:, None])[:, 0])
    D["u_drugmedian_median_lines_mean"] = farr(TW.Grid.dd_mean(B, um[:, None])[:, 0])
    D["u_dmso_median_lines_mean"] = farr(TW.Grid.dd_mean(B, uo[:, None])[:, 0])
    D["plate_dmso_offset_mean"] = farr(TW.Grid.dd_mean(B, vals["poff"][:, None])[:, 0])
    cs = np.asarray(B @ cnt).ravel()
    ts = np.asarray(B @ tot).ravel()
    D["umi_count_sum"] = pa.array(cs.astype(np.float64))
    D["total_umi_sum"] = pa.array(ts.astype(np.float64))
    D["n_cells_sum"] = pa.array(np.asarray(B @ ctx._nc_w).ravel().astype(np.float64))
    with quiet():
        D["cpm_pooled"] = farr(np.where(ts > 0, cs / ts * 1e6, np.nan), np.float64)
    return pa.table(D)


def baseline_rows(ctx, label, base, dy, dmc):
    """Per (gene, plate, line): the drug-median log2 CPM baseline, the pooled DMSO level and DMSO UMIs."""
    nP, L = base.shape
    pi = np.repeat(np.arange(nP), L)
    li = np.tile(np.arange(L), nP)
    return pa.table({"gene": dict_col([label], np.zeros(nP * L, np.int32)), "plate": dict_col(ctx.plates, pi),
                     "cell_line_id": dict_col(ctx.lines, li), "drug_median_log2cpm": farr(base.ravel()),
                     "dmso_log2cpm": farr(dy.ravel(), np.float64),
                     "dmso_umi": pa.array(dmc.ravel().astype(np.float64))})


def atlas_dd(ctx, cols):
    """Atlas drug-dose arrays for atlas gene positions cols: dict of (nd x len(cols))."""
    fx = ctx.fx
    gc = ctx.gi[np.asarray(cols)]
    out = {k: np.asarray(getattr(fx, k))[:, gc] for k in ("DD_lfc", "DD_z", "DD_qup", "DD_qdn", "DD_poseff")}
    out["DD_posunc"] = np.asarray(fx.DD_posunc)[:, gc].astype(bool)
    return out


def atlas_block(ctx, side, pos, cols, counts, r2_src):
    """Every per (well, line) value of a chunk of atlas genes (positions pos in the pass, atlas gene indices cols):
    counts and r2_src (genes x wells x lines) -> dict of arrays and the identity checks."""
    tot, nc = side["tot"], side["nc"]
    g = len(cols)
    em = ctx.em[:, cols].T                                     # genes x lines
    Y = np.empty(counts.shape, np.float32)
    for j in range(g):                                         # elementwise as the pass: identical float32 values
        Y[j] = logcpm(counts[j][:, :, None], tot, nc)[:, :, 0]
    Y[~np.broadcast_to(em[:, None, :], Y.shape)] = np.nan
    base = side["base"][:, :, pos]                             # plates x lines x g
    dy = side["dy"][:, :, pos]
    u_dm = Y - base[ctx.pidx].transpose(2, 0, 1)
    u_dmso = (Y.astype(np.float64) - dy[ctx.pidx].transpose(2, 0, 1)).astype(np.float32)
    r1c = u_dm - ctx.comp[None]
    with quiet():
        nfin = np.isfinite(r1c).sum(axis=2)
        W1ok = nfin >= A.MIN_LINES
    gc = ctx.gi[cols]
    W1a = np.asarray(ctx.fx.W1)[:, gc].T                      # g x wells
    W2a = np.asarray(ctx.fx.W2)[:, gc].T
    eff = np.nan_to_num(W1a - W2a).astype(np.float32)
    r2_here = np.where(W1ok[:, :, None], r1c - eff[:, :, None], np.nan).astype(np.float32)
    chk = {"r2_vs_source": maxabs(r2_src, r2_here)}
    with quiet():                                              # one call per chunk (fast); per gene it is slow
        W2m = np.nanmedian(r2_src, axis=2)
        um = np.nanmedian(u_dm, axis=2)
        uo = np.nanmedian(u_dmso, axis=2)
    chk["W2"] = maxabs(W2m, W2a)
    posunc = np.asarray(ctx.fx.posunc)[:, gc].T.astype(bool)
    poff = np.asarray(ctx.fx.plate_offset)[:, gc].T[:, ctx.pidx]  # g x wells
    return {"Y": Y, "u_dm": u_dm, "u_dmso": u_dmso, "r2": r2_src, "eff": np.where(W1ok, eff, np.nan),
            "posunc": posunc, "W1": W1a, "W2": W2a, "W2m": W2m, "um": um, "uo": uo, "poff": poff, "em": em}, chk


def store_files(sdir, name):
    return {"per_profile": os.path.join(sdir, "per_profile", f"{name}.parquet"),
            "per_drugdose": os.path.join(sdir, "per_drugdose", f"{name}.parquet"),
            "plate_baselines": os.path.join(sdir, "plate_baselines", f"{name}.parquet")}


def store_complete(sdir):
    """Every file of a finished gene store is there: genes.csv, profiles.parquet, plate_line.parquet and every file
    genes.csv names. (Deleting all_genes/ is the obvious way to get the disk back; the store is then rebuilt, not
    trusted from .state.)"""
    try:
        idx = pd.read_csv(os.path.join(sdir, "genes.csv"))
    except (OSError, ValueError):
        return False
    need = {"profiles.parquet", "plate_line.parquet"}
    for c in ("file", "drugdose_file", "baselines_file"):
        if c in idx:
            need |= set(idx[c].astype(str))
    return all(os.path.exists(os.path.join(sdir, f)) for f in need)


def store_genes_done(st_d, sdir, key, n, chunk):
    """Genes of a store under construction already written for this key (chunks whose state and files are there), for
    the free-disk check of a resumed run."""
    k_done = 0
    for cj in glob.glob(os.path.join(st_d, "chunks", "chunk_*.json")):
        name = os.path.basename(cj)[:-5]
        try:
            with open(cj, encoding="utf-8") as fh:
                d = json.load(fh)
            k = int(name[6:10])
        except (OSError, ValueError):
            continue
        if d.get("key") == key and all(os.path.exists(f) for f in store_files(sdir, name).values()):
            k_done += max(0, min(n, (k + 1) * chunk) - k * chunk)
    return k_done


def write_store(ctx, side, P_, sdir, cols, extra_res, chunk, tensor, need_r2, key, st, ck):
    """The gene store: profiles.parquet, genes.csv (index gene -> files) and, per gene chunk, per_profile/,
    per_drugdose/, plate_baselines/ Parquet files (one row group per gene). Chunks already written for this key are
    skipped (resume); each chunk's checks go to .state/chunks/."""
    t0 = time.time()
    os.makedirs(sdir, exist_ok=True)
    prof = Profiles(ctx, side)
    ctx._tot_w = side["tot"].sum(axis=1)
    ctx._nc_w = side["nc"].sum(axis=1)
    int_counts = int(side["nonint"]) == 0
    schema = row_schema(int_counts)
    pp = os.path.join(sdir, "profiles.parquet")
    write_parquet(prof.table(ctx), pp)
    write_parquet(pa.table({"plate": dict_col(ctx.plates, np.repeat(np.arange(len(ctx.plates)), ctx.L)),
                            "cell_line_id": dict_col(ctx.lines, np.tile(np.arange(ctx.L), len(ctx.plates))),
                            "dmso_total_umi": pa.array(side["dmt"].ravel()),
                            "dmso_cells": pa.array(side["dmn"].ravel()),
                            "n_dmso_wells_with_line": pa.array(side["dmk"].ravel().astype(np.int32))}),
                  os.path.join(sdir, "plate_line.parquet"))
    cdir = os.path.join(st.d, "chunks")
    os.makedirs(cdir, exist_ok=True)
    cols = np.asarray(cols, dtype=np.int64)
    idx_rows, chk_all = [], []
    nch = (len(cols) + chunk - 1) // chunk
    for k in range(nch):
        a, b = k * chunk, min(len(cols), (k + 1) * chunk)
        name = f"chunk_{k:04d}"
        F = store_files(sdir, name)
        cj = os.path.join(cdir, f"{name}.json")
        labels = [ctx.glabel[c] for c in cols[a:b]]
        for j, c in enumerate(cols[a:b]):
            idx_rows.append({"gene": ctx.glabel[c], "symbol": ctx.gsym[c], "kind": "atlas", "atlas_col": int(ctx.gi[c]),
                             "token": int(ctx.gtok[c]), "file": f"per_profile/{name}.parquet", "row_group": j,
                             "drugdose_file": f"per_drugdose/{name}.parquet",
                             "baselines_file": f"plate_baselines/{name}.parquet",
                             "pooled_cpm": ctx.gpooled[c], "median_line_cpm": ctx.gmed[c],
                             "n_lines_expressing": int(ctx.gnexp[c]),
                             "correction_path": "atlas (method v3; position effect = atlas W1 - W2)"})
        done = None
        if os.path.exists(cj) and all(os.path.exists(f) for f in F.values()):
            try:
                with open(cj, encoding="utf-8") as fh:
                    done = json.load(fh)
            except (OSError, ValueError):
                done = None
        if done is not None and done.get("key") == key:
            chk_all.append(done["checks"])
            continue
        tc = time.time()
        counts = P_.read(P_.counts_p, a, b)
        r2s = tensor.take(cols[a:b]) if tensor is not None else P_.read(P_.r2_p, a, b)
        V, chk = atlas_block(ctx, side, np.arange(a, b), cols[a:b], counts, r2s)
        dd = atlas_dd(ctx, cols[a:b])
        with quiet():
            ddm = TW.Grid.dd_mean(ctx.B, V["W2m"].T.astype(np.float64))
        chk["DD_lfc"] = maxabs(ddm, dd["DD_lfc"])
        wr = [row_writer(F["per_profile"] + ".tmp", schema), None, None]
        dtabs, btabs = [], []
        for j in range(b - a):
            vals = {"counts": counts[j], "expressed": V["em"][j], "u_dmso": V["u_dmso"][j], "u_dm": V["u_dm"][j],
                    "eff": V["eff"][j], "posunc": V["posunc"][j], "r2": V["r2"][j]}
            wr[0].write_table(gene_rows(prof, labels[j], vals, int_counts).cast(schema), row_group_size=prof.P)
            dvals = {"um": V["um"][j], "uo": V["uo"][j], "rm": V["W2m"][j], "W1": V["W1"][j],
                     "poff": V["poff"][j], "counts": counts[j], "r2": V["r2"][j]}
            dtabs.append(drugdose_rows(ctx, labels[j], dvals, {kk: vv[:, j] for kk, vv in dd.items()}))
            btabs.append(baseline_rows(ctx, labels[j], side["base"][:, :, a + j], side["dy"][:, :, a + j],
                                       side["dmc"][:, :, a + j]))
        wr[0].close()
        os.replace(F["per_profile"] + ".tmp", F["per_profile"])
        write_parquet(pa.concat_tables(dtabs, promote_options="permissive"), F["per_drugdose"],
                      row_group_size=ctx.B.shape[0])
        write_parquet(pa.concat_tables(btabs, promote_options="permissive"), F["plate_baselines"],
                      row_group_size=len(ctx.plates) * ctx.L)
        cks = {k_: list(v_) for k_, v_ in chk.items()}
        write_json(cj, {"key": key, "checks": cks})
        chk_all.append(cks)
        log(f"  store {name}: genes {a}-{b - 1} of {len(cols)} ({time.time() - tc:.0f} s; peak RSS "
            f"{UT.peak_gb():.2f} GB)")
        del counts, r2s, V
    # extra (non-atlas) genes: one more file of the same schema
    if extra_res:
        F = store_files(sdir, "extra_genes")
        wr = row_writer(F["per_profile"] + ".tmp", schema)
        dtabs, btabs = [], []
        for j, (s, E) in enumerate(sorted(extra_res.items())):
            vals = {"counts": E["counts"], "expressed": E["expressed"], "u_dmso": E["u_dmso"], "u_dm": E["u_dm"],
                    "eff": E["eff"], "posunc": None, "r2": E["r2"]}
            wr.write_table(gene_rows(prof, s, vals, int_counts).cast(schema), row_group_size=prof.P)
            nd = ctx.B.shape[0]
            ddv = {"DD_lfc": E["ddl"], "DD_z": E["ddz"], "DD_qup": np.full(nd, np.nan), "DD_qdn": np.full(nd, np.nan),
                   "DD_poseff": TW.Grid.dd_mean(ctx.B, np.nan_to_num(E["eff"])[:, None])[:, 0], "DD_posunc": None}
            dvals = {"u_dm": E["u_dm"], "u_dmso": E["u_dmso"], "r2": E["r2"], "W1": E["W1"],
                     "poff": np.full(ctx.NW, np.nan), "counts": E["counts"]}
            dtabs.append(drugdose_rows(ctx, s, dvals, ddv))
            btabs.append(baseline_rows(ctx, s, E["base"], E["dy"], E["dmc"]))
            idx_rows.append({"gene": s, "symbol": s, "kind": "extra (not an atlas gene)", "atlas_col": -1,
                             "token": int(E["token"]), "file": "per_profile/extra_genes.parquet", "row_group": j,
                             "drugdose_file": "per_drugdose/extra_genes.parquet",
                             "baselines_file": "plate_baselines/extra_genes.parquet", "pooled_cpm": np.nan,
                             "median_line_cpm": np.nan, "n_lines_expressing": ctx.L,
                             "correction_path": "extra gene: upstream_tf.corrected_effects (its own two-pass position "
                                                "correction; kept in every line)"})
        wr.close()
        os.replace(F["per_profile"] + ".tmp", F["per_profile"])
        write_parquet(pa.concat_tables(dtabs, promote_options="permissive"), F["per_drugdose"],
                      row_group_size=ctx.B.shape[0])
        write_parquet(pa.concat_tables(btabs, promote_options="permissive"), F["plate_baselines"],
                      row_group_size=len(ctx.plates) * ctx.L)
    for f in glob.glob(os.path.join(sdir, "*", "chunk_*.parquet")):    # chunks of an earlier, larger layout
        if int(os.path.basename(f)[6:10]) >= nch:
            os.remove(f)
    write_csv(pd.DataFrame(idx_rows), os.path.join(sdir, "genes.csv"))
    names = ("r2_vs_source", "W2", "DD_lfc")
    agg = {}
    for nm in names:
        vals = [c[nm] for c in chk_all if nm in c]
        d = [v[0] for v in vals if v[0] == v[0]]
        agg[nm] = (max(d) if d else float("nan"), int(sum(v[1] for v in vals)), int(sum(v[2] for v in vals)))
    src = "genome_wide's tensor" if tensor is not None else "upstream_tf.plate_r2 in the pass that built the store"
    ck.add(f"r2 ({src}) vs u_drugmedian - composition_shift - position_effect recomputed: max |diff|",
           agg["r2_vs_source"][0], agg["r2_vs_source"][1], f"finite-pattern mismatches {agg['r2_vs_source'][2]}")
    ck.add("median over lines of r2 vs atlas W2, all wells and store genes: max |diff|", agg["W2"][0], agg["W2"][1],
           f"finite-pattern mismatches {agg['W2'][2]}")
    ck.add("drug-dose mean of the per-well median of r2 vs atlas DD_lfc: max |diff|", agg["DD_lfc"][0],
           agg["DD_lfc"][1], f"finite-pattern mismatches {agg['DD_lfc'][2]}")
    log(f"gene store {sdir}: {len(cols)} atlas genes + {len(extra_res)} extra, {prof.P} profiles per gene "
        f"({time.time() - t0:.0f} s)")
    return prof


class Store:
    """Read access to a gene store by gene (label or symbol): one row group per gene."""

    def __init__(self, sdir):
        self.d = sdir
        self.idx = pd.read_csv(os.path.join(sdir, "genes.csv"))
        self.by = {}
        for r in self.idx.itertuples():
            self.by.setdefault(str(r.gene), r)
        for r in self.idx.itertuples():
            self.by.setdefault(str(r.symbol), r)
        self.prof = pq.read_table(os.path.join(sdir, "profiles.parquet")).to_pandas()
        self._pf = {}

    def has(self, g):
        return str(g) in self.by

    def _file(self, rel):
        if rel not in self._pf:
            self._pf[rel] = pq.ParquetFile(os.path.join(self.d, rel))
        return self._pf[rel]

    def rows(self, g):
        r = self.by[str(g)]
        return self._file(r.file).read_row_group(int(r.row_group))

    def drugdose(self, g):
        r = self.by[str(g)]
        return self._file(r.drugdose_file).read_row_group(int(r.row_group))

    def baselines(self, g):
        r = self.by[str(g)]
        return self._file(r.baselines_file).read_row_group(int(r.row_group))

    def entry(self, g):
        return self.by[str(g)]


# ============================================================================= per-gene tables
def to_grid(ctx, prof, v, fill=np.nan, dtype=np.float64):
    out = np.full((ctx.NW, ctx.L), fill, dtype=dtype)
    out[prof["_w"], prof["_l"]] = v
    return out


def full_profile_frame(ctx, store, g):
    """(2) for one gene: every profile, raw, uncorrected, correction terms, corrected, flags (pandas DataFrame)."""
    t = store.rows(g).to_pandas()
    p = store.prof
    e = store.entry(g)
    cnt = t["umi_count"].to_numpy(np.float64)
    tot = t["total_umi"].to_numpy(np.float64)
    with quiet():
        cpm = np.where(tot > 0, cnt / tot * 1e6, np.nan)
        l2 = np.where(tot > 0, np.log2((cnt + 0.5) / (tot + 1.0) * 1e6), np.nan)
    df = pd.DataFrame({
        "gene": str(e.gene), "plate": t["plate"].astype(str), "well": t["well"].astype(str), "slot": p["slot"],
        "sample": p["sample"].astype(str), "drug": t["drug"].astype(str), "concentration_uM": t["concentration_uM"],
        "is_dmso": t["is_dmso"], "well_used": t["well_used"], "drug_dose_row": p["drug_dose_row"],
        "unreliable_plate": p["unreliable_plate"], "cell_line_id": t["cell_line_id"].astype(str),
        "cell_name": p["cell_name"].astype(str), "tp53_group": p["tp53_group"].astype(str),
        "n_cells": t["n_cells"], "umi_count": t["umi_count"], "total_umi": t["total_umi"], "cpm": cpm,
        "log2cpm": l2.astype(np.float32), "usable": t["usable"], "expressed": t["expressed"],
        "u_dmso": t["u_dmso"], "u_drugmedian": t["u_drugmedian"], "composition_shift": p["composition_shift"],
        "position_effect": t["position_effect"], "posunc": t["posunc"], "r2": t["r2"],
        "correction_path": str(e.correction_path)})
    return df


def well_index(ctx, store):
    p = store.prof
    if "_w" not in p:
        wi = {s: i for i, s in enumerate(ctx.w["sample"].astype(str))}
        li = {s: i for i, s in enumerate(ctx.lines)}
        p["_w"] = p["sample"].astype(str).map(wi).to_numpy(int)
        p["_l"] = p["cell_line_id"].astype(str).map(li).to_numpy(int)
    return p


def per_gene_grids(ctx, store, g):
    """(wells x lines) arrays of one gene from its store rows."""
    p = well_index(ctx, store)
    t = store.rows(g)
    out = {}
    for c in ("umi_count", "n_cells", "total_umi", "u_dmso", "u_drugmedian", "position_effect", "r2"):
        v = t.column(c).to_numpy(zero_copy_only=False).astype(np.float64)
        out[c] = to_grid(ctx, p, v, fill=0.0 if c in ("umi_count", "n_cells", "total_umi") else np.nan)
    out["composition_shift"] = to_grid(ctx, p, p["composition_shift"].to_numpy(np.float64))
    out["exists"] = to_grid(ctx, p, 1.0, fill=0.0) > 0
    out["expressed"] = np.zeros(ctx.L, bool)
    ex = t.column("expressed").to_numpy(zero_copy_only=False)
    out["expressed"][p["_l"].to_numpy()[ex]] = True
    return out


def per_drugdose_line(ctx, gr, gene):
    """Per (drug-dose, line): means over the drug-dose's used wells (as trim72_ida_per_line's per_line and two_way's
    Grid.dd_mean), sums of counts, UMIs and cells over the used wells. Which wells each mean uses:
      r2_mean, u_drugmedian_mean_r2wells, composition_shift_mean, position_effect_mean: the n_wells_r2 used wells where
          the line has an r2 value, so that r2_mean = u_drugmedian_mean_r2wells - composition_shift_mean -
          position_effect_mean exactly (the corrections shown are the ones that produced r2_mean);
      u_drugmedian_mean: the n_wells_u used wells where the line has a u_drugmedian value (usable and expressed: also
          wells whose well-level value is missing, < MIN_LINES lines);
      u_dmso_mean: the n_wells_u_dmso used wells where the line has a u_dmso value (also needs >= MIN_CELLS pooled DMSO
          cells of the line on the plate)."""
    B = ctx.B
    nd, L = B.shape[0], ctx.L
    r2w = np.isfinite(gr["r2"])
    res = {"r2_mean": TW.Grid.dd_mean(B, gr["r2"]),
           "u_drugmedian_mean": TW.Grid.dd_mean(B, gr["u_drugmedian"]),
           "u_dmso_mean": TW.Grid.dd_mean(B, gr["u_dmso"])}
    for c, nm in (("u_drugmedian", "u_drugmedian_mean_r2wells"), ("composition_shift", "composition_shift_mean"),
                  ("position_effect", "position_effect_mean")):
        res[nm] = TW.Grid.dd_mean(B, np.where(r2w, gr[c], np.nan))
    nw = np.asarray(B @ r2w.astype(float))
    nwu = np.asarray(B @ np.isfinite(gr["u_drugmedian"]).astype(float))
    nwo = np.asarray(B @ np.isfinite(gr["u_dmso"]).astype(float))
    cnt = np.asarray(B @ gr["umi_count"])
    tot = np.asarray(B @ gr["total_umi"])
    ncl = np.asarray(B @ gr["n_cells"])
    dd = ctx.fx.dd
    di = np.repeat(np.arange(nd), L)
    li = np.tile(np.arange(L), nd)
    with quiet():
        cpm = np.where(tot > 0, cnt / tot * 1e6, np.nan)
    df = pd.DataFrame({"gene": gene, "drug_dose_row": di, "drug": dd["drug"].astype(str).to_numpy()[di],
                       "concentration_uM": dd["conc"].to_numpy(float)[di], "cell_line_id": np.array(ctx.lines)[li],
                       "cell_name": ctx.line_name[li], "tp53_group": ctx.tp53["tp53_group"].to_numpy()[li],
                       "expressed": gr["expressed"][li], "n_wells_r2": nw.ravel().astype(int),
                       "r2_mean": res["r2_mean"].ravel(), "fold_change": 2.0 ** res["r2_mean"].ravel(),
                       "u_drugmedian_mean_r2wells": res["u_drugmedian_mean_r2wells"].ravel(),
                       "composition_shift_mean": res["composition_shift_mean"].ravel(),
                       "position_effect_mean": res["position_effect_mean"].ravel(),
                       "n_wells_u": nwu.ravel().astype(int), "u_drugmedian_mean": res["u_drugmedian_mean"].ravel(),
                       "n_wells_u_dmso": nwo.ravel().astype(int), "u_dmso_mean": res["u_dmso_mean"].ravel(),
                       "umi_count_sum": cnt.ravel(), "total_umi_sum": tot.ravel(), "n_cells_sum": ncl.ravel(),
                       "cpm_pooled": cpm.ravel()})
    return df, res


def per_well(ctx, store, gr, gene):
    """Per well (DMSO included): atlas W1 / W2 / Z / position effect / posunc / plate_offset of the gene, and the
    medians over lines of the per-profile values."""
    fx = ctx.fx
    e = store.entry(gene)
    w = ctx.w
    with quiet():
        med = {c: np.nanmedian(np.where(gr["exists"], gr[c], np.nan), axis=1)
               for c in ("u_drugmedian", "u_dmso", "r2")}
        r1c = gr["u_drugmedian"] - gr["composition_shift"]
        W1r = np.nanmedian(r1c, axis=1)
    W1r[np.isfinite(r1c).sum(axis=1) < A.MIN_LINES] = np.nan
    nfin = np.isfinite(gr["r2"]).sum(axis=1)
    cnt, tot = gr["umi_count"].sum(axis=1), gr["total_umi"].sum(axis=1)
    if int(e.atlas_col) >= 0:
        c = int(e.atlas_col)
        W1, W2, Z = (np.asarray(getattr(fx, k))[:, c].astype(np.float64) for k in ("W1", "W2", "Z"))
        posunc = np.asarray(fx.posunc)[:, c].astype(bool)
        poff = np.asarray(fx.plate_offset)[ctx.pidx, c].astype(np.float64)
    else:
        W1 = W2 = Z = poff = np.full(ctx.NW, np.nan)
        posunc = np.zeros(ctx.NW, bool)
    with quiet():
        cpm = np.where(tot > 0, cnt / tot * 1e6, np.nan)
    with quiet():
        pe = np.nanmax(gr["position_effect"], axis=1)          # the well's value (the same in every line)
    return pd.DataFrame({
        "gene": gene, "plate": ctx.plate_w, "well": w["well"].fillna("").astype(str).to_numpy(),
        "slot": w["slot"].to_numpy(float), "sample": w["sample"].astype(str).to_numpy(),
        "drug": w["drug"].astype(str).to_numpy(), "concentration_uM": w["conc"].to_numpy(float),
        "is_dmso": ~ctx.drug_w, "well_used": ctx.used, "drug_dose_row": ctx.ddr,
        "n_lines_profile": gr["exists"].sum(axis=1), "n_lines_r2": nfin, "umi_count_sum": cnt, "total_umi_sum": tot,
        "n_cells_sum": gr["n_cells"].sum(axis=1), "cpm_pooled": cpm, "W1_atlas": W1, "W2_atlas": W2, "Z_atlas": Z,
        "position_effect": pe, "posunc": posunc, "plate_dmso_offset": poff,
        "u_drugmedian_median_lines": med["u_drugmedian"], "u_dmso_median_lines": med["u_dmso"],
        "W1_recomputed": W1r, "r2_median_lines": med["r2"]})


def per_drugdose(ctx, store, gene, gflags=None):
    """Per drug-dose: the store's per-drug-dose rows (atlas DD values and the uncorrected medians) with the drug-dose
    description and the gene's atlas flags."""
    t = store.drugdose(gene).to_pandas()
    dd = ctx.fx.dd
    t["gene"] = t["gene"].astype(str)
    t["drug"] = t["drug"].astype(str)
    t.insert(4, "dose", dd["dose"].astype(str).to_numpy())
    t.insert(6, "plates", dd["plates"].astype(str).to_numpy())
    t.insert(7, "wells", dd["wells"].astype(str).to_numpy())
    t["fold_change"] = 2.0 ** t["DD_lfc"].astype(float)
    for c in ("cells_log2_vs_plate", "cells_log2_best_well"):     # cell loss (24 h survivors), from the atlas
        t[c] = dd[c].to_numpy(float) if c in dd else np.nan
    t["flags"] = gflags if gflags is not None else ""
    for c in ("moa_broad", "moa_fine", "targets"):
        t[c] = dd[c].astype(str).to_numpy() if c in dd else ""
    return t


def wide(ctx, df, col):
    m = df.pivot(index="drug_dose_row", columns="cell_line_id", values=col)
    m = m.reindex(index=np.arange(ctx.B.shape[0]), columns=ctx.lines)
    dd = ctx.fx.dd
    out = pd.DataFrame({"drug_dose_row": m.index.to_numpy(), "drug": dd["drug"].astype(str).to_numpy(),
                        "concentration_uM": dd["conc"].to_numpy(float)})
    return pd.concat([out, m.reset_index(drop=True)], axis=1)


def gene_flags(ctx, store, gene):
    e = store.entry(gene)
    if int(e.atlas_col) < 0:
        return ""
    with quiet():
        return A.gene_flag_col(ctx.fx, int(e.atlas_col))


def exposure_tables(ctx, store, gene, folder):
    """<GENE>/: per profile (CSV), per well, per (drug-dose, line), per drug-dose and the drug-dose x line matrices."""
    files = {}
    f = full_profile_frame(ctx, store, gene)
    files["per_profile"] = os.path.join(folder, f"{gene}_per_profile.csv")
    write_csv(f, files["per_profile"])
    gr = per_gene_grids(ctx, store, gene)
    pw = per_well(ctx, store, gr, gene)
    files["per_well"] = os.path.join(folder, f"{gene}_per_well.csv")
    write_csv(pw, files["per_well"])
    dl, _res = per_drugdose_line(ctx, gr, gene)
    files["per_drugdose_line"] = os.path.join(folder, f"{gene}_per_drugdose_line.csv")
    write_csv(dl, files["per_drugdose_line"])
    pdd = per_drugdose(ctx, store, gene, gene_flags(ctx, store, gene))
    files["per_drugdose"] = os.path.join(folder, f"{gene}_per_drugdose.csv")
    write_csv(pdd, files["per_drugdose"])
    for col, nm in (("r2_mean", "r2"), ("u_drugmedian_mean", "u_drugmedian"), ("u_dmso_mean", "u_dmso")):
        files[f"matrix_{nm}"] = os.path.join(folder, f"{gene}_matrix_{nm}.csv")
        write_csv(wide(ctx, dl, col), files[f"matrix_{nm}"])
    return files, f, pw, dl, pdd


def set_tables(ctx, store, genes, folder, why):
    """genes_per_profile.parquet (the store's per-profile rows + correction_path), genes_per_drugdose_line.parquet,
    genes_per_drugdose.parquet and .csv.gz for a gene set (one row group per gene)."""
    pp = os.path.join(folder, "genes_per_profile.parquet")
    pl = os.path.join(folder, "genes_per_drugdose_line.parquet")
    pd_ = os.path.join(folder, "genes_per_drugdose.parquet")
    os.makedirs(folder, exist_ok=True)
    w1 = w2 = None
    dds = []
    for g in genes:
        t = store.rows(g)
        t = t.append_column("correction_path", dict_col([str(store.entry(g).correction_path)],
                                                        np.zeros(t.num_rows, np.int32)))
        if w1 is None:
            w1 = row_writer(pp + ".tmp", t.schema)
        w1.write_table(t.cast(w1.schema), row_group_size=t.num_rows)
        gr = per_gene_grids(ctx, store, g)
        dl, _ = per_drugdose_line(ctx, gr, str(store.entry(g).gene))
        tl = pa.Table.from_pandas(dl, preserve_index=False)
        if w2 is None:
            w2 = pq.ParquetWriter(pl + ".tmp", tl.schema, **PQ,
                                  use_dictionary=[f.name for f in tl.schema if pa.types.is_string(f.type)])
        w2.write_table(tl.cast(w2.schema), row_group_size=tl.num_rows)
        dds.append(per_drugdose(ctx, store, g, gene_flags(ctx, store, g)))
    if w1 is not None:
        w1.close()
        w2.close()
        os.replace(pp + ".tmp", pp)
        os.replace(pl + ".tmp", pl)
    D = pd.concat(dds, ignore_index=True) if dds else pd.DataFrame()
    if len(D):
        D = D.merge(why[["gene", "reasons"]], on="gene", how="left")
        write_parquet(pa.Table.from_pandas(D, preserve_index=False), pd_)
        write_csv(D, os.path.join(folder, "genes_per_drugdose.csv.gz"), gz=True)
    return [pp, pl, pd_] if len(D) else []


def set_scores(ctx, store, members, prof):
    """Per (well, line): the mean over a set's genes of r2, u_drugmedian and u_dmso (NaN-aware: the members the line
    expresses, as genome_wide.set_means), and how many members had a value."""
    S = {c: np.zeros((ctx.NW, ctx.L)) for c in ("r2", "u_drugmedian", "u_dmso")}
    N = {c: np.zeros((ctx.NW, ctx.L)) for c in S}
    for g in members:
        gr = per_gene_grids(ctx, store, g)
        for c in S:
            f = np.isfinite(gr[c])
            S[c] += np.where(f, gr[c], 0.0)
            N[c] += f
    with quiet():
        return {c: np.where(N[c] > 0, S[c] / N[c], np.nan) for c in S}, N["r2"]


# ============================================================================= metadata
def genotype_map(ctx):
    feats = A.genotype_features(ctx.fx)
    per = {i: [] for i in range(ctx.L)}
    for k in sorted(feats):
        for i in feats[k]:
            per[int(i)].append(k)
    return feats, per


def meta_tables(ctx, side, xpos, xlabel, xatlas_col, mdir, extra_x=None):
    """metadata/: cell_lines.csv, drugs.csv, wells.csv, drug_doses.csv, plates.csv."""
    fx = ctx.fx
    data = ctx.data
    feats, per = genotype_map(ctx)
    ln = fx.lines
    cl = pd.DataFrame({"cell_line_id": ctx.lines, "cell_name": ln["cell_name"].astype(str).to_numpy(),
                       "depmap_id": ln["Cell_ID_DepMap"].fillna("").astype(str).to_numpy() if "Cell_ID_DepMap" in ln
                       else "", "organ": ln["Organ"].astype(str).to_numpy(), "drivers": ln["drivers"].astype(str),
                       "driver_changes": ln["driver_changes"].astype(str),
                       "genotype_features": ["; ".join(per[i]) for i in range(ctx.L)]})
    for c in ("tp53_group", "tp53_status", "tp53_changes", "tp53_source"):
        cl[c] = ctx.tp53[c].to_numpy()
    for c in ("n_cells_total", "in_growth_analysis", "wells_usable", "pct_wells_usable"):
        cl[c] = ln[c].to_numpy() if c in ln else np.nan
    G = xlabel
    if xpos is not None:
        dmc = side["dmc"][:, :, xpos]
        dk = side["dmk"]
    else:
        dmc = extra_x["dmc"]
        dk = side["dmk"]
    dmt = side["dmt"]
    relp = np.array([p not in fx.unreliable for p in ctx.plates], bool)     # plates the atlas treats as reliable
    with quiet():
        lv = np.where((side["dmn"] >= A.MIN_CELLS), np.log2((dmc + 0.5 * np.maximum(dk, 1)) /
                                                             (dmt + np.maximum(dk, 1)) * 1e6), np.nan)
        for suf, pm in (("", np.ones(len(ctx.plates), bool)), ("_reliable_plates", relp)):
            umi = dmc[pm].sum(axis=0)
            tt = dmt[pm].sum(axis=0)
            cl[f"{G}_umi_dmso{suf}"] = umi
            cl[f"{G}_total_umi_dmso{suf}"] = tt
            cl[f"{G}_cpm_dmso{suf}"] = np.where(tt > 0, umi / tt * 1e6, np.nan)
            cl[f"{G}_log2cpm_dmso_median_plates{suf}"] = np.nanmedian(lv[pm], axis=0) if pm.any() else np.nan
    if xatlas_col is not None:
        cl[f"{G}_cpm_all_wells"] = np.asarray(fx.line_cpm)[:, xatlas_col]
        cl[f"{G}_expressed"] = np.asarray(fx.expr_mask)[:, xatlas_col].astype(bool)
    else:
        cl[f"{G}_cpm_all_wells"] = np.nan
        cl[f"{G}_expressed"] = True
    write_csv(cl, os.path.join(mdir, "cell_lines.csv"))
    fl = pd.DataFrame([(k, ctx.lines[i], ctx.line_name[i]) for k in sorted(feats) for i in sorted(feats[k])],
                      columns=["feature", "cell_line_id", "cell_name"])
    # drugs
    dd = fx.dd
    dm = pd.read_parquet(os.path.join(data, "metadata", "drug_metadata.parquet"))
    dm["_key"] = dm["drug"].astype(str).str.strip()
    dm = dm.drop_duplicates("_key").set_index("_key")
    w = ctx.w
    rows = []
    for d, g in w.groupby(w["drug"].astype(str), sort=True):
        k = d.strip()
        m = dm.loc[k] if k in dm.index else None
        gd = dd[dd["drug"].astype(str) == d]

        def get(c):
            return "" if m is None or c not in m or pd.isna(m[c]) else m[c]
        rows.append({"drug": d, "is_dmso": bool(g["is_dmso"].astype(bool).all()), "in_drug_metadata": m is not None,
                     "moa_broad": get("moa-broad"), "moa_fine": get("moa-fine"), "targets": get("targets"),
                     "human_approved": get("human-approved"), "clinical_trials": get("clinical-trials"),
                     "pubchem_cid": get("pubchem_cid"), "canonical_smiles": get("canonical_smiles"),
                     "n_doses": int(len(gd)),
                     "concentrations_uM": ";".join(f"{c:g}" for c in sorted(g["conc"].astype(float).unique())),
                     "n_wells": int(len(g)), "plates": ",".join(sorted(g["plate"].astype(str).unique(),
                                                                         key=lambda s: (len(s), s)))})
    drugs = pd.DataFrame(rows)
    write_csv(drugs, os.path.join(mdir, "drugs.csv"))
    # wells (failed wells included)
    nlp = (side["nc"] > 0).sum(axis=1)
    nlu = (side["nc"] >= A.MIN_CELLS).sum(axis=1)
    rel = fx.reliable_w
    st, rs = [], []
    for i in range(ctx.NW):
        r = []
        if not ctx.drug_w[i]:
            s = "DMSO control (the plate's DMSO reference of u_dmso and plate_offset; in no drug-dose)"
        elif ctx.used[i]:
            s = "used"
        else:
            s = "excluded: unreliable plate (its drug-dose has wells on reliable plates)" if not rel[i] else \
                "excluded: not in a drug-dose"
        if not rel[i]:
            r.append("unreliable plate")
            if ctx.used[i]:
                r.append("used although on an unreliable plate (its drug-dose has no reliable well)")
        if "position_not_correctable" in w and str(w["position_not_correctable"].iloc[i]).lower() == "true":
            r.append(f"position not correctable (< {A.T.MIN_SLOT_WELLS} other-drug wells at the position: no "
                     "position correction)")
        if nlu[i] < A.MIN_LINES:
            r.append(f"too few usable lines (< {A.MIN_LINES} with >= {A.MIN_CELLS} cells): no well-level effect, r2 "
                     "empty")
        st.append(s)
        rs.append("; ".join(r))
    W = pd.DataFrame({"sample": w["sample"].astype(str), "plate": ctx.plate_w, "well": w["well"].fillna("").astype(str),
                      "slot": w["slot"], "drug": w["drug"].astype(str), "concentration_uM": w["conc"].astype(float),
                      "is_dmso": ~ctx.drug_w, "in_atlas": True, "status": st, "reasons": rs,
                      "used_in_drugdose": ctx.used, "drug_dose_row": ctx.ddr, "unreliable_plate": ~rel,
                      "cells": w["cells"] if "cells" in w else np.nan, "n_lines_with_profile": nlp,
                      "n_lines_usable": nlu})
    for c in ("position_not_correctable", "position_wells_used", "plate_scale_group", "plate_scale",
              "composition_shift_log2", "cells_log2_vs_plate", "umi_per_cell", "genes_per_cell"):
        W[c] = w[c].to_numpy() if c in w else np.nan
    fpath = os.path.join(data, "atlas", "effects", "failed_wells.csv")
    if os.path.exists(fpath):
        fw = pd.read_csv(fpath, dtype={"sample": str, "plate": str})
        if len(fw):
            F = pd.DataFrame({"sample": fw["sample"].astype(str), "plate": fw["plate"].astype(str),
                              "well": fw["well"].fillna("").astype(str) if "well" in fw else "",
                              "slot": fw["slot"] if "slot" in fw else np.nan, "drug": fw["drug"].astype(str),
                              "concentration_uM": fw["conc"].astype(float), "is_dmso": fw["is_dmso"].astype(bool),
                              "in_atlas": False,
                              "status": "excluded: failed well (dropped by the atlas: < 1/8 of the plate's typical "
                                        "cells while the same drug kept >= half at the same or a higher dose "
                                        "elsewhere)",
                              "reasons": "failed well", "used_in_drugdose": False, "drug_dose_row": -1,
                              "unreliable_plate": fw["plate"].astype(str).isin(fx.unreliable).to_numpy(),
                              "cells": fw["n_cells"] if "n_cells" in fw else np.nan, "n_lines_with_profile": 0,
                              "n_lines_usable": 0})
            F["cells_log2_vs_plate"] = fw["cells_log2_vs_plate"].to_numpy() if "cells_log2_vs_plate" in fw else np.nan
            W = pd.concat([W, F], ignore_index=True)
    order = {p: i for i, p in enumerate(ctx.plates)}
    W["_o"] = W["plate"].map(order).fillna(99)
    W = W.sort_values(["_o", "slot", "sample"], kind="stable").drop(columns="_o")
    write_csv(W, os.path.join(mdir, "wells.csv"))
    # drug-doses
    keep = ["drug", "dose", "conc", "n_wells", "n_wells_all", "plates", "wells", "wells_left_out",
            "unreliable_plate_only", "position_not_correctable", "flags", "cells_log2_vs_plate",
            "umi_per_cell_log2_vs_plate", "genes_per_cell_log2_vs_plate", "composition_shift_log2",
            "cells_log2_best_well", "plate_scale", "n_sig_genes", "n_genes_up", "n_genes_down", "replicate_r",
            "moa_broad", "moa_fine", "targets"]
    D = dd[[c for c in keep if c in dd]].copy()
    D.insert(0, "drug_dose_row", np.arange(len(D)))
    D = D.rename(columns={"conc": "concentration_uM", "n_wells": "n_wells_used"})
    write_csv(D, os.path.join(mdir, "drug_doses.csv"))
    # plates
    prow = []
    for pi, p in enumerate(ctx.plates):
        ii = np.flatnonzero(ctx.pidx == pi)
        doses = sorted(w["conc"].iloc[ii][ctx.drug_w[ii]].astype(float).unique())
        nfail = int((W["plate"].eq(p) & ~W["in_atlas"]).sum())
        prow.append({"plate": p, "unreliable": p in fx.unreliable, "n_wells_in_atlas": len(ii),
                     "n_dmso_wells": int((~ctx.drug_w[ii]).sum()), "n_drug_wells_used": int(ctx.used[ii].sum()),
                     "n_failed_wells": nfail, "drug_concentrations_uM": ";".join(f"{c:g}" for c in doses),
                     f"{G}_plate_dmso_offset": (float(np.asarray(fx.plate_offset)[pi, xatlas_col])
                                                if xatlas_col is not None else np.nan)})
    write_csv(pd.DataFrame(prow), os.path.join(mdir, "plates.csv"))
    return cl, fl, drugs, W, D


# ============================================================================= Tahoe's DESeq2 table
def deseq2_files(data):
    return sorted(glob.glob(os.path.join(data, "metadata", "pseudobulk_differential_expression", "*.parquet")))


def plate_atlas(col):
    """Tahoe's DESeq2 plate value ('4', 4 or 'plate4') as the atlas names it ('plate4')."""
    s = pc.utf8_trim_whitespace(pc.cast(col, pa.string()))
    s = pc.replace_substring_regex(s, pattern=r"^(\d+)\.0$", replacement=r"\1")
    num = pc.match_substring_regex(s, pattern=r"^\d+$")
    return pc.if_else(num, pc.binary_join_element_wise(pa.scalar("plate"), s, ""), s)


def stored_precision(col):
    """A numeric Arrow column as float64 at the precision it was stored with: float32 values become the float64 of
    their shortest float32 text (a float32 0.05 -> 0.05, not 0.05000000074505806), so they equal the export's
    concentrations; float64 stays as it is."""
    a = pc.cast(col, pa.float64()).to_numpy(zero_copy_only=False)
    if not pa.types.is_float32(col.type) and not pa.types.is_float16(col.type):
        return a
    u, inv = np.unique(a, return_inverse=True)
    v = np.array([float(str(np.float32(x))) if np.isfinite(x) else x for x in u], dtype=np.float64)
    return v[inv.ravel()]


UNIT_TO_UM = {"": 1.0, "um": 1.0, "µm": 1.0, "μm": 1.0, "micromolar": 1.0, "nm": 1e-3, "mm": 1e3}


def dict_codes(a):
    """An Arrow string column as (codes: int64, -1 for null; its distinct values)."""
    if isinstance(a, pa.ChunkedArray):
        a = a.combine_chunks()
    d = pc.dictionary_encode(a)
    return (np.asarray(pc.fill_null(d.indices, -1).to_numpy(zero_copy_only=False), dtype=np.int64),
            d.dictionary.to_pylist())


def deseq2_keys(ctx):
    """The atlas's join keys for Tahoe's DESeq2 rows: (drug, concentration uM) -> drug_dose_row; Cellosaurus ids; DepMap
    id -> Cellosaurus id (Cell_ID_Cellosaur may be missing from the files)."""
    dd = ctx.fx.dd
    ddk = {}
    for i, (d, c) in enumerate(zip(dd["drug"].astype(str), dd["conc"].astype(float))):
        ddk.setdefault((d.strip(), round(c, 6)), i)
    ln = ctx.fx.lines
    dep = {}
    if "Cell_ID_DepMap" in ln:
        for c, d in zip(ln["cell_line_id"].astype(str), ln["Cell_ID_DepMap"].astype(str)):
            if d and d != "nan":
                dep.setdefault(d.strip(), c)
    return {"dd": ddk, "cello": set(ctx.lines), "depmap": dep}


def deseq2_extract(files, genes, folder, exposure, keys=None):
    """One streamed pass over Tahoe's pseudobulk DESeq2 files: per row group, the gene_name column first (row groups
    whose gene_name statistics cannot hold a wanted gene are skipped), then the other columns of the matching rows
    only. Writes genes.parquet (all wanted genes) and <exposure>_deseq2.csv; returns rows per gene. keys
    (deseq2_keys) adds the atlas's join keys: concentration_uM, drug_dose_row, cell_line_id."""
    keys = keys or {"dd": {}, "cello": set(), "depmap": {}}
    kdd = keys["dd"]
    want = sorted(set(genes))
    vs = pa.array(want, pa.string())
    out_schema = pa.schema([("gene_name", pa.string()), ("baseMean", pa.float64()), ("log2FoldChange", pa.float64()),
                            ("lfcSE", pa.float64()), ("stat", pa.float64()), ("pvalue", pa.float64()),
                            ("padj", pa.float64()), ("plate", pa.string()), ("plate_atlas", pa.string()),
                            ("n_cells_trt", pa.int64()), ("n_cells_ctrl", pa.int64()),
                            ("Cell_ID_Cellosaur", pa.string()), ("Cell_ID_DepMap", pa.string()), ("drug", pa.string()),
                            ("concentration", pa.float64()), ("concentration_unit", pa.string()),
                            ("Cell_Name_Vevo", pa.string()), ("concentration_uM", pa.float64()),
                            ("drug_dose_row", pa.int32()), ("cell_line_id", pa.string()),
                            ("source_file", pa.string())])
    path = os.path.join(folder, "genes.parquet")
    os.makedirs(folder, exist_ok=True)
    wr = pq.ParquetWriter(path + ".tmp", out_schema, **PQ,
                          use_byte_stream_split=[f.name for f in out_schema if pa.types.is_floating(f.type)],
                          use_dictionary=[f.name for f in out_schema if pa.types.is_string(f.type)])
    xrows, counts = [], {}
    n_rg = n_skip = n_read = n_nodd = n_nocl = 0
    t0 = time.time()
    for k, f in enumerate(files):
        pf = pq.ParquetFile(f)
        names = pf.schema_arrow.names
        miss = [c for c in DESEQ_NEED if c not in names]
        if miss:
            raise ValueError(f"{f}: missing columns {miss}")
        gi = pf.metadata.schema.names.index("gene_name") if "gene_name" in pf.metadata.schema.names else None
        gtype = pf.schema_arrow.field("gene_name").type
        # row-group statistics are used only for a plain text / bytes gene_name column (bytes decoded: a BYTE_ARRAY
        # without the UTF8 annotation reports bytes, whose str() would skip every row group)
        use_stats = gi is not None and (pa.types.is_string(gtype) or pa.types.is_large_string(gtype)
                                        or pa.types.is_binary(gtype) or pa.types.is_large_binary(gtype))
        cols = [c for c in DESEQ_COLS if c in names]
        for rg in range(pf.num_row_groups):
            n_rg += 1
            st = pf.metadata.row_group(rg).column(gi).statistics if use_stats else None
            if st is not None and st.has_min_max:
                lo, hi = st.min, st.max
                lo = lo.decode("utf-8", "replace") if isinstance(lo, (bytes, bytearray)) else str(lo)
                hi = hi.decode("utf-8", "replace") if isinstance(hi, (bytes, bytearray)) else str(hi)
                if not any(lo <= g <= hi for g in want):
                    n_skip += 1
                    continue
            gcol = pf.read_row_group(rg, columns=["gene_name"]).column(0)
            if pa.types.is_dictionary(gcol.type):
                gcol = pc.cast(gcol, gcol.type.value_type)
            m = pc.is_in(pc.cast(gcol, pa.string()), value_set=vs)
            if not pc.any(m).as_py():
                continue
            t = pf.read_row_group(rg, columns=cols).filter(m)
            n_read += t.num_rows
            arrs = {}
            for fld in out_schema:
                c = fld.name
                if c == "plate":
                    arrs[c] = pc.cast(t.column("plate"), pa.string())
                elif c == "plate_atlas":
                    arrs[c] = plate_atlas(t.column("plate"))
                elif c == "source_file":
                    arrs[c] = pa.array([os.path.basename(f)] * t.num_rows, pa.string())
                elif c == "concentration":
                    arrs[c] = pa.array(stored_precision(t.column(c)), pa.float64())
                elif c in ("concentration_uM", "drug_dose_row", "cell_line_id"):
                    continue
                elif c in t.column_names:
                    col = t.column(c)
                    if pa.types.is_dictionary(col.type):
                        col = pc.cast(col, col.type.value_type)
                    arrs[c] = pc.cast(col, fld.type)
                else:
                    arrs[c] = pa.nulls(t.num_rows, fld.type)
            # the atlas's join keys (mapped on the few distinct values, then taken back to the rows)
            ui, uv = dict_codes(arrs["concentration_unit"])
            fac = np.array([UNIT_TO_UM.get(str(v).strip().lower(), np.nan) for v in uv] + [1.0])[ui]  # null: uM
            cum = arrs["concentration"].to_numpy(zero_copy_only=False) * fac
            di, dv = dict_codes(arrs["drug"])
            cu, cix = np.unique(np.round(cum, 6), return_inverse=True)
            n_c = max(len(cu), 1)
            code = np.where(di >= 0, di, -1) * n_c + cix.ravel()
            uc, inv = np.unique(code, return_inverse=True)
            look = np.array([kdd.get((str(dv[k // n_c]).strip() if k // n_c >= 0 else "", float(cu[k % n_c])), -1)
                             for k in uc.tolist()], dtype=np.int32)
            ddr = look[inv.ravel()] if len(uc) else np.zeros(0, np.int32)
            c1, v1 = dict_codes(arrs["Cell_ID_Cellosaur"])
            c2, v2 = dict_codes(arrs["Cell_ID_DepMap"])
            code = (c1 + 1) * (len(v2) + 1) + (c2 + 1)
            uc, inv = np.unique(code, return_inverse=True)
            vals = []
            for k in uc.tolist():
                a1, a2 = k // (len(v2) + 1) - 1, k % (len(v2) + 1) - 1
                c_ = v1[a1] if a1 >= 0 else None
                vals.append(c_ if c_ in keys["cello"] else keys["depmap"].get(str(v2[a2]).strip(), "") if a2 >= 0
                            else "")
            cid = np.array(vals, dtype=object)[inv.ravel()] if len(uc) else np.zeros(0, object)
            arrs["concentration_uM"] = pa.array(cum, pa.float64(), from_pandas=True)
            arrs["drug_dose_row"] = pa.array(ddr, pa.int32())
            arrs["cell_line_id"] = pa.array(cid, pa.string())
            tt = pa.table({fld.name: arrs[fld.name] for fld in out_schema}, schema=out_schema)
            n_nodd += int((ddr < 0).sum())
            n_nocl += int((cid == "").sum())
            wr.write_table(tt)
            for vc in pc.value_counts(tt.column("gene_name")).to_pylist():
                counts[vc["values"]] = counts.get(vc["values"], 0) + int(vc["counts"])
            xm = pc.equal(tt.column("gene_name"), exposure)
            if pc.any(xm).as_py():
                xrows.append(tt.filter(xm))
        if (k + 1) % 50 == 0:
            log(f"  DESeq2: {k + 1}/{len(files)} files ({time.time() - t0:.0f} s; rows kept {n_read:,}; peak RSS "
                f"{UT.peak_gb():.2f} GB)")
    wr.close()
    os.replace(path + ".tmp", path)
    X = pa.concat_tables(xrows).to_pandas() if xrows else pd.DataFrame(columns=out_schema.names)
    X = X.sort_values(["drug", "concentration_uM", "plate_atlas", "cell_line_id", "Cell_ID_DepMap"], kind="stable")
    write_csv(X, os.path.join(folder, f"{exposure}_deseq2.csv"))
    return counts, {"files": len(files), "row_groups": n_rg, "row_groups_skipped_by_statistics": n_skip,
                    "rows_kept": n_read, "rows_without_drug_dose_row": n_nodd, "rows_without_cell_line_id": n_nocl,
                    "seconds": round(time.time() - t0, 1)}


# ============================================================================= main
def as_bool_env(v, default=True):
    if v is None or str(v).strip() == "":
        return default
    return str(v).strip().lower() not in ("0", "false", "no", "off")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--gene", default=os.environ.get("MG53_GW_EXPOSURE") or GENE,
                    help="the exposure gene (default $MG53_GW_EXPOSURE, else TRIM72)")
    ap.add_argument("--no-all-genes", action="store_true", help="leave out all_genes/ (~21 GB on the real data); "
                    "also MG53_EXPORT_ALL_GENES=0")
    ap.add_argument("--chunk", type=int, default=256, help="genes per all_genes Parquet file (default 256)")
    ap.add_argument("--locus-genes", default=None, help="locus genes (comma list; default FUS,PYCARD-AS1,ITGAM for "
                    "TRIM72, else none); non-atlas genes go through the extra-gene path")
    ap.add_argument("--coreg-dir", default=None, help="upstream_coregulation tables (default <out>/../"
                    "upstream_coregulation/tables, used only for TRIM72)")
    ap.add_argument("--gw-dir", default=None, help="genome_wide's folder (default <out>/../genome_wide)")
    ap.add_argument("--redo", action="store_true", help="forget the finished parts and rebuild everything")
    a = ap.parse_args()
    t_all = time.time()
    data = os.path.abspath(os.path.expanduser(a.data))
    out = os.path.abspath(os.environ.get("MG53_OUT") or os.path.join(data, "mg53_p53", "export"))
    sib = os.path.dirname(out)
    all_genes = not a.no_all_genes and as_bool_env(os.environ.get("MG53_EXPORT_ALL_GENES"), True)
    gene = a.gene
    for sub in ("atlas", "gene_panel"):                      # never write into the inputs
        r = os.path.realpath(os.path.join(data, sub))
        if os.path.realpath(out) == r or os.path.realpath(out).startswith(r + os.sep):
            sys.exit(f"the output folder {out} lies inside {r}; choose another --out / MG53_OUT")
    log(f"data {data}; out {out}; exposure {gene}; all_genes {'on' if all_genes else 'off'}")
    ctx = Ctx(data, out, sib, a)
    ck = Checks()
    xi = ctx.sym2idx.get(gene)
    if xi is None:
        print(f"{gene} is not an expressed atlas gene in {data} (on the synthetic build TRIM72 has no counts); choose "
              f"--gene / MG53_GW_EXPOSURE", file=sys.stderr, flush=True)
        sys.exit(2)
    xlabel = ctx.glabel[xi]
    gwdir = os.path.abspath(a.gw_dir) if a.gw_dir else os.path.join(sib, "genome_wide")
    coreg_dir = os.path.abspath(a.coreg_dir) if a.coreg_dir else os.path.join(sib, "upstream_coregulation", "tables")
    locus_syms = [s.strip() for s in (a.locus_genes if a.locus_genes is not None
                                      else ",".join(LOCUS_DEFAULTS.get(gene, []))).split(",") if s.strip()]
    # ---------------------------------------------------------------- inputs from the sibling steps (read only)
    gw_ok, gw_stat, gw_exposure, gw_ri = gw_status(gwdir)
    gwtab = os.path.join(gwdir, "tables")
    gw_state, gw_reason = "finished", ""
    if not gw_ok:
        gw_state = "not finished"
        gw_reason = (f"genome_wide has not finished ({rel(gwtab, ctx)} lacks run_info.json, c_screen_genes.csv.gz or "
                     "b_p53_program.csv)")
    elif gw_exposure not in (None, gene):
        gw_ok, gw_state = False, "other exposure"
        gw_reason = f"genome_wide finished for another exposure ({gw_exposure}, not {gene}): its screen and programs are " \
                    "not used"
    screen = read_screen(gwtab) if gw_ok else None
    prog = read_programs(gwtab) if gw_ok else None
    if gw_ok:
        nbad, nchk, ex = gw_tables_mismatch(ctx, screen, prog)
        if nbad:
            gw_ok, gw_state, screen, prog = False, "other atlas", None, None
            gw_reason = (f"genome_wide's tables do not match this atlas ({nbad} of {nchk} rows name another gene at their "
                         f"idx; e.g. {ex}): they were built from another atlas; rerun genome_wide (--steps genome_wide)")
    ck.add("genome_wide tables used", int(gw_ok), note=rel(gwtab, ctx) if gw_ok else f"{rel(gwtab, ctx)}: {gw_reason}")
    co = coreg_tables(ctx, coreg_dir, a.coreg_dir is not None, gene, ck)
    locus = locus_genes(ctx, locus_syms, ck)
    up = upstream_selection(ctx, screen, co, locus, xi)
    down = downstream_selection(ctx, screen, prog, xi)
    extra = sorted({k[1] for k in list(up) + list(down) if isinstance(k, tuple)})
    sel_atlas = sorted({xi} | {k for k in list(up) + list(down) if not isinstance(k, tuple)})
    overlays = GW.overlay_sets(ctx.sym2idx, sib, GW.Checks()) if gw_ok else {}
    ov_atlas = sorted({ctx.sym2idx[s] for syms, _ in overlays.values() for s in syms
                       if isinstance(s, str) and s in ctx.sym2idx})
    store_cols = list(range(ctx.G)) if all_genes else sorted(set(sel_atlas) | set(ov_atlas))
    # ---------------------------------------------------------------- keys and the disk check (nothing written yet)
    man = data_manifest(data)
    kdata = sha(man)
    kstore = sha({"data": kdata, "all": all_genes, "cols": "all" if all_genes else [ctx.glabel[c] for c in store_cols],
                  "extra": extra, "chunk": a.chunk})
    tensor, tnote = valid_tensor(ctx, gwdir)
    need_r2 = tensor is None
    kpass = sha({"store": kstore, "need_r2": need_r2})
    kmeta = sha({"data": kdata, "gene": gene, "store": kstore})
    kgenes = sha({"store": kstore, "gw": gw_stat if gw_ok else None, "gw_reason": gw_reason, "co": sorted(co),
                  "co_stat": {f: stat_of(os.path.join(coreg_dir, f)) for f in sorted(os.listdir(coreg_dir))}
                  if co else None, "gene": gene, "locus": locus_syms, "meta": kmeta,
                  "overlays": {k: [s for s in v[0] if isinstance(s, str)] for k, v in sorted(overlays.items())}})
    dfiles = deseq2_files(data)
    dgenes = deseq2_gene_list(ctx, None, xlabel, up, down, locus)
    kdes = sha({"data": kdata, "files": {os.path.basename(f): stat_of(f) for f in dfiles}, "genes": dgenes})
    sdir = os.path.join(out, "all_genes") if all_genes else os.path.join(out, ".cache", "store")
    mdir = os.path.join(out, "metadata")
    ddir = os.path.join(out, "tahoe_deseq2")
    need_meta = [os.path.join(mdir, f) for f in ("cell_lines.csv", "drugs.csv", "wells.csv", "drug_doses.csv",
                                                 "plates.csv")]
    need_genes = [os.path.join(out, xlabel, f"{xlabel}_per_profile.csv"), os.path.join(out, "upstream", "genes.csv"),
                  os.path.join(out, "downstream", "genes.csv" if gw_ok else "NOTE.md")]
    need_des = [os.path.join(ddir, "NOTE.md")]
    st0 = State(out) if os.path.isdir(os.path.join(out, ".state")) else None
    if a.redo and st0 is not None:
        log("--redo: forgetting every finished part")

    def done0(part, key, need=()):
        return st0 is not None and not a.redo and st0.done(part, key) and all(os.path.exists(p) for p in need)
    store_done = done0("store", kstore) and store_complete(sdir)
    if done0("store", kstore) and not store_done:
        log(f"gene store: marked done but files of {sdir} are missing: rebuilt (chunks still there are kept)")
    P_ = Pass(os.path.join(out, ".cache", "pass"))
    # free disk: the peak of (pass cache + gene store) and of (gene store + gene tables + DESeq2 rows), counting only
    # what this run still writes; what it deletes first (a stale store, a stale pass cache) is credited
    GBy = 1e9
    npf = ctx.NW * ctx.L
    per_gene = npf * EST_BYTES_ROW + ctx.B.shape[0] * 60 + len(ctx.plates) * ctx.L * 30
    credit = cache_new = cache_old = store_rem = 0.0
    other = os.path.join(out, ".cache", "store") if all_genes else os.path.join(out, "all_genes")
    if not store_done:
        if P_.ready(kpass, need_r2) and not a.redo:          # --redo clears the cache after this check
            cache_old = dir_gb(P_.d)
        else:
            credit += dir_gb(P_.d)
            cache_new = (len(store_cols) + len(extra)) * npf * 4 * (2 if need_r2 else 1) * 1.05 / GBy
        credit += dir_gb(other) if os.path.isdir(other) else 0.0
        prog_key = ((st0.get("store_progress") or {}).get("key")) if st0 is not None and not a.redo else None
        if os.path.isdir(sdir) and prog_key != kstore:
            credit += dir_gb(sdir)
            n_done = 0
        else:
            n_done = store_genes_done(st0.d, sdir, kstore, len(store_cols), a.chunk) if st0 is not None else 0
        store_rem = (len(store_cols) - n_done + len(extra)) * per_gene / GBy
    else:
        credit += dir_gb(P_.d) if os.path.isdir(P_.d) else 0.0          # a pass cache left by a killed run
    n_set = len(up) + len(down)
    xfold = [d for d in (sorted(os.listdir(out)) if os.path.isdir(out) else [])
             if os.path.isfile(os.path.join(out, d, f"{d}_per_profile.csv"))]
    genes_todo = not done0("genes", kgenes, need_genes)
    set_gene = npf * SET_BYTES_PROFILE + ctx.B.shape[0] * ctx.L * SET_BYTES_DDLINE + ctx.B.shape[0] * SET_BYTES_DD
    sets_new = n_set * set_gene / GBy if genes_todo else 0.0
    sets_old = sum(dir_gb(os.path.join(out, d)) for d in xfold + ["upstream", "downstream"]
                   if os.path.isdir(os.path.join(out, d))) if genes_todo else 0.0
    des_todo = not done0("deseq2", kdes, need_des)
    des_new = len(dgenes) * int(ctx.drug_w.sum()) * ctx.L * DESEQ_BYTES_ROW / GBy if (dfiles and des_todo) else 0.0
    des_old = dir_gb(ddir) if (des_todo and os.path.isdir(ddir)) else 0.0
    phase1 = cache_new + store_rem
    phase2 = store_rem - cache_old + sets_new - sets_old + max(0.0, des_new - des_old)
    gb = 0.3 + max(phase1, phase2, 0.0)
    need_disk(out, gb, f"the export ({'all genes' if all_genes else 'selected genes'}; {len(store_cols)} atlas genes in "
                       f"the store, {'done' if store_done else f'{store_rem:.1f} GB of it still to write'}; "
                       f"{n_set} selected-gene entries)", credit)
    # ---------------------------------------------------------------- state
    os.makedirs(out, exist_ok=True)
    st = State(out)
    if a.redo:
        for part in ("metadata", "store", "genes", "deseq2"):
            st.clear(part)
        st.clear("chunks")
        shutil.rmtree(os.path.join(st.d, "chunks"), ignore_errors=True)
        P_.clear()
    info = {"export_version": EXPORT_VERSION, "exposure": gene, "exposure_label": xlabel, "all_genes": all_genes,
            "data": os.path.realpath(data), "min_cells": A.MIN_CELLS, "min_lines": A.MIN_LINES,
            "genome_wide_finished": gw_state != "not finished", "genome_wide_used": gw_ok,
            "genome_wide_state": gw_state, "genome_wide_reason": gw_reason,
            "upstream_coregulation_tables": sorted(co), "locus_genes": locus_syms, "extra_genes": extra,
            "n_upstream_genes": len(up), "n_downstream_genes": len(down), "store": os.path.relpath(sdir, out),
            "store_atlas_genes": len(store_cols), "deseq2_files": len(dfiles), "parts": {}}
    run = {"stage_seconds": {}, "disk_check_gb": round(gb, 3), "disk_credit_gb": round(credit, 3)}

    # ---------------------------------------------------------------- the pass and the gene store
    t0 = time.time()
    if store_done:
        log(f"gene store: done earlier ({sdir})")
        side = None
        for r in (st.get("store") or {}).get("info", {}).get("checks", []):   # the checks of the run that built it
            ck.add(r["check"], r["value"], r["n"], r["note"])
    else:
        if os.path.isdir(other):                              # the other store kind is stale for this run
            shutil.rmtree(other, ignore_errors=True)
        if os.path.isdir(sdir) and (st.get("store_progress") or {}).get("key") != kstore:
            shutil.rmtree(sdir, ignore_errors=True)
            shutil.rmtree(os.path.join(st.d, "chunks"), ignore_errors=True)
        st.clear("store")
        st.mark("store_progress", kstore)
        n_ck0 = len(ck.rows)
        ck.add("genome_wide tensor reused for r2", int(tensor is not None), note=tnote)
        side = run_pass(ctx, store_cols, extra, P_, kpass, need_r2, ck)
        pass_checks(side, ck)
        ext = extra_effects(ctx, side, extra)
        write_store(ctx, side, P_, sdir, store_cols, ext, a.chunk, tensor, need_r2, kstore, st, ck)
        st.mark("store", kstore, {"checks": ck.rows[n_ck0:], "r2_source": "tensor" if tensor is not None else
                                  "plate_r2"})
    P_.clear()                                                # also a cache left by a run killed after the store
    if all_genes and os.path.isdir(os.path.join(out, ".cache")) and not os.listdir(os.path.join(out, ".cache")):
        os.rmdir(os.path.join(out, ".cache"))
    r2src = (st.get("store") or {}).get("info", {}).get("r2_source", "tensor" if tensor is not None else "plate_r2")
    info["r2_source"] = r2src
    info["genome_wide_tensor_reused"] = r2src == "tensor"
    run["stage_seconds"]["pass and gene store"] = round(time.time() - t0, 1)
    store = Store(sdir)
    info["profiles_per_gene"] = int(len(store.prof))

    # ---------------------------------------------------------------- metadata
    t0 = time.time()

    def meta_part():
        sd, xp = (store_side(ctx, store, xlabel), 0) if side is None else (side, store_cols.index(xi))
        meta_tables(ctx, sd, xp, xlabel, int(ctx.gi[xi]), mdir)       # side None: the DMSO sums from the store
        return {}
    st.run("metadata", kmeta, ck, meta_part, need_meta)
    run["stage_seconds"]["metadata"] = round(time.time() - t0, 1)

    # ---------------------------------------------------------------- exposure, upstream, downstream
    t0 = time.time()

    def g_part():
        for d in xfold + [xlabel, "upstream", "downstream"]:    # also an earlier exposure's folder
            shutil.rmtree(os.path.join(out, d), ignore_errors=True)
        return genes_part(ctx, store, out, xlabel, up, down, screen, prog, co, overlays, gw_ok, locus, ck,
                          gw_reason=gw_reason, gw_ri=gw_ri if gw_ok else None)
    info["parts"]["genes"] = st.run("genes", kgenes, ck, g_part, need_genes)
    run["stage_seconds"]["exposure, upstream, downstream"] = round(time.time() - t0, 1)

    # ---------------------------------------------------------------- Tahoe's DESeq2 table
    t0 = time.time()

    def d_part():
        shutil.rmtree(ddir, ignore_errors=True)
        return deseq2_part(ctx, data, ddir, dfiles, dgenes, xlabel, ck)
    info["parts"]["deseq2"] = st.run("deseq2", kdes, ck, d_part, need_des)
    run["stage_seconds"]["tahoe_deseq2"] = round(time.time() - t0, 1)

    # ---------------------------------------------------------------- README, checks, info
    ckf = ck.frame()
    write_csv(ckf, os.path.join(out, "checks.csv"))
    info["sizes_bytes"] = folder_sizes(out)
    status = DOC.status_lines(info, gw_ok, co, dfiles, all_genes)
    write_text(os.path.join(out, "README.md"), DOC.readme(out, info, status, xlabel))
    undoc = DOC.undocumented(out, xlabel)
    if undoc:
        log("WARNING: columns without a README entry: " + "; ".join(undoc[:20]))
    info["undocumented_columns"] = undoc
    write_json(os.path.join(out, "export_info.json"), info)
    run.update(wall_seconds=round(time.time() - t_all, 1), peak_rss_gb=round(UT.peak_gb(), 3),
               peak_rss_how=UT._MEM_PEAK["how"], versions={"python": sys.version.split()[0], "numpy": np.__version__,
                                                           "pandas": pd.__version__, "pyarrow": pa.__version__})
    write_json(os.path.join(out, "run_info.json"), run)
    for s in status:
        log(s)
    log(f"export done ({time.time() - t_all:.0f} s; peak RSS {UT.peak_gb():.2f} GB): {os.path.join(out, 'README.md')}")


def store_side(ctx, store, xlabel):
    """The DMSO sums of the exposure, read back from the store (for metadata when the store was built earlier)."""
    b = store.baselines(xlabel).to_pandas()
    pl = pq.read_table(os.path.join(store.d, "plate_line.parquet")).to_pandas()
    nP, L = len(ctx.plates), ctx.L
    dmc = b["dmso_umi"].to_numpy(np.float64).reshape(nP, L)[:, :, None]
    p = well_index(ctx, store)
    tot, nc = np.zeros((ctx.NW, ctx.L)), np.zeros((ctx.NW, ctx.L))
    tot[p["_w"], p["_l"]] = p["total_umi"].to_numpy(float)
    nc[p["_w"], p["_l"]] = p["n_cells"].to_numpy(float)
    return {"dmc": dmc, "dmt": pl["dmso_total_umi"].to_numpy(float).reshape(nP, L),
            "dmn": pl["dmso_cells"].to_numpy(float).reshape(nP, L),
            "dmk": pl["n_dmso_wells_with_line"].to_numpy(int).reshape(nP, L), "tot": tot, "nc": nc}


def why_frame(ctx, sel, kind):
    rows = []
    for k, r in sel.items():
        if isinstance(k, tuple):
            g, sym, atlas = k[1], k[1], False
        else:
            g, sym, atlas = ctx.glabel[k], ctx.gsym[k], True
        rows.append({"gene": g, "symbol": sym, "kind": "atlas" if atlas else "extra (not an atlas gene)",
                     "reasons": "; ".join(r["reasons"]), "n_reasons": len(r["reasons"]),
                     "median_line_cpm": ctx.gmed[k] if atlas else np.nan,
                     "n_lines_expressing": int(ctx.gnexp[k]) if atlas else ctx.L, "_idx": k if atlas else -1})
    df = pd.DataFrame(rows, columns=["gene", "symbol", "kind", "reasons", "n_reasons", "median_line_cpm",
                                     "n_lines_expressing", "_idx"])
    return df.sort_values(["kind", "gene"], kind="stable").reset_index(drop=True)


def exposure_reading(ctx, xprof):
    """Numbers behind README.md's reading caveats, from the exposure's per-profile rows: how many UMIs a usable profile
    has (low counts: a zero count still gets a log2cpm set by the library size alone) and how often lines survive at
    >= MIN_CELLS cells in drug-doses the atlas flags toxic vs the others (24 h: survivors only)."""
    p = xprof
    ue = p[p["usable"].astype(bool) & p["expressed"].astype(bool)]
    u = ue["umi_count"].to_numpy(float)
    tot = ue["total_umi"].to_numpy(float)
    nan = float("nan")
    res = {"profiles_usable_expressed": int(len(ue))}
    if len(ue):
        mt = float(np.median(tot))
        res.update(frac_zero_umi=round(float((u == 0).mean()), 4), umi_median=float(np.median(u)),
                   umi_p90=float(np.quantile(u, 0.9)), total_umi_median=mt,
                   cpm_pooled=round(float(u.sum() / tot.sum() * 1e6), 3),
                   log2cpm_of_zero_at_median_total=round(float(np.log2(0.5 / (mt + 1.0) * 1e6)), 3),
                   log2cpm_of_zero_range=[round(float(np.log2(0.5 / (tot.max() + 1.0) * 1e6)), 3),
                                          round(float(np.log2(0.5 / (tot.min() + 1.0) * 1e6)), 3)])
    dd = ctx.fx.dd
    flags = dd["flags"].fillna("").astype(str) if "flags" in dd else pd.Series([""] * len(dd))
    tox = set(np.flatnonzero(flags.str.contains(r"\btoxic\b", regex=True).to_numpy()).tolist())
    d = p[p["well_used"].astype(bool) & (p["drug_dose_row"] >= 0)]
    it = d["drug_dose_row"].isin(tox)
    res.update(n_drugdoses_toxic=len(tox),
               usable_share_toxic=round(float(d.loc[it, "usable"].mean()), 3) if it.any() else nan,
               usable_share_other=round(float(d.loc[~it, "usable"].mean()), 3) if (~it).any() else nan)
    return res


def gm_entry_symbol(s, sym2idx):
    """gene_modules.csv 'gene/assay' -> the gene symbol it names: genome_wide.gm_symbol when that is an atlas gene,
    else the first word without its assay suffix ('TRIM72_total (exon2-exon3 junction)' -> TRIM72)."""
    g = GW.gm_symbol(s, sym2idx)
    if isinstance(g, str) and g:
        return g
    return str(s).split(" ")[0].split("(")[0].strip().split("_")[0]


def curated_rows(ctx, overlays, ck):
    """downstream/overlay/curated_sets.csv: every entry of each curated list as the list writes it, the gene it names
    and whether that is an expressed atlas gene (genome_wide.overlay_sets keeps only the atlas genes' symbols, so the
    other gene_modules.csv entries are read back from the file here)."""
    gm = None
    p = os.path.join(MGDIR, "gene_modules.csv")
    if os.path.exists(p):
        gm = pd.read_csv(p)
        gm["_sym"] = [gm_entry_symbol(s, ctx.sym2idx) for s in gm["gene/assay"]]
    rows = []
    for nm, (syms, src) in sorted(overlays.items()):
        ent = None
        if nm.startswith("OVERLAY_GM_") and gm is not None:
            mod = nm[len("OVERLAY_GM_"):]
            m = gm["module"].astype(str)
            sel = (m.isin(["p53_primary", "p53_secondary"]) if mod == "p53_all" else
                   (m.str.startswith("screen_") | m.eq("stress_markers")) if mod == "MG53_pathways" else m.eq(mod))
            ent = [(str(r), str(s)) for r, s in zip(gm.loc[sel, "gene/assay"], gm.loc[sel, "_sym"])]
            mine = sorted(s for _r, s in ent if s in ctx.sym2idx)
            theirs = sorted(s for s in syms if isinstance(s, str) and s in ctx.sym2idx)
            if mine != theirs:
                ck.add(f"overlay {nm}: members read back from gene_modules.csv differ from genome_wide's", 0,
                       note=f"{len(mine)} vs {len(theirs)}")
        if ent is None:
            ent = [(str(s), str(s)) for s in syms if isinstance(s, str) and s]
        for raw, s in ent:
            rows.append({"label": "overlay", "set": nm, "gene": s, "curated_entry": raw, "source": src,
                         "gene_in_atlas": s in ctx.sym2idx})
    return pd.DataFrame(rows, columns=["label", "set", "gene", "curated_entry", "source", "gene_in_atlas"])


def program_flags(gw_ri, prog):
    """genome_wide's run-level flags of its Tahoe p53 program (run_info.json 'B'; the same lines as GENOME_WIDE.md's
    'Flags'), as rows (item, value)."""
    B = (gw_ri or {}).get("B") or {}
    rows = []
    for item, k in (("P_is_fallback", "P_fallback"), ("P_down_is_fallback", "P_down_fallback"), ("S1_drug_doses", "S1"),
                    ("S2_drug_doses", "S2"), ("P_genes", "P"), ("P_down_genes", "P_down")):
        if k in B:
            rows.append((item, B[k]))
    if prog is not None and not any(r[0] == "P_is_fallback" for r in rows):
        for nm, lab in (("P", "P ("), ("P_down", "P-down")):
            m = prog[prog["program"].astype(str).str.startswith(lab)]
            rows.append((f"{nm}_is_fallback", bool(m["program_is_fallback"].astype(str).str.lower().eq("true").any())))
    for i, s in enumerate(B.get("fold_status", []) or []):
        rows.append((f"fold_{i}_status", s))
    for f in B.get("flags", []) or []:
        rows.append(("flag", f))
    return pd.DataFrame(rows, columns=["item", "value"])


def genes_part(ctx, store, out, xlabel, up, down, screen, prog, co, overlays, gw_ok, locus, ck, gw_reason="",
               gw_ri=None):
    """<GENE>/, upstream/ and downstream/ from the gene store."""
    info = {}
    xdir = os.path.join(out, xlabel)
    files, xprof, xwell, xdl, xdd = exposure_tables(ctx, store, xlabel, xdir)
    info["exposure_files"] = sorted(os.path.relpath(f, out) for f in files.values())
    info["exposure_reading"] = exposure_reading(ctx, xprof)
    # ------------------------------------------------ upstream
    udir = os.path.join(out, "upstream")
    U = xdd.copy()
    if "dog_index" in co:
        d = co["dog_index"].copy()
        d["_k"] = d["drug"].astype(str) + "|" + d["conc"].astype(float).round(6).astype(str)
        U["_k"] = U["drug"].astype(str) + "|" + U["concentration_uM"].astype(float).round(6).astype(str)
        keep = [c for c in ("DoG_sense_index_z", "DoG_antisense_index_z", "DoG_sense_index_log2",
                            "DoG_antisense_index_log2", "DoG_sense_index_robust_z", "rank_sense_index") if c in d]
        U = U.merge(d.drop_duplicates("_k").set_index("_k")[keep], left_on="_k", right_index=True, how="left") \
            .drop(columns="_k")
    hd = pd.read_parquet(os.path.join(ctx.data, "metadata", "drug_metadata.parquet"))
    hd["_key"] = hd["drug"].astype(str).str.strip()
    hd = hd.drop_duplicates("_key").set_index("_key")
    U["human_approved"] = U["drug"].astype(str).str.strip().map(hd["human-approved"]) if "human-approved" in hd else ""
    write_csv(U, os.path.join(udir, f"{xlabel}_per_drugdose.csv"))
    write_csv(xdl, os.path.join(udir, f"{xlabel}_per_drugdose_line.csv"))
    cl = pd.read_csv(os.path.join(out, "metadata", "cell_lines.csv"), dtype={"cell_line_id": str})
    lt = cl[["cell_line_id", "cell_name", "organ", "tp53_group", "tp53_status", "tp53_changes", "genotype_features"]
            + [c for c in cl.columns if c.startswith(xlabel + "_")]].copy()
    if "baseline" in co:
        b = co["baseline"].drop_duplicates("cell_line_id").set_index("cell_line_id")
        for c in ("TRIM72_log2cpm_vs_plate_mean", "TRIM72_mean_rank_within_plate", "FUS_log2cpm_vs_plate_mean"):
            if c in b:
                lt[f"coreg_{c}"] = lt["cell_line_id"].map(b[c])
    write_csv(lt, os.path.join(udir, "line_traits.csv"))
    feats, _per = genotype_map(ctx)
    fl = pd.DataFrame([(k, ctx.lines[i], ctx.line_name[i]) for k in sorted(feats) for i in sorted(feats[k])],
                      columns=["feature", "cell_line_id", "cell_name"])
    write_csv(fl, os.path.join(udir, "line_features.csv"))
    uw = why_frame(ctx, up, "upstream")
    uw = annotate_up(ctx, uw, screen, co)
    write_csv(uw.drop(columns="_idx"), os.path.join(udir, "genes.csv"))
    ug = [g for g in uw["gene"] if store.has(g)]
    set_tables(ctx, store, ug, udir, uw)
    info["n_upstream_genes"] = len(ug)
    lack, cav = [], []
    if screen is None:
        lack.append(f"- {gw_reason or 'genome_wide has not finished'}: the genes of its common-slope screen (q < 0.1, "
                    "top 200 by |t|) are missing from genes.csv and the gene tables.")
    if not co:
        lack.append("- upstream_coregulation's tables are not present (or describe another exposure): no "
                    "co-regulation partners, no readthrough (DoG) index per drug-dose, no DoG classes.")
    if screen is not None and "screen_q_common" in uw:
        top = uw["reasons"].astype(str).str.contains(f"top {TOP_T} by")
        nsig = int((uw["screen_q_common"] < Q_SCREEN).sum())
        nns = int((top & ~(uw["screen_q_common"] < Q_SCREEN)).sum())
        info["upstream_screen_significant"], info["upstream_top_t_not_significant"] = nsig, nns
        if nns:
            cav.append(f"- {nns} of the {int(top.sum())} genes listed as the top {TOP_T} by |t_common| have q_common >= "
                       f"{Q_SCREEN:g} ({nsig} genes pass q < {Q_SCREEN:g} in this run): they are the screen's strongest "
                       "co-varying genes, not significant ones (their reasons say so).")
    cav.append("- A gene whose response tracks the exposure's (common slope q < 0.1) is listed in both upstream/ and "
               "downstream/ with the same reason: co-variation within drug-doses has no direction, so putting it above "
               "or below the exposure is a reading, not a result of the data.")
    write_text(os.path.join(udir, "NOTE.md"), DOC.UPSTREAM_NOTE.format(
        lack="\n".join(lack) if lack else "- nothing: every input of upstream/ was present.", caveats="\n".join(cav)))
    # ------------------------------------------------ downstream
    ddir = os.path.join(out, "downstream")
    os.makedirs(ddir, exist_ok=True)
    if not gw_ok:
        write_text(os.path.join(ddir, "NOTE.md"), DOC.DOWNSTREAM_MISSING.format(
            reason=gw_reason or "genome_wide has not finished"))
        info["n_downstream_genes"] = 0
        info["downstream"] = f"missing: {gw_reason or 'genome_wide has not finished'}"
        return info
    dw = why_frame(ctx, down, "downstream")
    dw = annotate_down(ctx, dw, screen, prog)
    write_csv(dw.drop(columns="_idx"), os.path.join(ddir, "genes.csv"))
    pm = prog.copy()
    pm.insert(0, "gene", [ctx.glabel[int(i)] for i in pm["idx"]])
    pm = pm.drop(columns=[c for c in pm.columns if c.startswith("overlay_")] + ["idx"])
    write_csv(pm, os.path.join(ddir, "program_members.csv"))
    pf = program_flags(gw_ri, prog)
    write_csv(pf, os.path.join(ddir, "program_flags.csv"))
    info["program_flags"] = [f"{r.item}: {r.value}" for r in pf.itertuples()]
    dg = [g for g in dw["gene"] if store.has(g)]
    set_tables(ctx, store, dg, ddir, dw)
    info["n_downstream_genes"] = len(dg)
    # program scores per profile and per (drug-dose, line)
    p = well_index(ctx, store)
    pw_, pl_ = p["_w"].to_numpy(), p["_l"].to_numpy()
    sc = pd.DataFrame({"plate": p["plate"].astype(str), "well": p["well"].astype(str),
                       "sample": p["sample"].astype(str), "drug": p["drug"].astype(str),
                       "concentration_uM": p["concentration_uM"], "is_dmso": p["is_dmso"],
                       "well_used": p["well_used"], "drug_dose_row": p["drug_dose_row"],
                       "cell_line_id": p["cell_line_id"].astype(str), "cell_name": p["cell_name"].astype(str),
                       "tp53_group": p["tp53_group"].astype(str)})
    sdl = None
    progs = {}
    for nm, lab in (("P", "P ("), ("P_down", "P-down")):
        m = prog[prog["program"].astype(str).str.startswith(lab)]
        progs[nm] = ([ctx.glabel[int(i)] for i in m["idx"] if int(i) != ctx.sym2idx.get(xlabel, -1)],
                     bool(m["program_is_fallback"].astype(str).str.lower().eq("true").any()) if len(m) else False)
    for nm, (mem, fb) in progs.items():
        mem = [g for g in mem if store.has(g)]
        S, N = set_scores(ctx, store, mem, p)
        for c in ("r2", "u_drugmedian", "u_dmso"):
            sc[f"{nm}_{c}"] = S[c][pw_, pl_]
        sc[f"{nm}_n_genes_r2"] = N[pw_, pl_].astype(int)
        sc[f"{nm}_is_fallback"] = fb
        part = pd.DataFrame({f"{nm}_{c}_mean": TW.Grid.dd_mean(ctx.B, S[c]).ravel() for c in ("r2", "u_drugmedian",
                                                                                               "u_dmso")})
        part[f"{nm}_n_wells_r2"] = np.asarray(ctx.B @ np.isfinite(S["r2"]).astype(float)).ravel().astype(int)
        part[f"{nm}_is_fallback"] = fb
        sdl = part if sdl is None else pd.concat([sdl, part], axis=1)
    write_csv(sc, os.path.join(ddir, "program_scores_per_profile.csv"))
    nd = ctx.B.shape[0]
    di, li = np.repeat(np.arange(nd), ctx.L), np.tile(np.arange(ctx.L), nd)
    head = pd.DataFrame({"drug_dose_row": di, "drug": ctx.fx.dd["drug"].astype(str).to_numpy()[di],
                         "concentration_uM": ctx.fx.dd["conc"].to_numpy(float)[di],
                         "cell_line_id": np.array(ctx.lines)[li], "cell_name": ctx.line_name[li],
                         "tp53_group": ctx.tp53["tp53_group"].to_numpy()[li]})
    write_csv(pd.concat([head, sdl], axis=1), os.path.join(ddir, "program_scores_per_drugdose_line.csv"))
    # overlays (labelled): membership and scores
    odir = os.path.join(ddir, "overlay")
    ocols = {}
    for nm, (syms, src) in sorted(overlays.items()):
        mem = [ctx.glabel[ctx.sym2idx[s]] for s in syms
               if isinstance(s, str) and s in ctx.sym2idx and ctx.sym2idx[s] != ctx.sym2idx.get(xlabel)]
        mem = [g for g in mem if store.has(g)]
        S, _N = set_scores(ctx, store, mem, p)
        ocols[f"{nm}_r2_mean"] = TW.Grid.dd_mean(ctx.B, S["r2"]).ravel()
        ocols[f"{nm}_u_drugmedian_mean"] = TW.Grid.dd_mean(ctx.B, S["u_drugmedian"]).ravel()
    write_csv(curated_rows(ctx, overlays, ck), os.path.join(odir, "curated_sets.csv"))
    write_csv(pd.concat([head, pd.DataFrame(ocols)], axis=1), os.path.join(odir, "scores_per_drugdose_line.csv"))
    write_text(os.path.join(odir, "NOTE.md"), DOC.OVERLAY_NOTE)
    return info


def annotate_up(ctx, uw, screen, co):
    if screen is not None:
        s = screen.set_index("idx")
        s = s[s["tested"].astype(str).str.lower().eq("true")]
        rk = s["t_common"].abs().rank(ascending=False, method="first")
        for c in ("b_common", "se_common", "t_common", "p_common", "q_common", "diff", "q_diff"):
            uw[f"screen_{c}"] = uw["_idx"].map(s[c]) if c in s else np.nan
        uw["screen_rank_abs_t_common"] = uw["_idx"].map(rk)
    if "coreg" in co:
        c = co["coreg"].drop_duplicates("gene").set_index("gene")
        for k in ("r_z_raw", "q_raw", "r_z_minus_3pc", "q_minus_3pc", "DoG_class", "up_same_strand_expressed_gene"):
            if k in c:
                uw[f"coreg_{k}"] = uw["gene"].map(c[k])
    if "dog_class" in co:
        d = co["dog_class"].drop_duplicates("symbol").set_index("symbol")
        uw["dog_class"] = uw["symbol"].map(d["class"]) if "class" in d else ""
    if "locus" in co:
        lc = co["locus"].drop_duplicates("label").set_index("label")
        for k in ("rel_to_TRIM72", "same_strand_as_TRIM72", "distance_bp", "biotype"):
            if k in lc:
                uw[f"locus_{k}"] = uw["symbol"].map(lc[k])
    return uw


def annotate_down(ctx, dw, screen, prog):
    if prog is not None:
        pr = prog.set_index("idx")
        dw["program"] = dw["_idx"].map(pr["program"])
        dw["program_is_fallback"] = dw["_idx"].map(pr["program_is_fallback"])
        for c in ("z_program", "q_up", "q_down", "wt_minus_alt_log2", "wt_mean_log2", "rank_in_P", "loco_frequency"):
            if c in pr:
                dw[f"program_{c}"] = dw["_idx"].map(pr[c])
    if screen is not None:
        s = screen.set_index("idx")
        for c in ("b_common", "t_common", "q_common", "b_WT", "b_alt", "diff", "t_diff", "q_diff", "q_label_diff"):
            if c in s:
                dw[f"screen_{c}"] = dw["_idx"].map(s[c])
    return dw


def deseq2_gene_list(ctx, store, xlabel, up, down, locus):
    g = {ctx.gsym[ctx.label2idx[xlabel]]} if xlabel in ctx.label2idx else {xlabel}
    for sel in (up, down):
        for k in sel:
            g.add(k[1] if isinstance(k, tuple) else ctx.gsym[k])
    return sorted(g)


def deseq2_part(ctx, data, ddir, files, genes, xlabel, ck):
    os.makedirs(ddir, exist_ok=True)
    if not files:
        write_text(os.path.join(ddir, "NOTE.md"), DOC.DESEQ2_ABSENT)
        ck.add("Tahoe DESeq2 rows extracted", 0, note="metadata/pseudobulk_differential_expression not present "
               "(setup --mode needed / stream does not download it)")
        return {"status": "absent"}
    xs = ctx.gsym[ctx.label2idx[xlabel]] if xlabel in ctx.label2idx else xlabel
    counts, stats = deseq2_extract(files, genes, ddir, xs, deseq2_keys(ctx))
    gl = pd.DataFrame({"gene": genes, "rows": [counts.get(g, 0) for g in genes],
                       "is_exposure": [g == xs for g in genes]})
    write_csv(gl, os.path.join(ddir, "genes.csv"))
    warn = ""
    if stats["rows_kept"] == 0:                # a table is there but none of ~1,000 wanted symbols matched: loud
        warn = (f"WARNING: none of the {len(genes)} wanted genes has a row in Tahoe's DESeq2 table "
                f"({stats['files']} files, {stats['row_groups']} row groups). Its gene_name column may not hold gene "
                "symbols in this download; check one file (e.g. pyarrow.parquet.read_table(f, columns=['gene_name'])).")
        log(warn)
    note = DOC.DESEQ2_NOTE.format(
        n=stats["rows_kept"], nodd=stats["rows_without_drug_dose_row"], nocl=stats["rows_without_cell_line_id"],
        warn=("\n**" + warn + "**\n") if warn else "")
    write_text(os.path.join(ddir, "NOTE.md"), note)
    ck.add("Tahoe DESeq2 rows extracted", stats["rows_kept"], len(genes),
           f"{stats['files']} files, {stats['row_groups']} row groups ({stats['row_groups_skipped_by_statistics']} "
           f"skipped by their gene_name statistics); genes with no row: {int((gl['rows'] == 0).sum())}"
           + (f"; {warn}" if warn else ""))
    ck.add("Tahoe DESeq2 rows without an atlas drug_dose_row / cell_line_id", stats["rows_without_drug_dose_row"],
           stats["rows_kept"], f"rows without cell_line_id: {stats['rows_without_cell_line_id']} (drug-doses or lines "
           "the atlas does not have, or a drug / DepMap id spelled otherwise)")
    return {"status": "extracted" if not warn else "WARNING: no rows", "warning": warn,
            **{k: v for k, v in stats.items() if k != "seconds"}}


def folder_sizes(out):
    res = {}
    for d in sorted(os.listdir(out)):
        p = os.path.join(out, d)
        if d.startswith(".") or not os.path.isdir(p):
            continue
        res[d] = int(sum(os.path.getsize(f) for f in glob.glob(os.path.join(p, "**", "*"), recursive=True)
                         if os.path.isfile(f)))
    return res


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:                                          # noqa: BLE001
        traceback.print_exc()
        sys.exit(1)
