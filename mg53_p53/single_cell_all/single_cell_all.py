#!/usr/bin/env python3
"""single_cell_all (D1b at full scale): within every (well, cell line) of Tahoe-100M, do cells with detected TRIM72 (MG53)
mRNA carry more or less p53-target mRNA than cells without, and is that difference larger in TP53 wild-type lines?

Tahoe has no MG53 perturbation and measures mRNA only, so every number here is an ASSOCIATION between TRIM72 mRNA and
p53-target mRNA in single cells (p53 activity is read from its targets' mRNA; p53 protein is never measured). The TP53
genotype is the control: an MG53 -> p53 effect can only act where p53 works, so the primary estimand is the TRIM72
log rate ratio in TP53-WT lines MINUS that in TP53-altered lines; what is equal in both groups does not go through p53.

Design (all from Tahoe's own data, no new experiments)
 1. Stream gene_panel/cells/*.parquet file by file (95.6M cells; only the needed columns). Keep the (well, line) groups
    with >= --min-cells cells and >= --min-det TRIM72-detected (>= 1 UMI) and undetected cells, in lines that express
    TRIM72 (atlas expr_mask; NCI-H661 is out). Optional uniform subsample to --max-cells-per-group cells per group
    (Bernoulli, seeded per file; uniform so that the placebo-predictor fits stay valid). A plate is fitted as soon as
    all of its cells have been read (counts from gene_panel/well_line.parquet), so at most ~2 plates are in memory.
 2. Per group, quasi-Poisson log-linear model (IRLS; dispersion = Pearson chi2/df, floored at 1), as in
    downstream_p53.py (d): counts ~ detected + log(total UMI) + log S-phase fraction + log G2M fraction, offset
    log(total UMI). Predictor 'TRIM72 detected' with every outcome: the 21-gene P53_ACTIVITY score (members summed),
    the 5 primary p53 targets summed (MDM2, CDKN1A, FDXR, ZMAT3, DDB2), each of them, TP53, every other P53_ACTIVITY
    member, the screen modules of mg53_p53/gene_modules.csv that the per-cell panel holds (NF-kB:
    NFKBIA/TNFAIP3/CXCL8 and the panel's 8-gene NF-kB set; ferroptosis: SLC7A11/GPX4/CHAC1; apoptosis:
    BAX/BBC3/PMAIP1; stress: ATF3, PMAIP1, DDIT3) and every non-p53 panel gene (PLACEBO OUTCOMES).
    PLACEBO PREDICTORS: 'gene X detected' for every non-p53-linked, non-screen panel gene whose detection rate in the
    fitted groups is within 1/--placebo-range x to --placebo-range x of TRIM72's, same model, outcomes = the p53 and
    screen read-outs. Their estimates are the null distribution for TRIM72's.
    AMBIENT NEGATIVE CONTROLS: 'CDKN2A detected' in CDKN2A-deleted lines and 'MTAP detected' in MTAP-null lines
    (gene panel p53_functional_status.csv flags, kept only where the line's reads of the gene are at the ambient
    level of its wells): every such read is soup, so these predictors show what pure ambient capture does.
    CAP-0 SAMPLE: a random --cap0-frac of the groups that the cap could leave with < --min-det TRIM72-detected cells
    are also fitted with ALL their cells, so the groups the cap drops can be put back (sensitivity).
 3. Two-stage random effects (DerSimonian-Laird): per (line, well class) over its wells, then per TP53 group over lines
    (the 17 WT lines repeat in every well, so lines, not wells, are the units). Stage-2 inference uses Hartung-Knapp
    SEs (t on lines - 1 df; variance factor floored at 1, so never narrower than DL); the DL normal SE is kept as a
    secondary column. WT minus altered: difference of the two line-level means (HK SE, Welch-Satterthwaite df) and a
    TP53-label permutation over lines (--perm); a within-well paired version (WT groups minus altered groups of the
    same well, then over wells) as a check. Well classes: DMSO; drug-doses that raise TRIM72 (gene panel call 'up');
    drug-doses that activate p53 (P53_ACTIVITY z >= 3 and FDR < 0.10, not raisers); all other drugs; all wells.
    Alternative grouping: TP53 FUNCTIONAL status (gene panel call responsive vs unresponsive) and the continuous p53
    responsiveness (random-effects meta-regression over lines), each against the placebo predictors.
 4. What the test can exclude per doubling of a cell's TRIM72: the negative-binomial overdispersion of TRIM72 counts
    given depth (moment estimator, pooled per class and TP53 group) gives, under a gamma model, the ratio of the true
    TRIM72 rate in detected vs undetected cells; the log rate ratio CI divided by its log2 is the CI per doubling
    (also with half of alpha taken as technical).

    python3 single_cell_all.py [--data DIR] [--max-cells-per-group 2000] [--workers 3] [--perm 10000] [--recompute]

Data folder: --data (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M), read only. Gene modules: ../gene_modules.csv
(--modules). Tables: $MG53_OUT/tables (default <this folder>/tables), see README_tables.txt there; cache:
$MG53_OUT/cache (per-group fits; reused when the parameters match, so the tables can be rebuilt in ~1-2 min).
Python: numpy, pandas, scipy, pyarrow (parquet); psutil is used for memory reporting when installed.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import glob  # noqa: E402
import json  # noqa: E402
import multiprocessing as mp  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
import warnings  # noqa: E402
from collections import deque  # noqa: E402
from concurrent.futures import ThreadPoolExecutor  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

try:
    import resource  # noqa: E402  (POSIX only)
except ImportError:  # pragma: no cover  (Windows)
    resource = None
try:
    import psutil  # noqa: E402  (optional, memory reporting only)
except ImportError:
    psutil = None

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
MODULES_CSV = os.path.join(os.path.dirname(HERE), "gene_modules.csv")      # mg53_p53/gene_modules.csv
VERSION = 2
GENE = "TRIM72"
# ambient negative controls: gene -> p53_functional_status.csv flag of the lines that lack it
AMBIENT = {"CDKN2A": "cdkn2a_deleted", "MTAP": "mtap_null"}
# the gene panel's 21-gene P53_ACTIVITY score (= tahoe_gene_panel.P53_ACTIVITY; checked at run time when importable)
P53_MEMBERS = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC",
               "PHLDA3", "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
P53_EXT = ["TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "TNFRSF10B", "PHLDA3", "SPATA18", "TRIAP1", "RPS27L", "ACER2",
           "TP53INP1", "PLK3", "POLH", "EDA2R", "CCNG1", "BTG2", "TIGAR"]               # tahoe_gene_panel CONTEXT P53_EXT
P53_PRIMARY = ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2"]     # gene_modules.csv p53_primary (best WT/alt separators)
PRIMARY_OUT = ["P53_SCORE", "P53_PRIMARY5"] + P53_PRIMARY + ["TP53"]
# p53-linked genes: never a placebo predictor or placebo outcome
P53_LINKED = set(P53_MEMBERS + P53_EXT + ["TP53", "GADD45A", "SESN2", "PMAIP1", "ATF3", "PSMD10", "CDKN2A", GENE])
CONTEXT = {"NRF2_CORE": ["NQO1", "GCLM", "GCLC", "TXNRD1", "SRXN1", "OSGIN1", "AKR1C1", "AKR1C2", "AKR1B10", "G6PD", "ME1",
                    "PIR", "ABCC3"],
           "ISR_ATF4": ["DDIT3", "ASNS", "TRIB3", "ATF3", "PSAT1", "PHGDH", "PSPH", "SLC3A2", "SLC7A5", "VEGFA",
                        "CEBPB"],
           "UPR_ER": ["HSPA5", "HERPUD1", "DNAJB9", "SDF2L1", "SEL1L", "PDIA4", "XBP1"],
           "HSF1_HEAT": ["HSPA1A", "HSPA1B", "DNAJB1", "HSPH1", "HSPA6", "BAG3"],
           "IFN": ["ISG15", "IFIT1", "IFIT3", "MX1", "OAS1", "IFI6", "IFI44L", "STAT1", "IRF7", "IFITM1"],
           "NFKB": ["NFKBIA", "TNFAIP3", "RELB", "NFKB2", "BIRC3", "CXCL8", "ICAM1", "IER3"]}
FERRO = ["PTGS2", "CHAC1", "SLC7A11", "GPX4", "ACSL4", "LPCAT3", "AIFM2", "NFE2L2", "HMOX1", "TFRC", "FTH1", "FTL",
         "NCOA4"]
PYRO = ["GSDMD", "GSDME", "NLRP3", "AIM2", "PYCARD", "CASP1", "CASP4", "CASP5", "CASP3", "IL1B", "IL18"]
STRESS_PROGRAM = set(sum(CONTEXT.values(), [])) | {"HMOX1"}      # 'stress program' label of a placebo predictor
# screen modules (mg53_p53/gene_modules.csv, restricted to genes in the per-cell panel)
SCORES = {"P53_SCORE": P53_MEMBERS, "P53_PRIMARY5": P53_PRIMARY,
          "NFKB_SCORE": ["NFKBIA", "TNFAIP3", "CXCL8"], "NFKB8_SCORE": CONTEXT["NFKB"],
          "FERROPTOSIS_SCORE": ["SLC7A11", "GPX4", "CHAC1"], "APOPTOSIS_SCORE": ["BAX", "BBC3", "PMAIP1"]}
SCREEN_GENES = ["NFKBIA", "TNFAIP3", "CXCL8", "RELB", "NFKB2", "BIRC3", "ICAM1", "IER3", "SLC7A11", "GPX4", "CHAC1",
                "BAX", "BBC3", "PMAIP1", "ATF3", "DDIT3"]
SCREEN_OUT = ["NFKB_SCORE", "NFKB8_SCORE", "FERROPTOSIS_SCORE", "APOPTOSIS_SCORE"] + SCREEN_GENES
# outcomes of the placebo-predictor fits (the p53 and screen read-outs)
K2_OUT = (PRIMARY_OUT + [x for x in P53_MEMBERS if x not in PRIMARY_OUT]
          + ["NFKB_SCORE", "FERROPTOSIS_SCORE", "APOPTOSIS_SCORE", "SLC7A11", "ATF3", "PMAIP1"])
SCREEN_MODULE_OF = {"NFKB_SCORE": "NF-kB", "NFKB8_SCORE": "NF-kB", "FERROPTOSIS_SCORE": "ferroptosis",
                    "APOPTOSIS_SCORE": "apoptosis", "NFKBIA": "NF-kB", "TNFAIP3": "NF-kB", "CXCL8": "NF-kB",
                    "RELB": "NF-kB", "NFKB2": "NF-kB", "BIRC3": "NF-kB", "ICAM1": "NF-kB", "IER3": "NF-kB",
                    "SLC7A11": "ferroptosis", "GPX4": "ferroptosis", "CHAC1": "ferroptosis", "BAX": "apoptosis",
                    "BBC3": "apoptosis", "PMAIP1": "apoptosis / stress", "ATF3": "stress", "DDIT3": "stress"}
NOT_IN_CELL_PANEL_NOTE = ("gene_modules.csv modules not in the per-cell panel (no single-cell test possible): "
                          "PI3K-AKT/FAK (TXNIP, IRS1, PTK2), cell cycle (CCND1, KIF11), RAC1, MCL1, FOS, HEXIM1, GDF15")
CLASSES = ["DMSO", "TRIM72 raisers", "p53 activators", "other drugs", "all wells"]
HIGH_TRIM72_PLATES = {"plate1", "plate2", "plate3", "plate14"}
MAX_ITER = 25
GZ = dict(method="gzip", mtime=0)       # gzip header without a timestamp: reruns give byte-identical files
TOL = 1e-6


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


_MEM_PEAK = {"self": 0.0, "children": 0.0}


def _ru_maxrss_gb(who):
    """getrusage peak RSS in GB (ru_maxrss is bytes on macOS, KiB on Linux / BSD); nan without the resource module."""
    if resource is None:
        return float("nan")
    v = resource.getrusage(who).ru_maxrss
    return v / 1024 ** 3 if sys.platform == "darwin" else v / 1024 ** 2


def rss_gb():
    """Peak resident memory of this process (GB): psutil's current RSS (running maximum over the calls) when psutil is
    installed, and getrusage's peak where the resource module exists; the larger of the two."""
    if psutil is not None:
        try:
            _MEM_PEAK["self"] = max(_MEM_PEAK["self"], psutil.Process().memory_info().rss / 1024 ** 3)
        except Exception:  # noqa: BLE001
            pass
    if resource is not None:
        _MEM_PEAK["self"] = max(_MEM_PEAK["self"], _ru_maxrss_gb(resource.RUSAGE_SELF))
    return _MEM_PEAK["self"]


def children_rss_gb():
    """Largest RSS of one child process (GB): psutil (running maximum over the calls, live children) and getrusage
    RUSAGE_CHILDREN (children that have exited and been waited for); the larger of the two."""
    if psutil is not None:
        try:
            kids = psutil.Process().children(recursive=True)
            if kids:
                _MEM_PEAK["children"] = max(_MEM_PEAK["children"],
                                            max(k.memory_info().rss for k in kids) / 1024 ** 3)
        except Exception:  # noqa: BLE001
            pass
    if resource is not None:
        _MEM_PEAK["children"] = max(_MEM_PEAK["children"], _ru_maxrss_gb(resource.RUSAGE_CHILDREN))
    return _MEM_PEAK["children"]


def bh(p):
    p = np.asarray(p, dtype=float)
    out = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    if ok.sum():
        pv = p[ok]
        o = np.argsort(pv)
        r = pv[o] * len(pv) / np.arange(1, len(pv) + 1)
        r = np.minimum.accumulate(r[::-1])[::-1]
        q = np.empty_like(r)
        q[o] = np.minimum(r, 1)
        out[ok] = q
    return out


# ============================================================================= statistics (shared with the workers)
def poisson_glm(y, X, off, n_iter=30, tol=1e-8):
    """Scalar quasi-Poisson GLM, a copy of downstream_p53.poisson_glm: used to check the batched fit."""
    n, p = X.shape
    b = np.zeros(p)
    b[0] = np.log(max(y.mean(), 1e-8) / np.exp(off).mean())
    for _ in range(n_iter):
        eta = X @ b + off
        mu = np.exp(np.clip(eta, -30, 30))
        z = eta - off + (y - mu) / mu
        XtW = X.T * mu
        bn = np.linalg.solve(XtW @ X, XtW @ z)
        if np.max(np.abs(bn - b)) < tol:
            b = bn
            break
        b = bn
    mu = np.exp(np.clip(X @ b + off, -30, 30))
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, n - p)))
    cov = phi * np.linalg.inv((X.T * mu) @ X)
    return b, cov, phi


def _solve(A, b):
    try:
        return np.linalg.solve(A, b[:, :, None])[:, :, 0]
    except np.linalg.LinAlgError:
        out = np.empty_like(b)
        for i in range(len(A)):
            out[i] = np.linalg.lstsq(A[i], b[i], rcond=None)[0]
        return out


def irls_batch(Y, Xs, D, pidx, off):
    """Many quasi-Poisson GLMs on the same cells at once. Column c: Y[:, c] ~ Xs + D[:, pidx[c]], offset off.
    Returns the predictor coefficient, its quasi-Poisson SE, the dispersion, iterations and a converged flag."""
    n, C = Y.shape
    q = Xs.shape[1]
    p = q + 1
    P = D.shape[1]
    B = np.zeros((C, p))
    B[:, 0] = np.log(np.maximum(Y.sum(0), 0.5) / np.exp(off).sum())
    XX = (Xs[:, :, None] * Xs[:, None, :]).reshape(n, q * q)
    DX = (D[:, :, None] * Xs[:, None, :]).reshape(n, P * q)
    sel = pidx[:, None] * q + np.arange(q)[None, :]
    Yt = np.ascontiguousarray(Y.T)
    act = np.arange(C)
    its = np.zeros(C, np.int16)
    conv = np.zeros(C, bool)
    offr = off[None, :]
    for _ in range(MAX_ITER):
        if not len(act):
            break
        na = len(act)
        ar = np.arange(na)
        Ba = B[act]
        M = np.zeros((P, na))
        M[pidx[act], ar] = Ba[:, q]
        etaT = Ba[:, :q] @ Xs.T + M.T @ D.T + offr
        np.clip(etaT, -30, 30, out=etaT)
        muT = np.exp(etaT)
        mzT = muT * (etaT - offr) + (Yt[act] - muT)
        A = np.empty((na, p, p))
        A[:, :q, :q] = (muT @ XX).reshape(na, q, q)
        sd = (muT @ DX)[ar[:, None], sel[act]]
        A[:, :q, q] = sd
        A[:, q, :q] = sd
        A[:, q, q] = sd[:, 0]
        bb = np.empty((na, p))
        bb[:, :q] = mzT @ Xs
        bb[:, q] = (mzT @ D)[ar, pidx[act]]
        Bn = _solve(A, bb)
        dmax = np.abs(Bn - Ba).max(1)
        B[act] = Bn
        its[act] += 1
        done = dmax < TOL
        conv[act[done]] = True
        act = act[~done]
    ar = np.arange(C)
    M = np.zeros((P, C))
    M[pidx, ar] = B[:, q]
    etaT = np.clip(B[:, :q] @ Xs.T + M.T @ D.T + offr, -30, 30)
    muT = np.exp(etaT)
    phi = np.maximum(1.0, ((Yt - muT) ** 2 / muT).sum(1) / max(1, n - p))
    A = np.empty((C, p, p))
    A[:, :q, :q] = (muT @ XX).reshape(C, q, q)
    sd = (muT @ DX)[ar[:, None], sel]
    A[:, :q, q] = sd
    A[:, q, :q] = sd
    A[:, q, q] = sd[:, 0]
    with np.errstate(invalid="ignore"):
        try:
            Ainv = np.linalg.inv(A)
        except np.linalg.LinAlgError:
            Ainv = np.linalg.pinv(A)
        se = np.sqrt(phi * Ainv[:, q, q])
    return B[:, q], se, phi, its, conv


# ============================================================================= worker side
W = {}


def init_worker(cfg):
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    W.update(cfg)


def fit_group(T, S, G, Ym, line):
    """One (well, line) group. Ym: cells x panel columns (uint16)."""
    c = W
    n = len(T)
    T = T.astype(np.float64)
    lt = np.log(T)
    sS = np.log((S + 0.5) / T)
    sG = np.log((G + 0.5) / T)
    cols_x = [np.ones(n), lt - lt.mean(), sS - sS.mean(), sG - sG.mean()]
    for a_ in c["adj_cols"]:                                  # --adjust: log fraction of an extra gene
        v = np.log((Ym[:, a_] + 0.5) / T)
        cols_x.append(v - v.mean())
    Xs = np.column_stack(cols_x)
    Yf = Ym.astype(np.float64)
    Yo = Yf @ c["Wout"]                                       # cells x outcomes (scores = member sums)
    y72 = Yf[:, c["col72"]]
    pcols = c["pred_cols"]
    Dall = (Ym[:, pcols] > 0)
    nd = Dall.sum(0)
    ysum = Yo.sum(0)
    Tsum = T.sum()
    expr_o = c["expr_out"][line]
    expr_p = c["expr_pred"][line]
    gstat = dict(n_used=n, n_det=int(nd[0]), y72=float(y72.sum()))
    r72 = y72.sum() / Tsum
    m = T * r72
    gstat["alpha_num"] = float(((y72 - m) ** 2 - y72).sum())
    gstat["alpha_den"] = float((m ** 2).sum())
    gstat["mbar"] = float(m.mean())
    cols_k, cols_j, pj_used = [], [], []
    for j in range(len(pcols)):
        if not expr_p[j] or nd[j] < c["min_det"] or n - nd[j] < c["min_det"]:
            continue
        Tdet = T[Dall[:, j]].sum()
        ks = c["out_trim"] if j == 0 else c["out_k2"]
        ks = ks[expr_o[ks] & (ysum[ks] >= c["min_counts"]) & (ysum[ks] / Tsum * Tdet >= c["min_exp_det"])]
        if not len(ks):
            continue
        cols_k.append(ks)
        cols_j.append(np.full(len(ks), len(pj_used)))
        pj_used.append(j)
    if not pj_used:
        return gstat, None
    ks = np.concatenate(cols_k)
    jj = np.concatenate(cols_j)
    D = Dall[:, pj_used].astype(np.float64)
    beta, se, phi, its, conv = irls_batch(Yo[:, ks], Xs, D, jj, lt)
    Dk = D[:, jj].astype(bool)
    Yk = Yo[:, ks]
    ydet = (Yk * Dk).sum(0)
    Tdet = (T[:, None] * Dk).sum(0)
    yund = ysum[ks] - ydet
    Tund = Tsum - Tdet
    sep = (ydet <= 0) | (yund <= 0)
    bad = sep | ~conv | ~np.isfinite(se)
    unadj = np.log((ydet + 0.5) / Tdet) - np.log((yund + 0.5) / Tund)
    res = dict(pred=np.asarray(pj_used, np.int16)[jj], outcome=ks.astype(np.int16),
               beta=np.where(bad, np.nan, beta).astype(np.float32), se=np.where(bad, np.nan, se).astype(np.float32),
               phi=phi.astype(np.float32), unadj=unadj.astype(np.float32), n_det_pred=nd[np.asarray(pj_used)[jj]]
               .astype(np.int32), y_tot=ysum[ks].astype(np.int32), y_det=ydet.astype(np.int32),
               flag=(sep.astype(np.int8) + 2 * (~conv).astype(np.int8)), iters=its)
    return gstat, res


def fit_chunk(chunk):
    """chunk: dict(gids, lines, offs, T, S, G, Y). Returns per-group stats and the stacked per-column fits."""
    out_g, out_f = [], []
    chk = []
    offs = chunk["offs"]
    for i, gid in enumerate(chunk["gids"]):
        a, b = offs[i], offs[i + 1]
        T, S, G, Ym = chunk["T"][a:b], chunk["S"][a:b], chunk["G"][a:b], chunk["Y"][a:b]
        line = int(chunk["lines"][i])
        if b - a < W["min_cells"]:
            out_g.append(dict(gid=int(gid), n_used=int(b - a), n_det=int((Ym[:, W["col72"]] > 0).sum()),
                              fitted=False))
            continue
        gstat, res = fit_group(T, S, G, Ym, line)
        gstat.update(gid=int(gid), fitted=res is not None)
        out_g.append(gstat)
        if res is not None:
            res["gid"] = np.full(len(res["beta"]), gid, np.int32)
            out_f.append(res)
            if gid < W["n_groups"] and gid % W["check_every"] == 0:   # scalar re-fit of TRIM72 x P53_SCORE (check)
                k0 = W["k_p53score"]
                sel = np.where((res["pred"] == 0) & (res["outcome"] == k0))[0]
                if len(sel) and np.isfinite(res["beta"][sel[0]]):
                    Tf = T.astype(np.float64)
                    lt = np.log(Tf)
                    sS = np.log((S + 0.5) / Tf)
                    sG = np.log((G + 0.5) / Tf)
                    det = (Ym[:, W["col72"]] > 0).astype(float)
                    xc = [np.ones(len(Tf)), det, lt - lt.mean(), sS - sS.mean(), sG - sG.mean()]
                    for a_ in W["adj_cols"]:
                        v = np.log((Ym[:, a_] + 0.5) / Tf)
                        xc.append(v - v.mean())
                    X = np.column_stack(xc)
                    y = Ym.astype(np.float64) @ W["Wout"][:, k0]
                    try:
                        bs, cov, _ = poisson_glm(y, X, lt)
                        chk.append((int(gid), float(res["beta"][sel[0]]), float(bs[1]), float(res["se"][sel[0]]),
                                    float(np.sqrt(cov[1, 1]))))
                    except np.linalg.LinAlgError:
                        pass
    fits = {k: np.concatenate([r[k] for r in out_f]) for k in out_f[0]} if out_f else None
    return out_g, fits, chk


# ============================================================================= setup
def resolve_paths(args):
    data = os.path.abspath(os.path.expanduser(args.data))
    out = os.environ.get("MG53_OUT") or HERE
    tab, cdir = os.path.join(out, "tables"), os.path.join(out, "cache")
    for d in (tab, cdir):
        os.makedirs(d, exist_ok=True)
    real_data = os.path.realpath(data)
    for d in (tab, cdir):
        if os.path.realpath(d).startswith(real_data + os.sep):
            sys.exit(f"refusing to write under the data folder: {d}")
    return data, tab, cdir


def load_setup(data, args):
    gp = os.path.join(data, "gene_panel")
    eff = os.path.join(data, "atlas", "effects")
    sm = pd.read_csv(os.path.join(gp, "sample_map.csv"))
    sm["sample"] = sm["sample"].astype(str)
    failed = set(pd.read_csv(os.path.join(eff, "failed_wells.csv"))["sample"].astype(str))
    # drug-dose classes
    res = os.path.join(gp, "results")
    tr = pd.read_csv(os.path.join(res, "TRIM72_drug_effects_by_dose.csv"))
    ps = pd.read_csv(os.path.join(res, "pathway_scores_by_dose.csv"))
    p53 = ps[ps["score"] == "P53_ACTIVITY"]
    raise_keys = set(map(tuple, tr.loc[tr["call"].eq("up"), ["drug", "conc"]].itertuples(index=False)))
    p53_keys = set(map(tuple, p53.loc[(p53["fdr_up"] < 0.10) & (p53["z"] >= 3), ["drug", "conc"]]
                       .itertuples(index=False)))
    known = set(map(tuple, tr[["drug", "conc"]].itertuples(index=False)))
    cls, sub = [], []
    for d, cc, dm in sm[["drug", "conc", "is_dmso"]].itertuples(index=False):
        k = (d, cc)
        if dm:
            cls.append("DMSO")
            sub.append("DMSO")
        elif k in raise_keys:
            cls.append("TRIM72 raisers")
            sub.append("TRIM72 raiser, p53 activated" if k in p53_keys else "TRIM72 raiser, p53 not activated")
        elif k in p53_keys:
            cls.append("p53 activators")
            sub.append("p53 activator")
        else:
            cls.append("other drugs")
            sub.append("other drug" if k in known else "other drug (no drug-dose call)")
    sm["well_class"] = cls
    sm["well_subclass"] = sub
    sm["failed_well"] = sm["sample"].isin(failed)
    # lines, TP53 groups, expression
    lines = pd.read_csv(os.path.join(eff, "lines.csv"))
    lines["cell_line_id"] = lines["cell_line_id"].astype(str)
    base = pd.read_csv(os.path.join(res, "baseline_by_cell_line.csv")).set_index("cell_line_id")
    lines["tp53_group"] = base["tp53_group"].reindex(lines["cell_line_id"]).to_numpy()
    # TP53 functional status (gene panel): the alternative grouping, and the flags of the ambient-control lines
    sp = os.path.join(res, "p53_functional_status.csv")
    lines["functional_call"] = np.nan
    lines["p53_responsiveness_log2"] = np.nan
    for flag in AMBIENT.values():
        lines[flag] = False
    if os.path.exists(sp):
        st = pd.read_csv(sp)
        st["cell_line_id"] = st["cell_line_id"].astype(str)
        st = st.drop_duplicates("cell_line_id").set_index("cell_line_id")
        lines["functional_call"] = st["functional_call"].reindex(lines["cell_line_id"]).to_numpy()
        lines["p53_responsiveness_log2"] = st["p53_responsiveness_log2"].reindex(lines["cell_line_id"]).to_numpy()
        for flag in AMBIENT.values():
            if flag in st.columns:
                lines[flag] = st[flag].reindex(lines["cell_line_id"]).eq(True).to_numpy()
    else:
        log(f"WARNING: {sp} not found: the TP53 functional-status grouping and the ambient controls are skipped")
    ga = pd.read_csv(os.path.join(eff, "genes.csv"))
    ga = ga[ga["kind"] == "gene"].drop_duplicates("symbol").set_index("symbol")
    em = np.load(os.path.join(eff, "expr_mask.npy"), mmap_mode="r")
    wl = pd.read_parquet(os.path.join(gp, "well_line.parquet"))
    panel = [c[4:] for c in wl.columns if c.startswith("det_")]
    expr = pd.DataFrame({g: (np.asarray(em[:, int(ga.loc[g, "col"])]).astype(bool) if g in ga.index
                             else np.zeros(len(lines), bool)) for g in panel}, index=lines["cell_line_id"])
    amb = ambient_lines(wl, lines, failed, args.ambient_max_ratio)
    return sm, lines, expr, wl, panel, ga, amb


def ambient_lines(wl, lines, failed, max_ratio):
    """Lines flagged as lacking CDKN2A / MTAP, with the ratio of their reads of that gene to the ambient expectation
    (soup = the other lines of the same wells pooled; expected = soup CPM x the line's UMI, summed over its wells).
    A truly deleted gene sits at the ambient level (ratio ~0.05-0.2); a ratio near 1 means the gene is expressed, so the
    line is not used as an ambient control (used = ratio < max_ratio)."""
    rows = []
    cols = ["gene", "flag", "cell_line_id", "cell_name", "tp53_group", "n_wells", "line_cpm", "soup_cpm",
            "ambient_ratio", "used"]
    genes = [x for x in AMBIENT if x in wl.columns]
    if not genes:
        return pd.DataFrame(columns=cols)
    w = wl[["sample", "cell_line_id", "total_counts"] + genes].copy()
    w["sample"] = w["sample"].astype(str)
    w["cell_line_id"] = w["cell_line_id"].astype(str)
    w = w[~w["sample"].isin(failed)].groupby(["sample", "cell_line_id"], as_index=False).sum()
    tot = w.groupby("sample")[["total_counts"] + genes].sum()
    for gname in genes:
        flag = AMBIENT[gname]
        for cid, cname, tp in lines.loc[lines[flag], ["cell_line_id", "cell_name", "tp53_group"]].itertuples(
                index=False):
            h = w[w["cell_line_id"] == cid].set_index("sample")
            if h.empty:
                continue
            t = tot.loc[h.index]
            soup = (t[gname] - h[gname]) / (t["total_counts"] - h["total_counts"])
            expd = float((soup * h["total_counts"]).sum())
            n_umi = float(h["total_counts"].sum())
            rows.append(dict(gene=gname, flag=flag, cell_line_id=cid, cell_name=cname, tp53_group=tp, n_wells=len(h),
                             line_cpm=1e6 * float(h[gname].sum()) / n_umi, soup_cpm=1e6 * expd / n_umi,
                             ambient_ratio=float(h[gname].sum()) / expd if expd > 0 else np.nan))
    if not rows:                                          # no flagged lines (or no p53_functional_status.csv)
        return pd.DataFrame(columns=cols)
    A = pd.DataFrame(rows)
    A["used"] = A["ambient_ratio"] < max_ratio
    return A


def build_design(sm, lines, expr, wl, panel, amb, args):
    """Groups, placebo predictors, ambient controls, outcomes and the cell-matrix columns."""
    li = {c: i for i, c in enumerate(lines["cell_line_id"])}
    si = {s: i for i, s in enumerate(sm["sample"])}
    g = wl[["sample", "cell_line_id", "n_cells"] + [f"det_{x}" for x in panel]].copy()
    g["sample"] = g["sample"].astype(str)
    g["cell_line_id"] = g["cell_line_id"].astype(str)
    # duplicate (sample, line) rows, if any, are summed
    g = g.groupby(["sample", "cell_line_id"], as_index=False).sum()
    g["s_idx"] = g["sample"].map(si)
    g["l_idx"] = g["cell_line_id"].map(li)
    g = g.dropna(subset=["s_idx", "l_idx"]).copy()
    g["s_idx"] = g["s_idx"].astype(int)
    g["l_idx"] = g["l_idx"].astype(int)
    smi = sm.set_index("sample")
    for col in ("plate", "drug", "conc", "well", "well_class", "well_subclass", "failed_well"):
        g[col] = smi[col].reindex(g["sample"]).to_numpy()
    g["tp53_group"] = lines["tp53_group"].to_numpy()[g["l_idx"]]
    g["cell_name"] = lines["cell_name"].to_numpy()[g["l_idx"]]
    g["trim72_expressed"] = expr[GENE].to_numpy()[g["l_idx"]]
    d72 = g[f"det_{GENE}"]
    reason = np.select([g["failed_well"].astype(bool), ~g["trim72_expressed"], ~g["tp53_group"].isin(["WT", "altered"]),
                        g["n_cells"] < args.min_cells, d72 < args.min_det, g["n_cells"] - d72 < args.min_det],
                       ["failed well", "TRIM72 not expressed in line", "TP53 group unknown",
                        f"< {args.min_cells} cells", f"< {args.min_det} TRIM72-detected cells",
                        f"< {args.min_det} undetected cells"], "")
    g["skip_reason"] = reason
    g["qualifies"] = reason == ""
    cap = args.max_cells_per_group
    g["keep_prob"] = np.where(g["qualifies"], np.minimum(1.0, cap / g["n_cells"]) if cap > 0 else 1.0, 0.0)
    g = g.sort_values(["s_idx", "l_idx"]).reset_index(drop=True)
    q = g["qualifies"].to_numpy()
    # cap-0 sample: groups the cap could leave with < min_det TRIM72-detected (or undetected) cells (binomial
    # probability > 1e-6 under the Bernoulli subsample) are 'at risk'; a random --cap0-frac of them is also fitted
    # with all cells, so the groups the cap drops can be put back in a sensitivity analysis
    risk = np.zeros(len(g), bool)
    cap0 = np.zeros(len(g), bool)
    if cap > 0 and args.cap0_frac > 0:
        pk, nn, dd = g["keep_prob"].to_numpy(), g["n_cells"].to_numpy(), g[f"det_{GENE}"].to_numpy()
        with np.errstate(invalid="ignore"):
            pdrop = (stats.binom.cdf(args.min_det - 1, dd, pk) + stats.binom.cdf(args.min_det - 1, nn - dd, pk))
        risk = q & (pk < 1) & (pdrop > 1e-6)
        cap0 = risk & (np.random.default_rng([args.seed, 999]).random(len(g)) < args.cap0_frac)
    g["cap0_at_risk"] = risk
    g["cap0_sampled"] = cap0
    # placebo predictors: detection rate in the qualifying groups within 1/r - r x of TRIM72's
    ncell = g.loc[q, "n_cells"].sum()
    rate = pd.Series({x: g.loc[q, f"det_{x}"].sum() / ncell for x in panel})
    r72 = rate[GENE]
    rr = args.placebo_range
    in_atlas = expr.any(axis=0)
    placebo = [x for x in panel if x not in P53_LINKED and x not in SCREEN_GENES and x != GENE and bool(in_atlas[x])
               and r72 / rr <= rate[x] <= r72 * rr]
    placebo = sorted(placebo, key=lambda x: rate[x])
    placebo_out = [x for x in panel if x not in P53_LINKED and x not in SCREEN_GENES and x != GENE
                   and bool(in_atlas[x])]
    # outcomes
    outcomes = (list(SCORES) + [x for x in P53_PRIMARY] + ["TP53"] + [x for x in P53_MEMBERS if x not in P53_PRIMARY]
                + [x for x in SCREEN_GENES if x not in P53_MEMBERS] + placebo_out)
    outcomes = list(dict.fromkeys(outcomes))
    adjust = [x.strip() for x in args.adjust.split(",") if x.strip()]
    bad = [x for x in adjust if x not in panel]
    if bad:
        sys.exit(f"--adjust: not in the per-cell panel: {', '.join(bad)}")
    # ambient negative controls: 'CDKN2A detected' in the CDKN2A-deleted lines (and MTAP in MTAP-null lines) whose
    # reads of that gene are at the ambient level; fitted only in those lines
    amb_lines = {}
    if len(amb):
        for gname in AMBIENT:
            ids = set(amb.loc[(amb["gene"] == gname) & amb["used"], "cell_line_id"])
            if gname in panel and gname not in adjust and gname not in placebo and len(ids) >= 2:
                amb_lines[gname] = ids
    amb_preds = list(amb_lines)
    amb_rate = {}
    for x in amb_preds:
        m = q & g["cell_line_id"].isin(amb_lines[x]).to_numpy()
        amb_rate[x] = g.loc[m, f"det_{x}"].sum() / max(1, g.loc[m, "n_cells"].sum())
        amb_rate[x + " (TRIM72)"] = g.loc[m, f"det_{GENE}"].sum() / max(1, g.loc[m, "n_cells"].sum())
    need = list(dict.fromkeys([GENE] + placebo + amb_preds + adjust
                              + [x for o in outcomes for x in (SCORES.get(o, [o]))]))
    need = [x for x in panel if x in need]                                # keep the file's column order
    cidx = {x: i for i, x in enumerate(need)}
    Wout = np.zeros((len(need), len(outcomes)))
    for k, o in enumerate(outcomes):
        for x in SCORES.get(o, [o]):
            Wout[cidx[x], k] = 1.0
    expr_out = np.ones((len(lines), len(outcomes)), bool)
    for k, o in enumerate(outcomes):
        if o not in SCORES:
            expr_out[:, k] = expr[o].to_numpy()
    preds = [GENE] + placebo + amb_preds
    expr_pred = np.column_stack([expr[x].to_numpy() for x in [GENE] + placebo]
                                + [lines["cell_line_id"].isin(amb_lines[x]).to_numpy() for x in amb_preds])
    otype = {}
    for o in outcomes:
        if o in ("P53_SCORE", "P53_PRIMARY5"):
            otype[o] = "p53 score"
        elif o in P53_PRIMARY:
            otype[o] = "p53 primary target"
        elif o == "TP53":
            otype[o] = "TP53 mRNA"
        elif o in P53_MEMBERS:
            otype[o] = "p53 target (score member)"
        elif o in SCORES:
            otype[o] = "screen module score"
        elif o in SCREEN_GENES:
            otype[o] = "screen gene"
        else:
            otype[o] = "placebo outcome (non-p53 panel gene)"
    return dict(groups=g, placebo=placebo, placebo_out=placebo_out, outcomes=outcomes, need=need, Wout=Wout, adjust=adjust,
                expr_out=expr_out, expr_pred=expr_pred, preds=preds, rate=rate, otype=otype, n_plac=len(placebo),
                amb_preds=amb_preds, amb_lines=amb_lines, amb_rate=amb_rate, amb=amb,
                total_cells=int(wl["n_cells"].sum()))


def program_of(x):
    for k, v in CONTEXT.items():
        if x in v:
            return k
    if x in FERRO:
        return "ferroptosis"
    if x in PYRO:
        return "pyroptosis"
    if x in ("MTAP", "CDKN2B"):
        return "9p21 anchor"
    if x in ("ABCB1", "ABCG2"):
        return "drug efflux"
    return "other"


# ============================================================================= streaming
class PlateBuf:
    def __init__(self, cap, ncol):
        cap = int(cap)
        self.n = 0
        self.gid = np.empty(cap, np.int32)
        self.T = np.empty(cap, np.float32)
        self.S = np.empty(cap, np.uint16)
        self.G = np.empty(cap, np.uint16)
        self.Y = np.empty((cap, ncol), np.uint16)

    def add(self, gid, T, S, G, Y):
        k = len(gid)
        if self.n + k > len(self.gid):
            new = int((self.n + k) * 1.25) + 1000
            for a in ("gid", "T", "S", "G", "Y"):
                old = getattr(self, a)
                arr = np.empty((new,) + old.shape[1:], old.dtype)
                arr[:self.n] = old[:self.n]
                setattr(self, a, arr)
        sl = slice(self.n, self.n + k)
        self.gid[sl], self.T[sl], self.S[sl], self.G[sl], self.Y[sl] = gid, T, S, G, Y
        self.n += k


def to_u16(a):
    return np.clip(np.rint(a), 0, 65535).astype(np.uint16)


def stream_and_fit(data, args, D, cdir):
    import pyarrow.parquet as pq
    g = D["groups"]
    files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))
    if args.limit_files:
        files = files[:args.limit_files]
    sm_samples = D["sm"]["sample"].tolist()
    s_index = {s: i for i, s in enumerate(sm_samples)}
    l_index = {c: i for i, c in enumerate(D["lines"]["cell_line_id"])}
    nS, nL = len(sm_samples), len(l_index)
    plates = sorted(D["sm"]["plate"].unique(), key=lambda x: int(x.replace("plate", "")))
    p_index = {p: i for i, p in enumerate(plates)}
    plate_of_s = D["sm"]["plate"].map(p_index).to_numpy()
    LUT = np.full((nS, nL), -1, np.int64)
    q = g["qualifies"].to_numpy()
    LUT[g.loc[q, "s_idx"], g.loc[q, "l_idx"]] = g.index[q]
    keep_prob = g["keep_prob"].to_numpy()
    cap0 = g["cap0_sampled"].to_numpy()                   # these groups are also fitted with all cells (gid + NG)
    NG = len(g)
    exp_plate = np.zeros(len(plates))
    np.add.at(exp_plate, plate_of_s[g["s_idx"].to_numpy()], g["n_cells"].to_numpy())
    kept_exp = np.zeros(len(plates))
    np.add.at(kept_exp, plate_of_s[g["s_idx"].to_numpy()], g["n_cells"].to_numpy() * (keep_prob + cap0))
    need = D["need"]
    cols = ["sample", "cell_line_id", "total_counts", "S_PHASE", "G2M_PHASE"] + need
    adj_cols = [need.index(x) for x in D["adjust"]]
    out_ok = ~(D["Wout"][adj_cols].sum(0) > 0) if adj_cols else np.ones(len(D["outcomes"]), bool)
    out_trim = np.arange(len(D["outcomes"]))
    out_k2 = np.array([D["outcomes"].index(o) for o in K2_OUT])
    cfg = dict(Wout=D["Wout"], col72=need.index(GENE), pred_cols=np.array([need.index(x) for x in D["preds"]]),
               out_trim=out_trim[out_ok[out_trim]], out_k2=out_k2[out_ok[out_k2]], adj_cols=adj_cols,
               expr_out=D["expr_out"],
               expr_pred=D["expr_pred"], min_det=args.min_det, min_counts=args.min_outcome_counts,
               min_exp_det=args.min_expected_det, min_cells=args.min_cells, check_every=args.check_every,
               k_p53score=D["outcomes"].index("P53_SCORE"), n_groups=NG)
    ctx = mp.get_context("spawn")
    pool = ctx.Pool(args.workers, initializer=init_worker, initargs=(cfg,)) if args.workers > 0 else None
    if pool is None:
        init_worker(cfg)
    seen_plate = np.zeros(len(plates))
    seen_group = np.zeros(len(g), np.int64)
    last_file = np.full(len(plates), -1)
    bufs, done_plates = {}, set()
    incomplete = []                                       # plates fitted before all their cells were read
    ignored = dict(cells=0, kept=0)                       # cells of a plate read after that plate was fitted
    results_g, results_f, checks = [], [], []
    inflight = None
    t0 = time.time()

    def collect(r):
        gs, fs, ck = r
        results_g.extend(gs)
        if fs is not None:
            results_f.append(fs)
        checks.extend(ck)

    def chunk_gen(b, order, ug, starts, ends):
        lines_of = g["l_idx"].to_numpy()
        cur, cur_n = [], 0
        for k in range(len(ug) + 1):
            if k < len(ug):
                cur.append(k)
                cur_n += ends[k] - starts[k]
            if cur and (cur_n >= args.chunk_cells or k == len(ug)):
                idx = np.concatenate([order[starts[j]:ends[j]] for j in cur])
                sizes = np.array([ends[j] - starts[j] for j in cur])
                yield dict(gids=ug[cur], lines=lines_of[ug[cur] % NG], offs=np.r_[0, np.cumsum(sizes)],
                           T=b.T[idx], S=b.S[idx], G=b.G[idx], Y=b.Y[idx])
                cur, cur_n = [], 0

    def drain():
        nonlocal inflight
        if inflight is not None:
            for r in inflight:                               # at most one plate in flight
                collect(r)
            inflight = None

    def flush(pi, complete):
        nonlocal inflight
        b = bufs.pop(pi)
        done_plates.add(pi)
        if not complete:
            incomplete.append(plates[pi])
        drain()
        if b.n == 0:
            return
        order = np.argsort(b.gid[:b.n], kind="stable")
        gids_sorted = b.gid[:b.n][order]
        ug, starts = np.unique(gids_sorted, return_index=True)
        ends = np.r_[starts[1:], len(order)]
        del gids_sorted
        gen = chunk_gen(b, order, ug, starts, ends)        # consumed lazily by the pool's feeder thread
        if pool is None:
            for ch in gen:
                collect(fit_chunk(ch))
        else:
            inflight = pool.imap_unordered(fit_chunk, gen)
        log(f"  {plates[pi]}: {len(ug)} groups, {b.n:,} cells sent to fit ({'complete' if complete else 'INCOMPLETE'}); "
            f"{len(results_g)} groups fitted before it; {time.time() - t0:.0f} s; peak RSS {rss_gb():.2f} GB, "
            f"largest worker {children_rss_gb():.2f} GB")
        del b

    def read(f):
        return pq.read_table(f, columns=cols, read_dictionary=["sample", "cell_line_id"], use_threads=False)

    ex = ThreadPoolExecutor(max_workers=max(1, args.readers))
    futs = deque()
    nxt = 0
    for _ in range(min(len(files), 2 * max(1, args.readers))):
        futs.append(ex.submit(read, files[nxt]))
        nxt += 1
    n_seen = 0
    for fi in range(len(files)):
        t = futs.popleft().result()
        if nxt < len(files):
            futs.append(ex.submit(read, files[nxt]))
            nxt += 1
        sa = t.column("sample").combine_chunks()
        la = t.column("cell_line_id").combine_chunks()
        smap = np.array([s_index.get(s, -1) for s in sa.dictionary.to_pylist()], np.int64)
        lmap = np.array([l_index.get(c, -1) for c in la.dictionary.to_pylist()], np.int64)
        s_ix = smap[sa.indices.to_numpy(zero_copy_only=False)]
        l_ix = lmap[la.indices.to_numpy(zero_copy_only=False)]
        okk = (s_ix >= 0) & (l_ix >= 0)
        if not okk.all():
            log(f"  WARNING {os.path.basename(files[fi])}: {int((~okk).sum())} cells of unknown sample / line")
        pl = np.where(okk, plate_of_s[np.where(s_ix >= 0, s_ix, 0)], -1)
        cnt = np.bincount(pl[okk], minlength=len(plates))
        seen_plate += cnt
        last_file[cnt > 0] = fi
        n_seen += len(s_ix)
        gid = np.where(okk, LUT[np.where(s_ix >= 0, s_ix, 0), np.where(l_ix >= 0, l_ix, 0)], -1)
        hit = gid >= 0
        seen_group += np.bincount(gid[hit], minlength=len(g))
        late = [pi for pi in np.nonzero(cnt)[0] if pi in done_plates]
        if late:                                          # cells of an already fitted plate: counted, then ignored
            ignored["cells"] += int(cnt[late].sum())
            log(f"  WARNING: {int(cnt[late].sum())} cells of {', '.join(plates[pi] for pi in late)} after the plate "
                f"was fitted (file {fi}); ignored")
        rng = np.random.default_rng([args.seed, fi])
        u = rng.random(len(gid))
        gsafe = np.where(hit, gid, 0)
        keep = hit & (u < keep_prob[gsafe])               # the capped subsample (main analysis)
        keep0 = hit & cap0[gsafe]                         # all cells of the cap-0 sample groups
        sel = keep | keep0
        if sel.any():
            ki = np.where(sel)[0]
            T = t.column("total_counts").to_numpy()[ki].astype(np.float32)
            S = to_u16(t.column("S_PHASE").to_numpy()[ki])
            Gm = to_u16(t.column("G2M_PHASE").to_numpy()[ki])
            Y = np.empty((len(ki), len(need)), np.uint16)
            for j, x in enumerate(need):
                Y[:, j] = to_u16(t.column(x).to_numpy()[ki])
            # rows: the subsampled cells under their group id, then the cap-0 cells under group id + NG
            r_main, r_cap0 = np.where(keep[ki])[0], np.where(keep0[ki])[0]
            rows = np.concatenate([r_main, r_cap0])
            gk = np.concatenate([gid[ki][r_main], gid[ki][r_cap0] + NG]).astype(np.int32)
            pk = pl[ki][rows]
            for pi in np.unique(pk):
                m = pk == pi
                if pi in done_plates:
                    ignored["kept"] += int(m.sum())
                    continue
                if pi not in bufs:
                    bufs[pi] = PlateBuf(kept_exp[pi] * 1.03 + 5000, len(need))
                rm = rows[m]
                bufs[pi].add(gk[m], T[rm], S[rm], Gm[rm], Y[rm])
        del t
        for pi in list(bufs):
            if seen_plate[pi] >= exp_plate[pi]:
                flush(pi, True)
            elif fi - last_file[pi] > args.stale_files:
                log(f"  WARNING: {plates[pi]} saw {seen_plate[pi]:.0f} of {exp_plate[pi]:.0f} cells and no cells for "
                    f"{args.stale_files} files: fitted as incomplete")
                flush(pi, False)
        if (fi + 1) % 200 == 0:
            log(f"  {fi + 1}/{len(files)} files, {n_seen:,} cells, {time.time() - t0:.0f} s, peak RSS {rss_gb():.2f} GB, "
                f"largest worker {children_rss_gb():.2f} GB")
    ex.shutdown()
    for pi in sorted(bufs):
        flush(pi, False)
    drain()
    if pool is not None:
        pool.close()
        pool.join()
    G = pd.DataFrame(results_g)
    F = {k: np.concatenate([r[k] for r in results_f]) for k in results_f[0]} if results_f else {}
    F = pd.DataFrame(F)
    info = dict(files_read=len(files), cells_read=int(n_seen), seen_group=seen_group.tolist(),
                seen_plate={plates[i]: int(seen_plate[i]) for i in range(len(plates))},
                expected_plate={plates[i]: int(exp_plate[i]) for i in range(len(plates))},
                stream_seconds=round(time.time() - t0, 1), children_peak_rss_gb=round(children_rss_gb(), 2),
                main_peak_rss_gb=round(rss_gb(), 2), incomplete_plates=incomplete,
                cells_ignored_after_flush=ignored["cells"], kept_cells_ignored_after_flush=ignored["kept"])
    return G, F, checks, info


# ============================================================================= meta-analysis
def dl_keys(key, b, se, nk):
    """Vectorised DerSimonian-Laird random-effects meta-analysis of b (SE se) within each key (0..nk-1)."""
    ok = np.isfinite(b) & np.isfinite(se) & (se > 0)
    key, b, se = key[ok], b[ok].astype(float), se[ok].astype(float)
    w = 1 / se ** 2
    k = np.bincount(key, minlength=nk).astype(float)
    sw = np.bincount(key, w, nk)
    sw2 = np.bincount(key, w ** 2, nk)
    with np.errstate(invalid="ignore", divide="ignore"):
        fe = np.bincount(key, w * b, nk) / sw
        Q = np.bincount(key, w * (b - fe[key]) ** 2, nk)
        c = sw - sw2 / sw
        tau2 = np.where((k >= 2) & (c > 0), np.maximum(0.0, (Q - (k - 1)) / c), 0.0)
        ws = 1 / (se ** 2 + tau2[key])
        sws = np.bincount(key, ws, nk)
        m = np.bincount(key, ws * b, nk) / sws
        s = np.sqrt(1 / sws)
        I2 = np.where(Q > 0, np.maximum(0.0, (Q - (k - 1)) / Q), 0.0)
        # Hartung-Knapp: variance scale q = sum w*(b - m)^2 / (k - 1) (used with t on k - 1 df); floored at 1 below
        hk_q = np.bincount(key, ws * (b - m[key]) ** 2, nk) / np.maximum(k - 1, 1)
        s_hk = np.sqrt(np.maximum(1.0, hk_q) / sws)
    npos = np.bincount(key, (b > 0).astype(float), nk)
    m[k == 0] = np.nan
    s[k == 0] = np.nan
    s_hk[k < 2] = np.nan
    return pd.DataFrame(dict(k=k.astype(int), est=m, se=s, tau2=tau2, I2=I2, n_pos=npos.astype(int), se_hk=s_hk,
                             hk_q=np.where(k >= 2, hk_q, np.nan)))


TPN = ["WT", "altered", "all lines"]


def meta_by(cols, dims, b, se):
    key = np.ravel_multi_index([np.asarray(c, np.int64) for c in cols], dims)
    uniq, inv = np.unique(key, return_inverse=True)
    r = dl_keys(inv, np.asarray(b, float), np.asarray(se, float), len(uniq))
    return np.unravel_index(uniq, dims), r, inv


def stage1(R, mask, dims, tp_line, cls_value=None):
    """DL over the wells of each (predictor, outcome, class, line)."""
    cls = R["cls"][mask] if cls_value is None else np.full(int(mask.sum()), cls_value)
    dec, r, _ = meta_by([R["pred"][mask], R["out"][mask], cls, R["line"][mask]], dims, R["b"][mask], R["se"][mask])
    df = pd.DataFrame(dict(pred=dec[0], out=dec[1], cls=dec[2], line=dec[3]))
    df = pd.concat([df, r.rename(columns={"k": "n_wells"})], axis=1)
    df["tp"] = tp_line[df["line"].to_numpy()]
    return df[df["n_wells"] > 0].reset_index(drop=True)


def stage2(s1, dims, all_lines=False, min_lines=2):
    """DL over lines within each (predictor, outcome, class, TP53 group). Headline inference: Hartung-Knapp SE (se;
    variance scale floored at 1, so never narrower than DL) with t on n_lines - 1 df (t, p); DL normal SE and p are
    kept as se_DL, p_DL."""
    tp = np.full(len(s1), 2) if all_lines else s1["tp"].to_numpy()
    d3 = dims[:3] + (3,)
    dec, r, inv = meta_by([s1["pred"], s1["out"], s1["cls"], tp], d3, s1["est"], s1["se"])
    df = pd.DataFrame(dict(pred=dec[0], out=dec[1], cls=dec[2], tp=dec[3]))
    df = pd.concat([df, r.rename(columns={"k": "n_lines"})], axis=1)
    df["n_groups"] = np.bincount(inv, s1["n_wells"].to_numpy(), len(df)).astype(int)
    df["median_line_log_rr"] = pd.Series(s1["est"].to_numpy()).groupby(inv).median().reindex(range(len(df))).to_numpy()
    df = df.rename(columns={"se": "se_DL"}).rename(columns={"se_hk": "se"})
    df.loc[df["n_lines"] < min_lines, ["est", "se", "se_DL"]] = np.nan
    df["df"] = (df["n_lines"] - 1).clip(lower=1)
    df["t"] = df["est"] / df["se"]
    df["p"] = 2 * stats.t.sf(np.abs(df["t"]), df["df"])
    df["p_DL"] = 2 * stats.norm.sf(np.abs(df["est"] / df["se_DL"]))
    return df


def perm_diff(b, se, is_wt, n_perm, rng):
    """Observed WT-minus-altered difference of the DL means over lines and its TP53-label permutation p."""
    b, se, is_wt = np.asarray(b, float), np.asarray(se, float), np.asarray(is_wt, bool)
    ok = np.isfinite(b) & np.isfinite(se) & (se > 0)
    b, se, is_wt = b[ok], se[ok], is_wt[ok]
    L, nw = len(b), int(is_wt.sum())
    if nw < 2 or L - nw < 2:
        return np.nan, np.nan
    Mw = np.zeros((n_perm + 1, L), bool)
    Mw[0] = is_wt
    pick = np.argsort(rng.random((n_perm, L)), axis=1)[:, :nw]
    Mw[np.repeat(np.arange(1, n_perm + 1), nw), pick.ravel()] = True
    w = 1 / se ** 2

    def dlm(Mb):
        Mf = Mb.astype(float)
        k = Mf.sum(1)
        sw = Mf @ w
        fe = (Mf @ (w * b)) / sw
        Q = (Mf * w[None] * (b[None] - fe[:, None]) ** 2).sum(1)
        c = sw - (Mf @ w ** 2) / sw
        tau2 = np.where(c > 0, np.maximum(0, (Q - (k - 1)) / c), 0)
        ws = Mf / (se[None] ** 2 + tau2[:, None])
        return (ws @ b) / ws.sum(1)

    d = dlm(Mw) - dlm(~Mw)
    return d[0], (1 + np.sum(np.abs(d[1:]) >= abs(d[0]) - 1e-12)) / (n_perm + 1)


def implied_ratio(alpha, mbar):
    """Gamma-Poisson: E[true rate | y >= 1] / E[true rate | y = 0] at mean count mbar and overdispersion alpha."""
    a = np.maximum(np.asarray(alpha, float), 1e-6)
    mbar = np.asarray(mbar, float)
    p0 = (1 + a * mbar) ** (-1 / a)
    e0 = mbar / (1 + a * mbar)
    with np.errstate(invalid="ignore", divide="ignore"):
        e1 = (mbar - p0 * e0) / (1 - p0)
        return e1 / e0


def welch_df(s1, df1, s0, df0):
    """Welch-Satterthwaite df of a difference of two estimates with SEs s1, s0 on df1, df0 df."""
    a, b = np.asarray(s1, float) ** 2, np.asarray(s0, float) ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a + b) ** 2 / (a ** 2 / np.asarray(df1, float) + b ** 2 / np.asarray(df0, float))


def wt_minus_alt(S2):
    """WT (tp 0) minus altered (tp 1) per (predictor, outcome, class): difference of the stage-2 means; headline SE =
    sqrt(sum of the two Hartung-Knapp SEs squared), t on Welch-Satterthwaite df; DL normal SE / p kept as *_DL."""
    k = ["pred", "out", "cls"]
    w = S2[S2["tp"] == 0].set_index(k)
    a = S2[S2["tp"] == 1].set_index(k)
    idx = w.index.intersection(a.index)
    C = pd.DataFrame(index=idx)
    C["log_rr_WT"], C["se_WT"], C["n_lines_WT"] = w.loc[idx, "est"], w.loc[idx, "se"], w.loc[idx, "n_lines"]
    C["log_rr_altered"], C["se_altered"], C["n_lines_altered"] = a.loc[idx, "est"], a.loc[idx, "se"], a.loc[idx,
                                                                                                           "n_lines"]
    C["se_WT_DL"], C["se_altered_DL"] = w.loc[idx, "se_DL"], a.loc[idx, "se_DL"]
    C["diff"] = C["log_rr_WT"] - C["log_rr_altered"]
    C["se_diff"] = np.sqrt(C["se_WT"] ** 2 + C["se_altered"] ** 2)
    C["df_diff"] = welch_df(C["se_WT"], w.loc[idx, "df"], C["se_altered"], a.loc[idx, "df"])
    C["t"] = C["diff"] / C["se_diff"]
    C["p"] = 2 * stats.t.sf(np.abs(C["t"]), C["df_diff"])
    C["se_diff_DL"] = np.sqrt(C["se_WT_DL"] ** 2 + C["se_altered_DL"] ** 2)
    C["p_DL"] = 2 * stats.norm.sf(np.abs(C["diff"] / C["se_diff_DL"]))
    return C.reset_index()


def dl_fast(b, v):
    """DerSimonian-Laird estimate and SE of one set of estimates b with variances v (no pandas)."""
    w = 1 / v
    sw = w.sum()
    fe = (w * b).sum() / sw
    Q = (w * (b - fe) ** 2).sum()
    c = sw - (w ** 2).sum() / sw
    tau2 = max(0.0, (Q - (len(b) - 1)) / c) if c > 0 else 0.0
    ws = 1 / (v + tau2)
    return (ws * b).sum() / ws.sum(), np.sqrt(1 / ws.sum())


def paired_perm(samp, line, b, se, tp_line, n_perm, rng):
    """Within-well WT-minus-altered contrast: per well, inverse-variance means of the WT and the altered groups, their
    difference, DL over wells; permutation p from reshuffling the TP53 labels of the lines (n_perm 0: none)."""
    us, si_ = np.unique(samp, return_inverse=True)
    ul, li_ = np.unique(line, return_inverse=True)
    lab = tp_line[ul]
    okl = lab >= 0
    w = 1 / se ** 2
    nS = len(us)

    def stat(is_wt_line):
        key = si_ * 2 + is_wt_line[li_].astype(int)
        sw = np.bincount(key, w, 2 * nS)
        swb = np.bincount(key, w * b, 2 * nS)
        both = (sw[0::2] > 0) & (sw[1::2] > 0)
        if both.sum() < 2:
            return np.nan, np.nan, 0
        d = swb[1::2][both] / sw[1::2][both] - swb[0::2][both] / sw[0::2][both]
        v = 1 / sw[1::2][both] + 1 / sw[0::2][both]
        est, se_ = dl_fast(d, v)
        return est, se_, int(both.sum())

    obs = stat(lab == 0)
    if not np.isfinite(obs[0]):
        return None
    pval = np.nan
    if n_perm > 0:
        nw = int((lab[okl] == 0).sum())
        idx = np.where(okl)[0]
        ex = 0
        for _ in range(n_perm):
            perm = np.zeros(len(ul), bool)
            perm[rng.choice(idx, nw, replace=False)] = True
            dd = stat(perm)[0]
            ex += np.isfinite(dd) and abs(dd) >= abs(obs[0]) - 1e-12
        pval = (1 + ex) / (n_perm + 1)
    return obs[2], obs[0], obs[1], pval


def metareg(b, v, X):
    """Random-effects meta-regression of line estimates b (variances v) on one covariate plus an intercept, for each
    row of X (rows = the observed covariate or permutations of it). Residual tau2 by the method of moments
    (DerSimonian-Laird type); slope SE Hartung-Knapp (variance scale floored at 1, t on k - 2 df) and DL (normal).
    Returns slope, se_hk, se_dl, tau2 (arrays over the rows of X)."""
    X = np.atleast_2d(np.asarray(X, float))
    b, v = np.asarray(b, float), np.asarray(v, float)
    k = len(b)
    w = 1 / v
    Sw, Swb = w.sum(), (w * b).sum()
    Swx, Swxx, Swxb = X @ w, (X ** 2) @ w, X @ (w * b)
    det = Sw * Swxx - Swx ** 2
    b1 = (Sw * Swxb - Swx * Swb) / det
    b0 = (Swb - b1 * Swx) / Sw
    QE = (w[None] * (b[None] - b0[:, None] - b1[:, None] * X) ** 2).sum(1)
    w2 = w ** 2
    tr = (Swxx * w2.sum() - 2 * Swx * (X @ w2) + Sw * ((X ** 2) @ w2)) / det
    tau2 = np.maximum(0.0, (QE - (k - 2)) / (Sw - tr))
    ws = 1 / (v[None] + tau2[:, None])
    S0, S1, S2 = ws.sum(1), (ws * X).sum(1), (ws * X ** 2).sum(1)
    T0, T1 = ws @ b, (ws * X) @ b
    d_ = S0 * S2 - S1 ** 2
    s1 = (S0 * T1 - S1 * T0) / d_
    s0 = (T0 - s1 * S1) / S0
    var1 = S0 / d_
    q = (ws * (b[None] - s0[:, None] - s1[:, None] * X) ** 2).sum(1) / max(1, k - 2)
    return s1, np.sqrt(np.maximum(1.0, q) * var1), np.sqrt(var1), tau2


def functional_status(s1, D, dims, args):
    """TP53 FUNCTIONAL status (gene panel p53_functional_status.csv) instead of the genotype, for TRIM72 and the
    placebo predictors (p53 and screen read-outs): stage-2 means of the 'responsive' and 'unresponsive' lines, their
    difference (HK SEs, Welch df; label permutation over the classified lines for TRIM72), and the slope of the line
    estimates on the continuous p53 responsiveness (meta-regression; permutation of the responsiveness over lines for
    TRIM72); TRIM72 is placed among the placebo predictors (percentile, empirical p)."""
    lines = D["lines"]
    fc = lines["functional_call"].astype(str).to_numpy()
    resp = lines["p53_responsiveness_log2"].to_numpy(float)
    fg = np.where(fc == "responsive", 0, np.where(fc == "unresponsive", 1, -1))
    if (fg == 0).sum() < 2 or (fg == 1).sum() < 2:
        return pd.DataFrame()
    outs, preds = D["outcomes"], D["preds"]
    npl = D["n_plac"]
    k2i = [outs.index(o) for o in K2_OUT]
    base = s1[(s1["pred"] <= npl) & s1["out"].isin(k2i)]
    sf = base[fg[base["line"].to_numpy()] >= 0].copy()
    sf["tp"] = fg[sf["line"].to_numpy()]
    S2f = stage2(sf, dims)
    Cf = wt_minus_alt(S2f)
    rng = np.random.default_rng(args.seed + 13)
    nperm = min(args.perm, 10000)
    rows = []
    lab = {0: "responsive", 1: "unresponsive"}
    for r in S2f.itertuples(index=False):
        rows.append(dict(pred=r.pred, out=r.out, cls=r.cls, contrast=lab[r.tp], n_lines=r.n_lines, n_lines_2=np.nan,
                         est=r.est, se=r.se, df=r.df, p=r.p, se_DL=r.se_DL, p_DL=r.p_DL))
    grp = {k: h for k, h in sf.groupby(["pred", "out", "cls"])}
    for r in Cf.itertuples(index=False):
        pp = np.nan
        if r.pred == 0 and args.perm > 0:
            h = grp[(r.pred, r.out, r.cls)]
            pp = perm_diff(h["est"], h["se"], h["tp"] == 0, nperm, rng)[1]
        rows.append(dict(pred=r.pred, out=r.out, cls=r.cls, contrast="responsive minus unresponsive",
                         n_lines=r.n_lines_WT, n_lines_2=r.n_lines_altered, est=r.diff, se=r.se_diff, df=r.df_diff,
                         p=r.p, se_DL=r.se_diff_DL, p_DL=r.p_DL, p_perm=pp))
    # continuous responsiveness: meta-regression over all lines with a responsiveness value
    okl = np.isfinite(resp)
    sc = base[okl[base["line"].to_numpy()] & np.isfinite(base["est"]) & (base["se"] > 0)]
    nperm_s = min(args.perm, 2000)
    for (pi, oi, ci), h in sc.groupby(["pred", "out", "cls"]):
        if len(h) < 6:
            continue
        b, v, x = h["est"].to_numpy(float), h["se"].to_numpy(float) ** 2, resp[h["line"].to_numpy()]
        sl, se_hk, se_dl, _ = metareg(b, v, x)
        dfr = len(h) - 2
        pp = np.nan
        if pi == 0 and args.perm > 0:
            Xp = x[np.argsort(rng.random((nperm_s, len(x))), axis=1)]
            sp = metareg(b, v, Xp)[0]
            pp = (1 + np.sum(np.abs(sp) >= abs(sl[0]) - 1e-12)) / (nperm_s + 1)
        rows.append(dict(pred=pi, out=oi, cls=ci, contrast="slope per log2 unit of p53 responsiveness",
                         n_lines=len(h), n_lines_2=np.nan, est=sl[0], se=se_hk[0], df=dfr,
                         p=2 * stats.t.sf(abs(sl[0] / se_hk[0]), dfr), se_DL=se_dl[0],
                         p_DL=2 * stats.norm.sf(abs(sl[0] / se_dl[0])), p_perm=pp))
    FS = pd.DataFrame(rows)
    FS["predictor"] = np.asarray(preds)[FS["pred"].to_numpy()]
    FS["role"] = np.where(FS["pred"] == 0, "TRIM72", "placebo predictor")
    FS["outcome"] = np.asarray(outs)[FS["out"].to_numpy()]
    FS["outcome_type"] = FS["outcome"].map(D["otype"])
    FS["class"] = np.asarray(CLASSES)[FS["cls"].to_numpy()]
    tq = stats.t.ppf(0.975, FS["df"])
    FS["ci_lo"], FS["ci_hi"] = FS["est"] - tq * FS["se"], FS["est"] + tq * FS["se"]
    # TRIM72 against the placebo predictors (same outcome, class, contrast)
    for c_ in ("placebo_median", "placebo_sd", "n_placebos", "TRIM72_percentile_among_placebos",
               "placebo_empirical_p"):
        FS[c_] = np.nan
    for _, h in FS.groupby(["out", "cls", "contrast"]):
        t = h[h["pred"] == 0]
        pl = h.loc[(h["pred"] > 0) & np.isfinite(h["est"]), "est"].to_numpy()
        if t.empty or len(pl) < 3 or not np.isfinite(t["est"].iloc[0]):
            continue
        e, med = t["est"].iloc[0], np.median(pl)
        FS.loc[t.index, ["placebo_median", "placebo_sd", "n_placebos", "TRIM72_percentile_among_placebos",
                         "placebo_empirical_p"]] = [med, np.std(pl, ddof=1), len(pl), 100 * np.mean(pl < e),
                                                    (1 + np.sum(np.abs(pl - med) >= abs(e - med))) / (len(pl) + 1)]
    co = {c: i for i, c in enumerate(["responsive", "unresponsive", "responsive minus unresponsive",
                                      "slope per log2 unit of p53 responsiveness"])}
    FS["_c"] = FS["contrast"].map(co)
    FS = FS.sort_values(["pred", "out", "cls", "_c"]).reset_index(drop=True)
    return FS[["predictor", "role", "outcome", "outcome_type", "class", "contrast", "n_lines", "n_lines_2", "est", "se",
               "df", "ci_lo", "ci_hi", "p", "p_perm", "se_DL", "p_DL", "placebo_median", "placebo_sd", "n_placebos",
               "TRIM72_percentile_among_placebos", "placebo_empirical_p"]]


def run_meta(D, G, F, args, G0=None, F0=None):
    t0 = time.time()
    g = D["groups"]
    outs, preds = D["outcomes"], D["preds"]
    nP, nO, nC, nL = len(preds), len(outs), len(CLASSES), len(D["lines"])
    dims = (nP, nO, nC, nL)
    tp_line = np.where(D["lines"]["tp53_group"].to_numpy() == "WT", 0,
                       np.where(D["lines"]["tp53_group"].to_numpy() == "altered", 1, -1))
    cls_g = g["well_class"].map({c: i for i, c in enumerate(CLASSES)}).to_numpy()
    line_g = g["l_idx"].to_numpy()
    samp_g = g["s_idx"].to_numpy()
    ok = np.isfinite(F["beta"].to_numpy()) & np.isfinite(F["se"].to_numpy()) & (F["se"].to_numpy() > 0)
    gid = F["gid"].to_numpy()[ok]
    R = dict(pred=F["pred"].to_numpy()[ok].astype(np.int64), out=F["outcome"].to_numpy()[ok].astype(np.int64),
             cls=cls_g[gid], line=line_g[gid], samp=samp_g[gid], gid=gid,
             b=F["beta"].to_numpy()[ok].astype(float), se=F["se"].to_numpy()[ok].astype(float))
    R["tp"] = tp_line[R["line"]]
    allm = np.ones(len(gid), bool)
    s1 = pd.concat([stage1(R, allm, dims, tp_line), stage1(R, allm, dims, tp_line, cls_value=CLASSES.index(
        "all wells"))], ignore_index=True)
    S2 = pd.concat([stage2(s1, dims), stage2(s1, dims, all_lines=True)], ignore_index=True)
    log(f"  meta stages 1/2: {len(s1):,} line rows, {len(S2):,} pooled rows ({time.time() - t0:.0f} s)")
    C = wt_minus_alt(S2)
    # permutation p (TRIM72; p53 and screen outcomes)
    rng = np.random.default_rng(args.seed + 7)
    perm_out = list(dict.fromkeys(PRIMARY_OUT + P53_MEMBERS + SCREEN_OUT))
    perm_oi = [outs.index(o) for o in perm_out]
    prim_oi = [outs.index(o) for o in PRIMARY_OUT + ["ATF3", "PMAIP1"] + list(SCORES)]
    C["p_perm"] = np.nan
    s1t = s1[s1["pred"] == 0]
    grp = {k: v for k, v in s1t.groupby(["out", "cls"])}
    if args.perm > 0:
        for i in C.index[(C["pred"] == 0) & C["out"].isin(perm_oi)]:
            h = grp.get((C.at[i, "out"], C.at[i, "cls"]))
            if h is not None:
                C.at[i, "p_perm"] = perm_diff(h["est"], h["se"], h["tp"] == 0, args.perm, rng)[1]
    log(f"  WT minus altered with {args.perm} permutations ({time.time() - t0:.0f} s)")
    # within-well paired check (TRIM72; p53 and screen outcomes): per well, inverse-variance mean of the WT groups
    # minus that of the altered groups, DL over wells; p by permuting the TP53 labels of the lines
    m = (R["pred"] == 0) & np.isin(R["out"], perm_oi)
    rows_pw = []
    rng_pw = np.random.default_rng(args.seed + 11)
    for oi in perm_oi:
        mo = m & (R["out"] == oi)
        for ci, cname in enumerate(CLASSES):
            mc = mo if cname == "all wells" else mo & (R["cls"] == ci)
            if mc.sum() < 10:
                continue
            res_ = paired_perm(R["samp"][mc], R["line"][mc], R["b"][mc], R["se"][mc], tp_line,
                               args.perm_paired if oi in prim_oi else 0, rng_pw)
            if res_ is not None:
                rows_pw.append(dict(pred=0, out=oi, cls=ci, paired_n_wells=res_[0], paired_diff=res_[1],
                                    paired_se=res_[2], paired_p_perm=res_[3]))
    PWt = pd.DataFrame(rows_pw)
    C = C.merge(PWt, on=["pred", "out", "cls"], how="left")
    log(f"  within-well paired check ({time.time() - t0:.0f} s)")
    # names
    for df in (s1, S2, C):
        df["predictor"] = np.asarray(preds)[df["pred"].to_numpy()]
        df["outcome_name"] = np.asarray(outs)[df["out"].to_numpy()]
        df["outcome_type"] = df["outcome_name"].map(D["otype"])
        df["class"] = np.asarray(CLASSES)[df["cls"].to_numpy()]
    for df in (s1, S2):
        df["tp53_group"] = np.asarray(TPN)[df["tp"].to_numpy()]
    s1["cell_line_id"] = D["lines"]["cell_line_id"].to_numpy()[s1["line"].to_numpy()]

    # ---------------------------------------------------------------- placebo predictors
    npl = D["n_plac"]
    k2 = S2[S2["outcome_name"].isin(K2_OUT) & (S2["pred"] <= npl)].copy()
    PP = k2.rename(columns={"tp53_group": "contrast"})[["predictor", "outcome_name", "class", "contrast", "n_lines",
                                                        "n_groups", "est", "se", "df", "p", "se_DL", "p_DL"]]
    Cd = C[C["outcome_name"].isin(K2_OUT) & (C["pred"] <= npl)][
        ["predictor", "outcome_name", "class", "n_lines_WT", "diff", "se_diff", "df_diff", "p", "se_diff_DL", "p_DL"]
    ].rename(columns={"diff": "est", "se_diff": "se", "df_diff": "df", "se_diff_DL": "se_DL", "n_lines_WT": "n_lines"})
    Cd["contrast"] = "WT minus altered"
    Cd["n_groups"] = np.nan
    PP = pd.concat([PP, Cd], ignore_index=True)
    PP["is_TRIM72"] = PP["predictor"] == GENE
    PP["program"] = PP["predictor"].map(lambda x: "TRIM72" if x == GENE else program_of(x))
    PP["stress_program"] = PP["predictor"].isin(STRESS_PROGRAM)
    PP["detection_rate"] = PP["predictor"].map(D["rate"])
    PP = ci_cols(PP, "est", "se", dfcol="df")
    nullp = []
    for (o, cl, ct), h in PP.groupby(["outcome_name", "class", "contrast"]):
        t = h[h["is_TRIM72"]]
        if t.empty or not np.isfinite(t["est"].iloc[0]):
            continue
        t = t.iloc[0]
        for lab_, pl in (("all placebos", h[~h["is_TRIM72"]]),
                         ("non-stress placebos", h[~h["is_TRIM72"] & ~h["stress_program"]])):
            pl = pl[np.isfinite(pl["est"])]
            v = pl["est"].to_numpy()
            if len(v) < 3:
                continue
            med, sd = np.median(v), np.std(v, ddof=1)
            nullp.append(dict(outcome=o, outcome_type=D["otype"][o], **{"class": cl}, contrast=ct, placebos=lab_,
                              n_placebos=len(v), TRIM72_log_rr=t["est"], TRIM72_se=t["se"], TRIM72_p=t["p"],
                              placebo_median=med, placebo_sd=sd, placebo_min=v.min(), placebo_max=v.max(),
                              placebo_n_p_lt_005=int((pl["p"] < 0.05).sum()),
                              TRIM72_minus_placebo_median=t["est"] - med,
                              TRIM72_percentile_among_placebos=100 * np.mean(v < t["est"]),
                              empirical_p=(1 + np.sum(np.abs(v - med) >= abs(t["est"] - med))) / (len(v) + 1),
                              placebo_calibrated_z=(t["est"] - med) / np.sqrt(t["se"] ** 2 + sd ** 2),
                              placebo_calibrated_p=2 * stats.norm.sf(abs(t["est"] - med) /
                                                                     np.sqrt(t["se"] ** 2 + sd ** 2))))
    NP = pd.DataFrame(nullp)

    # ---------------------------------------------------------------- placebo outcomes (TRIM72 predictor)
    po = set(D["placebo_out"])
    test_out = PRIMARY_OUT + SCREEN_OUT
    nullo = []
    St = S2[S2["predictor"] == GENE]
    Ct = C[C["predictor"] == GENE]
    for cl in CLASSES:
        for ct in ("WT", "altered", "all lines", "WT minus altered"):
            if ct == "WT minus altered":
                h = Ct[Ct["class"] == cl].rename(columns={"diff": "est", "se_diff": "se"})
            else:
                h = St[(St["class"] == cl) & (St["tp53_group"] == ct)]
            hp = h[h["outcome_name"].isin(po)].dropna(subset=["est", "se"])
            if len(hp) < 5:
                continue
            v = hp["est"].to_numpy()
            tv = (hp["est"] / hp["se"]).to_numpy()
            med, sd = np.median(v), np.std(v, ddof=1)
            for o in test_out:
                r = h[h["outcome_name"] == o]
                if r.empty or not np.isfinite(r["est"].iloc[0]):
                    continue
                e, s_ = r["est"].iloc[0], r["se"].iloc[0]
                nullo.append(dict(outcome=o, outcome_type=D["otype"][o], **{"class": cl}, contrast=ct, log_rr=e,
                                  se=s_, n_placebo_outcomes=len(v), placebo_outcome_median=med, placebo_outcome_sd=sd,
                                  placebo_outcome_min=v.min(), placebo_outcome_max=v.max(),
                                  minus_placebo_outcome_median=e - med,
                                  percentile_among_placebo_outcomes=100 * np.mean(v < e),
                                  empirical_p=(1 + np.sum(np.abs(v - med) >= abs(e - med))) / (len(v) + 1),
                                  t=e / s_, percentile_of_t=100 * np.mean(tv < e / s_),
                                  placebo_outcomes_p_lt_005=int((hp["p"] < 0.05).sum())))
    NO = pd.DataFrame(nullo)
    log(f"  placebo nulls ({time.time() - t0:.0f} s)")

    # ---------------------------------------------------------------- per doubling of the cell's TRIM72
    gg = g.merge(G, left_index=True, right_on="gid", how="inner")
    gg = gg[gg["fitted"].astype(bool)].copy()
    k0 = outs.index("P53_SCORE")
    fp = F[(F["pred"] == 0) & (F["outcome"] == k0)][["gid", "se"]].astype({"se": float})
    gg = gg.merge(fp.rename(columns={"se": "se_p53"}), on="gid", how="left")
    gg2 = pd.concat([gg, gg.assign(well_class="all wells")], ignore_index=True)
    gg2 = pd.concat([gg2, gg2.assign(tp53_group="all lines")], ignore_index=True)
    alph = []
    for (cl, tp), h in gg2.groupby(["well_class", "tp53_group"]):
        a = h["alpha_num"].sum() / h["alpha_den"].sum()
        w = 1 / h["se_p53"].to_numpy() ** 2
        d = dict(**{"class": cl}, tp53_group=tp, n_groups=len(h), alpha_TRIM72_pooled=a,
                 median_mean_TRIM72_per_cell=h["mbar"].median())
        for suf, fac in (("", 1.0), ("_half_alpha", 0.5)):    # half alpha: half of the overdispersion is technical
            Rr = implied_ratio(a * fac, h["mbar"].to_numpy())
            dl2 = np.log2(Rr)
            okw = np.isfinite(w) & np.isfinite(dl2)
            d["median_implied_ratio" + suf] = np.nanmedian(Rr)
            d["weighted_log2_ratio" + suf] = np.sum(w[okw] * dl2[okw]) / np.sum(w[okw]) if okw.any() else np.nan
        alph.append(d)
    AL = pd.DataFrame(alph)
    gg = gg.merge(AL[["class", "tp53_group", "alpha_TRIM72_pooled"]].rename(columns={"class": "well_class"}),
                  on=["well_class", "tp53_group"], how="left")
    gg["implied_true_ratio_det_vs_not"] = implied_ratio(gg["alpha_TRIM72_pooled"], gg["mbar"])
    pdb = []
    al_ix = AL.set_index(["class", "tp53_group"])
    for scen, col, fac in (("alpha as estimated", "weighted_log2_ratio", 1.0),
                           ("half of alpha technical", "weighted_log2_ratio_half_alpha", 0.5)):
        for o in PRIMARY_OUT + ["ATF3", "PMAIP1", "NFKB_SCORE", "FERROPTOSIS_SCORE", "APOPTOSIS_SCORE", "SLC7A11"]:
            for cl in CLASSES:
                r = {}
                for tp in ("WT", "altered"):
                    h = St[(St["outcome_name"] == o) & (St["class"] == cl) & (St["tp53_group"] == tp)]
                    if h.empty or (cl, tp) not in al_ix.index:
                        continue
                    dlt = al_ix.loc[(cl, tp), col]
                    e, s_, sdl, dfv = h["est"].iloc[0], h["se"].iloc[0], h["se_DL"].iloc[0], h["df"].iloc[0]
                    r[tp] = (e, s_, sdl, dfv, dlt)
                    pdb.append(dict(outcome=o, **{"class": cl}, alpha_scenario=scen, contrast=tp, log_rr=e, se=s_,
                                    df=dfv, alpha_TRIM72=al_ix.loc[(cl, tp), "alpha_TRIM72_pooled"] * fac,
                                    log2_true_ratio=dlt, per_doubling_log_rr=e / dlt, per_doubling_se=s_ / dlt,
                                    per_doubling_se_DL=sdl / dlt))
                if len(r) == 2:
                    (e1, s1_, l1_, f1, d1), (e0, s0_, l0_, f0, d0) = r["WT"], r["altered"]
                    pdb.append(dict(outcome=o, **{"class": cl}, alpha_scenario=scen, contrast="WT minus altered",
                                    log_rr=e1 - e0, se=np.hypot(s1_, s0_), df=welch_df(s1_ / d1, f1, s0_ / d0, f0),
                                    alpha_TRIM72=np.nan, log2_true_ratio=np.nan,
                                    per_doubling_log_rr=e1 / d1 - e0 / d0, per_doubling_se=np.hypot(s1_ / d1, s0_ / d0),
                                    per_doubling_se_DL=np.hypot(l1_ / d1, l0_ / d0)))
    PD = pd.DataFrame(pdb)
    tq = stats.t.ppf(0.975, PD["df"])
    PD["per_doubling_rr"] = np.exp(PD["per_doubling_log_rr"])
    PD["per_doubling_ci_lo"] = np.exp(PD["per_doubling_log_rr"] - tq * PD["per_doubling_se"])
    PD["per_doubling_ci_hi"] = np.exp(PD["per_doubling_log_rr"] + tq * PD["per_doubling_se"])
    PD["largest_change_not_excluded_pct"] = 100 * np.maximum(1 - PD["per_doubling_ci_lo"],
                                                             PD["per_doubling_ci_hi"] - 1)
    PD["mde80_per_doubling_pct"] = 100 * (np.exp((tq + stats.t.ppf(0.80, PD["df"])) * PD["per_doubling_se"]) - 1)
    PD["p"] = 2 * stats.t.sf(np.abs(PD["per_doubling_log_rr"] / PD["per_doubling_se"]), PD["df"])
    PD["per_doubling_ci_lo_DL"] = np.exp(PD["per_doubling_log_rr"] - 1.96 * PD["per_doubling_se_DL"])
    PD["per_doubling_ci_hi_DL"] = np.exp(PD["per_doubling_log_rr"] + 1.96 * PD["per_doubling_se_DL"])

    # ---------------------------------------------------------------- sensitivity subsets (primary outcomes)
    sens_oi = [outs.index(o) for o in PRIMARY_OUT + ["ATF3", "PMAIP1"]]

    def r_sel(Rx, msk):
        return {k: v[msk] for k, v in Rx.items()}

    def r_cat(*parts):
        return {k: np.concatenate([p_[k] for p_ in parts]) for k in parts[0]}

    def subset_rows(Rx, sname):
        """WT / altered / WT-minus-altered of TRIM72 in the fits Rx (all classes pooled), with the same contrast
        for the placebo predictors (not the ambient controls) as its null."""
        if not (Rx["pred"] == 0).any():
            return []
        a1 = stage1(Rx, np.ones(len(Rx["pred"]), bool), dims, tp_line, cls_value=0)
        a2 = stage2(a1, dims)
        Cs = wt_minus_alt(a2)
        nwell = len(np.unique(Rx["samp"][Rx["pred"] == 0]))
        out_rows = []
        for oi in sens_oi:
            t = Cs[(Cs["pred"] == 0) & (Cs["out"] == oi)]
            if t.empty or not np.isfinite(t["diff"].iloc[0]):
                continue
            t = t.iloc[0]
            pl = Cs[(Cs["pred"] >= 1) & (Cs["pred"] <= npl) & (Cs["out"] == oi)]["diff"].dropna().to_numpy()
            l1 = a1[(a1["pred"] == 0) & (a1["out"] == oi)]
            pp = perm_diff(l1["est"], l1["se"], l1["tp"] == 0, min(args.perm, 2000), rng)[1] if args.perm else np.nan
            h2 = a2[(a2["pred"] == 0) & (a2["out"] == oi)]
            p_w = h2.loc[h2["tp"] == 0, "p"]
            p_a = h2.loc[h2["tp"] == 1, "p"]
            med = np.median(pl) if len(pl) >= 3 else np.nan
            out_rows.append(dict(subset=sname, outcome=outs[oi], n_wells=nwell, n_lines_WT=t["n_lines_WT"],
                                 n_lines_altered=t["n_lines_altered"],
                                 n_groups=int(h2["n_groups"].sum()), rr_WT=np.exp(t["log_rr_WT"]),
                                 log_rr_WT=t["log_rr_WT"], se_WT=t["se_WT"], p_WT=p_w.iloc[0] if len(p_w) else np.nan,
                                 rr_altered=np.exp(t["log_rr_altered"]), log_rr_altered=t["log_rr_altered"],
                                 se_altered=t["se_altered"], p_altered=p_a.iloc[0] if len(p_a) else np.nan,
                                 diff=t["diff"], se_diff=t["se_diff"], df_diff=t["df_diff"], p_diff=t["p"], p_perm=pp,
                                 se_diff_DL=t["se_diff_DL"], p_diff_DL=t["p_DL"],
                                 n_placebos=len(pl), placebo_diff_median=med,
                                 placebo_diff_sd=np.std(pl, ddof=1) if len(pl) >= 3 else np.nan,
                                 TRIM72_percentile_among_placebos=100 * np.mean(pl < t["diff"]) if len(pl) else np.nan,
                                 placebo_empirical_p=(1 + np.sum(np.abs(pl - med) >= abs(t["diff"] - med))) /
                                 (len(pl) + 1) if len(pl) >= 3 else np.nan))
        return out_rows

    plate_g = g["plate"].to_numpy()[R["gid"]]
    sub_g = g["well_subclass"].to_numpy()[R["gid"]]
    drug_g = g["drug"].astype(str).to_numpy()[R["gid"]]
    conc_g = g["conc"].astype(float).to_numpy()[R["gid"]]
    base = np.isin(R["out"], sens_oi) & (R["pred"] <= npl)          # TRIM72 and the placebo predictors
    hi = np.isin(plate_g, list(HIGH_TRIM72_PLATES))
    subsets = {"all wells, excluding plate13": plate_g != "plate13",
               "all wells, high-TRIM72 plates (1-3, 14)": hi,
               "all wells, low-TRIM72 plates (4-13)": ~hi,
               "TRIM72 raisers that activate p53": sub_g == "TRIM72 raiser, p53 activated",
               "TRIM72 raisers that do not activate p53": sub_g == "TRIM72 raiser, p53 not activated",
               "idarubicin 5 uM (2 wells; D1 wells)": (np.char.startswith(drug_g.astype(str), "Idarubicin")
                                                       & (conc_g == 5.0))}
    srows = []
    for sname, msk in subsets.items():
        srows += subset_rows(r_sel(R, base & msk), sname)
    # cap-0 sample: the groups the 2,000-cell cap dropped, refitted with all their cells (random sample of them)
    cap0_info = {}
    if F0 is not None and len(F0) and G0 is not None and len(G0):
        NG = len(g)
        fit_main = np.zeros(NG, bool)
        fit_main[G.loc[G["fitted"].astype(bool), "gid"].to_numpy()] = True
        f0 = G0.loc[G0["fitted"].astype(bool), "gid"].to_numpy() - NG
        ok0 = np.isfinite(F0["beta"].to_numpy()) & np.isfinite(F0["se"].to_numpy()) & (F0["se"].to_numpy() > 0)
        gid0 = F0["gid"].to_numpy()[ok0] - NG
        R0 = dict(pred=F0["pred"].to_numpy()[ok0].astype(np.int64), out=F0["outcome"].to_numpy()[ok0].astype(np.int64),
                  cls=cls_g[gid0], line=line_g[gid0], samp=samp_g[gid0], gid=gid0,
                  b=F0["beta"].to_numpy()[ok0].astype(float), se=F0["se"].to_numpy()[ok0].astype(float))
        R0["tp"] = tp_line[R0["line"]]
        R0 = r_sel(R0, np.isin(R0["out"], sens_oi) & (R0["pred"] <= npl) & np.isin(R0["gid"], f0))
        Rb = r_sel(R, base)
        sampled = g["cap0_sampled"].to_numpy()
        dropped0 = ~fit_main[R0["gid"]]                      # cap-0 fits of groups the cap dropped
        both_ids = f0[fit_main[f0]]
        seen = D.get("seen_group")
        dropped = g["qualifies"].to_numpy() & ~fit_main & ((seen > 0) if seen is not None else True)
        cap0_info = dict(at_risk=int(g["cap0_at_risk"].sum()), sampled=int(sampled.sum()),
                         sampled_dropped=int((sampled & dropped).sum()),
                         sampled_dropped_fitted=int((~fit_main[f0]).sum()),
                         sampled_fitted_both=int(len(both_ids)), dropped_total=int(dropped.sum()),
                         dropped_not_at_risk=int((dropped & ~g["cap0_at_risk"].to_numpy()).sum()))
        srows += subset_rows(r_cat(Rb, r_sel(R0, dropped0)),
                             "cap 0: all fitted groups + the sampled cap-dropped groups (all cells)")
        srows += subset_rows(r_sel(R0, dropped0), "cap 0: the sampled cap-dropped groups alone (all cells)")
        srows += subset_rows(r_cat(r_sel(Rb, ~sampled[Rb["gid"]]), R0),
                             "cap 0 for every sampled at-risk group (all cells; replaces its cap-2,000 fit)")
        srows += subset_rows(r_sel(R0, np.isin(R0["gid"], both_ids)),
                             "cap 0: sampled at-risk groups fitted at both caps (all cells)")
        srows += subset_rows(r_sel(Rb, np.isin(Rb["gid"], both_ids)),
                             "cap 2,000: the same sampled at-risk groups (subsample)")
    SS = pd.DataFrame(srows)
    log(f"  sensitivity subsets incl. cap 0 ({time.time() - t0:.0f} s)")

    # ---------------------------------------------------------------- ambient negative controls
    arows = []
    for x in D["amb_preds"]:
        pa = preds.index(x)
        lin = np.isin(D["lines"]["cell_line_id"].to_numpy()[R["line"]], list(D["amb_lines"][x]))
        ma = lin & ((R["pred"] <= npl) | (R["pred"] == pa)) & np.isin(R["out"], [outs.index(o) for o in K2_OUT])
        if not (ma & (R["pred"] == pa)).any():
            continue
        a1 = pd.concat([stage1(R, ma, dims, tp_line), stage1(R, ma, dims, tp_line, cls_value=CLASSES.index(
            "all wells"))], ignore_index=True)
        a2 = pd.concat([stage2(a1, dims), stage2(a1, dims, all_lines=True)], ignore_index=True)
        Ca = wt_minus_alt(a2).rename(columns={"diff": "est", "se_diff": "se", "n_lines_WT": "n_lines"})
        Ca["tp"] = 3
        A = pd.concat([a2[["pred", "out", "cls", "tp", "n_lines", "est", "se", "p"]],
                       Ca[["pred", "out", "cls", "tp", "n_lines", "n_lines_altered", "est", "se", "p"]]],
                      ignore_index=True)
        for (oi, ci, tpi), h in A.groupby(["out", "cls", "tp"]):
            ra, rt = h[h["pred"] == pa], h[h["pred"] == 0]
            pl = h.loc[(h["pred"] >= 1) & (h["pred"] <= npl), "est"].dropna().to_numpy()
            if ra.empty or not np.isfinite(ra["est"].iloc[0]):
                continue
            ea = ra["est"].iloc[0]
            et = rt["est"].iloc[0] if len(rt) else np.nan
            med = np.median(pl) if len(pl) >= 3 else np.nan
            emp = (lambda e: (1 + np.sum(np.abs(pl - med) >= abs(e - med))) / (len(pl) + 1)
                   if len(pl) >= 3 and np.isfinite(e) else np.nan)
            arows.append(dict(control=f"{x} detected, {AMBIENT[x]} lines", ambient_gene=x, outcome=outs[oi],
                              outcome_type=D["otype"][outs[oi]], **{"class": CLASSES[ci]},
                              contrast=(TPN + ["WT minus altered"])[tpi], n_lines=ra["n_lines"].iloc[0],
                              n_lines_altered=ra["n_lines_altered"].iloc[0] if tpi == 3 else np.nan,
                              ambient_log_rr=ea, ambient_se=ra["se"].iloc[0], ambient_p=ra["p"].iloc[0],
                              TRIM72_log_rr=et, TRIM72_se=rt["se"].iloc[0] if len(rt) else np.nan,
                              TRIM72_p=rt["p"].iloc[0] if len(rt) else np.nan, n_placebos=len(pl),
                              placebo_median=med, placebo_min=pl.min() if len(pl) else np.nan,
                              placebo_max=pl.max() if len(pl) else np.nan,
                              ambient_percentile_among_placebos=100 * np.mean(pl < ea) if len(pl) else np.nan,
                              ambient_placebo_empirical_p=emp(ea),
                              TRIM72_percentile_among_placebos=100 * np.mean(pl < et) if len(pl) and np.isfinite(et)
                              else np.nan, TRIM72_placebo_empirical_p=emp(et),
                              ambient_detection_rate=D["amb_rate"].get(x, np.nan),
                              TRIM72_detection_rate_same_lines=D["amb_rate"].get(x + " (TRIM72)", np.nan)))
    AMB = pd.DataFrame(arows)
    if len(AMB):
        AMB["_o"] = AMB["outcome"].map({o: i for i, o in enumerate(K2_OUT)})
        AMB["_c"] = AMB["class"].map({c: i for i, c in enumerate(CLASSES)})
        AMB["_t"] = AMB["contrast"].map({c: i for i, c in enumerate(TPN + ["WT minus altered"])})
        AMB = AMB.sort_values(["ambient_gene", "_o", "_c", "_t"]).drop(columns=["_o", "_c", "_t"])
    log(f"  ambient negative controls ({time.time() - t0:.0f} s)")

    # ---------------------------------------------------------------- TP53 functional status as the grouping
    FS = functional_status(s1, D, dims, args)
    log(f"  TP53 functional-status grouping ({time.time() - t0:.0f} s)")

    # per-group fits of TRIM72 x p53 / screen outcomes, with labels
    keep = (F["pred"].to_numpy() == 0) & np.isin(F["outcome"].to_numpy(), perm_oi)
    Fg = F[keep].copy()
    gi = Fg["gid"].to_numpy()
    for c in ("sample", "plate", "well_class", "cell_line_id", "tp53_group"):
        Fg[c] = g[c].to_numpy()[gi]
    Fg["outcome_name"] = np.asarray(outs)[Fg["outcome"].to_numpy()]
    Fg = Fg.sort_values(["sample", "cell_line_id", "outcome_name"], kind="mergesort").reset_index(drop=True)
    log(f"  per-doubling bounds, subsets, controls ({time.time() - t0:.0f} s)")
    return dict(Fg=Fg, s1=s1, S2=S2, C=C, PP=PP, NP=NP, NO=NO, AL=AL, PD=PD, SS=SS, gg=gg, FS=FS, AMB=AMB,
                cap0_info=cap0_info)


# ============================================================================= tables
def ci_cols(df, est="est", se="se", prefix="", dfcol=None):
    """rate ratio and 95% CI; t quantile on the dfcol column when given (Hartung-Knapp), else normal."""
    q = stats.t.ppf(0.975, df[dfcol]) if dfcol is not None else 1.96
    df[prefix + "rate_ratio"] = np.exp(df[est])
    df[prefix + "ci_lo"] = np.exp(df[est] - q * df[se])
    df[prefix + "ci_hi"] = np.exp(df[est] + q * df[se])
    return df


def write_tables(D, M, G, info, checks_rows, args, tab, t_start):
    g = D["groups"]
    S2, C = M["S2"], M["C"]
    # 1. groups
    gg = g.merge(G, left_index=True, right_on="gid", how="left")
    gg = gg.merge(M["gg"][["gid", "alpha_TRIM72_pooled", "implied_true_ratio_det_vs_not"]], on="gid", how="left")
    gout = gg[["sample", "plate", "well", "drug", "conc", "well_class", "well_subclass", "cell_line_id", "cell_name",
               "tp53_group", "n_cells", f"det_{GENE}", "keep_prob", "n_used", "n_det", "fitted", "skip_reason",
               "mbar", "alpha_num", "alpha_den", "alpha_TRIM72_pooled", "implied_true_ratio_det_vs_not",
               "cap0_at_risk", "cap0_sampled"]].rename(
        columns={"n_cells": "n_cells_total", f"det_{GENE}": "n_TRIM72_detected_total", "keep_prob": "sampling_prob",
                 "n_used": "n_cells_used", "n_det": "n_TRIM72_detected_used",
                 "mbar": "mean_expected_TRIM72_per_cell", "alpha_num": "nb_moment_numerator",
                 "alpha_den": "nb_moment_denominator", "alpha_TRIM72_pooled": "alpha_TRIM72_pooled_class_tp53"})
    gout["fitted"] = gout["fitted"].eq(True)
    gout.loc[gout["skip_reason"].eq("") & ~gout["fitted"], "skip_reason"] = "too few detected cells after sampling"
    gout.to_csv(os.path.join(tab, "groups.csv.gz"), index=False, float_format="%.6g", compression=GZ)
    # 2. class summary
    fit = gout[gout["fitted"]]
    cs = []
    for cl in CLASSES:
        h0 = fit if cl == "all wells" else fit[fit["well_class"] == cl]
        for tp in ("WT", "altered", "all lines"):
            h = h0 if tp == "all lines" else h0[h0["tp53_group"] == tp]
            if h.empty:
                continue
            a = M["AL"]
            ar = a[(a["class"] == cl) & (a["tp53_group"] == tp)]
            gv = (lambda c_: ar[c_].iloc[0] if len(ar) else np.nan)
            cs.append(dict(**{"class": cl}, tp53_group=tp, n_wells=h["sample"].nunique(),
                           n_lines=h["cell_line_id"].nunique(), n_groups=len(h),
                           n_cells_total=int(h["n_cells_total"].sum()), n_cells_used=int(h["n_cells_used"].sum()),
                           n_TRIM72_detected_used=int(h["n_TRIM72_detected_used"].sum()),
                           pct_TRIM72_detected=100 * h["n_TRIM72_detected_used"].sum() / h["n_cells_used"].sum(),
                           alpha_TRIM72_pooled=gv("alpha_TRIM72_pooled"),
                           median_implied_true_ratio=gv("median_implied_ratio"),
                           weighted_log2_true_ratio=gv("weighted_log2_ratio"),
                           median_implied_true_ratio_half_alpha=gv("median_implied_ratio_half_alpha"),
                           weighted_log2_true_ratio_half_alpha=gv("weighted_log2_ratio_half_alpha")))
    pd.DataFrame(cs).to_csv(os.path.join(tab, "class_summary.csv"), index=False, float_format="%.6g")
    # 3. TRIM72 meta by TP53 group (all outcomes)
    T = S2[S2["predictor"] == GENE].copy().rename(columns={"outcome_name": "outcome", "est": "log_rr",
                                                           "tau2": "tau2_lines", "I2": "I2_lines",
                                                           "n_pos": "n_lines_positive", "hk_q": "hk_scale"})
    T = ci_cols(T, "log_rr", "se", dfcol="df")
    T["ci_lo_DL"] = np.exp(T["log_rr"] - 1.96 * T["se_DL"])
    T["ci_hi_DL"] = np.exp(T["log_rr"] + 1.96 * T["se_DL"])
    T["family"] = np.where(T["outcome_type"].str.startswith("placebo"), "placebo outcomes", "p53 + screen")
    T["q_bh"] = np.nan
    for fam, h in T.groupby("family"):
        T.loc[h.index, "q_bh"] = bh(h["p"].to_numpy())
    T["module"] = T["outcome"].map(SCREEN_MODULE_OF).fillna("")
    order = {o: i for i, o in enumerate(D["outcomes"])}
    T["_o"] = T["outcome"].map(order)
    T["_c"] = T["class"].map({c: i for i, c in enumerate(CLASSES)})
    T = T.sort_values(["_o", "_c", "tp53_group"]).drop(columns=["_o", "_c", "predictor"])
    T[["outcome", "outcome_type", "module", "class", "tp53_group", "n_lines", "n_groups", "rate_ratio", "ci_lo",
       "ci_hi", "log_rr", "se", "df", "t", "p", "q_bh", "family", "se_DL", "ci_lo_DL", "ci_hi_DL", "p_DL", "hk_scale",
       "tau2_lines", "I2_lines", "n_lines_positive", "median_line_log_rr"]].to_csv(
        os.path.join(tab, "trim72_meta_by_tp53_group.csv"), index=False, float_format="%.6g")
    # 4. WT minus altered (TRIM72)
    Ct = C[C["predictor"] == GENE].copy().rename(columns={"outcome_name": "outcome"})
    tq = stats.t.ppf(0.975, Ct["df_diff"])
    Ct["ratio_of_rate_ratios"] = np.exp(Ct["diff"])
    Ct["ci_lo"] = np.exp(Ct["diff"] - tq * Ct["se_diff"])
    Ct["ci_hi"] = np.exp(Ct["diff"] + tq * Ct["se_diff"])
    Ct["ci_lo_DL"] = np.exp(Ct["diff"] - 1.96 * Ct["se_diff_DL"])
    Ct["ci_hi_DL"] = np.exp(Ct["diff"] + 1.96 * Ct["se_diff_DL"])
    Ct["family"] = np.where(Ct["outcome_type"].str.startswith("placebo"), "placebo outcomes", "p53 + screen")
    Ct["p_used"] = Ct["p_perm"].fillna(Ct["p"])
    Ct["q_bh"] = np.nan
    for fam, h in Ct.groupby("family"):
        Ct.loc[h.index, "q_bh"] = bh(h["p_used"].to_numpy())
    Ct["module"] = Ct["outcome"].map(SCREEN_MODULE_OF).fillna("")
    Ct["_o"] = Ct["outcome"].map(order)
    Ct["_c"] = Ct["class"].map({c: i for i, c in enumerate(CLASSES)})
    Ct = Ct.sort_values(["_o", "_c"])
    Ct[["outcome", "outcome_type", "module", "class", "n_lines_WT", "n_lines_altered", "log_rr_WT", "se_WT",
        "log_rr_altered", "se_altered", "diff", "se_diff", "df_diff", "ratio_of_rate_ratios", "ci_lo", "ci_hi", "t",
        "p", "p_perm", "q_bh", "family", "se_diff_DL", "ci_lo_DL", "ci_hi_DL", "p_DL", "paired_n_wells",
        "paired_diff", "paired_se", "paired_p_perm"]].to_csv(
        os.path.join(tab, "trim72_WT_minus_altered.csv"), index=False, float_format="%.6g")
    # 5-6. placebo predictors
    PP = M["PP"].rename(columns={"outcome_name": "outcome", "est": "log_rr"})
    PP[["predictor", "program", "stress_program", "detection_rate", "outcome", "class", "contrast", "n_lines",
        "n_groups", "rate_ratio", "ci_lo", "ci_hi", "log_rr", "se", "df", "p", "se_DL", "p_DL"]].to_csv(
        os.path.join(tab, "placebo_predictors.csv"), index=False, float_format="%.6g")
    M["NP"].to_csv(os.path.join(tab, "placebo_predictor_null.csv"), index=False, float_format="%.6g")
    # 7. placebo outcomes
    M["NO"].to_csv(os.path.join(tab, "placebo_outcome_null.csv"), index=False, float_format="%.6g")
    # 8. per doubling
    PD = M["PD"]
    PD[["outcome", "class", "alpha_scenario", "contrast", "log_rr", "se", "df", "alpha_TRIM72", "log2_true_ratio",
        "per_doubling_log_rr", "per_doubling_se", "per_doubling_rr", "per_doubling_ci_lo", "per_doubling_ci_hi",
        "largest_change_not_excluded_pct", "mde80_per_doubling_pct", "p", "per_doubling_se_DL",
        "per_doubling_ci_lo_DL", "per_doubling_ci_hi_DL"]].to_csv(
        os.path.join(tab, "per_doubling_bounds.csv"), index=False, float_format="%.6g")
    # 9. sensitivity
    M["SS"].to_csv(os.path.join(tab, "sensitivity_subsets.csv"), index=False, float_format="%.6g")
    # 10. line-level estimates (TRIM72; p53 + screen outcomes)
    s1 = M["s1"]
    L = s1[(s1["predictor"] == GENE) & s1["outcome_name"].isin(PRIMARY_OUT + SCREEN_OUT +
                                                               [o for o in P53_MEMBERS])].copy()
    L = L.rename(columns={"outcome_name": "outcome", "est": "log_rr", "tau2": "tau2_wells", "n_pos":
                          "n_wells_positive"})
    li = D["lines"].set_index("cell_line_id")
    L["cell_name"] = L["cell_line_id"].map(li["cell_name"])
    L["tp53_functional_call"] = L["cell_line_id"].map(li["functional_call"])
    L["p53_responsiveness_log2"] = L["cell_line_id"].map(li["p53_responsiveness_log2"])
    L = L[["outcome", "outcome_type", "class", "cell_line_id", "cell_name", "tp53_group", "tp53_functional_call",
           "p53_responsiveness_log2", "n_wells", "log_rr", "se", "tau2_wells", "n_wells_positive"]]
    L.to_csv(os.path.join(tab, "line_estimates.csv.gz"), index=False, float_format="%.6g", compression=GZ)
    # 11. per-group fits (TRIM72; p53 + screen outcomes), sorted by (sample, cell_line_id, outcome)
    Fg = M["Fg"]
    Fg = Fg[["sample", "plate", "well_class", "cell_line_id", "tp53_group", "outcome_name", "beta", "se", "phi",
             "unadj", "n_det_pred", "y_tot", "y_det"]].rename(
        columns={"outcome_name": "outcome", "beta": "log_rr", "phi": "dispersion", "unadj": "log_rr_unadjusted",
                 "n_det_pred": "n_TRIM72_detected", "y_tot": "outcome_counts", "y_det": "outcome_counts_detected"})
    Fg.to_csv(os.path.join(tab, "group_fits_TRIM72_p53_screen.csv.gz"), index=False, float_format="%.5g",
              compression=GZ)
    # 12. modules (citations from mg53_p53/gene_modules.csv)
    mods = []
    cite = {}
    pdf = pd.read_csv(args.modules)
    for _, r in pdf.iterrows():
        gname = str(r["gene/assay"]).split(" ")[0]
        cite[gname] = (r.get("module", ""), r.get("literature_citation", ""))
    for o in list(SCORES) + SCREEN_GENES + P53_PRIMARY + ["TP53"]:
        mem = SCORES.get(o, [o])
        mods.append(dict(outcome=o, members=";".join(mem), n_members=len(mem),
                         gene_modules_csv_module=cite.get(o, ("", ""))[0] if o not in SCORES else
                         ";".join(sorted(set(str(cite.get(x, ("", ""))[0]) for x in mem))),
                         literature_citation=cite.get(o, ("", ""))[1] if o not in SCORES else ""))
    mods.append(dict(outcome="(not testable)", members=NOT_IN_CELL_PANEL_NOTE, n_members=0,
                     gene_modules_csv_module="", literature_citation=""))
    mods.append(dict(outcome="(placebo predictors)", members=";".join(D["placebo"]), n_members=len(D["placebo"]),
                     gene_modules_csv_module="", literature_citation=""))
    mods.append(dict(outcome="(placebo outcomes)", members=";".join(D["placebo_out"]),
                     n_members=len(D["placebo_out"]), gene_modules_csv_module="", literature_citation=""))
    for x in D["amb_preds"]:
        ids = D["amb_lines"][x]
        nm = D["lines"].set_index("cell_line_id").loc[sorted(ids), "cell_name"]
        mods.append(dict(outcome=f"(ambient control: {x} detected)", members=";".join(nm), n_members=len(ids),
                         gene_modules_csv_module="", literature_citation=""))
    pd.DataFrame(mods).to_csv(os.path.join(tab, "modules_and_gene_sets.csv"), index=False)
    # 13. TP53 functional status as the grouping; ambient negative controls
    if len(M["FS"]):
        M["FS"].to_csv(os.path.join(tab, "p53_functional_status_contrasts.csv"), index=False, float_format="%.6g")
    if len(D["amb"]):
        A = D["amb"].copy()
        fitl = G.loc[G["fitted"].astype(bool), "gid"].to_numpy()
        nfit = pd.Series(g["cell_line_id"].to_numpy()[fitl]).value_counts()
        A["n_fitted_groups"] = A["cell_line_id"].map(nfit).fillna(0).astype(int)
        A["used"] = A["used"] & A["gene"].isin(D["amb_preds"])
        A.to_csv(os.path.join(tab, "ambient_control_lines.csv"), index=False, float_format="%.6g")
    if len(M["AMB"]):
        M["AMB"].to_csv(os.path.join(tab, "ambient_negative_controls.csv"), index=False, float_format="%.6g")
    # 14. checks
    pd.DataFrame(checks_rows).to_csv(os.path.join(tab, "checks.csv"), index=False)
    # 15. headline
    head = []
    hv = Ct[Ct["outcome"].isin(PRIMARY_OUT + ["ATF3", "PMAIP1", "NFKB_SCORE", "FERROPTOSIS_SCORE",
                                              "APOPTOSIS_SCORE", "SLC7A11"])]
    NPt = M["NP"]
    NOt = M["NO"]
    FS = M["FS"]
    for _, r in hv.iterrows():
        np_ = NPt[(NPt["outcome"] == r["outcome"]) & (NPt["class"] == r["class"]) &
                  (NPt["contrast"] == "WT minus altered") & (NPt["placebos"] == "all placebos")]
        no_ = NOt[(NOt["outcome"] == r["outcome"]) & (NOt["class"] == r["class"]) &
                  (NOt["contrast"] == "WT minus altered")]
        pdr = PD[(PD["outcome"] == r["outcome"]) & (PD["class"] == r["class"]) & (PD["contrast"] == "WT minus altered")]
        pd1 = pdr[pdr["alpha_scenario"] == "alpha as estimated"]
        pd2 = pdr[pdr["alpha_scenario"] == "half of alpha technical"]
        sw = S2[(S2["predictor"] == GENE) & (S2["outcome_name"] == r["outcome"]) & (S2["class"] == r["class"])]
        rw = sw[sw["tp53_group"] == "WT"]
        ra = sw[sw["tp53_group"] == "altered"]
        fs = (FS[(FS["role"] == "TRIM72") & (FS["outcome"] == r["outcome"]) & (FS["class"] == r["class"])
                 & (FS["contrast"] == "responsive minus unresponsive")] if len(FS) else pd.DataFrame())
        tq1 = stats.t.ppf(0.975, r["df_diff"])
        head.append(dict(outcome=r["outcome"], **{"class": r["class"]}, n_lines_WT=r["n_lines_WT"],
                         n_lines_altered=r["n_lines_altered"],
                         rr_WT=np.exp(r["log_rr_WT"]), p_WT=rw["p"].iloc[0] if len(rw) else np.nan,
                         rr_altered=np.exp(r["log_rr_altered"]), p_altered=ra["p"].iloc[0] if len(ra) else np.nan,
                         WT_minus_altered_log_rr=r["diff"], ci_lo_log=r["diff"] - tq1 * r["se_diff"],
                         ci_hi_log=r["diff"] + tq1 * r["se_diff"], df=r["df_diff"], p=r["p"], p_perm=r["p_perm"],
                         q_bh=r["q_bh"], ci_lo_log_DL=r["diff"] - 1.96 * r["se_diff_DL"],
                         ci_hi_log_DL=r["diff"] + 1.96 * r["se_diff_DL"], p_DL=r["p_DL"],
                         paired_within_well_diff=r["paired_diff"], paired_p_perm=r["paired_p_perm"],
                         placebo_predictor_percentile=np_["TRIM72_percentile_among_placebos"].iloc[0]
                         if len(np_) else np.nan,
                         placebo_predictor_empirical_p=np_["empirical_p"].iloc[0] if len(np_) else np.nan,
                         placebo_outcome_percentile=no_["percentile_among_placebo_outcomes"].iloc[0]
                         if len(no_) else np.nan,
                         placebo_outcome_empirical_p=no_["empirical_p"].iloc[0] if len(no_) else np.nan,
                         per_doubling_diff_ci_lo=pd1["per_doubling_ci_lo"].iloc[0] if len(pd1) else np.nan,
                         per_doubling_diff_ci_hi=pd1["per_doubling_ci_hi"].iloc[0] if len(pd1) else np.nan,
                         per_doubling_diff_ci_lo_half_alpha=pd2["per_doubling_ci_lo"].iloc[0] if len(pd2) else np.nan,
                         per_doubling_diff_ci_hi_half_alpha=pd2["per_doubling_ci_hi"].iloc[0] if len(pd2) else np.nan,
                         functional_resp_minus_unresp=fs["est"].iloc[0] if len(fs) else np.nan,
                         functional_p_perm=fs["p_perm"].iloc[0] if len(fs) else np.nan,
                         functional_placebo_percentile=fs["TRIM72_percentile_among_placebos"].iloc[0]
                         if len(fs) else np.nan,
                         functional_placebo_empirical_p=fs["placebo_empirical_p"].iloc[0] if len(fs) else np.nan))
    H = pd.DataFrame(head)
    H.to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.6g")
    amb_txt = "; ".join(f"{x}: " + ", ".join(sorted(D["lines"].set_index("cell_line_id").loc[sorted(D["amb_lines"][x]),
                                                                                              "cell_name"]))
                        for x in D["amb_preds"]) or "none"
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        if D["adjust"]:
            fh.write(f"SENSITIVITY RUN: every model also adjusts for log((count + 0.5) / total UMI) of "
                     f"{', '.join(D['adjust'])}; outcomes that contain these genes are not fitted.\n\n")
        fh.write(README_TABLES.format(cap=args.max_cells_per_group, min_cells=args.min_cells, min_det=args.min_det,
                                      minc=args.min_outcome_counts, mine=args.min_expected_det,
                                      rr=args.placebo_range, perm=args.perm, placebos=", ".join(D["placebo"]),
                                      n_po=len(D["placebo_out"]), seed=args.seed, perm_paired=args.perm_paired,
                                      n_plac=len(D["placebo"]), n_plac1=len(D["placebo"]) + 1,
                                      amb_lines=amb_txt, amb_ratio=args.ambient_max_ratio,
                                      cap0_frac=args.cap0_frac))
    return H


README_TABLES = """Tables of single_cell_all.py (D1b at full scale; re-created by: python3 single_cell_all.py). ASSOCIATIONS ONLY:
Tahoe has no MG53 perturbation and measures mRNA, so 'TRIM72-detected cells carry X% more p53-target mRNA' says nothing
causal about MG53 -> p53, and p53 activity is read from its target genes' mRNA. The TP53 genotype is the control: an MG53
-> p53 effect can only act where p53 works, so the PRIMARY ESTIMAND is the TRIM72 log rate ratio in TP53-WT lines minus
that in TP53-altered lines ('WT minus altered'); what is equal in both groups is not via p53.

Model, per (well, cell line) group: quasi-Poisson GLM (IRLS, log link, dispersion = Pearson chi2/df floored at 1) of an
outcome's per-cell counts on 'predictor gene detected (>= 1 UMI)' + log(total UMI) + log S-phase fraction + log G2M
fraction (fractions = (module counts + 0.5) / total UMI), offset log(total UMI); same model as downstream_p53.py (d).
Groups: >= {min_cells} cells, >= {min_det} TRIM72-detected and >= {min_det} undetected cells, line expresses TRIM72 (atlas
expr_mask), TP53 group known, not a failed well. Cells: a uniform random subsample of at most {cap} cells per group (0 =
all; Bernoulli, seed {seed} per file). A fit (predictor x outcome x group) needs outcome counts >= {minc}, expected outcome
counts in the predictor-detected cells >= {mine} and a gene outcome expressed in the line; fits where the outcome is
entirely in one arm (separation) or that did not converge are dropped (checks.csv counts them).
Meta-analysis: two-stage DerSimonian-Laird (DL) random effects: stage 1 over the wells of a (line, well class), stage 2
over lines within a TP53 group (17 WT / 33 altered lines annotated; 17 / 30 have fitted groups: NCI-H661 does not express
TRIM72, NCI-H2122 and NCI-H596 have too few TRIM72-detected cells; lines are the units because the same lines repeat in
every well). STAGE-2 INFERENCE (headline): Hartung-Knapp (HK) SE of the DL mean, se = sqrt(max(1, q) / sum w*) with q =
sum w* (b - mean)^2 / (k - 1) (hk_scale = q; the floor at 1 keeps it never narrower than DL), and t on k - 1 df (k =
lines). 'WT minus altered' = difference of the two stage-2 means, se = sqrt(se_WT^2 + se_altered^2) (HK), t on the
Welch-Satterthwaite df (df_diff). CIs use these t quantiles. The DL normal SE / CI / p of the earlier version are kept as
se_DL, ci_lo_DL, ci_hi_DL, p_DL (narrower; secondary). Stage-1 (wells within a line) stays DL normal. p_perm = TP53-label
permutation over lines ({perm} permutations; the line-level estimates are fixed and the WT / altered split of the lines
with data is reshuffled; unaffected by the HK change). 'paired' = per well, inverse-variance mean of the WT groups minus
that of the altered groups, then DL over wells (compares lines only within the same well, so drug and well effects
cancel); its p (paired_p_perm) comes from reshuffling the TP53 labels of the lines ({perm_paired} permutations; scores,
primary outcomes, ATF3, PMAIP1), because a normal p over wells would treat the same lines in every well as independent.
All p-values are two-sided. Placebo-based empirical p-values cannot go below 1 / (n placebos + 1) (1/{n_plac1} with {n_plac}
placebos).
Well classes: DMSO; 'TRIM72 raisers' = drug-doses with the gene panel's TRIM72 call 'up' (21); 'p53 activators' =
P53_ACTIVITY z >= 3 and FDR < 0.10 and not a raiser; 'other drugs' = the rest; 'all wells' = all of them.
Outcomes: P53_SCORE = counts of the 21 P53_ACTIVITY members summed; P53_PRIMARY5 = MDM2+CDKN1A+FDXR+ZMAT3+DDB2 summed;
NFKB_SCORE = NFKBIA+TNFAIP3+CXCL8 (gene_modules.csv NF-kB), NFKB8_SCORE = the gene panel's 8 NF-kB targets;
FERROPTOSIS_SCORE = SLC7A11+GPX4+CHAC1; APOPTOSIS_SCORE = BAX+BBC3+PMAIP1; single genes as named. The p53 outcomes are 24
unique read-outs (P53_SCORE, P53_PRIMARY5, TP53 and the 21 score members). Placebo outcomes: the {n_po} non-p53-linked,
non-screen panel genes (modules_and_gene_sets.csv). Placebo predictors (detection rate within 1/{rr}x-{rr}x of TRIM72's in
the fitted groups, not p53-linked, not a screen gene): {placebos}.
Ambient negative controls (predictors fitted only in their lines, same model, same groups): 'CDKN2A detected' in the
CDKN2A-deleted lines and 'MTAP detected' in the MTAP-null lines (gene panel p53_functional_status.csv flags) whose reads of
that gene are < {amb_ratio} x the ambient expectation (ambient_control_lines.csv): {amb_lines}. Every such read is soup
or cross-contamination, so these show what pure ambient capture does to the outcomes.
Cap-0 sample: groups with a binomial probability > 1e-6 of falling below {min_det} TRIM72-detected (or undetected) cells
under the cap are 'at risk'; a random {cap0_frac} of them (seeded) is also fitted with all its cells in the same pass. The
groups the cap actually dropped among them are a simple random sample of all cap-dropped groups.
Effect sizes: log_rr = natural-log rate ratio (detected vs undetected cells); rate_ratio = exp(log_rr); CIs are 95%.

groups.csv.gz              one row per (well, line) in well_line.parquet: class, TP53 group, cells total / used, TRIM72-
                           detected cells, sampling probability, fitted (= TRIM72 fittable after the subsample; only
                           these groups enter the main tables) or skip_reason, NB moment sums of TRIM72 counts
                           (numerator sum((y-m)^2-y), denominator sum(m^2), m = depth x group rate), pooled alpha, the
                           implied true-rate ratio of detected vs undetected cells, cap0_at_risk / cap0_sampled.
class_summary.csv          per well class x TP53 group: wells, lines, groups, cells, TRIM72-detected cells, pooled
                           alpha, implied true-rate ratio (median; and its log2 weighted by the P53_SCORE fits' 1/se^2),
                           also with half of alpha taken as technical (*_half_alpha).
trim72_meta_by_tp53_group.csv  TRIM72 predictor, every outcome x class x TP53 group (WT, altered, all lines): stage-2
                           rate ratio, HK CI (t, df), t, p, q_bh (BH within family: 'p53 + screen' or 'placebo
                           outcomes'; on the HK p), DL se / CI / p, hk_scale, tau2 and I2 between lines, lines with a
                           positive estimate, median line estimate.
trim72_WT_minus_altered.csv    TRIM72: WT minus altered per outcome x class: both stage-2 estimates (HK SEs), difference,
                           se_diff (HK), df_diff, ratio of rate ratios with HK CI, t, p, p_perm, q_bh (BH within family
                           on p_perm where computed, else the HK p), DL se / CI / p, and the within-well paired check.
placebo_predictors.csv     every predictor (TRIM72 and the placebos) x p53/screen outcome x class x contrast (WT,
                           altered, all lines, WT minus altered): estimate, HK CI, se, df, p, DL se / p, detection rate,
                           program.
placebo_predictor_null.csv TRIM72 against the placebo-predictor distribution per outcome x class x contrast (all
                           placebos; non-stress placebos): placebo median / sd / range, placebos with HK p < 0.05,
                           TRIM72 percentile, empirical p = (1 + #placebos at least as far from the placebo median) /
                           (n + 1), calibrated z = (TRIM72 - placebo median) / sqrt(se^2 + placebo sd^2) (se = HK).
placebo_outcome_null.csv   TRIM72 predictor: each p53 / screen outcome against the distribution over the placebo
                           outcomes (same class x contrast): percentile, empirical p, t (= estimate / HK se) and its
                           percentile among the placebo outcomes' t, placebo outcomes with HK p < 0.05.
per_doubling_bounds.csv    what the test can exclude per doubling of a cell's TRIM72: log_rr / log2_true_ratio, where
                           log2_true_ratio = log2 of the implied true TRIM72 rate in detected vs undetected cells
                           (gamma-Poisson with the pooled alpha, at each group's mean count; averaged with the P53_SCORE
                           fits' 1/se^2 weights). alpha_scenario 'alpha as estimated' (headline) or 'half of alpha
                           technical' (alpha halved: smaller true-rate contrast, wider bounds). per_doubling_ci_lo/hi:
                           95% CI of the rate ratio per doubling from the HK SE and t (df; Welch for WT minus altered);
                           *_DL = the earlier normal DL bounds (narrower). largest_change_not_excluded_pct = largest change
                           per doubling inside the CI; mde80 = change per doubling detectable with 80% power ((t_0.975 +
                           t_0.80) x SE). For WT minus altered, each group is scaled by its own ratio. Even the
                           as-estimated alpha may include technical overdispersion not explained by depth, which would
                           overstate the true-rate contrast and make these bounds too tight.
sensitivity_subsets.csv    primary outcomes, WT / altered / difference (HK p and permutation p, 2,000 perms; DL se / p
                           kept) in: plate 13 left out; high-TRIM72 plates (1-3, 14) vs low (4-13) [TRIM72 untreated ~10x
                           lower on 4-13]; raisers that activate p53 and raisers that do NOT activate p53; the two
                           idarubicin 5 uM wells (D1's wells); and the CAP-0 rows: all fitted groups plus the sampled
                           cap-dropped groups refitted with all cells; those dropped groups alone; every sampled at-risk
                           group at cap 0 (replacing its cap-2,000 fit); the sampled groups fitted at both caps, at cap 0
                           and at cap 2,000. Not pre-specified: read with the placebo columns (the same WT-minus-altered
                           difference for the placebo predictors in the same fits: median, sd, TRIM72 percentile,
                           empirical p).
p53_functional_status_contrasts.csv  TP53 FUNCTIONAL status (gene panel call; 'uncertain' and unmeasured lines left out
                           of the binary contrast) instead of the genotype, for TRIM72 and every placebo predictor, p53 and
                           screen read-outs x class: stage-2 'responsive' and 'unresponsive' means (HK), 'responsive minus
                           unresponsive' (HK se, Welch df; p_perm = permutation of the functional labels over the
                           classified lines, TRIM72 only), and the 'slope per log2 unit of p53 responsiveness' over all
                           lines with a value (random-effects meta-regression, method-of-moments residual tau2, HK se on
                           k - 2 df; p_perm = 2,000 permutations of the responsiveness over lines, TRIM72 only). est is a
                           log rate ratio (or its slope); ci_lo / ci_hi on that log scale. TRIM72 rows carry the placebo
                           median / sd and TRIM72's percentile and empirical p among the placebo predictors.
ambient_negative_controls.csv  per ambient control (CDKN2A in CDKN2A-deleted lines, MTAP in MTAP-null lines) x p53/screen
                           outcome x class x contrast (WT, altered, all lines, WT minus altered), in those lines only: the
                           ambient gene's log rate ratio (HK se, p), TRIM72's in the same lines, the placebo predictors'
                           median / range there, and both genes' percentile and empirical p among the placebos; detection
                           rates of the ambient gene and of TRIM72 in those lines.
ambient_control_lines.csv  every CDKN2A-deleted / MTAP-null flagged line: its reads of the gene per million UMI, the
                           ambient expectation (soup = the other lines of the same wells pooled), their ratio, used,
                           fitted groups.
line_estimates.csv.gz      stage-1 per line x class (TRIM72; p53 and screen outcomes): estimate, SE, wells, tau2, TP53
                           genotype group, functional call and p53 responsiveness.
group_fits_TRIM72_p53_screen.csv.gz  per-group fits (TRIM72; p53 and screen outcomes), sorted by sample, line, outcome:
                           log_rr, SE, dispersion, unadjusted log rate ratio, TRIM72-detected cells, outcome counts.
modules_and_gene_sets.csv  outcome definitions with the mg53_p53/gene_modules.csv modules and citations (formerly
                           mg53_p53/gene_modules.csv); placebo gene lists; ambient-control lines; modules of
                           gene_modules.csv that the per-cell panel lacks.
key_results.csv            headline rows: p53 primary outcomes and screen modules, WT minus altered per class, with the HK
                           CI (ci_lo_log / ci_hi_log, df, p) and the DL ones (*_DL), the permutation p, the paired check,
                           both placebo nulls, the per-doubling CI (alpha as estimated; and with half of alpha technical)
                           and the functional-status contrast (responsive minus unresponsive: estimate, p_perm, placebo
                           percentile, empirical p).
checks.csv                 bookkeeping and agreement checks: cells read, coverage (groups / plates read completely, plates
                           fitted before all their cells were read, cells read after their plate was fitted: both 0 on a
                           full run), IRLS vs scalar GLM, dropped fits, gene lists, gene_modules.csv genes, TP53 genotype x
                           functional call, ambient lines, cap-0 sample, D1 comparison.
"""


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--modules", default=MODULES_CSV,
                    help="gene modules table (default mg53_p53/gene_modules.csv; formerly "
                         "mg53_p53/gene_modules.csv)")
    ap.add_argument("--max-cells-per-group", type=int, default=2000,
                    help="uniform subsample per (well, line); 0 = all cells (default 2000: 47M of the 60M cells "
                         "in qualifying groups, 87%% of their TRIM72-detected cells)")
    ap.add_argument("--cap0-frac", type=float, default=0.2,
                    help="fraction of the groups the cap could drop (binomial risk > 1e-6) that are also fitted with "
                         "all their cells (cap-0 sensitivity; 0 = off)")
    ap.add_argument("--ambient-max-ratio", type=float, default=0.3,
                    help="a CDKN2A-deleted / MTAP-null line is an ambient control only if its reads of the gene are "
                         "below this multiple of the ambient expectation")
    ap.add_argument("--min-cells", type=int, default=50)
    ap.add_argument("--min-det", type=int, default=5, help="TRIM72-detected (and undetected) cells per group")
    ap.add_argument("--min-outcome-counts", type=int, default=20)
    ap.add_argument("--min-expected-det", type=float, default=5.0,
                    help="expected outcome counts in the predictor-detected cells")
    ap.add_argument("--placebo-range", type=float, default=3.0)
    ap.add_argument("--workers", type=int, default=3, help="fitting processes (0 = in the main process)")
    ap.add_argument("--readers", type=int, default=2, help="parquet reading threads")
    ap.add_argument("--chunk-cells", type=int, default=60000)
    ap.add_argument("--perm", type=int, default=10000)
    ap.add_argument("--perm-paired", type=int, default=1000, help="permutations of the within-well paired check")
    ap.add_argument("--adjust", default="", help="sensitivity: extra per-cell covariates, log((gene + 0.5) / total UMI), "
                                                 "comma list of panel genes (e.g. ATF3); outcomes containing them are "
                                                 "skipped. Use a separate MG53_OUT.")
    ap.add_argument("--seed", type=int, default=20261025)
    ap.add_argument("--check-every", type=int, default=211, help="scalar re-fit of every n-th group id (check)")
    ap.add_argument("--stale-files", type=int, default=40)
    ap.add_argument("--limit-files", type=int, default=0, help="test runs: first N cell files only")
    ap.add_argument("--recompute", action="store_true", help="ignore the cache")
    args = ap.parse_args()
    t_start = time.time()
    try:
        import pyarrow.parquet  # noqa: F401
    except ImportError:
        sys.exit("single_cell_all.py needs pyarrow to read the parquet files (pip install pyarrow)")
    args.modules = os.path.abspath(os.path.expanduser(args.modules))
    if not os.path.exists(args.modules):
        sys.exit(f"gene modules table not found: {args.modules}\nIt is mg53_p53/gene_modules.csv (moved there from "
                 f"mg53_p53/gene_modules.csv); pass its location with --modules.")
    data, tab, cdir = resolve_paths(args)
    log(f"data {data}; tables {tab}; cache {cdir}; gene modules {args.modules}")
    sm, lines, expr, wl, panel, ga, amb = load_setup(data, args)
    D = build_design(sm, lines, expr, wl, panel, amb, args)
    D.update(sm=sm, lines=lines)
    del wl
    g = D["groups"]
    NG = len(g)
    q = g["qualifies"]
    log(f"groups: {len(g)} (well, line); {int(q.sum())} qualify ({int(g.loc[q, 'n_cells'].sum()):,} cells, "
        f"{int(g.loc[q, 'det_TRIM72'].sum()):,} TRIM72-detected); expected cells used "
        f"{int((g['n_cells'] * g['keep_prob']).sum()):,} (cap {args.max_cells_per_group}); cap-0 sample "
        f"{int(g['cap0_sampled'].sum())} of {int(g['cap0_at_risk'].sum())} at-risk groups "
        f"({int(g.loc[g['cap0_sampled'], 'n_cells'].sum()):,} cells)")
    log(f"placebo predictors ({len(D['placebo'])}): " + ", ".join(f"{x} {D['rate'][x]:.4f}" for x in D["placebo"])
        + f"; TRIM72 {D['rate'][GENE]:.4f}")
    log(f"ambient controls: " + ("; ".join(f"{x} in {len(D['amb_lines'][x])} lines (detected {D['amb_rate'][x]:.4f})"
                                          for x in D["amb_preds"]) or "none"))
    log(f"outcomes: {len(D['outcomes'])} ({len(D['placebo_out'])} placebo outcomes); cell columns {len(D['need'])}"
        + (f"; ADJUSTED for {', '.join(D['adjust'])} (sensitivity run)" if D["adjust"] else ""))
    params = dict(version=VERSION, cap=args.max_cells_per_group, min_cells=args.min_cells, min_det=args.min_det,
                  minc=args.min_outcome_counts, mine=args.min_expected_det, rr=args.placebo_range, seed=args.seed,
                  limit_files=args.limit_files, placebo=D["placebo"], outcomes=D["outcomes"], k2=K2_OUT,
                  n_files=len(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet"))),
                  data_realpath=os.path.realpath(data), total_cells=D["total_cells"], preds=D["preds"],
                  ambient_lines={x: sorted(D["amb_lines"][x]) for x in D["amb_preds"]}, cap0_frac=args.cap0_frac,
                  n_cap0=int(g["cap0_sampled"].sum()))
    if D["adjust"]:
        params["adjust"] = D["adjust"]
    pj = os.path.join(cdir, "run_info.json")
    fits_p, grp_p = os.path.join(cdir, "fits.parquet"), os.path.join(cdir, "group_stats.parquet")
    cached = False
    if not args.recompute and all(os.path.exists(p) for p in (pj, fits_p, grp_p)):
        old = json.load(open(pj, encoding="utf-8"))
        if old.get("params") == params:
            cached = True
        else:
            log("cache parameters differ (data folder, cell count, version or settings): refitting")
    checks_rows = []
    if cached:
        log("cache matches the parameters: per-group fits read from the cache (--recompute to redo)")
        F = pd.read_parquet(fits_p)
        G = pd.read_parquet(grp_p)
        info = json.load(open(pj, encoding="utf-8"))["info"]
        chk = json.load(open(pj, encoding="utf-8"))["irls_checks"]
    else:
        log(f"streaming {params['n_files'] if not args.limit_files else args.limit_files} cell files "
            f"({args.readers} readers, {args.workers} fitting workers)")
        G, F, chk, info = stream_and_fit(data, args, D, cdir)
        # deterministic order (the workers return groups in completion order)
        G = G.sort_values("gid", kind="mergesort").reset_index(drop=True)
        F = F.sort_values(["gid", "pred", "outcome"], kind="mergesort").reset_index(drop=True)
        chk = sorted(chk)
        F.to_parquet(fits_p, index=False)
        G.to_parquet(grp_p, index=False)
        info_s = {k: v for k, v in info.items()}
        with open(pj, "w", encoding="utf-8") as fh:
            json.dump(dict(params=params, info=info_s, irls_checks=chk), fh)
        log(f"streamed and fitted in {info['stream_seconds']:.0f} s: {len(G)} groups, {len(F):,} fits; "
            f"peak RSS main {rss_gb():.2f} GB, largest worker {info['children_peak_rss_gb']} GB")
    # cap-0 refits (group id + NG) go to their own frames
    G0 = G[G["gid"] >= NG].reset_index(drop=True)
    F0 = F[F["gid"] >= NG].reset_index(drop=True)
    G = G[G["gid"] < NG].reset_index(drop=True)
    F = F[F["gid"] < NG].reset_index(drop=True)
    # a group counts as fitted only if TRIM72 itself is fittable after the subsample (>= min_det detected and
    # undetected cells); placebo-predictor fits of the other groups are dropped, so that TRIM72 and the placebos
    # use the same groups
    n_any = int(G["fitted"].sum())
    for GG in (G, G0):
        GG["fitted"] = (GG["fitted"].astype(bool) & (GG["n_det"] >= args.min_det)
                        & (GG["n_used"] - GG["n_det"] >= args.min_det))
    F = F[F["gid"].isin(G.loc[G["fitted"], "gid"])].reset_index(drop=True)
    F0 = F0[F0["gid"].isin(G0.loc[G0["fitted"], "gid"])].reset_index(drop=True)
    # ------------------------------------------------------------------ checks
    seen = np.asarray(info["seen_group"])
    qq = g["qualifies"].to_numpy()
    mism = int(np.sum(seen[qq] != g.loc[qq, "n_cells"].to_numpy()))
    lim = " (--limit-files run: expected to be > 0)" if args.limit_files else ""
    checks_rows.append(dict(check="cells read (all files)", value=info["cells_read"], n=info["files_read"],
                            note="Tahoe-100M has 95,624,334 cells in 3,388 files"))
    checks_rows.append(dict(check="qualifying groups whose cells read != well_line n_cells", value=mism,
                            n=int(qq.sum()), note="0 = every qualifying group was read completely" + lim))
    badp = [p for p in info["expected_plate"] if info["seen_plate"].get(p) != info["expected_plate"][p]]
    checks_rows.append(dict(check="plates with cells read != well_line total", value=len(badp), n=14,
                            note=", ".join(badp)))
    inc = info.get("incomplete_plates")
    checks_rows.append(dict(check="plates fitted before all their cells were read (stale-flushed or at end of stream)",
                            value=len(inc) if inc is not None else np.nan, n=len(info["expected_plate"]),
                            note=(", ".join(inc) if inc else "") + " (must be 0 on a full run)" + lim))
    checks_rows.append(dict(check="cells read after their plate had been fitted (ignored)",
                            value=info.get("cells_ignored_after_flush", np.nan),
                            n=info.get("kept_cells_ignored_after_flush", np.nan),
                            note="n = of them, cells sampled for fitting; must be 0 on a full run"))
    if chk:
        ca = np.array(chk)
        checks_rows.append(dict(check="batched IRLS vs scalar GLM (downstream_p53.poisson_glm copy), TRIM72 x "
                                      "P53_SCORE: max |diff| of log_rr", value=float(np.max(np.abs(ca[:, 1] - ca[:, 2]))),
                                n=len(ca), note="every --check-every-th group id"))
        checks_rows.append(dict(check="same: max relative |diff| of SE",
                                value=float(np.max(np.abs(ca[:, 3] - ca[:, 4]) / ca[:, 4])), n=len(ca), note=""))
    fl = F["flag"].to_numpy()
    checks_rows.append(dict(check="fits dropped: separation (outcome entirely in one arm)", value=int((fl & 1).sum()),
                            n=len(F), note="mostly sparse genes; dropped before the meta-analysis"))
    checks_rows.append(dict(check="fits dropped: IRLS not converged (without separation)", value=int((fl == 2).sum()),
                            n=len(F),
                            note=f"max {MAX_ITER} iterations, tol {TOL}"))
    checks_rows.append(dict(check="groups fitted (TRIM72 fittable after the subsample) / qualifying",
                            value=int(G["fitted"].sum()), n=int(qq.sum()),
                            note=f"{n_any - int(G['fitted'].sum())} qualifying groups fell below {args.min_det} "
                                 f"TRIM72-detected cells in the subsample; their placebo fits are dropped too"))
    try:
        sys.path.insert(0, REPO)
        import tahoe_gene_panel as P
        ok = list(P.P53_ACTIVITY) == P53_MEMBERS and list(P.CONTEXT["P53_EXT"]) == P53_EXT and all(
            list(P.CONTEXT[k]) == v for k, v in CONTEXT.items())
        checks_rows.append(dict(check="gene lists equal tahoe_gene_panel (P53_ACTIVITY, P53_EXT, context modules)",
                                value=int(ok), n=1, note=""))
    except Exception as e:  # noqa: BLE001
        checks_rows.append(dict(check="gene lists vs tahoe_gene_panel", value=np.nan, n=0, note=f"not importable: {e}"))
    gm = pd.read_csv(args.modules)
    gm_genes = {str(x).split(" ")[0]: m for x, m in zip(gm["gene/assay"], gm["module"])}
    in_panel = [x for x in gm_genes if x in panel]
    used = set(PRIMARY_OUT + P53_MEMBERS + SCREEN_GENES)
    checks_rows.append(dict(check="gene_modules.csv genes in the per-cell panel / of them tested as p53 or screen "
                                  "outcomes", value=len(in_panel), n=sum(x in used for x in in_panel),
                            note=f"{args.modules}; not tested as such: " + ", ".join(
                                f"{x} ({gm_genes[x]})" for x in in_panel if x not in used)))
    fitl = np.unique(g["l_idx"].to_numpy()[G.loc[G["fitted"], "gid"].to_numpy()])
    ct = pd.crosstab(lines["tp53_group"].to_numpy()[fitl], lines["functional_call"].fillna("none").to_numpy()[fitl])
    checks_rows.append(dict(check="lines with fitted groups: TP53 genotype x functional call (gene panel)",
                            value=len(fitl), n=np.nan,
                            note="; ".join(f"{r} / {c}: {int(ct.loc[r, c])}" for r in ct.index for c in ct.columns
                                           if ct.loc[r, c] > 0)))
    for x in D["amb_preds"]:
        a_ = D["amb"][D["amb"]["gene"] == x]
        checks_rows.append(dict(check=f"ambient control {x}: flagged lines used (reads < {args.ambient_max_ratio} x "
                                      f"ambient expectation) / flagged", value=int(a_["used"].sum()), n=len(a_),
                                note="not used: " + ", ".join(f"{r.cell_name} (ratio {r.ambient_ratio:.2f})"
                                                              for r in a_[~a_["used"]].itertuples())))
    # ------------------------------------------------------------------ meta + tables
    log("meta-analysis")
    D["seen_group"] = seen
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        M = run_meta(D, G, F, args, G0=G0, F0=F0)
    ci0 = M["cap0_info"]
    if ci0:
        checks_rows.append(dict(check="cap-0 sample: at-risk groups / sampled (all cells also fitted)",
                                value=ci0["sampled"], n=ci0["at_risk"],
                                note=f"--cap0-frac {args.cap0_frac}; at risk = binomial probability > 1e-6 of < "
                                     f"{args.min_det} TRIM72-detected or undetected cells after the cap"))
        checks_rows.append(dict(check="cap-0 sample: sampled groups the cap dropped / all groups the cap dropped",
                                value=ci0["sampled_dropped"], n=ci0["dropped_total"],
                                note=f"{ci0['sampled_dropped_fitted']} of the sampled dropped groups fitted at cap 0; "
                                     f"{ci0['sampled_fitted_both']} sampled groups fitted at both caps; "
                                     f"{ci0['dropped_not_at_risk']} dropped groups were outside the at-risk set "
                                     f"(should be 0)"))
    # D1 comparison (read-only, if the downstream step's table is there)
    for cand in (os.path.join(os.path.dirname(os.environ.get("MG53_OUT") or HERE), "downstream_p53", "tables",
                              "d_single_cell_meta_main.csv"),
                 os.path.join(REPO, "mg53_p53", "downstream_p53", "tables", "d_single_cell_meta_main.csv")):
        if os.path.exists(cand):
            d1 = pd.read_csv(cand)
            d1 = d1[(d1["wellset"] == "idarubicin 5 uM, both wells") & (d1["outcome"] == "P53_SCORE")]
            ss = M["SS"]
            mine = ss[(ss["subset"].str.startswith("idarubicin 5 uM")) & (ss["outcome"] == "P53_SCORE")]
            for _, r in d1.iterrows():
                v = mine[f"rr_{r['tp53_group']}"].iloc[0] if len(mine) else np.nan
                checks_rows.append(dict(check=f"idarubicin 5 uM P53_SCORE rate ratio, {r['tp53_group']}: this step "
                                              f"(per well, then lines) vs D1 (per line, both wells in one fit)",
                                        value=float(v), n=int(r["n_lines"]),
                                        note=f"D1 {r['rate_ratio']:.4f} ({cand}); differences: per-well fits, "
                                             f"two-stage pooling, {args.max_cells_per_group}-cell subsample"))
            break
    H = write_tables(D, M, G, info, checks_rows, args, tab, t_start)
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    show = H[H["outcome"].isin(["P53_SCORE", "P53_PRIMARY5", "MDM2", "ATF3", "NFKB_SCORE"])]
    print(show[["outcome", "class", "n_lines_WT", "n_lines_altered", "rr_WT", "rr_altered", "WT_minus_altered_log_rr",
                "ci_lo_log", "ci_hi_log", "p_perm", "placebo_predictor_empirical_p", "placebo_outcome_empirical_p",
                "per_doubling_diff_ci_lo", "per_doubling_diff_ci_hi"]].round(4).to_string(index=False))
    print(pd.DataFrame(checks_rows).to_string(index=False))
    log(f"tables written to {tab}; wall {time.time() - t_start:.0f} s; peak RSS main {rss_gb():.2f} GB, largest "
        f"child {children_rss_gb():.2f} GB")


if __name__ == "__main__":
    main()
