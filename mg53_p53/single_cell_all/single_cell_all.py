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
    member, the screen modules of mg53_perturbation/assay_panel/panel.csv that the per-cell panel holds (NF-kB:
    NFKBIA/TNFAIP3/CXCL8 and the panel's 8-gene NF-kB set; ferroptosis: SLC7A11/GPX4/CHAC1; apoptosis:
    BAX/BBC3/PMAIP1; stress: ATF3, PMAIP1, DDIT3) and every non-p53 panel gene (PLACEBO OUTCOMES).
    PLACEBO PREDICTORS: 'gene X detected' for every non-p53-linked, non-screen panel gene whose detection rate in the
    fitted groups is within 1/--placebo-range x to --placebo-range x of TRIM72's, same model, outcomes = the p53 and
    screen read-outs. Their estimates are the null distribution for TRIM72's.
 3. Two-stage random effects (DerSimonian-Laird): per (line, well class) over its wells, then per TP53 group over lines
    (the 17 WT lines repeat in every well, so lines, not wells, are the units). WT minus altered: difference of the
    two line-level means (normal SE) and a TP53-label permutation over lines (--perm); a within-well paired version
    (WT groups minus altered groups of the same well, then over wells) as a check. Well classes: DMSO; drug-doses that
    raise TRIM72 (gene panel call 'up'); drug-doses that activate p53 (P53_ACTIVITY z >= 3 and FDR < 0.10, not
    raisers); all other drugs; and all wells together.
 4. What the test can exclude per doubling of a cell's TRIM72: the negative-binomial overdispersion of TRIM72 counts
    given depth (moment estimator, pooled per class and TP53 group) gives, under a gamma model, the ratio of the true
    TRIM72 rate in detected vs undetected cells; the log rate ratio CI divided by its log2 is the CI per doubling.

    python3 single_cell_all.py [--data DIR] [--max-cells-per-group 2000] [--workers 3] [--perm 10000] [--recompute]

Data folder: --data (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M), read only. Tables: $MG53_OUT/tables (default
<this folder>/tables), see README_tables.txt there; cache: $MG53_OUT/cache (per-group fits; reused when the
parameters match, so the tables can be rebuilt in ~1 min). Python: numpy, pandas, scipy (+ pyarrow to read parquet).
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import glob  # noqa: E402
import json  # noqa: E402
import multiprocessing as mp  # noqa: E402
import resource  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
import warnings  # noqa: E402
from collections import deque  # noqa: E402
from concurrent.futures import ThreadPoolExecutor  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
VERSION = 1
GENE = "TRIM72"
# the gene panel's 21-gene P53_ACTIVITY score (= tahoe_gene_panel.P53_ACTIVITY; checked at run time when importable)
P53_MEMBERS = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC",
               "PHLDA3", "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
P53_EXT = ["TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "TNFRSF10B", "PHLDA3", "SPATA18", "TRIAP1", "RPS27L", "ACER2",
           "TP53INP1", "PLK3", "POLH", "EDA2R", "CCNG1", "BTG2", "TIGAR"]               # tahoe_gene_panel CONTEXT P53_EXT
P53_PRIMARY = ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2"]     # panel.csv p53_primary (best WT-vs-altered separators)
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
# screen modules (mg53_perturbation/assay_panel/panel.csv, restricted to genes in the per-cell panel)
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
NOT_IN_CELL_PANEL_NOTE = ("panel.csv modules not in the per-cell panel (no single-cell test possible): PI3K-AKT/FAK "
                          "(TXNIP, IRS1, PTK2), cell cycle (CCND1, KIF11), RAC1, MCL1, FOS, HEXIM1, GDF15")
CLASSES = ["DMSO", "TRIM72 raisers", "p53 activators", "other drugs", "all wells"]
HIGH_TRIM72_PLATES = {"plate1", "plate2", "plate3", "plate14"}
MAX_ITER = 25
TOL = 1e-6


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def rss_gb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 2


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
            if gid % W["check_every"] == 0:                 # scalar re-fit of TRIM72 x P53_SCORE (check)
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
    ga = pd.read_csv(os.path.join(eff, "genes.csv"))
    ga = ga[ga["kind"] == "gene"].drop_duplicates("symbol").set_index("symbol")
    em = np.load(os.path.join(eff, "expr_mask.npy"), mmap_mode="r")
    wl = pd.read_parquet(os.path.join(gp, "well_line.parquet"))
    panel = [c[4:] for c in wl.columns if c.startswith("det_")]
    expr = pd.DataFrame({g: (np.asarray(em[:, int(ga.loc[g, "col"])]).astype(bool) if g in ga.index
                             else np.zeros(len(lines), bool)) for g in panel}, index=lines["cell_line_id"])
    return sm, lines, expr, wl, panel, ga


def build_design(sm, lines, expr, wl, panel, args):
    """Groups, placebo predictors, outcomes and the cell-matrix columns."""
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
    need = list(dict.fromkeys([GENE] + placebo + adjust + [x for o in outcomes for x in (SCORES.get(o, [o]))]))
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
    preds = [GENE] + placebo
    expr_pred = np.column_stack([expr[x].to_numpy() for x in preds])
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
                expr_out=expr_out, expr_pred=expr_pred, preds=preds, rate=rate, otype=otype)


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
    exp_plate = np.zeros(len(plates))
    np.add.at(exp_plate, plate_of_s[g["s_idx"].to_numpy()], g["n_cells"].to_numpy())
    kept_exp = np.zeros(len(plates))
    np.add.at(kept_exp, plate_of_s[g["s_idx"].to_numpy()], g["n_cells"].to_numpy() * keep_prob)
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
               k_p53score=D["outcomes"].index("P53_SCORE"))
    ctx = mp.get_context("spawn")
    pool = ctx.Pool(args.workers, initializer=init_worker, initargs=(cfg,)) if args.workers > 0 else None
    if pool is None:
        init_worker(cfg)
    seen_plate = np.zeros(len(plates))
    seen_group = np.zeros(len(g), np.int64)
    last_file = np.full(len(plates), -1)
    bufs, done_plates = {}, set()
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
                yield dict(gids=ug[cur], lines=lines_of[ug[cur]], offs=np.r_[0, np.cumsum(sizes)],
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
            f"{len(results_g)} groups fitted before it; {time.time() - t0:.0f} s; peak RSS {rss_gb():.2f} GB")
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
        rng = np.random.default_rng([args.seed, fi])
        u = rng.random(len(gid))
        keep = hit & (u < keep_prob[np.where(hit, gid, 0)])
        if keep.any():
            ki = np.where(keep)[0]
            T = t.column("total_counts").to_numpy()[ki].astype(np.float32)
            S = to_u16(t.column("S_PHASE").to_numpy()[ki])
            Gm = to_u16(t.column("G2M_PHASE").to_numpy()[ki])
            Y = np.empty((len(ki), len(need)), np.uint16)
            for j, x in enumerate(need):
                Y[:, j] = to_u16(t.column(x).to_numpy()[ki])
            pk = pl[ki]
            for pi in np.unique(pk):
                if pi in done_plates:
                    log(f"  WARNING: cells of {plates[pi]} after it was fitted (file {fi}); ignored")
                    continue
                m = pk == pi
                if pi not in bufs:
                    bufs[pi] = PlateBuf(kept_exp[pi] * 1.03 + 5000, len(need))
                bufs[pi].add(gid[ki][m].astype(np.int32), T[m], S[m], Gm[m], Y[m])
        del t
        for pi in list(bufs):
            if seen_plate[pi] >= exp_plate[pi]:
                flush(pi, True)
            elif fi - last_file[pi] > args.stale_files:
                log(f"  WARNING: {plates[pi]} saw {seen_plate[pi]:.0f} of {exp_plate[pi]:.0f} cells and no cells for "
                    f"{args.stale_files} files: fitted as incomplete")
                flush(pi, False)
        if (fi + 1) % 200 == 0:
            log(f"  {fi + 1}/{len(files)} files, {n_seen:,} cells, {time.time() - t0:.0f} s, peak RSS {rss_gb():.2f} GB")
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
                stream_seconds=round(time.time() - t0, 1), children_peak_rss_gb=round(
                    resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024 ** 2, 2))
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
    npos = np.bincount(key, (b > 0).astype(float), nk)
    m[k == 0] = np.nan
    s[k == 0] = np.nan
    return pd.DataFrame(dict(k=k.astype(int), est=m, se=s, tau2=tau2, I2=I2, n_pos=npos.astype(int)))


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
    """DL over lines within each (predictor, outcome, class, TP53 group)."""
    tp = np.full(len(s1), 2) if all_lines else s1["tp"].to_numpy()
    d3 = dims[:3] + (3,)
    dec, r, inv = meta_by([s1["pred"], s1["out"], s1["cls"], tp], d3, s1["est"], s1["se"])
    df = pd.DataFrame(dict(pred=dec[0], out=dec[1], cls=dec[2], tp=dec[3]))
    df = pd.concat([df, r.rename(columns={"k": "n_lines"})], axis=1)
    df["n_groups"] = np.bincount(inv, s1["n_wells"].to_numpy(), len(df)).astype(int)
    df["median_line_log_rr"] = pd.Series(s1["est"].to_numpy()).groupby(inv).median().reindex(range(len(df))).to_numpy()
    df.loc[df["n_lines"] < min_lines, ["est", "se"]] = np.nan
    df["z"] = df["est"] / df["se"]
    df["p"] = 2 * stats.norm.sf(np.abs(df["z"]))
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


def wt_minus_alt(S2):
    k = ["pred", "out", "cls"]
    w = S2[S2["tp"] == 0].set_index(k)
    a = S2[S2["tp"] == 1].set_index(k)
    idx = w.index.intersection(a.index)
    C = pd.DataFrame(index=idx)
    C["log_rr_WT"], C["se_WT"], C["n_lines_WT"] = w.loc[idx, "est"], w.loc[idx, "se"], w.loc[idx, "n_lines"]
    C["log_rr_altered"], C["se_altered"], C["n_lines_altered"] = a.loc[idx, "est"], a.loc[idx, "se"], a.loc[idx,
                                                                                                           "n_lines"]
    C["diff"] = C["log_rr_WT"] - C["log_rr_altered"]
    C["se_diff"] = np.sqrt(C["se_WT"] ** 2 + C["se_altered"] ** 2)
    C["z"] = C["diff"] / C["se_diff"]
    C["p"] = 2 * stats.norm.sf(np.abs(C["z"]))
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


def run_meta(D, G, F, args):
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
    k2 = S2[S2["outcome_name"].isin(K2_OUT)].copy()
    PP = k2.rename(columns={"tp53_group": "contrast"})[["predictor", "outcome_name", "class", "contrast", "n_lines",
                                                        "n_groups", "est", "se", "p"]]
    Cd = C[C["outcome_name"].isin(K2_OUT)][["predictor", "outcome_name", "class", "n_lines_WT", "diff", "se_diff",
                                            "p"]].rename(columns={"diff": "est", "se_diff": "se",
                                                                  "n_lines_WT": "n_lines"})
    Cd["contrast"] = "WT minus altered"
    Cd["n_groups"] = np.nan
    PP = pd.concat([PP, Cd], ignore_index=True)
    PP["is_TRIM72"] = PP["predictor"] == GENE
    PP["program"] = PP["predictor"].map(lambda x: "TRIM72" if x == GENE else program_of(x))
    PP["stress_program"] = PP["predictor"].isin(STRESS_PROGRAM)
    PP["detection_rate"] = PP["predictor"].map(D["rate"])
    PP["rate_ratio"] = np.exp(PP["est"])
    PP["ci_lo"] = np.exp(PP["est"] - 1.96 * PP["se"])
    PP["ci_hi"] = np.exp(PP["est"] + 1.96 * PP["se"])
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
            zv = (hp["est"] / hp["se"]).to_numpy()
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
                                  z=e / s_, percentile_of_z=100 * np.mean(zv < e / s_),
                                  placebo_outcomes_p_lt_005=int((2 * stats.norm.sf(np.abs(zv)) < 0.05).sum())))
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
        Rr = implied_ratio(a, h["mbar"].to_numpy())
        dl2 = np.log2(Rr)
        w = 1 / h["se_p53"].to_numpy() ** 2
        okw = np.isfinite(w) & np.isfinite(dl2)
        alph.append(dict(**{"class": cl}, tp53_group=tp, n_groups=len(h), alpha_TRIM72_pooled=a,
                         median_mean_TRIM72_per_cell=h["mbar"].median(), median_implied_ratio=np.nanmedian(Rr),
                         weighted_log2_ratio=np.sum(w[okw] * dl2[okw]) / np.sum(w[okw]) if okw.any() else np.nan))
    AL = pd.DataFrame(alph)
    gg = gg.merge(AL[["class", "tp53_group", "alpha_TRIM72_pooled"]].rename(columns={"class": "well_class"}),
                  on=["well_class", "tp53_group"], how="left")
    gg["implied_true_ratio_det_vs_not"] = implied_ratio(gg["alpha_TRIM72_pooled"], gg["mbar"])
    pdb = []
    al_ix = AL.set_index(["class", "tp53_group"])
    for o in PRIMARY_OUT + ["ATF3", "PMAIP1", "NFKB_SCORE", "FERROPTOSIS_SCORE", "APOPTOSIS_SCORE", "SLC7A11"]:
        for cl in CLASSES:
            r = {}
            for tp in ("WT", "altered"):
                h = St[(St["outcome_name"] == o) & (St["class"] == cl) & (St["tp53_group"] == tp)]
                if h.empty or (cl, tp) not in al_ix.index:
                    continue
                dlt = al_ix.loc[(cl, tp), "weighted_log2_ratio"]
                e, s_ = h["est"].iloc[0], h["se"].iloc[0]
                r[tp] = (e, s_, dlt)
                pdb.append(dict(outcome=o, **{"class": cl}, contrast=tp, log_rr=e, se=s_,
                                alpha_TRIM72=al_ix.loc[(cl, tp), "alpha_TRIM72_pooled"], log2_true_ratio=dlt,
                                per_doubling_log_rr=e / dlt, per_doubling_se=s_ / dlt))
            if len(r) == 2:
                (e1, s1_, d1), (e0, s0_, d0) = r["WT"], r["altered"]
                pdb.append(dict(outcome=o, **{"class": cl}, contrast="WT minus altered", log_rr=e1 - e0,
                                se=np.hypot(s1_, s0_), alpha_TRIM72=np.nan, log2_true_ratio=np.nan,
                                per_doubling_log_rr=e1 / d1 - e0 / d0, per_doubling_se=np.hypot(s1_ / d1, s0_ / d0)))
    PD = pd.DataFrame(pdb)
    PD["per_doubling_rr"] = np.exp(PD["per_doubling_log_rr"])
    PD["per_doubling_ci_lo"] = np.exp(PD["per_doubling_log_rr"] - 1.96 * PD["per_doubling_se"])
    PD["per_doubling_ci_hi"] = np.exp(PD["per_doubling_log_rr"] + 1.96 * PD["per_doubling_se"])
    PD["largest_change_not_excluded_pct"] = 100 * np.maximum(1 - PD["per_doubling_ci_lo"],
                                                             PD["per_doubling_ci_hi"] - 1)
    PD["mde80_per_doubling_pct"] = 100 * (np.exp(2.80 * PD["per_doubling_se"]) - 1)
    PD["p"] = 2 * stats.norm.sf(np.abs(PD["per_doubling_log_rr"] / PD["per_doubling_se"]))

    # ---------------------------------------------------------------- sensitivity subsets (primary outcomes)
    plate_g = g["plate"].to_numpy()[R["gid"]]
    sub_g = g["well_subclass"].to_numpy()[R["gid"]]
    drug_g = g["drug"].astype(str).to_numpy()[R["gid"]]
    conc_g = g["conc"].astype(float).to_numpy()[R["gid"]]
    sens_oi = [outs.index(o) for o in PRIMARY_OUT + ["ATF3", "PMAIP1"]]
    base = np.isin(R["out"], sens_oi)                       # TRIM72 and the placebo predictors
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
        mm = base & msk
        if not (mm & (R["pred"] == 0)).any():
            continue
        a1 = stage1(R, mm, dims, tp_line, cls_value=0)
        a2 = stage2(a1, dims)
        Cs = wt_minus_alt(a2)
        nwell = len(np.unique(R["samp"][mm & (R["pred"] == 0)]))
        for oi in sens_oi:
            t = Cs[(Cs["pred"] == 0) & (Cs["out"] == oi)]
            if t.empty or not np.isfinite(t["diff"].iloc[0]):
                continue
            t = t.iloc[0]
            pl = Cs[(Cs["pred"] > 0) & (Cs["out"] == oi)]["diff"].dropna().to_numpy()
            l1 = a1[(a1["pred"] == 0) & (a1["out"] == oi)]
            pp = perm_diff(l1["est"], l1["se"], l1["tp"] == 0, min(args.perm, 2000), rng)[1] if args.perm else np.nan
            h2 = a2[(a2["pred"] == 0) & (a2["out"] == oi)]
            p_w = h2.loc[h2["tp"] == 0, "p"]
            p_a = h2.loc[h2["tp"] == 1, "p"]
            med = np.median(pl) if len(pl) >= 3 else np.nan
            srows.append(dict(subset=sname, outcome=outs[oi], n_wells=nwell, n_lines_WT=t["n_lines_WT"],
                              n_lines_altered=t["n_lines_altered"],
                              n_groups=int(h2["n_groups"].sum()), rr_WT=np.exp(t["log_rr_WT"]),
                              log_rr_WT=t["log_rr_WT"], se_WT=t["se_WT"], p_WT=p_w.iloc[0] if len(p_w) else np.nan,
                              rr_altered=np.exp(t["log_rr_altered"]), log_rr_altered=t["log_rr_altered"],
                              se_altered=t["se_altered"], p_altered=p_a.iloc[0] if len(p_a) else np.nan,
                              diff=t["diff"], se_diff=t["se_diff"], p_diff=t["p"], p_perm=pp,
                              n_placebos=len(pl), placebo_diff_median=med,
                              placebo_diff_sd=np.std(pl, ddof=1) if len(pl) >= 3 else np.nan,
                              TRIM72_percentile_among_placebos=100 * np.mean(pl < t["diff"]) if len(pl) else np.nan,
                              placebo_empirical_p=(1 + np.sum(np.abs(pl - med) >= abs(t["diff"] - med))) /
                              (len(pl) + 1) if len(pl) >= 3 else np.nan))
    SS = pd.DataFrame(srows)
    # per-group fits of TRIM72 x p53 / screen outcomes, with labels
    keep = (F["pred"].to_numpy() == 0) & np.isin(F["outcome"].to_numpy(), perm_oi)
    Fg = F[keep].copy()
    gi = Fg["gid"].to_numpy()
    for c in ("sample", "plate", "well_class", "cell_line_id", "tp53_group"):
        Fg[c] = g[c].to_numpy()[gi]
    Fg["outcome_name"] = np.asarray(outs)[Fg["outcome"].to_numpy()]
    log(f"  per-doubling bounds and sensitivity subsets ({time.time() - t0:.0f} s)")
    return dict(Fg=Fg, s1=s1, S2=S2, C=C, PP=PP, NP=NP, NO=NO, AL=AL, PD=PD, SS=SS, gg=gg)


# ============================================================================= tables
def ci_cols(df, est="est", se="se", prefix=""):
    df[prefix + "rate_ratio"] = np.exp(df[est])
    df[prefix + "ci_lo"] = np.exp(df[est] - 1.96 * df[se])
    df[prefix + "ci_hi"] = np.exp(df[est] + 1.96 * df[se])
    return df


def write_tables(D, M, G, info, checks_rows, args, tab, t_start):
    g = D["groups"]
    S2, C = M["S2"], M["C"]
    # 1. groups
    gg = g.merge(G, left_index=True, right_on="gid", how="left")
    gg = gg.merge(M["gg"][["gid", "alpha_TRIM72_pooled", "implied_true_ratio_det_vs_not"]], on="gid", how="left")
    gout = gg[["sample", "plate", "well", "drug", "conc", "well_class", "well_subclass", "cell_line_id", "cell_name",
               "tp53_group", "n_cells", f"det_{GENE}", "keep_prob", "n_used", "n_det", "fitted", "skip_reason",
               "mbar", "alpha_num", "alpha_den", "alpha_TRIM72_pooled", "implied_true_ratio_det_vs_not"]].rename(
        columns={"n_cells": "n_cells_total", f"det_{GENE}": "n_TRIM72_detected_total", "keep_prob": "sampling_prob",
                 "n_used": "n_cells_used", "n_det": "n_TRIM72_detected_used",
                 "mbar": "mean_expected_TRIM72_per_cell", "alpha_num": "nb_moment_numerator",
                 "alpha_den": "nb_moment_denominator", "alpha_TRIM72_pooled": "alpha_TRIM72_pooled_class_tp53"})
    gout["fitted"] = gout["fitted"].fillna(False).astype(bool)
    gout.loc[gout["skip_reason"].eq("") & ~gout["fitted"], "skip_reason"] = "too few detected cells after sampling"
    gout.to_csv(os.path.join(tab, "groups.csv.gz"), index=False, float_format="%.6g")
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
            cs.append(dict(**{"class": cl}, tp53_group=tp, n_wells=h["sample"].nunique(),
                           n_lines=h["cell_line_id"].nunique(), n_groups=len(h),
                           n_cells_total=int(h["n_cells_total"].sum()), n_cells_used=int(h["n_cells_used"].sum()),
                           n_TRIM72_detected_used=int(h["n_TRIM72_detected_used"].sum()),
                           pct_TRIM72_detected=100 * h["n_TRIM72_detected_used"].sum() / h["n_cells_used"].sum(),
                           alpha_TRIM72_pooled=ar["alpha_TRIM72_pooled"].iloc[0] if len(ar) else np.nan,
                           median_implied_true_ratio=ar["median_implied_ratio"].iloc[0] if len(ar) else np.nan,
                           weighted_log2_true_ratio=ar["weighted_log2_ratio"].iloc[0] if len(ar) else np.nan))
    pd.DataFrame(cs).to_csv(os.path.join(tab, "class_summary.csv"), index=False, float_format="%.6g")
    # 3. TRIM72 meta by TP53 group (all outcomes)
    T = S2[S2["predictor"] == GENE].copy().rename(columns={"outcome_name": "outcome", "est": "log_rr",
                                                           "tau2": "tau2_lines", "I2": "I2_lines",
                                                           "n_pos": "n_lines_positive"})
    T = ci_cols(T, "log_rr", "se")
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
       "ci_hi", "log_rr", "se", "z", "p", "q_bh", "family", "tau2_lines", "I2_lines", "n_lines_positive",
       "median_line_log_rr"]].to_csv(os.path.join(tab, "trim72_meta_by_tp53_group.csv"), index=False,
                                     float_format="%.6g")
    # 4. WT minus altered (TRIM72)
    Ct = C[C["predictor"] == GENE].copy().rename(columns={"outcome_name": "outcome"})
    Ct["ratio_of_rate_ratios"] = np.exp(Ct["diff"])
    Ct["ci_lo"] = np.exp(Ct["diff"] - 1.96 * Ct["se_diff"])
    Ct["ci_hi"] = np.exp(Ct["diff"] + 1.96 * Ct["se_diff"])
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
        "log_rr_altered", "se_altered", "diff", "se_diff", "ratio_of_rate_ratios", "ci_lo", "ci_hi", "z", "p",
        "p_perm", "q_bh", "family", "paired_n_wells", "paired_diff", "paired_se", "paired_p_perm"]].to_csv(
        os.path.join(tab, "trim72_WT_minus_altered.csv"), index=False, float_format="%.6g")
    # 5-6. placebo predictors
    PP = M["PP"].rename(columns={"outcome_name": "outcome", "est": "log_rr"})
    PP[["predictor", "program", "stress_program", "detection_rate", "outcome", "class", "contrast", "n_lines",
        "n_groups", "rate_ratio", "ci_lo", "ci_hi", "log_rr", "se", "p"]].to_csv(
        os.path.join(tab, "placebo_predictors.csv"), index=False, float_format="%.6g")
    M["NP"].to_csv(os.path.join(tab, "placebo_predictor_null.csv"), index=False, float_format="%.6g")
    # 7. placebo outcomes
    M["NO"].to_csv(os.path.join(tab, "placebo_outcome_null.csv"), index=False, float_format="%.6g")
    # 8. per doubling
    PD = M["PD"]
    PD.to_csv(os.path.join(tab, "per_doubling_bounds.csv"), index=False, float_format="%.6g")
    # 9. sensitivity
    M["SS"].to_csv(os.path.join(tab, "sensitivity_subsets.csv"), index=False, float_format="%.6g")
    # 10. line-level estimates (TRIM72; p53 + screen outcomes)
    s1 = M["s1"]
    L = s1[(s1["predictor"] == GENE) & s1["outcome_name"].isin(PRIMARY_OUT + SCREEN_OUT +
                                                               [o for o in P53_MEMBERS])].copy()
    L = L.rename(columns={"outcome_name": "outcome", "est": "log_rr", "tau2": "tau2_wells", "n_pos":
                          "n_wells_positive"})
    L["cell_name"] = L["cell_line_id"].map(D["lines"].set_index("cell_line_id")["cell_name"])
    L = L[["outcome", "outcome_type", "class", "cell_line_id", "cell_name", "tp53_group", "n_wells", "log_rr", "se",
           "tau2_wells", "n_wells_positive"]]
    L.to_csv(os.path.join(tab, "line_estimates.csv.gz"), index=False, float_format="%.6g")
    # 11. per-group fits (TRIM72; p53 + screen outcomes)
    Fg = M["Fg"]
    Fg = Fg[["sample", "plate", "well_class", "cell_line_id", "tp53_group", "outcome_name", "beta", "se", "phi",
             "unadj", "n_det_pred", "y_tot", "y_det"]].rename(
        columns={"outcome_name": "outcome", "beta": "log_rr", "phi": "dispersion", "unadj": "log_rr_unadjusted",
                 "n_det_pred": "n_TRIM72_detected", "y_tot": "outcome_counts", "y_det": "outcome_counts_detected"})
    Fg.to_csv(os.path.join(tab, "group_fits_TRIM72_p53_screen.csv.gz"), index=False, float_format="%.5g")
    # 12. modules
    mods = []
    pc = os.path.join(REPO, "mg53_perturbation", "assay_panel", "panel.csv")
    cite = {}
    if os.path.exists(pc):
        pdf = pd.read_csv(pc)
        for _, r in pdf.iterrows():
            gname = str(r["gene/assay"]).split(" ")[0]
            cite[gname] = (r.get("module", ""), r.get("literature_citation", ""))
    for o in list(SCORES) + SCREEN_GENES + P53_PRIMARY + ["TP53"]:
        mem = SCORES.get(o, [o])
        mods.append(dict(outcome=o, members=";".join(mem), n_members=len(mem),
                         panel_csv_module=cite.get(o, ("", ""))[0] if o not in SCORES else
                         ";".join(sorted(set(str(cite.get(x, ("", ""))[0]) for x in mem))),
                         literature_citation=cite.get(o, ("", ""))[1] if o not in SCORES else ""))
    mods.append(dict(outcome="(not testable)", members=NOT_IN_CELL_PANEL_NOTE, n_members=0, panel_csv_module="",
                     literature_citation=""))
    mods.append(dict(outcome="(placebo predictors)", members=";".join(D["placebo"]), n_members=len(D["placebo"]),
                     panel_csv_module="", literature_citation=""))
    mods.append(dict(outcome="(placebo outcomes)", members=";".join(D["placebo_out"]),
                     n_members=len(D["placebo_out"]), panel_csv_module="", literature_citation=""))
    pd.DataFrame(mods).to_csv(os.path.join(tab, "modules_and_gene_sets.csv"), index=False)
    # 13. checks
    pd.DataFrame(checks_rows).to_csv(os.path.join(tab, "checks.csv"), index=False)
    # 14. headline
    head = []
    hv = Ct[Ct["outcome"].isin(PRIMARY_OUT + ["ATF3", "PMAIP1", "NFKB_SCORE", "FERROPTOSIS_SCORE",
                                              "APOPTOSIS_SCORE", "SLC7A11"])]
    NPt = M["NP"]
    NOt = M["NO"]
    for _, r in hv.iterrows():
        np_ = NPt[(NPt["outcome"] == r["outcome"]) & (NPt["class"] == r["class"]) &
                  (NPt["contrast"] == "WT minus altered") & (NPt["placebos"] == "all placebos")]
        no_ = NOt[(NOt["outcome"] == r["outcome"]) & (NOt["class"] == r["class"]) &
                  (NOt["contrast"] == "WT minus altered")]
        pdr = PD[(PD["outcome"] == r["outcome"]) & (PD["class"] == r["class"]) & (PD["contrast"] == "WT minus altered")]
        sw = S2[(S2["predictor"] == GENE) & (S2["outcome_name"] == r["outcome"]) & (S2["class"] == r["class"])]
        rw = sw[sw["tp53_group"] == "WT"]
        ra = sw[sw["tp53_group"] == "altered"]
        head.append(dict(outcome=r["outcome"], **{"class": r["class"]}, n_lines_WT=r["n_lines_WT"],
                         n_lines_altered=r["n_lines_altered"],
                         rr_WT=np.exp(r["log_rr_WT"]), p_WT=rw["p"].iloc[0] if len(rw) else np.nan,
                         rr_altered=np.exp(r["log_rr_altered"]), p_altered=ra["p"].iloc[0] if len(ra) else np.nan,
                         WT_minus_altered_log_rr=r["diff"], ci_lo_log=r["diff"] - 1.96 * r["se_diff"],
                         ci_hi_log=r["diff"] + 1.96 * r["se_diff"], p=r["p"], p_perm=r["p_perm"], q_bh=r["q_bh"],
                         paired_within_well_diff=r["paired_diff"], paired_p_perm=r["paired_p_perm"],
                         placebo_predictor_percentile=np_["TRIM72_percentile_among_placebos"].iloc[0]
                         if len(np_) else np.nan,
                         placebo_predictor_empirical_p=np_["empirical_p"].iloc[0] if len(np_) else np.nan,
                         placebo_outcome_percentile=no_["percentile_among_placebo_outcomes"].iloc[0]
                         if len(no_) else np.nan,
                         placebo_outcome_empirical_p=no_["empirical_p"].iloc[0] if len(no_) else np.nan,
                         per_doubling_diff_ci_lo=pdr["per_doubling_ci_lo"].iloc[0] if len(pdr) else np.nan,
                         per_doubling_diff_ci_hi=pdr["per_doubling_ci_hi"].iloc[0] if len(pdr) else np.nan))
    H = pd.DataFrame(head)
    H.to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.6g")
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        if D["adjust"]:
            fh.write(f"SENSITIVITY RUN: every model also adjusts for log((count + 0.5) / total UMI) of "
                     f"{', '.join(D['adjust'])}; outcomes that contain these genes are not fitted.\n\n")
        fh.write(README_TABLES.format(cap=args.max_cells_per_group, min_cells=args.min_cells, min_det=args.min_det,
                                      minc=args.min_outcome_counts, mine=args.min_expected_det,
                                      rr=args.placebo_range, perm=args.perm, placebos=", ".join(D["placebo"]),
                                      n_po=len(D["placebo_out"]), seed=args.seed, perm_paired=args.perm_paired))
    return H


README_TABLES = """Tables of single_cell_all.py (D1b at full scale; re-created by: python3 single_cell_all.py). ASSOCIATIONS ONLY:
Tahoe has no MG53 perturbation and measures mRNA, so 'TRIM72-detected cells carry X% more p53-target mRNA' says nothing
causal about MG53 -> p53, and p53 activity is read from its target genes' mRNA. The TP53 genotype is the control: an MG53
-> p53 effect can only act where p53 works, so the PRIMARY ESTIMAND is the TRIM72 log rate ratio in TP53-WT lines minus
that in TP53-altered lines ('WT minus altered'); what is equal in both groups is not via p53.

Model, per (well, cell line) group: quasi-Poisson GLM (IRLS, log link, dispersion = Pearson chi2/df floored at 1) of an
outcome's per-cell counts on 'predictor gene detected (>= 1 UMI)' + log(total UMI) + log S-phase fraction + log G2M
fraction (fractions = (module counts + 0.5) / total UMI), offset log(total UMI); same model as downstream_p53.py (d).
Groups: >= {min_cells} cells, >= {min_det} TRIM72-detected and >= {min_det} undetected cells, line expresses TRIM72 (atlas expr_mask),
TP53 group known, not a failed well. Cells: a uniform random subsample of at most {cap} cells per group (0 = all; Bernoulli,
seed {seed} per file). A fit (predictor x outcome x group) needs outcome counts >= {minc}, expected outcome counts in the
predictor-detected cells >= {mine} and a gene outcome expressed in the line; fits where the outcome is entirely in one arm
(separation) or that did not converge are dropped (checks.csv counts them).
Meta-analysis: two-stage DerSimonian-Laird random effects: stage 1 over the wells of a (line, well class), stage 2 over
lines within a TP53 group (17 WT / 33 altered lines annotated; 17 / 30 have fitted groups: NCI-H661 does not express
TRIM72, NCI-H2122 and NCI-H596 have too few TRIM72-detected cells; lines are the units because the same lines repeat in
every well). WT minus altered = difference of the two stage-2 means, SE = sqrt(sum of squared SEs); p_perm = TP53-label
permutation over lines ({perm} permutations; the line-level estimates are fixed and the WT / altered split of the lines
with data is reshuffled). 'paired' = per
well, inverse-variance mean of the WT groups minus that of the altered groups, then DL over wells (compares lines only
within the same well, so drug and well effects cancel); its p (paired_p_perm) comes from reshuffling the TP53 labels of
the lines ({perm_paired} permutations; scores, primary outcomes, ATF3, PMAIP1), because a normal p over wells would treat
the same lines in every well as independent.
All p-values are two-sided. Placebo-based empirical p-values cannot go below 1 / (n placebos + 1) (1/17 = 0.059).
Well classes: DMSO; 'TRIM72 raisers' = drug-doses with the gene panel's TRIM72 call 'up' (21); 'p53 activators' =
P53_ACTIVITY z >= 3 and FDR < 0.10 and not a raiser; 'other drugs' = the rest; 'all wells' = all of them.
Outcomes: P53_SCORE = counts of the 21 P53_ACTIVITY members summed; P53_PRIMARY5 = MDM2+CDKN1A+FDXR+ZMAT3+DDB2 summed;
NFKB_SCORE = NFKBIA+TNFAIP3+CXCL8 (panel.csv NF-kB), NFKB8_SCORE = the gene panel's 8 NF-kB targets; FERROPTOSIS_SCORE =
SLC7A11+GPX4+CHAC1; APOPTOSIS_SCORE = BAX+BBC3+PMAIP1; single genes as named. Placebo outcomes: the {n_po} non-p53-linked,
non-screen panel genes (modules_and_gene_sets.csv). Placebo predictors (detection rate within 1/{rr}x-{rr}x of TRIM72's in the
fitted groups, not p53-linked, not a screen gene): {placebos}.
Effect sizes: log_rr = natural-log rate ratio (detected vs undetected cells); rate_ratio = exp(log_rr); CIs are 95%.

groups.csv.gz              one row per (well, line) in well_line.parquet: class, TP53 group, cells total / used, TRIM72-
                           detected cells, sampling probability, fitted (= TRIM72 fittable after the subsample; only
                           these groups enter any table) or skip_reason, NB moment sums of TRIM72 counts
                           (numerator sum((y-m)^2-y), denominator sum(m^2), m = depth x group rate), pooled alpha and
                           the implied true-rate ratio of detected vs undetected cells.
class_summary.csv          per well class x TP53 group: wells, lines, groups, cells, TRIM72-detected cells, pooled
                           alpha, implied true-rate ratio (median; and its log2 weighted by the P53_SCORE fits' 1/se^2).
trim72_meta_by_tp53_group.csv  TRIM72 predictor, every outcome x class x TP53 group (WT, altered, all lines): stage-2
                           rate ratio, CI, p, q_bh (BH within family: 'p53 + screen' or 'placebo outcomes'), tau2 and
                           I2 between lines, lines with a positive estimate, median line estimate.
trim72_WT_minus_altered.csv    TRIM72: WT minus altered per outcome x class: both stage-2 estimates, difference, ratio of
                           rate ratios with CI, p (normal), p_perm, q_bh (BH within family on p_perm where computed,
                           else p), and the within-well paired check (paired_p_perm).
placebo_predictors.csv     every predictor (TRIM72 and the placebos) x p53/screen outcome x class x contrast (WT,
                           altered, all lines, WT minus altered): estimate, CI, p, detection rate, program.
placebo_predictor_null.csv TRIM72 against the placebo-predictor distribution per outcome x class x contrast (all
                           placebos; non-stress placebos): placebo median / sd / range, TRIM72 percentile, empirical p
                           = (1 + #placebos at least as far from the placebo median) / (n + 1), calibrated z =
                           (TRIM72 - placebo median) / sqrt(se^2 + placebo sd^2).
placebo_outcome_null.csv   TRIM72 predictor: each p53 / screen outcome against the distribution over the placebo
                           outcomes (same class x contrast): percentile, empirical p, percentile of z.
per_doubling_bounds.csv    what the test can exclude per doubling of a cell's TRIM72: log_rr / log2_true_ratio, where
                           log2_true_ratio = log2 of the implied true TRIM72 rate in detected vs undetected cells
                           (gamma-Poisson with the pooled alpha, at each group's mean count; averaged with the P53_SCORE
                           fits' 1/se^2 weights). per_doubling_ci_lo/hi: 95% CI of the rate ratio per doubling;
                           largest_change_not_excluded_pct = largest change per doubling inside the CI; mde80 = change
                           per doubling detectable with 80% power (2.80 x SE). For WT minus altered, each group is
                           scaled by its own ratio. alpha includes technical overdispersion not explained by depth, which
                           would overstate the true-rate contrast and make these bounds too tight.
sensitivity_subsets.csv    primary outcomes, WT / altered / difference (normal p and permutation p, 2,000 perms) in:
                           plate 13 left out; high-TRIM72 plates (1-3, 14) vs low (4-13) [TRIM72 untreated ~10x lower on
                           4-13]; raisers with vs without p53 activation; the two idarubicin 5 uM wells (D1's wells).
                           Not pre-specified: read with the placebo columns (the same WT-minus-altered difference for
                           the placebo predictors in the same subset: median, sd, TRIM72 percentile, empirical p).
line_estimates.csv.gz      stage-1 per line x class (TRIM72; p53 and screen outcomes): estimate, SE, wells, tau2.
group_fits_TRIM72_p53_screen.csv.gz  per-group fits (TRIM72; p53 and screen outcomes): log_rr, SE, dispersion,
                           unadjusted log rate ratio, TRIM72-detected cells, outcome counts.
modules_and_gene_sets.csv  outcome definitions with panel.csv modules and citations; placebo gene lists; modules of
                           panel.csv that the per-cell panel lacks.
key_results.csv            headline rows: p53 primary outcomes and screen modules, WT minus altered per class, with the
                           permutation p, the paired check, both placebo nulls and the per-doubling CI.
checks.csv                 bookkeeping and agreement checks.
"""


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--max-cells-per-group", type=int, default=2000,
                    help="uniform subsample per (well, line); 0 = all cells (default 2000: 47M of the 60M cells "
                         "in qualifying groups, 87%% of their TRIM72-detected cells)")
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
    data, tab, cdir = resolve_paths(args)
    log(f"data {data}; tables {tab}; cache {cdir}")
    sm, lines, expr, wl, panel, ga = load_setup(data, args)
    D = build_design(sm, lines, expr, wl, panel, args)
    D.update(sm=sm, lines=lines)
    del wl
    g = D["groups"]
    q = g["qualifies"]
    log(f"groups: {len(g)} (well, line); {int(q.sum())} qualify ({int(g.loc[q, 'n_cells'].sum()):,} cells, "
        f"{int(g.loc[q, 'det_TRIM72'].sum()):,} TRIM72-detected); expected cells used "
        f"{int((g['n_cells'] * g['keep_prob']).sum()):,} (cap {args.max_cells_per_group})")
    log(f"placebo predictors ({len(D['placebo'])}): " + ", ".join(f"{x} {D['rate'][x]:.4f}" for x in D["placebo"])
        + f"; TRIM72 {D['rate'][GENE]:.4f}")
    log(f"outcomes: {len(D['outcomes'])} ({len(D['placebo_out'])} placebo outcomes); cell columns {len(D['need'])}"
        + (f"; ADJUSTED for {', '.join(D['adjust'])} (sensitivity run)" if D["adjust"] else ""))
    params = dict(version=VERSION, cap=args.max_cells_per_group, min_cells=args.min_cells, min_det=args.min_det,
                  minc=args.min_outcome_counts, mine=args.min_expected_det, rr=args.placebo_range, seed=args.seed,
                  limit_files=args.limit_files, placebo=D["placebo"], outcomes=D["outcomes"], k2=K2_OUT,
                  n_files=len(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet"))))
    if D["adjust"]:
        params["adjust"] = D["adjust"]
    pj = os.path.join(cdir, "run_info.json")
    fits_p, grp_p = os.path.join(cdir, "fits.parquet"), os.path.join(cdir, "group_stats.parquet")
    cached = False
    if not args.recompute and all(os.path.exists(p) for p in (pj, fits_p, grp_p)):
        old = json.load(open(pj, encoding="utf-8"))
        if old.get("params") == params:
            cached = True
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
        F.to_parquet(fits_p, index=False)
        G.to_parquet(grp_p, index=False)
        info_s = {k: v for k, v in info.items()}
        with open(pj, "w", encoding="utf-8") as fh:
            json.dump(dict(params=params, info=info_s, irls_checks=chk), fh)
        log(f"streamed and fitted in {info['stream_seconds']:.0f} s: {len(G)} groups, {len(F):,} fits; "
            f"peak RSS main {rss_gb():.2f} GB, largest worker {info['children_peak_rss_gb']} GB")
    # a group counts as fitted only if TRIM72 itself is fittable after the subsample (>= min_det detected and
    # undetected cells); placebo-predictor fits of the other groups are dropped, so that TRIM72 and the placebos
    # use the same groups
    n_any = int(G["fitted"].sum())
    G["fitted"] = (G["fitted"].astype(bool) & (G["n_det"] >= args.min_det)
                   & (G["n_used"] - G["n_det"] >= args.min_det))
    F = F[F["gid"].isin(G.loc[G["fitted"], "gid"])].reset_index(drop=True)
    # ------------------------------------------------------------------ checks
    seen = np.asarray(info["seen_group"])
    qq = g["qualifies"].to_numpy()
    mism = int(np.sum(seen[qq] != g.loc[qq, "n_cells"].to_numpy()))
    checks_rows.append(dict(check="cells read (all files)", value=info["cells_read"], n=info["files_read"],
                            note="Tahoe-100M has 95,624,334 cells in 3,388 files"))
    checks_rows.append(dict(check="qualifying groups whose cells read != well_line n_cells", value=mism,
                            n=int(qq.sum()), note="0 = every qualifying group was read completely"))
    badp = [p for p in info["expected_plate"] if info["seen_plate"].get(p) != info["expected_plate"][p]]
    checks_rows.append(dict(check="plates with cells read != well_line total", value=len(badp), n=14,
                            note=", ".join(badp)))
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
    # ------------------------------------------------------------------ meta + tables
    log("meta-analysis")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        M = run_meta(D, G, F, args)
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
        f"child {resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024 ** 2:.2f} GB")


if __name__ == "__main__":
    main()
