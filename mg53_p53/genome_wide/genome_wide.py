#!/usr/bin/env python3
"""The list-free version of the MG53 (TRIM72) analysis, Tahoe-100M only (no new data), method-v3 effects: every atlas
gene's per (well x line) effects kept as a cache, a p53 program found from the data, TRIM72 against every expressed
gene with the TP53 genotype as the control, and data-driven gene programs. Curated lists (the panel's 21-gene
P53_ACTIVITY, gene_modules.csv, CollecTRI, the S / G2M modules) appear only as labelled overlays or as one labelled
covariate set with a list-free twin; they never define the search space, the outcome, the exposure or a selection.

Tahoe has no MG53 perturbation and measures mRNA, so every estimate is an ASSOCIATION between TRIM72 mRNA and other
mRNA across cell lines inside the same drug-doses (24 h). p53 activity is read from the mRNA of a p53 program that this
step derives from the data.

(A) Tensor. One streamed pass over <data>/atlas/pseudobulk (upstream_tf.stream_plates and plate_r2: plate drug-well
    baseline per line, composition shift, the atlas's own position correction W1 - W2; wells whose W1 has < MIN_LINES
    lines left out) keeps the corrected log2 effect r2 of every atlas gene per (well, line) as a float32 cache, gene-
    major (16,643 genes x 1,329 wells x 50 lines = 4.4 GB on the real data), read later gene chunk by gene chunk.
    Checked against atlas W1 (per plate), W2 (median over lines), DD_lfc and the gene panel's per-line effects.
(B) Tahoe p53 program. Per drug-dose and gene, the TP53-WT minus TP53-altered contrast z (difference of line means
    over the label-free SD of the drug-dose's line values), for the true labels and --perm permutations of them (one
    set for all genes and drug-doses). Selection 1: drug-doses whose genome-wide WT-vs-altered divergence (log of the
    mean of the top 1% of z^2 over genes) beats the permutations: calibrated z, then a permutation FDR < 0.05 over the
    'keep' drug-doses (BH on the pooled p of the z against the same z of every permuted labelling treated as the
    truth: it keeps the skew of the null and the labelling all drug-doses share; the null S1 sizes are reported): S1.
    Compound folds are dealt after S1 is known (S1 compounds round-robin by divergence, the rest by a seeded
    permutation; F_eff = min(--folds, S1 compounds)). Selection 2, out of fold: every drug-dose is scored with
    the top-N signature (N = max(25, 0.15% of genes)) of the S1 compounds outside its fold; S2 (p53-activating) =
    permutation FDR < 0.05 (the same way, the signatures held fixed) and a positive score; when S1 is a fallback, S2
    and P are flagged exploratory. Program P = genes (the exposure excluded) with drug-equal, permutation-calibrated
    WT-selective induction across S2: BH q < 0.05, WT minus altered > 0 and up in >= half the compounds, and the
    WT arm itself up (drug-weighted WT mean > 0, > 0 in >= half the compounds); P-down is the mirror (fewer than 10
    genes passing: the top 25 by z, flagged as a fallback in checks.csv, key_results.csv and GENOME_WIDE.md).
    Cross-fitted P_-f uses no drug-dose of fold f (its drug-doses are selected with nested signatures from S1 minus
    folds f and their own fold). Stability: leave-one-compound-out, fold Jaccards, P without the exposure-moving
    drug-doses (atlas |DD_z| >= 3), S1 / S2 / program sizes under permuted labels. Specificity: the same divergence
    for every driver / protein-change / organ line grouping of the atlas (tahoe_atlas.genotype_features, 20
    permutations each) on the S1 and S2 drug-doses and for P: is the TP53 status the grouping that explains them best?
(C) Screen. two_way's ddxg model (drug-dose x TP53-group FE + line FE, covariates x group, unweighted OLS) with every
    expressed atlas gene as the outcome and the exposure's per (drug-dose, line) r2 as X. The occupancy of each gene
    (its expressed lines, wells with its W1) is handled exactly: a two-way FE projection per gene, vectorised over
    gene chunks (verified against two_way.Design + many_diffs + fit). b_common, b_WT, b_alt, diff = b_WT - b_alt with
    the conservative two-way (drug, line) cluster SE of two_way; BH over the tested genes. Nulls: the TP53 labels
    relabelled for the whole genome (diff; keeps the gene-gene correlation), the exposure shuffled across lines within
    each drug-dose x group cell (common slope and diff), and two placebo-exposure families chosen without looking at
    any outcome: expression-matched (level, lines expressing, finite cells) and response-matched (share of drug-doses
    with |DD_z| >= 3, residual SD after the FE, lines expressing). The within-cell shuffles break the exposure's
    line-level structure (a line's consistent response across drug-doses), so they are a null only for the per-gene
    studentised t, whose two-way SE carries that structure (the pooled per-gene p and the genome-wide count); an
    unstudentised or set-level statistic calibrated by them is anti-conservative and is not reported as a test. Set
    level: program-level outcomes (mean r2 of a set's members a line expresses) with two_way's D1 machinery
    (two_way.run_models: conservative two-way SE and TP53-label permutations; its within-cell permutation p stays in
    c_program_models.csv as within-cell noise only), and a camera-style test inside the screen (TP53 relabellings
    calibrate its diff; its common slope has the camera p only).
(D) What moves with the exposure: the screen's common-slope ranking; tahoe_atlas.angle_programs (written into this
    step's tables/d_programs; per-line program means from the tensor) and each program's association with the exposure
    across drug-doses (drug-block permutations) and within lines; curated sets as overlays.
(E) Not run here: a TRIM72-detection-stratified single-cell pseudobulk (it needs a pass over the raw cells; GENOME_WIDE.md
    says what it would take).

PRIMARY TEST (declared here before any real-data run; every other row is secondary, sensitivity, screen, overlay or
check): fe ddxg, all drug-doses, covariate set gw (DD_beta, DD_A and resp_bg = the line's mean |r2| over the atlas
genes outside every data-derived program and the exposure; all data-driven), outcome P53PROG_UP_cf (the cross-fitted
Tahoe p53 program), estimand b_WT - b_alt, inference by the conservative two-way SE (TP53-label permutation p next to
it).

    python3 genome_wide.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute]
                           [--exposure GENE (default $MG53_GW_EXPOSURE, else TRIM72)] [--chunk 64] [--workers 2]
                           [--perm 100] [--folds 5] [--label-perm 20] [--x-perm 20] [--placebos 20]
                           [--placebos-set 200] [--set-label-perm 2000] [--set-within-perm 1000] [--d-perm 1000]
                           [--extra-genes PYCARD-AS1] [--rt-covariates FUS,PYCARD-AS1] [--quick]

Outputs ($MG53_OUT/tables; README_tables.txt there explains every column): key_results.csv (the primary test first),
checks.csv, run_info.json; a_tensor_summary.csv, a_panel_check.csv; b_drugdose_p53_activation.csv,
b_p53_program_genes.csv.gz, b_p53_program.csv, b_program_stability.csv, b_feature_specificity.csv, b_overlays.csv;
c_screen_genes.csv.gz, c_screen_top.csv, c_calibration.csv, c_placebos.csv, c_program_models.csv, c_set_tests.csv;
d_programs/ (tahoe_atlas.angle_programs), d_program_vs_exposure.csv; and $MG53_OUT/GENOME_WIDE.md (the findings).

Reads <data>/atlas/effects, <data>/atlas/pseudobulk (one streamed pass of 20 GB, as upstream_tf), <data>/metadata
(gene tokens), <data>/gene_panel/results (TP53 groups; overlays), and for the panel check <data>/gene_panel
(well_line, per-cell files; two_way's panel cache builder). Nothing is downloaded; raw cells are not read; nothing is
written under <data>/atlas or <data>/gene_panel. Tables to $MG53_OUT/tables (default <this folder>/tables), findings to
$MG53_OUT/GENOME_WIDE.md, caches to $MG53_OUT/cache (manifest.json keyed to the data folder; the tensor, (B) pass 1,
the program-scores pass and the finished screen chunks are reused, so an interrupted run resumes; (B) passes 2-5 and
the models are recomputed, ~10-20 min; cache files are written through a temporary file, and an unreadable one is
rebuilt). Memory: the tensor is memory-mapped and read per gene chunk; peak RSS expected ~3-3.5 GB in the parent
during the tensor pass (as upstream_tf's pass plus the per-plate W2 check), ~1 GB later, and ~0.9 GB per worker on the
real data (target < 8 GB). Time on the real data (4 CPUs, defaults), estimated from the kernels timed at the real
dimensions on simulated arrays (not yet run on the real data): 1.5-3 h cold (the screen ~45-130 min with 2 workers, by
how many genes share an occupancy); ~5 GB of cache (the free disk is checked before the tensor is written).
numpy / pandas / scipy (+ pyarrow); psutil only for memory reports.
"""
import argparse
import contextlib
import glob
import hashlib
import json
import multiprocessing as mp
import os
import shutil
import sys
import time
import traceback
import zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures.process import BrokenProcessPool

# BLAS threads: 2 per process (with --workers 2: 4 CPUs), set before numpy loads, overridable from the environment
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

sys.dont_write_bytecode = True        # no __pycache__ written into the sibling step folders imported below
HERE = os.path.dirname(os.path.abspath(__file__))
MGDIR = os.path.dirname(HERE)
REPO = os.path.dirname(MGDIR)
for _p in (REPO, os.path.join(MGDIR, "two_way"), os.path.join(MGDIR, "upstream_tf")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import tahoe_atlas as A     # noqa: E402  (FX, composition_matrix, genotype_features, angle_programs, robust_z)
import two_way as TW        # noqa: E402  (Grid, Design, fit, run_models, covariates, se_conservative, caches, bh)
import upstream_tf as UT    # noqa: E402  (load_profiles, stream_plates, plate_r2, drug_block_perms, peak_gb)

GENE = "TRIM72"             # default exposure (--exposure; $MG53_GW_EXPOSURE)
SEED = 20261030
CACHE_VERSION = 1           # bump when a cache builder changes
# the primary test, declared up front
PRIMARY = {"fe": "ddxg", "dd": "all", "covset": "gw", "outcome": "P53PROG_UP_cf", "estimand": "b_WT - b_alt"}
# covariate sets (per drug-dose x line, each entered x TP53 group); gw_rt is completed at run time (readthrough)
COVSETS = {"gw": ["beta", "A", "resp_bg"],                                 # primary, list-free
           "gw_all": ["beta", "A", "resp_all"],                            # mean |r2| over ALL genes (sensitivity)
           "gw_pc": ["beta", "A", "resp_bg", "pc1", "pc2", "pc3"],         # + genome-wide components (sensitivity)
           "curated_cycle": ["beta", "A", "S", "G2M", "resp_bg"],          # LABELLED curated (Tirosh S / G2M)
           "none": []}
RT_DEFAULTS = {"TRIM72": (["PYCARD-AS1"], ["FUS", "PYCARD-AS1"])}   # exposure: (extra genes, readthrough covariates)
Q_SEL = 0.05                # FDR of the (B) selections
Q_REP = 0.10                # reporting threshold of the screen (two_way's convention)
TOPK_FRAC = 0.01            # divergence: mean of the top 1% of z^2 over genes (at least 10 genes)
TOPN_FRAC = 0.0015          # out-of-fold signatures: top max(25, 0.15% of genes) by program z
PROG_MIN, PROG_FALLBACK, CORE_N = 10, 25, 100
N_FEAT_PERM = 20            # permutations of each line grouping in the specificity check
FEAT_DD_MAX = 40            # drug-doses per selection that get the specificity check (the strongest)
N_NULL_PROG = 20            # permuted labellings treated as the truth (null program sizes)
MIN_ROWS, MIN_LINES_GROUP, MIN_DRUGS = 50, 3, 10    # a screen gene is 'tested' with at least these
XPERM_BATCH = 5             # exposure shuffles fitted together (one FE solve)
LAMBDA_NULL = stats.chi2.ppf(0.5, 1)                # 0.4549: median of t^2 under the null (genomic inflation)
GZ = {"method": "gzip", "mtime": 0}                 # byte-identical .csv.gz across runs

log, quiet, bh, holm = TW.log, TW.quiet, TW.bh, TW.holm


class Checks:
    """checks.csv rows: check, value, n, note."""

    def __init__(self):
        self.rows = []

    def add(self, check, value, n=np.nan, note=""):
        self.rows.append({"check": check, "value": value, "n": n, "note": note})

    def frame(self):
        return pd.DataFrame(self.rows, columns=["check", "value", "n", "note"])


@contextlib.contextmanager
def stage(name, info):
    t0 = time.time()
    log(f"{name} ...")
    yield
    dt = time.time() - t0
    info["stage_seconds"][name] = round(dt, 1)
    log(f"{name} done ({dt:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")


def optional(name, fn, ck, default=None):
    """An optional stage: an error is logged and written to checks.csv, and the step goes on (only (A), (B) and the
    primary (C) fit may fail the step)."""
    try:
        return fn()
    except Exception as err:  # noqa: BLE001
        msg = f"{type(err).__name__}: {err}"[:400]
        log(f"WARNING: optional stage '{name}' skipped ({msg})")
        traceback.print_exc(limit=3)
        ck.add(f"optional stage skipped: {name}", np.nan, note=msg)
        return default


def sha(obj):
    h = hashlib.sha1()
    if isinstance(obj, (list, tuple)):
        for o in obj:
            h.update(sha(o).encode())
    elif isinstance(obj, np.ndarray):
        h.update(str((obj.dtype, obj.shape)).encode())
        h.update(np.ascontiguousarray(obj).tobytes())
    else:
        h.update(json.dumps(obj, sort_keys=True, default=str).encode())
    return h.hexdigest()


def calib(obs, null, axis=-1):
    """Permutation-calibrated z: (observed - mean of the null) / SD of the null (ddof 1), NaN-aware."""
    with quiet():
        return (obs - np.nanmean(null, axis=axis)) / np.nanstd(null, axis=axis, ddof=1)


def save_npz(path, **arrs):
    """np.savez through path.tmp and os.replace: an interrupted write never leaves a truncated cache file."""
    with open(path + ".tmp", "wb") as fh:
        np.savez(fh, **arrs)
    os.replace(path + ".tmp", path)


def load_npz(path):
    """A cache file's arrays, or None when it is missing or unreadable (an unreadable file is deleted and rebuilt)."""
    if not os.path.exists(path):
        return None
    try:
        with np.load(path, allow_pickle=False) as z:
            return {k_: z[k_] for k_ in z.files}
    except (OSError, ValueError, EOFError, KeyError, zipfile.BadZipFile) as err:
        log(f"WARNING: cache {os.path.basename(path)} unreadable ({type(err).__name__}); rebuilding it")
        os.remove(path)
        return None


# ============================================================================= setup: caches, labels, exposure
def gw_manifest(data, extra, panel_min_cells):
    """two_way's cache manifest (data folder, wells.csv, pseudobulk files, gene panel) plus the atlas effects files this
    step reads, the extra (non-atlas) genes collected by the pass and this step's cache version."""
    man = TW.cache_manifest(data)
    fxd = os.path.join(data, "atlas", "effects")
    st = {}
    for f in ("genes.csv", "lines.csv", "drugdose.csv", "plates.csv", "W1.npy", "W2.npy", "expr_mask.npy",
              "composition_shift.parquet", "info.json", "DD_z.npy"):
        try:
            s = os.stat(os.path.join(fxd, f))
            st[f] = [int(s.st_size), int(s.st_mtime_ns)]
        except OSError:
            st[f] = None
    man["genome_wide"] = {"cache_version": CACHE_VERSION, "atlas_effects": st, "extra_genes": list(extra),
                          "panel_min_cells": panel_min_cells}
    return man


def validate_cache(cdir, want, recompute):
    """Delete every cache file when --recompute is given or cache/manifest.json differs from the current inputs (the
    tensor, its index files, side arrays, the pass caches, the panel cache and the screen parts)."""
    mp_ = os.path.join(cdir, "manifest.json")
    have = None
    if os.path.exists(mp_):
        try:
            with open(mp_, encoding="utf-8") as fh:
                have = json.load(fh)
        except (OSError, ValueError):
            have = None
    old = TW.cache_files(cdir) + glob.glob(os.path.join(cdir, "r2_*")) + glob.glob(os.path.join(cdir, "*.tmp")) \
        + ([os.path.join(cdir, "screen")] if os.path.isdir(os.path.join(cdir, "screen")) else [])
    if recompute or have != want:
        if old:
            why = "--recompute" if recompute else ("no cache/manifest.json" if have is None else "inputs changed")
            log(f"rebuilding the caches ({why})")
            for f in old:
                if os.path.isdir(f):
                    shutil.rmtree(f, ignore_errors=True)
                elif os.path.exists(f):
                    os.remove(f)
        if os.path.exists(mp_):
            os.remove(mp_)
        return False
    return True


def tp53_labels(data, lines):
    """TP53 groups as upstream_tf reads them (gene_panel/results/baseline_by_cell_line.csv, column tp53_group):
    wt (L,) bool, labelled (L,) bool (WT or altered; other lines are left out of (B) and (C), where two_way keeps a line
    without a TP53 group as altered)."""
    p = os.path.join(data, "gene_panel", "results", "baseline_by_cell_line.csv")
    if not os.path.exists(p):
        sys.exit(f"{p} not found: the gene panel ('tahoe_gene_panel.py all') gives the TP53 groups")
    bl = pd.read_csv(p, dtype={"cell_line_id": str}).drop_duplicates("cell_line_id").set_index("cell_line_id")
    grp = bl["tp53_group"].reindex(lines).astype(str)
    return (grp == "WT").to_numpy(), grp.isin(["WT", "altered"]).to_numpy()


# ============================================================================= (A) the per (well x line) tensor
class Tensor:
    """Read access to cache/r2_wl.npy (float32, genes x wells x lines, gene-major). Every read maps only the rows it
    needs and drops the map after copying, so the file stays memory-mapped and the logged peak RSS counts only the
    copies (a map kept open over the whole file would count up to 4.4 GB of reclaimable page cache as 'RSS')."""

    def __init__(self, cdir):
        self.path = os.path.join(cdir, "r2_wl.npy")
        self.off, self.shape, _dt = TW.npy_layout(self.path)
        self.G, self.NW, self.L = self.shape
        self.rowb = self.NW * self.L * 4

    def read(self, g0, g1):
        """Genes g0..g1-1: (m, wells, lines) float32."""
        mm = np.memmap(self.path, np.float32, "r", offset=self.off + g0 * self.rowb, shape=(g1 - g0, self.NW, self.L))
        out = np.array(mm)
        del mm
        return out

    def take(self, idx):
        """Any genes (tensor indices, any order): (len(idx), wells, lines) float32, read in runs of consecutive genes."""
        idx = np.asarray(idx, dtype=np.int64)
        out = np.empty((len(idx), self.NW, self.L), np.float32)
        if not len(idx):
            return out
        o = np.argsort(idx, kind="stable")
        s = idx[o]
        brk = np.flatnonzero(np.diff(s) != 1) + 1
        for a, b in zip(np.r_[0, brk], np.r_[brk, len(s)]):
            blk = self.read(int(s[a]), int(s[b - 1]) + 1)
            out[o[a:b]] = blk[s[a:b] - s[a]]
        return out


def dd_level(block, B):
    """(m, wells, lines) per (well, line) r2 -> (m, rows of B, lines) float64: the mean over each drug-dose's used wells
    with a value (two_way's Grid.dd_mean; B = drug-doses x wells, possibly a subset of rows)."""
    m, nw, L = block.shape
    out = TW.Grid.dd_mean(B, block.transpose(1, 0, 2).reshape(nw, m * L))
    return out.reshape(B.shape[0], m, L).transpose(1, 0, 2)


def runs_of(rows):
    """Positions (i0, i1) of the runs of consecutive values in rows (sorted)."""
    brk = np.flatnonzero(np.diff(rows) != 1) + 1
    return list(zip(np.r_[0, brk].tolist(), np.r_[brk, len(rows)].tolist()))


def build_tensor(data, fx, grid, cdir, extra):
    """(A) One streamed pass over atlas/pseudobulk (upstream_tf.stream_plates; each file read once): per plate, as soon
    as its profiles are read, the method-v3 r2 of every atlas gene per (well, line) (upstream_tf.plate_r2, checked
    against the atlas W1), written gene-major into cache/r2_wl.npy (plates are contiguous runs of wells: one write per
    gene and run, so the pass holds only one or two plates in memory). Also per (well, line): mean |r2| over all genes
    (resp_all), total counts, cells and the counts of the extra (non-atlas) genes; per plate the W2 check (median over
    lines of r2 vs atlas W2). Wells of a plate without profiles are written as NaN (a new file reads as zeros)."""
    path = os.path.join(cdir, "r2_wl.npy")
    side_p = os.path.join(cdir, "side_wl.npz")
    need = [path, side_p] + [os.path.join(cdir, f) for f in ("r2_genes.csv", "r2_wells.csv", "r2_lines.csv",
                                                              "r2_expr_mask.npy")]
    if extra:
        need.append(os.path.join(cdir, "pseudobulk_effects.npz"))
    if all(os.path.exists(p) for p in need):
        side = load_npz(side_p)                            # written last: it marks a finished pass
        if side is not None:
            log(f"tensor: cache {path}")
            return side
    t0 = time.time()
    gi = fx.gi
    genes = fx.genes.iloc[gi].reset_index(drop=True)
    toks = genes["token"].astype(int).to_numpy()
    G = len(gi)
    w = fx.wells
    NW = len(w)
    lines = fx.lines["cell_line_id"].astype(str).tolist()
    L = len(lines)
    em = np.asarray(fx.expr_mask)[:, gi].astype(bool)                     # lines x genes
    comp = A.composition_matrix(fx)                                         # wells x lines
    gm = pd.read_parquet(os.path.join(data, "metadata", "gene_metadata.parquet"), columns=["gene_symbol", "token_id"])
    tok_of = dict(zip(gm["gene_symbol"].astype(str), gm["token_id"].astype(int)))   # as upstream_tf / two_way
    miss = [s for s in extra if s not in tok_of]
    if miss:
        sys.exit(f"--extra-genes: {', '.join(miss)} not in metadata/gene_metadata.parquet")
    etoks = np.array([tok_of[s] for s in extra], dtype=int)
    prof = UT.load_profiles(os.path.join(data, "atlas", "pseudobulk"))
    wi = {s: i for i, s in enumerate(w["sample"].astype(str))}
    li = {s: i for i, s in enumerate(lines)}
    prof = prof[prof["sample"].isin(wi) & prof["cell_line_id"].isin(li)].copy()
    prof["wi"] = prof["sample"].map(wi).astype(int)
    prof["li"] = prof["cell_line_id"].map(li).astype(int)
    plate_w = w["plate"].astype(str).to_numpy()
    prof["plate"] = plate_w[prof["wi"].to_numpy()]
    plates = list(fx.plates)
    rows_of = {p: np.flatnonzero(plate_w == p) for p in plates}
    prof = prof[prof["plate"].isin(plates)]
    tot = np.zeros((NW, L))
    nc = np.zeros((NW, L))
    np.add.at(tot, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["total_counts"].to_numpy(float))
    np.add.at(nc, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["n_cells"].to_numpy(float))
    tmp = path + ".tmp"
    for f in (path, tmp, side_p, os.path.join(cdir, "pseudobulk_effects.npz")):   # an earlier or interrupted pass
        if os.path.exists(f):
            os.remove(f)
    need_b = G * NW * L * 4 * 1.15 + 0.5e9                 # the tensor fills a sparse file during the pass
    free_b = shutil.disk_usage(cdir).free
    if free_b < need_b:
        sys.exit(f"genome_wide needs ~{need_b / 1e9:.1f} GB free in {cdir} for its tensor cache; {free_b / 1e9:.1f} GB "
                 "free. Free some disk, then rerun.")
    mm = np.lib.format.open_memmap(tmp, mode="w+", dtype=np.float32, shape=(G, NW, L))   # header + sparse file
    del mm
    off = TW.npy_layout(tmp)[0]
    rowb = NW * L * 4
    resp_all = np.full((NW, L), np.nan, np.float32)
    W2m_all = np.full((NW, G), np.nan, np.float32)
    nfin = np.zeros(G, np.int64)
    exw = np.zeros((NW, L, len(extra)), np.float32)
    written = np.zeros(NW, bool)
    val = []
    log(f"tensor pass: {G} genes x {NW} wells x {L} lines ({G * rowb / 1e9:.2f} GB) from {prof['file'].nunique()} "
        f"pseudobulk files; extra genes: {', '.join(extra) or 'none'}")
    fh = open(tmp, "r+b")

    def write_rows(rows, Yt):
        """Yt: genes x len(rows) x lines, written at the wells rows (one write per gene and run of wells)."""
        for i0, i1 in runs_of(rows):
            r0 = int(rows[i0])
            for g in range(G):
                fh.seek(off + g * rowb + r0 * L * 4)
                fh.write(np.ascontiguousarray(Yt[g, i0:i1]).tobytes())
        written[rows] = True

    def on_plate(p, C, Ex):
        tp = time.time()
        rows = rows_of[p]
        exw[rows] = Ex
        W1a = np.asarray(fx.W1[rows])[:, gi]
        W2a = np.asarray(fx.W2[rows])[:, gi]
        Y, _W1m, v = UT.plate_r2(C, tot[rows], nc[rows], em, fx.drug_w[rows], comp[rows], W1a, W2a)
        fin = np.isfinite(Y)
        with quiet():
            W2m = np.nanmedian(Y, axis=1)                  # the atlas's W2 = median over lines of r2
            resp_all[rows] = np.nanmean(np.abs(Y), axis=2)
        both = np.isfinite(W2m) & np.isfinite(W2a)
        nfin[:] += fin.sum(axis=(0, 1))
        W2m_all[rows] = W2m
        val.append({"plate": p, "wells": len(rows)} | v | {
            "profiles_with_cells": int((nc[rows] >= A.MIN_CELLS).sum()), "finite_cells": int(fin.sum()),
            "W2_cells_both_finite": int(both.sum()),
            "W2_max_abs_diff_vs_atlas": float(np.max(np.abs(W2m[both] - W2a[both]))) if both.any() else np.nan,
            "W2_finite_pattern_mismatch": int((np.isfinite(W2m) != np.isfinite(W2a)).sum())})
        write_rows(rows, Y.transpose(2, 0, 1))
        log(f"  plate {p}: {len(rows)} wells ({time.time() - tp:.0f} s; W1 max |diff| vs atlas "
            f"{val[-1]['W1_max_abs_diff_vs_atlas']:.2g}; peak RSS {UT.peak_gb():.2f} GB)")

    UT.stream_plates(prof, rows_of, plates, NW, L, toks, etoks, on_plate)
    nowrite = np.flatnonzero(~written)
    if len(nowrite):                                       # never leave the zeros of the new file as 'no change'
        log(f"WARNING: {len(nowrite)} wells had no profiles (plates "
            f"{', '.join(sorted(set(plate_w[nowrite])))}): written as NaN")
        write_rows(nowrite, np.broadcast_to(np.full((1, len(nowrite), L), np.nan, np.float32), (G, len(nowrite), L)))
    fh.close()
    os.replace(tmp, path)
    genes_out = pd.DataFrame({"idx": np.arange(G), "col": gi, "token": toks,
                              "symbol": genes["symbol"].astype(str), "label": genes["label"].astype(str),
                              "pooled_cpm": genes["pooled_cpm"], "median_line_cpm": genes["median_line_cpm"],
                              "n_lines_expressing": genes["n_lines_expressing"], "n_finite_well_line": nfin})
    genes_out.to_csv(os.path.join(cdir, "r2_genes.csv"), index=False)
    pd.DataFrame({"idx": np.arange(NW), "sample": w["sample"].astype(str), "plate": plate_w, "drug": w["drug"],
                  "conc": w["conc"], "drugdose_row": grid.ddr, "used_in_drugdose": grid.used,
                  "written_from_profiles": np.isin(np.arange(NW), nowrite, invert=True)}).to_csv(
        os.path.join(cdir, "r2_wells.csv"), index=False)
    pd.DataFrame({"idx": np.arange(L), "cell_line_id": lines,
                  "cell_name": fx.lines["cell_name"].astype(str)}).to_csv(os.path.join(cdir, "r2_lines.csv"),
                                                                         index=False)
    np.save(os.path.join(cdir, "r2_expr_mask.npy"), em)
    # drug-dose level: mean over the used wells of the per-well W2 vs the atlas DD_lfc
    with quiet():
        ddw2 = TW.Grid.dd_mean(grid.B, W2m_all.astype(np.float64))
    ddl = np.asarray(fx.DD_lfc, dtype=np.float64)[:, gi]
    both = np.isfinite(ddw2) & np.isfinite(ddl)
    lfc = {"cells_both_finite": int(both.sum()),
           "max_abs_diff": float(np.max(np.abs(ddw2[both] - ddl[both]))) if both.any() else np.nan,
           "finite_pattern_mismatch": int((np.isfinite(ddw2) != np.isfinite(ddl)).sum())}
    del ddw2, ddl
    side = {"tot": tot, "nc": nc, "resp_all": resp_all, "exw": exw, "extra": np.array(extra, dtype=str),
            "nfin": nfin, "validation": np.array(json.dumps(val)), "ddlfc_check": np.array(json.dumps(lfc)),
            "plates_written": np.array([v["plate"] for v in val], dtype=str),
            "wells_not_written": nowrite, "finite_total": np.int64(sum(v["finite_cells"] for v in val))}
    if extra:
        pbc = {"counts": exw, "tot": tot, "nc": nc, "symbols": np.array(extra), "tokens": etoks}
        TW.pseudobulk_effects(data, cdir, grid, pbc)       # corrected_effects() per extra gene (two_way's file)
    save_npz(side_p, **side)                               # last: a pass interrupted before this point is redone
    log(f"tensor pass done ({time.time() - t0:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")
    return side


def tensor_checks(side, fx, ck):
    """checks.csv rows of (A) and a_tensor_summary.csv (per plate)."""
    val = json.loads(str(side["validation"]))
    V = pd.DataFrame(val)
    for _, r in V.iterrows():
        ck.add(f"tensor W1 (median over lines) vs atlas W1, plate {r['plate']}: max |diff|",
               r["W1_max_abs_diff_vs_atlas"], r["W1_cells_both_finite"],
               f"finite here only {r['W1_finite_here_not_atlas']}, in the atlas only {r['W1_finite_atlas_not_here']}")
    ck.add("tensor median over lines vs atlas W2, all plates: max |diff|", float(V["W2_max_abs_diff_vs_atlas"].max()),
           int(V["W2_cells_both_finite"].sum()), f"finite-pattern mismatches {int(V['W2_finite_pattern_mismatch'].sum())}")
    lfc = json.loads(str(side["ddlfc_check"]))
    ck.add("drug-dose mean of the tensor's per-well W2 vs atlas DD_lfc: max |diff|", lfc["max_abs_diff"],
           lfc["cells_both_finite"], f"finite-pattern mismatches {lfc['finite_pattern_mismatch']}")
    pw = set(str(p) for p in side["plates_written"])
    pl = set(fx.wells["plate"].astype(str))
    ck.add("plates written by the tensor pass = plates in wells.csv", float(pw == pl), len(pl),
           f"written {len(pw)}; in wells.csv {len(pl)}; not written: {', '.join(sorted(pl - pw)) or 'none'}; "
           f"wells written as NaN (no profiles) {len(side['wells_not_written'])}")
    return V


# ============================================================================= the genome-wide ddxg engine
def prune(ok):
    """two_way.Design's singleton rule per gene (ok: genes x drug-doses x lines): drug-doses and lines with < 2 rows
    dropped, repeated to a fixed point (at most 10 rounds, as Design)."""
    ok = ok.copy()
    for _ in range(10):
        bad = (ok.sum(axis=2) < 2)[:, :, None] | (ok.sum(axis=1) < 2)[:, None, :]
        if not (ok & bad).any():
            break
        ok &= ~bad
    return ok


def _solve(Am, Bm):
    """Batched solve; a singular system (a disconnected design) falls back to least squares, gene by gene (any
    solution of the normal equations gives the same residuals)."""
    try:
        return np.linalg.solve(Am, Bm)
    except np.linalg.LinAlgError:
        out = np.empty(Am.shape[:-1] + Bm.shape[-1:])
        for g in range(Am.shape[0]):
            try:
                out[g] = np.linalg.solve(Am[g], Bm[g])
            except np.linalg.LinAlgError:
                out[g] = np.linalg.lstsq(Am[g], Bm[g], rcond=None)[0]
        return out


def group_resid(V, O):
    """Two-way FE residuals (cell = drug-dose within this TP53 group, line) of the columns V (genes x J x drug-doses x
    lines of the group, 0 off the occupancy) on each gene's own occupancy O (genes x drug-doses x lines): the
    concentrated normal equations for the line effects, as two_way.label_perm_ddxg's group(), solved per gene. Lines
    without rows get alpha = 0; the one null direction (all line effects against all cell effects) is fixed by adding
    u u' (u = present lines / sqrt(#present)); the residuals do not depend on that choice."""
    m, J, nd, k = V.shape
    Of = O.astype(np.float64)
    c = Of.sum(axis=2)                                         # genes x drug-doses: lines per cell
    ci = np.where(c > 0, 1.0 / np.where(c > 0, c, 1.0), 0.0)
    nrow = Of.sum(axis=1)                                      # genes x lines
    Am = -np.matmul((Of * ci[:, :, None]).transpose(0, 2, 1), Of)
    di = np.arange(k)
    Am[:, di, di] += nrow
    present = nrow > 0
    Am[:, di, di] += ~present
    u = present / np.sqrt(np.maximum(present.sum(axis=1, keepdims=True), 1))
    Am += u[:, :, None] * u[:, None, :]
    S = V.sum(axis=3)                                          # genes x J x drug-doses: cell sums
    r = V.sum(axis=2) - np.matmul(S * ci[:, None, :], Of)     # genes x J x lines
    al = _solve(Am, r.transpose(0, 2, 1)).transpose(0, 2, 1)
    de = (S - np.matmul(al, Of.transpose(0, 2, 1))) * ci[:, None, :]
    return (V - de[..., None] - al[:, :, None, :]) * Of[:, None]


def _fe_fwl(V, O, P, K):
    """group_resid, then the K covariates (columns P..P+K-1) partialled out of every column (FWL), batched over the
    leading axis: V (b x J x drug-doses x lines), O (b x drug-doses x lines). Returns b x J x cells."""
    b, J, nd, k = V.shape
    np.copyto(V, 0.0, where=~O[:, None])
    Rf = group_resid(V, O).reshape(b, J, nd * k)
    if K:                                                  # FWL: the covariates x group out of x and y
        Gm = np.matmul(Rf, Rf.transpose(0, 2, 1))
        cs = slice(P, P + K)
        coef = _solve(Gm[:, cs, cs], Gm[:, cs, :])
        Rf = Rf - np.matmul(coef.transpose(0, 2, 1), Rf[:, cs])
    return Rf


def group_fit(Y, Xs, C, O, idx):
    """FE and covariate residuals of the exposures (xt: genes x P x drug-doses x lines) and of each outcome (yt) for one
    TP53 group (lines idx), each gene on its own occupancy O. Genes that share an occupancy pattern (most expressed
    genes: same lines, same wells) are fitted together, one FE solve for all of them (the exposure and covariate
    columns are residualised once); genes with a pattern of their own are batched gene by gene. Same numbers either
    way (up to rounding)."""
    m, nd, _L = Y.shape
    P, K = Xs.shape[0], C.shape[0]
    k = len(idx)
    xt, yt = np.empty((m, P, nd, k)), np.empty((m, nd, k))
    _u, inv, cnt = np.unique(np.packbits(O.reshape(m, -1), axis=1), axis=0, return_inverse=True, return_counts=True)
    inv = np.asarray(inv).reshape(-1)
    single = np.flatnonzero(cnt[inv] == 1)
    for u in np.flatnonzero(cnt > 1):
        gi = np.flatnonzero(inv == u)
        V = np.empty((1, P + K + len(gi), nd, k))
        V[0, :P] = Xs[..., idx]
        if K:
            V[0, P:P + K] = C[..., idx]
        V[0, P + K:] = Y[gi][..., idx]
        Rf = _fe_fwl(V, O[gi[:1]], P, K)[0]
        xt[gi] = Rf[:P].reshape(1, P, nd, k)
        yt[gi] = Rf[P + K:].reshape(len(gi), nd, k)
    for c0 in range(0, len(single), 64):
        gi = single[c0:c0 + 64]
        V = np.empty((len(gi), P + K + 1, nd, k))
        V[:, :P] = Xs[None][..., idx]
        if K:
            V[:, P:P + K] = C[None][..., idx]
        V[:, P + K] = Y[gi][..., idx]
        Rf = _fe_fwl(V, O[gi], P, K)
        xt[gi] = Rf[:, :P].reshape(len(gi), P, nd, k)
        yt[gi] = Rf[:, P + K].reshape(len(gi), nd, k)
    return xt, yt


def fit_chunk(Y, Xs, C, ok, wt, use, starts, want_scores=False):
    """two_way's ddxg model for a chunk of outcome genes, each on its own occupancy. Y: genes x drug-doses x lines
    (drug-doses sorted by compound, starts = first row of each compound); Xs: P exposures (P x drug-doses x lines)
    sharing the occupancy ok (genes x drug-doses x lines; they must be finite on it); C: K covariates (each x TP53
    group); wt, use: TP53-WT and analysed lines. With drug-dose x group FE, line FE and every slope by group the model
    splits into a WT regression and an altered regression; each is fitted by group_resid, then the covariates are
    partialled out (FWL). b_WT, b_alt, diff, b_common (one slope, FE and covariates by group) with CR1 cluster SEs by
    compound, line and compound x line and the conservative two-way SE of two_way (the same numbers as two_way.Design
    + many_diffs + fit). Returns per-gene arrays (P x genes); with want_scores, also the cluster score vectors of the
    first exposure's diff and common slope (compound, line, compound x line) for the camera-style set test."""
    m, nd, L = Y.shape
    P, K = Xs.shape[0], C.shape[0]
    ok = prune(ok & use[None, None, :])
    ndrug = len(starts)
    G = {}
    for gname, idx in (("WT", np.flatnonzero(wt & use)), ("alt", np.flatnonzero(~wt & use))):
        O = ok[:, :, idx]
        xt, yt = group_fit(Y, Xs, C, O, idx)
        G[gname] = {"idx": idx, "O": O, "xt": xt, "yt": yt, "sxx": (xt * xt).sum(axis=(2, 3)),
                    "sxy": (xt * yt[:, None]).sum(axis=(2, 3)),
                    "ncell": (O.sum(axis=2) > 0).sum(axis=1), "nline": (O.sum(axis=1) > 0).sum(axis=1)}
    W_, A_ = G["WT"], G["alt"]
    n = ok.sum(axis=(1, 2)).astype(float)
    p_all = 2 + 2 * K + W_["ncell"] + A_["ncell"] + W_["nline"] + A_["nline"] - 1
    stot = W_["sxx"] + A_["sxx"]
    with quiet():
        bW, bA = W_["sxy"] / W_["sxx"], A_["sxy"] / A_["sxx"]
        bC = (W_["sxy"] + A_["sxy"]) / stot

        def sums(Pg, b, den):                              # per-row influence -> compound x line, line, compound sums
            s = Pg["xt"] * (Pg["yt"][:, None] - b[:, :, None, None] * Pg["xt"]) / den[:, :, None, None]
            i_ = np.add.reduceat(s, starts, axis=2)       # genes x P x compounds x lines
            return i_, s.sum(axis=2), i_.sum(axis=3)
        iW, lW, dW = sums(W_, bW, W_["sxx"])
        iA, lA, dA = sums(A_, bA, A_["sxx"])
        iCW, lCW, dCW = sums(W_, bC, stot)
        iCA, lCA, dCA = sums(A_, bC, stot)
    cW = np.add.reduceat(W_["O"].astype(np.int32), starts, axis=1)
    cA = np.add.reduceat(A_["O"].astype(np.int32), starts, axis=1)
    Gd = ((cW.sum(axis=2) + cA.sum(axis=2)) > 0).sum(axis=1)
    Gl = W_["nline"] + A_["nline"]
    Gi = (cW > 0).sum(axis=(1, 2)) + (cA > 0).sum(axis=(1, 2))

    def cf(Gc, p):                                         # CR1: G/(G-1) (n-1)/(n-p)
        return (Gc / np.maximum(Gc - 1, 1) * (n - 1) / np.maximum(n - p, 1))[:, None]
    fd, fl, fi = cf(Gd, p_all), cf(Gl, p_all), cf(Gi, p_all)
    fdc, flc, fic = cf(Gd, p_all - 1), cf(Gl, p_all - 1), cf(Gi, p_all - 1)
    ssq = (lambda a: (a ** 2).sum(axis=2), lambda a: (a ** 2).sum(axis=(2, 3)))
    V_ = {"WT": (fd * ssq[0](dW), fl * ssq[0](lW), fi * ssq[1](iW)),
          "alt": (fd * ssq[0](dA), fl * ssq[0](lA), fi * ssq[1](iA)),
          "diff": (fd * ssq[0](dW - dA), fl * (ssq[0](lW) + ssq[0](lA)), fi * (ssq[1](iW) + ssq[1](iA))),
          "common": (fdc * ssq[0](dCW + dCA), flc * (ssq[0](lCW) + ssq[0](lCA)), fic * (ssq[1](iCW) + ssq[1](iCA)))}
    df = (np.minimum(Gd, Gl) - 1).astype(float)[:, None]
    out = {"b_WT": bW, "b_alt": bA, "diff": bW - bA, "b_common": bC}
    with quiet():
        for k_, (vd, vl, vi) in V_.items():
            out[f"se_{k_}"] = TW.se_conservative(vd, vl, vi)[0]
        out["se_diff_drug"], out["se_common_drug"] = np.sqrt(V_["diff"][0]), np.sqrt(V_["common"][0])
        for k_, est in (("diff", "diff"), ("common", "b_common"), ("WT", "b_WT"), ("alt", "b_alt")):
            t = out[est] / out[f"se_{k_}"]
            out[f"t_{k_}"] = t
            out[f"p_{k_}"] = np.where(df > 0, 2 * stats.t.sf(np.abs(t), np.maximum(df, 1)), np.nan)
        out["sd_x_resid"] = np.sqrt(stot / np.maximum(n, 1)[:, None])
    out["tested"] = ((n[:, None] >= MIN_ROWS) & (W_["nline"][:, None] >= MIN_LINES_GROUP)
                     & (A_["nline"][:, None] >= MIN_LINES_GROUP) & (Gd[:, None] >= MIN_DRUGS)
                     & (W_["sxx"] > 1e-10) & (A_["sxx"] > 1e-10) & np.isfinite(out["se_diff"]) & (out["se_diff"] > 0)
                     & np.isfinite(out["se_common"]) & (out["se_common"] > 0))
    res = {k_: np.asarray(v).T for k_, v in out.items()}               # P x genes
    shared = {"n_rows": n, "n_lines_WT": W_["nline"], "n_lines_alt": A_["nline"], "n_drugs": Gd, "df": df[:, 0],
              "n_drugdoses": ((W_["O"].sum(axis=2) + A_["O"].sum(axis=2)) > 0).sum(axis=1)}
    res.update({k_: np.broadcast_to(v, (P, m)) for k_, v in shared.items()})
    if want_scores:                                        # first exposure: cluster scores of diff and common
        res["scores"] = {}
        for est, sw, sa in (("diff", iW[:, 0], -iA[:, 0]), ("common", iCW[:, 0], iCA[:, 0])):
            inter = np.zeros((m, ndrug, L))
            inter[:, :, W_["idx"]] = sw
            inter[:, :, A_["idx"]] = sa
            res["scores"][est] = {"drug": inter.sum(axis=2), "line": inter.sum(axis=1), "inter": inter}
    return res


def resid_sd(Y, wt, use):
    """Per gene: RMS of its dd-level r2 after drug-dose x TP53-group FE and line FE (its own occupancy) and the number of
    cells (placebo matching on the exposure's response)."""
    ok = prune(np.isfinite(Y) & use[None, None, :])
    ss = np.zeros(Y.shape[0])
    for idx in (np.flatnonzero(wt & use), np.flatnonzero(~wt & use)):
        O = ok[:, :, idx]
        V = np.where(O, Y[:, :, idx], 0.0)[:, None]
        ss += (group_resid(V, O) ** 2).sum(axis=(1, 2, 3))
    n = ok.sum(axis=(1, 2))
    with quiet():
        return np.sqrt(ss / n), n


def contrast_z(Y, U, use):
    """(B1) TP53-WT minus TP53-altered contrast per gene x drug-dose for many labellings at once. Y: genes x drug-doses
    x lines; U: lines x labellings (1 = WT under that labelling); only the lines in use. z = (WT mean - altered mean) /
    (s sqrt(1/n_W + 1/n_A)), s = SD of the drug-dose's line values over all used lines (label-free, so the
    permutations are cheap); NaN unless >= 3 lines per group. Returns z (genes x drug-doses x labellings, float32) and,
    for the first labelling, the difference of means (log2) and the WT mean."""
    m, nd, _L = Y.shape
    Yl = Y[:, :, use]
    Ul = U[use].astype(np.float64)
    M = np.isfinite(Yl)
    Yf = np.where(M, Yl, 0.0).reshape(-1, Yl.shape[2])
    Mf = M.reshape(-1, Yl.shape[2]).astype(np.float64)
    n, s, q = Mf.sum(1), Yf.sum(1), (Yf * Yf).sum(1)
    with quiet():
        sd = np.sqrt(np.maximum(q / n - (s / n) ** 2, 0) * n / np.maximum(n - 1, 1))
        s1, n1 = Yf @ Ul, Mf @ Ul
        n2, s2 = n[:, None] - n1, s[:, None] - s1
        d = s1 / n1 - s2 / n2
        z = d / (sd[:, None] * np.sqrt(1 / n1 + 1 / n2))
    z[(n1 < 3) | (n2 < 3) | ~(sd[:, None] > 0)] = np.nan
    with quiet():
        wmean = s1[:, 0] / n1[:, 0]
    d0 = np.where((n1[:, 0] >= 3) & (n2[:, 0] >= 3), d[:, 0], np.nan)
    return (z.reshape(m, nd, -1).astype(np.float32), d0.reshape(m, nd).astype(np.float32),
            np.where(n1[:, 0] >= 3, wmean, np.nan).reshape(m, nd).astype(np.float32))


# ============================================================================= (B) the Tahoe p53 program
def labellings(wt, lab, B, rng):
    """lines x (1 + B) bool: column 0 = the TP53-WT lines, columns 1..B = the labels permuted over the labelled lines
    (group sizes kept). One set serves every gene and drug-dose, so their correlation is kept."""
    U = np.zeros((len(wt), B + 1), bool)
    U[:, 0] = wt & lab
    li = np.flatnonzero(lab)
    for b in range(1, B + 1):
        U[li, b] = rng.permutation(wt[li])
    return U


def feature_labellings(fx, wt, lab, rng):
    """The atlas's line groupings (tahoe_atlas.genotype_features: drivers, protein changes, organs, MTAP loss) within
    the labelled lines (>= 3 lines in and out), each followed by N_FEAT_PERM permutations of itself. Returns names,
    sizes, whether the grouping is the TP53 split itself, and U (lines x groupings*(1+N_FEAT_PERM))."""
    li = np.flatnonzero(lab)
    names, sizes, same, cols = [], [], [], []
    for nm, mem in A.genotype_features(fx).items():
        m_ = np.zeros(len(wt), bool)
        m_[list(mem)] = True
        m_ &= lab
        k = int(m_.sum())
        if k < 3 or len(li) - k < 3:
            continue
        names.append(nm)
        sizes.append(k)
        same.append(bool((m_[li] == wt[li]).all() or (m_[li] == ~wt[li]).all()))
        cols.append(m_)
        for _ in range(N_FEAT_PERM):
            c = np.zeros(len(wt), bool)
            c[li] = rng.permutation(m_[li])
            cols.append(c)
    return names, sizes, same, (np.column_stack(cols) if cols else np.zeros((len(wt), 0), bool))


def topk_update(top, z, k):
    """Running top-k (over genes, axis 0) of z^2 per drug-dose x labelling (NaN counts as 0)."""
    z2 = np.nan_to_num(z * z)
    cat = z2 if top is None else np.concatenate([top, z2])
    return cat if cat.shape[0] <= k else np.partition(cat, -k, axis=0)[-k:]


def b_pass1(T, grid, U, wt, lab, chunk, cpath):
    """(B1, B2) Pass 1 over every gene and drug-dose, all labellings: the contrast z, a running top-k of z^2 per
    drug-dose and labelling (k = max(10, 1% of genes)) -> divergence D = log mean of the top k; kept for the later
    passes: z, the WT-minus-altered difference and the WT mean at the true labels (genes x drug-doses, float32), and the
    per-gene residual SD after the ddxg FE (placebo matching)."""
    z = load_npz(cpath)
    if z is not None:
        log(f"(B) pass 1: cache {os.path.basename(cpath)}")
        return z
    t0 = time.time()
    G, nd = T.G, grid.nd
    k = max(10, int(round(TOPK_FRAC * G)))
    top = None
    z0, d0, w0 = (np.full((G, nd), np.nan, np.float32) for _ in range(3))
    rsd, nres = np.full(G, np.nan), np.zeros(G, np.int64)
    for g0 in range(0, G, chunk):
        g1 = min(G, g0 + chunk)
        Y = dd_level(T.read(g0, g1), grid.B)
        z, d, wm = contrast_z(Y, U, lab)
        z0[g0:g1], d0[g0:g1], w0[g0:g1] = z[:, :, 0], d, wm
        top = topk_update(top, z, k)
        rsd[g0:g1], nres[g0:g1] = resid_sd(Y, wt, lab)
        if (g0 // chunk) % max(1, (G // chunk) // 10) == 0:
            log(f"  (B) pass 1: {g1}/{G} genes ({time.time() - t0:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")
    with quiet():
        D = np.log(top.astype(np.float64).mean(axis=0))
    res = {"D": D, "z0": z0, "d0": d0, "w0": w0, "rsd": rsd, "nres": nres, "k": np.int64(k)}
    save_npz(cpath, **res)
    return res


def dd_weights(sets, cols, comp):
    """(B3) Drug-equal weights over the drug-doses cols: W (len(cols) x sets), set v gets 1 / (K_v n_k,v) on its
    drug-doses (K_v compounds, n_k,v doses of compound k in the set), so each compound counts equally; plus each set's
    compound indicator block (len(cols) x K_v)."""
    pos = {int(d): i for i, d in enumerate(cols)}
    W = np.zeros((len(cols), len(sets)))
    blocks = []
    for v, S in enumerate(sets):
        S = [int(d) for d in S]
        cnt = pd.Series(comp[S]).value_counts() if S else pd.Series(dtype=float)
        for d in S:
            W[pos[d], v] = 1.0 / (len(cnt) * cnt[comp[d]])
        Kb = np.zeros((len(cols), len(cnt)))
        for j, c in enumerate(sorted(cnt.index)):
            Kb[[pos[d] for d in S if comp[d] == c], j] = 1.0
        blocks.append(Kb)
    return W, blocks


def null_z(mv, n_null):
    """mv: genes x labellings (column 0 true). For b = 1..n_null the calibrated z of labelling b treated as the truth,
    against the other permuted labellings (b left out of its own null)."""
    rest = mv[:, 1:]
    fin = np.isfinite(rest)
    r0 = np.where(fin, rest, 0.0)
    S, Q, N = r0.sum(axis=1), (r0 ** 2).sum(axis=1), fin.sum(axis=1)
    out = np.full((mv.shape[0], n_null), np.nan, np.float32)
    with quiet():
        for b in range(1, min(n_null, mv.shape[1] - 1) + 1):
            mb = mv[:, b]
            fb = np.isfinite(mb)
            mb0 = np.where(fb, mb, 0.0)
            n_ = N - fb
            mu = (S - mb0) / n_
            var = (Q - mb0 ** 2 - n_ * mu ** 2) / (n_ - 1)
            out[:, b - 1] = (mb - mu) / np.sqrt(var)
    return out


def perm_fdr(z, zn, mask, sizes=True):
    """(B) Permutation FDR across drug-doses (selections S1 and S2). z (n,): the calibrated z of the true labelling;
    zn (n x B): the same z of each permuted labelling treated as the truth (null_z); -inf = a drug-dose the rule cannot
    select (S2: score <= 0), NaN = no value. p = pooled one-sided p of z against every (drug-dose in mask, labelling)
    value of zn; q = BH of p over mask, i.e. the mean count of a permuted labelling's drug-doses at or above the
    threshold over the observed count. Pooling keeps what a normal tail of the calibrated z misses: the null is skewed,
    and all drug-doses share one labelling (a labelling that lines up with a strong line axis lifts many drug-doses at
    once). With sizes, also each permuted labelling's selection size under the same rule (its z against the pooled
    null of the other labellings): the null sizes."""
    z = np.asarray(z, np.float64)
    Z = np.asarray(zn, np.float64)[mask]
    nul = np.sort(Z[~np.isnan(Z)])
    p = np.full(len(z), np.nan)
    if not len(nul):
        return p, p.copy(), []

    def above(srt, v):                                     # #values >= v
        return len(srt) - np.searchsorted(srt, v - 1e-12, side="left")
    m = mask & ~np.isnan(z)
    p[m] = (1 + above(nul, z[m])) / (1 + len(nul))
    q = bh(p)
    out = []
    for b in range(Z.shape[1] if sizes else 0):
        col = Z[:, b][~np.isnan(Z[:, b])]
        own = np.sort(col)
        pb = (1 + above(nul, col) - above(own, col)) / (1 + len(nul) - len(own))
        out.append(int((bh(pb) < Q_SEL).sum()))
    return p, q, out


def b_pass_sets(T, grid, U, lab, cols, sets, chunk, n_null=0, UF=None, fpos=None, k=10):
    """(B3) One pass over every gene on the drug-doses cols, all labellings: per gene and drug-dose set the drug-equal
    mean z (m_g^b) -> calibrated program z (zm, genes x sets) and the compounds with a z (true labels); for the first
    set also the null z of the first n_null permuted labellings; with UF (line groupings), the top-k mean of their
    contrast z^2 per drug-dose for the drug-doses at positions fpos of cols (the specificity check)."""
    W, blocks = dd_weights(sets, cols, grid.drug_id)
    Bsub = grid.B[np.asarray(cols)]
    G = T.G
    zm = np.full((G, len(sets)), np.nan, np.float32)
    m0 = np.full((G, len(sets)), np.nan, np.float32)
    ncomp = np.zeros((G, len(sets)), np.int32)
    nullz = np.full((G, n_null), np.nan, np.float32)
    ftop = None
    for g0 in range(0, G, chunk):
        g1 = min(G, g0 + chunk)
        Y = dd_level(T.read(g0, g1), Bsub)
        z = contrast_z(Y, U, lab)[0]
        fin = np.isfinite(z)
        num = np.matmul(np.where(fin, z, 0.0).astype(np.float64).transpose(0, 2, 1), W)    # genes x labellings x sets
        den = np.matmul(fin.astype(np.float64).transpose(0, 2, 1), W)
        with quiet():
            mv = (num / den).transpose(0, 2, 1)                                              # genes x sets x labellings
        zm[g0:g1] = calib(mv[:, :, 0], mv[:, :, 1:])
        m0[g0:g1] = mv[:, :, 0]
        F0 = fin[:, :, 0].astype(np.float64)
        for v, Kb in enumerate(blocks):
            ncomp[g0:g1, v] = ((F0 @ Kb) > 0).sum(axis=1) if Kb.shape[1] else 0
        if n_null:
            nullz[g0:g1] = null_z(mv[:, 0, :], n_null)
        if UF is not None and UF.shape[1] and len(fpos):
            Yf = Y[:, fpos]
            parts = []
            for j0 in range(0, UF.shape[1], 1050):     # bounded memory: ~50 groupings x 21 labellings at a time
                parts.append(contrast_z(Yf, UF[:, j0:j0 + 1050], lab)[0])
            ftop = topk_update(ftop, np.concatenate(parts, axis=2), k)
    out = {"zm": zm, "m0": m0, "ncomp": ncomp, "nullz": nullz}
    if ftop is not None:
        with quiet():
            out["D_feat"] = np.log(ftop.astype(np.float64).mean(axis=0))          # fdd x groupings*(1+NFP)
    return out


def b_pass_scores(T, grid, U, lab, sigs, chunk):
    """(B4) Every drug-dose x labelling scored with each signature: s = mean over the signature's genes of z (only the
    signature genes are read)."""
    genes = np.array(sorted(set(int(g) for s in sigs for g in s)), dtype=np.int64)
    Ms = np.zeros((len(genes), len(sigs)))
    pos = {g: i for i, g in enumerate(genes)}
    for j, s in enumerate(sigs):
        Ms[[pos[int(g)] for g in s], j] = 1.0
    S = np.zeros((len(sigs), grid.nd, U.shape[1]))
    N = np.zeros_like(S)
    for c0 in range(0, len(genes), chunk):
        ii = genes[c0:c0 + chunk]
        z = contrast_z(dd_level(T.take(ii), grid.B), U, lab)[0]
        fin = np.isfinite(z)
        S += np.tensordot(Ms[c0:c0 + chunk], np.where(fin, z, 0.0).astype(np.float64), axes=([0], [0]))
        N += np.tensordot(Ms[c0:c0 + chunk], fin.astype(np.float64), axes=([0], [0]))
    with quiet():
        return S / N


def b_selectivity(T, grid, Ulist, lab, cols, S, genes, chunk):
    """P's selectivity under several labellings: per labelling the mean over the program genes of the drug-equal mean
    z over S (cols = S). Returns one vector per labelling matrix in Ulist."""
    W, _ = dd_weights([S], cols, grid.drug_id)
    Bsub = grid.B[np.asarray(cols)]
    acc = [np.zeros(Uq.shape[1]) for Uq in Ulist]
    cnt = [np.zeros(Uq.shape[1]) for Uq in Ulist]
    genes = np.asarray(genes, dtype=np.int64)
    for c0 in range(0, len(genes), chunk):
        Y = dd_level(T.take(genes[c0:c0 + chunk]), Bsub)
        for j, Uq in enumerate(Ulist):
            if not Uq.shape[1]:
                continue
            z = contrast_z(Y, Uq, lab)[0]
            fin = np.isfinite(z)
            with quiet():
                mv = (np.where(fin, z, 0.0).astype(np.float64).transpose(0, 2, 1) @ W)[:, :, 0] / \
                     (fin.astype(np.float64).transpose(0, 2, 1) @ W)[:, :, 0]               # genes x labellings
            f2 = np.isfinite(mv)
            acc[j] += np.where(f2, mv, 0.0).sum(axis=0)
            cnt[j] += f2.sum(axis=0)
    with quiet():
        return [a / c for a, c in zip(acc, cnt)]


def set_stats(S, p1, comp):
    """Per gene, from the true-label pass-1 arrays over the drug-doses S (drug-equal weights): the mean WT-minus-altered
    difference (log2) and WT mean; the share of compounds (with a value) whose mean z is > 0 / < 0 and whose WT mean
    is > 0 / < 0; the number of compounds with a z."""
    S = np.asarray(S, dtype=np.int64)
    G = p1["z0"].shape[0]
    if not len(S):
        nan = np.full(G, np.nan)
        return {"dbar": nan, "wtbar": nan, "frac_up": nan, "frac_down": nan, "frac_wt_up": nan,
                "frac_wt_down": nan, "n_comp": np.zeros(G, int)}
    cnt = pd.Series(comp[S]).value_counts()
    w = np.array([1.0 / (len(cnt) * cnt[comp[d]]) for d in S])
    z0, d0, w0 = (p1[k_][:, S].astype(np.float64) for k_ in ("z0", "d0", "w0"))

    def wmean(V):
        f = np.isfinite(V)
        with quiet():
            return (np.where(f, V, 0.0) @ w) / (f @ w)

    def cmean(V):
        with quiet():
            return np.column_stack([np.nanmean(V[:, comp[S] == c], axis=1) for c in sorted(cnt.index)])
    a, aw = cmean(z0), cmean(w0)
    na, nw_ = np.isfinite(a).sum(axis=1), np.isfinite(aw).sum(axis=1)
    with quiet():
        return {"dbar": wmean(d0), "wtbar": wmean(w0), "frac_up": (a > 0).sum(axis=1) / na,
                "frac_down": (a < 0).sum(axis=1) / na, "frac_wt_up": (aw > 0).sum(axis=1) / nw_,
                "frac_wt_down": (aw < 0).sum(axis=1) / nw_, "n_comp": na}


def program_rule(zm, ncomp, st, excl, sign, min_comp):
    """(B3) The program of a drug-dose set in direction sign (+1 WT-selective induction, -1 repression): BH q < 0.05
    over genes in that direction, WT minus altered in that direction (drug-weighted and in >= half the compounds) and
    the WT arm itself in that direction (drug-weighted WT mean, and in >= half the compounds; a lineage- or
    driver-selective repression of the altered lines alone does not qualify). Fewer than PROG_MIN genes: the top
    PROG_FALLBACK by z with the same direction rules ('small program'). Returns (genes by z, q, p, small)."""
    with quiet():
        p = stats.norm.sf(sign * zm)
        dir_ok = ((sign * st["dbar"] > 0) & (sign * st["wtbar"] > 0)
                  & ((st["frac_up"] if sign > 0 else st["frac_down"]) >= 0.5)
                  & ((st["frac_wt_up"] if sign > 0 else st["frac_wt_down"]) >= 0.5))
    p = np.where(np.isfinite(zm) & (ncomp >= min_comp) & ~excl, p, np.nan)
    q = bh(p)
    sel = np.flatnonzero((q < Q_SEL) & dir_ok)
    small = False
    if len(sel) < PROG_MIN:
        cand = np.flatnonzero(np.isfinite(p) & dir_ok & (sign * zm > 0))
        sel = cand
        small = True
    sel = sel[np.argsort(-sign * zm[sel], kind="stable")]
    return (sel[:PROG_FALLBACK] if small else sel), q, p, small


def top_signature(zm, ncomp, st, excl, N):
    """Out-of-fold scoring signature: the top N genes by program z with WT minus altered > 0 (one compound allowed)."""
    with quiet():
        cand = np.flatnonzero(np.isfinite(zm) & (ncomp >= 1) & ~excl & (st["dbar"] > 0) & (zm > 0))
    return cand[np.argsort(-zm[cand], kind="stable")][:N]


def jaccard(a, b):
    a, b = set(int(x) for x in a), set(int(x) for x in b)
    return len(a & b) / len(a | b) if (a or b) else np.nan


def derive_program(T, grid, fx, wt, lab, U, p1, x_idx, ddz_x, n_folds, chunk, UFt, ck, info):
    """(B) Selections S1, folds, out-of-fold scores, S2, the program P and its variants (see the module docstring).
    Returns a dict with every set, per-gene and per-drug-dose statistic needed for the tables."""
    G, nd = T.G, grid.nd
    dd = grid.dd
    comp = grid.drug_id
    cname = dd["drug"].astype(str).to_numpy()
    keep = ~(fx.dd["unreliable_plate_only"].to_numpy(bool) | fx.dd["position_not_correctable"].to_numpy(bool))
    excl = np.zeros(G, bool)
    excl[x_idx] = True
    N_sig = max(25, int(round(TOPN_FRAC * G)))
    k = int(p1["k"])
    fnames, fsizes, fsame, UF = UFt
    R = {"keep": keep, "N_sig": N_sig, "flags": []}

    def ncompounds(S):
        return len(set(comp[np.asarray(S, dtype=np.int64)])) if len(S) else 0

    # --- selection 1: genome-wide WT-vs-altered divergence per drug-dose (permutation FDR across drug-doses)
    D = p1["D"]
    zD = calib(D[:, 0], D[:, 1:])
    zD20 = calib(D[:, 0], D[:, 1:1 + N_FEAT_PERM])
    pD, qD, null_S1 = perm_fdr(zD, null_z(D, D.shape[1] - 1), keep)
    S1 = np.flatnonzero(qD < Q_SEL)
    n_S1_q = len(S1)
    s1_fallback = ncompounds(S1) < 2
    if s1_fallback:
        cand = np.flatnonzero(keep & np.isfinite(zD))
        S1 = np.sort(cand[np.argsort(-zD[cand], kind="stable")][:10])
        R["flags"].append("S1 fallback: fewer than 2 compounds at permutation FDR < 0.05; the top 10 keep drug-doses "
                          "by zD used (S2 and the program are exploratory)")
    R.update(zD=zD, zD20=zD20, pD=pD, qD=qD, S1=S1, n_S1_q=n_S1_q, null_S1=null_S1, s1_fallback=s1_fallback)
    # --- compound folds, dealt after S1 (S1 compounds round-robin by their best zD, the others by a seeded permutation)
    best = pd.Series(zD[S1], index=S1).groupby(comp[S1]).max()
    s1c = [int(c) for c in sorted(best.index, key=lambda c: (-best[c], cname[np.flatnonzero(comp == c)[0]]))]
    F = max(1, min(n_folds, len(s1c)))
    fold_c = {c: i % F for i, c in enumerate(s1c)}
    others = sorted(set(int(c) for c in comp) - set(s1c), key=lambda c: cname[np.flatnonzero(comp == c)[0]])
    for j, i in enumerate(np.random.default_rng([SEED, 2]).permutation(len(others))):
        fold_c[others[i]] = j % F
    fold = np.array([fold_c[int(c)] for c in comp])
    R.update(F=F, fold=fold)
    if F < 2:
        R["flags"].append("cross-fitting impossible: S1 has one compound (F_eff = 1); every cross-fitted program falls "
                          "back to P")
    pairs = [(f, g) for f in range(F) for g in range(f + 1, F)]
    # --- pass 2: all genes on S1 (S1, S1 minus fold f, S1 minus folds f and g) + specificity on S1
    sets2 = [S1] + [S1[fold[S1] != f] for f in range(F)] + [S1[(fold[S1] != f) & (fold[S1] != g)] for f, g in pairs]
    fpos1 = np.argsort(-zD[S1], kind="stable")[:FEAT_DD_MAX]
    t0 = time.time()
    r2 = b_pass_sets(T, grid, U, lab, S1, sets2, chunk, UF=UF, fpos=fpos1, k=k)
    log(f"  (B) pass 2 (all genes on the {len(S1)} S1 drug-doses): {time.time() - t0:.0f} s")
    st1 = set_stats(S1, p1, comp)
    P1, q1, _p1p, small1 = program_rule(r2["zm"][:, 0], r2["ncomp"][:, 0], st1, excl, +1, 2)
    sig = {"all": top_signature(r2["zm"][:, 0], r2["ncomp"][:, 0], st1, excl, N_sig)}
    for f in range(F):
        S_ = sets2[1 + f]
        if ncompounds(S_):
            sig[("f", f)] = top_signature(r2["zm"][:, 1 + f], r2["ncomp"][:, 1 + f], set_stats(S_, p1, comp), excl, N_sig)
    for j, (f, g) in enumerate(pairs):
        S_ = sets2[1 + F + j]
        if ncompounds(S_):
            sig[("fg", f, g)] = top_signature(r2["zm"][:, 1 + F + j], r2["ncomp"][:, 1 + F + j],
                                              set_stats(S_, p1, comp), excl, N_sig)
    sig = {k_: v for k_, v in sig.items() if len(v)}
    R.update(P1=P1, zm1=r2["zm"][:, 0], q1=q1, small1=small1, sig=sig, D_feat1=r2.get("D_feat"), fdd1=S1[fpos1])
    # --- pass 3: every drug-dose scored with each signature; out-of-fold score; S2
    keys = list(sig)
    t0 = time.time()
    s = b_pass_scores(T, grid, U, lab, [sig[k_] for k_ in keys], chunk)
    log(f"  (B) pass 3 ({len(keys)} signatures, {len(set(int(g) for v in sig.values() for g in v))} genes, every "
        f"drug-dose): {time.time() - t0:.0f} s")
    zs = calib(s[:, :, 0], s[:, :, 1:])
    zsn = np.stack([null_z(s[j], s.shape[2] - 1) for j in range(len(keys))])     # signatures x drug-doses x labellings
    ar = np.arange(nd)
    kpos = {k_: i for i, k_ in enumerate(keys)}

    def s2_z(ii, rows_ok):
        """Observed and null z of the S2 rule for the signature choice ii (-1: none): the calibrated z where the score
        is > 0, else -inf (not selectable); NaN without a value or outside rows_ok."""
        j_ = np.maximum(ii, 0)
        has = (ii >= 0) & rows_ok
        s_, z_, zn_ = s[j_, ar], zs[j_, ar], zsn[j_, ar]
        with quiet():
            zo = np.where(has & np.isfinite(z_), np.where(s_[:, 0] > 0, z_, -np.inf), np.nan)
            zb = np.where(has[:, None] & np.isfinite(zn_), np.where(s_[:, 1:] > 0, zn_, -np.inf), np.nan)
        return zo, zb

    def pick(d, f_excl=None):
        """Signature index for drug-dose d: out of its own fold (and out of fold f_excl, nested), else a fallback."""
        g = int(fold[d])
        if f_excl is None:
            if ("f", g) in kpos:
                return kpos[("f", g)], "out of fold"
            return kpos.get("all"), "NOT out of fold (no S1 compound outside the fold)"
        a, b = min(f_excl, g), max(f_excl, g)
        if a != b and ("fg", a, b) in kpos:
            return kpos[("fg", a, b)], "nested"
        if ("f", f_excl) in kpos:
            return kpos[("f", f_excl)], "nested fallback: signature of S1 minus fold f only"
        return kpos.get("all"), "NOT cross-fitted (no signature without fold f)"
    oof = [pick(d) for d in range(nd)]
    oi = np.array([-1 if o[0] is None else o[0] for o in oof])
    s0 = np.where(oi >= 0, s[np.maximum(oi, 0), ar, 0], np.nan)
    zs_oof = np.where(oi >= 0, zs[np.maximum(oi, 0), ar], np.nan)
    ps_oof, qs_oof, null_S2 = perm_fdr(*s2_z(oi, keep), keep)
    S2 = np.flatnonzero(keep & (qs_oof < Q_SEL) & (s0 > 0))
    n_S2_q = len(S2)
    n_not_oof = int(sum(1 for d in range(nd) if keep[d] and not oof[d][1].startswith("out of fold")))
    if n_not_oof:
        R["flags"].append(f"{n_not_oof} keep drug-doses scored with a signature that is not out of fold")
    if ncompounds(S2) < 2:
        R["flags"].append(f"S2 fallback: {ncompounds(S2)} compound(s) at permutation FDR < 0.05 out of fold; S2 = S1")
        S2 = S1.copy()
    elif s1_fallback:
        R["flags"].append("S2 rests on the S1 fallback: its signatures come from the top 10 drug-doses by zD and its "
                          "null holds them fixed, so S2 and the program are exploratory")
    R.update(s_oof=s0, zs_oof=zs_oof, ps_oof=ps_oof, qs_oof=qs_oof, oof_how=[o[1] for o in oof], S2=S2,
             n_S2_q=n_S2_q, null_S2=null_S2)
    S2f, nested_fb = [], []
    for f in range(F):
        tr = keep & (fold != f)
        pk = [pick(d, f) if tr[d] else (None, "") for d in range(nd)]
        ii = np.array([-1 if (p_[0] is None) else p_[0] for p_ in pk])
        sf0 = np.where(ii >= 0, s[np.maximum(ii, 0), ar, 0], np.nan)
        qf = perm_fdr(*s2_z(ii, tr), tr, sizes=False)[1]
        Sf = np.flatnonzero(tr & (qf < Q_SEL) & (sf0 > 0))
        nfb = sum(1 for d in range(nd) if tr[d] and not pk[d][1] == "nested")
        nested_fb.append(nfb)
        if ncompounds(Sf) < 1:
            Sf = S1[fold[S1] != f]
            R["flags"].append(f"fold {f}: no drug-dose selected out of fold; S2_-f = S1 minus fold {f}")
        S2f.append(Sf)
    R.update(S2f=S2f, nested_fallback=nested_fb)
    # --- pass 4: all genes on S2 and the S2_-f; P, P-down, P_-f, P_noX, leave-one-compound-out, null sizes
    X = keep & (np.abs(ddz_x) >= 3)
    s2c = sorted(set(int(c) for c in comp[S2]))
    sets4 = [S2] + S2f + [S2[~X[S2]]] + [S2[comp[S2] != c] for c in s2c]
    cols4 = np.array(sorted(set(int(d) for S_ in sets4 for d in S_)), dtype=np.int64)
    pos4 = {int(d): i for i, d in enumerate(cols4)}
    o2 = S2[np.argsort(-np.nan_to_num(zs_oof[S2], nan=-np.inf), kind="stable")][:FEAT_DD_MAX]
    fpos4 = np.array([pos4[int(d)] for d in o2], dtype=np.int64)
    t0 = time.time()
    r4 = b_pass_sets(T, grid, U, lab, cols4, sets4, chunk, n_null=N_NULL_PROG, UF=UF, fpos=fpos4, k=k)
    log(f"  (B) pass 4 (all genes on the {len(cols4)} drug-doses of S2 and the S2_-f): {time.time() - t0:.0f} s")
    st2 = set_stats(S2, p1, comp)
    P, q_up, p_up, small = program_rule(r4["zm"][:, 0], r4["ncomp"][:, 0], st2, excl, +1, 2)
    Pd, q_dn, p_dn, small_d = program_rule(r4["zm"][:, 0], r4["ncomp"][:, 0], st2, excl, -1, 2)
    if small:
        R["flags"].append(f"small program: fewer than {PROG_MIN} genes pass; P = the top {PROG_FALLBACK} by z")
    if small_d:
        R["flags"].append(f"P-down fallback: fewer than {PROG_MIN} genes pass; P-down = the top {PROG_FALLBACK} by z "
                          "(exploratory)")
    Pf, Pdf, fstat, small_f, small_df = [], [], [], [], []
    for f in range(F):
        nc_ = ncompounds(S2f[f])
        if nc_ < 1:
            Pf.append(np.array([], int))
            Pdf.append(np.array([], int))
            fstat.append("no training drug-doses")
            small_f.append(False)
            small_df.append(False)
            continue
        stf = set_stats(S2f[f], p1, comp)
        a_, _, _, sm_ = program_rule(r4["zm"][:, 1 + f], r4["ncomp"][:, 1 + f], stf, excl, +1, min(2, nc_))
        b_, _, _, smd_ = program_rule(r4["zm"][:, 1 + f], r4["ncomp"][:, 1 + f], stf, excl, -1, min(2, nc_))
        Pf.append(a_)
        Pdf.append(b_)
        small_f.append(bool(sm_))
        small_df.append(bool(smd_))
        fstat.append(("cross-fitted" if F >= 2 else "NOT cross-fitted") + (" (single training compound)" if nc_ == 1
                                                                           else "") + (" (small)" if sm_ else "")
                     + (" (P-down small)" if smd_ else ""))
    for nm_, fl_ in (("P", small_f), ("P-down", small_df)):
        if any(fl_):
            R["flags"].append(f"{nm_}_-f fallback (top {PROG_FALLBACK} by z) in fold(s) "
                              f"{', '.join(str(f) for f in range(F) if fl_[f])}")
    jx = 1 + F
    PnoX, small_noX = np.array([], int), False
    if ncompounds(sets4[jx]) >= 2:
        PnoX, _, _, small_noX = program_rule(r4["zm"][:, jx], r4["ncomp"][:, jx], set_stats(sets4[jx], p1, comp), excl,
                                             +1, 2)
    loco = {}
    for j, c in enumerate(s2c):
        S_ = sets4[jx + 1 + j]
        if ncompounds(S_) >= 1:
            loco[c] = program_rule(r4["zm"][:, jx + 1 + j], r4["ncomp"][:, jx + 1 + j], set_stats(S_, p1, comp), excl,
                                   +1, min(2, ncompounds(S_)))[0]
    null_sizes = []
    for b in range(r4["nullz"].shape[1]):
        pb = np.where(excl | (r4["ncomp"][:, 0] < 2), np.nan, stats.norm.sf(r4["nullz"][:, b]))
        null_sizes.append(int((bh(pb) < Q_SEL).sum()))
    n_obs_zonly = int((q_up < Q_SEL).sum())
    R.update(P=P, Pd=Pd, zm=r4["zm"][:, 0], m0=r4["m0"][:, 0], q_up=q_up, p_up=p_up, q_dn=q_dn, p_dn=p_dn, st2=st2,
             st1=st1, small=small, small_d=small_d, small_f=small_f, small_df=small_df, small_noX=bool(small_noX),
             Pf=Pf, Pdf=Pdf, fold_status=fstat, PnoX=PnoX, X=X, loco=loco,
             s2c=s2c, null_sizes=null_sizes, n_obs_zonly=n_obs_zonly, ncomp=r4["ncomp"][:, 0],
             D_feat2=r4.get("D_feat"), fdd2=o2)
    # --- pass 5: P's selectivity: TP53 (true + 20 permutations) vs each line grouping (true + 20 permutations)
    if len(P) and ncompounds(S2) >= 1:
        t0 = time.time()
        selv = b_selectivity(T, grid, [U[:, :1 + N_FEAT_PERM], UF], lab, S2, S2, P, chunk)
        R["sel_tp53"] = float(calib(selv[0][0], selv[0][1:]))
        R["sel_feat"] = [float(calib(selv[1][j * (1 + N_FEAT_PERM)], selv[1][j * (1 + N_FEAT_PERM) + 1:
                                                                              (j + 1) * (1 + N_FEAT_PERM)]))
                         for j in range(len(fnames))]
        log(f"  (B) pass 5 (P's selectivity, {len(fnames)} line groupings): {time.time() - t0:.0f} s")
    return R


# ============================================================================= gene sets and program scores
def set_means(T, grid, sets, chunk=128):
    """Per (well, line) the mean r2 over each set's genes (NaN-aware: the members the line expresses), then the
    drug-dose mean over used wells (as two_way's P53_SCORE). Reads only the member genes. Returns [drug-doses x lines]."""
    genes = np.array(sorted(set(int(g) for s in sets for g in s)), dtype=np.int64)
    if not len(genes):
        return [np.full((grid.nd, T.L), np.nan) for _ in sets]
    pos = {g: i for i, g in enumerate(genes)}
    M = np.zeros((len(genes), len(sets)))
    for j, s in enumerate(sets):
        M[[pos[int(g)] for g in s], j] = 1.0
    S = np.zeros((len(sets), T.NW * T.L))
    N = np.zeros_like(S)
    for c0 in range(0, len(genes), chunk):
        blk = T.take(genes[c0:c0 + chunk]).reshape(-1, T.NW * T.L)
        f = np.isfinite(blk)
        S += M[c0:c0 + chunk].T @ np.where(f, blk, 0.0).astype(np.float64)
        N += M[c0:c0 + chunk].T @ f.astype(np.float64)
    with quiet():
        Wl = np.where(N > 0, S / N, np.nan)
    return [TW.Grid.dd_mean(grid.B, Wl[j].reshape(T.NW, T.L)) for j in range(len(sets))]


def atlas_programs(fx, T, grid, tok2idx, folder):
    """(D) tahoe_atlas.angle_programs (data-driven programs: SVD of the atlas well z of responsive genes, broad axes
    removed, k-means with the function's own seed) written into folder, with two attributes of tahoe_atlas swapped for
    the call: write_brief (no agent brief) and per_line_columns (the per-line program means from the tensor instead of
    a second 20 GB pseudobulk pass; the mean member r2, not the atlas's log of summed counts). Returns {program: tensor
    gene indices}."""
    held = {}

    def plc(_fx, specs, gene_cols=None):
        held["specs"] = dict(specs)
        names = list(specs)
        mem = [[tok2idx[int(t)] for t in specs[nm] if int(t) in tok2idx] for nm in names]
        return np.stack(set_means(T, grid, mem), axis=2).astype(np.float32) if names else \
            np.zeros((grid.nd, T.L, 0), np.float32)
    os.makedirs(folder, exist_ok=True)
    saved = (A.write_brief, A.per_line_columns)
    A.write_brief = lambda *a, **k: None
    A.per_line_columns = plc
    try:
        A.angle_programs(fx, folder)
    finally:
        A.write_brief, A.per_line_columns = saved
    return {nm: np.array(sorted({tok2idx[int(t)] for t in toks if int(t) in tok2idx}), dtype=np.int64)
            for nm, toks in held.get("specs", {}).items()}


def gm_symbol(s, sym2idx):
    """gene_modules.csv 'gene/assay' -> atlas symbol (first word; 'TRIM72_total' -> TRIM72), else None."""
    tok = str(s).split(" ")[0].split("(")[0].strip()
    if tok in sym2idx:
        return tok
    base = tok.split("_")[0]
    return base if base in sym2idx else None


def overlay_sets(sym2idx, sib, ck):
    """Curated lists, used only as labelled overlays after the genome-wide results: the panel's 21-gene P53_ACTIVITY,
    mg53_p53/gene_modules.csv (each module, and the unions p53 and MG53-linked pathways), CollecTRI TP53-activated
    targets if upstream_tf's cache has the file (never downloaded here). Returns {name: (symbols, source)}."""
    out = {"OVERLAY_P53_ACTIVITY21": ([g for g in TW.DP.P.P53_ACTIVITY], "tahoe_gene_panel.P53_ACTIVITY (21 genes)")}

    def gm():
        t = pd.read_csv(os.path.join(MGDIR, "gene_modules.csv"))
        t["sym"] = [gm_symbol(s, sym2idx) for s in t["gene/assay"]]
        res = {}
        for mod, g in t.groupby("module", sort=True):
            res[f"OVERLAY_GM_{mod}"] = ([s for s in g["sym"] if s], f"gene_modules.csv module {mod}")
        u = t[t["module"].isin(["p53_primary", "p53_secondary"])]["sym"]
        res["OVERLAY_GM_p53_all"] = ([s for s in u if s], "gene_modules.csv p53_primary + p53_secondary")
        u = t[t["module"].astype(str).str.startswith("screen_") | (t["module"] == "stress_markers")]["sym"]
        res["OVERLAY_GM_MG53_pathways"] = ([s for s in u if s], "gene_modules.csv screen_* + stress_markers")
        return res
    out.update(optional("overlay: gene_modules.csv", gm, ck, {}))

    def collectri():
        p = os.path.join(sib, "upstream_tf", "cache", "external", "collectri.tsv")
        if not os.path.exists(p):
            ck.add("overlay: CollecTRI TP53 targets", np.nan, note=f"not used: {os.path.relpath(p, sib)} (next to this "
                   "step's folder) not present; never downloaded here")
            return {}
        reg = UT.read_regulon(p, "CollecTRI")
        tg = sorted(reg.loc[(reg["tf"] == "TP53") & (reg["weight"] > 0), "target"].astype(str))
        return {"OVERLAY_CollecTRI_TP53_activated": (tg, f"CollecTRI ({p}), TP53 activated targets")}
    out.update(optional("overlay: CollecTRI", collectri, ck, {}))
    return out


def build_registry(B_, atlas_progs, overlays, sym2idx, x_idx, rt_idx, ck):
    """Every gene set of the step: the data-derived p53 programs, the atlas programs, the overlays. The exposure is
    removed from every set before any scoring; sets left with < tahoe_atlas.MODULE_MIN genes are kept for annotation
    but not tested (column tested_as_set); sets holding the readthrough covariate genes are flagged."""
    reg = []

    def add(name, role, members, source):
        mem = np.array(sorted(set(int(g) for g in members) - {int(x_idx)}), dtype=np.int64)
        n_raw = len(set(int(g) for g in members))
        reg.append({"name": name, "role": role, "members": mem, "n_raw": n_raw, "n": len(mem), "source": source,
                    "tested_as_set": len(mem) >= A.MODULE_MIN,
                    "exposure_removed": n_raw > len(mem),
                    "contains_rt_genes": bool(set(mem.tolist()) & set(int(g) for g in rt_idx))})
    add("P53PROG_UP", "p53 program (data)", B_["P"], "P = program of S2")
    for f, pf in enumerate(B_["Pf"]):
        add(f"P53PROG_UP_f{f}", "p53 program (data)", pf, f"P_-{f}: cross-fitted program used for fold {f}")
    if len(B_["PnoX"]):
        add("P53PROG_UP_noX", "p53 program (data)", B_["PnoX"], "P of S2 without the exposure-moving drug-doses")
    if len(B_["P"]) > CORE_N:
        add("P53PROG_UP_core", "p53 program (data)", B_["P"][:CORE_N], f"top {CORE_N} of P by z")
    add("P53PROG_DOWN", "p53 program (data)", B_["Pd"], "P-down = WT-selective repression across S2")
    for f, pf in enumerate(B_["Pdf"]):
        add(f"P53PROG_DOWN_f{f}", "p53 program (data)", pf, f"P-down_-{f}")
    for nm in sorted(atlas_progs):
        add(f"PROG_{nm}", "program (atlas angle_programs)", atlas_progs[nm], "tahoe_atlas.angle_programs")
    for nm, (syms, src) in overlays.items():
        add(nm, "overlay", [sym2idx[s] for s in syms if s in sym2idx], src)
    for r in reg:
        if not r["tested_as_set"]:
            ck.add(f"set not tested as a set (< {A.MODULE_MIN} genes after removing the exposure): {r['name']}", r["n"],
                   r["n_raw"], r["source"])
        if r["contains_rt_genes"]:
            ck.add(f"set contains readthrough-covariate genes: {r['name']}", r["n"], note=r["source"])
    return reg


def pc_loadings(fx):
    """Gene loadings of the top 3 genome-wide components (tahoe_atlas FX.svd: atlas W2 of the drug wells, standardised
    per gene) and that standardisation (mean, SD per gene)."""
    X = np.nan_to_num(np.asarray(fx.W2, dtype=np.float64)[fx.drug_w][:, fx.gi])
    mu, sd = X.mean(axis=0), X.std(axis=0)
    sd[sd == 0] = 1.0
    del X
    _X, U, _S, _Vt = fx.svd()
    U3 = np.array(U[:, :3])
    fx._svd = None
    return U3, mu, sd


def scores_pass(T, grid, sets, bg, U3, mu, sd, chunk, cpath):
    """One pass over the whole tensor after (B): per (well, line) the mean r2 over each set's genes, resp_bg = mean |r2|
    over the genes outside every data-derived program and the exposure (bg), the scores on the top-3 genome-wide
    components (sum_g U_gj (r2 - mu_g)/sd_g / sum_g U_gj^2 over the finite genes) and the finite cells (a check of the
    build); everything then as drug-dose means over the used wells."""
    z = load_npz(cpath)
    if z is not None:
        log(f"program scores: cache {os.path.basename(cpath)}")
        return z
    t0 = time.time()
    G, NWL = T.G, T.NW * T.L
    M = np.zeros((G, len(sets)))
    for j, s in enumerate(sets):
        M[np.asarray(s, dtype=np.int64), j] = 1.0
    S, N = np.zeros((len(sets), NWL)), np.zeros((len(sets), NWL))
    bS, bN = np.zeros(NWL), np.zeros(NWL)
    pS, pN = np.zeros((3, NWL)), np.zeros((3, NWL))
    nfin = 0
    bgf = bg.astype(np.float64)
    for g0 in range(0, G, chunk):
        g1 = min(G, g0 + chunk)
        blk = T.read(g0, g1).reshape(g1 - g0, NWL).astype(np.float64)
        f = np.isfinite(blk)
        b0 = np.where(f, blk, 0.0)
        ff = f.astype(np.float64)
        S += M[g0:g1].T @ b0
        N += M[g0:g1].T @ ff
        bS += bgf[g0:g1] @ np.abs(b0)
        bN += bgf[g0:g1] @ ff
        zst = np.where(f, (blk - mu[g0:g1, None]) / sd[g0:g1, None], 0.0)
        pS += U3[g0:g1].T @ zst
        pN += (U3[g0:g1] ** 2).T @ ff
        nfin += int(f.sum())
    with quiet():
        Wl = np.where(N > 0, S / N, np.nan).reshape(len(sets), T.NW, T.L)
        rb = np.where(bN > 0, bS / bN, np.nan).reshape(T.NW, T.L)
        pc = np.where(pN > 0, pS / pN, np.nan).reshape(3, T.NW, T.L)
    res = {"sets": np.stack([TW.Grid.dd_mean(grid.B, Wl[j]) for j in range(len(sets))]) if len(sets) else
           np.zeros((0, grid.nd, T.L)), "resp_bg": TW.Grid.dd_mean(grid.B, rb),
           "pcs": np.stack([TW.Grid.dd_mean(grid.B, pc[j]) for j in range(3)]), "nfin": np.int64(nfin)}
    save_npz(cpath, **res)
    log(f"program scores pass: {len(sets)} sets, resp_bg over {int(bg.sum())} genes, 3 components "
        f"({time.time() - t0:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")
    return res


# ============================================================================= (C) the genome-wide screen
def choose_placebos(gdf, p1, ddz, keep, x_idx, excluded, n_per_family, nd, n_lab):
    """Placebo exposures, chosen before any fit and without looking at any outcome. Candidates: atlas genes outside
    every data-derived gene set of the step (the p53 programs and the atlas programs; the curated overlays do not
    shape the pool), not the exposure, not the readthrough covariates. Two families by the nearest standardised
    (Euclidean) distance to the exposure:
    'expression' (log2 median line CPM, lines expressing, share of finite drug-dose x line cells) and 'response'
    (share of keep drug-doses with atlas |DD_z| >= 3, SD of the r2 left after the drug-dose x TP53-group and line FE,
    lines expressing): TRIM72 rises after strong cytotoxic drugs, and only genes that move as much within lines can
    show whether it is special. Ties broken by symbol."""
    with quiet():
        feats = {"log2_median_line_cpm": np.log2(gdf["median_line_cpm"].to_numpy(float) + 0.1),
                 "n_lines_expressing": gdf["n_lines_expressing"].to_numpy(float),
                 "frac_finite_cells": p1["nres"] / float(nd * n_lab),
                 "frac_keep_dd_absz_ge3": np.nanmean(np.abs(ddz[keep]) >= 3, axis=0),
                 "resid_sd_after_fe": p1["rsd"]}
    fam = {"expression": ["log2_median_line_cpm", "n_lines_expressing", "frac_finite_cells"],
           "response": ["frac_keep_dd_absz_ge3", "resid_sd_after_fe", "n_lines_expressing"]}
    G = len(gdf)
    cand = np.ones(G, bool)
    cand[list(excluded)] = False
    cand[x_idx] = False
    rows = []
    for fname, cols in fam.items():
        F = np.column_stack([feats[c] for c in cols])
        ok = cand & np.isfinite(F).all(axis=1)
        sdv = np.nanstd(F, axis=0)
        sdv[~(sdv > 0)] = 1.0
        d = np.sqrt((((F - F[x_idx]) / sdv) ** 2).sum(axis=1))
        idx = np.flatnonzero(ok)
        o = idx[np.lexsort((gdf["symbol"].to_numpy()[idx].astype(str), d[idx]))][:n_per_family]
        for r, g in enumerate(o):
            rows.append({"family": fname, "rank": r + 1, "idx": int(g), "symbol": gdf.at[g, "symbol"], "distance": d[g]}
                        | {c: feats[c][g] for c in feats})
    out = pd.DataFrame(rows)
    ex = {"family": "exposure", "rank": 0, "idx": int(x_idx), "symbol": gdf.at[x_idx, "symbol"], "distance": 0.0}
    return pd.concat([pd.DataFrame([ex | {c: feats[c][x_idx] for c in feats}]), out], ignore_index=True)


def xperm_arrays(x, dom, wt, n, rng):
    """n copies of the exposure, each shuffled across lines within every drug-dose x TP53-group cell over the cells of
    dom (finite exposure and covariates; two_way's within_dd_perm cells): the same shuffles serve every gene, and the
    occupancy of every gene stays the same (x stays finite exactly on dom)."""
    out = np.full((n,) + x.shape, np.nan)
    for b in range(n):
        xp = np.where(dom, x, np.nan)
        for d in range(x.shape[0]):
            for grp in (wt, ~wt):
                pos = np.flatnonzero(dom[d] & grp)
                if len(pos) > 1:
                    xp[d, pos] = x[d, rng.permutation(pos)]
        out[b] = xp
    return out


_SH = {}             # the shared screen data of this process (set by screen_init)


def screen_init(shared):
    _SH.clear()
    _SH.update(shared)


MAIN_KEYS = ["n_rows", "n_lines_WT", "n_lines_alt", "n_drugdoses", "n_drugs", "df", "b_WT", "b_alt", "diff",
             "b_common", "se_WT", "se_alt", "se_diff", "se_common", "se_diff_drug", "se_common_drug", "t_WT", "t_alt",
             "t_diff", "t_common", "p_WT", "p_alt", "p_diff", "p_common", "tested", "sd_x_resid"]
CS_KEYS = ["b_common", "diff", "t_common", "t_diff", "p_common", "p_diff", "tested"]


def camera_vectors(sc, ok):
    """Normalised cluster-score vectors of the genes ok: compound and line versions (u / ||u||), the two-way version
    (u / s, s^2 = ||u_drug||^2 + ||u_line||^2 - ||u_inter||^2; only where s^2 > 0) and the genes with s^2 <= 0."""
    ud, ul, ui = sc["drug"], sc["line"], sc["inter"].reshape(sc["inter"].shape[0], -1)
    nd_, nl_, ni_ = (np.sqrt((u ** 2).sum(axis=1)) for u in (ud, ul, ui))
    s2 = nd_ ** 2 + nl_ ** 2 - ni_ ** 2
    good = ok & (s2 > 0)
    with quiet():
        out = {"d": np.where(ok[:, None], ud / nd_[:, None], 0.0), "l": np.where(ok[:, None], ul / nl_[:, None], 0.0),
               "twd": np.where(good[:, None], ud / np.sqrt(np.where(good, s2, 1.0))[:, None], 0.0),
               "twl": np.where(good[:, None], ul / np.sqrt(np.where(good, s2, 1.0))[:, None], 0.0),
               "twi": np.where(good[:, None], ui / np.sqrt(np.where(good, s2, 1.0))[:, None], 0.0)}
    for k_ in out:
        out[k_] = np.nan_to_num(out[k_])
    return out, ok & ~(s2 > 0)


def screen_job(job):
    """One gene chunk (a worker job): the main fit (covariate set gw, true labels, exposure) with its cluster scores,
    the covariate-set sensitivities, the exposure shuffles (same occupancy, fitted together), the TP53 relabellings
    and the placebo exposures. Writes cache/screen/<key>/chunk_NNNNN.npz (per-gene arrays and the chunk's sums of
    normalised score vectors); an existing file is kept (resume)."""
    ci, g0, g1 = job
    sh = _SH
    path = os.path.join(sh["sdir"], f"chunk_{ci:05d}.npz")
    if os.path.exists(path):
        return ci, float("nan")
    tp, off, shape = sh["tensor"]
    m = g1 - g0
    mm = np.memmap(tp, np.float32, "r", offset=off + g0 * shape[1] * shape[2] * 4, shape=(m, shape[1], shape[2]))
    blk = np.array(mm)
    del mm
    Y = np.ascontiguousarray(dd_level(blk, sh["B"])[:, sh["order"]])
    del blk
    finY = np.isfinite(Y)
    wt, use, st = sh["wt"], sh["use"], sh["starts"]
    x = sh["x"]
    res = {}
    for cs, C in sh["covs"].items():
        ok = finY & sh["dom"][cs][None]
        r = fit_chunk(Y, x[None], C, ok, wt, use, st, want_scores=(cs == "gw"))
        if cs == "gw":
            for k_ in MAIN_KEYS:
                res[f"main_{k_}"] = np.asarray(r[k_][0])
            tested_c = r["tested"][0].copy()
            if g0 <= sh["x_idx"] < g1:
                tested_c[sh["x_idx"] - g0] = False                  # the exposure itself is never an outcome
            for est in ("diff", "common"):
                vec, bad = camera_vectors(r["scores"][est], tested_c)
                for k_, v in vec.items():
                    res[f"cam_{est}_{k_}"] = v.sum(axis=0)
                res[f"cam_{est}_nbad"] = np.int64(bad.sum())
            res["cam_n"] = np.int64(tested_c.sum())
            nxp = sh["xperm"].shape[0]
            tc, td, tt = (np.full((nxp, m), np.nan, np.float32), np.full((nxp, m), np.nan, np.float32),
                          np.zeros((nxp, m), bool))
            for b0 in range(0, nxp, XPERM_BATCH):
                rr = fit_chunk(Y, sh["xperm"][b0:b0 + XPERM_BATCH], C, ok, wt, use, st)
                tc[b0:b0 + XPERM_BATCH], td[b0:b0 + XPERM_BATCH] = rr["t_common"], rr["t_diff"]
                tt[b0:b0 + XPERM_BATCH] = rr["tested"]
            res.update(xp_t_common=tc, xp_t_diff=td, xp_tested=tt)
            nrl = sh["relabel"].shape[0]
            td, tt = np.full((nrl, m), np.nan, np.float32), np.zeros((nrl, m), bool)
            for b in range(nrl):
                rr = fit_chunk(Y, x[None], C, ok, sh["relabel"][b], use, st)
                td[b], tt[b] = rr["t_diff"][0], rr["tested"][0]
            res.update(rl_t_diff=td, rl_tested=tt)
        else:
            for k_ in CS_KEYS:
                res[f"cs_{cs}_{k_}"] = np.asarray(r[k_][0])
    npl = sh["plac"].shape[0]
    tc, td, tt = np.full((npl, m), np.nan, np.float32), np.full((npl, m), np.nan, np.float32), np.zeros((npl, m), bool)
    for p in range(npl):
        okp = finY & sh["pdom"][p][None]
        rr = fit_chunk(Y, sh["plac"][p][None], sh["covs"]["gw"], okp, wt, use, st)
        tc[p], td[p], tt[p] = rr["t_common"][0], rr["t_diff"][0], rr["tested"][0]
    res.update(pl_t_common=tc, pl_t_diff=td, pl_tested=tt, peak_gb=np.float64(UT.peak_gb()))
    with open(path + ".tmp", "wb") as fh:
        np.savez(fh, **res)
    os.replace(path + ".tmp", path)
    return ci, float(res["peak_gb"])


def run_screen(shared, chunks, workers):
    """The screen over every gene chunk: in this process (--workers 1) or a spawn process pool (the repo's convention;
    each worker re-imports this step and reads its chunks from the memory-mapped tensor itself; a worker that dies,
    e.g. out of memory, stops the step with a message instead of a silent wait). Finished chunks are skipped, so an
    interrupted screen resumes; results are assembled in chunk order, independent of worker timing."""
    sdir = shared["sdir"]
    todo = [c for c in chunks if not os.path.exists(os.path.join(sdir, f"chunk_{c[0]:05d}.npz"))]
    log(f"(C) screen: {len(chunks)} gene chunks ({len(chunks) - len(todo)} done earlier), {workers} worker(s); "
        f"per chunk {len(shared['covs'])} covariate sets, {shared['xperm'].shape[0]} exposure shuffles, "
        f"{shared['relabel'].shape[0]} TP53 relabellings, {shared['plac'].shape[0]} placebo exposures")
    t0 = time.time()
    peaks = []
    step = max(1, len(todo) // 10)
    if workers <= 1 or len(todo) <= 1:
        screen_init(shared)
        for i, job in enumerate(todo):
            peaks.append(screen_job(job)[1])
            if (i + 1) % step == 0 or i + 1 == len(todo):
                log(f"  screen: {i + 1}/{len(todo)} chunks ({time.time() - t0:.0f} s; peak RSS {UT.peak_gb():.2f} GB)")
    else:
        with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn"), initializer=screen_init,
                                 initargs=(shared,)) as ex:
            try:
                futs = [ex.submit(screen_job, job) for job in todo]
                for i, fu in enumerate(as_completed(futs)):
                    peaks.append(fu.result()[1])
                    if (i + 1) % step == 0 or i + 1 == len(todo):
                        log(f"  screen: {i + 1}/{len(todo)} chunks ({time.time() - t0:.0f} s; worker peak RSS "
                            f"{np.nanmax(peaks):.2f} GB)")
            except BrokenProcessPool:
                sys.exit("(C) screen: a worker process died (out of memory?). The finished gene chunks are kept: rerun "
                         "to resume, with --workers 1 if memory is short.")
    return float(np.nanmax(peaks)) if peaks and np.isfinite(peaks).any() else float("nan")


def assemble(sdir, chunks):
    """Per-gene arrays of every chunk, in chunk order (1-D: genes; 2-D: replicate x genes), and the summed camera
    vectors. Each file is closed after it is read (261 chunk files on the real data; macOS allows 256 open files)."""
    parts = []
    for ci, _g0, _g1 in chunks:
        with np.load(os.path.join(sdir, f"chunk_{ci:05d}.npz"), allow_pickle=False) as z:
            parts.append({k_: z[k_] for k_ in z.files})
    out = {}
    for k_ in parts[0]:
        if k_.startswith("cam_") or k_ == "peak_gb":
            out[k_] = np.sum([p[k_] for p in parts], axis=0)
        elif parts[0][k_].ndim == 1:
            out[k_] = np.concatenate([p[k_] for p in parts])
        else:
            out[k_] = np.concatenate([p[k_] for p in parts], axis=1)
    out["worker_peak_gb"] = float(np.nanmax([float(p["peak_gb"]) for p in parts]))
    return out


def gw_count(t, tested, df):
    """Genome-wide count at q < 0.1 (BH over the tested genes, p from the two-way t with the gene's df) and the
    inflation lambda = median(t^2) / 0.4549."""
    t = np.asarray(t, float)
    ok = tested & np.isfinite(t) & (df > 0)
    if not ok.any():
        return 0, np.nan
    p = 2 * stats.t.sf(np.abs(t[ok]), df[ok])
    return int((bh(p) < Q_REP).sum()), float(np.median(t[ok] ** 2) / LAMBDA_NULL)


def pooled_null_p(t_obs, tested, t_null, tested_null):
    """Pooled empirical p of |t| against every (replicate, gene) of a null that keeps the gene-gene correlation."""
    nul = np.sort(np.abs(t_null[tested_null & np.isfinite(t_null)]).astype(float))
    p = np.full(len(t_obs), np.nan)
    ok = tested & np.isfinite(t_obs)
    if len(nul):
        p[ok] = (1 + len(nul) - np.searchsorted(nul, np.abs(t_obs[ok]) - 1e-12, side="left")) / (1 + len(nul))
    return p


def camera_test(t, tested, mem, sums_S, sums_all, nbad_all, null=None):
    """two_way.set_test at genome scale: statistic = mean t of the set's tested genes minus mean t of all other tested
    genes; variance = pooled within-set variance of t x a'Ra, R = correlation between the genes' estimates from their
    cluster scores (compound, line and two-way versions; a'Ra = ||sum_g a_g u_g / ||u_g||||^2 from projections summed
    over genes, so no gene x gene matrix is formed), the largest used, never below independence 1/m1 + 1/m2; the
    two-way version is skipped when any gene has s^2 <= 0 (as two_way). t with m1 + m2 - 2 df. With null = (t, tested)
    replicates (the TP53 relabellings, for diff), the same statistic per replicate -> calibrated p ((statistic - null
    mean) / null SD against t with replicates - 1 df, as the SD comes from few replicates). The within-cell exposure
    shuffles are not used as such a null: they break the exposure's line-level structure, which the set statistic,
    unlike a gene's studentised t, does not account for, so they make it anti-conservative."""
    inS = np.zeros(len(t), bool)
    inS[np.asarray(mem, dtype=np.int64)] = True
    inS &= tested & np.isfinite(t)
    rest = tested & np.isfinite(t) & ~inS
    m1, m2 = int(inS.sum()), int(rest.sum())
    if m1 < A.MODULE_MIN or m2 < 2:
        return None
    q0 = 1.0 / m1 + 1.0 / m2
    qs = {}
    for c, keys in (("drug", ("d",)), ("line", ("l",)), ("twoway", ("twd", "twl", "twi"))):
        if c == "twoway" and nbad_all > 0:
            continue
        v = [sums_S[k_] / m1 - (sums_all[k_] - sums_S[k_]) / m2 for k_ in keys]
        qs[c] = float((v[0] ** 2).sum()) if c != "twoway" else float((v[0] ** 2).sum() + (v[1] ** 2).sum()
                                                                      - (v[2] ** 2).sum())
    q = max([q0] + list(qs.values()))
    src = "independence (floor)" if q == q0 else max(qs, key=qs.get)
    a, b = t[inS], t[rest]
    s2 = (((a - a.mean()) ** 2).sum() + ((b - b.mean()) ** 2).sum()) / (m1 + m2 - 2)
    stat = float(a.mean() - b.mean())
    se = float(np.sqrt(s2 * q))
    out = {"m1": m1, "m2": m2, "mean_t_set": float(a.mean()), "mean_t_rest": float(b.mean()), "stat": stat, "se": se,
           "t": stat / se, "df": m1 + m2 - 2, "p_set_camera": float(2 * stats.t.sf(abs(stat / se), m1 + m2 - 2)),
           "p_set_independent": float(2 * stats.t.sf(abs(stat) / np.sqrt(s2 * q0), m1 + m2 - 2)),
           "vif_effective": q / q0, "vif_from": src, "vif_drug": qs.get("drug", np.nan) / q0,
           "vif_line": qs.get("line", np.nan) / q0, "vif_twoway": qs.get("twoway", np.nan) / q0,
           "twoway_skipped_genes_s2_le_0": int(nbad_all)}
    if null is not None:
        tn, okn = null
        sn = []
        for b_ in range(tn.shape[0]):
            ia, ib = inS & okn[b_] & np.isfinite(tn[b_]), rest & okn[b_] & np.isfinite(tn[b_])
            if ia.sum() >= 2 and ib.sum() >= 2:
                sn.append(float(tn[b_][ia].mean() - tn[b_][ib].mean()))
        sn = np.array(sn)
        if len(sn) >= 2 and sn.std(ddof=1) > 0:
            zc = (stat - sn.mean()) / sn.std(ddof=1)
            out.update({"n_null": len(sn), "null_mean": float(sn.mean()), "null_sd": float(sn.std(ddof=1)),
                        "z_null_calibrated": float(zc),
                        "p_null_calibrated": float(2 * stats.t.sf(abs(zc), len(sn) - 1)),   # SD from few replicates
                        "p_null_empirical": TW.perm_p(stat - sn.mean(), sn - sn.mean())})
    return out


def members_pass(T, grid, order, shared, sets, tested, chunk):
    """The cluster-score vectors of each set's tested genes, summed per set: one more main fit (gw, true labels) over
    the union of the sets' genes only (the chunk files keep only the genome-wide sums)."""
    genes = np.array(sorted(set(int(g) for s in sets for g in s) & set(np.flatnonzero(tested).tolist())), np.int64)
    pos = {g: i for i, g in enumerate(genes)}
    M = np.zeros((len(genes), len(sets)))
    for j, s in enumerate(sets):
        ii = [pos[int(g)] for g in s if int(g) in pos]
        M[ii, j] = 1.0
    sums = {est: {} for est in ("diff", "common")}
    nbad = {est: np.zeros(len(sets), int) for est in ("diff", "common")}
    C = shared["covs"]["gw"]
    for c0 in range(0, len(genes), chunk):
        ii = genes[c0:c0 + chunk]
        Y = np.ascontiguousarray(dd_level(T.take(ii), grid.B)[:, order])
        ok = np.isfinite(Y) & shared["dom"]["gw"][None]
        r = fit_chunk(Y, shared["x"][None], C, ok, shared["wt"], shared["use"], shared["starts"], want_scores=True)
        okg = r["tested"][0] & tested[ii]
        for est in ("diff", "common"):
            vec, bad = camera_vectors(r["scores"][est], okg)
            for k_, v in vec.items():
                sums[est][k_] = sums[est].get(k_, 0.0) + M[c0:c0 + chunk].T @ v
            nbad[est] += (M[c0:c0 + chunk].T @ bad.astype(float)).astype(int)
    return sums, nbad


# ============================================================================= program-level models, placebos, (D)
def program_models(tabs, grid, wt, plan, rng, covsets):
    """two_way's D1 machinery on program-level outcomes, nothing new: two_way.run_models (one Design per occupancy;
    the outcomes of a design share its within-cell and TP53-label permutations; two_way.fit's columns). plan: dicts with
    outcome, fe, covset, variant, ddmask, role, family, B_within, B_label. This step's covariate sets are added to
    two_way.COVSETS for the call only."""
    specs = [{"family": p["family"], "module": p["role"], "readout": p["outcome"], "variant": p["variant"],
              "covset": p["covset"], "fe": p["fe"], "xname": "exposure_r2", "tabs": "main", "X": tabs["x"],
              "ddmask": p["ddmask"], "B_within": p["B_within"], "B_label": p["B_label"]} for p in plan]
    saved = dict(TW.COVSETS)
    TW.COVSETS.update(covsets)
    try:
        res, _sl = TW.run_models(specs, {"main": tabs}, grid, wt, rng)
    finally:
        TW.COVSETS.clear()
        TW.COVSETS.update(saved)
    res.insert(0, "role", [p["role"] for p in plan])
    return res


def placebo_program_models(tabs, grid, wt, outcome, covs, X_list, info_rows):
    """The primary program-level model (ddxg, gw, all drug-doses; TW.Design + TW.fit, no permutations) with each placebo
    gene's r2 as the exposure."""
    rows = []
    Y = tabs[outcome]
    for Xp, info_ in zip(X_list, info_rows):
        ok = np.isfinite(Xp) & np.isfinite(Y)
        for c in covs:
            ok &= np.isfinite(tabs[c])
        des = TW.Design(ok, Xp, [tabs[c] for c in covs], wt, grid.drug_id, "ddxg")
        o, _ = TW.fit(des, Y[des.d, des.l].astype(float))
        rows.append(info_ | {"n_rows": o["n_rows"], "b_WT": o["b_WT"], "b_alt": o["b_alt"], "diff": o["diff"],
                             "se_diff_twoway": o["se_diff_twoway"], "t_diff": o["diff"] / o["se_diff_twoway"],
                             "p_diff_twoway": o["p_diff_twoway"], "b_common": o["b_common"],
                             "se_common_twoway": o["se_common_twoway"],
                             "t_common": o["b_common"] / o["se_common_twoway"],
                             "p_common_twoway": o["p_common_twoway"]})
    return pd.DataFrame(rows)


def placebo_compare(obs_t, plac_t):
    """Where the exposure's t sits among the placebos': fraction of placebo t below it, and the two-sided empirical p
    (1 + #|t_placebo| >= |t|) / (n + 1)."""
    v = np.asarray(plac_t, float)
    v = v[np.isfinite(v)]
    if not len(v) or not np.isfinite(obs_t):
        return np.nan, np.nan, 0
    return float((v < obs_t).mean()), float((1 + (np.abs(v) >= abs(obs_t) - 1e-12).sum()) / (len(v) + 1)), len(v)


def corr_rows(V, x):
    """Pearson r of each row of V with x over the positions where both are finite."""
    f = np.isfinite(V) & np.isfinite(x)[None]
    n = f.sum(axis=1)
    Vz, xz = np.where(f, V, 0.0), np.where(f, x[None], 0.0)
    with quiet():
        mv, mx = Vz.sum(1) / n, xz.sum(1) / n
        cov = (Vz * xz).sum(1) / n - mv * mx
        vv = (Vz ** 2).sum(1) / n - mv ** 2
        vx = (xz ** 2).sum(1) / n - mx ** 2
        return np.where(n >= 10, cov / np.sqrt(vv * vx), np.nan)


def across_dd(fx, keep, ddz_x, scores, B, rng):
    """(D1) Each set's drug-dose score (score_z) vs the exposure's atlas DD_z over the keep drug-doses: Pearson r, with a
    drug-block permutation null (upstream_tf.drug_block_perms: whole compounds swapped among compounds with the same
    doses) -> calibrated normal p (r / null SD)."""
    ddk = fx.dd[keep].reset_index(drop=True)
    perms = UT.drug_block_perms(ddk, B, rng)
    x = ddz_x[keep]
    out = {}
    for nm, sz in scores.items():
        v = np.asarray(sz, float)[keep]
        r = float(corr_rows(v[None], x)[0])
        nul = corr_rows(v[perms], x)
        sdn = float(np.nanstd(nul, ddof=1))
        out[nm] = {"r_across_dd": r, "n_dd": int((np.isfinite(v) & np.isfinite(x)).sum()), "null_sd": sdn,
                   "z_across_dd": r / sdn if sdn > 0 else np.nan,
                   "p_across_dd": float(2 * stats.norm.sf(abs(r / sdn))) if sdn > 0 else np.nan, "n_perm": B}
    return out


def engine_check(T, grid, order, shared, genes, covs, wt):
    """checks.csv: fit_chunk vs two_way.Design + many_diffs + fit (fe ddxg, covariate set gw) for some real genes:
    the largest relative difference of b_WT, b_alt, diff, b_common, se_diff and se_common, and n_rows equal."""
    inv = np.empty_like(order)
    inv[order] = np.arange(len(order))
    Yd = dd_level(T.take(genes), grid.B)                                  # grid order
    Ys = np.ascontiguousarray(Yd[:, order])
    ok = np.isfinite(Ys) & shared["dom"]["gw"][None]
    r = fit_chunk(Ys, shared["x"][None], shared["covs"]["gw"], ok, shared["wt"], shared["use"], shared["starts"])
    worst, nr = {}, 0
    xg = shared["x"][inv]
    for j in range(len(genes)):
        okg = np.isfinite(Yd[j]) & np.isfinite(xg)
        for c in covs:
            okg &= np.isfinite(c)
        des = TW.Design(okg, xg, covs, wt, grid.drug_id, "ddxg")
        y = Yd[j][des.d, des.l]
        o, _ = TW.many_diffs(des, y[:, None])
        f, _ = TW.fit(des, y)
        nr += int(des.n != r["n_rows"][0][j])
        for k_, ref in (("b_WT", o["b_WT"][0]), ("b_alt", o["b_alt"][0]), ("diff", o["diff"][0]),
                        ("b_common", f["b_common"]), ("se_diff", f["se_diff_twoway"]),
                        ("se_common", f["se_common_twoway"])):
            v = r[k_][0][j]
            if np.isfinite(ref) or np.isfinite(v):
                worst[k_] = max(worst.get(k_, 0.0), abs(v - ref) / max(1e-12, abs(ref)))
    return worst, nr


def sibling_annotations(sib, exposure, gdf, ck):
    """Annotations from sibling steps' tables, if present under the same output folder (never fetched): the
    readthrough-geometry class (upstream_coregulation c_DoG), the across-drug-dose correlation with TRIM72 (raw and 3
    PCs removed; a_coreg_genomewide), and the TRIM72 +- 200 kb locus (upstream_tf's Ensembl file or its built-in list).
    The coregulation and locus columns describe TRIM72 and are left empty for another exposure."""
    ann = pd.DataFrame(index=gdf["symbol"].astype(str))

    def dog():
        p = os.path.join(sib, "upstream_coregulation", "tables", "c_DoG_gene_exposure_classes.csv")
        if not os.path.exists(p):
            ck.add("annotation: readthrough-geometry class", np.nan, note=f"{os.path.relpath(p, sib)} (next to this "
                   "step's folder) not present")
            return
        t = pd.read_csv(p, usecols=["symbol", "class"]).drop_duplicates("symbol").set_index("symbol")
        ann["dog_class"] = t["class"].reindex(ann.index).to_numpy()
    optional("annotation: c_DoG_gene_exposure_classes", dog, ck)
    if exposure != "TRIM72":
        return ann

    def coreg():
        p = os.path.join(sib, "upstream_coregulation", "tables", "a_coreg_genomewide.csv")
        if not os.path.exists(p):
            ck.add("annotation: across-drug-dose co-regulation with TRIM72", np.nan, note=f"{os.path.relpath(p, sib)} "
                   "(next to this step's folder) not present")
            return
        t = pd.read_csv(p, usecols=["gene", "r_z_raw", "r_z_minus_3pc"]).drop_duplicates("gene").set_index("gene")
        ann["coreg_r_across_dd_raw"] = t["r_z_raw"].reindex(ann.index).to_numpy()
        ann["coreg_r_across_dd_minus_3pc"] = t["r_z_minus_3pc"].reindex(ann.index).to_numpy()
    optional("annotation: a_coreg_genomewide", coreg, ck)

    def locus():
        ids, src = UT.locus_genes(os.path.join(sib, "upstream_tf", "cache", "external"))
        names = {n for n in ids.values() if n}
        ann["in_TRIM72_locus_200kb"] = ann.index.isin(names)
        ck.add("annotation: TRIM72 +- 200 kb locus genes", len(names), note=src)
    optional("annotation: TRIM72 locus", locus, ck)
    return ann


# ============================================================================= tables of (B)
def b_tables(B_, grid, fx, gdf, x_idx, ddz_x, UFt, sib, data, sym2idx, overlays):
    """b_drugdose_p53_activation.csv, b_p53_program_genes.csv.gz, b_p53_program.csv, b_program_stability.csv,
    b_feature_specificity.csv (frames)."""
    dd = grid.dd
    nd, G = grid.nd, len(gdf)
    fnames, fsizes, fsame, _UF = UFt
    nfp = 1 + N_FEAT_PERM
    # specificity: per checked drug-dose, every grouping's calibrated divergence vs TP53's (same 20-permutation scale)
    frows, fsum = [], {}
    for scope, Df, fdd in (("S1", B_.get("D_feat1"), B_["fdd1"]), ("S2", B_.get("D_feat2"), B_["fdd2"])):
        if Df is None:
            continue
        for j, d in enumerate(fdd):
            zf = np.array([float(calib(Df[j, i * nfp], Df[j, i * nfp + 1:(i + 1) * nfp])) for i in range(len(fnames))])
            ztp = float(B_["zD20"][d])
            for i, nm in enumerate(fnames):
                frows.append({"scope": f"drug-dose ({scope})", "drugdose_row": int(d), "drug": dd.at[d, "drug"],
                              "conc": dd.at[d, "conc"], "grouping": nm, "n_lines_in_group": fsizes[i],
                              "same_as_tp53_split": fsame[i], "z_divergence": zf[i], "z_divergence_TP53_20perm": ztp})
            oth = np.array([not s for s in fsame])
            if oth.any() and np.isfinite(zf[oth]).any():
                jb = np.flatnonzero(oth)[np.nanargmax(zf[oth])]
                fsum[int(d)] = {"z_divergence_TP53_20perm": ztp, "best_other_grouping": fnames[jb],
                                "best_other_grouping_z": zf[jb],
                                "n_groupings_above_TP53": int(np.nansum(zf[oth] > ztp)),
                                "TP53_explains_best": bool(ztp >= np.nanmax(zf[oth]))}
    if "sel_tp53" in B_:
        for i, nm in enumerate(fnames):
            frows.append({"scope": "program P (selectivity over S2)", "grouping": nm, "n_lines_in_group": fsizes[i],
                          "same_as_tp53_split": fsame[i], "z_divergence": B_["sel_feat"][i],
                          "z_divergence_TP53_20perm": B_["sel_tp53"]})
    FS = pd.DataFrame(frows)
    # per drug-dose
    keep = B_["keep"]
    D = dd[["drug", "conc", "plates", "n_wells"]].copy()
    D.insert(0, "drugdose_row", np.arange(nd))
    D["moa_fine"] = fx.dd["moa_fine"].to_numpy()
    D["keep"] = keep
    D["divergence_D"] = B_["D0"]
    D["zD"], D["pD"], D["qD"] = B_["zD"], B_["pD"], B_["qD"]
    D["in_S1"] = np.isin(np.arange(nd), B_["S1"])
    D["fold"] = B_["fold"]
    D["oof_signature"] = B_["oof_how"]
    D["s_oof_program_contrast"] = B_["s_oof"]
    D["zs_oof"], D["ps_oof"], D["qs_oof"] = B_["zs_oof"], B_["ps_oof"], B_["qs_oof"]
    D["in_S2_p53_activating"] = np.isin(np.arange(nd), B_["S2"])
    for f, Sf in enumerate(B_["S2f"]):
        D[f"in_S2_minus_fold{f}"] = np.isin(np.arange(nd), Sf)
    P = B_["P"]
    with quiet():
        D["program_P_delta_log2"] = np.nanmean(B_["d0"][P], axis=0) if len(P) else np.nan
    D["exposure_DD_z"] = ddz_x
    D["exposure_moving_absz_ge3"] = B_["X"]
    for c in ("z_divergence_TP53_20perm", "best_other_grouping", "best_other_grouping_z", "n_groupings_above_TP53",
              "TP53_explains_best"):
        D[c] = [fsum.get(i, {}).get(c, np.nan) for i in range(nd)]
    try:
        ps = pd.read_csv(os.path.join(data, "gene_panel", "results", "pathway_scores_by_dose.csv"))
        ps = ps.loc[ps["score"] == "P53_ACTIVITY", ["drug", "conc", "z"]].assign(ck=lambda t: t["conc"].round(6))
        m = D.assign(ck=D["conc"].round(6)).merge(ps.drop_duplicates(["drug", "ck"])[["drug", "ck", "z"]],
                                                  on=["drug", "ck"], how="left")
        D["overlay_panel_P53_ACTIVITY_z"] = m["z"].to_numpy()
    except (OSError, KeyError, ValueError):
        D["overlay_panel_P53_ACTIVITY_z"] = np.nan
    p2 = os.path.join(sib, "two_way", "tables", "drugdose_sets.csv")
    if os.path.exists(p2):
        t = pd.read_csv(p2)
        m = D.assign(ck=D["conc"].round(6)).merge(t.assign(ck=t["conc"].round(6)).drop_duplicates(["drug", "ck"])[
            ["drug", "ck", "in_ii_p53", "in_ii_active"]], on=["drug", "ck"], how="left")
        D["overlay_two_way_in_ii_p53"], D["overlay_two_way_in_ii_active"] = m["in_ii_p53"].to_numpy(), \
            m["in_ii_active"].to_numpy()
    # per gene
    sym = gdf["symbol"].astype(str).to_numpy()
    Gt = pd.DataFrame({"idx": np.arange(G), "symbol": sym, "median_line_cpm": gdf["median_line_cpm"],
                       "n_lines_expressing": gdf["n_lines_expressing"]})
    st = B_["st2"]
    Gt["z_S1_stage1"] = B_["zm1"]
    Gt["z_program"], Gt["m_drug_equal_z"] = B_["zm"], B_["m0"]
    Gt["p_up"], Gt["q_up"], Gt["p_down"], Gt["q_down"] = B_["p_up"], B_["q_up"], B_["p_dn"], B_["q_dn"]
    Gt["wt_minus_alt_log2"], Gt["wt_mean_log2"] = st["dbar"], st["wtbar"]
    Gt["frac_compounds_up"], Gt["frac_compounds_down"] = st["frac_up"], st["frac_down"]
    Gt["frac_compounds_wt_up"], Gt["frac_compounds_wt_down"] = st["frac_wt_up"], st["frac_wt_down"]
    Gt["n_compounds_with_z"] = B_["ncomp"]
    isin = lambda s: np.isin(np.arange(G), np.asarray(s, dtype=np.int64))   # noqa: E731
    Gt["in_P1_stage1"], Gt["in_P"], Gt["in_P_down"] = isin(B_["P1"]), isin(P), isin(B_["Pd"])
    for f in range(B_["F"]):
        Gt[f"in_P_minus_fold{f}"], Gt[f"in_P_down_minus_fold{f}"] = isin(B_["Pf"][f]), isin(B_["Pdf"][f])
    Gt["in_P_noX"] = isin(B_["PnoX"])
    lo = B_["loco"]
    Gt["loco_frequency"] = (np.sum([isin(v) for v in lo.values()], axis=0) / len(lo)) if lo else np.nan
    rank = np.full(G, np.nan)
    rank[P] = np.arange(1, len(P) + 1)
    Gt["rank_in_P"] = rank
    Gt["is_exposure"] = np.arange(G) == x_idx
    for nm, (syms, _src) in overlays.items():
        Gt[f"overlay_{nm}"] = np.isin(sym, syms)
    PG = Gt[Gt["in_P"] | Gt["in_P_down"]].copy()
    PG.insert(1, "program", np.where(PG["in_P"], "P (WT-selective induction)", "P-down (WT-selective repression)"))
    PG.insert(2, "program_is_fallback", np.where(PG["in_P"], bool(B_["small"]), bool(B_["small_d"])))
    PG = PG.sort_values(["program", "z_program"], ascending=[True, False])
    fsets = [set(v.tolist()) for v in B_["Pf"]], [set(v.tolist()) for v in B_["Pdf"]]
    PG["n_folds_with_gene"] = [sum(int(i) in fs for fs in fsets[0 if r_.startswith("P (") else 1])
                               for i, r_ in zip(PG["idx"], PG["program"])]
    # stability
    srows = []
    for f in range(B_["F"]):
        srows.append({"kind": "fold program", "a": f"P_minus_fold{f}", "b": "P", "value": jaccard(B_["Pf"][f], P),
                      "n": len(B_["Pf"][f]), "note": B_["fold_status"][f] + f"; training drug-doses {len(B_['S2f'][f])}"
                      f"; nested-signature fallbacks {B_['nested_fallback'][f]}"})
    for f in range(B_["F"]):
        for g in range(f + 1, B_["F"]):
            srows.append({"kind": "fold Jaccard", "a": f"P_minus_fold{f}", "b": f"P_minus_fold{g}",
                          "value": jaccard(B_["Pf"][f], B_["Pf"][g]), "n": np.nan, "note": ""})
    cn = {int(c): str(dd["drug"].to_numpy()[np.flatnonzero(grid.drug_id == c)[0]]) for c in B_["s2c"]}
    for c, v in lo.items():
        srows.append({"kind": "leave one compound out", "a": f"P without {cn[c]}", "b": "P", "value": jaccard(v, P),
                      "n": len(v), "note": ""})
    srows.append({"kind": "P without the exposure-moving drug-doses", "a": "P_noX", "b": "P",
                  "value": jaccard(B_["PnoX"], P), "n": len(B_["PnoX"]),
                  "note": f"{int(np.isin(B_['S2'], np.flatnonzero(B_['X'])).sum())} of {len(B_['S2'])} S2 drug-doses "
                          "have |DD_z(exposure)| >= 3"})
    for nm_, obs_, nul_ in (("S1", B_["n_S1_q"], B_["null_S1"]), ("S2", B_["n_S2_q"], B_["null_S2"])):
        nul_ = np.array(nul_, float)
        srows.append({"kind": f"null {nm_} sizes (each permuted labelling as the truth, same rule: permutation FDR < "
                              "0.05 against the other labellings" + ("; signatures held fixed" if nm_ == "S2" else "")
                              + ")", "a": f"{nm_} at permutation FDR < 0.05 (before any fallback)", "b": "",
                      "value": float(nul_.max()) if len(nul_) else np.nan, "n": len(nul_),
                      "note": f"observed {obs_}; max over labellings (value) {int(nul_.max()) if len(nul_) else 'NA'}, "
                              f"mean {nul_.mean() if len(nul_) else np.nan:.2f}, share non-empty "
                              f"{(nul_ > 0).mean() if len(nul_) else np.nan:.2f}; all: {[int(v) for v in nul_]}"})
    for b, n_ in enumerate(B_["null_sizes"]):
        srows.append({"kind": "null program size (permuted labelling as truth, S2 fixed, q < 0.05 by z only)",
                      "a": f"labelling {b + 1}", "b": "", "value": n_, "n": np.nan,
                      "note": f"observed with the same rule: {B_['n_obs_zonly']}"})
    for f, s_ in enumerate(B_["S2f"]):
        srows.append({"kind": "training drug-doses of P_-f", "a": f"S2_minus_fold{f}", "b": "S2",
                      "value": jaccard(s_, B_["S2"]), "n": len(s_), "note": ""})
    return D, Gt, PG, pd.DataFrame(srows), FS


def b_overlay_table(B_, gdf, overlays, x_idx, D):
    """b_overlays.csv: the curated lists against the data-derived program (role overlay): overlap with P, P-down and
    the stage-1 program, hypergeometric p, median percentile of the members' program z, each member's rank; the
    p53-activating drug-doses against the panel's P53_ACTIVITY z >= 3 and two_way's ii_p53."""
    G = len(gdf)
    sym = gdf["symbol"].astype(str).to_numpy()
    zm = B_["zm"]
    pop = np.isfinite(zm) & (np.arange(G) != x_idx)
    pct = np.full(G, np.nan)
    o = np.argsort(np.argsort(zm[pop]))
    pct[pop] = 100.0 * (o + 0.5) / pop.sum()
    rank = np.full(G, np.nan)
    rank[np.flatnonzero(pop)[np.argsort(-zm[pop], kind="stable")]] = np.arange(1, pop.sum() + 1)
    rows = []
    for nm, (syms, src) in overlays.items():
        mem = np.isin(sym, syms) & pop
        for pname, P_ in (("P", B_["P"]), ("P-down", B_["Pd"]), ("P1 (stage 1, S1)", B_["P1"])):
            inP = np.isin(np.arange(G), P_) & pop
            k_, n_, N_ = int((mem & inP).sum()), int(mem.sum()), int(pop.sum())
            rows.append({"role": "overlay", "overlay": nm, "source": src, "program": pname, "n_listed": len(syms),
                         "n_in_atlas_tested": n_, "program_size": int(inP.sum()), "n_overlap": k_,
                         "expected_overlap": n_ * inP.sum() / N_ if N_ else np.nan,
                         "p_hypergeometric_enrichment": float(stats.hypergeom.sf(k_ - 1, N_, n_, int(inP.sum())))
                         if n_ else np.nan,
                         "median_percentile_program_z": float(np.nanmedian(pct[mem])) if n_ else np.nan,
                         "members_rank_by_program_z": "; ".join(f"{s} {int(r)}" for s, r in sorted(
                             zip(sym[mem], rank[mem]), key=lambda t: t[1])) if pname == "P" else "",
                         "overlap_genes": ", ".join(sym[mem & inP])})
    S2 = D["in_S2_p53_activating"].to_numpy()
    if "overlay_panel_P53_ACTIVITY_z" in D:
        pz = D["overlay_panel_P53_ACTIVITY_z"].to_numpy(float)
        k = D["keep"].to_numpy(bool) & np.isfinite(pz)
        hi = pz >= 3
        rows.append({"role": "overlay", "overlay": "panel P53_ACTIVITY z >= 3 (pathway_scores_by_dose.csv)",
                     "program": "S2 (p53-activating drug-doses)", "n_in_atlas_tested": int((hi & k).sum()),
                     "program_size": int((S2 & k).sum()), "n_overlap": int((S2 & hi & k).sum()),
                     "spearman_zs_oof_vs_panel_z": float(stats.spearmanr(D["zs_oof"].to_numpy(float)[k], pz[k])[0])
                     if k.sum() > 5 else np.nan})
    if "overlay_two_way_in_ii_p53" in D:
        ii = D["overlay_two_way_in_ii_p53"].astype("boolean").fillna(False).to_numpy(bool)
        rows.append({"role": "overlay", "overlay": "two_way in_ii_p53 (drugdose_sets.csv)",
                     "program": "S2 (p53-activating drug-doses)", "n_in_atlas_tested": int(ii.sum()),
                     "program_size": int(S2.sum()), "n_overlap": int((S2 & ii).sum())})
    return pd.DataFrame(rows)


# ============================================================================= README and findings
README = """Tables of genome_wide.py (re-created by: python3 genome_wide.py --data <Tahoe-100M folder>; with
run_mg53_p53.py the step 'genome_wide'). Associations only: Tahoe has no MG53 perturbation and measures mRNA at 24 h.
Everything is genome-wide and data-driven at the base; curated lists (the panel's 21-gene P53_ACTIVITY,
gene_modules.csv, CollecTRI TP53 targets, the S / G2M modules) appear only as overlays (column role = overlay, set names
OVERLAY_*) or as the labelled covariate set curated_cycle, which has list-free twins (gw, gw_all, gw_pc).
'exposure' = the gene given by --exposure (TRIM72 by default; run_info.json names it); b = log2 change in the outcome
per log2 change in the exposure, both method-v3 corrected effects r2 averaged over a drug-dose's used wells.

PRIMARY TEST (first row of key_results.csv; declared in the script before any real-data run): fe ddxg (drug-dose x
TP53-group FE + line FE), all drug-doses, covariate set gw, outcome P53PROG_UP_cf, estimand b_WT - b_alt, conservative
two-way (compound, line) SE; the TP53-label permutation p is reported next to it. Everything else is secondary
(other outcomes or the common slope of the primary model), sensitivity, screen, overlay or check.

(A) Tensor (cache/r2_wl.npy, float32 genes x wells x lines; index files cache/r2_genes.csv, r2_wells.csv, r2_lines.csv,
r2_expr_mask.npy). r2 per (well, line) of every atlas gene by upstream_tf's per-plate steps (log CPM of profiles with
>= min_cells cells in the lines that express the gene -> minus the plate's drug-well median of the line -> minus the
composition shift -> minus the atlas's position effect W1 - W2; wells whose own W1 has < 5 lines -> NaN).
a_tensor_summary.csv   per plate: wells, profiles with cells, finite cells, W1 check (median over lines vs atlas W1),
                       W2 check (median over lines of r2 vs atlas W2).
a_panel_check.csv      per gene panel gene in the atlas: tensor r2 vs the panel's per (well, line) r2 (two_way's panel
                       cache, with the atlas's min_cells): cells in both, Pearson r, median / max |diff|, cells finite in
                       one only, whether the two expressed-line sets agree (the panel and the atlas decide expression by
                       different rules for a few genes).

(B) The Tahoe p53 program. Contrast z per gene x drug-dose = (mean r2 of the TP53-WT lines - mean of the altered lines)
/ (SD over the drug-dose's lines x sqrt(1/n_WT + 1/n_alt)); every permutation of the labels uses the same genes and
drug-doses. 'keep' drug-doses = not unreliable-plate-only, not position-not-correctable. Lines without a TP53 group
are left out of (B) and (C) (two_way keeps them as altered; checks.csv names them).
Selections across drug-doses use a permutation FDR: each permuted labelling is treated as the truth (its z calibrated
against the other permuted labellings), p = pooled one-sided p of the true z against all of them over the keep
drug-doses, q = BH of that p (the mean count of a permuted labelling's drug-doses above the threshold over the observed
count). It keeps the skew of the permutation null and the fact that all drug-doses share one labelling.
b_drugdose_p53_activation.csv  per drug-dose: divergence_D (log mean of the top 1% z^2 over genes, true labels), zD
                       (calibrated by the label permutations), pD (pooled permutation p), qD (permutation FDR over
                       keep), in_S1 (qD < 0.05; fewer than 2 compounds: the top 10 by zD, flagged); fold (compound
                       folds dealt after S1); oof_signature (which signature scored it: 'out of fold', 'NOT out of
                       fold' only when S1 has one compound); s_oof_program_contrast (mean z over that signature's
                       genes), zs_oof (that score calibrated by the label permutations), ps_oof, qs_oof (pooled
                       permutation p and permutation FDR over keep; only a positive score counts; the signatures,
                       chosen with the true labels on other compounds, are held fixed in the null, so when S1 is a
                       fallback S2 is flagged exploratory): the step's list-free p53-activation score of every
                       drug-dose; in_S2_p53_activating (qs_oof < 0.05 and positive); in_S2_minus_foldF (the
                       training drug-doses of P_-F, selected with nested signatures); program_P_delta_log2 (mean WT-minus-altered difference over the genes of P);
                       exposure_DD_z and exposure_moving_absz_ge3 (atlas); specificity (the S1 and S2 drug-doses with
                       the strongest scores): z_divergence_TP53_20perm (TP53's divergence calibrated on 20 permutations,
                       the scale of the groupings), best_other_grouping and its z, n_groupings_above_TP53,
                       TP53_explains_best; overlays: overlay_panel_P53_ACTIVITY_z, overlay_two_way_in_ii_p53 /
                       in_ii_active (when the sibling tables are present).
b_p53_program_genes.csv.gz  per atlas gene: z_S1_stage1 (program z over S1), z_program (over S2: drug-equal mean z,
                       calibrated by the label permutations), p_up / q_up, p_down / q_down (BH over genes, the exposure
                       left out), wt_minus_alt_log2 and wt_mean_log2 (drug-weighted over S2), frac_compounds_up / down,
                       frac_compounds_wt_up / down, n_compounds_with_z, in_P1_stage1, in_P, in_P_down, in_P_minus_foldF
                       (the cross-fitted programs), in_P_noX, loco_frequency (share of leave-one-compound-out programs
                       holding the gene), rank_in_P; overlay_* columns (curated lists, after the fact).
                       Fewer than 10 genes passing makes a program a fallback (the top 25 by z): flagged in checks.csv,
                       key_results.csv (P53PROG_* rows) and GENOME_WIDE.md, and to be read as exploratory.
b_p53_program.csv      the members of P and P-down, by z, with program_is_fallback and their stability (loco_frequency,
                       n_folds_with_gene).
b_program_stability.csv  fold programs vs P (Jaccard; status: cross-fitted, single training compound, small, P-down
                       small), fold Jaccards, leave-one-compound-out Jaccards, P without the exposure-moving drug-doses,
                       null S1 / S2 sizes (each permuted labelling treated as the truth with the same permutation-FDR
                       rule; value = the largest, note = the observed size, the mean, the share of labellings with a
                       non-empty selection and every size), null program sizes (each of 20 permuted labellings treated
                       as the truth with S2 fixed; q < 0.05 by z alone, next to the observed count with the same rule).
b_feature_specificity.csv  every line grouping of the atlas (drivers, protein changes, organs, MTAP loss; 20
                       permutations each) on the checked S1 / S2 drug-doses (z of the same top-k divergence) and for P
                       (z of the program's mean drug-equal contrast over S2, 20 permutations); TP53's own z on the same
                       20-permutation scale next to it. P is selected for TP53 by construction; a grouping that comes
                       close says that P (or a drug-dose's divergence) could equally be a lineage or driver response.
b_overlays.csv         role overlay: each curated list vs P, P-down and the stage-1 program (overlap, expected overlap,
                       hypergeometric p, median percentile of the members' program z, each member's rank); S2 vs the
                       panel's P53_ACTIVITY z >= 3 (overlap, Spearman of zs_oof with the panel z) and vs two_way's ii_p53.

(C) Screen and program-level models. Model per outcome: Y = drug-dose x TP53-group FE + line FE + b_WT x WT + b_alt x
altered + covariates x group (two_way's ddxg); b_common = one slope for all lines (FE and covariates still by group).
Covariate sets: gw (primary) = DD_beta (0 where the drug-dose has no consensus response), DD_A (relative abundance),
resp_bg (the line's mean |r2| over the atlas genes outside every data-derived program and the exposure); gw_all = gw with
resp_all (mean |r2| over all genes: contains the p53 program in WT lines under p53 activators, so it can absorb part of
b_WT); gw_pc = gw + the line's scores on the top 3 genome-wide components (atlas W2 SVD); curated_cycle = DD_beta, DD_A,
S, G2M (Tirosh modules: curated, labelled), resp_bg; none; gw_rt = gw + the readthrough covariates (--rt-covariates;
TRIM72: FUS and PYCARD-AS1 r2, two_way's full_rt). The exposure (and every placebo gene) is never an outcome of its own
fit: its row has tested = False.
c_screen_genes.csv.gz  every atlas gene as the outcome (gw, true labels): tested (n_rows >= 50, >= 3 lines per group,
                       >= 10 compounds, x varies in both groups), n_rows, n_lines_WT / alt, n_drugdoses, n_drugs, b_common,
                       se_common (conservative two-way), t_common, p_common, q_common (BH over tested genes), b_WT, b_alt,
                       diff, se_diff, t_diff, p_diff, q_diff, the compound-cluster SEs, sd_x_resid; nulls:
                       p_label_pooled_diff / q_label_diff (|t_diff| against every relabelling x gene: TP53 labels permuted
                       over the analysed lines, the same permutation for all genes), p_label_own_diff (the gene's own
                       relabellings: coarse), p_xperm_pooled_common / q_xperm_common and p_xperm_pooled_diff (|t|
                       against the exposure shuffled across lines within each drug-dose x group cell, the same shuffles
                       for all genes: a null for the gene's studentised t, whose two-way SE carries the line-level
                       structure the shuffles break; not for unstudentised or set statistics),
                       placebo_pct_common / diff_<family> (share of that family's placebo t below
                       the gene's t); b_common / diff / p_* under each other covariate set; in_P, in_P_down,
                       atlas_program, overlay_*, placebo_family; dog_class, coreg_r_across_dd_*, in_TRIM72_locus_200kb
                       (sibling tables, when present).
c_screen_top.csv       the top 200 genes by |t_common| and the top 200 by |t_diff| (rank_by says which).
c_calibration.csv      genome-wide counts: kind = observed / tp53_relabelling (diff only: relabelling keeps the
                       within-line association, so it is NOT a null for the common slope) / exposure_shuffle (common and
                       diff) / placebo_expression / placebo_response (each placebo's own fit, its own gene and the
                       exposure left out); N_q01_common / N_q01_diff (BH q < 0.1 within the replicate), lambda_common /
                       lambda_diff (median t^2 / 0.4549), camera_stat_P53PROG_UP_* (the set statistic of P in that
                       replicate: descriptive; under the exposure shuffles it is not a null of the set statistic, see
                       c_set_tests); summary rows (kind = p_count / rank): p_count = (1 + #replicates with N >=
                       observed) / (1 + replicates), and the exposure's rank among each placebo family.
c_placebos.csv         the placebo exposures (atlas genes outside the data-derived programs, not the exposure or the
                       readthrough covariates; the curated overlays play no part): family (expression, response), rank,
                       symbol, distance, the matching features
                       (log2 median line CPM, lines expressing, share of finite cells, share of keep drug-doses with |DD_z|
                       >= 3, residual SD after the FE), used_genome_wide, and the primary program-level model with that
                       placebo as the exposure (b_WT, b_alt, diff, t_diff, b_common, t_common).
c_program_models.csv   two_way.run_models on program-level outcomes (mean r2 of a set's members a line expresses, per
                       well, then the drug-dose mean): every two_way d1 column (b_WT, b_alt with compound-cluster and
                       conservative two-way SE / CI / p, diff with compound, line and two-way SE, p_diff_tp53_label_perm
                       (studentised, whole model refitted), mde_diff_80, b_common ...; p_*_perm_within_dd: two_way's
                       within-cell permutation p, unstudentised; it shuffles the exposure within each cell and so breaks
                       its line-level structure: within-cell noise only, NOT a null for a line-level association
                       (anti-conservative when exposure and outcome share line-level structure; not used in
                       key_results.csv or GENOME_WIDE.md)), role
                       (primary / secondary / sensitivity / program / overlay), variant (all; S2cf_or_X, S2cf, X = the
                       data-defined active sets: the out-of-fold p53-activating drug-doses and the exposure-moving ones);
                       p_holm_covsets_* = Holm over the covariate sets of the primary outcome; placebo_* = the primary
                       model's diff / common t among each placebo family (fraction below, empirical two-sided p).
                       Outcomes: P53PROG_UP_cf (primary: each drug-dose scored with the program cross-fitted for its
                       fold), P53PROG_UP, _noX, _core, P53PROG_DOWN(_cf), P53PROG_UP_fF (each fold's program on all
                       drug-doses), PROG_Pnn (atlas programs), OVERLAY_* (curated, role overlay; OVERLAY_P53_ACTIVITY21
                       with curated_cycle is the bridge to two_way's primary P53_SCORE row; it uses resp_bg for
                       two_way's bg_abs_r2 and leaves out the line without a TP53 group, which two_way counts as
                       altered). Programs and overlays use a quarter of the permutations of the p53-program rows.
c_set_tests.csv        camera-style test inside the screen for each set with >= 8 tested genes (two_way.set_test at genome
                       scale): estimate diff or common, m1 set genes vs m2 all other tested genes, statistic = mean t of
                       the set minus mean t of the rest, variance inflated by a'Ra from the genes' cluster scores
                       (compound, line, two-way: the largest, never below independence; two-way skipped when any gene
                       has s^2 <= 0), p_set_camera (the test), p_set_independent; p_null_calibrated / p_null_empirical
                       (diff only): the same statistic over the TP53 relabellings. The common slope has no permutation
                       p: a relabelling leaves it unchanged, and the within-cell exposure shuffles break the exposure's
                       line-level structure, which makes a set statistic calibrated by them anti-conservative.

(D) What moves with the exposure.
d_programs/            tahoe_atlas.angle_programs written here (programs.csv, program_members.csv, broad_components.csv,
                       program_drug_effects.parquet, program_line_context.csv); its per-line program values are the
                       mean member r2 from the tensor (not the atlas's log of summed counts).
d_program_vs_exposure.csv  per atlas program (and per data-derived program and overlay): across drug-doses, r of the
                       set's drug-dose score (program_drug_effects score_z; for the other sets the robust z of the mean
                       DD_z of its genes) with the exposure's DD_z over the keep drug-doses, drug-block permutation null
                       (null_sd, z, p; q over the atlas programs); within lines, the program-level model (ddxg, gw:
                       b_common, p_common_twoway, diff, p_diff_twoway, p_diff_tp53_label_perm; q over the atlas
                       programs); the camera t of the set's genes in the screen.

key_results.csv        the headline numbers, the primary test first: section, role, what, fe, covset, n, estimate,
                       ci_lo, ci_hi, p_twoway, p_label_perm, q, detail. p_label_perm holds TP53-label permutation p
                       only (for the camera rows of diff: calibrated by the relabellings); within-cell shuffle p are not
                       shown here. A detail that starts with FALLBACK marks an outcome built from a fallback program.
checks.csv             tensor vs atlas W1 / W2 / DD_lfc, plates written, finite cells, panel genes, the engine vs
                       two_way.Design + many_diffs + fit on real genes, two_way's label engine at the true labels, the
                       (B) fallbacks, sets not tested, optional stages skipped (with the error).
run_info.json          arguments, exposure, versions, stage times, peak RSS of the parent and the workers (and how it is
                       measured), date, cache keys, genes tested, the (B) sizes, null S1 / S2 sizes and flags.
GENOME_WIDE.md (in the step's output folder) states the findings in words, from these tables (no date in it, so it is
byte-identical across runs of the same data; run_info.json has the date).

(E) A TRIM72-detection-stratified single-cell pseudobulk (every gene an outcome at the cell level) is not run here: it
needs one more pass over the raw cells; GENOME_WIDE.md says what it would take.
"""

E_NOTE = """A TRIM72-detection-stratified single-cell pseudobulk would make every gene an outcome at the cell level. It
needs one more pass over the raw cells (338 GB; a re-download in stream mode), so this step, which reads no raw
cells, does not run it. What it would take: in tahoe_atlas._build_group, add a 'TRIM72 detected' flag to the (sample,
line) key (tahoe_atlas.py:507; about 2 x 20 GB of pseudobulk, ~1 h); then, per (well, line), the detected-minus-
undetected contrast of every gene with this step's per-plate r2 steps applied to each stratum, modelled with the
TP53-group interaction and two-way clusters as here; placebo strata from detection-matched genes chosen by data. Limits
to expect: detected cells are a small minority (803,499 of ~95M), and depth confounding needs a per-cell UMI
adjustment, as single_cell_all does."""


def fmt(v, f="{:.3g}"):
    try:
        return f.format(v) if v is not None and np.isfinite(v) else "NA"
    except (TypeError, ValueError):
        return str(v)


def write_findings(path, exposure, KR, info, B_, n_tested, top_common, programs_moving, special):
    """GENOME_WIDE.md: the findings in words, generated from key_results.csv and the tables."""
    pr = KR.iloc[0]

    def row(what_prefix):
        h = KR[KR["what"].astype(str).str.startswith(what_prefix)]
        return h.iloc[0] if len(h) else None
    L_ = [f"# Genome-wide, list-free: {exposure} and p53 output in Tahoe-100M",
          "",
          "Generated by `genome_wide.py` (date and run details in `tables/run_info.json`). Associations in 24 h mRNA, "
          "Tahoe-100M only; "
          "every result is genome-wide and data-driven at the base, and curated lists appear only as overlays. "
          f"Exposure: **{exposure}**. Tables: `tables/` (README_tables.txt explains every column).",
          "",
          "## Primary test",
          f"{pr['what']} (fe {pr['fe']}, covariates {pr['covset']}, all drug-doses): **{fmt(pr['estimate'], '{:+.4f}')}** "
          f"(95% CI {fmt(pr['ci_lo'], '{:+.4f}')} to {fmt(pr['ci_hi'], '{:+.4f}')}; conservative two-way p "
          f"{fmt(pr['p_twoway'])}; TP53-label permutation p {fmt(pr['p_label_perm'])}). {pr['detail']}",
          ""]
    L_ += [f"**Is {exposure} special?** Judged against the response-matched placebo exposures (genes that move as "
           f"often and as much within lines as {exposure}, chosen without looking at any outcome): {special}", ""]
    for pref in ("placebo (response-matched)", "placebo (expression-matched)"):
        r = row(pref)
        if r is not None:
            L_.append(f"- {r['what']}: {r['detail']}")
    def nulls(obs, sizes):
        v = np.array(sizes, float)
        if not len(v):
            return f"{obs} at permutation FDR < 0.05"
        return (f"{obs} at permutation FDR < 0.05; each of {len(v)} permuted labellings as the truth gives max "
                f"{int(v.max())}, non-empty in {100 * (v > 0).mean():.0f}%")
    fbk = f"FALLBACK: fewer than {PROG_MIN} genes pass, the top {PROG_FALLBACK} by z (exploratory)"
    L_ += ["", "## The Tahoe p53 program (found from the data)",
           f"- Selection 1 (genome-wide WT-vs-altered divergence; {nulls(B_['n_S1_q'], B_['null_S1'])}): "
           f"{len(B_['S1'])} drug-doses of {len(set(B_['drug_id'][B_['S1']]))} compounds"
           + (" (S1 FALLBACK: the top 10 by zD; S2 and the program are exploratory)" if B_["s1_fallback"] else "")
           + f"; compound folds F_eff = {B_['F']}.",
           f"- p53-activating drug-doses (out-of-fold program score; {nulls(B_['n_S2_q'], B_['null_S2'])}, the "
           f"signatures held fixed): {len(B_['S2'])} drug-doses of {len(set(B_['drug_id'][B_['S2']]))} compounds: "
           f"{B_['S2_names']}.",
           f"- Program P: {len(B_['P'])} genes WT-selectively induced" + (f" ({fbk})" if B_["small"] else "")
           + f"; P-down: {len(B_['Pd'])} repressed" + (f" ({fbk})" if B_["small_d"] else "")
           + f"; top genes of P: {B_['P_top']}.",
           f"- Cross-fitting: {'; '.join(f'fold {f}: {s}' for f, s in enumerate(B_['fold_status']))}.",
           f"- Null program sizes (20 permuted labellings as truth, S2 fixed): max {max(B_['null_sizes'] or [0])} "
           f"(observed with the same rule {B_['n_obs_zonly']}).",
           f"- Specificity (line groupings of the atlas, 20 permutations each): {B_['spec_text']}"]
    for pref in ("21-gene P53_ACTIVITY", "OVERLAY_P53_ACTIVITY21"):
        r = row(pref)
        if r is not None:
            L_.append(f"- Overlay: {r['what']}: {r['detail']}")
    if B_["flags"]:
        L_.append(f"- Flags: {'; '.join(B_['flags'])}.")
    L_ += ["", "## Genome-wide screen (every expressed gene as the outcome)"]
    for pref in ("screen: common slope", "screen: b_WT - b_alt"):
        r = row(pref)
        if r is not None:
            L_.append(f"- {r['what']}: {r['detail']}")
    L_.append(f"- Genes tested: {n_tested}. Strongest common slopes (q, readthrough class where known): {top_common}.")
    L_ += ["", "## What moves with the exposure: data-driven programs", f"- {programs_moving}", "",
           "## Single cells (E, not run)", E_NOTE, "",
           "## Limits",
           "- Associations in mRNA at one time point; no MG53 protein, no p53 protein, no perturbation of MG53.",
           "- The p53 program is selected for its TP53-WT selectivity: a program-level association with the exposure "
           "inside WT lines is what the primary test measures; the program's membership is not evidence of p53 "
           "binding (b_feature_specificity.csv says whether a lineage / driver grouping explains it as well).",
           "- Within-line slopes use only line-to-line variation inside the same drug-dose and TP53 group; an exposure "
           "that tracks a line's drug sensitivity can look 'WT-specific' against any WT-only response, which is why "
           "the response-matched placebos are the comparison for 'is TRIM72 special'.",
           "- TRIM72 is barely expressed in these lines (~4 CPM): estimates are attenuated by counting noise.", ""]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L_))


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild the caches (the tensor too)")
    ap.add_argument("--exposure", default=os.environ.get("MG53_GW_EXPOSURE") or GENE,
                    help="the exposure gene (an atlas gene; default $MG53_GW_EXPOSURE, else TRIM72)")
    ap.add_argument("--chunk", type=int, default=64, help="genes per chunk (memory ~ chunk; default 64)")
    ap.add_argument("--workers", type=int, default=2, help="screen processes (2 BLAS threads each; default 2)")
    ap.add_argument("--perm", type=int, default=100, help="TP53-label permutations of the program derivation (B)")
    ap.add_argument("--folds", type=int, default=5, help="compound folds for cross-fitting (B, C)")
    ap.add_argument("--label-perm", type=int, default=20, help="genome-wide TP53 relabellings (C)")
    ap.add_argument("--x-perm", type=int, default=20, help="genome-wide within-cell exposure shuffles (C; a null for "
                    "the per-gene studentised t only)")
    ap.add_argument("--placebos", type=int, default=20, help="genome-wide placebo exposures, half per family (C)")
    ap.add_argument("--placebos-set", type=int, default=200, help="placebos of the primary program-level model, half "
                    "per family (C)")
    ap.add_argument("--set-label-perm", type=int, default=2000, help="TP53-label permutations per program-level design")
    ap.add_argument("--set-within-perm", type=int, default=1000, help="within-cell permutations per program-level "
                    "design (two_way's; reported as within-cell noise only, not as a test)")
    ap.add_argument("--d-perm", type=int, default=1000, help="drug-block permutations of the across-drug-dose test (D)")
    ap.add_argument("--extra-genes", default=None, help="non-atlas genes whose counts the pass also collects (comma "
                    "list; default PYCARD-AS1 when the exposure is TRIM72, else none)")
    ap.add_argument("--rt-covariates", default=None, help="readthrough covariates of the gw_rt set (comma list of atlas "
                    "or extra genes; default FUS,PYCARD-AS1 when the exposure is TRIM72, else none)")
    ap.add_argument("--quick", action="store_true", help="few permutations, relabellings and placebos (a test run)")
    a = ap.parse_args()
    if a.quick:
        a.perm, a.label_perm, a.x_perm, a.placebos, a.placebos_set = 50, 2, 2, 2, 20
        a.set_label_perm, a.set_within_perm, a.d_perm = 200, 100, 200
    t_all = time.time()
    out = os.environ.get("MG53_OUT") or HERE
    cdir, tab = os.path.join(out, "cache"), os.path.join(out, "tables")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(tab, exist_ok=True)
    sib = os.path.dirname(os.path.abspath(out))           # the other steps' folders (run_mg53_p53.py layout)
    data = a.data
    exposure = a.exposure
    info = {"args": vars(a), "exposure": exposure, "data": os.path.realpath(data), "out": os.path.realpath(out),
            "stage_seconds": {}, "versions": {"python": sys.version.split()[0], "numpy": np.__version__,
                                              "pandas": pd.__version__, "scipy": __import__("scipy").__version__}}
    ck = Checks()
    log(f"data {data}; out {out}; exposure {exposure}")
    log("primary test (declared up front): fe {fe}, drug-doses {dd}, covariates {covset}, outcome {outcome}, "
        "estimand {estimand}, conservative two-way SE; everything else is secondary, sensitivity, screen, overlay or "
        "a check".format(**PRIMARY))
    fx = A.FX(os.path.join(data, "atlas"))                 # sets tahoe_atlas.MIN_CELLS from info.json
    gsym = fx.genes.iloc[fx.gi]["symbol"].astype(str).to_numpy()
    sym2idx = {}
    for i, s in enumerate(gsym):
        sym2idx.setdefault(s, i)
    if exposure not in sym2idx:
        print(f"{exposure} is not an expressed atlas gene in {data} (on the synthetic build TRIM72 has no counts); "
              f"choose --exposure", file=sys.stderr, flush=True)
        sys.exit(2)
    x_idx = sym2idx[exposure]
    dx, dr = RT_DEFAULTS.get(exposure, ([], []))
    extra = [s.strip() for s in (a.extra_genes if a.extra_genes is not None else ",".join(dx)).split(",") if s.strip()]
    rt = [s.strip() for s in (a.rt_covariates if a.rt_covariates is not None else ",".join(dr)).split(",") if s.strip()]
    bad = [s for s in rt if s not in sym2idx and s not in extra]
    if bad:
        print(f"--rt-covariates: {', '.join(bad)} is neither an atlas gene nor in --extra-genes", file=sys.stderr)
        sys.exit(2)
    info.update(extra_genes=extra, rt_covariates=rt)
    panel_min = int(fx.info.get("min_cells", TW.DP.T.MIN_CELLS))
    want = gw_manifest(data, extra, panel_min)
    validate_cache(cdir, want, a.recompute)
    grid = TW.Grid(data)
    if list(grid.w["sample"].astype(str)) != list(fx.wells["sample"].astype(str)):
        sys.exit("atlas wells.csv read twice gives different well orders")
    lines = fx.lines["cell_line_id"].astype(str).tolist()
    wt, lab = tp53_labels(data, lines)
    L, nd = len(lines), grid.nd
    if not lab.all():
        log(f"WARNING: {int((~lab).sum())} lines without a TP53 group are left out of (B) and (C)")
    ck.add("lines with a TP53 group (WT / altered)", int(lab.sum()), L,
           f"WT {int((wt & lab).sum())}, altered {int((~wt & lab).sum())}; left out: "
           f"{', '.join(np.array(lines)[~lab]) or 'none'}")

    # ---------------------------------------------------------------- (A)
    with stage("(A) tensor", info):
        side = build_tensor(data, fx, grid, cdir, extra)
        TW.write_manifest(cdir, want)
        T = Tensor(cdir)
        V = tensor_checks(side, fx, ck)
    V.to_csv(os.path.join(tab, "a_tensor_summary.csv"), index=False, float_format="%.6g")
    gdf = pd.read_csv(os.path.join(cdir, "r2_genes.csv"))
    tok2idx = dict(zip(gdf["token"].astype(int), gdf["idx"].astype(int)))
    info["tensor"] = {"genes": T.G, "wells": T.NW, "lines": T.L, "gb": round(T.G * T.rowb / 1e9, 3)}

    def panel_check():
        TW.DP.T.MIN_CELLS = panel_min                      # the panel setup hard-codes T.MIN_CELLS (30)
        E = TW.build_panel_cache(data, cdir)
        genes = [g for g in E.genes if g in sym2idx]
        pw = TW.panel_well_arrays(E, grid, genes)
        R2 = T.take([sym2idx[g] for g in genes])
        rows = []
        for j, g in enumerate(genes):
            xg, yg = R2[j].astype(float), pw[g]
            m = np.isfinite(xg) & np.isfinite(yg)
            same = bool((np.isfinite(xg).any(axis=0) == np.isfinite(yg).any(axis=0)).all())
            rows.append({"gene": g, "n_both": int(m.sum()),
                         "pearson_r": float(np.corrcoef(xg[m], yg[m])[0, 1]) if m.sum() > 2 else np.nan,
                         "median_abs_diff": float(np.median(np.abs(xg[m] - yg[m]))) if m.any() else np.nan,
                         "max_abs_diff": float(np.max(np.abs(xg[m] - yg[m]))) if m.any() else np.nan,
                         "tensor_only": int((np.isfinite(xg) & ~np.isfinite(yg)).sum()),
                         "panel_only": int((~np.isfinite(xg) & np.isfinite(yg)).sum()),
                         "same_expressed_lines": same})
        P_ = pd.DataFrame(rows)
        P_.to_csv(os.path.join(tab, "a_panel_check.csv"), index=False, float_format="%.6g")
        s_ = P_[P_["same_expressed_lines"]]
        ck.add("tensor vs panel per (well, line) r2, genes with identical expressed-line sets: max |diff|",
               float(s_["max_abs_diff"].max()) if len(s_) else np.nan, len(s_),
               f"median of the per-gene max |diff| {s_['max_abs_diff'].median():.2g}; min Pearson r "
               f"{s_['pearson_r'].min():.6f}; panel min_cells set to the atlas's {panel_min}")
        d_ = P_[~P_["same_expressed_lines"]]
        ck.add("tensor vs panel: genes whose expressed-line rules differ (panel vs atlas)", len(d_), len(P_),
               ", ".join(d_["gene"].astype(str)[:20]))
    optional("panel check", panel_check, ck)

    x = dd_level(T.take([x_idx]), grid.B)[0]
    x[:, ~lab] = np.nan
    ddz = np.asarray(fx.DD_z, dtype=np.float32)[:, fx.gi]
    ddz_x = ddz[:, x_idx].astype(float)
    keep = ~(fx.dd["unreliable_plate_only"].to_numpy(bool) | fx.dd["position_not_correctable"].to_numpy(bool))
    if exposure == "TRIM72":
        def ida():
            ref = os.path.join(REPO, "trim72_idarubicin", "corrected", "TRIM72_idarubicin_5uM_per_line_corrected.csv")
            r = grid.dd.index[(grid.dd["drug"] == "Idarubicin (hydrochloride)") & np.isclose(grid.dd["conc"], 5)]
            if not (os.path.exists(ref) and len(r)):
                return
            t_ = pd.read_csv(ref).set_index("cell_line_id")["log2FC_corrected"].reindex(grid.L).to_numpy(float)
            v = x[int(r[0])]
            m = np.isfinite(t_) & np.isfinite(v)
            ck.add("idarubicin 5 uM per-line TRIM72 r2 (tensor, mean of the wells) vs trim72_idarubicin/corrected, "
                   "max |diff|", float(np.max(np.abs(t_[m] - v[m]))) if m.any() else np.nan, int(m.sum()))
        optional("idarubicin check", ida, ck)

    # ---------------------------------------------------------------- (B)
    with stage("(B) Tahoe p53 program", info):
        U = labellings(wt, lab, a.perm, np.random.default_rng([SEED, 1]))
        key1 = sha([want, a.perm, SEED, U, CACHE_VERSION])[:12]
        for f in glob.glob(os.path.join(cdir, "b_pass1_*.npz")):
            if not f.endswith(f"_{key1}.npz"):
                os.remove(f)
        p1 = b_pass1(T, grid, U, wt, lab, a.chunk, os.path.join(cdir, f"b_pass1_{key1}.npz"))
        UFt = feature_labellings(fx, wt, lab, np.random.default_rng([SEED, 4]))
        log(f"  line groupings for the specificity check: {len(UFt[0])}")
        B_ = derive_program(T, grid, fx, wt, lab, U, p1, x_idx, ddz_x, a.folds, a.chunk, UFt, ck, info)
        B_.update(D0=p1["D"][:, 0], d0=p1["d0"], drug_id=grid.drug_id)
    for fl in B_["flags"]:
        ck.add("(B) flag", np.nan, note=fl)
    ck.add("(B) compound folds F_eff = min(--folds, S1 compounds)", B_["F"], a.folds,
           "; ".join(f"fold {f}: {s}" for f, s in enumerate(B_["fold_status"])))
    for nm_, obs_, nul_ in (("S1", B_["n_S1_q"], B_["null_S1"]), ("S2", B_["n_S2_q"], B_["null_S2"])):
        ck.add(f"(B) {nm_} sizes with each permuted labelling as the truth (permutation FDR < 0.05): max",
               max(nul_ or [np.nan]), len(nul_), f"observed {obs_} (before any fallback); non-empty in "
               f"{sum(v > 0 for v in nul_)} of {len(nul_)}")
    ck.add("(B) program sizes under 20 permuted labellings (S2 fixed; q < 0.05 by z alone): max",
           max(B_["null_sizes"] or [np.nan]), len(B_["null_sizes"]), f"observed with the same rule {B_['n_obs_zonly']}; "
           f"all: {B_['null_sizes']}")
    nm2 = grid.dd["drug"].astype(str).to_numpy()
    B_["S2_names"] = "; ".join(f"{nm2[d]} {grid.dd.at[d, 'conc']:g}" for d in B_["S2"][
        np.argsort(-np.nan_to_num(B_["zs_oof"][B_["S2"]], nan=-np.inf), kind="stable")][:30]) + \
        (" ..." if len(B_["S2"]) > 30 else "")
    B_["P_top"] = ", ".join(gsym[B_["P"][:25]])
    log(f"(B) S1 {len(B_['S1'])} drug-doses ({B_['n_S1_q']} at permutation FDR < 0.05; null max "
        f"{max(B_['null_S1'] or [0])}); S2 {len(B_['S2'])} drug-doses ({B_['n_S2_q']}; null max "
        f"{max(B_['null_S2'] or [0])}); P {len(B_['P'])} genes (P-down {len(B_['Pd'])}); top: {B_['P_top']}")
    for fl in B_["flags"]:
        log(f"(B) flag: {fl}")

    # ---------------------------------------------------------------- sets, scores, covariates
    with stage("(D-prep) atlas programs", info):
        progs = optional("atlas programs (tahoe_atlas.angle_programs)",
                         lambda: atlas_programs(fx, T, grid, tok2idx, os.path.join(tab, "d_programs")), ck, {})
    overlays = overlay_sets(sym2idx, sib, ck)
    rt_idx = [sym2idx[s] for s in rt if s in sym2idx]
    reg = build_registry(B_, progs, overlays, sym2idx, x_idx, rt_idx, ck)
    names = [r["name"] for r in reg]
    bg = np.ones(T.G, bool)
    for r in reg:
        if r["role"].startswith("p53 program"):
            bg[r["members"]] = False
    bg[x_idx] = False
    with stage("program scores pass", info):
        U3, mu, sdv = pc_loadings(fx)
        skey = sha([want, [r["members"] for r in reg], bg, U3, CACHE_VERSION])[:12]
        for f in glob.glob(os.path.join(cdir, "scores_*.npz")):
            if not f.endswith(f"_{skey}.npz"):
                os.remove(f)
        sc = scores_pass(T, grid, [r["members"] for r in reg], bg, U3, mu, sdv, max(a.chunk, 128),
                         os.path.join(cdir, f"scores_{skey}.npz"))
    ck.add("finite cells in the tensor = finite cells counted plate by plate during the pass",
           float(int(sc["nfin"]) == int(side["finite_total"])), int(sc["nfin"]),
           f"counted during the pass {int(side['finite_total'])}")
    tabs = {k_: v for k_, v in TW.covariates(grid).items()}
    tabs["resp_all"] = TW.Grid.dd_mean(grid.B, side["resp_all"].astype(np.float64))
    tabs["resp_bg"] = sc["resp_bg"]
    for j in range(3):
        tabs[f"pc{j + 1}"] = sc["pcs"][j]
    covsets = {k_: list(v) for k_, v in COVSETS.items()}
    if rt:
        pbe = np.load(os.path.join(cdir, "pseudobulk_effects.npz"), allow_pickle=False) if extra else None
        for s in rt:
            if s in sym2idx:
                tabs[f"rt_{s}"] = dd_level(T.take([sym2idx[s]]), grid.B)[0]
            else:
                j = [str(v) for v in pbe["symbols"]].index(s)
                tabs[f"rt_{s}"] = TW.Grid.dd_mean(grid.B, pbe["r2"][:, :, j].astype(np.float64))
        covsets["gw_rt"] = covsets["gw"] + [f"rt_{s}" for s in rt]
    else:
        ck.add("covariate set gw_rt (readthrough)", np.nan, note="not fitted: no readthrough covariates for this "
               "exposure (--rt-covariates) or no extra genes")
    tabs["x"] = x
    for j, nm in enumerate(names):
        tabs[nm] = sc["sets"][j]
    cf_up, cf_dn = tabs["P53PROG_UP"].copy(), tabs["P53PROG_DOWN"].copy()
    fold = B_["fold"]
    n_cf = 0
    for f in range(B_["F"]):
        rows_f = fold == f
        if f"P53PROG_UP_f{f}" in tabs and len(B_["Pf"][f]):
            cf_up[rows_f] = tabs[f"P53PROG_UP_f{f}"][rows_f]
            n_cf += int(rows_f.sum())
        if f"P53PROG_DOWN_f{f}" in tabs and len(B_["Pdf"][f]):
            cf_dn[rows_f] = tabs[f"P53PROG_DOWN_f{f}"][rows_f]
    tabs["P53PROG_UP_cf"], tabs["P53PROG_DOWN_cf"] = cf_up, cf_dn
    ck.add("P53PROG_UP_cf: drug-doses scored with their fold's cross-fitted program", n_cf, nd,
           "the others use P (not cross-fitted)" if n_cf < nd else "all")

    # ---------------------------------------------------------------- (C) program-level models (the primary first)
    if not np.isfinite(tabs["P53PROG_UP_cf"]).any():
        sys.exit("(C) the primary outcome P53PROG_UP_cf has no value (the p53 program is empty); see checks.csv")
    S2cf = np.isin(np.arange(nd), B_["S2"])
    Xset = B_["X"]
    alldd = np.ones(nd, bool)
    Bw, Bl = a.set_within_perm, a.set_label_perm
    Bw4, Bl4 = max(1, Bw // 4), max(1, Bl // 4)
    plan = [{"outcome": "P53PROG_UP_cf", "fe": "ddxg", "covset": "gw", "variant": "all", "ddmask": alldd,
             "role": "primary", "family": "p53 program (cross-fitted)", "B_within": Bw, "B_label": Bl}]
    for cs in [c for c in covsets if c != "gw"]:
        plan.append(dict(plan[0], covset=cs, role="sensitivity"))
    plan.append(dict(plan[0], fe="dd", role="sensitivity"))
    for vn, m_ in (("S2cf_or_X", S2cf | Xset), ("S2cf", S2cf), ("X", Xset)):
        if len(set(grid.drug_id[m_])) >= 2:              # the data-defined active sets (two_way's ii_* analogues)
            plan.append(dict(plan[0], variant=vn, ddmask=m_, role="sensitivity"))
        else:
            ck.add(f"program-level sensitivity on drug-dose set {vn}", np.nan, int(m_.sum()), "not fitted: < 2 compounds")
    for oc, role in (("P53PROG_DOWN_cf", "secondary"), ("P53PROG_UP", "sensitivity"), ("P53PROG_UP_noX", "sensitivity"),
                     ("P53PROG_UP_core", "sensitivity"), ("P53PROG_DOWN", "sensitivity")):
        if oc in tabs and np.isfinite(tabs[oc]).any():
            plan.append(dict(plan[0], outcome=oc, role=role, family="p53 program"))
    with stage("(C) program-level models: the p53 programs", info):
        PM = program_models(tabs, grid, wt, plan, np.random.default_rng([SEED, 6]), covsets)
    prim = PM.iloc[0]
    log(f"PRIMARY {prim['readout']} [ddxg, gw, all]: diff {prim['diff']:+.4f} (95% CI {prim['ci_diff_lo_twoway']:+.4f} "
        f"to {prim['ci_diff_hi_twoway']:+.4f}; conservative two-way p {prim['p_diff_twoway']:.3g}; label p "
        f"{prim.get('p_diff_tp53_label_perm', np.nan):.3g})")

    def other_models():
        pl2 = []
        for r in reg:
            if r["role"] == "p53 program (data)" and r["name"].startswith("P53PROG_UP_f") and r["n"] > 0:
                pl2.append(dict(plan[0], outcome=r["name"], role="sensitivity", family="p53 program (fold)",
                                B_within=Bw4, B_label=Bl4))
        for r in reg:
            if r["tested_as_set"] and r["role"] != "p53 program (data)":
                fam = "program" if r["role"].startswith("program") else "overlay"
                pl2.append(dict(plan[0], outcome=r["name"], role=fam, family=r["role"], B_within=Bw4, B_label=Bl4))
                if r["name"] == "OVERLAY_P53_ACTIVITY21":
                    pl2.append(dict(pl2[-1], covset="curated_cycle"))
        return program_models(tabs, grid, wt, pl2, np.random.default_rng([SEED, 7]), covsets) if pl2 else None
    with stage("(C/D) program-level models: atlas programs, folds, overlays", info):
        PM2 = optional("program-level models of the atlas programs and overlays", other_models, ck)
    PMall = pd.concat([PM] + ([PM2] if PM2 is not None else []), ignore_index=True)
    m_ = (PMall["readout"] == "P53PROG_UP_cf") & (PMall["fe"] == "ddxg") & (PMall["variant"] == "all")
    for col, pc in (("p_holm_covsets_twoway", "p_diff_twoway"), ("p_holm_covsets_label", "p_diff_tp53_label_perm")):
        PMall[col] = np.nan
        PMall.loc[m_, col] = holm(PMall.loc[m_, pc].to_numpy())
    ck.add("two_way label engine at the true labels minus the main fit (program-level models): max |diff| of diff",
           float(PMall["check_label_engine_minus_main"].abs().max()), len(PMall),
           f"t: {PMall['check_label_engine_t_minus_main'].abs().max():.2g}")

    # ---------------------------------------------------------------- placebos
    excluded = set()
    for r in reg:
        if r["role"] != "overlay":                         # data-derived sets only: no curated list shapes the pool
            excluded |= set(r["members"].tolist())
    excluded |= set(rt_idx)
    n_set_f, n_gw_f = max(1, a.placebos_set // 2), max(1, a.placebos // 2) if a.placebos > 0 else 0
    PL = choose_placebos(gdf, p1, ddz, keep, x_idx, excluded, max(n_set_f, n_gw_f), nd, int(lab.sum()))
    PL["used_genome_wide"] = (PL["family"] != "exposure") & (PL["rank"] <= n_gw_f)
    PL["used_program_level"] = (PL["family"] != "exposure") & (PL["rank"] <= n_set_f)
    pls = PL[PL["used_program_level"] | PL["used_genome_wide"]]
    Xp_all = dd_level(T.take(pls["idx"].to_numpy()), grid.B)
    Xp_all[:, :, ~lab] = np.nan
    Xp = {int(g): Xp_all[j] for j, g in enumerate(pls["idx"])}

    def plac_models():
        sub = PL[PL["used_program_level"]]
        return placebo_program_models(tabs, grid, wt, "P53PROG_UP_cf", covsets["gw"],
                                      [Xp[int(g)] for g in sub["idx"]],
                                      [{"family": f_, "rank": r_, "idx": int(g), "symbol": s}
                                       for f_, r_, g, s in zip(sub["family"], sub["rank"], sub["idx"], sub["symbol"])])
    with stage("(C) placebo program-level models", info):
        PPM = optional("placebo program-level models", plac_models, ck)
    plac_summary = {}
    if PPM is not None and len(PPM):
        PL = PL.merge(PPM.drop(columns=["rank", "symbol"]), on=["family", "idx"], how="left")
        t_d, t_c = prim["diff"] / prim["se_diff_twoway"], prim["b_common"] / prim["se_common_twoway"]
        for fam in ("expression", "response"):
            g = PPM[PPM["family"] == fam]
            plac_summary[fam] = {"diff": placebo_compare(t_d, g["t_diff"]), "common": placebo_compare(t_c, g["t_common"])}
            for est in ("diff", "common"):
                fr, pe, n_ = plac_summary[fam][est]
                PMall.loc[0, f"placebo_{fam}_{est}_frac_below"] = fr
                PMall.loc[0, f"placebo_{fam}_{est}_p_empirical"] = pe
                PMall.loc[0, f"placebo_{fam}_n"] = n_
    PL.to_csv(os.path.join(tab, "c_placebos.csv"), index=False, float_format="%.6g")
    PMall.to_csv(os.path.join(tab, "c_program_models.csv"), index=False, float_format="%.6g")

    # ---------------------------------------------------------------- (C) the genome-wide screen
    order = np.argsort(grid.drug_id, kind="stable")
    starts = np.flatnonzero(np.r_[True, np.diff(grid.drug_id[order]) != 0])
    xo = x[order]
    covs_o = {cs: (np.stack([tabs[c][order] for c in cl]) if cl else np.zeros((0, nd, L))) for cs, cl in covsets.items()}
    dom = {}
    for cs, C in covs_o.items():
        dm = np.isfinite(xo) & lab[None, :]
        for c in C:
            dm &= np.isfinite(c)
        dom[cs] = dm
    rng_s = np.random.default_rng([SEED, 3])
    an = lab & dom["gw"].any(axis=0)
    relabel = np.zeros((a.label_perm, L), bool)
    for b in range(a.label_perm):
        relabel[b] = wt
        relabel[b, an] = rng_s.permutation(wt[an])
    xperm = xperm_arrays(xo, dom["gw"], wt, a.x_perm, np.random.default_rng([SEED, 5]))
    gwp = PL[PL["used_genome_wide"]]
    gw_idx = list(dict.fromkeys(int(g) for g in gwp["idx"]))     # a gene in both families is fitted once
    gw_pos = {g: j for j, g in enumerate(gw_idx)}
    plac = np.stack([Xp[g][order] for g in gw_idx]) if gw_idx else np.zeros((0, nd, L))
    pdom = np.isfinite(plac) & dom["gw"][None] if gw_idx else np.zeros((0, nd, L), bool)
    shared = {"tensor": (T.path, T.off, T.shape), "B": grid.B, "order": order, "starts": starts, "wt": wt,
              "use": lab, "x": xo, "covs": covs_o, "dom": dom, "relabel": relabel, "xperm": xperm, "plac": plac,
              "pdom": pdom, "x_idx": int(x_idx)}
    skey2 = sha([want, exposure, covsets, xo, [covs_o[c] for c in covs_o], relabel, xperm, plac, a.chunk,
                 MAIN_KEYS, CS_KEYS, [MIN_ROWS, MIN_LINES_GROUP, MIN_DRUGS], CACHE_VERSION])[:16]
    sroot = os.path.join(cdir, "screen")
    for d_ in glob.glob(os.path.join(sroot, "*")):
        if os.path.basename(d_) != skey2:
            shutil.rmtree(d_, ignore_errors=True)
    shared["sdir"] = os.path.join(sroot, skey2)
    os.makedirs(shared["sdir"], exist_ok=True)
    chunks = [(i, g0, min(T.G, g0 + a.chunk)) for i, g0 in enumerate(range(0, T.G, a.chunk))]
    with stage("(C) genome-wide screen", info):
        run_screen(shared, chunks, a.workers)
        S = assemble(shared["sdir"], chunks)
    info["screen"] = {"key": skey2, "chunks": len(chunks), "workers": a.workers, "worker_peak_rss_gb": S["worker_peak_gb"]}
    ck.add("screen chunks assembled (gene chunks x genes)", len(chunks), T.G,
           "worker count and memory in run_info.json (the tables do not depend on them)")
    G = T.G
    gi_ = np.arange(G)
    tested = S["main_tested"].astype(bool) & (gi_ != x_idx)
    dfm = S["main_df"]
    sym = gdf["symbol"].astype(str).to_numpy()
    SG = pd.DataFrame({"idx": gi_, "symbol": sym, "tested": tested})
    for k_ in MAIN_KEYS:
        if k_ != "tested":
            SG[k_] = S[f"main_{k_}"]
    SG.loc[x_idx, "note"] = "the exposure (not an outcome of its own fit)"
    for est in ("common", "diff"):
        SG[f"q_{est}"] = bh(np.where(tested, SG[f"p_{est}"], np.nan))
    rlt, rlok = S["rl_t_diff"].astype(float), S["rl_tested"] & tested[None]
    SG["p_label_pooled_diff"] = pooled_null_p(SG["t_diff"].to_numpy(), tested, rlt, rlok)
    SG["q_label_diff"] = bh(SG["p_label_pooled_diff"].to_numpy())
    with quiet():
        SG["p_label_own_diff"] = np.where(tested, (1 + (np.abs(rlt) >= np.abs(SG["t_diff"].to_numpy())[None] - 1e-12)
                                                   .sum(axis=0)) / (1 + rlt.shape[0]), np.nan) if rlt.shape[0] else np.nan
    xpc, xpd, xpok = S["xp_t_common"].astype(float), S["xp_t_diff"].astype(float), S["xp_tested"] & tested[None]
    SG["p_xperm_pooled_common"] = pooled_null_p(SG["t_common"].to_numpy(), tested, xpc, xpok)
    SG["q_xperm_common"] = bh(SG["p_xperm_pooled_common"].to_numpy())
    SG["p_xperm_pooled_diff"] = pooled_null_p(SG["t_diff"].to_numpy(), tested, xpd, xpok)
    plt_c, plt_d, plok = S["pl_t_common"].astype(float), S["pl_t_diff"].astype(float), S["pl_tested"]
    for fam in ("expression", "response"):
        jj = np.array([gw_pos[int(g)] for g in gwp.loc[gwp["family"] == fam, "idx"]], dtype=np.int64)
        for est, tn in (("common", plt_c), ("diff", plt_d)):
            v = np.where(plok[jj], tn[jj], np.nan)
            with quiet():
                SG[f"placebo_pct_{est}_{fam}"] = np.where(
                    tested, np.nanmean(np.where(np.isfinite(v), v < SG[f"t_{est}"].to_numpy()[None], np.nan), axis=0)
                    if len(jj) else np.nan, np.nan)
    for cs in covsets:
        if cs == "gw":
            continue
        for k_ in ("b_common", "diff", "p_common", "p_diff"):
            SG[f"{k_}_{cs}"] = S[f"cs_{cs}_{k_}"]
    inset = {r["name"]: np.isin(gi_, r["members"]) for r in reg}
    SG["in_P"], SG["in_P_down"] = inset["P53PROG_UP"], inset["P53PROG_DOWN"]
    prog_of = np.full(G, "", dtype=object)
    for r in reg:
        if r["role"].startswith("program"):
            prog_of[r["members"]] = r["name"]
    SG["atlas_program"] = prog_of
    for r in reg:
        if r["role"] == "overlay":
            SG[r["name"]] = inset[r["name"]]
    SG["placebo_family"] = ""
    for _, r in gwp.iterrows():
        g = int(r["idx"])
        SG.loc[g, "placebo_family"] = "; ".join(x_ for x_ in [SG.at[g, "placebo_family"],
                                                             f"{r['family']} (genome-wide)"] if x_)
    ann = optional("sibling annotations", lambda: sibling_annotations(sib, exposure, gdf, ck), ck)
    if ann is not None and len(ann.columns):
        for c in ann.columns:
            SG[c] = ann[c].to_numpy()

    # ---------------------------------------------------------------- calibration
    n_obs_c, lam_c = gw_count(SG["t_common"].to_numpy(), tested, dfm)
    n_obs_d, lam_d = gw_count(SG["t_diff"].to_numpy(), tested, dfm)
    sets_cam = [r for r in reg if r["tested_as_set"]]
    cam_rows = []

    def camera_all():
        sums, nbad = members_pass(T, grid, order, shared, [r["members"] for r in sets_cam], tested, a.chunk)
        rows = []
        for j, r in enumerate(sets_cam):
            for est, null in (("diff", (rlt, rlok)), ("common", None)):       # no shuffle null for a set (README)
                tt = SG[f"t_{est}"].to_numpy()
                res = camera_test(tt, tested, r["members"], {k_: v[j] for k_, v in sums[est].items()},
                                  {k_: S[f"cam_{est}_{k_}"] for k_ in ("d", "l", "twd", "twl", "twi")},
                                  int(S[f"cam_{est}_nbad"]), null)
                if res is not None:
                    rows.append({"set": r["name"], "role": r["role"], "estimate": est,
                                 "null": "TP53 relabellings" if est == "diff" else
                                 "none (p_set_camera is the test; within-cell shuffles are no null for a set)"} | res)
        return rows
    with stage("(C) camera-style set tests", info):
        cam_rows = optional("camera-style set tests", camera_all, ck, []) or []
    CT = pd.DataFrame(cam_rows)
    CT.to_csv(os.path.join(tab, "c_set_tests.csv"), index=False, float_format="%.6g")
    pmem = reg[0]["members"]

    def cam_stat(t_, ok_):
        inS = np.isin(gi_, pmem) & ok_ & np.isfinite(t_)
        rs = ok_ & np.isfinite(t_) & ~inS
        return float(t_[inS].mean() - t_[rs].mean()) if inS.sum() >= 2 and rs.sum() >= 2 else np.nan
    crow = [{"kind": "observed", "replicate": 0, "gene": exposure, "N_q01_common": n_obs_c, "N_q01_diff": n_obs_d,
             "lambda_common": lam_c, "lambda_diff": lam_d,
             "camera_stat_P53PROG_UP_diff": cam_stat(SG["t_diff"].to_numpy(), tested),
             "camera_stat_P53PROG_UP_common": cam_stat(SG["t_common"].to_numpy(), tested)}]
    Nrl = []
    for b in range(rlt.shape[0]):
        n_, l_ = gw_count(rlt[b], rlok[b], dfm)
        Nrl.append(n_)
        crow.append({"kind": "tp53_relabelling", "replicate": b + 1, "N_q01_diff": n_, "lambda_diff": l_,
                     "camera_stat_P53PROG_UP_diff": cam_stat(rlt[b], rlok[b]),
                     "note": "common slope not given: a relabelling keeps the within-line association (not a null)"})
    Nxc, Nxd = [], []
    for b in range(xpc.shape[0]):
        nc_, lc_ = gw_count(xpc[b], xpok[b], dfm)
        nd_, ld_ = gw_count(xpd[b], xpok[b], dfm)
        Nxc.append(nc_)
        Nxd.append(nd_)
        crow.append({"kind": "exposure_shuffle", "replicate": b + 1, "N_q01_common": nc_, "N_q01_diff": nd_,
                     "lambda_common": lc_, "lambda_diff": ld_,
                     "camera_stat_P53PROG_UP_common": cam_stat(xpc[b], xpok[b]),
                     "camera_stat_P53PROG_UP_diff": cam_stat(xpd[b], xpok[b])})
    plc_N = {"expression": [], "response": []}
    for _i, r in gwp.iterrows():
        p = gw_pos[int(r["idx"])]
        okp = plok[p] & (gi_ != x_idx) & (gi_ != int(r["idx"]))
        nc_, lc_ = gw_count(plt_c[p], okp, dfm)
        nd_, ld_ = gw_count(plt_d[p], okp, dfm)
        plc_N[r["family"]].append((nc_, nd_, lc_, ld_))
        crow.append({"kind": f"placebo_{r['family']}", "replicate": int(r["rank"]), "gene": r["symbol"],
                     "N_q01_common": nc_, "N_q01_diff": nd_, "lambda_common": lc_, "lambda_diff": ld_,
                     "note": "its own gene and the exposure left out"})

    def pcount(obs, nul):
        return (1 + sum(v >= obs for v in nul)) / (1 + len(nul)) if len(nul) else np.nan
    summ = {"p_count_diff_vs_relabelling": pcount(n_obs_d, Nrl), "p_count_common_vs_shuffles": pcount(n_obs_c, Nxc),
            "p_count_diff_vs_shuffles": pcount(n_obs_d, Nxd)}
    for k_, v in summ.items():
        crow.append({"kind": "p_count", "gene": k_, "value": v})
    for fam, vals in plc_N.items():
        if vals:
            arr = np.array(vals, float)
            for j, nm in enumerate(("N_q01_common", "N_q01_diff", "lambda_common", "lambda_diff")):
                obs = [n_obs_c, n_obs_d, lam_c, lam_d][j]
                crow.append({"kind": f"rank among placebo_{fam}", "gene": nm, "value": obs,
                             "note": f"{int((arr[:, j] >= obs).sum())} of {len(arr)} placebos at or above the "
                                     f"exposure; placebo median {np.nanmedian(arr[:, j]):.3g}"})
    CAL = pd.DataFrame(crow)
    CAL.to_csv(os.path.join(tab, "c_calibration.csv"), index=False, float_format="%.6g")
    SG.to_csv(os.path.join(tab, "c_screen_genes.csv.gz"), index=False, float_format="%.6g", compression=GZ)
    top = pd.concat([SG[tested].assign(rank_by="|t_common|", _k=SG["t_common"].abs()).nlargest(200, "_k"),
                     SG[tested].assign(rank_by="|t_diff|", _k=SG["t_diff"].abs()).nlargest(200, "_k")])
    top.drop(columns="_k").to_csv(os.path.join(tab, "c_screen_top.csv"), index=False, float_format="%.6g")
    log(f"(C) screen: {int(tested.sum())} genes tested; q < 0.1: common {n_obs_c} (lambda {lam_c:.2f}; shuffles "
        f"{Nxc}), diff {n_obs_d} (lambda {lam_d:.2f}; relabellings {Nrl})")

    # engine vs two_way on real genes
    def eng():
        cand = np.flatnonzero(tested)
        pick = np.sort(np.random.default_rng([SEED, 9]).choice(cand, min(20, len(cand)), replace=False))
        worst, nr = engine_check(T, grid, order, shared, pick, [tabs[c] for c in covsets["gw"]], wt)
        ck.add("screen engine vs two_way.Design + many_diffs + fit (ddxg, gw) on 20 tested genes: max relative diff",
               max(worst.values()) if worst else np.nan, len(pick),
               "; ".join(f"{k_} {v:.1e}" for k_, v in worst.items()) + f"; n_rows differ in {nr} genes")
    optional("engine check", eng, ck)

    # ---------------------------------------------------------------- (D) programs vs the exposure
    def dtab():
        scores = {}
        pde = os.path.join(tab, "d_programs", "program_drug_effects.parquet")
        md = pd.read_parquet(pde) if os.path.exists(pde) else None
        for r in reg:
            if not r["tested_as_set"]:
                continue
            if r["name"].startswith("PROG_") and md is not None:
                g = md[md["program"] == r["name"][5:]]
                scores[r["name"]] = g["score_z"].to_numpy(float) if len(g) == nd else np.full(nd, np.nan)
            else:
                with quiet():
                    scores[r["name"]] = A.robust_z(np.nanmean(ddz[:, r["members"]].astype(float), axis=1))
        ac = across_dd(fx, keep, ddz_x, scores, a.d_perm, np.random.default_rng([SEED, 8]))
        rows = []
        for r in reg:
            if r["name"] not in ac:
                continue
            row = {"set": r["name"], "role": r["role"], "n_genes": r["n"], "source": r["source"]} | ac[r["name"]]
            pm = PMall[(PMall["readout"] == r["name"]) & (PMall["fe"] == "ddxg") & (PMall["covset"] == "gw")
                       & (PMall["variant"] == "all")]
            if len(pm):
                q_ = pm.iloc[0]
                row.update({"b_common_within": q_["b_common"], "p_common_twoway": q_["p_common_twoway"],
                            "diff_within": q_["diff"], "p_diff_twoway": q_["p_diff_twoway"],
                            "p_diff_tp53_label_perm": q_.get("p_diff_tp53_label_perm", np.nan)})
            for est in ("common", "diff"):
                h = CT[(CT["set"] == r["name"]) & (CT["estimate"] == est)] if len(CT) else []
                row[f"camera_t_{est}"] = h.iloc[0]["t"] if len(h) else np.nan
                row[f"camera_p_{est}"] = h.iloc[0]["p_set_camera"] if len(h) else np.nan
            rows.append(row)
        Dt = pd.DataFrame(rows)
        pr_ = Dt["role"].astype(str).str.startswith("program")
        for col, pc in (("q_across_dd", "p_across_dd"), ("q_common_within", "p_common_twoway"),
                        ("q_diff_within", "p_diff_twoway")):
            Dt[col] = np.nan
            if pc in Dt and pr_.any():
                Dt.loc[pr_, col] = bh(Dt.loc[pr_, pc].to_numpy(float))
        return Dt
    with stage("(D) programs vs the exposure", info):
        DT = optional("(D) programs vs the exposure", dtab, ck)
    if DT is not None:
        DT.to_csv(os.path.join(tab, "d_program_vs_exposure.csv"), index=False, float_format="%.6g")

    # ---------------------------------------------------------------- (B) tables and overlays
    Dd, Gt, PG, ST, FS = b_tables(B_, grid, fx, gdf, x_idx, ddz_x, UFt, sib, data, sym2idx, overlays)
    Dd.to_csv(os.path.join(tab, "b_drugdose_p53_activation.csv"), index=False, float_format="%.6g")
    Gt.to_csv(os.path.join(tab, "b_p53_program_genes.csv.gz"), index=False, float_format="%.6g", compression=GZ)
    PG.to_csv(os.path.join(tab, "b_p53_program.csv"), index=False, float_format="%.6g")
    ST.to_csv(os.path.join(tab, "b_program_stability.csv"), index=False, float_format="%.6g")
    FS.to_csv(os.path.join(tab, "b_feature_specificity.csv"), index=False, float_format="%.6g")
    OV = optional("overlay table (b_overlays.csv)", lambda: b_overlay_table(B_, gdf, overlays, x_idx, Dd), ck)
    if OV is not None:
        OV.to_csv(os.path.join(tab, "b_overlays.csv"), index=False, float_format="%.6g")
    chk = Dd[Dd["TP53_explains_best"].notna()]
    B_["spec_text"] = (f"TP53 status explains the divergence best in {int(chk['TP53_explains_best'].astype(bool).sum())}"
                       f" of {len(chk)} checked S1/S2 drug-doses" if len(chk) else "not computed") + (
        f"; P's selectivity: TP53 z {B_['sel_tp53']:.1f} vs the best other grouping "
        f"{max([v for v, s_ in zip(B_['sel_feat'], UFt[2]) if not s_] or [np.nan]):.1f}" if "sel_tp53" in B_ else "")

    # ---------------------------------------------------------------- key results
    kr = []

    def add(section, role, what, fe="", covset="", n=np.nan, est=np.nan, lo=np.nan, hi=np.nan, p2=np.nan,
            pl=np.nan, q=np.nan, detail=""):
        kr.append({"section": section, "role": role, "what": what, "fe": fe, "covset": covset, "n": n,
                   "estimate": est, "ci_lo": lo, "ci_hi": hi, "p_twoway": p2, "p_label_perm": pl, "q": q,
                   "detail": detail})
    fb_of = {"P53PROG_UP": B_["small"], "P53PROG_UP_cf": B_["small"] or any(B_["small_f"]),
             "P53PROG_UP_noX": B_["small_noX"], "P53PROG_DOWN": B_["small_d"],
             "P53PROG_DOWN_cf": B_["small_d"] or any(B_["small_df"])}
    fb_of.update({f"P53PROG_UP_f{f}": B_["small_f"][f] for f in range(B_["F"])})

    def fb_note(readout):
        """The detail's prefix for an outcome built from a fallback program (or from S2 on a fallback S1)."""
        n_ = []
        if fb_of.get(readout, False):
            n_.append(f"FALLBACK: built from a program with fewer than {PROG_MIN} genes at q < 0.05 (the top "
                      f"{PROG_FALLBACK} by z); exploratory")
        if B_["s1_fallback"]:
            n_.append("S1 FALLBACK (no drug-dose at permutation FDR < 0.05): S2 and the program are exploratory")
        return "; ".join(n_) + ("; " if n_ else "")
    for _, r in PMall.iterrows():
        if not str(r["readout"]).startswith("P53PROG") or r["role"] == "program":
            continue
        add("C program-level", r["role"], f"{r['readout']} [{r['variant']} drug-doses]: b_WT - b_alt", r["fe"],
            r["covset"], r["n_rows"], r["diff"], r["ci_diff_lo_twoway"], r["ci_diff_hi_twoway"], r["p_diff_twoway"],
            r.get("p_diff_tp53_label_perm", np.nan), r.get("p_holm_covsets_twoway", np.nan),
            fb_note(r["readout"]) + (
                f"b_WT {r['b_WT']:+.4f} (two-way p {r['p_WT_twoway']:.3g}); b_alt {r['b_alt']:+.4f} (two-way p "
                f"{r['p_alt_twoway']:.3g}); MDE (80%) {r.get('mde_diff_80', np.nan):.3g}; {r['n_drugdoses']} "
                f"drug-doses, {r['n_drugs']} compounds, {r['n_lines_WT']} WT + {r['n_lines_alt']} altered lines; q = "
                "Holm over the covariate sets" if r["role"] == "primary" or r["covset"] != "gw" else
                f"b_WT {r['b_WT']:+.4f}; b_alt {r['b_alt']:+.4f}; {r['n_drugdoses']} drug-doses"))
        if r["role"] == "primary":
            add("C program-level", "secondary", f"{r['readout']} [all drug-doses]: common slope b_common", r["fe"],
                r["covset"], r["n_rows"], r["b_common"], r["ci_common_lo_twoway"], r["ci_common_hi_twoway"],
                r["p_common_twoway"], np.nan, np.nan,
                fb_note(r["readout"]) + "conservative two-way p; no permutation p (a TP53 relabelling leaves the "
                "common slope unchanged, and within-cell shuffles break the exposure's line-level structure)")
    for fam, lab_ in (("response", "placebo (response-matched)"), ("expression", "placebo (expression-matched)")):
        if fam in plac_summary:
            (frd, ped, nn), (frc, pec) = plac_summary[fam]["diff"], plac_summary[fam]["common"][:2]
            add("C placebos", "check", f"{lab_}: primary model with each placebo as the exposure", "ddxg", "gw", nn,
                frd, detail=f"the exposure's diff t is above {100 * frd:.0f}% of {nn} placebo t (two-sided "
                f"empirical p {ped:.3g}); common-slope t above {100 * frc:.0f}% (p {pec:.3g})")
    add("C screen", "screen", "screen: common slope, genes at q < 0.1", "ddxg", "gw", int(tested.sum()), n_obs_c,
        p2=summ["p_count_common_vs_shuffles"],
        detail=f"lambda {lam_c:.2f}; within-cell exposure shuffles: N {Nxc}, p_count {summ['p_count_common_vs_shuffles']:.3g}"
        + "".join(f"; {fam} placebos: N {[v[0] for v in vals]}" for fam, vals in plc_N.items() if vals))
    add("C screen", "screen", "screen: b_WT - b_alt, genes at q < 0.1", "ddxg", "gw", int(tested.sum()), n_obs_d,
        p2=summ["p_count_diff_vs_relabelling"],
        detail=f"lambda {lam_d:.2f}; TP53 relabellings: N {Nrl}, p_count {summ['p_count_diff_vs_relabelling']:.3g}; "
        f"exposure shuffles: N {Nxd}" + "".join(f"; {fam} placebos: N {[v[1] for v in vals]}"
                                                for fam, vals in plc_N.items() if vals))
    tc = SG[tested].nsmallest(10, "p_common")
    top_common = ", ".join(f"{r['symbol']} ({r['b_common']:+.3f}, q {r['q_common']:.2g}"
                           + (f", {r['dog_class']}" if "dog_class" in SG and isinstance(r.get("dog_class"), str) else "")
                           + ")" for _, r in tc.iterrows())
    add("C screen", "screen", "screen: strongest common slopes", "ddxg", "gw", detail=top_common)
    if len(CT):
        for _, r in CT[CT["set"].isin(["P53PROG_UP", "P53PROG_DOWN", "OVERLAY_P53_ACTIVITY21"])].iterrows():
            dif = r["estimate"] == "diff"
            add("C set test", "overlay" if r["role"] == "overlay" else "secondary",
                f"{r['set']} genes as a set (camera, {r['estimate']})", "ddxg", "gw", r["m1"], r["stat"],
                p2=r["p_set_camera"], pl=r.get("p_null_calibrated", np.nan) if dif else np.nan,
                detail=(fb_note(r["set"]) if r["set"].startswith("P53PROG") else "")
                + f"mean t {r['mean_t_set']:+.2f} vs {r['mean_t_rest']:+.2f}; camera p {r['p_set_camera']:.3g} "
                  f"(VIF {r['vif_effective']:.2f} from {r['vif_from']}; genes treated as independent: p "
                  f"{r['p_set_independent']:.3g}); "
                + (f"calibrated by the TP53 relabellings: p {r.get('p_null_calibrated', np.nan):.3g} (column "
                   "p_label_perm)" if dif else "no permutation p: within-cell exposure shuffles break the exposure's "
                   "line-level structure, so they are no null for a set statistic; the camera p is the test"))
    add("B program", "secondary", "Tahoe p53 program: sizes", n=len(B_["P"]), est=len(B_["S2"]),
        detail=f"S1 {len(B_['S1'])} drug-doses ({B_['n_S1_q']} at permutation FDR < 0.05; null max "
               f"{max(B_['null_S1'] or [np.nan])}){' FALLBACK' if B_['s1_fallback'] else ''}; S2 {len(B_['S2'])} "
               f"drug-doses ({B_['n_S2_q']} at permutation FDR < 0.05; null max {max(B_['null_S2'] or [np.nan])}; "
               f"{B_['S2_names']}); P {len(B_['P'])} genes{' (FALLBACK)' if B_['small'] else ''}, P-down "
               f"{len(B_['Pd'])}{' (FALLBACK)' if B_['small_d'] else ''}; null program sizes max "
               f"{max(B_['null_sizes'] or [np.nan])}; flags: {'; '.join(B_['flags']) or 'none'}; {B_['spec_text']}")
    if OV is not None and len(OV):
        o = OV[(OV["overlay"] == "OVERLAY_P53_ACTIVITY21") & (OV["program"] == "P")]
        if len(o):
            o = o.iloc[0]
            add("B overlay", "overlay", "21-gene P53_ACTIVITY (curated) vs the Tahoe program P", n=o["n_in_atlas_tested"],
                est=o["n_overlap"], p2=o["p_hypergeometric_enrichment"],
                detail=f"{o['n_overlap']} of {o['n_in_atlas_tested']} in P ({o['program_size']} genes; expected "
                       f"{o['expected_overlap']:.2f}); median percentile of their program z "
                       f"{o['median_percentile_program_z']:.1f}; {o['overlap_genes']}")
    for _, r in PMall[PMall["readout"] == "OVERLAY_P53_ACTIVITY21"].iterrows():
        add("C overlay", "overlay", f"OVERLAY_P53_ACTIVITY21 [{r['covset']}]: b_WT - b_alt (bridge to two_way's "
            "P53_SCORE)", r["fe"], r["covset"], r["n_rows"], r["diff"], r["ci_diff_lo_twoway"], r["ci_diff_hi_twoway"],
            r["p_diff_twoway"], r.get("p_diff_tp53_label_perm", np.nan), detail="two_way's primary (P53_SCORE, full) "
            "is the comparison; resp_bg replaces two_way's panel-based bg_abs_r2"
            + (f", and the {int((~lab).sum())} line(s) without a TP53 group are left out here (two_way counts them as "
               "altered)" if (~lab).any() else ""))
    tw_kr = os.path.join(sib, "two_way", "tables", "key_results.csv")
    if os.path.exists(tw_kr):
        t_ = pd.read_csv(tw_kr)
        for v in ("i_all", "ii_active", "ii_p53"):
            h = t_[(t_["what"].astype(str).str.startswith(f"P53_SCORE [{v}, full]")) & (t_["fe"] == "ddxg")]
            if len(h):
                h = h.iloc[0]
                add("C overlay", "overlay", f"two_way P53_SCORE [{v}, full] (sibling table, for comparison)", "ddxg",
                    "full", h["n"], h["estimate"], h["ci_lo"], h["ci_hi"], h["p_twoway"], h["p_label_perm"])
    moving = "not computed"
    if DT is not None and len(DT):
        pr_ = DT[DT["role"].astype(str).str.startswith("program")]
        hits = pr_[(pr_["q_common_within"] < Q_REP) | (pr_["q_across_dd"] < Q_REP)]
        moving = (f"{len(hits)} of {len(pr_)} atlas programs track the exposure at q < 0.1 (within lines or across "
                  "drug-doses)" + (": " if len(hits) else ".") + "; ".join(f"{r['set']} (within b {r.get('b_common_within', np.nan):+.3f}, q "
                                              f"{r['q_common_within']:.2g}; across r {r['r_across_dd']:+.2f}, q "
                                              f"{r['q_across_dd']:.2g})" for _, r in hits.head(12).iterrows()))
        add("D programs", "screen", "atlas programs tracking the exposure (q < 0.1)", n=len(pr_), est=len(hits),
            detail=moving)
    for _, r in ck.frame().iterrows():
        if str(r["check"]).startswith(("tensor W1", "tensor vs panel per", "screen engine", "plates written",
                                       "finite cells")):
            add("A/C check", "check", r["check"], n=r["n"], est=r["value"], detail=str(r["note"]))
    add("E", "context", "single cells (TRIM72-detection-stratified pseudobulk): not run", detail=E_NOTE.replace("\n", " "))
    KR = pd.DataFrame(kr)
    KR = pd.concat([KR[KR["role"] == "primary"], KR[KR["role"] != "primary"]], ignore_index=True)
    KR.to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.6g")
    ck.frame().to_csv(os.path.join(tab, "checks.csv"), index=False)
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    special = "not computed (no placebo fits)"
    if "response" in plac_summary:
        (frd, ped, nn) = plac_summary["response"]["diff"]
        vals = np.array(plc_N.get("response") or [], float).reshape(-1, 4)
        special = (f"in the primary model the exposure's b_WT - b_alt t is above {100 * frd:.0f}% of {nn} placebo t "
                   f"(two-sided empirical p {ped:.3g})")
        if len(vals):
            special += (f"; genome-wide, {int((vals[:, 0] >= n_obs_c).sum())} of {len(vals)} placebos have at least as "
                        f"many common-slope genes at q < 0.1 ({n_obs_c} for the exposure) and "
                        f"{int((vals[:, 1] >= n_obs_d).sum())} at least as many b_WT - b_alt genes ({n_obs_d}); "
                        f"lambda common {lam_c:.2f} vs placebo median {np.nanmedian(vals[:, 2]):.2f}")
        special += "."
    write_findings(os.path.join(out, "GENOME_WIDE.md"), exposure, KR, info, B_, int(tested.sum()), top_common, moving,
                   special)
    info.update({"peak_rss_gb_parent": round(UT.peak_gb(), 3), "peak_rss_how": UT._MEM_PEAK["how"],
                 "peak_rss_gb_workers": round(S["worker_peak_gb"], 3), "wall_seconds": round(time.time() - t_all, 1),
                 "genes_tested": int(tested.sum()), "cache_manifest_sha1": sha(want),
                 "date": time.strftime("%Y-%m-%d"),
                 "B": {"S1": len(B_["S1"]), "S2": len(B_["S2"]), "P": len(B_["P"]), "P_down": len(B_["Pd"]),
                       "S1_at_fdr": B_["n_S1_q"], "S2_at_fdr": B_["n_S2_q"], "null_S1_sizes": B_["null_S1"],
                       "null_S2_sizes": B_["null_S2"], "P_fallback": bool(B_["small"]),
                       "P_down_fallback": bool(B_["small_d"]),
                       "F_eff": B_["F"], "fold_status": B_["fold_status"], "flags": B_["flags"],
                       "null_sizes": B_["null_sizes"], "signature_N": B_["N_sig"]},
                 "placebos": {"genome_wide_per_family": n_gw_f, "program_level_per_family": n_set_f}})
    with open(os.path.join(tab, "run_info.json"), "w", encoding="utf-8") as fh:
        json.dump(info, fh, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
    pr = KR.iloc[0]
    log(f"PRIMARY {pr['what']} [fe {pr['fe']}, {pr['covset']}]: {pr['estimate']:+.4f} (95% CI {pr['ci_lo']:+.4f} to "
        f"{pr['ci_hi']:+.4f}; conservative two-way p {pr['p_twoway']:.3g}; label-permutation p "
        f"{pr['p_label_perm']:.3g})")
    log(f"tables written to {tab}; peak RSS {UT.peak_gb():.2f} GB (workers {S['worker_peak_gb']:.2f} GB); wall "
        f"{time.time() - t_all:.0f} s")


if __name__ == "__main__":
    main()
