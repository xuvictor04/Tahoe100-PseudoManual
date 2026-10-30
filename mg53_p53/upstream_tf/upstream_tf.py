#!/usr/bin/env python3
"""Upstream of TRIM72 (MG53), U1/U2: which transcription-factor (TF) activities track TRIM72, and which cell-line
properties predict its untreated level and its inducibility. Tahoe-100M only (no new data), method-v3 effects.

Every result is an ASSOCIATION in mRNA. Tahoe has no TF or MG53 perturbation; a TF's activity is inferred from the
mRNA of its targets, and a TF whose activity tracks TRIM72 may be a co-responder to the same drugs, not a regulator.

Regulons. CollecTRI (signed TF -> target network) from the OmniPath web service, processed as decoupler's
get_collectri: the COMPLEX sources made only of AP-1 (JUN, JUNB, JUND, FOS, FOSB, FOSL1, FOSL2) or only of NF-kB (REL,
RELA, RELB, NFKB1, NFKB2) members (dimers and homodimers) are merged into AP1 and NFKB; the single-protein sources
(JUN, FOS, RELA, ...) stay TFs of their own; sign -1 where OmniPath's consensus says inhibition (else its
is_inhibition), +1 otherwise (CollecTRI's default activation). DoRothEA A-C (OmniPath) is a sensitivity source. TRIM72
and every gene within 200 kb of it (Ensembl GRCh38 region 16:31014017-31431537: FUS, PYCARD-AS1, PYCARD, ITGAM, ...)
are left out of every regulon and of the gene universe; the TF -> TRIM72 / locus edges the databases list are reported
first. CollecTRI is required: if it can be neither downloaded nor found in cache/external, the step stops before the
pseudobulk pass with a message saying where to put the file (no fallback). Without DoRothEA the DoRothEA rows are left
out; without a TP53 regulon (A3 controls) the positive control is skipped and checks.csv says so.
Activity = univariate linear model (ULM, decoupler's default): per sample, the gene vector regressed on the TF's signed
weights (0 = not a target) over the sample's gene universe. A TF needs >= 5 targets in the universe. Second method
(drug-dose level): the mean of the signed target z (weight x z, averaged over the TF's targets with a z).

(a) A1 per drug-dose (1,086 drug-doses: unreliable-plate-only and position-not-correctable ones out): ULM t on the atlas
    DD_z (primary), mean signed target z, ULM slope on DD_lfc, DoRothEA ULM t, and the TF's own mRNA z. Each vs TRIM72 z
    (own), TRIM72_rt z (two_way's readthrough correction: per (well, line) TRIM72 r2 minus its within-drug-dose-and-line
    fit on FUS and PYCARD-AS1 r2, then the atlas's well median, robust z and Stouffer steps) and TRIM72 z with FUS and
    PYCARD-AS1 z partialled (rt_across, the strict version). Partial Pearson r: raw; covariates (global activity: n
    significant genes, RMS z, cell loss, UMI and genes per cell, composition, S / G2M / proteasome z); top 3 and top 10
    PC scores of the standardised DD_z gene matrix. Drug-block permutation null (whole drugs swapped, B = 1000) ->
    calibrated p, BH over TFs; 95% CI = r +- 1.96 x the larger of the drug-block null SD and the leave-one-drug-out
    jackknife SE; where TRIM72's r sits among 300 expression-matched random genes' r with the same TF (specificity).
    Method-robust rank: the worse of a TF's ranks under ULM t and mean target z. Regulon-overlap control: each TF with
    its AP-1 / ATF3 targets and immediate-early genes removed, and with ATF3, PMAIP1, DDIT3 z, an IEG score and AP1
    activity partialled. Plate-batch split: the same association in drug-doses on the high-TRIM72 plates (1-3) only and
    on the low-TRIM72 plates (4-12) only.
    A2 within lines: per (drug-dose, line) ULM slope of each TF from the pseudobulk (method-v3 r2 of every atlas gene,
    rebuilt plate by plate: plate drug-well baseline per line, composition shift, the atlas's own position correction;
    checked against atlas W1) vs TRIM72 r2 (own, readthrough-corrected), two-way fixed effects (drug-dose + line) with
    DD_beta, DD_A, S, G2M and mean |r2| (x TP53 group) as covariates; drug-cluster and two-way (drug, line) cluster SE;
    the slope in TP53-WT minus altered lines (line-cluster SE). BH over TFs. Noise ceiling: TRIM72's within-line r with
    single co-responding genes (FOS, EGR1, JUN, ATF3, FUS, PMAIP1, DDIT3) under the same model.
    A3 positive control: TP53 activity (MDM2 and CDKN1A left out of its regulon) vs MDM2 / CDKN1A across drug-doses and
    within lines (WT vs altered lines), and vs the panel's P53_ACTIVITY z.  A4 muscle / promoter TFs (MyoD, myogenin,
    MEF2: the literature's TRIM72 promoter TFs): mRNA level, regulon activity and its association with TRIM72.
(b) Line features (50 lines): TRIM72 untreated level (DMSO wells, observed / expected counts with the expected count
    from the plate's median expressing line: within-plate standardised, reliable plates pooled) and inducibility (per-line
    TRIM72 r2 under idarubicin 5 uM and homoharringtonine 5 uM, two wells each; their mean; each adjusted for the
    untreated level) vs TP53 group, lineage, driver genes (cell_line_metadata, 4 to 46 lines), baseline TF activities
    (ULM t on DMSO within-plate relative expression), FUS / PYCARD-AS1 untreated level. Spearman / mean difference,
    label-permutation calibrated p, organ-adjusted versions, BH within each outcome (all families; also within outcome x
    family and over every line test), MDE (small n).

    python3 upstream_tf.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute] [--offline]
                           [--perm 1000] [--line-perm 10000] [--quick]

Reads <data>/atlas/effects, <data>/atlas/pseudobulk (one streamed pass of 20 GB: 3.4 min with an empty page cache on a
~100 MB/s disk, 2.2 min with half the files cached, ~11 min at 30 MB/s; peak RSS 1.5 GB), <data>/gene_panel
(results/, well_line.parquet for a check), <data>/metadata. Downloads (once, into cache/external; curl, or Python's
urllib when curl is missing, both through $HTTPS_PROXY and with the system / $SSL_CERT_FILE CA bundle): CollecTRI and
DoRothEA from omnipathdb.org, the TRIM72 region from rest.ensembl.org (fallback: the region's gene list in this file).
Tables to $MG53_OUT/tables (default <this folder>/tables), caches to $MG53_OUT/cache (the pass, ~200 MB, reused while
the regulons are unchanged). Whole run: 5-5.5 min from scratch, peak RSS 2.4 GiB (run_info.json records both; 4 CPUs).
numpy / pandas / scipy (+ pyarrow for
the parquet reads); psutil, when installed, only for memory reporting. Self-contained apart from the repo's
tahoe_atlas.py (the helpers it once imported from upstream_coregulation are copied below).
"""
import argparse
import contextlib
import glob
import hashlib
import json
import os
import shutil
import ssl
import subprocess
import sys
import time
import urllib.request
import warnings

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import sparse, stats  # noqa: E402

try:
    import resource  # noqa: E402  (POSIX only)
except ImportError:  # pragma: no cover  (Windows)
    resource = None
try:
    import psutil  # noqa: E402  (optional, memory reporting only)
except ImportError:
    psutil = None

sys.dont_write_bytecode = True        # no __pycache__ written next to tahoe_atlas.py
HERE = os.path.dirname(os.path.abspath(__file__))
MGDIR = os.path.dirname(HERE)
REPO = os.path.dirname(MGDIR)
if REPO not in sys.path:
    sys.path.insert(0, REPO)
import tahoe_atlas as A               # noqa: E402  (log_cpm, composition, robust_cols, loo_effect, FX)

GENE = "TRIM72"
SEED = 20261026
TMIN = 5                                                 # targets needed in the universe (decoupler's tmin)
Z80 = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)      # 2.80: MDE = Z80 x SE
AP1 = {"JUN", "JUNB", "JUND", "FOS", "FOSB", "FOSL1", "FOSL2"}
NFKB = {"REL", "RELA", "RELB", "NFKB1", "NFKB2"}
MUSCLE_TFS = ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2B", "MEF2C", "MEF2D", "SRF"]
P53_CTRL = ["MDM2", "CDKN1A"]
TP53_CTRL_TF = "TP53 (MDM2, CDKN1A out)"
TP53_ACT_TF = "TP53 activated targets (MDM2, CDKN1A out)"
CTRL_TFS = (TP53_CTRL_TF, TP53_ACT_TF)
SEL_EXTRA = ["FUS", "MDM2", "CDKN1A", "TP53", "ATF3", "PMAIP1", "FOS", "JUN", "EGR1", "DDIT3"]
EXTRA_SYMBOLS = ["PYCARD-AS1", "MYOD1", "MYOG", "MYF5", "MYF6", "MEF2B"]   # not in the atlas gene list
RAISERS = {"idarubicin_5": ("Idarubicin (hydrochloride)", 5.0), "homoharringtonine_5": ("Homoharringtonine", 5.0)}
COLLECTRI_URL = ("https://omnipathdb.org/interactions?datasets=collectri&genesymbols=yes&loops=yes&organisms=9606"
                 "&format=tsv")
DOROTHEA_URL = ("https://omnipathdb.org/interactions?datasets=dorothea&dorothea_levels=A,B,C&genesymbols=yes&loops=yes"
                "&organisms=9606&format=tsv&fields=dorothea_level")
REGION_URL = ("https://rest.ensembl.org/overlap/region/human/16:31014017-31431537?feature=gene;"
              "content-type=application/json")
# immediate-early genes for the regulon-overlap control (both names of CCN1 / CCN2; those in the atlas are used)
IEG = ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "IER2", "IER3", "IER5", "ATF3", "DUSP1", "NR4A1", "KLF6",
       "KLF4", "PPP1R15A", "GADD45B", "MYC", "ZFP36", "CCN1", "CYR61", "CCN2", "CTGF", "SERTAD1", "BTG2"]
MEDIATOR_GENES = ["ATF3", "PMAIP1", "DDIT3"]             # partialled (z) in the overlap control, with the IEG score + AP1
NOISE_GENES = ["FOS", "EGR1", "JUN", "ATF3", "FUS", "PMAIP1", "DDIT3"]   # within-line noise ceiling (single genes)
HIGH_PLATES = ("plate1", "plate2", "plate3", "plate14")  # TRIM72 untreated level ~10x higher than on plates 4-13
# Ensembl genes overlapping TRIM72 +- 200 kb (GRCh38; rest.ensembl.org overlap, Ensembl 116): the fallback when the
# REST service is down (gene ids only; no numbers)
LOCUS_FALLBACK = {"ENSG00000103496": "STX4", "ENSG00000299404": "", "ENSG00000260911": "", "ENSG00000232748": "",
                  "ENSG00000167394": "ZNF668", "ENSG00000261124": "", "ENSG00000167395": "ZNF646",
                  "ENSG00000151006": "PRSS53", "ENSG00000255439": "", "ENSG00000167397": "VKORC1",
                  "ENSG00000297437": "", "ENSG00000280160": "", "ENSG00000103507": "BCKDK", "ENSG00000103510": "KAT8",
                  "ENSG00000262766": "", "ENSG00000278133": "", "ENSG00000261385": "", "ENSG00000052344": "PRSS8",
                  "ENSG00000178226": "PRSS36", "ENSG00000263343": "", "ENSG00000262366": "NDUFA3P6",
                  "ENSG00000089280": "FUS", "ENSG00000260304": "", "ENSG00000261359": "PYCARD-AS1",
                  "ENSG00000103490": "PYCARD", "ENSG00000177238": "TRIM72", "ENSG00000169900": "PYDC1",
                  "ENSG00000310348": "", "ENSG00000169896": "ITGAM", "ENSG00000289930": "", "ENSG00000301315": "",
                  "ENSG00000140678": "ITGAX", "ENSG00000261245": "", "ENSG00000308290": "", "ENSG00000156886": "ITGAD",
                  "ENSG00000260757": "", "ENSG00000156885": "COX6A2", "ENSG00000277543": ""}
PASS_VERSION = "upstream_tf pass v1"
CHUNK = 256


@contextlib.contextmanager
def quiet():
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        yield


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


_MEM_PEAK = {"gb": 0.0, "how": "none"}


def peak_gb():
    """Peak resident memory of this process in GB (1024^3 bytes): getrusage's ru_maxrss (KiB on Linux / BSD, bytes on
    macOS) where the resource module exists, and psutil's current RSS (running maximum over the calls) when psutil is
    installed; the larger of the two. NaN when neither is available (e.g. Windows without psutil)."""
    vals = []
    if resource is not None:
        try:
            v = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            vals.append(("getrusage", v / 1024 ** 3 if sys.platform == "darwin" else v / 1024 ** 2))
        except (OSError, ValueError):
            pass
    if psutil is not None:
        try:
            vals.append(("psutil", psutil.Process().memory_info().rss / 1024 ** 3))
        except Exception:  # noqa: BLE001
            pass
    for how, v in vals:
        if v > _MEM_PEAK["gb"]:
            _MEM_PEAK["gb"], _MEM_PEAK["how"] = v, how
    return _MEM_PEAK["gb"] if vals or _MEM_PEAK["gb"] > 0 else float("nan")


# ============================================================================= helpers copied from upstream_coregulation
# (bh, download, drug_block_perms, corrected_effects: copied so that edits to that step cannot change this one)
def bh(p):
    p = np.asarray(p, dtype=float)
    q = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    pv = p[ok]
    n = pv.size
    if n == 0:
        return q
    o = np.argsort(pv)
    r = pv[o] * n / np.arange(1, n + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    out = np.empty(n)
    out[o] = np.minimum(r, 1)
    q[ok] = out
    return q


def _ssl_context():
    """The system CA store, plus the bundle named by $SSL_CERT_FILE / $REQUESTS_CA_BUNDLE / $CURL_CA_BUNDLE (e.g. a
    corporate or proxy CA) when set."""
    ctx = ssl.create_default_context()
    for v in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
        p = os.environ.get(v)
        if p and os.path.isfile(p):
            try:
                ctx.load_verify_locations(cafile=p)
            except (ssl.SSLError, OSError):
                pass
    return ctx


def _fetch_once(url, tmp, timeout, use_curl):
    """One attempt; returns '' on success, else the error text."""
    if use_curl:
        r = subprocess.run(["curl", "-sSfL", "-m", str(timeout), "-o", tmp, url], capture_output=True, text=True)
        return "" if r.returncode == 0 else ((r.stderr or "").strip()[-200:] or f"curl exit {r.returncode}")
    # urllib: ProxyHandler() reads $HTTPS_PROXY / $https_proxy and $NO_PROXY from the environment
    opener = urllib.request.build_opener(urllib.request.ProxyHandler(),
                                         urllib.request.HTTPSHandler(context=_ssl_context()))
    try:
        with opener.open(urllib.request.Request(url, headers={"User-Agent": "upstream_tf.py"}), timeout=timeout) as r, \
                open(tmp, "wb") as fh:
            shutil.copyfileobj(r, fh, 1 << 20)
        return ""
    except Exception as err:  # noqa: BLE001  (URLError, HTTPError, timeouts, SSL errors)
        return f"urllib: {err}"[:200]


def download(url, dest, timeout=300, tries=3, use_curl=None):
    """Download to dest via a temporary file, with curl when it is installed, else Python's urllib (both honour
    $HTTPS_PROXY; urllib uses the system CA store plus $SSL_CERT_FILE / $REQUESTS_CA_BUNDLE / $CURL_CA_BUNDLE). HTTP
    errors fail and are retried; an HTML page (a service error such as Ensembl's '503 Service Unavailable') is never
    saved as data."""
    if use_curl is None:
        use_curl = shutil.which("curl") is not None
    tmp = dest + ".part"
    err = ""
    for k in range(tries):
        err = _fetch_once(url, tmp, timeout, use_curl)
        if not err:
            with open(tmp, "rb") as fh:
                head = fh.read(512).lower()
            if b"<html" not in head and b"<!doctype html" not in head and b"service unavailable" not in head:
                os.replace(tmp, dest)
                return True
            err = "the server returned an HTML page instead of data"
        print(f"{time.strftime('%H:%M:%S')}   download failed ({err}); retry {k + 1}/{tries - 1}" if k + 1 < tries
              else f"{time.strftime('%H:%M:%S')}   download failed ({err})", flush=True)
        if k + 1 < tries:
            time.sleep(min(60, 10 * (k + 1)))
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def drug_block_perms(dd, B, rng):
    """B permutations of the drug-dose rows that move whole drugs: a drug's doses go together to another drug with
    the same set of doses (keeps the dose structure; drug-doses of one drug are not independent)."""
    sig = dd.groupby("drug")["conc"].apply(lambda s: tuple(sorted(s.round(3))))
    rows_of = {d: dd.index[dd["drug"] == d].to_numpy() for d in sig.index}
    conc_of = dd["conc"].round(3).to_dict()
    pos = {i: k for k, i in enumerate(dd.index)}
    perms = np.empty((B, len(dd)), dtype=np.int64)
    groups = {}
    for d, s in sig.items():
        groups.setdefault(s, []).append(d)
    for b in range(B):
        p = np.arange(len(dd))
        for s, drugs in groups.items():
            if len(drugs) < 2:
                continue
            shuf = rng.permutation(drugs)
            for src, dst in zip(drugs, shuf):        # rows of drug src get the values of drug dst
                for i in rows_of[src]:
                    j = next(j for j in rows_of[dst] if conc_of[j] == conc_of[i])
                    p[pos[i]] = pos[j]
        perms[b] = p
    return perms


def corrected_effects(fx, counts, tot, nc, expressed=None):
    """The atlas's per_line_columns steps (method v3) on counts (atlas wells x lines x C): plate drug-well
    baseline per line, composition shift, two-pass leave-drug-out position correction on the column's own
    well-level values; returns per (well, line) r2, well-level W1/W2, per-well z (robust over reliable drug wells),
    per drug-dose per-line means and Stouffer z. expressed (lines x C, bool): lines that do not express a column
    are left out (as the atlas's expr_mask). fx = the atlas's tahoe_atlas.FX (it sets A.MIN_CELLS from info.json)."""
    w = fx.wells
    Y = A.log_cpm(counts, tot, nc)
    if expressed is not None:
        Y[:, ~expressed] = np.nan
    S = A.composition_matrix(fx)
    r1 = np.full_like(Y, np.nan)
    for p in fx.plates:
        rows = np.flatnonzero((w["plate"] == p).to_numpy())
        drug = rows[fx.drug_w[rows]]
        base = np.nanmedian(Y[drug], axis=0)
        r1[rows] = Y[rows] - base[None] - S[rows][:, :, None]
    W1 = np.nanmedian(r1, axis=1)
    W1[np.isfinite(r1).sum(axis=1) < A.MIN_LINES] = np.nan
    slot, dname = w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object)
    f1 = w["plate_scale_pass1"].to_numpy(dtype=float)
    e1, _, _ = A.loo_effect(W1, slot, dname, fx.drug_w)
    c, s = A.robust_cols(W1 - e1, fx.ref_w)
    clean = np.abs((W1 - e1 - c) / (s * f1[:, None])) < A.POS_CLEAN_Z
    eff = A.loo_effect(W1, slot, dname, fx.drug_w, clean=clean)[0]
    W2 = W1 - eff
    r2 = np.where(np.isfinite(W1)[:, None, :], r1 - eff[:, None, :], np.nan)
    c2, s2 = A.robust_cols(W2, fx.ref_w)
    zw = (W2 - c2) / (s2 * w["plate_scale"].to_numpy(dtype=float)[:, None])
    nd = len(fx.dd)
    per = np.full((nd, r2.shape[1], r2.shape[2]), np.nan, dtype=np.float32)
    ddl = np.full((nd, r2.shape[2]), np.nan)
    ddz = np.full((nd, r2.shape[2]), np.nan)
    for d, ii in fx.wells_of_dd.items():
        if len(ii):
            per[d] = np.nanmean(r2[ii], axis=0)
            ddl[d] = np.nanmean(W2[ii], axis=0)
            ddz[d] = np.nansum(zw[ii], axis=0) / np.sqrt(np.isfinite(zw[ii]).sum(axis=0).clip(1))
    return r1, r2, W2, zw, per, ddl, ddz


class TW:
    """The fixed-effects helpers of two_way.py (copied, so that this step does not change when that one does)."""

    @staticmethod
    def npy_layout(path):
        a = np.load(path, mmap_mode="r")
        if not a.flags.c_contiguous:
            raise ValueError(f"{path}: expected a C-ordered array")
        out = (int(a.offset), tuple(a.shape), a.dtype)
        del a
        return out

    class FE:
        """Projection off drug-dose and line fixed effects (unbalanced): dd-demeaning (exact), then off the
        dd-demeaned line dummies (exact, by an orthonormal basis)."""

        def __init__(self, d, l_):
            n = len(d)
            self.du, dinv = np.unique(d, return_inverse=True)
            self.lu, linv = np.unique(l_, return_inverse=True)
            self.D = sparse.csr_matrix((np.ones(n), (np.arange(n), dinv)), shape=(n, len(self.du)))
            self.cnt = np.bincount(dinv).astype(float)
            Lm = np.zeros((n, len(self.lu)))
            Lm[np.arange(n), linv] = 1.0
            Ld = self.dd_demean(Lm)
            U, s, _ = np.linalg.svd(Ld, full_matrices=False)
            self.Q = U[:, s > s[0] * 1e-9]

        def dd_demean(self, V):
            one = V.ndim == 1
            V2 = V[:, None] if one else V
            out = V2 - self.D @ ((self.D.T @ V2) / self.cnt[:, None])
            return out[:, 0] if one else out

        def M(self, V):
            Vd = self.dd_demean(V)
            return Vd - self.Q @ (self.Q.T @ Vd)

    @staticmethod
    def orth(A_, tol=1e-9):
        if A_.shape[1] == 0:
            return np.zeros((A_.shape[0], 0))
        U, s, _ = np.linalg.svd(A_, full_matrices=False)
        return U[:, s > (s[0] if len(s) else 0) * tol] if len(s) and s[0] > 0 else np.zeros((A_.shape[0], 0))

    @staticmethod
    def cluster_vcov(Xt, e, groups, bread, n, p):
        """CR1 cluster-robust covariance of the coefficients of Xt (FWL-partialled regressors)."""
        gid = pd.factorize(groups)[0]
        G = gid.max() + 1
        sc = Xt * e[:, None]
        S = np.zeros((G, Xt.shape[1]))
        np.add.at(S, gid, sc)
        c = G / max(G - 1, 1) * (n - 1) / max(n - p, 1)
        return c * bread @ (S.T @ S) @ bread, G

    @staticmethod
    def tp(est, se, df):
        return float(2 * stats.t.sf(abs(est / se), df)) if np.isfinite(se) and se > 0 else np.nan


# ============================================================================= downloads and regulons
def fetch(ext, offline):
    """CollecTRI, DoRothEA A-C and the TRIM72 region into ext/ (kept; re-downloaded only when missing)."""
    os.makedirs(ext, exist_ok=True)
    status = {}
    for name, url, minsize in (("collectri.tsv", COLLECTRI_URL, 1_000_000), ("dorothea_ABC.tsv", DOROTHEA_URL, 500_000),
                               ("ensembl_trim72_region.json", REGION_URL, 1000)):
        p = os.path.join(ext, name)
        if os.path.exists(p) and os.path.getsize(p) >= minsize:
            status[name] = "cached"
            continue
        if offline:
            status[name] = "missing (offline)"
            continue
        log(f"download {url}" + ("" if shutil.which("curl") else " (curl not found: Python urllib)"))
        ok = download(url, p, tries=3)
        status[name] = "downloaded" if ok and os.path.getsize(p) >= minsize else "failed"
    return status


def read_regulon(path, source):
    """Signed TF -> target table (tf, target, weight) as decoupler's get_collectri / get_dorothea. CollecTRI: only the
    COMPLEX sources made of AP-1 members (or of NF-kB members) become AP1 (NFKB); single-protein sources such as JUN,
    FOS or RELA keep their own names (decoupler's merge). Other complexes (none in CollecTRI 2024) are left out."""
    t = pd.read_csv(path, sep="\t")
    need = {"source", "source_genesymbol", "target_genesymbol", "is_stimulation", "is_inhibition"}
    if not need <= set(t.columns) or len(t) < 1000:
        raise ValueError(f"{path}: not an OmniPath interaction table")
    sym = t["source_genesymbol"].astype(str)
    mem = sym.str.split("_")
    tf = sym.copy()
    if source == "CollecTRI":
        cx = t["source"].astype(str).str.startswith("COMPLEX").to_numpy()
        ap1 = cx & mem.map(lambda m: set(m) <= AP1).to_numpy()
        nfk = cx & mem.map(lambda m: set(m) <= NFKB).to_numpy()
        tf[ap1], tf[nfk] = "AP1", "NFKB"
        other_cx = cx & ~ap1 & ~nfk
        t, tf = t[~other_cx], tf[~other_cx]
    b = {c: t[c].astype(str).str.lower().eq("true").to_numpy() for c in
         ("is_stimulation", "is_inhibition", "consensus_stimulation", "consensus_inhibition") if c in t}
    s, i = b["is_stimulation"], b["is_inhibition"]
    cs, ci = b.get("consensus_stimulation", s), b.get("consensus_inhibition", i)
    w = np.where(cs & ~ci, 1, np.where(ci & ~cs, -1, np.where(i & ~s, -1, 1)))
    df = pd.DataFrame({"tf": tf.to_numpy(), "target": t["target_genesymbol"].astype(str).to_numpy(), "w": w})
    if "dorothea_level" in t:
        df["level"] = t["dorothea_level"].astype(str).to_numpy()
    g = df.groupby(["tf", "target"], sort=False)["w"].agg(["mean", "size"]).reset_index()
    g["weight"] = np.where(g["mean"] < 0, -1, 1)
    g = g.rename(columns={"size": "n_records"}).drop(columns="mean")
    g.insert(0, "source", source)
    return g


def locus_genes(ext):
    p = os.path.join(ext, "ensembl_trim72_region.json")
    try:
        d = json.load(open(p, encoding="utf-8"))
        ids = {g["id"]: (g.get("external_name") or "") for g in d}
        if "ENSG00000177238" not in ids:
            raise ValueError
        return ids, "Ensembl REST (rest.ensembl.org overlap, TRIM72 +- 200 kb)"
    except (OSError, ValueError, KeyError, TypeError):
        return dict(LOCUS_FALLBACK), "fallback list in upstream_tf.py (Ensembl 116, TRIM72 +- 200 kb)"


# ============================================================================= atlas context
class Ctx:
    def __init__(self, data):
        self.data = data
        self.fxd = os.path.join(data, "atlas", "effects")
        self.fx = A.FX(os.path.join(data, "atlas"))          # sets A.MIN_CELLS from info.json
        fx = self.fx
        self.gcol = fx.gi                                     # atlas columns of the genes
        g = fx.genes.iloc[self.gcol]
        self.gsym = g["symbol"].astype(str).to_numpy()
        self.gtok = g["token"].astype(int).to_numpy()
        self.ng = len(self.gcol)
        self.gidx = {}
        for j, s in enumerate(self.gsym):
            self.gidx.setdefault(s, j)
        self.lines = fx.lines["cell_line_id"].astype(str).tolist()
        self.nl = len(self.lines)
        self.w = fx.wells
        self.nw = len(self.w)
        self.dd = fx.dd
        self.nd = len(self.dd)
        self.em = np.asarray(fx.expr_mask)[:, self.gcol].astype(bool)          # lines x genes
        self.comp = A.composition_matrix(fx)                                      # wells x lines
        self.keep = ~(self.dd["unreliable_plate_only"].to_numpy(bool) | self.dd["position_not_correctable"].to_numpy(bool))
        self.drug_id = pd.factorize(self.dd["drug"])[0]
        gm = pd.read_parquet(os.path.join(data, "metadata", "gene_metadata.parquet"))
        self.tok_of = dict(zip(gm["gene_symbol"].astype(str), gm["token_id"].astype(int)))
        self.ens_tok = dict(zip(gm["ensembl_id"].astype(str), gm["token_id"].astype(int)))
        self.j_trim = self.gidx[GENE]

    def dd_row(self, drug, conc):
        r = self.dd.index[(self.dd["drug"] == drug) & np.isclose(self.dd["conc"].astype(float), conc)]
        return int(r[0]) if len(r) else None

    def dd_mean(self, V):
        """wells x ... -> drug-doses x ...: nanmean over each drug-dose's used wells (the atlas's per-line means)."""
        out = np.full((self.nd,) + V.shape[1:], np.nan, dtype=np.float32)
        with quiet():
            for d, ii in self.fx.wells_of_dd.items():
                if len(ii):
                    out[d] = np.nanmean(V[ii], axis=0)
        return out


def regulon_matrix(reg, ctx, excl):
    """Sparse genes x TFs weight matrix over the atlas genes outside the TRIM72 locus; TFs with >= TMIN targets."""
    j = reg["target"].map(ctx.gidx)
    r = reg[j.notna()].copy()
    r["j"] = j[j.notna()].astype(int)
    r = r[~excl[r["j"].to_numpy()]]
    cnt = r.groupby("tf")["j"].size()
    tfs = sorted(cnt.index[cnt >= TMIN])
    r = r[r["tf"].isin(tfs)]
    ti = {t: k for k, t in enumerate(tfs)}
    W = sparse.csr_matrix((r["weight"].to_numpy(float), (r["j"].to_numpy(), r["tf"].map(ti).to_numpy())),
                          shape=(ctx.ng, len(tfs)))
    return W, tfs, cnt.reindex(tfs).to_numpy()


class ULM:
    """Per-row univariate linear model of a gene vector on each TF's weights over the row's finite genes."""

    def __init__(self, W):
        Wt = W.T.tocsr()
        self.Wt, self.W2t, self.Wnzt = Wt, Wt.multiply(Wt).tocsr(), (Wt != 0).astype(np.float64).tocsr()
        self.T = W.shape[1]

    def __call__(self, R, block=256, want_t=True):
        n_r = R.shape[0]
        slope = np.full((n_r, self.T), np.nan)
        tval = np.full((n_r, self.T), np.nan) if want_t else None
        ntar = np.zeros((n_r, self.T))
        for s0 in range(0, n_r, block):
            X = np.asarray(R[s0:s0 + block], dtype=np.float64)
            F = np.isfinite(X)
            n = F.sum(axis=1).astype(float)
            Xz = np.where(F, X, 0.0)
            with quiet():
                rbar = Xz.sum(axis=1) / np.maximum(n, 1)
            Rc = np.where(F, Xz - rbar[:, None], 0.0)
            Ff = F.astype(np.float64)
            num = np.asarray(self.Wt @ Rc.T).T
            sW = np.asarray(self.Wt @ Ff.T).T
            sW2 = np.asarray(self.W2t @ Ff.T).T
            nt = np.asarray(self.Wnzt @ Ff.T).T
            with quiet():
                den = sW2 - sW ** 2 / n[:, None]
                b = num / den
                bad = (nt < TMIN) | ~(den > 1e-12) | (n[:, None] < TMIN + 3)
                b[bad] = np.nan
                slope[s0:s0 + block] = b
                if want_t:
                    rss = (Rc ** 2).sum(axis=1)[:, None] - b ** 2 * den
                    t = b / np.sqrt(np.clip(rss, 1e-300, None) / (n[:, None] - 2) / den)
                    tval[s0:s0 + block] = t
            ntar[s0:s0 + block] = nt
        return slope, tval, ntar


# ============================================================================= the pseudobulk pass
def load_profiles(pb):
    parts = []
    for m in sorted(glob.glob(os.path.join(pb, "group*_profiles.csv"))):
        t = pd.read_csv(m, dtype={"sample": str, "cell_line_id": str})
        t["file"] = m.replace("_profiles.csv", ".npy")
        parts.append(t)
    if not parts:
        sys.exit(f"no pseudobulk profiles in {pb}: the atlas must keep atlas/pseudobulk")
    return pd.concat(parts, ignore_index=True)


def stream_plates(prof, rows_of, plates, nw, L, toks, etoks, on_plate, chunk=CHUNK):
    """One sequential pass over the pseudobulk files of prof (columns file, row, wi, li, plate, as build_pass makes
    them; each file read once): per plate, the counts of the atlas tokens toks and of the extra tokens etoks summed
    per (well of the plate, line) as float32 (wells in rows_of[p] order). on_plate(p, C, Ex) is called as soon as
    every file holding that plate's profiles has been read; C and Ex are dropped after the call. Raises on a (sample,
    line) profile listed twice in one file and on a short read. Plates without any profile are never passed on."""
    G, E = len(toks), len(etoks)
    pos = np.empty(nw, dtype=int)
    for p in plates:
        pos[rows_of[p]] = np.arange(len(rows_of[p]))
    files = sorted(prof["file"].unique())
    pending = {p: set(prof.loc[prof["plate"] == p, "file"]) for p in plates}
    acc = {}
    for f in files:
        g = prof[prof["file"] == f].sort_values("row")
        if g.duplicated(["wi", "li"]).any():
            raise ValueError(f"{f}: a (sample, line) profile appears twice in one file")
        off, shape, dt = TW.npy_layout(f)
        rb = shape[1] * dt.itemsize
        rows = g["row"].to_numpy()
        a_w, a_l, a_p = g["wi"].to_numpy(), g["li"].to_numpy(), g["plate"].to_numpy()
        for p in np.unique(a_p):
            if p not in acc:
                acc[p] = (np.zeros((len(rows_of[p]), L, G), dtype=np.float32),
                          np.zeros((len(rows_of[p]), L, E), dtype=np.float32))
        buf = np.empty((chunk, shape[1]), dtype=dt)
        tf0 = time.time()
        with open(f, "rb") as fh:
            for s0 in range(0, shape[0], chunk):
                n = min(chunk, shape[0] - s0)
                lo, hi = np.searchsorted(rows, [s0, s0 + n])
                if hi <= lo:
                    continue
                fh.seek(off + s0 * rb)
                if fh.readinto(buf[:n]) != n * rb:
                    raise IOError(f"{f}: short read at row {s0}")
                rr = rows[lo:hi] - s0
                sub = buf[rr[:, None], toks[None, :]]
                ex = buf[rr[:, None], etoks[None, :]]
                pp = a_p[lo:hi]
                for p in np.unique(pp):
                    m = pp == p
                    C, Ex = acc[p]
                    ix = (pos[a_w[lo:hi][m]], a_l[lo:hi][m])
                    C[ix] += sub[m]
                    Ex[ix] += ex[m]
        log(f"  read {os.path.basename(f)}: {len(g)} profiles ({time.time() - tf0:.0f} s)")
        for p in np.unique(a_p):
            pending[p].discard(f)
            if not pending[p]:
                C, Ex = acc.pop(p)
                on_plate(p, C, Ex)
                del C, Ex


def plate_r2(C, tot, nc, em, drug, comp, W1a, W2a):
    """Method-v3 r2 of the atlas genes for one plate, in place on C (the plate's wells x lines x genes counts, float32
    -> r2): log CPM as tahoe_atlas.log_cpm (profiles with >= A.MIN_CELLS cells; lines that do not express the gene,
    em = lines x genes False, -> NaN), minus the plate's drug-well median of the line (drug: bool per well of the
    plate), minus the composition shift (comp: the plate's wells x lines), minus the atlas's position effect W1a - W2a
    of the gene; wells whose own W1 has < A.MIN_LINES lines -> NaN. tot, nc: the plate's wells x lines total counts and
    cells. Returns (r2, the plate's W1 (wells x genes), its validation against the atlas W1a: cells finite in both,
    max |diff|, finite here only, finite in the atlas only)."""
    L, G = em.shape
    nwp = C.shape[0]
    for i in range(nwp):                              # log CPM exactly as tahoe_atlas.log_cpm, expressing lines only
        ok = nc[i] >= A.MIN_CELLS
        Yi = np.full((L, G), np.nan, dtype=np.float32)
        Yi[ok] = np.log2((C[i][ok] + 0.5) / (tot[i][ok][:, None] + 1.0) * 1e6)
        Yi[~em] = np.nan
        C[i] = Yi
    Y = C
    with quiet():
        for l_ in range(L):
            base = np.nanmedian(Y[drug, l_, :], axis=0)
            Y[:, l_, :] -= base[None, :]
            Y[:, l_, :] -= comp[:, l_][:, None]
        W1m = np.full((nwp, G), np.nan, dtype=np.float32)
        for i in range(nwp):
            v = np.nanmedian(Y[i], axis=0)
            v[np.isfinite(Y[i]).sum(axis=0) < A.MIN_LINES] = np.nan
            W1m[i] = v
    both = np.isfinite(W1m) & np.isfinite(W1a)
    val = {"W1_cells_both_finite": int(both.sum()),
           "W1_max_abs_diff_vs_atlas": float(np.max(np.abs(W1m[both] - W1a[both]))) if both.any() else np.nan,
           "W1_finite_here_not_atlas": int((np.isfinite(W1m) & ~np.isfinite(W1a)).sum()),
           "W1_finite_atlas_not_here": int((~np.isfinite(W1m) & np.isfinite(W1a)).sum())}
    eff = np.nan_to_num(W1a - W2a).astype(np.float32)
    fin = np.isfinite(W1m)
    for i in range(nwp):
        Y[i] = np.where(fin[i][None, :], Y[i] - eff[i][None, :], np.nan)
    return Y, W1m, val


def build_pass(ctx, W, tfs, sel, excl, cdir, key):
    """One streamed pass over atlas/pseudobulk (each file read once, sequentially). Per plate, as soon as all its
    profiles are read: method-v3 r2 of every atlas gene per (well, line) (log CPM -> minus the plate's drug-well
    median of the line -> minus the composition shift -> minus the atlas's position effect W1 - W2 of the gene; wells
    whose own W1 has < MIN_LINES lines left out), checked against the atlas W1; then per (well, line) the ULM slope of
    every TF over the line's expressed genes outside the TRIM72 locus, r2 of the selected genes, mean |r2|; DMSO
    counts per plate x line; counts of the extra (non-atlas) genes per (well, line)."""
    path = os.path.join(cdir, f"pass_{key}.npz")
    if os.path.exists(path):
        log(f"pseudobulk pass: cache {os.path.basename(path)}")
        z = np.load(path, allow_pickle=False)
        return {k: z[k] for k in z.files} | {"_from_cache": True}
    t0 = time.time()
    fx, w = ctx.fx, ctx.w
    NW, L, G, T = ctx.nw, ctx.nl, ctx.ng, len(tfs)
    etok = np.array([ctx.tok_of[s] for s in EXTRA_SYMBOLS], dtype=int)
    E = len(etok)
    sel_j = np.array([ctx.gidx[s] for s in sel])
    prof = load_profiles(os.path.join(ctx.data, "atlas", "pseudobulk"))
    wi = {s: i for i, s in enumerate(w["sample"].astype(str))}
    li = {s: i for i, s in enumerate(ctx.lines)}
    prof = prof[prof["sample"].isin(wi) & prof["cell_line_id"].isin(li)].copy()
    prof["wi"] = prof["sample"].map(wi).astype(int)
    prof["li"] = prof["cell_line_id"].map(li).astype(int)
    plate_w = w["plate"].astype(str).to_numpy()
    prof["plate"] = plate_w[prof["wi"].to_numpy()]
    plates = list(fx.plates)
    rows_of = {p: np.flatnonzero(plate_w == p) for p in plates}
    tot = np.zeros((NW, L))
    nc = np.zeros((NW, L))
    np.add.at(tot, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["total_counts"].to_numpy(float))
    np.add.at(nc, (prof["wi"].to_numpy(), prof["li"].to_numpy()), prof["n_cells"].to_numpy(float))
    tfw = np.full((NW, L, T), np.nan, dtype=np.float32)
    selw = np.full((NW, L, len(sel)), np.nan, dtype=np.float32)
    bgw = np.full((NW, L), np.nan, dtype=np.float32)
    exw = np.zeros((NW, L, E), dtype=np.float32)
    dm_c = np.zeros((len(plates), L, G), dtype=np.float32)
    dm_e = np.zeros((len(plates), L, E), dtype=np.float32)
    dm_t = np.zeros((len(plates), L))
    dm_n = np.zeros((len(plates), L))
    ulm = ULM(W)
    val = []

    def process_plate(p, C, Ex):
        tp = time.time()
        rows = rows_of[p]
        pi = plates.index(p)
        t_, n_ = tot[rows], nc[rows]
        dm = ~fx.drug_w[rows]
        dm_c[pi], dm_e[pi] = C[dm].sum(axis=0), Ex[dm].sum(axis=0)
        dm_t[pi], dm_n[pi] = t_[dm].sum(axis=0), n_[dm].sum(axis=0)
        exw[rows] = Ex
        W1a = np.asarray(fx.W1[rows])[:, ctx.gcol]
        W2a = np.asarray(fx.W2[rows])[:, ctx.gcol]
        Y, _W1m, v = plate_r2(C, t_, n_, ctx.em, fx.drug_w[rows], ctx.comp[rows], W1a, W2a)
        val.append({"plate": p, "wells": len(rows)} | v)
        selw[rows] = Y[:, :, sel_j]
        with quiet():
            for i in range(len(rows)):
                bgw[rows[i]] = np.nanmean(np.abs(Y[i][:, ~excl]), axis=1)
            for l_ in range(L):
                R = Y[:, l_, :].astype(np.float64)
                R[:, excl] = np.nan
                b, _t, _n = ulm(R, want_t=False)
                tfw[rows, l_, :] = b
        log(f"  plate {p}: {len(rows)} wells processed ({time.time() - tp:.0f} s; W1 max |diff| vs atlas "
            f"{val[-1]['W1_max_abs_diff_vs_atlas']:.2g}; peak RSS {peak_gb():.2f} GB)")

    stream_plates(prof, rows_of, plates, NW, L, ctx.gtok, etok, process_plate)
    tf_dd = ctx.dd_mean(tfw)
    res = {"tf_dd": tf_dd, "selw": selw, "bgw": bgw, "exw": exw, "tot": tot, "nc": nc, "dm_c": dm_c, "dm_e": dm_e,
           "dm_t": dm_t, "dm_n": dm_n, "tfs": np.array(tfs), "sel": np.array(sel), "extra": np.array(EXTRA_SYMBOLS),
           "plates": np.array(plates), "validation": np.array(json.dumps(val))}
    np.savez(path, **res)
    log(f"pseudobulk pass done ({time.time() - t0:.0f} s; peak RSS {peak_gb():.2f} GB)")
    return res


# ============================================================================= statistics helpers
def presid(V, Q):
    return V - Q @ (Q.T @ V)


def qbasis(n, *cols):
    M = [np.ones(n)] + [np.asarray(c, float).reshape(n, -1) for c in cols if c is not None and np.size(c)]
    return TW.orth(np.column_stack(M))


def unit_cols(X):
    nrm = np.sqrt((X ** 2).sum(axis=0))
    return X / np.where(nrm > 0, nrm, np.nan)


def ranks(X):
    return stats.rankdata(X, axis=0)


def fisher_ci(r, n, k=0, se_mult=1.0):
    se = se_mult / np.sqrt(np.maximum(n - 3 - k, 1))
    z = np.arctanh(np.clip(r, -0.999999, 0.999999))
    return np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)


def perm_test_cols(yr, Xn, perms):
    """r of yr (residual) with unit columns Xn, and its permutation null (rows of perms reorder yr)."""
    yu = yr / np.linalg.norm(yr)
    r = yu @ Xn
    nul = yu[perms] @ Xn
    sd = nul.std(axis=0)
    with quiet():
        p_cal = 2 * stats.norm.sf(np.abs(r / sd))
    p_emp = (1 + (np.abs(nul) >= np.abs(r)[None] - 1e-12).sum(axis=0)) / (len(perms) + 1)
    return r, sd, p_cal, p_emp


def drug_jackknife_se(yr, Xr, groups, Q):
    """Leave-one-drug-out jackknife SE of the partial r of y with each column of X: each drug's rows are left out in
    turn and the covariates are re-fitted on the remaining rows (exact, by downdating the cross-products). yr, Xr = y
    and X already residualised on Q (orthonormal basis of intercept + covariates, all rows)."""
    gid = pd.factorize(np.asarray(groups))[0]
    G = int(gid.max()) + 1
    if G < 3:
        return np.full(Xr.shape[1], np.nan)
    Xr = np.where(np.isfinite(Xr), Xr, 0.0)
    k = Q.shape[1]
    yy0, yX0, XX0 = float(yr @ yr), yr @ Xr, (Xr ** 2).sum(axis=0)
    rj = np.empty((G, Xr.shape[1]))
    order = np.argsort(gid, kind="stable")
    bounds = np.searchsorted(gid[order], np.arange(G + 1))
    with quiet():
        for g in range(G):
            ii = order[bounds[g]:bounds[g + 1]]
            Qg, yg, Xg = Q[ii], yr[ii], Xr[ii]
            Am = np.eye(k) - Qg.T @ Qg                      # Q'Q on the rows kept (Q'Q = I on all rows)
            ay, aX = -(Qg.T @ yg), -(Qg.T @ Xg)             # Q' y and Q' X on the rows kept (both 0 on all rows)
            try:
                By, BX = np.linalg.solve(Am, ay), np.linalg.solve(Am, aX)
            except np.linalg.LinAlgError:
                Ai = np.linalg.pinv(Am)
                By, BX = Ai @ ay, Ai @ aX
            yy = yy0 - yg @ yg - ay @ By
            yX = yX0 - yg @ Xg - ay @ BX
            XX = XX0 - (Xg ** 2).sum(axis=0) - (aX * BX).sum(axis=0)
            rj[g] = yX / np.sqrt(yy * XX)
        return np.sqrt((G - 1) / G * ((rj - rj.mean(axis=0)) ** 2).sum(axis=0))


def drug_ci(r, null_sd, se_jack):
    """95% CI of a partial r over drug-doses: r +- 1.96 x the larger of the drug-block null SD and the drug jackknife
    SE (drug-doses of one drug are not independent; the iid Fisher SE is too small), clipped to [-1, 1]."""
    se = np.fmax(null_sd, se_jack)
    return np.clip(r - 1.96 * se, -1, 1), np.clip(r + 1.96 * se, -1, 1), se


def assoc_cols(y, X, cols, perms, groups):
    """Partial Pearson r of y with each column of X (intercept + cols partialled from both), drug-block null SD and
    calibrated p, empirical p, drug jackknife SE and the drug CI. Returns a dict of arrays (one entry per column)."""
    n = len(y)
    Q = qbasis(n, *cols)
    yr = presid(np.asarray(y, float), Q)
    Xr = presid(np.where(np.isfinite(X), X, 0.0), Q)
    Xn = unit_cols(Xr)
    r, sd, p_cal, p_emp = perm_test_cols(yr, np.nan_to_num(Xn), perms)
    sej = drug_jackknife_se(yr, Xr, groups, Q)
    lo, hi, se = drug_ci(r, sd, sej)
    bad = ~np.isfinite(Xn).all(axis=0)
    out = {"r": r, "null_sd_drug_block": sd, "se_jackknife_drug": sej, "ci_lo": lo, "ci_hi": hi, "p": p_cal,
           "p_perm_empirical": p_emp, "n_partialled": np.full(X.shape[1], Q.shape[1])}
    for k_ in ("r", "null_sd_drug_block", "se_jackknife_drug", "ci_lo", "ci_hi", "p", "p_perm_empirical"):
        out[k_] = np.where(bad, np.nan, out[k_])
    return out


# ============================================================================= (a) A1: across drug-doses
def dd_level(ctx, acts, xvers, cov_df, fus_pyc, a, rng, tab_rows_extra):
    """acts: {source: (n x T activity matrix over the kept drug-doses, names)}; xvers: {name: y vector}."""
    keep = np.flatnonzero(ctx.keep)
    n = len(keep)
    ddk = ctx.dd.iloc[keep][["drug", "conc"]].reset_index(drop=True)
    drug_k = ctx.drug_id[keep]
    log(f"A1: drug-block permutations ({a.perm})")
    perms = drug_block_perms(ddk, a.perm, rng)
    Z = np.nan_to_num(np.asarray(np.load(os.path.join(ctx.fxd, "DD_z.npy"), mmap_mode="r")[keep][:, ctx.gcol],
                                 dtype=np.float64))
    univ = ~ctx.excl
    Zu = Z[:, univ]
    Zs = (Zu - Zu.mean(axis=0)) / np.where(Zu.std(axis=0) > 0, Zu.std(axis=0), 1.0)
    U, S, _Vt = np.linalg.svd(Zs, full_matrices=False)
    del _Vt, Zs
    var_ex = S ** 2 / (S ** 2).sum()
    # expression-matched random genes (TRIM72 level within 2x, expressed in >= 45 lines, outside the locus)
    g = ctx.fx.genes.iloc[ctx.gcol]
    lvl = g["median_line_cpm"].to_numpy(float)
    nle = g["n_lines_expressing"].to_numpy(float)
    lt = lvl[ctx.j_trim]
    cand = np.flatnonzero((lvl >= lt / 2) & (lvl <= lt * 2) & (nle >= 45) & univ)
    rnd = rng.choice(cand, size=min(300, cand.size), replace=False)
    Zr = Z[:, rnd]
    C = cov_df.to_numpy(float)
    variants = {"raw": [], "covariates": [C], "minus_3pc": [U[:, :3]], "minus_10pc": [U[:, :10]]}
    rows = []
    for xname, y in xvers.items():
        extra = [fus_pyc] if xname == "TRIM72_rt_across" else []
        for vname, cols in variants.items():
            Q = qbasis(n, *(cols + extra))
            yr = presid(y, Q)
            Rr = unit_cols(presid(Zr, Q))
            mr = (yr / np.linalg.norm(yr)) @ Rr                 # random genes' own r with TRIM72 (for reference)
            # genome-wide: r of each TF's activity with every gene of the universe (CollecTRI, own and rt)
            Gr = unit_cols(presid(Zu, Q)).astype(np.float32) if (vname != "raw" and xname != "TRIM72_rt_across") \
                else None
            for src, (X, names) in acts.items():
                ok = np.isfinite(X).all(axis=0)
                Xr = presid(np.where(np.isfinite(X), X, 0.0), Q)
                Xn = unit_cols(Xr)
                r, sd, p_cal, p_emp = perm_test_cols(yr, Xn, perms)
                # specificity: r of each matched random gene with the same TF activity
                Rm = Rr.T @ Xn                                      # 300 x T
                pct = 100 * np.mean(Rm < r[None], axis=0)
                pct_abs = 100 * np.mean(np.abs(Rm) < np.abs(r)[None], axis=0)
                # Spearman partial (ranks of everything)
                Qs = qbasis(n, *[ranks(c) for c in cols + extra])
                ys = presid(ranks(y), Qs)
                Xs = unit_cols(presid(ranks(np.where(np.isfinite(X), X, 0.0)), Qs))
                rs = (ys / np.linalg.norm(ys)) @ Xs
                dfree = n - Q.shape[1] - 1
                with quiet():
                    ts = rs * np.sqrt(dfree / (1 - rs ** 2))
                ps = 2 * stats.t.sf(np.abs(ts), dfree)
                sej = drug_jackknife_se(yr, Xr, drug_k, Q)
                lo, hi, _se = drug_ci(r, sd, sej)
                q = bh(np.where(ok, p_cal, np.nan))
                pct_all = np.full(len(names), np.nan)
                rank_all = np.full(len(names), np.nan)
                if Gr is not None and src == "CollecTRI_t":
                    Rall = np.nan_to_num(Xn).astype(np.float32).T @ Gr
                    pct_all = 100 * np.mean(Rall < r[:, None].astype(np.float32), axis=1)
                    rank_all = 1 + (Rall > r[:, None].astype(np.float32)).sum(axis=1)
                    del Rall
                for k, nm in enumerate(names):
                    if not ok[k]:
                        continue
                    rows.append({"source": src, "tf": nm, "trim72_version": xname, "variant": vname, "n_drugdoses": n,
                                 "n_partialled": Q.shape[1], "r": r[k], "ci_lo": lo[k], "ci_hi": hi[k],
                                 "null_sd_drug_block": sd[k], "se_jackknife_drug": sej[k],
                                 "p": p_cal[k], "p_perm_empirical": p_emp[k], "q_bh": q[k],
                                 "rho_spearman_partial": rs[k], "p_spearman": ps[k],
                                 "pct_vs_matched_genes": pct[k], "pct_abs_vs_matched_genes": pct_abs[k],
                                 "matched_genes_median_r": float(np.median(Rm[:, k])),
                                 "pct_vs_all_genes": pct_all[k], "rank_vs_all_genes": rank_all[k],
                                 "n_genes_universe": Zu.shape[1]})
            del Gr
            tab_rows_extra.append({"trim72_version": xname, "variant": vname, "n_drugdoses": n,
                                   "matched_genes_r_with_TRIM72_median": float(np.median(mr)),
                                   "matched_genes_r_with_TRIM72_p90_abs": float(np.percentile(np.abs(mr), 90))})
        log(f"A1: {xname} done")
    pcs = pd.DataFrame({"pc": np.arange(1, 11), "variance_explained": var_ex[:10],
                        "r_with_TRIM72_z": [np.corrcoef(U[:, k], xvers["TRIM72"])[0, 1] for k in range(10)]})
    return pd.DataFrame(rows), pcs, U, perms


def plate_batch_subsets(ctx):
    """Kept drug-doses by plate batch of their used wells: all on the high-TRIM72 plates (1-3, 14), all on the
    low-TRIM72 plates (4-12), or mixed (mostly the replicated drug-doses on plates 6 and 14)."""
    pl = ctx.dd.iloc[np.flatnonzero(ctx.keep)]["plates"].fillna("").astype(str).str.split(r"[;,]")
    hi = pl.map(lambda s: all(p.strip() in HIGH_PLATES for p in s if p.strip())).to_numpy()
    lo = pl.map(lambda s: not any(p.strip() in HIGH_PLATES for p in s if p.strip())).to_numpy()
    return {"high_plates_only": hi, "low_plates_only": lo, "mixed_plates": ~hi & ~lo}


def dd_subset_assoc(ctx, acts, y, cov, subsets, B, rng):
    """The A1 covariates test (TRIM72 z vs each TF activity, covariates partialled) within subsets of the kept
    drug-doses, each subset with its own drug-block permutations; BH over TFs within source x subset."""
    keep = np.flatnonzero(ctx.keep)
    ddk = ctx.dd.iloc[keep][["drug", "conc"]].reset_index(drop=True)
    drug_k = ctx.drug_id[keep]
    rows = []
    for sname, m in subsets.items():
        if m.sum() < 30:
            continue
        perms = drug_block_perms(ddk[m].reset_index(drop=True), B, rng)
        for src, (X, names) in acts.items():
            o = assoc_cols(y[m], X[m], [cov[m]], perms, drug_k[m])
            q = bh(o["p"])
            for k, nm in enumerate(names):
                rows.append({"source": src, "tf": nm, "subset": sname, "n_drugdoses": int(m.sum()),
                             "n_drugs": int(len(np.unique(drug_k[m]))), "n_partialled": int(o["n_partialled"][k]),
                             "r": o["r"][k], "ci_lo": o["ci_lo"][k], "ci_hi": o["ci_hi"][k],
                             "null_sd_drug_block": o["null_sd_drug_block"][k],
                             "se_jackknife_drug": o["se_jackknife_drug"][k], "p": o["p"][k],
                             "p_perm_empirical": o["p_perm_empirical"][k], "q_bh": q[k]})
        log(f"A1 plate-batch split: {sname} ({int(m.sum())} drug-doses)")
    return pd.DataFrame(rows)


def overlap_control(W, tfs, Zk_u, y, cov, mediators, overlap_j, perms, drug_k):
    """Regulon-overlap control (TRIM72 z, covariates): each TF's ULM t on DD_z with its targets in overlap_j (AP-1 and
    ATF3 targets, immediate-early genes) removed, and with the mediators (ATF3, PMAIP1, DDIT3 z, IEG score, AP1
    activity) partialled; the reference is the A1 covariates test. BH over TFs within variant."""
    keep_row = np.ones(W.shape[0])
    keep_row[overlap_j] = 0.0
    Wm = (sparse.diags(keep_row) @ W).tocsr()
    Wm.eliminate_zeros()
    n_all = np.asarray(abs(W).sum(axis=0)).ravel().astype(int)
    n_left = np.asarray(abs(Wm).sum(axis=0)).ravel().astype(int)
    _b, t_full, _n = ULM(W)(Zk_u)
    _b, t_min, _n = ULM(Wm)(Zk_u)
    variants = {"covariates (reference, full regulon)": (t_full, [cov]),
                "minus_overlap_targets": (t_min, [cov]),
                "plus_mediators_partialled": (t_full, [cov, mediators]),
                "minus_overlap_targets_plus_mediators": (t_min, [cov, mediators])}
    rows = []
    for vname, (X, cols) in variants.items():
        o = assoc_cols(y, X, cols, perms, drug_k)
        ok = np.isfinite(X).all(axis=0) & np.isfinite(o["r"])
        q = bh(np.where(ok, o["p"], np.nan))
        for k, nm in enumerate(tfs):
            rows.append({"tf": nm, "variant": vname, "n_targets": n_all[k],
                         "n_targets_used": n_left[k] if "minus" in vname else n_all[k],
                         "n_drugdoses": len(y), "n_partialled": int(o["n_partialled"][k]),
                         "r": o["r"][k] if ok[k] else np.nan, "ci_lo": o["ci_lo"][k] if ok[k] else np.nan,
                         "ci_hi": o["ci_hi"][k] if ok[k] else np.nan,
                         "null_sd_drug_block": o["null_sd_drug_block"][k],
                         "se_jackknife_drug": o["se_jackknife_drug"][k],
                         "p": o["p"][k] if ok[k] else np.nan, "q_bh": q[k]})
    D = pd.DataFrame(rows)
    ref = D[D["variant"].str.startswith("covariates")].set_index("tf")["r"]
    D["r_reference"] = D["tf"].map(ref)
    return D


# ============================================================================= (a) A2: within lines (two-way FE)
def clean_ok(ok):
    ok = ok.copy()
    for _ in range(10):                                         # singletons carry no within information
        bad = (ok.sum(axis=1) < 2)[:, None] | (ok.sum(axis=0) < 2)[None, :]
        if not (ok & bad).any():
            break
        ok &= ~bad
    return ok


def fe_screen(ok, y2d, X3d, covs, wt_line, drug_id, chunk=150):
    """y (dd x lines) on each column of X3d (dd x lines x T) with drug-dose and line fixed effects and covariates x
    TP53 group. Returns per column: common slope (drug-cluster and two-way (drug, line) cluster SE), partial r, SD of
    the residual X, and the TP53-WT and altered slopes with their difference (line-cluster and drug-cluster SE)."""
    d, l_ = np.nonzero(ok)
    n = len(d)
    fe = TW.FE(d, l_)
    wt = wt_line[l_]
    drug = drug_id[d]
    K = len(covs)
    if K:
        Cm = np.column_stack([c[d, l_] for c in covs])
        Qc = TW.orth(fe.M(np.column_stack([Cm * wt[:, None], Cm * (~wt)[:, None]])))
    else:
        Qc = np.zeros((n, 0))

    def R(V):
        MV = fe.M(V)
        return MV - Qc @ (Qc.T @ MV) if Qc.shape[1] else MV
    yt = R(y2d[d, l_].astype(float))
    syy = float(yt @ yt)

    def ind(g):
        gid = pd.factorize(g)[0]
        return sparse.csr_matrix((np.ones(n), (gid, np.arange(n))), shape=(gid.max() + 1, n)), gid.max() + 1
    Sd, Gd = ind(drug)
    Sl, Gl = ind(l_)
    Si, Gi = ind(drug.astype(np.int64) * 1000 + l_)
    p_all = 2 + 2 * K + len(fe.du) + len(fe.lu) - 1

    def cfac(G):
        return G / max(G - 1, 1) * (n - 1) / max(n - p_all, 1)
    out = []
    T = X3d.shape[2]
    for c0 in range(0, T, chunk):
        X = X3d[d, l_, c0:c0 + chunk].astype(float)
        Xt = R(X)
        sxx = (Xt ** 2).sum(axis=0)
        sxy = Xt.T @ yt
        with quiet():
            b = sxy / sxx
            e = yt[:, None] - Xt * b
            Ux = Xt * e
            vd = cfac(Gd) * np.asarray((Sd @ Ux)) ** 2
            vd = vd.sum(axis=0) / sxx ** 2
            vl = (cfac(Gl) * np.asarray(Sl @ Ux) ** 2).sum(axis=0) / sxx ** 2
            vi = (cfac(Gi) * np.asarray(Si @ Ux) ** 2).sum(axis=0) / sxx ** 2
            v2 = vd + vl - vi
            se2 = np.where(v2 > 0, np.sqrt(np.abs(v2)), np.sqrt(np.maximum(vd, vl)))
            sed = np.sqrt(vd)
            r = sxy / np.sqrt(sxx * syy)
            sdx = np.sqrt(sxx / n)
            # by TP53 group
            X1 = R(X * wt[:, None])
            X2 = R(X * (~wt)[:, None])
            a11, a22, a12 = (X1 ** 2).sum(0), (X2 ** 2).sum(0), (X1 * X2).sum(0)
            c1, c2 = X1.T @ yt, X2.T @ yt
            det = a11 * a22 - a12 ** 2
            b1, b2 = (a22 * c1 - a12 * c2) / det, (a11 * c2 - a12 * c1) / det
            e2 = yt[:, None] - X1 * b1 - X2 * b2
            P11, P22, P12 = a22 / det, a11 / det, -a12 / det
            res = {}
            for nm, Sm, Gm in (("line", Sl, Gl), ("drug", Sd, Gd)):
                S1, S2 = np.asarray(Sm @ (X1 * e2)), np.asarray(Sm @ (X2 * e2))
                m11, m22, m12 = (S1 ** 2).sum(0), (S2 ** 2).sum(0), (S1 * S2).sum(0)
                V11 = cfac(Gm) * (P11 ** 2 * m11 + 2 * P11 * P12 * m12 + P12 ** 2 * m22)
                V22 = cfac(Gm) * (P12 ** 2 * m11 + 2 * P12 * P22 * m12 + P22 ** 2 * m22)
                V12 = cfac(Gm) * (P11 * P12 * m11 + (P11 * P22 + P12 ** 2) * m12 + P12 * P22 * m22)
                res[nm] = (np.sqrt(V11), np.sqrt(V22), np.sqrt(np.clip(V11 + V22 - 2 * V12, 0, None)))
        for k in range(X.shape[1]):
            o = {"n_rows": n, "n_drugdoses": len(fe.du), "n_lines": len(fe.lu), "n_drugs": int(Gd),
                 "b": b[k], "se_drug": sed[k], "p_drug": TW.tp(b[k], sed[k], Gd - 1), "se_twoway": se2[k],
                 "ci_lo_twoway": b[k] - stats.t.ppf(0.975, min(Gd, Gl) - 1) * se2[k],
                 "ci_hi_twoway": b[k] + stats.t.ppf(0.975, min(Gd, Gl) - 1) * se2[k],
                 "p_twoway": TW.tp(b[k], se2[k], min(Gd, Gl) - 1), "r_partial_within": r[k],
                 "sd_tf_resid": sdx[k], "b_per_sd_tf": b[k] * sdx[k],
                 "b_WT": b1[k], "se_WT_line": res["line"][0][k], "b_alt": b2[k], "se_alt_line": res["line"][1][k],
                 "diff_WT_minus_alt": b1[k] - b2[k], "se_diff_line": res["line"][2][k],
                 "p_diff_line": TW.tp(b1[k] - b2[k], res["line"][2][k], Gl - 1),
                 "se_diff_drug": res["drug"][2][k], "p_diff_drug": TW.tp(b1[k] - b2[k], res["drug"][2][k], Gd - 1),
                 "mde_diff_80_line": Z80 * res["line"][2][k]}
            out.append(o)
    return out


def within_lines(ctx, tf_dd, tfs, ys, covsets, wt_line):
    rows = []
    keep = ctx.keep
    for yname, Y in ys.items():
        for csname, covs in covsets.items():
            base = np.isfinite(Y) & keep[:, None]
            for c in covs:
                base &= np.isfinite(c)
            fin = np.isfinite(tf_dd)                            # dd x lines x T
            # group TFs by their missing pattern within the base rows
            pat = {}
            for k in range(len(tfs)):
                m = base & fin[:, :, k]
                key = hashlib.md5(np.packbits(m).tobytes()).hexdigest()
                pat.setdefault(key, (m, []))[1].append(k)
            for key, (m, ks) in pat.items():
                ok = clean_ok(m)
                if ok.sum() < 100:
                    continue
                res = fe_screen(ok, Y, tf_dd[:, :, ks], covs, wt_line, ctx.drug_id)
                for k, o in zip(ks, res):
                    rows.append({"tf": tfs[k], "trim72_version": yname, "covset": csname} | o)
            log(f"A2: {yname} [{csname}]: {len(pat)} missing-value pattern(s)")
    df = pd.DataFrame(rows)
    df["q_bh_twoway"] = np.nan
    df["q_bh_diff_line"] = np.nan
    for _k, g in df.groupby(["trim72_version", "covset"]):
        m = ~g["tf"].isin(CTRL_TFS)
        df.loc[g.index[m], "q_bh_twoway"] = bh(g.loc[m, "p_twoway"].to_numpy())
        df.loc[g.index[m], "q_bh_diff_line"] = bh(g.loc[m, "p_diff_line"].to_numpy())
    return df


# ============================================================================= (b) line features
def oe_level(c, t, n_, expressed, plates_use, min_e=2.0):
    """Within-plate standardised level: summed observed counts over summed expected counts (the plate's median
    expressing line's CPM x the profile's library), over the plates used; log2((O+0.5)/(E+0.5)); NaN when E < min_e."""
    O = np.zeros(c.shape[1])
    Ex = np.zeros(c.shape[1])
    per = np.full((len(plates_use), c.shape[1]), np.nan)
    for k, p in enumerate(plates_use):
        ok = n_[p] >= A.MIN_CELLS
        cpm = np.where(ok, 1e6 * c[p] / np.where(t[p] > 0, t[p], np.nan), np.nan)
        med = np.nanmedian(cpm[ok & expressed])
        e = np.where(ok, t[p] / 1e6 * med, 0.0)
        O += np.where(ok, c[p], 0.0)
        Ex += e
        with quiet():
            per[k] = np.where(e >= 0.5, np.log2((c[p] + 0.5) / (e + 0.5)), np.nan)
    with quiet():
        rel = np.where(Ex >= min_e, np.log2((O + 0.5) / (Ex + 0.5)), np.nan)
    return rel, O, Ex, per


def baseline_relative(ctx, P_, plates_use):
    """Lines x genes: per reliable plate, log CPM of the DMSO wells (lines with >= MIN_CELLS cells, expressing lines)
    minus the plate's median line; mean over plates."""
    acc = np.zeros((ctx.nl, ctx.ng))
    cnt = np.zeros((ctx.nl, ctx.ng))
    for p in plates_use:
        c, t, n_ = P_["dm_c"][p].astype(np.float64), P_["dm_t"][p], P_["dm_n"][p]
        ok = n_ >= A.MIN_CELLS
        y = np.full(c.shape, np.nan)
        y[ok] = np.log2((c[ok] + 0.5) / (t[ok][:, None] + 1.0) * 1e6)
        y[~ctx.em] = np.nan
        with quiet():
            y = y - np.nanmedian(y, axis=0)[None, :]
        f = np.isfinite(y)
        acc += np.where(f, y, 0.0)
        cnt += f
    with quiet():
        return np.where(cnt > 0, acc / cnt, np.nan)


def _block_tests(yv, X, names, og, fam, rng, B):
    """One block of features without missing values over the same lines: Spearman-type r of rank(y) with rank(x)
    (0/1 for binary features), label-permutation calibrated p, organ-adjusted r (organ means out of both; within-organ
    permutation p); binary features also group means and the Welch difference."""
    n = len(yv)
    ry = stats.rankdata(yv)
    binary = np.all(np.isin(X, [0.0, 1.0]), axis=0)
    Rx = np.where(binary[None, :], X, stats.rankdata(X, axis=0))
    ryc = (ry - ry.mean()) / np.linalg.norm(ry - ry.mean())
    Xc = Rx - Rx.mean(axis=0)
    Xn = Xc / np.linalg.norm(Xc, axis=0)
    r = ryc @ Xn
    perm = np.argsort(rng.random((B, n)), axis=1)
    nul = ryc[perm] @ Xn
    sd = nul.std(axis=0)
    p_cal = 2 * stats.norm.sf(np.abs(r / sd))
    p_emp = (1 + (np.abs(nul) >= np.abs(r)[None] - 1e-12).sum(axis=0)) / (B + 1)
    ra = pa = np.full(len(names), np.nan)
    if fam != "lineage":
        Dm = pd.get_dummies(og).to_numpy(float)
        H = np.eye(n) - Dm @ np.linalg.pinv(Dm)
        groups = [np.flatnonzero(og == o) for o in np.unique(og)]
        permw = np.tile(np.arange(n), (B // 2, 1))
        for b_ in range(B // 2):
            for gi in groups:
                permw[b_, gi] = gi[rng.permutation(len(gi))]
        ya = H @ (ry - ry.mean())
        Xa = H @ Xc
        with quiet():
            Xan = Xa / np.linalg.norm(Xa, axis=0)
            ra = (ya / np.linalg.norm(ya)) @ Xan
            nula = (ya[permw] / np.linalg.norm(ya)) @ Xan
            pa = 2 * stats.norm.sf(np.abs(ra / nula.std(axis=0)))
    lo, hi = fisher_ci(r, n, 0, 1.06)
    rows = []
    for k, nm in enumerate(names):
        o = {"family": fam, "feature": nm, "n_lines": n, "feature_type": "binary" if binary[k] else "continuous",
             "rho": r[k], "rho_ci_lo": lo[k], "rho_ci_hi": hi[k], "null_sd": sd[k], "p": p_cal[k],
             "p_perm_empirical": p_emp[k], "rho_organ_adjusted": ra[k], "p_organ_adjusted": pa[k],
             "mde_rho_80": float(np.tanh(Z80 * 1.06 / np.sqrt(n - 3)))}
        if binary[k]:
            a1, a0 = yv[X[:, k] == 1], yv[X[:, k] == 0]
            se = np.sqrt(a1.var(ddof=1) / len(a1) + a0.var(ddof=1) / len(a0)) if min(len(a1), len(a0)) > 1 \
                else np.nan
            o.update({"n_with": len(a1), "n_without": len(a0), "mean_with": a1.mean(), "mean_without": a0.mean(),
                      "median_with": np.median(a1), "median_without": np.median(a0),
                      "diff_mean": a1.mean() - a0.mean(), "diff_ci_lo": a1.mean() - a0.mean() - 1.96 * se,
                      "diff_ci_hi": a1.mean() - a0.mean() + 1.96 * se,
                      "mde_diff_80_sd_units": Z80 * np.sqrt(1 / max(len(a1), 1) + 1 / max(len(a0), 1))})
        rows.append(o)
    return rows


def line_tests(outcomes, families, organ, rng, B, min_lines=10):
    """outcomes: DataFrame lines x outcome; families: {family: DataFrame lines x features (binary 0/1 or continuous)}.
    Each feature is tested over the lines where both it and the outcome are present (features sharing a missing
    pattern are tested together)."""
    vc = organ.value_counts()
    og_all = organ.where(organ.map(vc) >= 3, "other").to_numpy()
    rows = []
    for oname in outcomes.columns:
        y = outcomes[oname].to_numpy(float)
        for fam, F in families.items():
            Xall = F.reindex(outcomes.index).to_numpy(float)
            fin = np.isfinite(Xall) & np.isfinite(y)[:, None]
            pats = {}
            for k in range(Xall.shape[1]):
                pats.setdefault(fin[:, k].tobytes(), []).append(k)
            for _key, ks in pats.items():
                m = fin[:, ks[0]]
                if m.sum() < min_lines:
                    continue
                X = Xall[m][:, ks]
                okc = np.nanstd(X, axis=0) > 0
                if not okc.any():
                    continue
                ks = [k for k, o_ in zip(ks, okc) if o_]
                for o in _block_tests(y[m], X[:, okc], [F.columns[k] for k in ks], og_all[m], fam, rng, B):
                    rows.append({"outcome": oname} | o)
        # lineage overall: Kruskal-Wallis with a permutation p
        m = np.isfinite(y)
        yv, lab = y[m], organ.to_numpy()[m]
        if len(np.unique(lab)) > 1:
            H0 = stats.kruskal(*[yv[lab == o] for o in np.unique(lab)]).statistic
            Hn = np.array([stats.kruskal(*[yv[rng.permutation(len(yv))][lab == o] for o in np.unique(lab)]).statistic
                           for _ in range(2000)])
            rows.append({"outcome": oname, "family": "lineage", "feature": "organ (all, Kruskal-Wallis H)",
                         "n_lines": int(m.sum()), "feature_type": "categorical", "rho": np.nan, "kruskal_H": H0,
                         "p": (1 + (Hn >= H0).sum()) / (len(Hn) + 1), "n_organs": len(np.unique(lab))})
    df = pd.DataFrame(rows)
    df["q_bh"] = bh(df["p"].to_numpy())    # headline: BH over every outcome x feature test of the table (conservative)
    df["q_bh_outcome"] = np.nan             # BH over every test of the outcome (all feature families)
    df["q_bh_family"] = np.nan              # BH within outcome x family (the least conservative; the earlier q_bh)
    for _k, g in df.groupby("outcome"):
        df.loc[g.index, "q_bh_outcome"] = bh(g["p"].to_numpy())
    for _k, g in df.groupby(["outcome", "family"]):
        df.loc[g.index, "q_bh_family"] = bh(g["p"].to_numpy())
    return df


# ============================================================================= README
README = """Tables of upstream_tf.py (re-created by: python3 upstream_tf.py --data <Tahoe-100M folder>). Associations only:
Tahoe has no TF or MG53 perturbation and measures mRNA; a TF's activity is read from its targets' mRNA, and a TF whose
activity tracks TRIM72 may be a co-responder to the same drugs rather than a regulator.

Regulons: CollecTRI (OmniPath, decoupler's processing: only the COMPLEX sources made of AP-1 members, or of NF-kB
members, are merged into AP1 and NFKB; single-protein sources such as JUN, FOS, RELA or NFKB1 stay TFs of their own;
weight -1 = repression by consensus, else +1); DoRothEA A-C (OmniPath) as a sensitivity source. CollecTRI is required:
without it (no internet and no cache/external/collectri.tsv) the script stops before the pseudobulk pass and says where
to put the file; there is no fallback. TRIM72 and the Ensembl genes within 200 kb of it are out of every regulon and of
the gene universe (checks.csv lists them). TFs need >= 5 targets among the atlas genes outside the locus. Activity =
ULM: per sample, the gene vector (DD_z, DD_lfc, or r2 per well x line) regressed on the TF's weights (0 = non-target)
over the sample's genes; t-value (drug-dose level) or slope (per drug-dose x line: log2 change per unit weight, i.e. ~
the targets' signed mean change relative to the other genes). Second method (drug-dose level only): mean_z = the mean
of weight x DD_z over the TF's targets (no centring, no fit). TP53 (MDM2, CDKN1A out) = TP53's CollecTRI regulon without
the two positive-control targets. Drug-doses: the atlas's 1,132 minus unreliable-plate-only and
position-not-correctable ones (1,086). TP53 groups: the gene panel's (17 WT, 33 altered). TRIM72 versions: TRIM72
(atlas DD_z; per line: r2), TRIM72_rt (two_way's readthrough correction: per (well, line) TRIM72 r2 minus its within
drug-dose and line fit on FUS r2 and PYCARD-AS1 r2, then well median over lines, robust z over reliable drug wells / the
TRIM72 plate factor, Stouffer over the drug-dose's used wells), TRIM72_rt_across (TRIM72 z with FUS z and PYCARD-AS1 z
partialled out of both sides: removes everything TRIM72 shares with its locus neighbours across drug-doses, genuine
co-regulation included). p = permutation-calibrated normal p (observed / SD of the null), q_bh = Benjamini-Hochberg
within the family named. Drug-dose CIs (A1): r +- 1.96 x se_for_ci, se_for_ci = the larger of null_sd_drug_block and
se_jackknife_drug (drug-doses of one drug are correlated; the iid Fisher SE 1/sqrt(n - 3 - k), ~0.031 here, is too
small and is no longer reported). The drug-block null SD is the SD of r under no association, the jackknife SE the
spread of r when one drug's drug-doses are left out (covariates partialled once on all drug-doses); p stays the
permutation-calibrated p (a test of no association), so a CI can be wider than p alone suggests.

a0_regulon_sizes.csv      per source and TF: targets in the database, targets among the atlas genes outside the locus
                          (used), TF mRNA in the atlas (median line CPM, lines expressing).
a0_regulons_used.csv.gz   every (source, TF, target) edge read, with weight, target in the atlas, target in the locus.
a0_tf_edges_to_trim72_locus.csv  the database edges TF -> TRIM72 or a locus gene (all removed before any test).
a0_readthrough_fit.csv    TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (two_way's correction, here on
                          the 1,086 drug-doses): slopes, drug-cluster SE, within R2.
a1_tf_activity_by_drugdose.csv.gz  CollecTRI ULM t per drug-dose (rows: drug, conc) and TF (columns).
a1_dd_tf_vs_trim72.csv.gz one row per source (CollecTRI_t primary; CollecTRI_mean_z = the second method;
                          CollecTRI_lfc_slope; DoRothEA_t; TF_mRNA_z = the TF's own mRNA) x TF x trim72_version x variant
                          (raw; covariates = intercept + log n significant genes, cell loss, UMI / cell, genes / cell,
                          composition shift, S, G2M and proteasome z, RMS z over genes; minus_3pc / minus_10pc = top 3 /
                          10 PC scores of the standardised DD_z gene matrix partialled). r = partial Pearson r across
                          drug-doses; ci_lo / ci_hi = the drug CI above; null_sd_drug_block = SD of r when whole drugs are
                          swapped (drugs with the same dose set; keeps a drug's doses together); se_jackknife_drug; p
                          (calibrated), p_perm_empirical, q_bh (over TFs within source x version x variant),
                          rho_spearman_partial and p_spearman (ranks; t approximation), pct_vs_matched_genes = percentile
                          of r among the r of 300 random genes of TRIM72's expression level (2x; >= 45 lines; same TF,
                          same variant): ~50 = the TF tracks such genes as much as TRIM72; pct_abs_* the same for |r|
                          (these genes are about as drug-responsive as TRIM72: checks.csv); pct_vs_all_genes /
                          rank_vs_all_genes (CollecTRI_t; TRIM72 and TRIM72_rt; not raw): where TRIM72's r sits among
                          the r of the same TF activity with every gene of the universe (the TF's own targets included):
                          ~100 / rank 1 = TRIM72 tracks the TF like its best-tracking genes.
a1_matched_genes_reference.csv  how strongly the 300 matched random genes themselves track TRIM72 (per version x variant).
a1_pc_variance.csv        the top PCs of the standardised DD_z gene matrix: variance explained, r with TRIM72 z.
a1_regulon_overlap_control.csv  TRIM72 z vs each CollecTRI TF's ULM t (covariates, drug-block null, drug CI) in four
                          variants: the reference (full regulon; = a1 covariates), minus_overlap_targets (every target
                          that is also a target of AP1, of the AP-1 single proteins JUN / JUNB / JUND / FOS / FOSB /
                          FOSL1 / FOSL2 or of ATF3, and every immediate-early gene (IEG list in checks.csv), taken out of
                          the TF's regulon; TFs left with < 5 targets drop out), plus_mediators_partialled (ATF3 z,
                          PMAIP1 z, DDIT3 z, the mean z of the IEGs and the AP1 ULM t partialled from both sides, with the
                          covariates), and both; n_targets / n_targets_used, r_reference, q_bh over TFs within variant.
                          It asks whether a TF tracks TRIM72 only through the shared AP-1 / IEG / ATF3 stress arm.
a1_plate_batch_split.csv  TRIM72 z vs CollecTRI_t and CollecTRI_mean_z (covariates) in all 1,086 drug-doses and
                          separately in the drug-doses whose used wells are all on the high-TRIM72 plates (1-3 and 14;
                          in practice 1-3: high_plates_only, 250), all on the low-TRIM72 plates (4-12: low_plates_only,
                          735) or on both (mixed_plates, 101: mostly the plate 6 + plate 14 replicates); each subset
                          with its own drug-block permutations, BH within source x subset; n_drugs. TRIM72's untreated
                          level is ~10x lower on plates 4-13 (13 is unreliable and out), so a TF that tracks TRIM72 only
                          in one batch would point to a plate artefact.
a2_within_line_tf_vs_trim72.csv.gz  per TF x trim72_version (TRIM72 r2; TRIM72_rt r2) x covset (full = DD_beta (0 where
                          the drug-dose has no consensus), DD_A, S and G2M per-line effects, mean |r2| over the line's
                          genes, each x TP53 group: 47 lines, NCI-H2122 and NCI-H596 have no DD_A; none = fixed effects
                          only: 49 lines, NCI-H661 has no TRIM72 r2): Y = TRIM72 per (drug-dose, line), X = the
                          TF's ULM slope per (drug-dose, line) (mean over the used wells), drug-dose and line fixed
                          effects. n_rows / n_lines (they differ by TF: a TF's slope is missing where a line expresses
                          < 5 of its targets), b (log2 TRIM72 per unit activity), b_per_sd_tf (per SD of the residual
                          activity), r_partial_within, drug-cluster and two-way (drug, line) cluster SE / CI / p,
                          q_bh_twoway (over TFs); b_WT, b_alt and their difference with line-cluster SE (p_diff_line,
                          q_bh_diff_line, mde_diff_80_line) and drug-cluster SE. Rows = drug-dose x line cells with TRIM72
                          and all covariates present.
a2_noise_ceiling_genes.csv  the same model with X = a single gene's r2 (FOS, EGR1, JUN, ATF3, FUS, PMAIP1, DDIT3; columns
                          as a2, 'gene' for 'tf'): how large a within-line r TRIM72 reaches with its strongest
                          co-responding genes, i.e. the ceiling against which the TF activities' within-line r are read
                          (TRIM72 has ~5 counts per well x line, so its r2 is noisy). For TRIM72_rt the FUS row is ~0 by
                          construction (FUS is regressed out of it).
a1a2_tf_summary.csv       one row per CollecTRI TF: the drug-dose results (own, rt, rt_across; raw / covariates / PCs;
                          pct_vs_matched_* and pct_vs_all_genes_* as in a1; the drug CI of the covariates r), the second
                          method (r / q_mean_z_dd_TRIM72_covariates) and the ranks: rank_pos_* (1 = largest positive r)
                          and rank_neg_* (1 = most negative r) under ULM (rank_*_ulm) and mean z (rank_*_mean_z), and
                          rank_*_method_robust = the worse (larger) of the two; the overlap control (r / q
                          _dd_TRIM72_minus_overlap, _plus_mediators, _minus_overlap_plus_mediators; n_targets_minus_overlap)
                          and the plate-batch split (r / q _dd_TRIM72_high_plates_only, _low_plates_only), DoRothEA and
                          TF-mRNA r (covariates; DoRothEA has no AP1 / NFKB: their row shows the family member with the
                          largest |r|), within-line results (own and rt, full covariates; within_n_rows / within_n_lines),
                          the WT - altered slope difference, and flags: tracks_TRIM72_all_tests (q < 0.1 and the same sign
                          in the drug-dose covariates, minus_3pc and minus_10pc tests, the drug-dose rt covariates test,
                          and within lines, own and rt), lists_TRIM72_as_target (CollecTRI / DoRothEA), muscle_TF,
                          tf_gene_in_trim72_locus (the TF's own mRNA sits within 200 kb of TRIM72, so its mRNA r is
                          readthrough-exposed).
a3_tp53_positive_control.csv  TP53 activity (full CollecTRI regulon; MDM2 / CDKN1A out; only its activated targets,
                          MDM2 / CDKN1A out: the repressed targets are mostly cell-cycle genes) vs MDM2 z, CDKN1A z and the
                          panel's P53_ACTIVITY z across drug-doses (partial r, covariates; drug-block null), and within
                          lines (Y = MDM2 / CDKN1A r2, X = the TP53 activities without MDM2 / CDKN1A, same model as a2:
                          n, n_lines, b_WT, b_alt, difference); TP53 activity per line in WT minus altered lines across
                          the panel's p53-activating drug-doses (P53_ACTIVITY z >= 5) vs all other drug-doses.
a4_muscle_promoter_tfs.csv  MYOD1, MYOG, MYF5, MYF6, MEF2A-D, SRF: in which source, regulon size, whether the source
                          lists TRIM72 as a target, untreated mRNA (atlas median line CPM / lines expressing, or DMSO CPM
                          from the pseudobulk for genes below the atlas list), drug-dose and within-line association with
                          TRIM72, baseline activity vs the line outcomes (q = the b2 headline q_bh).
b1_line_outcomes.csv      per line: TRIM72 untreated level (log2 observed / expected DMSO counts, reliable plates; also
                          plates 1-3 and 14 vs 4-12 separately), its counts / expected counts, TRIM72 r2 under idarubicin
                          5 uM and homoharringtonine 5 uM (mean of the 2 wells, and each well), the mean induction, each
                          induction adjusted for the untreated level (*_adj_untreated: residual of a linear fit on
                          TRIM72_untreated_rel; how much this removes differs by raiser, see below), FUS / PYCARD-AS1
                          untreated level, TP53 group, organ, drivers.
b2_line_feature_tests.csv one row per outcome x feature (tested over the lines where both are present): families tp53,
                          lineage (each organ with >= 3 lines vs the rest; Kruskal-Wallis over all organs, 2,000
                          permutations), drivers (genes altered in 4 to 46 of the lines, cell_line_metadata; TP53 left
                          to the tp53 family; plus 'n driver genes altered', the number of driver genes a line has
                          altered), baseline_tf (ULM t of CollecTRI TFs on the line's untreated within-plate relative
                          expression), locus (FUS, PYCARD-AS1 untreated level). rho = Spearman (binary features:
                          rank-biserial-type r of rank(y) with 0/1) with CI (Fisher, x1.06), p calibrated by 10,000 label
                          permutations, empirical p, organ-adjusted r (organ means out of both; within-organ permutation
                          p, 5,000 permutations); q_bh = BH over every outcome x feature test of the table (5,075: the
                          headline, the most conservative), q_bh_outcome = BH over every test of the outcome (725, all
                          families), q_bh_family = BH within outcome x family (the q_bh of the earlier version; the least
                          conservative: e.g. KMT2D vs the untreated level 0.007 there, 0.046 within the outcome, 0.12
                          over all line tests); binary features also: n and mean / median per group, mean difference
                          with Welch CI, MDE in SD units; mde_rho_80 = smallest |rho| detectable with 80% power at
                          two-sided 5% (one test; with BH over many tests larger).
b3_baseline_tf_activity_per_line.csv  lines x CollecTRI TFs: ULM t of the untreated within-plate relative expression.
checks.csv                pass reconstruction vs the atlas (W1 per plate, TRIM72 drug-dose log2FC and z), DMSO TRIM72 counts
                          vs gene_panel well_line, idarubicin per-line TRIM72 vs trim72_idarubicin/corrected, regulon
                          and locus bookkeeping (AP1 / NFKB merge, the overlap-control gene set and IEGs, plate-batch
                          subsets), the TP53 controls available, untreated TRIM72 line ranking high- vs low-baseline
                          plates, each raiser's induction vs the untreated level (rho, R2, well-to-well rho after the
                          adjustment), KMT2D vs the untreated level with the driver-count controls.
key_results.csv           the headline numbers (A2 rows give n rows / n lines per TF).
run_info.json             downloads (status, date, md5 of the regulon files), regulon sizes, runtime, peak memory (getrusage
                          or psutil, whichever is larger) and whether the pass came from the cache.

What the tables say (numbers from key_results.csv and the tables named; all associations in mRNA)
- Across drug-doses (a1, CollecTRI ULM t, TRIM72 z, covariates): 348 of 679 TFs track TRIM72 positively and 125
  negatively at q < 0.1; the strongest, ATF5 and ATF4 (r 0.36, drug CI 0.29-0.43 and 0.28-0.44), TWIST1, GCM1, TWIST2,
  sit at the 99th-100th percentile of 300 expression-matched genes. The drug CIs are ~1.3x wider than the iid Fisher
  CIs reported before (median SE 0.040 vs 0.031; the drug jackknife SE is the larger for 626 of 679 TFs): 409 of 679
  TFs have a CI that excludes 0 (459 of 667 with the Fisher CI), and 64 of the 473 TFs at q < 0.1 (either sign) have a
  CI that includes 0 (their p rests on the null SD, which the jackknife SE exceeds); read those as weak.
- Second method (mean signed target z): r across TFs 0.86 with the ULM r. Method-robust top (the worse of the two
  ranks): TWIST2, TWIST1, ATF5, ATF4, CREBBP, APEX1, ASCL1, PBRM1, XBP1, ZNF91; bottom: YBX3, NFIL3, NAB2, MYF6, RB1.
- Regulon overlap (a1_regulon_overlap_control): much of the top associations runs through the shared AP-1 / IEG / ATF3
  stress arm. Taking the AP-1 / ATF3 targets and IEGs out of the regulons lowers r by a median 0.12 over the 50
  highest-r TFs (ATF5 0.36 -> 0.00, ATF4 0.36 -> 0.22; 13 of the 50 keep < 5 targets); with ATF3, PMAIP1, DDIT3, the
  IEG score and AP1 activity also partialled the median drop is 0.18 (ATF4 0.09, XBP1 0.04, HSF1 0.07, CREB1 0.08), and
  22 of the 37 testable ones still track TRIM72 at q < 0.1 (e.g. ZNF91 0.32, TWIST1 0.21, APEX1 0.17, SRF 0.17).
  AP1, NFKB and TP53 activity lose their positive association (TP53 0.12 -> -0.18 with the mediators partialled).
  None of this makes a TF a regulator of TRIM72: these are co-responders to the same drugs.
- Plate batch (a1_plate_batch_split): the top TFs track TRIM72 in both batches (ATF4 0.37 / 0.37, ATF5 0.32 / 0.35,
  ELK4 0.31 / 0.36 on the high- / low-TRIM72 plates), but over all TFs the two batches agree only moderately (r 0.47
  across TFs; 250 drug-doses of 88 drugs vs 735 of 276); AP1 (0.08 / 0.23), ASCL1 (0.14 / 0.33) and CREB1 (0.15 / 0.28)
  come mostly from the low plates.
- Within lines (a2): 187 of 679 TFs at q < 0.1 (57 positive), all with |r| <= 0.08 (MYBL1 0.071, E2F4 -0.080); ATF4,
  ATF5, XBP1, AP1 are ~0 within lines (|r| <= 0.02). The noise ceiling (a2_noise_ceiling_genes) is of the same size:
  TRIM72's within-line r with its best single co-responders is FOS 0.080, EGR1 0.067, FUS 0.066, JUN 0.063, ATF3 0.062,
  so a within-line r of ~0.07 is about as large as TRIM72's noisy per-line values allow; ATF4, ATF5 and XBP1 stay far
  below it (|r| <= 0.01): their drug-dose association does not carry over to line-to-line differences within a
  drug-dose. No TF's slope differs between TP53-WT and altered lines (q_bh_diff_line >= 0.1 for all).
- Inducibility vs the untreated level, per raiser: idarubicin 5 uM induction is strongly tied to a line's untreated
  TRIM72 level (rho -0.79, linear R2 0.34: low-baseline lines get larger folds; the well-to-well rho drops from 0.63 to
  0.38 once it is removed), homoharringtonine 5 uM only weakly (rho -0.33, R2 0.10; well-to-well rho 0.82 raw, 0.81
  after removal): the homoharringtonine induction is a reproducible line property that the untreated level hardly
  explains, while much of the idarubicin per-line fold is the low-baseline effect.
- Line features (b2, headline q over all 5,075 line tests): only the locus (PYCARD-AS1 rho 0.82 and FUS 0.57 with the
  untreated level; PYCARD-AS1 -0.63 with the idarubicin induction) and two baseline TF activities for the idarubicin
  induction (NFKBIB, TP73) reach q < 0.1. KMT2D-altered lines (14) have a higher untreated level (rho 0.54, p 0.0002):
  q 0.046 within the untreated outcome, 0.12 over all line tests (0.007 within the 37 driver tests only). It is not
  explained by the number of altered driver genes (rho partial on that number 0.49; random line sets of the same size
  drawn in proportion to driver count reach it with P 0.0008), so the 'hypermutation marker' reading is not supported;
  it remains an unexplained, unreplicated association. TP53 group: nominal only for the untreated-adjusted idarubicin
  induction (WT ranked higher, rho 0.30, p 0.04; q 0.38 over all line tests), none for the other six outcomes.
- The locus link (TRIM72's untreated level following PYCARD-AS1 and FUS across lines) fits readthrough from FUS, but a
  line's 16p11.2 copy number would raise all genes of the region together and give the same pattern; Tahoe has no
  copy-number data to tell them apart.
"""


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild the pseudobulk pass cache")
    ap.add_argument("--offline", action="store_true", help="no downloads (cached files or fallbacks)")
    ap.add_argument("--perm", type=int, default=1000, help="drug-block permutations (drug-dose level)")
    ap.add_argument("--line-perm", type=int, default=10000, help="label permutations (line features)")
    ap.add_argument("--quick", action="store_true", help="few permutations (a test run)")
    a = ap.parse_args()
    if a.quick:
        a.perm, a.line_perm = 100, 1000
    t_start = time.time()
    out = os.environ.get("MG53_OUT") or HERE
    cdir, tab = os.path.join(out, "cache"), os.path.join(out, "tables")
    ext = os.path.join(cdir, "external")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(tab, exist_ok=True)
    rng = np.random.default_rng(SEED)
    log(f"data {a.data}; out {out}")
    ctx = Ctx(a.data)
    checks = []

    def add(check, value, n=np.nan, note=""):
        checks.append({"check": check, "value": value, "n": n, "note": note})

    # ------------------------------------------------------------------ regulons and the locus
    status = fetch(ext, a.offline)
    log("downloads: " + "; ".join(f"{k} {v}" for k, v in status.items()))
    locus, locus_src = locus_genes(ext)
    ltoks = {ctx.ens_tok[e] for e in locus if e in ctx.ens_tok}
    excl = np.isin(ctx.gtok, list(ltoks)) | np.isin(ctx.gsym, [s for s in locus.values() if s])
    ctx.excl = excl
    add("TRIM72 locus genes (+- 200 kb) left out of regulons and universe: in the atlas gene list", int(excl.sum()),
        len(locus), f"{locus_src}; atlas genes: {', '.join(ctx.gsym[excl])}")
    regs = {}
    for src, fn in (("CollecTRI", "collectri.tsv"), ("DoRothEA_ABC", "dorothea_ABC.tsv")):
        p = os.path.join(ext, fn)
        try:
            regs[src] = read_regulon(p, src)
        except (OSError, ValueError, KeyError) as err:
            log(f"WARNING: {src} not usable ({err})")
    if "CollecTRI" not in regs:      # no fallback: every analysis here is regulon-based; stop before the long pass
        sys.exit(f"upstream_tf: the CollecTRI regulons are not available ({status.get('collectri.tsv')}), so no "
                 "analysis was run (nothing written to tables/).\nThis step needs the CollecTRI TF -> target network "
                 "from OmniPath. Either run it once with internet access (curl or Python urllib, through $HTTPS_PROXY "
                 f"if set), or download\n  {COLLECTRI_URL}\non a machine with access and save it as\n  "
                 f"{os.path.join(ext, 'collectri.tsv')}\n(optionally DoRothEA as dorothea_ABC.tsv from {DOROTHEA_URL}), "
                 "then rerun (add --offline to skip download attempts).")
    reg_all = pd.concat(regs.values(), ignore_index=True)
    locus_syms = set(s for s in locus.values() if s) | {GENE}
    edges = reg_all[reg_all["target"].isin(locus_syms)].copy()
    edges["target_is_TRIM72"] = edges["target"].eq(GENE)
    edges.sort_values(["target_is_TRIM72", "target", "source", "tf"], ascending=[False, True, True, True]).to_csv(
        os.path.join(tab, "a0_tf_edges_to_trim72_locus.csv"), index=False)
    lists_trim72 = set(edges.loc[edges["target_is_TRIM72"], "tf"])
    log(f"TFs listed as regulating TRIM72: {sorted(lists_trim72)}")
    W, tfs, ntar = regulon_matrix(regs["CollecTRI"], ctx, excl)
    if not tfs:
        sys.exit("upstream_tf: no CollecTRI TF has >= 5 targets among the atlas genes; check cache/external/collectri.tsv")
    tp = regs["CollecTRI"]
    ctrl = tp[(tp["tf"] == "TP53") & ~tp["target"].isin(P53_CTRL)].assign(tf=TP53_CTRL_TF)
    ctrl = pd.concat([ctrl, ctrl[ctrl["weight"] > 0].assign(tf=TP53_ACT_TF)])
    Wc, tfc, ntc = regulon_matrix(ctrl, ctx, excl)
    Wp = sparse.hstack([W, Wc]).tocsr()
    tfs_p = tfs + tfc
    if "TP53" not in tfs or len(tfc) < len(CTRL_TFS):
        log(f"WARNING: TP53 control regulons incomplete (TP53 in CollecTRI: {'TP53' in tfs}; controls: {tfc}); "
            "the A3 rows that need them are skipped")
    Wd, tfs_d, ntar_d = regulon_matrix(regs["DoRothEA_ABC"], ctx, excl) if "DoRothEA_ABC" in regs else (None, [], [])
    log(f"regulons: CollecTRI {len(tfs)} TFs with >= {TMIN} targets ({int(W.nnz)} edges); DoRothEA A-C {len(tfs_d)}")
    g_at = ctx.fx.genes.iloc[ctx.gcol].set_index("symbol")
    rs_rows = []
    for src, tl, nt in (("CollecTRI", tfs, ntar), ("DoRothEA_ABC", tfs_d, ntar_d)):
        dbn = regs[src].groupby("tf").size() if src in regs else pd.Series(dtype=float)
        for t_, k in zip(tl, nt):
            rs_rows.append({"source": src, "tf": t_, "targets_in_database": int(dbn.get(t_, 0)),
                            "targets_used": int(k), "tf_mRNA_in_atlas": t_ in ctx.gidx,
                            "tf_median_line_cpm": float(g_at["median_line_cpm"].get(t_, np.nan))
                            if t_ in ctx.gidx else np.nan,
                            "tf_n_lines_expressing": float(g_at["n_lines_expressing"].get(t_, np.nan))
                            if t_ in ctx.gidx else np.nan})
    pd.DataFrame(rs_rows).to_csv(os.path.join(tab, "a0_regulon_sizes.csv"), index=False, float_format="%.4g")
    reg_out = reg_all.copy()
    reg_out["target_in_atlas"] = reg_out["target"].isin(ctx.gidx)
    reg_out["target_in_trim72_locus"] = reg_out["target"].isin(locus_syms)
    fam_tfs = [t_ for t_ in sorted(AP1 | NFKB) if t_ in tfs]
    add("CollecTRI TFs with >= 5 targets (atlas genes, locus out)", len(tfs), int(W.nnz),
        "AP1 / NFKB = the COMPLEX sources of AP-1 / NF-kB members only (decoupler); single-protein family members "
        f"kept as TFs: {', '.join(fam_tfs)}; AP1 targets used {int(ntar[tfs.index('AP1')]) if 'AP1' in tfs else 0}, "
        f"NFKB {int(ntar[tfs.index('NFKB')]) if 'NFKB' in tfs else 0}")
    add("DoRothEA A-C TFs with >= 5 targets", len(tfs_d), int(Wd.nnz) if Wd is not None else 0,
        "" if Wd is not None else "DoRothEA not available: its rows are left out")

    # ------------------------------------------------------------------ the pass
    sel = [GENE] + [g for g in SEL_EXTRA if g in ctx.gidx]
    hsh = hashlib.md5()
    for arr in (Wp.indptr, Wp.indices, Wp.data, excl.astype(np.int8)):
        hsh.update(np.ascontiguousarray(arr).tobytes())
    hsh.update(("|".join(tfs_p) + "|".join(sel) + PASS_VERSION).encode())
    key = hsh.hexdigest()[:12]
    if a.recompute:
        for f in glob.glob(os.path.join(cdir, "pass_*.npz")):
            os.remove(f)
    for f in glob.glob(os.path.join(cdir, "pass_*.npz")):
        if not f.endswith(f"pass_{key}.npz"):
            os.remove(f)                                    # a stale pass (regulons changed)
    P_ = build_pass(ctx, Wp, tfs_p, sel, excl, cdir, key)
    t_pass = time.time() - t_start
    val = pd.DataFrame(json.loads(str(P_["validation"])))
    add("pass: per-well W1 (median over lines of r1) vs atlas W1.npy, max |diff| over all plates",
        float(val["W1_max_abs_diff_vs_atlas"].max()), int(val["W1_cells_both_finite"].sum()),
        f"finite here not in atlas {int(val['W1_finite_here_not_atlas'].sum())}; finite in atlas not here "
        f"{int(val['W1_finite_atlas_not_here'].sum())}")
    selw = P_["selw"].astype(np.float64)
    sel = [str(s) for s in P_["sel"]]
    sj = {s: k for k, s in enumerate(sel)}
    tf_dd = P_["tf_dd"]
    tfs_p = [str(s) for s in P_["tfs"]]

    # PYCARD-AS1 (below the atlas gene list): corrected_effects() on its counts, kept in every line (as two_way)
    exs = [str(s) for s in P_["extra"]]
    with quiet():
        _r1, r2p, _W2, _zw, _per, ddl_p, ddz_p = corrected_effects(
            ctx.fx, P_["exw"][:, :, [exs.index("PYCARD-AS1")]].astype(np.float64), P_["tot"], P_["nc"], None)
    pyc_w = r2p[:, :, 0].astype(np.float64)
    del _r1, _W2, _zw, _per

    # per (drug-dose, line) values
    trim_w = selw[:, :, sj[GENE]]
    fus_w = selw[:, :, sj["FUS"]]
    trim_dd = ctx.dd_mean(trim_w).astype(float)
    fus_dd = ctx.dd_mean(fus_w).astype(float)
    pyc_dd = ctx.dd_mean(pyc_w).astype(float)
    # readthrough fit (two_way's): TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line
    ok = clean_ok(np.isfinite(trim_dd) & np.isfinite(fus_dd) & np.isfinite(pyc_dd) & ctx.keep[:, None])
    d_, l_ = np.nonzero(ok)
    fe = TW.FE(d_, l_)
    MX = fe.M(trim_dd[d_, l_])
    MF = fe.M(np.column_stack([fus_dd[d_, l_], pyc_dd[d_, l_]]))
    bread = np.linalg.inv(MF.T @ MF)
    s_rt = bread @ (MF.T @ MX)
    e_rt = MX - MF @ s_rt
    Vrt, Grt = TW.cluster_vcov(MF, e_rt, ctx.drug_id[d_], bread, len(d_), 2 + len(fe.du) + len(fe.lu) - 1)
    rtfit = pd.DataFrame([{"predictor": nm, "slope": s_rt[i], "se_drug": np.sqrt(Vrt[i, i]),
                           "p_drug": TW.tp(s_rt[i], np.sqrt(Vrt[i, i]), Grt - 1), "n_rows": len(d_),
                           "n_drugdoses": len(fe.du), "n_lines": len(fe.lu),
                           "within_R2_of_TRIM72": float(1 - (e_rt @ e_rt) / (MX @ MX))}
                          for i, nm in enumerate(["FUS_r2", "PYCARD-AS1_r2"])])
    rtfit.to_csv(os.path.join(tab, "a0_readthrough_fit.csv"), index=False, float_format="%.6g")
    rt_w = trim_w - s_rt[0] * fus_w - s_rt[1] * pyc_w
    rt_dd = ctx.dd_mean(rt_w).astype(float)

    # drug-dose level z of TRIM72 (check) and of TRIM72_rt: well median over lines -> robust z (reliable drug wells,
    # TRIM72's plate factor) -> Stouffer over the used wells
    fx = ctx.fx
    tcol = int(ctx.gcol[ctx.j_trim])
    fscale = fx.gene_scale([tcol])[:, 0]

    def dd_z_of(Vw):
        with quiet():
            Wv = np.nanmedian(Vw, axis=1)
            Wv[np.isfinite(Vw).sum(axis=1) < A.MIN_LINES] = np.nan
        c, s = A.robust_cols(Wv[:, None], fx.ref_w)
        zw = (Wv - c[0]) / (s[0] * fscale)
        lfc = np.full(ctx.nd, np.nan)
        z = np.full(ctx.nd, np.nan)
        for d, ii in fx.wells_of_dd.items():
            if len(ii):
                with quiet():
                    lfc[d] = np.nanmean(Wv[ii])
                f = np.isfinite(zw[ii])
                z[d] = np.nansum(zw[ii]) / np.sqrt(max(f.sum(), 1)) if f.any() else np.nan
        return lfc, z
    lfc_t, z_t = dd_z_of(trim_w)
    lfc_rt, z_rt = dd_z_of(np.where(np.isfinite(fus_w) & np.isfinite(pyc_w), rt_w, np.nan))
    DDl = np.load(os.path.join(ctx.fxd, "DD_lfc.npy"), mmap_mode="r")
    DDz = np.load(os.path.join(ctx.fxd, "DD_z.npy"), mmap_mode="r")
    at_l, at_z = np.asarray(DDl[:, tcol], float), np.asarray(DDz[:, tcol], float)
    mm = np.isfinite(at_l) & np.isfinite(lfc_t)
    add("TRIM72 drug-dose log2FC rebuilt from the pass vs atlas DD_lfc, max |diff|", float(np.max(np.abs(
        at_l[mm] - lfc_t[mm]))), int(mm.sum()))
    mm = np.isfinite(at_z) & np.isfinite(z_t)
    add("TRIM72 drug-dose z rebuilt from the pass (well median, robust z, gene plate factor, Stouffer) vs atlas DD_z, "
        "max |diff|", float(np.max(np.abs(at_z[mm] - z_t[mm]))), int(mm.sum()),
        f"Pearson r {np.corrcoef(at_z[mm], z_t[mm])[0, 1]:.6f}")
    kk = ctx.keep & np.isfinite(z_rt) & np.isfinite(at_z)
    add("TRIM72_rt z vs TRIM72 z across the analysed drug-doses, Pearson r", float(np.corrcoef(z_rt[kk], at_z[kk])[0, 1]),
        int(kk.sum()))
    add("analysed drug-doses without a TRIM72_rt z (set to 0 in A1)", int((ctx.keep & ~np.isfinite(z_rt)).sum()),
        int(ctx.keep.sum()))

    # ------------------------------------------------------------------ A1 across drug-doses
    keep = np.flatnonzero(ctx.keep)
    n_k = len(keep)
    dd = ctx.dd
    Zk = np.nan_to_num(np.asarray(DDz[keep][:, ctx.gcol], dtype=np.float64))
    Lk = np.nan_to_num(np.asarray(DDl[keep][:, ctx.gcol], dtype=np.float64))
    Zk_u = np.where(excl[None, :], np.nan, Zk)
    Lk_u = np.where(excl[None, :], np.nan, Lk)
    ulm_c = ULM(Wp)
    _b, t_col, _n = ulm_c(Zk_u)
    b_lfc, _t, _n = ulm_c(Lk_u, want_t=False)
    # second activity method: mean signed target z (weight x z averaged over the TF's targets; missing z count as 0,
    # as in the ULM input)
    n_tg = np.asarray(abs(W).sum(axis=0)).ravel()
    mean_z = np.asarray(W.T @ Zk.T).T / np.where(n_tg > 0, n_tg, np.nan)[None, :]
    acts = {"CollecTRI_t": (t_col[:, :len(tfs)], tfs), "CollecTRI_mean_z": (mean_z, tfs),
            "CollecTRI_lfc_slope": (b_lfc[:, :len(tfs)], tfs)}
    if Wd is not None:
        _b, t_d, _n = ULM(Wd)(Zk_u)
        acts["DoRothEA_t"] = (t_d, tfs_d)
    mr = [t_ for t_ in tfs if t_ in ctx.gidx]
    acts["TF_mRNA_z"] = (Zk[:, [ctx.gidx[t_] for t_ in mr]], mr)
    pd.DataFrame(t_col[:, :len(tfs)], columns=tfs).assign(drug=dd["drug"].to_numpy()[keep],
                                                           conc=dd["conc"].to_numpy()[keep]).set_index(
        ["drug", "conc"]).to_csv(os.path.join(tab, "a1_tf_activity_by_drugdose.csv.gz"), float_format="%.4g")
    ddk = dd.iloc[keep]
    cov_df = pd.DataFrame({"log_n_sig": np.log1p(ddk["n_sig_genes"].fillna(0).to_numpy(float)),
                           "cells": ddk["cells_log2_vs_plate"].fillna(0).to_numpy(float),
                           "umi": ddk["umi_per_cell_log2_vs_plate"].fillna(0).to_numpy(float),
                           "genes_pc": ddk["genes_per_cell_log2_vs_plate"].fillna(0).to_numpy(float),
                           "comp": ddk["composition_shift_log2"].fillna(0).to_numpy(float),
                           "S": ddk["S_PHASE_z"].fillna(0).to_numpy(float),
                           "G2M": ddk["G2M_PHASE_z"].fillna(0).to_numpy(float),
                           "PROT": ddk["PROTEASOME_z"].fillna(0).to_numpy(float),
                           "rms_z": np.sqrt((Zk ** 2).mean(axis=1))})
    fus_z = Zk[:, ctx.gidx["FUS"]]
    pyc_z = np.nan_to_num(np.asarray(ddz_p[keep, 0], dtype=float))
    xvers = {"TRIM72": Zk[:, ctx.j_trim], "TRIM72_rt": np.nan_to_num(z_rt[keep]),
             "TRIM72_rt_across": Zk[:, ctx.j_trim]}
    mref = []
    A1, pcs, U, perms = dd_level(ctx, acts, xvers, cov_df, np.column_stack([fus_z, pyc_z]), a, rng, mref)
    A1.to_csv(os.path.join(tab, "a1_dd_tf_vs_trim72.csv.gz"), index=False, float_format="%.5g")
    rms = np.sqrt((Zk ** 2).mean(axis=0))
    g_ = ctx.fx.genes.iloc[ctx.gcol]
    lvl, nle = g_["median_line_cpm"].to_numpy(float), g_["n_lines_expressing"].to_numpy(float)
    lt_ = lvl[ctx.j_trim]
    cand = (lvl >= lt_ / 2) & (lvl <= lt_ * 2) & (nle >= 45) & ~excl
    add("TRIM72 responsiveness (RMS of DD_z over the analysed drug-doses): percentile among the universe genes",
        float(100 * np.mean(rms[~excl] < rms[ctx.j_trim])), int((~excl).sum()),
        f"TRIM72 RMS z {rms[ctx.j_trim]:.3f}; level-matched candidate genes (the matched null's pool) median "
        f"{np.median(rms[cand]):.3f} (n {int(cand.sum())}): the level-matched null is also roughly "
        "responsiveness-matched")
    pd.DataFrame(mref).to_csv(os.path.join(tab, "a1_matched_genes_reference.csv"), index=False, float_format="%.4g")
    pcs.to_csv(os.path.join(tab, "a1_pc_variance.csv"), index=False, float_format="%.4g")
    drug_k = ctx.drug_id[keep]
    C_ = cov_df.to_numpy(float)
    y_t = xvers["TRIM72"]

    # regulon-overlap control: AP-1 (complex and single members) and ATF3 targets and the IEGs out of every regulon;
    # ATF3 / PMAIP1 / DDIT3 z, an IEG score and AP1 activity partialled
    ov_tfs = [t_ for t_ in ["AP1", "ATF3"] + sorted(AP1) if t_ in tfs]
    ov_j = set(np.flatnonzero(np.asarray(abs(W[:, [tfs.index(t_) for t_ in ov_tfs]]).sum(axis=1)).ravel() > 0))
    ieg_j = [ctx.gidx[g] for g in IEG if g in ctx.gidx and not excl[ctx.gidx[g]]]
    ov_j = np.array(sorted(ov_j | set(ieg_j)), dtype=int)
    ieg_score = Zk[:, ieg_j].mean(axis=1)
    med_names = [g for g in MEDIATOR_GENES if g in ctx.gidx] + [f"IEG score (mean z of {len(ieg_j)} IEGs)"] + \
        (["AP1 activity (CollecTRI ULM t)"] if "AP1" in tfs else [])
    med = np.column_stack([Zk[:, ctx.gidx[g]] for g in MEDIATOR_GENES if g in ctx.gidx] + [ieg_score] +
                          ([t_col[:, tfs.index("AP1")]] if "AP1" in tfs else []))
    OV = overlap_control(W, tfs, Zk_u, y_t, C_, med, ov_j, perms, drug_k)
    OV.to_csv(os.path.join(tab, "a1_regulon_overlap_control.csv"), index=False, float_format="%.4g")
    add("regulon-overlap control: genes taken out of every regulon (targets of " + ", ".join(ov_tfs) +
        " in the universe, plus the IEGs)", len(ov_j), int((~excl).sum()),
        f"IEGs in the atlas: {', '.join(ctx.gsym[ieg_j])}; partialled: {'; '.join(med_names)}")
    log(f"A1 regulon-overlap control: {len(ov_j)} genes out of the regulons")

    # plate-batch split of the drug-dose associations (own drug-block permutations per subset; separate RNG stream so
    # the other analyses' random draws are unchanged)
    subsets = plate_batch_subsets(ctx)
    PB = dd_subset_assoc(ctx, {k_: acts[k_] for k_ in ("CollecTRI_t", "CollecTRI_mean_z")}, y_t, C_, subsets,
                         a.perm, np.random.default_rng([SEED, 2]))
    allr = A1[(A1["trim72_version"] == "TRIM72") & (A1["variant"] == "covariates")
              & A1["source"].isin(["CollecTRI_t", "CollecTRI_mean_z"])].assign(subset="all")
    PB = pd.concat([allr[PB.columns.intersection(allr.columns).tolist()].assign(
        n_drugs=int(len(np.unique(drug_k)))), PB], ignore_index=True)[PB.columns]
    PB.to_csv(os.path.join(tab, "a1_plate_batch_split.csv"), index=False, float_format="%.4g")
    for sname, m in subsets.items():
        add(f"plate-batch split: drug-doses in subset '{sname}'", int(m.sum()), int(len(np.unique(drug_k[m]))),
            "n = drugs")

    # ------------------------------------------------------------------ A2 within lines
    bl = pd.read_csv(os.path.join(a.data, "gene_panel", "results", "baseline_by_cell_line.csv"),
                     dtype={"cell_line_id": str}).set_index("cell_line_id")
    grp = bl["tp53_group"].reindex(ctx.lines)
    wt_line = (grp == "WT").to_numpy()
    beta = np.load(os.path.join(ctx.fxd, "DD_beta.npy")).astype(float)
    beta[np.isnan(beta).all(axis=1)] = 0.0
    Aab = np.load(os.path.join(ctx.fxd, "DD_A.npy")).astype(float)
    mods = np.load(os.path.join(ctx.fxd, "DD_r2_modules.npy")).astype(float)
    bg_dd = ctx.dd_mean(P_["bgw"].astype(float)).astype(float)
    covsets = {"full": [beta, Aab, mods[:, :, 0], mods[:, :, 1], bg_dd], "none": []}
    ys = {"TRIM72": trim_dd, "TRIM72_rt": rt_dd}
    A2 = within_lines(ctx, tf_dd, tfs_p, ys, covsets, wt_line)
    A2.to_csv(os.path.join(tab, "a2_within_line_tf_vs_trim72.csv.gz"), index=False, float_format="%.5g")
    # within-line noise ceiling: TRIM72 r2 vs single co-responding genes' r2, same model
    ng_ = [g for g in NOISE_GENES if g in sj]
    G3 = ctx.dd_mean(selw[:, :, [sj[g] for g in ng_]]).astype(np.float32)
    NC = within_lines(ctx, G3, ng_, ys, covsets, wt_line).rename(columns={"tf": "gene"})
    NC.to_csv(os.path.join(tab, "a2_noise_ceiling_genes.csv"), index=False, float_format="%.5g")
    del G3

    # ------------------------------------------------------------------ A3 TP53 positive control
    pc_rows = []
    # every TP53 control is optional (a CollecTRI table without TP53 skips it; checks.csv says so)
    ctrl_cols = tuple((nm_, tfs_p.index(t_)) for nm_, t_ in (("TP53 (full regulon)", "TP53"),
                                                             (TP53_CTRL_TF, TP53_CTRL_TF), (TP53_ACT_TF, TP53_ACT_TF))
                      if t_ in tfs_p)
    kt = tfs_p.index("TP53") if "TP53" in tfs_p else None
    add("A3 TP53 positive control: TP53 activities available", len(ctrl_cols), len(CTRL_TFS) + 1,
        "; ".join(nm_ for nm_, _k in ctrl_cols) or "none: A3 skipped (no TP53 regulon in CollecTRI)")
    ps = pd.read_csv(os.path.join(a.data, "gene_panel", "results", "pathway_scores_by_dose.csv"))
    ps = ps[ps["score"] == "P53_ACTIVITY"][["drug", "conc", "z"]]
    pz = ddk[["drug", "conc"]].assign(ck=ddk["conc"].round(6)).merge(
        ps.assign(ck=ps["conc"].round(6)).drop_duplicates(["drug", "ck"])[["drug", "ck", "z"]],
        on=["drug", "ck"], how="left")["z"].to_numpy(float)
    for tfname, k_ in ctrl_cols:
        col = t_col[:, k_]
        for yname, yv in (("MDM2 z", Zk[:, ctx.gidx["MDM2"]]), ("CDKN1A z", Zk[:, ctx.gidx["CDKN1A"]]),
                          ("panel P53_ACTIVITY z", pz)):
            m = np.isfinite(yv)
            Qm = qbasis(int(m.sum()), cov_df.to_numpy(float)[m])
            pm = perms[:, m] if m.all() else None
            yr = presid(yv[m], Qm)
            xr = unit_cols(presid(col[m][:, None], Qm))
            if pm is not None:
                r, sd, p_cal, p_emp = perm_test_cols(yr, xr, pm)
            else:
                r = (yr / np.linalg.norm(yr)) @ xr
                sd, p_emp = np.array([np.nan]), np.array([np.nan])
                tt = r * np.sqrt((m.sum() - Qm.shape[1] - 1) / (1 - r ** 2))
                p_cal = 2 * stats.t.sf(np.abs(tt), m.sum() - Qm.shape[1] - 1)
            rraw = np.corrcoef(col[m], yv[m])[0, 1]
            pc_rows.append({"test": "across drug-doses (partial r, covariates)", "tf_activity": tfname,
                            "readout": yname, "n": int(m.sum()), "estimate": float(r[0]), "r_raw": rraw,
                            "p": float(p_cal[0]), "p_perm_empirical": float(p_emp[0]), "null_sd": float(sd[0])})
    for yname in P53_CTRL:                            # the controls whose regulons leave MDM2 and CDKN1A out
        Y = ctx.dd_mean(selw[:, :, sj[yname]]).astype(float)
        for csname, covs in covsets.items():
            for tfname, k_ in [c_ for c_ in ctrl_cols if c_[0] in CTRL_TFS]:
                base = np.isfinite(Y) & ctx.keep[:, None] & np.isfinite(tf_dd[:, :, k_])
                for c in covs:
                    base &= np.isfinite(c)
                o = fe_screen(clean_ok(base), Y, tf_dd[:, :, [k_]], covs, wt_line, ctx.drug_id)[0]
                pc_rows.append({"test": f"within lines (two-way FE, {csname})", "tf_activity": tfname,
                                "readout": f"{yname} r2", "n": o["n_rows"], "n_lines": o["n_lines"],
                                "estimate": o["b"], "p": o["p_twoway"],
                                "b_WT": o["b_WT"], "se_WT_line": o["se_WT_line"], "b_alt": o["b_alt"],
                                "se_alt_line": o["se_alt_line"], "diff_WT_minus_alt": o["diff_WT_minus_alt"],
                                "p_diff_line": o["p_diff_line"], "r_partial_within": o["r_partial_within"]})
    # TP53 activity per line, WT minus altered, in p53-activating drug-doses vs the others
    pz_all = np.full(ctx.nd, np.nan)
    pz_all[keep] = pz
    act = (pz_all >= 5) & ctx.keep
    oth = (pz_all < 5) & ctx.keep
    for nm_, k_ in ctrl_cols:
        V = tf_dd[:, :, k_].astype(float)
        with quiet():
            dwt = np.nanmean(V[:, wt_line], axis=1) - np.nanmean(V[:, ~wt_line], axis=1)
        for lab_, msk in (("p53-activating drug-doses (P53_ACTIVITY z >= 5)", act), ("other drug-doses", oth)):
            v = dwt[msk & np.isfinite(dwt)]
            if len(v) < 3:
                continue
            tt = stats.ttest_1samp(v, 0.0)
            pc_rows.append({"test": f"per-line activity, WT minus altered lines: {lab_}", "tf_activity": nm_,
                            "readout": "ULM slope (mean over drug-doses of the WT - altered mean)", "n": len(v),
                            "estimate": float(v.mean()), "ci_lo": float(v.mean() - 1.96 * v.std(ddof=1) / np.sqrt(len(v))),
                            "ci_hi": float(v.mean() + 1.96 * v.std(ddof=1) / np.sqrt(len(v))), "p": float(tt.pvalue),
                            "n_positive": int((v > 0).sum())})
    PC = pd.DataFrame(pc_rows) if pc_rows else pd.DataFrame(columns=["test", "tf_activity", "readout", "n", "estimate",
                                                                      "p", "note"])
    PC.to_csv(os.path.join(tab, "a3_tp53_positive_control.csv"), index=False, float_format="%.5g")

    # ------------------------------------------------------------------ summary per CollecTRI TF
    A1c = A1[A1["source"] == "CollecTRI_t"]
    summ = pd.DataFrame({"tf": tfs, "n_targets_used": ntar})
    for ver in xvers:
        for var in ("raw", "covariates", "minus_3pc", "minus_10pc"):
            s = A1c[(A1c["trim72_version"] == ver) & (A1c["variant"] == var)].set_index("tf")
            tag = f"dd_{ver}_{var}"
            summ[f"r_{tag}"] = summ["tf"].map(s["r"])
            if var != "raw":
                summ[f"q_{tag}"] = summ["tf"].map(s["q_bh"])
            if ver == "TRIM72" and var in ("covariates", "minus_3pc"):
                summ[f"pct_vs_matched_{tag}"] = summ["tf"].map(s["pct_vs_matched_genes"])
            if ver in ("TRIM72", "TRIM72_rt") and var != "raw":
                summ[f"pct_vs_all_genes_{tag}"] = summ["tf"].map(s["pct_vs_all_genes"])
    for src in ("DoRothEA_t", "TF_mRNA_z", "CollecTRI_lfc_slope"):
        s = A1[(A1["source"] == src) & (A1["trim72_version"] == "TRIM72") & (A1["variant"] == "covariates")]
        s = s.set_index("tf")
        nm = {"DoRothEA_t": "dorothea", "TF_mRNA_z": "tf_mRNA", "CollecTRI_lfc_slope": "lfc_slope"}[src]
        key_ = summ["tf"]
        if src == "DoRothEA_t":                      # AP1 / NFKB: the family member with the largest |r|
            fam = {"AP1": AP1, "NFKB": NFKB}
            best = {f: s.loc[s.index.isin(m_)].reindex(s.loc[s.index.isin(m_), "r"].abs().sort_values().index[-1:])
                    for f, m_ in fam.items() if s.index.isin(m_).any()}
            summ[f"r_{nm}_covariates"] = [best[t_]["r"].iloc[0] if t_ in best else s["r"].get(t_, np.nan)
                                          for t_ in key_]
            summ[f"q_{nm}_covariates"] = [best[t_]["q_bh"].iloc[0] if t_ in best else s["q_bh"].get(t_, np.nan)
                                          for t_ in key_]
        else:
            summ[f"r_{nm}_covariates"] = key_.map(s["r"])
            summ[f"q_{nm}_covariates"] = key_.map(s["q_bh"])
    s = A1c[(A1c["trim72_version"] == "TRIM72") & (A1c["variant"] == "covariates")].set_index("tf")
    summ["ci_lo_dd_TRIM72_covariates"] = summ["tf"].map(s["ci_lo"])
    summ["ci_hi_dd_TRIM72_covariates"] = summ["tf"].map(s["ci_hi"])
    # second activity method (mean signed target z) and the method-robust rank (the worse of the two ranks)
    s = A1[(A1["source"] == "CollecTRI_mean_z") & (A1["trim72_version"] == "TRIM72")
           & (A1["variant"] == "covariates")].set_index("tf")
    summ["r_mean_z_dd_TRIM72_covariates"] = summ["tf"].map(s["r"])
    summ["q_mean_z_dd_TRIM72_covariates"] = summ["tf"].map(s["q_bh"])
    for d_, asc in (("pos", False), ("neg", True)):
        ru = summ["r_dd_TRIM72_covariates"].rank(ascending=asc, method="min")
        rm = summ["r_mean_z_dd_TRIM72_covariates"].rank(ascending=asc, method="min")
        summ[f"rank_{d_}_ulm"], summ[f"rank_{d_}_mean_z"] = ru, rm
        summ[f"rank_{d_}_method_robust"] = np.fmax(ru, rm)
    # regulon-overlap control and plate-batch split (TRIM72, covariates)
    for vname, tag in (("minus_overlap_targets", "minus_overlap"), ("plus_mediators_partialled", "plus_mediators"),
                       ("minus_overlap_targets_plus_mediators", "minus_overlap_plus_mediators")):
        s = OV[OV["variant"] == vname].set_index("tf")
        summ[f"r_dd_TRIM72_{tag}"] = summ["tf"].map(s["r"])
        summ[f"q_dd_TRIM72_{tag}"] = summ["tf"].map(s["q_bh"])
    summ["n_targets_minus_overlap"] = summ["tf"].map(OV[OV["variant"] == "minus_overlap_targets"].set_index("tf")[
        "n_targets_used"])
    for sname in ("high_plates_only", "low_plates_only"):
        s = PB[(PB["source"] == "CollecTRI_t") & (PB["subset"] == sname)].set_index("tf")
        summ[f"r_dd_TRIM72_{sname}"] = summ["tf"].map(s["r"])
        summ[f"q_dd_TRIM72_{sname}"] = summ["tf"].map(s["q_bh"])
    for ver in ys:
        s = A2[(A2["trim72_version"] == ver) & (A2["covset"] == "full")].set_index("tf")
        if ver == "TRIM72":
            summ["within_n_rows"] = summ["tf"].map(s["n_rows"])
            summ["within_n_lines"] = summ["tf"].map(s["n_lines"])
        summ[f"within_{ver}_b_per_sd"] = summ["tf"].map(s["b_per_sd_tf"])
        summ[f"within_{ver}_r"] = summ["tf"].map(s["r_partial_within"])
        summ[f"within_{ver}_p"] = summ["tf"].map(s["p_twoway"])
        summ[f"within_{ver}_q"] = summ["tf"].map(s["q_bh_twoway"])
        if ver == "TRIM72":
            summ["within_diff_WT_minus_alt"] = summ["tf"].map(s["diff_WT_minus_alt"])
            summ["within_diff_p_line"] = summ["tf"].map(s["p_diff_line"])
            summ["within_diff_q"] = summ["tf"].map(s["q_bh_diff_line"])
    cols_q = ["q_dd_TRIM72_covariates", "q_dd_TRIM72_minus_3pc", "q_dd_TRIM72_minus_10pc", "q_dd_TRIM72_rt_covariates",
              "within_TRIM72_q", "within_TRIM72_rt_q"]
    cols_r = ["r_dd_TRIM72_covariates", "r_dd_TRIM72_minus_3pc", "r_dd_TRIM72_minus_10pc", "r_dd_TRIM72_rt_covariates",
              "within_TRIM72_r", "within_TRIM72_rt_r"]
    sig = (summ[cols_q] < 0.1).all(axis=1)
    sgn = np.sign(summ[cols_r]).nunique(axis=1).eq(1)
    summ["tracks_TRIM72_all_tests"] = sig & sgn
    summ["n_tests_q_lt_0.1"] = (summ[cols_q] < 0.1).sum(axis=1)
    summ["lists_TRIM72_as_target"] = summ["tf"].isin(lists_trim72)
    summ["muscle_TF"] = summ["tf"].isin(MUSCLE_TFS)
    summ["tf_gene_in_trim72_locus"] = summ["tf"].isin(locus_syms)       # its own mRNA is readthrough-exposed
    summ["tf_mRNA_median_line_cpm"] = [float(g_at["median_line_cpm"].get(t_, np.nan)) if t_ in ctx.gidx else np.nan
                                       for t_ in summ["tf"]]
    summ = summ.sort_values("r_dd_TRIM72_covariates", ascending=False)
    summ.to_csv(os.path.join(tab, "a1a2_tf_summary.csv"), index=False, float_format="%.4g")

    # ------------------------------------------------------------------ (b) line features
    plates = [str(p) for p in P_["plates"]]
    rel_pl = [i for i, p in enumerate(plates) if p not in fx.unreliable]
    high = [i for i in rel_pl if plates[i] in ("plate1", "plate2", "plate3", "plate14")]
    low = [i for i in rel_pl if i not in high]
    dmc = P_["dm_c"]
    exp_t = ctx.em[:, ctx.j_trim]
    lev = {}
    for nm, c in ((GENE, dmc[:, :, ctx.j_trim]), ("FUS", dmc[:, :, ctx.gidx["FUS"]]),
                  ("PYCARD-AS1", P_["dm_e"][:, :, exs.index("PYCARD-AS1")])):
        expd = ctx.em[:, ctx.gidx[nm]] if nm in ctx.gidx else np.ones(ctx.nl, bool)
        lev[nm] = oe_level(c.astype(float), P_["dm_t"], P_["dm_n"], expd, rel_pl)
    r_hi = oe_level(dmc[:, :, ctx.j_trim].astype(float), P_["dm_t"], P_["dm_n"], exp_t, high)[0]
    r_lo = oe_level(dmc[:, :, ctx.j_trim].astype(float), P_["dm_t"], P_["dm_n"], exp_t, low)[0]
    lines = fx.lines.set_index("cell_line_id")
    out_b = pd.DataFrame({"cell_line": lines["cell_name"].reindex(ctx.lines).to_numpy(),
                          "organ": lines["Organ"].reindex(ctx.lines).to_numpy(), "tp53_group": grp.to_numpy(),
                          "TRIM72_expressed_atlas": exp_t,
                          "TRIM72_untreated_rel": lev[GENE][0], "TRIM72_untreated_rel_plates_1_3_14": r_hi,
                          "TRIM72_untreated_rel_plates_4_12": r_lo, "TRIM72_dmso_counts": lev[GENE][1],
                          "TRIM72_dmso_expected": lev[GENE][2]}, index=pd.Index(ctx.lines, name="cell_line_id"))
    for nm, (d_name, conc) in RAISERS.items():
        r_ = ctx.dd_row(d_name, conc)
        out_b[f"TRIM72_r2_{nm}"] = trim_dd[r_]
        for k, wi_ in enumerate(fx.wells_of_dd[r_]):
            out_b[f"TRIM72_r2_{nm}_well_{ctx.w['plate'].iloc[wi_]}"] = trim_w[wi_]
    with quiet():
        out_b["TRIM72_induction_mean"] = out_b[[f"TRIM72_r2_{k}" for k in RAISERS]].mean(axis=1, skipna=False)
    for oc in [f"TRIM72_r2_{k}" for k in RAISERS] + ["TRIM72_induction_mean"]:
        mfit = out_b[[oc, "TRIM72_untreated_rel"]].dropna()           # low-baseline lines get larger folds
        sl = np.polyfit(mfit["TRIM72_untreated_rel"], mfit[oc], 1)
        out_b[f"{oc}_adj_untreated"] = out_b[oc] - np.polyval(sl, out_b["TRIM72_untreated_rel"])
    out_b["FUS_untreated_rel"] = lev["FUS"][0]
    out_b["PYCARD-AS1_untreated_rel"] = lev["PYCARD-AS1"][0]
    md = pd.read_parquet(os.path.join(a.data, "metadata", "cell_line_metadata.parquet"))
    md = md[md["Cell_ID_Cellosaur"].isin(ctx.lines)]
    drv = md.groupby("Cell_ID_Cellosaur")["Driver_Gene_Symbol"].apply(lambda s: sorted(set(s.dropna().astype(str))))
    out_b["drivers_cell_line_metadata"] = [";".join(drv.get(l_, [])) for l_ in ctx.lines]
    out_b.to_csv(os.path.join(tab, "b1_line_outcomes.csv"), float_format="%.5g")
    # features
    Dg = pd.DataFrame(0.0, index=ctx.lines, columns=sorted(set(md["Driver_Gene_Symbol"].dropna().astype(str))))
    for l_, gs in drv.items():
        Dg.loc[l_, gs] = 1.0
    cnt = Dg.sum(axis=0)
    n_drv = Dg.sum(axis=1)
    Dg = Dg.loc[:, (cnt >= 4) & (cnt <= len(ctx.lines) - 4) & (Dg.columns != "TP53")]
    Dg["n driver genes altered"] = n_drv
    organ = out_b["organ"].fillna("other")
    vc = organ.value_counts()
    lin = pd.DataFrame({f"organ: {o}": (organ == o).astype(float) for o in vc.index[vc >= 3]})
    rel = baseline_relative(ctx, P_, rel_pl)
    Rb = np.where(excl[None, :], np.nan, rel)
    _b, tb, _n = ULM(W)(Rb)
    btf = pd.DataFrame(tb, index=ctx.lines, columns=tfs)
    btf.index.name = "cell_line_id"
    btf.to_csv(os.path.join(tab, "b3_baseline_tf_activity_per_line.csv"), float_format="%.4g")
    fams = {"tp53": pd.DataFrame({"TP53 WT (vs altered)": wt_line.astype(float)}, index=ctx.lines),
            "lineage": lin.set_axis(ctx.lines), "drivers": Dg,
            "baseline_tf": btf,
            "locus": out_b[["FUS_untreated_rel", "PYCARD-AS1_untreated_rel"]]}
    outc = out_b[["TRIM72_untreated_rel", "TRIM72_r2_idarubicin_5", "TRIM72_r2_homoharringtonine_5",
                  "TRIM72_induction_mean", "TRIM72_r2_idarubicin_5_adj_untreated",
                  "TRIM72_r2_homoharringtonine_5_adj_untreated", "TRIM72_induction_mean_adj_untreated"]]
    log(f"(b) line features: {len(Dg.columns)} driver genes, {lin.shape[1]} organs, {btf.shape[1]} baseline TFs")
    B2 = line_tests(outc, fams, organ, rng, a.line_perm)
    # inducibility vs the untreated level, per raiser (how much of a line's fold is set by its low baseline)
    ind_rows = []
    for oc in [f"TRIM72_r2_{k}" for k in RAISERS] + ["TRIM72_induction_mean"]:
        m_ = out_b[[oc, "TRIM72_untreated_rel"]].dropna()
        sp = stats.spearmanr(m_[oc], m_["TRIM72_untreated_rel"])
        ind_rows.append({"outcome": oc, "n_lines": len(m_), "rho": float(sp.correlation), "p": float(sp.pvalue),
                         "R2_linear": float(np.corrcoef(m_[oc], m_["TRIM72_untreated_rel"])[0, 1] ** 2)})
        add(f"{oc} vs TRIM72 untreated level across lines, Spearman rho (the *_adj_untreated outcomes remove the "
            "linear part)", ind_rows[-1]["rho"], len(m_), f"p {sp.pvalue:.2g}; linear R2 {ind_rows[-1]['R2_linear']:.2f}")
        wells_ = [c for c in out_b.columns if c.startswith(f"{oc}_well_")] if oc != "TRIM72_induction_mean" else []
        if len(wells_) == 2:
            m2 = out_b[wells_ + ["TRIM72_untreated_rel"]].dropna()
            u_ = m2["TRIM72_untreated_rel"]
            res_ = [m2[c] - np.polyval(np.polyfit(u_, m2[c], 1), u_) for c in wells_]
            add(f"{oc}: well-to-well Spearman rho after removing the untreated level from each well "
                f"({wells_[0].split('_well_')[1]} vs {wells_[1].split('_well_')[1]})", float(stats.spearmanr(res_[0], res_[1]).correlation), len(m2),
                f"raw well-to-well rho {stats.spearmanr(m2[wells_[0]], m2[wells_[1]]).correlation:.2f}")
    # KMT2D and the untreated level: is it a driver-count (mutation-burden) effect? Partial on the number of driver
    # genes, and a null of pseudo-driver line sets of the same size drawn with probability ~ n driver genes
    kmt = {}
    if "KMT2D" in Dg.columns:
        yv = out_b["TRIM72_untreated_rel"].to_numpy(float)
        m_ = np.isfinite(yv)
        kv, nd_, yv = Dg["KMT2D"].to_numpy(float)[m_], n_drv.to_numpy(float)[m_], yv[m_]
        ry = stats.rankdata(yv)
        Xd = np.column_stack([np.ones(len(yv)), stats.rankdata(nd_)])

        def _res(v):
            return v - Xd @ np.linalg.lstsq(Xd, v, rcond=None)[0]
        rho_k = float(np.corrcoef(ry, kv)[0, 1])
        rho_part = float(np.corrcoef(_res(ry), _res(kv))[0, 1])
        rng_k = np.random.default_rng([SEED, 3])
        nul = np.empty(5000)
        for b_ in range(len(nul)):
            v_ = np.zeros(len(yv))
            v_[rng_k.choice(len(yv), int(kv.sum()), replace=False, p=nd_ / nd_.sum())] = 1.0
            nul[b_] = np.corrcoef(ry, v_)[0, 1]
        kmt = {"rho": rho_k, "rho_partial_n_drivers": rho_part, "p_pseudo_driver_null": float(np.mean(nul >= rho_k)),
               "null_mean": float(nul.mean()), "n_mut": int(kv.sum()), "n_lines": len(yv),
               "n_drivers_median_mut": float(np.median(nd_[kv == 1])), "n_drivers_median_wt": float(np.median(nd_[kv == 0]))}
        add("KMT2D-altered lines vs TRIM72 untreated level: rho; partial on n driver genes; pseudo-driver null",
            rho_k, len(yv), f"{kmt['n_mut']} KMT2D lines; rho partial on n drivers {rho_part:.2f}; 5,000 random sets of "
            f"{kmt['n_mut']} lines drawn with probability ~ n driver genes: mean rho {kmt['null_mean']:.2f}, "
            f"P(rho >= observed) {kmt['p_pseudo_driver_null']:.4f}; median n drivers {kmt['n_drivers_median_mut']:.0f} "
            f"(KMT2D) vs {kmt['n_drivers_median_wt']:.0f}")
    B2.to_csv(os.path.join(tab, "b2_line_feature_tests.csv"), index=False, float_format="%.5g")

    # ------------------------------------------------------------------ A4 muscle / promoter TFs
    mrows = []
    dmcpm = {}
    for nm in MUSCLE_TFS:
        if nm in ctx.gidx:
            c = dmc[rel_pl][:, :, ctx.gidx[nm]].astype(float).sum(axis=0)
        elif nm in exs:
            c = P_["dm_e"][rel_pl][:, :, exs.index(nm)].astype(float).sum(axis=0)
        else:
            c = None
        t_ = P_["dm_t"][rel_pl].sum(axis=0)
        dmcpm[nm] = np.median(1e6 * c / t_) if c is not None else np.nan
    for nm in MUSCLE_TFS:
        o = {"tf": nm, "in_atlas_gene_list": nm in ctx.gidx,
             "atlas_median_line_cpm": float(g_at["median_line_cpm"].get(nm, np.nan)) if nm in ctx.gidx else np.nan,
             "atlas_n_lines_expressing": float(g_at["n_lines_expressing"].get(nm, np.nan)) if nm in ctx.gidx else
             np.nan, "dmso_median_line_cpm_pseudobulk": dmcpm[nm],
             "CollecTRI_lists_TRIM72": bool(((edges["source"] == "CollecTRI") & (edges["tf"] == nm)
                                             & edges["target_is_TRIM72"]).any()),
             "DoRothEA_lists_TRIM72": bool(((edges["source"] == "DoRothEA_ABC") & (edges["tf"] == nm)
                                            & edges["target_is_TRIM72"]).any()),
             "CollecTRI_targets_used": int(ntar[tfs.index(nm)]) if nm in tfs else 0,
             "DoRothEA_targets_used": int(ntar_d[tfs_d.index(nm)]) if nm in tfs_d else 0}
        if nm in tfs:
            r = summ.set_index("tf").loc[nm]
            for c_ in ("r_dd_TRIM72_covariates", "q_dd_TRIM72_covariates", "r_dd_TRIM72_minus_3pc",
                       "q_dd_TRIM72_minus_3pc", "r_dd_TRIM72_rt_covariates", "q_dd_TRIM72_rt_covariates",
                       "within_TRIM72_r", "within_TRIM72_q", "within_TRIM72_rt_r", "within_TRIM72_rt_q",
                       "pct_vs_matched_dd_TRIM72_covariates"):
                o[c_] = r[c_]
            bt = B2[(B2["family"] == "baseline_tf") & (B2["feature"] == nm)].set_index("outcome")
            for oc in ("TRIM72_untreated_rel", "TRIM72_induction_mean"):
                o[f"baseline_activity_vs_{oc}_rho"] = bt["rho"].get(oc, np.nan)
                o[f"baseline_activity_vs_{oc}_q"] = bt["q_bh"].get(oc, np.nan)
        if nm in tfs_d:
            s = A1[(A1["source"] == "DoRothEA_t") & (A1["tf"] == nm) & (A1["trim72_version"] == "TRIM72")
                   & (A1["variant"] == "covariates")]
            o["dorothea_r_dd_TRIM72_covariates"] = float(s["r"].iloc[0]) if len(s) else np.nan
            o["dorothea_q_dd_TRIM72_covariates"] = float(s["q_bh"].iloc[0]) if len(s) else np.nan
        mrows.append(o)
    pd.DataFrame(mrows).to_csv(os.path.join(tab, "a4_muscle_promoter_tfs.csv"), index=False, float_format="%.4g")

    # ------------------------------------------------------------------ checks
    wl = pd.read_parquet(os.path.join(a.data, "gene_panel", "well_line.parquet"),
                         columns=["sample", "cell_line_id", "n_cells", "total_counts", GENE])
    wl = wl[wl["sample"].astype(str).isin(ctx.w["sample"]) & wl["cell_line_id"].astype(str).isin(ctx.lines)]
    wl["plate"] = wl["sample"].astype(str).map(dict(zip(ctx.w["sample"].astype(str), ctx.w["plate"].astype(str))))
    isd = dict(zip(ctx.w["sample"].astype(str), ~fx.drug_w))
    wl = wl[wl["sample"].astype(str).map(isd)]
    agg = wl.groupby(["plate", "cell_line_id"])[GENE].sum()
    mine = pd.Series(dmc[:, :, ctx.j_trim].ravel().astype(float),
                     index=pd.MultiIndex.from_product([plates, ctx.lines]))
    add("DMSO TRIM72 counts per plate x line: pass vs gene_panel well_line, max |diff|",
        float((agg - mine.reindex(agg.index)).abs().max()), len(agg))
    ref = os.path.join(REPO, "trim72_idarubicin", "corrected", "TRIM72_idarubicin_5uM_per_line_corrected.csv")
    if os.path.exists(ref):
        t_ = pd.read_csv(ref, dtype={"cell_line_id": str}).set_index("cell_line_id")["log2FC_corrected"]
        v = out_b["TRIM72_r2_idarubicin_5"]
        m = t_.reindex(ctx.lines).notna().to_numpy() & v.notna().to_numpy()
        add("idarubicin 5 uM per-line TRIM72 r2 (mean of 2 wells) vs trim72_idarubicin/corrected, max |diff|",
            float(np.max(np.abs(t_.reindex(ctx.lines).to_numpy()[m] - v.to_numpy()[m]))), int(m.sum()))
    rr = stats.spearmanr(r_hi, r_lo, nan_policy="omit")
    add("TRIM72 untreated line ranking: plates 1-3,14 vs plates 4-12, Spearman rho", float(rr.correlation),
        int((np.isfinite(r_hi) & np.isfinite(r_lo)).sum()), f"p {rr.pvalue:.2g}")
    rr = stats.spearmanr(out_b["TRIM72_r2_idarubicin_5_well_plate6"], out_b["TRIM72_r2_idarubicin_5_well_plate14"],
                         nan_policy="omit") if "TRIM72_r2_idarubicin_5_well_plate6" in out_b else None
    if rr is not None:
        add("idarubicin 5 uM per-line TRIM72 r2: plate-6 well vs plate-14 well, Spearman rho", float(rr.correlation),
            int(out_b[["TRIM72_r2_idarubicin_5_well_plate6", "TRIM72_r2_idarubicin_5_well_plate14"]].dropna().shape[0]),
            f"p {rr.pvalue:.2g}")
    hh = [c for c in out_b.columns if c.startswith("TRIM72_r2_homoharringtonine_5_well_")]
    if len(hh) == 2:
        rr = stats.spearmanr(out_b[hh[0]], out_b[hh[1]], nan_policy="omit")
        add(f"homoharringtonine 5 uM per-line TRIM72 r2: {hh[0].split('_well_')[1]} vs {hh[1].split('_well_')[1]} "
            "well, Spearman rho",
            float(rr.correlation), int(out_b[hh].dropna().shape[0]), f"p {rr.pvalue:.2g}")
    kk = ctx.keep
    mm = np.isfinite(pz_all) & kk
    if kt is not None:
        add("TP53 CollecTRI ULM t vs panel P53_ACTIVITY z across drug-doses, Pearson r (raw)",
            float(np.corrcoef(t_col[:, kt][np.isfinite(pz)], pz[np.isfinite(pz)])[0, 1]), int(mm.sum()))
    CK = pd.concat([pd.DataFrame(checks), val.assign(check="pass validation per plate").rename(
        columns={"W1_max_abs_diff_vs_atlas": "value", "W1_cells_both_finite": "n"})[["check", "plate", "value", "n",
                                                                                     "W1_finite_here_not_atlas",
                                                                                     "W1_finite_atlas_not_here"]]],
                   ignore_index=True)
    CK.to_csv(os.path.join(tab, "checks.csv"), index=False)

    # ------------------------------------------------------------------ key results
    kr = []

    def _nl(r_):                    # within-line rows and lines of one TF (they differ by the TF's missing pattern)
        return f"n {int(r_.n_rows)} rows / {int(r_.n_lines)} lines"
    for ver in xvers:
        for var in ("covariates", "minus_3pc", "minus_10pc"):
            s = A1c[(A1c["trim72_version"] == ver) & (A1c["variant"] == var)]
            top = s.sort_values("r", ascending=False).head(5)
            bot = s.sort_values("r").head(3)
            kr.append({"section": "A1 across drug-doses (CollecTRI ULM t)", "what": f"{ver} [{var}]: TFs with q < 0.1 "
                       "(positive / negative)", "n": int(s["n_drugdoses"].iloc[0]),
                       "estimate": int(((s["q_bh"] < 0.1) & (s["r"] > 0)).sum()),
                       "detail": f"negative {int(((s['q_bh'] < 0.1) & (s['r'] < 0)).sum())} of {len(s)} TFs; top: " +
                                 "; ".join(f"{r_.tf} r {r_.r:.2f} (drug CI {r_.ci_lo:.2f} to {r_.ci_hi:.2f}) q "
                                           f"{r_.q_bh:.2g} pct matched {r_.pct_vs_matched_genes:.0f} pct all genes "
                                           f"{r_.pct_vs_all_genes:.1f}" for r_ in top.itertuples()) + "; bottom: " +
                                 "; ".join(f"{r_.tf} r {r_.r:.2f} q {r_.q_bh:.2g}" for r_ in bot.itertuples())})
    s = A1c[(A1c["trim72_version"] == "TRIM72") & (A1c["variant"] == "covariates")]
    kr.append({"section": "A1 across drug-doses (CollecTRI ULM t)",
               "what": "TRIM72 [covariates]: SE used for the CI (larger of drug-block null SD and drug jackknife SE), "
                       "median over TFs", "n": len(s), "estimate": float(np.fmax(s["null_sd_drug_block"],
                                                                                 s["se_jackknife_drug"]).median()),
               "detail": f"null SD median {s['null_sd_drug_block'].median():.3f}; jackknife SE median "
                         f"{s['se_jackknife_drug'].median():.3f} (larger for {int((s['se_jackknife_drug'] > s['null_sd_drug_block']).sum())} "
                         f"of {len(s)} TFs); iid Fisher SE would be {1 / np.sqrt(n_k - 3 - (s['n_partialled'].iloc[0] - 1)):.3f}"})
    # method robustness
    sm = summ.dropna(subset=["r_dd_TRIM72_covariates", "r_mean_z_dd_TRIM72_covariates"])
    for d_ in ("pos", "neg"):
        tt = sm.sort_values([f"rank_{d_}_method_robust", f"rank_{d_}_ulm"]).head(10)
        kr.append({"section": "A1 method robustness (ULM t vs mean signed target z; TRIM72, covariates)",
                   "what": f"top 10 {'positive' if d_ == 'pos' else 'negative'} TFs by method-robust rank (the worse "
                           "of the two ranks); estimate = Pearson r across TFs of the two methods' r",
                   "n": len(sm), "estimate": float(np.corrcoef(sm["r_dd_TRIM72_covariates"],
                                                               sm["r_mean_z_dd_TRIM72_covariates"])[0, 1]),
                   "detail": "; ".join(f"{r_.tf} robust rank {int(getattr(r_, f'rank_{d_}_method_robust'))} (ULM r "
                                       f"{r_.r_dd_TRIM72_covariates:.2f} rank {int(getattr(r_, f'rank_{d_}_ulm'))}; mean z r "
                                       f"{r_.r_mean_z_dd_TRIM72_covariates:.2f} rank {int(getattr(r_, f'rank_{d_}_mean_z'))})"
                                       for r_ in tt.itertuples())})
    # regulon-overlap control
    top_u = summ.sort_values("r_dd_TRIM72_covariates", ascending=False)["tf"].head(10).tolist()
    top_r = summ.sort_values(["rank_pos_method_robust", "rank_pos_ulm"])["tf"].head(10).tolist()
    top_ov = list(dict.fromkeys(top_u + top_r + [t_ for t_ in ("AP1", "NFKB", "HSF1", "CREB1", "SRF", "ELK4", "XBP1",
                                                               "ATF4", "TP53") if t_ in tfs]))
    so = summ.set_index("tf").loc[top_ov]
    for vname, tag in (("minus_overlap_targets", "minus_overlap"), ("plus_mediators_partialled", "plus_mediators"),
                       ("minus_overlap_targets_plus_mediators", "minus_overlap_plus_mediators")):
        v_ = OV[OV["variant"] == vname]
        kr.append({"section": "A1 regulon-overlap control (TRIM72, covariates, ULM t)",
                   "what": f"{vname}: TFs with q < 0.1 (positive); detail = top TFs' r: reference -> this variant",
                   "n": int(v_["r"].notna().sum()), "estimate": int(((v_["q_bh"] < 0.1) & (v_["r"] > 0)).sum()),
                   "detail": f"median change in r over these {len(so)} TFs {np.nanmedian(so[f'r_dd_TRIM72_{tag}'] - so['r_dd_TRIM72_covariates']):+.3f}; " +
                             "; ".join(f"{t_} {r_['r_dd_TRIM72_covariates']:.2f} -> {r_[f'r_dd_TRIM72_{tag}']:.2f}"
                                       + (f" (q {r_[f'q_dd_TRIM72_{tag}']:.2g})" if pd.notna(r_[f'q_dd_TRIM72_{tag}']) else "")
                                       + (f" [{int(r_['n_targets_minus_overlap'])} of {int(r_['n_targets_used'])} targets left]"
                                          if "overlap" in tag else "")
                                       for t_, r_ in so.iterrows())})
    # plate-batch split
    pv = PB[PB["source"] == "CollecTRI_t"].pivot_table(index="tf", columns="subset", values="r")
    hl = pv[["high_plates_only", "low_plates_only"]].dropna()
    nsub = PB[PB["source"] == "CollecTRI_t"].groupby("subset")["n_drugdoses"].first()
    qsub = PB[PB["source"] == "CollecTRI_t"].groupby("subset").apply(
        lambda g: int(((g["q_bh"] < 0.1) & (g["r"] > 0)).sum()), include_groups=False)
    kr.append({"section": "A1 plate-batch split (TRIM72, covariates, ULM t)",
               "what": "r in drug-doses on the high-TRIM72 plates (1-3) only vs the low-TRIM72 plates (4-12) only; "
                       "estimate = Pearson r across TFs", "n": len(hl),
               "estimate": float(np.corrcoef(hl["high_plates_only"], hl["low_plates_only"])[0, 1]),
               "detail": "drug-doses: " + ", ".join(f"{k_} {int(v_)}" for k_, v_ in nsub.items()) +
                         "; positive TFs with q < 0.1: " + ", ".join(f"{k_} {int(v_)}" for k_, v_ in qsub.items()) +
                         "; top TFs r all / high / low: " + "; ".join(
                             f"{t_} {pv.loc[t_, 'all']:.2f} / {pv.loc[t_, 'high_plates_only']:.2f} / "
                             f"{pv.loc[t_, 'low_plates_only']:.2f}" for t_ in top_ov if t_ in pv.index)})
    for ver in ys:
        s = A2[(A2["trim72_version"] == ver) & (A2["covset"] == "full") & ~A2["tf"].isin(CTRL_TFS)]
        top = s.sort_values("r_partial_within", ascending=False).head(5)
        bot = s.sort_values("r_partial_within").head(3)
        kr.append({"section": "A2 within lines (two-way FE, full covariates)", "what": f"{ver}: TFs with q < 0.1",
                   "n": int(s["n_rows"].max()), "estimate": int((s["q_bh_twoway"] < 0.1).sum()),
                   "detail": f"rows per TF {int(s['n_rows'].min())}-{int(s['n_rows'].max())}, lines "
                             f"{int(s['n_lines'].min())}-{int(s['n_lines'].max())}; top: " +
                             "; ".join(f"{r_.tf} r {r_.r_partial_within:.3f} b/SD {r_.b_per_sd_tf:.3f} q "
                                       f"{r_.q_bh_twoway:.2g} ({_nl(r_)})" for r_ in top.itertuples()) +
                             "; bottom: " + "; ".join(f"{r_.tf} r {r_.r_partial_within:.3f} q {r_.q_bh_twoway:.2g} "
                                                      f"({_nl(r_)})" for r_ in bot.itertuples()) +
                             f"; WT-altered slope differences with q < 0.1: {int((s['q_bh_diff_line'] < 0.1).sum())}"})
    for ver in ys:
        s = NC[(NC["trim72_version"] == ver) & (NC["covset"] == "full")]
        a2v = A2[(A2["trim72_version"] == ver) & (A2["covset"] == "full") & ~A2["tf"].isin(CTRL_TFS)]
        kr.append({"section": "A2 within-line noise ceiling (two-way FE, full covariates)",
                   "what": f"{ver} r2 vs single co-responding genes' r2: within-line r (estimate = the largest |r|)",
                   "n": int(s["n_rows"].max()), "estimate": float(s["r_partial_within"].abs().max()),
                   "detail": "; ".join(f"{r_.gene} r {r_.r_partial_within:.3f} ({_nl(r_)})" for r_ in s.itertuples()) +
                             f"; for comparison the largest |r| of a TF activity: "
                             f"{a2v['r_partial_within'].abs().max():.3f}" +
                             ("; FUS is regressed out of TRIM72_rt by construction" if ver == "TRIM72_rt" else "")})
    named = ["AP1", "NFKB", "JUN", "FOS", "RELA", "ATF3", "ATF4", "XBP1", "DDIT3", "HSF1", "NFE2L2", "SRF", "ELK1",
             "ELK4", "CREB1", "EGR1", "TP53", "MYC", "E2F1", "E2F4", "FOXO1", "FOXO3", "MEF2A", "MEF2C", "MYOD1", "MYOG"]
    sn = summ.set_index("tf").reindex([t_ for t_ in named if t_ in tfs])
    kr.append({"section": "A1+A2 named TFs", "what": "drug-dose r (covariates; minus 10 PCs; mean target z) | within-line "
               "r (q; rows / lines)", "n": len(sn), "detail": "; ".join(
                   f"{t_} {r_['r_dd_TRIM72_covariates']:.2f}/{r_['r_dd_TRIM72_minus_10pc']:.2f}/"
                   f"{r_['r_mean_z_dd_TRIM72_covariates']:.2f} | {r_['within_TRIM72_r']:.3f} (q "
                   f"{r_['within_TRIM72_q']:.2g}; {r_['within_n_rows']:.0f} / {r_['within_n_lines']:.0f})"
                   for t_, r_ in sn.iterrows())})
    rob = summ[summ["tracks_TRIM72_all_tests"]]
    kr.append({"section": "A1+A2", "what": "CollecTRI TFs tracking TRIM72 in all six tests (q < 0.1, same sign)",
               "n": len(summ), "estimate": len(rob),
               "detail": "; ".join(f"{r_.tf} (dd r {r_.r_dd_TRIM72_covariates:.2f}, within r {r_.within_TRIM72_r:.3f}"
                                   f" n {r_.within_n_rows:.0f} rows / {r_.within_n_lines:.0f} lines, pct vs matched "
                                   f"{r_.pct_vs_matched_dd_TRIM72_covariates:.0f}, method-robust rank "
                                   f"{min(r_.rank_pos_method_robust, r_.rank_neg_method_robust):.0f})"
                                   for r_ in rob.itertuples())})
    for r_ in PC.itertuples():
        kr.append({"section": "A3 TP53 positive control", "what": f"{r_.test}: {r_.tf_activity} vs {r_.readout}",
                   "n": r_.n, "estimate": r_.estimate, "p": r_.p,
                   "detail": (f"b_WT {r_.b_WT:.3g}, b_alt {r_.b_alt:.3g}, diff p {r_.p_diff_line:.2g}; "
                              f"{int(r_.n_lines)} lines" if pd.notna(getattr(r_, "b_WT", np.nan)) else "")})
    for o in mrows:
        kr.append({"section": "A4 muscle / promoter TFs", "what": o["tf"], "estimate": o.get("r_dd_TRIM72_covariates"),
                   "q": o.get("q_dd_TRIM72_covariates"),
                   "detail": f"atlas median CPM {o['atlas_median_line_cpm']}, DMSO CPM {o['dmso_median_line_cpm_pseudobulk']:.3g}; "
                             f"CollecTRI lists TRIM72 {o['CollecTRI_lists_TRIM72']}; targets {o['CollecTRI_targets_used']}; "
                             f"within r {o.get('within_TRIM72_r', np.nan):.3g} q {o.get('within_TRIM72_q', np.nan):.2g}"})
    for (oc, fam), g in B2.groupby(["outcome", "family"]):
        g2 = g.sort_values("p").head(3)
        kr.append({"section": "(b) line features", "what": f"{oc} ~ {fam}: features with q < 0.1 (BH over all "
                   f"{len(B2)} line tests)", "n": int(g["n_lines"].max()), "estimate": int((g["q_bh"] < 0.1).sum()),
                   "detail": f"{len(g)} tests; q < 0.1 with BH within the outcome {int((g['q_bh_outcome'] < 0.1).sum())}, "
                             f"within outcome x family {int((g['q_bh_family'] < 0.1).sum())}; smallest p: " +
                             "; ".join(f"{r_.feature} rho {r_.rho:.2f} p {r_.p:.2g} q {r_.q_bh:.2g} (outcome "
                                       f"{r_.q_bh_outcome:.2g}, family {r_.q_bh_family:.2g})"
                                       for r_ in g2.itertuples())})
    for o in ind_rows:              # F7, per raiser: how much of a line's induction is set by its untreated level
        kr.append({"section": "(b) inducibility vs untreated level (per raiser)",
                   "what": f"{o['outcome']} vs TRIM72_untreated_rel across lines (Spearman)", "n": o["n_lines"],
                   "estimate": o["rho"], "p": o["p"],
                   "detail": f"linear R2 {o['R2_linear']:.2f}: " + (
                       "strongly tied (low-baseline lines get larger folds)" if abs(o["rho"]) >= 0.5 else
                       "only weakly tied") + "; the *_adj_untreated outcome removes the linear part"})
    kb = B2[(B2["feature"] == "KMT2D") & (B2["outcome"] == "TRIM72_untreated_rel")]
    if len(kb) and kmt:
        k_ = kb.iloc[0]
        kr.append({"section": "(b) line features", "what": "KMT2D-altered lines vs TRIM72 untreated level",
                   "n": int(k_["n_lines"]), "estimate": float(k_["rho"]), "p": float(k_["p"]), "q": float(k_["q_bh"]),
                   "detail": f"q {k_['q_bh_outcome']:.2g} within the untreated outcome (all "
                             f"{int((B2['outcome'] == 'TRIM72_untreated_rel').sum())} tests), {k_['q_bh']:.2g} over all "
                             f"{len(B2)} line tests (the headline q; {k_['q_bh_family']:.2g} within the "
                             f"{int(((B2['outcome'] == 'TRIM72_untreated_rel') & (B2['family'] == 'drivers')).sum())} "
                             f"driver tests); {kmt['n_mut']} KMT2D lines; rho partial on the number of driver genes "
                             f"{kmt['rho_partial_n_drivers']:.2f}; pseudo-driver sets drawn ~ n drivers reach rho >= "
                             f"observed with P {kmt['p_pseudo_driver_null']:.4f}: " +
                             ("not explained by the number of altered drivers (no support for a mutation-burden / "
                              "hypermutation reading); unexplained" if kmt["p_pseudo_driver_null"] < 0.05 else
                              "compatible with a driver-count (mutation-burden) effect")})
    lb = B2[(B2["family"] == "locus") & (B2["outcome"] == "TRIM72_untreated_rel")]
    kr.append({"section": "(b) line features", "what": "TRIM72 untreated level vs its locus neighbours' untreated level",
               "n": int(lb["n_lines"].max()) if len(lb) else 0,
               "detail": "; ".join(f"{r_.feature} rho {r_.rho:.2f} p {r_.p:.2g}" for r_ in lb.itertuples()) +
                         ": readthrough from FUS fits, but a line's 16p11.2 copy number (more copies -> all genes of "
                         "the region higher) would give the same link; Tahoe has no copy-number data to separate them"})
    pd.DataFrame(kr).to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.4g")
    reg_out.to_csv(os.path.join(tab, "a0_regulons_used.csv.gz"), index=False)
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    md5 = {}
    for fn in ("collectri.tsv", "dorothea_ABC.tsv"):
        if os.path.exists(os.path.join(ext, fn)):
            with open(os.path.join(ext, fn), "rb") as fh:
                md5[fn] = hashlib.md5(fh.read()).hexdigest()
    pk = peak_gb()
    info = {"downloads": status, "download_date_utc": time.strftime("%Y-%m-%d", time.gmtime(
        os.path.getmtime(os.path.join(ext, "collectri.tsv")))) if os.path.exists(os.path.join(ext, "collectri.tsv"))
        else None, "regulon_md5": md5, "locus_source": locus_src, "n_tfs_collectri": len(tfs),
        "n_tfs_dorothea": len(tfs_d), "n_drugdoses": int(n_k), "perm": a.perm, "line_perm": a.line_perm,
        "pass_seconds_incl_setup": round(t_pass, 1), "pass_from_cache": bool(P_.get("_from_cache", False)),
        "wall_seconds": round(time.time() - t_start, 1), "peak_rss_gb": round(pk, 2) if np.isfinite(pk) else None,
        "peak_rss_source": _MEM_PEAK["how"], "python": sys.version.split()[0], "platform": sys.platform}
    with open(os.path.join(tab, "run_info.json"), "w", encoding="utf-8") as fh:
        json.dump(info, fh, indent=1)
    print(CK.head(len(checks)).to_string(index=False))
    log(f"tables written to {tab}; peak RSS {peak_gb():.2f} GB; wall {time.time() - t_start:.0f} s")


if __name__ == "__main__":
    main()
