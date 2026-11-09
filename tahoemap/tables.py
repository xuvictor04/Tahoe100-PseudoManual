"""tables - the fold-change tables: for every gene, which drug-doses raise or lower it (pooled over the cell lines and
line by line), in which cell lines, and the drug, drug-dose, cell-line, plate and well context needed to read them.

Why this stage exists: the atlas (atlas/effects) keeps its results as dense matrices addressed by row numbers
(drug-doses x genes, wells x genes, drug-doses x lines) and the tensor stage adds the per-cell-line layer (genes x
drug-doses x lines). Answering "select a gene: which drugs raise it, in which lines, how cleanly?" from those needs
the matrices, the index tables, the flag rules and the significance rules at once. This stage does that join once,
genome-wide, and writes plain parquet tables keyed by gene col / drug-dose row (dd) / line, with symbols, drug names,
doses, flags and cell-line names spelled out. Every number is taken from, or is a simple summary of, the atlas and
tensor values; the two things estimated here are the per-line |z| cut and each gene's cell-cycle slopes (below).

Flagged values are kept. Every table lists flagged drug-doses in their ranked place, with their flags and clean =
False, so that readers can show them with an alert; ranked lists that are capped (drug_line_top) keep the strongest
over all drug-doses and also the strongest clean ones that would fall outside them. Only estimates leave
artifact-flagged drug-doses out: the per-line |z| calibration (a null), response_sd (a typical spread) and the
cell-cycle slopes.

Pooled vs per line. The pooled values are the atlas's median over the cell lines, so a response that only a minority
of the measured lines show (fewer than about half: e.g. a p53 response in the TP53-wild-type lines only) does not
reach drug_effects or the n_dd_* / best_* columns of genes.parquet. line_effects and drug_line_top are where such
responses appear.

Per-line significance. A per-line z rests on one or two wells and on a spread estimated from that line's reference
wells, and its tails are heavier than a normal's: with ~1,000 clean drug-doses per (gene, line), a fixed cut of 3 or 4
passes by chance. The cut is therefore calibrated on the data: the null is the per-line z of the (gene, clean
drug-dose) pairs whose pooled |z| < 2 (in up to CAL_MAX_GENES evenly spaced genes), and the cut t is the smallest grid
value >= LINE_Z_FLOOR whose expected number of chance passes per (gene, line) over the clean drug-doses, P(|z| >= t) x
(clean drug-doses), is <= LINE_CHANCE_MAX. line_effects (n_dd_up / n_dd_down and best_*) and drug_line_top use t;
tables/info.json records it (line_z_threshold, line_z_expected_chance, the null's tail). The 'lines up' of
drug_effects (per-line z >= 2, fold >= 1.2, given a pooled call) stays a descriptive, uncalibrated count of where
the pooled effect shows up.

Lines that do not express a gene. 'expressed' and n_lines_expressing are tensor/line_measured.npy: the atlas's
expr_mask AND a line level >= tensor.AMB_FRAC x the gene's pooled CPM; below it the line reads only the wells'
ambient RNA, and its per-line values are NaN (tensor stage).

Baseline. Every fold change here is relative to the SAME cell line's median over the plate's DRUG wells (the typical
treated well: most drugs leave most genes alone), never to DMSO. Per line and well the atlas takes log2 CPM minus that
line's plate median, minus the profile's composition (library) shift, minus the well-position effect; pooled values
(DD_lfc, DD_z) take the median over lines per well and then the mean (lfc) or Stouffer sum (z) over the drug-dose's
used wells; per-line values (tensor DDL_lfc, DDL_z) skip the median over lines. fold = 2 ** lfc.

Rules reused verbatim from the atlas: significance (up = q_up < 0.10 and lfc >= log2 1.2; down symmetric), the flag
strings (drug-dose flags + atlas_core.gene_flags per gene), "clean" = no atlas_core.ARTIFACT_FLAGS flag (for a gene:
the drug-dose's flags plus 'position correction uncertain' for that gene; atlas_core.has_artifact), dose patterns
(atlas_core.dose_shape, here vectorised by dose_shape_codes and checked against it), noise-class RNAs
(atlas_core.NOISE_RNA_RE) and salt forms (tlib.salt_base). One refinement: the cell-cycle shift.

Cell-cycle shift. The atlas flags a drug-dose 'cell-cycle shift' when its S_PHASE or G2M_PHASE module moved: its cells
moved into or out of S or G2/M. Whether that explains one gene's change depends on how much the gene goes with the
cycle, which is measured here (cell_cycle_share): per gene, a robust regression of its pooled lfc on the two modules'
pooled lfc (lfc ~ a + bS x S + bG x G) over the drug-doses without another artifact flag. At every drug-dose with the
flag the shift predicts bS x S + bG x G, with the slopes fitted without that drug-dose (leave-one-out, so the change
being judged does not pull the slopes toward explaining itself), and cc_share = |that| / |lfc| when it has the sign
of the change (else 0, at most 1). Fitted slopes are attenuated by measurement noise, so the rule doubles them
(CC_SAFETY = 2): the shift is not the explanation when 2 x cc_share < 0.5 and the change left after the doubled
prediction is at least the 1.2x floor; then the gene's flags read 'cell-cycle shift (explains ~N% here)', which is no
artifact flag, while the plain token 'cell-cycle shift' (an artifact flag) stays everywhere else. Other artifact
flags of a drug-dose still apply. Real-data example (full-fit slopes, before the leave-one-out step): TRIM72 (slopes
bS +0.50, bG +0.47) is raised 12.2x by idarubicin 5 uM, of which the shift would explain ~4% (cleared), while
panobinostat 0.5 uM (~87%) stays flagged; classic cycle genes (PCNA, CCNE2 bS ~ +1.5; TOP2A, CCNB1 bG ~ +1.4) keep
the flag at a real shift.

Outputs in OUT/tables/ (README.md there documents every column, its units and its baseline):
    genes.parquet          one row per gene: level, counts of drug-doses up / down, best drug-dose up / down (any and
                           clean), specificity (z gap to the next compound), correlation with the S / G2M modules,
                           cell-cycle slopes (cc_slope_S / cc_slope_G2M)
    drug_effects.parquet   gene x drug-dose rows with |z| >= 3 or q_up / q_down < 0.1, flagged ones included: pooled
                           fold change, z, q, flags, clean, how many / which lines move, dose pattern, cc_share
    line_effects.parquet   gene x line: baseline level, whether the line expresses it, spread of the line's
                           responses, drug-doses moving the gene >= 1.5x at per-line |z| >= t (calibrated, >= 4) and
                           the strongest of them up / down in that line, over the clean drug-doses and (*_all, with
                           the flags) over all drug-doses
    drug_line_top.parquet  per gene: the 15 strongest (drug-dose, line) cells up and down over all drug-doses (with
                           flags and clean), plus any of the 15 strongest clean ones beyond them (per-line |z| >= t)
    drugdoses.parquet      drugdose.csv + dd, salt_base, top 15 significant genes up / down
    drugs.parquet          per drug: doses, significant genes by dose, best dose, lowest active dose, flags, signature
                           similarity between doses
    lines.parquet          lines.csv + TP53 status, drug-doses that deplete the line (-1 = not measured), median
                           response strength
    plates.parquet         per plate: wells, doses, reliability, plate factor, DMSO and failed wells, cells per well
    wells.parquet          wells.csv + total UMI per well (per-gene counts stay in tensor/well_counts.npy)
    info.json              row counts, the per-line |z| calibration (line_z_threshold, line_fold_min, ...) and the
                           cell-cycle rule's counts (cell_cycle_rule)

Memory: the pooled drug-dose x gene matrices are held in memory (~75 MB each at full scale); the per-line tensor
(~1.9 GB per array in float16) is read in gene chunks sized by mem_gb, and drug_effects.parquet is streamed to disk
chunk by chunk, so the peak stays near mem_gb + ~1 GB whatever the number of genes.
"""

import json
import math
import os
import time
import warnings

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import scipy.sparse as sp

from . import atlas_core as A
from . import tlib as T
from .common import log, read_effects_index, replace_file, stamp_stage, write_json, write_parquet
from .tensor import AMB_FRAC, measured_mask

VERSION = 4                         # 3: a cell-cycle shift blocks a gene only when it explains its change;
#                                     4: each cell-cycle-flagged drug-dose is judged with slopes fitted without it

LFC_MIN = A.LFC_MIN                 # log2(1.2): smallest change the atlas counts
Q_CUT = A.Q_CUT                     # 0.10: the atlas FDR cut
KEEP_Z = 3.0                        # drug_effects keeps |pooled z| >= this, or q_up / q_down < Q_CUT
LINE_Z = 2.0                        # drug_effects (descriptive): a line is 'up' at per-line z >= 2 and lfc >= log2 1.2
LINE_Z_FLOOR = 4.0                  # per-line significance: the calibrated |z| cut t is never below this
LINE_CHANCE_MAX = 0.05              # t: expected chance passes per (gene, line) over the clean drug-doses <= this
NULL_POOLED_Z = 2.0                 # calibration null: (gene, clean drug-dose) pairs with pooled |z| < this
CAL_MAX_GENES = 3000                # calibration: at most this many genes (evenly spaced cols)
CAL_STEP = 0.05                     # calibration: grid of candidate cuts (and histogram bin width)
CAL_Z_MAX = 50.0                    # calibration: the grid ends here (|z| above it share the last bin)
STRONG_LFC = math.log2(1.5)         # line_effects counts: fold >= 1.5 (or <= 1/1.5)
DEPLETE_Z = -3.0                    # lines.n_dd_depleted: relative-abundance z (DD_Az) <= this
ABUNDANCE_UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")   # flags that make a
                                    # drug-dose's cell counts untrustworthy (toxic etc. are what depletion means)
MIN_SD_DD = 10                      # response_sd needs >= this many measured clean drug-doses
CC_FLAG = "cell-cycle shift"        # the drug-dose flag (atlas_core.flags_for) that cell_cycle_share() refines per gene
CC_CLEARED = "cell-cycle shift (explains ~{pct}% here)"   # its gene-level text where the shift is not the explanation
                                    # of the gene's change: no artifact flag (pct = round(100 x share))
CC_SAFETY = 2.0                     # the fitted slopes are doubled before the rule (noise attenuates fitted slopes)
CC_SHARE_MAX = 0.5                  # not the explanation: CC_SAFETY x share < this and the change left after the
                                    # doubled prediction, |lfc| x (1 - CC_SAFETY x share), >= log2 1.2
CC_HUBER = 2.5                      # cell-cycle slopes: Huber weights beyond this many robust SDs of the residuals
CC_MIN_FIT = 20                     # cell-cycle slopes need >= this many fitted drug-doses (per gene: finite lfc)
CC_MODULES = ("S_PHASE", "G2M_PHASE")   # the atlas modules whose pooled lfc (drugdose.csv <module>_lfc) the slopes use
MAX_LINES_LISTED = 12               # lines_up / lines_down: at most this many names
TOP_CELLS = 15                      # drug_line_top: (drug-dose, line) cells per gene and direction
TOP_GENES = 15                      # drugdoses top_up / top_down
MIN_ACTIVE_GENES = 10               # lowest_active_dose: significant genes a dose needs to count as active
RESPONSIVE_MIN_DD = 3               # signature_r_between_doses: genes significant in >= this many drug-doses
PATTERNS = ("none", "single dose", "all doses, stronger at high dose", "all doses, flat", "top dose only",
            "rises with dose", "two highest doses", "inconsistent across doses")   # atlas_core.dose_shape outcomes
_PAT = np.array(PATTERNS, dtype=object)


# ----------------------------------------------------------------------------- vectorised atlas rules
def dose_shape_codes(V, thr=2.0):
    """atlas_core.dose_shape for many rows at once. V = rows x doses (ascending conc, signed so that positive = the
    effect; NaN = no value at that dose) -> int8 codes into PATTERNS. Same rules in the same order: NaNs are dropped
    first (the remaining doses keep their order), then none / single dose / all doses (stronger or flat) / top dose
    only / rises with dose / two highest doses / inconsistent."""
    V = np.asarray(V, dtype=np.float64)
    if V.ndim == 1:
        V = V[:, None]
    nr, m = V.shape
    fin = np.isfinite(V)
    n = fin.sum(axis=1)
    C = np.take_along_axis(V, np.argsort(~fin, axis=1, kind="stable"), axis=1)   # finite values first, in order
    pos = np.arange(m)[None, :]
    r = np.arange(nr)
    first = C[:, 0]
    last = C[r, np.maximum(n - 1, 0)]
    sec = C[r, np.maximum(n - 2, 0)]
    mx = np.max(np.where(pos < n[:, None], C, -np.inf), axis=1)
    mn = np.min(np.where(pos < n[:, None], C, np.inf), axis=1)
    mx_prev = np.max(np.where(pos < (n - 1)[:, None], C, -np.inf), axis=1)
    if m > 1:
        mono = ((C[:, 1:] >= C[:, :-1] - 0.5) | ~(pos[:, 1:] < n[:, None])).all(axis=1)
    else:
        mono = np.ones(nr, dtype=bool)
    top = last >= thr
    conds = [(n == 0) | (mx < thr), n == 1, (mn >= thr) & (last - first >= 1.0), mn >= thr,
             top & (mx_prev < thr * 0.75), top & mono, (n >= 3) & (np.minimum(sec, last) >= thr)]
    return np.select(conds, list(range(7)), 7).astype(np.int8)


def flag_strings(base, d, posunc, poseff, pscale, cc_pct=None):
    """Per (drug-dose d, gene) item: atlas_core.gene_flags(base[d], posunc, poseff, pscale=pscale) and whether it is
    clean (no artifact flag). cc_pct (int per item; -1 = no change): where the drug-dose's 'cell-cycle shift' is not
    the explanation of this gene's change (cell_cycle_share), the percentage of the change it explains; the token
    then reads CC_CLEARED, which is no artifact flag. gene_flags only thresholds its inputs, so each distinct
    (d, cc_pct, noisy, uncertain, removed) combination is formatted once."""
    d = np.asarray(d, dtype=np.int64)
    if d.size == 0:
        return np.array([], dtype=object), np.array([], dtype=bool)
    posunc = np.asarray(posunc, dtype=bool)
    poseff = np.asarray(poseff, dtype=np.float64)
    pscale = np.asarray(pscale, dtype=np.float64)
    pct = np.full(d.size, -1, dtype=np.int64) if cc_pct is None else np.clip(np.asarray(cc_pct, np.int64), -1, 100)
    noisy = np.isfinite(pscale) & (pscale > A.PLATE_SCALE_FLAG)
    moved = np.isfinite(poseff) & (np.abs(poseff) > 0.2)
    key = (d * 102 + pct + 1) * 8 + noisy * 4 + posunc * 2 + moved
    _, first, inv = np.unique(key, return_index=True, return_inverse=True)
    strs = []
    for i in first:
        f = A.gene_flags(base[d[i]], bool(posunc[i]), float(poseff[i]), pscale=float(pscale[i]))
        if pct[i] >= 0:
            f = "; ".join(CC_CLEARED.format(pct=int(pct[i])) if x == CC_FLAG else x for x in f.split("; "))
        strs.append(f)
    clean = np.array([not A.has_artifact(s) for s in strs], dtype=bool)
    return np.array(strs, dtype=object)[inv.ravel()], clean[inv.ravel()]


def cc_cleared(lfc, share, safety=CC_SAFETY):
    """The cell-cycle rule (module docstring, 'Cell-cycle shift'): the shift is not the explanation of a change lfc
    of which it would explain `share` when safety x share < CC_SHARE_MAX and the change left after the safety-scaled
    prediction, |lfc| x (1 - safety x share), is at least the 1.2x floor. NaN share -> False (the flag stays)."""
    lfc = np.abs(np.asarray(lfc, dtype=np.float64))
    share = np.asarray(share, dtype=np.float64)
    with np.errstate(invalid="ignore"):
        return np.isfinite(share) & (safety * share < CC_SHARE_MAX) & (lfc * (1.0 - safety * share) >= LFC_MIN)


def cc_rule(lfc, pred, safety=CC_SAFETY):
    """For (drug-dose, gene) items whose drug-dose carries 'cell-cycle shift': lfc = the gene's pooled log2 fold
    change there, pred = the part of it the shift predicts (bS x S + bG x G, the gene's fitted slopes times the
    drug-dose's S / G2M module lfc). Returns (share, cleared): share = |pred| / |lfc| when pred has the sign of lfc,
    else 0, capped at 1 (NaN when either is missing); cleared = cc_cleared(lfc, share, safety)."""
    lfc = np.asarray(lfc, dtype=np.float64)
    pred = np.asarray(pred, dtype=np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        same = (np.sign(pred) == np.sign(lfc)) & (lfc != 0)
        share = np.where(same, np.minimum(np.abs(pred) / np.where(lfc != 0, np.abs(lfc), 1.0), 1.0), 0.0)
    share = np.where(np.isfinite(lfc) & np.isfinite(pred), share, np.nan)
    return share, cc_cleared(lfc, share, safety)


def cell_cycle_share(lfc, s_lfc, g_lfc, dd_flags, posunc=None, chunk=4096):
    """How much of a gene's change at a drug-dose flagged 'cell-cycle shift' the shift itself would explain.

    The flag is a property of the drug-dose: its cells moved into or out of S or G2/M (the S_PHASE / G2M_PHASE
    modules' pooled lfc moved). A gene's change there may then only reflect the new mix of cell-cycle phases - for a
    gene that goes with the cell cycle. How much a gene goes with it is measured on the data: per gene, a robust
    regression (OLS, then one Huber reweighting at CC_HUBER robust SDs of the residuals) of its pooled lfc on the two
    modules' pooled lfc, lfc ~ a + bS x S + bG x G, over the drug-doses without any other artifact flag (none, or
    only the cell-cycle shift; per gene also without 'position correction uncertain'). At every drug-dose whose flags
    include 'cell-cycle shift' the shift predicts pred = bS x S + bG x G of the change (cc_rule gives the share and
    whether it is cleared), with the slopes fitted without that drug-dose when it is in the fit (leave-one-out: a
    rank-1 downdate of the final weighted fit, the Huber weights kept): the flagged drug-doses have the largest |S|
    and |G|, so a strong change of the gene's own there would otherwise pull the slopes toward explaining it. Slopes
    need >= CC_MIN_FIT fitted drug-doses with a value for the gene (also after leaving one out). The slopes returned
    (bS, bG: genes.parquet cc_slope_*) are those of the full fit.
    Returns cc (bool per drug-dose: its flags include 'cell-cycle shift'), share (drug-doses x genes float32; NaN
    outside the cc rows or without slopes), cleared (drug-doses x genes bool), the slopes bS, bG (float32 per gene,
    NaN without a fit) and the number of drug-doses in the fit."""
    Dn, gK = lfc.shape
    toks = [set(str(f or "").split("; ")) for f in dd_flags]
    cc = np.array([CC_FLAG in t for t in toks], dtype=bool)
    S = np.asarray(s_lfc, dtype=np.float64)
    G = np.asarray(g_lfc, dtype=np.float64)
    fit = np.array([(t & set(A.ARTIFACT_FLAGS)) <= {CC_FLAG} for t in toks], dtype=bool) & np.isfinite(S) \
        & np.isfinite(G)
    share = np.full((Dn, gK), np.nan, dtype=np.float32)
    cleared = np.zeros((Dn, gK), dtype=bool)
    bS = np.full(gK, np.nan, dtype=np.float32)
    bG = np.full(gK, np.nan, dtype=np.float32)
    nf = int(fit.sum())
    if nf < CC_MIN_FIT or not cc.any():
        return cc, share, cleared, bS, bG, nf
    fi = np.flatnonzero(fit)
    pos_fit = {int(d): k for k, d in enumerate(fi)}                          # drug-dose -> its row in the fit
    rows = np.flatnonzero(cc & np.isfinite(S) & np.isfinite(G))
    X = np.column_stack([np.ones(nf), S[fi], G[fi]])                         # n x 3
    XX = (X[:, :, None] * X[:, None, :]).reshape(nf, 9)                       # n x 9: the products x_i x_j
    for g0 in range(0, gK, chunk):
        g1 = min(gK, g0 + chunk)
        Y = np.asarray(lfc[fi, g0:g1], dtype=np.float64)                      # n x c
        ok = np.isfinite(Y)
        if posunc is not None:
            ok &= ~np.asarray(posunc[fi, g0:g1], dtype=bool)
        n_ok = ok.sum(axis=0)
        enough = n_ok >= CC_MIN_FIT
        W = ok.astype(np.float64)
        Y = np.where(ok, Y, 0.0)
        for it in range(2):                                                   # OLS, then one Huber reweighting
            A_ = (W.T @ XX).reshape(-1, 3, 3) + np.eye(3)[None] * 1e-9          # c x 3 x 3: X' W X per gene
            rhs = (W * Y).T @ X                                                # c x 3: X' W y per gene
            B = np.linalg.solve(A_, rhs[..., None])[..., 0]                   # c x 3
            if it:
                break
            R = Y - X @ B.T
            with np.errstate(all="ignore"):
                sc = 1.4826 * np.nanmedian(np.where(ok, np.abs(R), np.nan), axis=0)
                sc = np.where(np.isfinite(sc) & (sc > 0), sc, 1.0)
                W = ok * np.minimum(1.0, CC_HUBER * sc[None, :] / np.maximum(np.abs(R), 1e-12))
        B[~enough] = np.nan
        bS[g0:g1], bG[g0:g1] = B[:, 1], B[:, 2]
        if rows.size:
            pred = S[rows, None] * B[None, :, 1] + G[rows, None] * B[None, :, 2]
            # leave-one-out: a judged drug-dose that is itself in the fit (its only artifact flag is the shift) is
            # judged with the slopes fitted without it (a rank-1 downdate of X'WX and X'Wy, with the Huber weights
            # of the full fit), so a strong change of its own does not pull the slopes toward explaining it
            for ri, d_ in enumerate(rows):
                k = pos_fit.get(int(d_))
                if k is None:
                    continue
                w = W[k]                                                       # c: this row's weight per gene
                if not (w > 0).any():
                    continue
                A1 = A_ - w[:, None, None] * XX[k].reshape(1, 3, 3)
                r1 = rhs - (w * Y[k])[:, None] * X[k][None, :]
                with np.errstate(all="ignore"):
                    B1 = np.linalg.solve(A1, r1[..., None])[..., 0]
                p1 = S[d_] * B1[:, 1] + G[d_] * B1[:, 2]
                p1[(n_ok - ok[k]) < CC_MIN_FIT] = np.nan
                pred[ri] = np.where(w > 0, p1, pred[ri])
            sh, cl = cc_rule(lfc[rows, g0:g1], pred)
            share[rows, g0:g1] = sh
            cleared[rows, g0:g1] = cl
    return cc, share, cleared, bS, bG, nf


def _module_cols(genes, fxd, gK):
    """{module: gene cols} for CC_MODULES from atlas/effects/modules.json, which lists TOKEN ids (genes.csv 'token')."""
    p = os.path.join(fxd, "modules.json")
    if not os.path.exists(p) or "token" not in genes:
        return {}
    try:
        with open(p, encoding="utf-8") as fh:
            mods = json.load(fh)
    except (OSError, ValueError):
        return {}
    g = genes.iloc[:gK]
    tok = pd.to_numeric(g["token"], errors="coerce").to_numpy()
    out = {}
    for m in CC_MODULES:
        want = {int(t) for t in mods.get(m, []) or [] if str(t).lstrip("-").isdigit()}
        out[m] = np.flatnonzero(np.isin(tok, list(want))) if want else np.zeros(0, dtype=np.int64)
    return out


def _cc_summary(genes, fxd, gK, cc_dd, cc_only, share, cleared, lfc, sig, bS, bG, n_fit):
    """The cell-cycle rule's counts for info.json and README.md: the significant changes at the drug-doses whose only
    artifact flag is the shift and how many the rule clears (with the doubled slopes, and with the slopes as fitted
    for comparison); and, as a check, the same for the genes of the atlas's S_PHASE / G2M_PHASE modules at every
    cell-cycle-flagged drug-dose (the shift is what moves them, so they should rarely be cleared)."""
    ro = np.flatnonzero(cc_only)
    so = sig[ro]
    x1 = cc_cleared(lfc[ro], share[ro], 1.0) & so if ro.size else np.zeros((0, gK), dtype=bool)
    info = {"flag": CC_FLAG, "gene_level_text": CC_CLEARED, "safety_factor": CC_SAFETY,
            "share_max": CC_SHARE_MAX, "lfc_floor": LFC_MIN, "modules": list(CC_MODULES),
            "drugdoses_flagged": int(cc_dd.sum()), "drugdoses_cc_only": int(cc_only.sum()),
            "drugdoses_fitted": int(n_fit), "genes_with_slopes": int(np.isfinite(bS).sum()),
            "significant_at_cc_only": int(so.sum()), "cleared_at_cc_only": int((cleared[ro] & so).sum()),
            "cleared_at_cc_only_x1": int(x1.sum()),
            "significant_at_flagged": int(sig[cc_dd].sum()),
            "cleared_at_flagged": int((cleared[cc_dd] & sig[cc_dd]).sum()), "module_genes": {}}
    rc = np.flatnonzero(cc_dd)
    for m, cols in _module_cols(genes, fxd, gK).items():
        s = sig[np.ix_(rc, cols)]
        info["module_genes"][m] = {
            "genes": int(cols.size), "significant_at_cc": int(s.sum()),
            "cleared": int((cleared[np.ix_(rc, cols)] & s).sum()),
            "median_slope_S": float(np.nanmedian(bS[cols])) if np.isfinite(bS[cols]).any() else None,
            "median_slope_G2M": float(np.nanmedian(bG[cols])) if np.isfinite(bG[cols]).any() else None}
    return info


# ----------------------------------------------------------------------------- helpers
def _nanmedian_last(V):
    """Median over the last axis ignoring NaN (sort-based; NaN sorts last); all-NaN -> NaN. Also the counts."""
    k = np.isfinite(V).sum(axis=-1)
    S = np.sort(V, axis=-1)
    lo = np.take_along_axis(S, np.maximum((k - 1) // 2, 0)[..., None], axis=-1)[..., 0]
    hi = np.take_along_axis(S, np.maximum(k // 2, 0)[..., None], axis=-1)[..., 0]
    return np.where(k > 0, (lo + hi) / 2, np.nan), k


def _corr_with(W, v, chunk=4096):
    """Pearson r of every column of W with v over the rows where both are finite (NaN with < 3 such rows)."""
    v = np.asarray(v, dtype=np.float64)
    fv = np.isfinite(v)
    out = np.full(W.shape[1], np.nan, dtype=np.float32)
    for g0 in range(0, W.shape[1], chunk):
        x = np.asarray(W[:, g0:g0 + chunk], dtype=np.float64)
        m = np.isfinite(x) & fv[:, None]
        n = m.sum(axis=0).astype(np.float64)
        xm = np.where(m, x, 0.0)
        vm = np.where(m, np.where(fv, v, 0.0)[:, None], 0.0)
        sx, sv = xm.sum(axis=0), vm.sum(axis=0)
        nn = np.maximum(n, 1)
        cov = (xm * vm).sum(axis=0) - sx * sv / nn
        vx = (xm * xm).sum(axis=0) - sx * sx / nn
        vv = (vm * vm).sum(axis=0) - sv * sv / nn
        ok = (n >= 3) & (vx > 0) & (vv > 0)
        out[g0:g0 + chunk] = np.where(ok, cov / np.sqrt(np.where(ok, vx * vv, 1.0)), np.nan)
    return out


def _dd_gene_scale(wells, fxd, Dn, gK):
    """Drug-doses x genes: the mean over the drug-dose's used wells of the gene's z divisor (plate_scale_gene.npy row
    of the well's plate group; 1 without a group) - atlas_core.FX.gene_plate_scale for every gene at once."""
    N = len(wells)
    ddr = wells["drugdose_row"].to_numpy(dtype=np.int64)
    m = wells["used_in_drugdose"].to_numpy(dtype=bool) & (ddr >= 0)
    nw = np.bincount(ddr[m], minlength=Dn).astype(np.float64)
    agg = sp.csr_matrix((1.0 / nw[ddr[m]], (ddr[m], np.flatnonzero(m))), shape=(Dn, N))
    p = os.path.join(fxd, "plate_scale_gene.npy")
    if "plate_scale_group_id" in wells and os.path.exists(p):
        gid = wells["plate_scale_group_id"].to_numpy(dtype=np.int64)
        FG = np.load(p, mmap_mode="r")
        fw = np.ones((N, gK), dtype=np.float32)
        ok = gid >= 0
        fw[ok] = np.asarray(FG[:, :gK], dtype=np.float32)[gid[ok]]
    else:
        f = wells["plate_scale"].to_numpy(dtype=np.float32) if "plate_scale" in wells else np.ones(N, np.float32)
        fw = np.repeat(f[:, None], gK, axis=1)
    out = np.asarray(agg @ fw, dtype=np.float32)
    out[nw == 0] = 1.0
    return out


def calibrate_line_z(DZ, z, clean, measured, chunk):
    """The per-line |z| cut t (module docstring, 'Per-line significance'). DZ = tensor DDL_z (genes x drug-doses x
    lines), z = pooled DD_z and clean = clean matrix (drug-doses x genes), measured = tensor line_measured (lines x
    genes). Null = per-line z of the (gene, clean drug-dose) pairs with pooled |z| < NULL_POOLED_Z, over up to
    CAL_MAX_GENES evenly spaced genes. Returns the dict stored in tables/info.json."""
    gK = z.shape[1]
    gsel = np.unique(np.linspace(0, gK - 1, min(gK, CAL_MAX_GENES)).round().astype(np.int64))
    nb = int(round(CAL_Z_MAX / CAL_STEP)) + 1
    h_pos = np.zeros(nb, dtype=np.int64)                         # histogram of z >= 0 by floor(z / CAL_STEP)
    h_neg = np.zeros(nb, dtype=np.int64)                         # the same for -z, z < 0
    for i in range(0, gsel.size, chunk):
        gs = gsel[i:i + chunk]
        Zl = np.asarray(DZ[gs], dtype=np.float32)                # genes x drug-doses x lines
        null = (clean[:, gs] & (np.abs(z[:, gs]) < NULL_POOLED_Z)).T[:, :, None] & measured[:, gs].T[:, None, :]
        v = Zl[null & np.isfinite(Zl)]
        b = np.minimum((np.abs(v) / CAL_STEP).astype(np.int64), nb - 1)
        h_pos += np.bincount(b[v >= 0], minlength=nb)
        h_neg += np.bincount(b[v < 0], minlength=nb)
        del Zl, null, v, b
    n = int(h_pos.sum() + h_neg.sum())
    n_clean = int(np.median(clean.sum(axis=0))) if gK else 0      # clean drug-doses of the typical gene
    grid = np.round(np.arange(nb) * CAL_STEP, 6)

    def tail(h):                                                 # P(value >= grid[k]) for every k
        return np.cumsum(h[::-1])[::-1] / max(n, 1)

    p_abs, p_up, p_dn = tail(h_pos + h_neg), tail(h_pos), tail(h_neg)
    ok = np.flatnonzero((grid >= LINE_Z_FLOOR) & (p_abs * n_clean <= LINE_CHANCE_MAX))
    k = int(ok[0]) if ok.size else nb - 1
    if n == 0:
        k = int(np.searchsorted(grid, LINE_Z_FLOOR))
    t = float(grid[k])

    def at(pp):                                                  # the tail at a few round values, for the docs
        return {f"{x:g}": (float(pp[int(np.searchsorted(grid, x))]) if n else None) for x in (2, 3, 4, 5, 6, 8, 10)}
    k2 = int(np.searchsorted(grid, LINE_Z))
    return {"line_z_threshold": t, "line_fold_min": STRONG_LFC,
            "line_z_expected_chance": float(p_abs[k] * n_clean) if n else None,
            "line_z_expected_chance_all": float(p_abs[k] * z.shape[0]) if n else None,
            "line_z_method": (f"smallest |z| on a {CAL_STEP:g} grid, >= {LINE_Z_FLOOR:g}, with P(|per-line z| >= t) x "
                              f"(clean drug-doses of the typical gene, {n_clean}) <= {LINE_CHANCE_MAX:g}; null = "
                              f"per-line z of (gene, clean drug-dose) pairs with pooled |z| < {NULL_POOLED_Z:g} in "
                              f"{gsel.size} evenly spaced genes ({n:,} values); both directions counted"),
            "line_z_n_clean_drugdoses": n_clean, "line_z_null_values": n, "line_z_null_genes": int(gsel.size),
            "line_z_null_tail": at(p_abs), "line_z_null_tail_up": at(p_up), "line_z_null_tail_down": at(p_dn),
            "lines_up_chance_rate": float(p_up[k2]) if n else None,
            "lines_down_chance_rate": float(p_dn[k2]) if n else None,
            "lines_up_rule": f"descriptive: per-line z >= {LINE_Z:g} and fold >= 1.2 (drug_effects n_lines_up)"}


def _z_gap(Zc, comp):
    """Per gene (column of Zc, rows = drug-doses, -inf = not eligible): the best z minus the best z of any other
    compound (NaN unless two compounds have a value)."""
    order = np.argsort(comp, kind="stable")
    cs = comp[order]
    starts = np.flatnonzero(np.r_[True, cs[1:] != cs[:-1]])
    if starts.size < 2:
        return np.full(Zc.shape[1], np.nan, dtype=np.float32)
    M = np.maximum.reduceat(Zc[order], starts, axis=0)
    P = np.partition(-M, 1, axis=0)[:2]
    t1, t2 = -P[0], -P[1]
    return np.where(np.isfinite(t1) & np.isfinite(t2), t1 - t2, np.nan).astype(np.float32)


def _line_lists(names, V, M, sign, cap=MAX_LINES_LISTED):
    """Per row: the names of the lines where M holds, strongest (sign * V largest) first, at most cap, ', '-joined."""
    S = np.where(M, sign * V, -np.inf)
    k = min(cap, S.shape[1])
    o = np.argsort(-S, axis=1, kind="stable")[:, :k]
    cnt = np.minimum(M.sum(axis=1), k)
    nm = names[o]
    out = np.full(len(S), "", dtype=object)
    for i in np.flatnonzero(cnt):
        out[i] = ", ".join(nm[i, :cnt[i]])
    return out


def _top_k(S, k):
    """Per row of S: column indices of the k largest finite values, largest first, and the values (-inf = none)."""
    k = min(k, S.shape[1])
    part = np.argpartition(-S, k - 1, axis=1)[:, :k]
    vals = np.take_along_axis(S, part, axis=1)
    o = np.argsort(-vals, axis=1, kind="stable")
    return np.take_along_axis(part, o, axis=1), np.take_along_axis(vals, o, axis=1)


def _ext(arr, fill=None):
    """arr with one extra element (fill) at the end, so that index -1 ... is mapped to it via np.where(i < 0, n, i)."""
    a = np.asarray(arr, dtype=object)
    return np.append(a, np.array([fill], dtype=object))


def _pick(arr, idx, fill=None):
    idx = np.asarray(idx)
    return _ext(arr, fill)[np.where(idx < 0, len(arr), idx)]


def _well_key(w):
    s = T.slot_from_well(w)
    return (s if np.isfinite(s) else 999.0, str(w))


def _write_text(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    replace_file(tmp, path)


def _file_index(atl):
    p = os.path.join(atl, "file_index.json")
    if not os.path.exists(p):
        return {}
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _read_meta(fi, key, cols):
    files = [f for f in fi.get(key, []) or [] if os.path.exists(f)]
    if not files:
        return None
    try:
        return T.read_tables(files, cols)
    except Exception as e:  # noqa: BLE001  (metadata is optional: log and go on)
        log(f"  could not read the {key} metadata ({e}); going on without it")
        return None


def _tp53_status(lines, fi):
    """'altered' (a TP53 row in the cell-line metadata), 'wild type' (the line is there without one), 'unknown'."""
    cl = _read_meta(fi, "cell_line", ["Cell_ID_Cellosaur", "Driver_Gene_Symbol"])
    ids = lines["cell_line_id"].astype(str)
    if cl is not None and "Cell_ID_Cellosaur" in cl and "Driver_Gene_Symbol" in cl:
        cid = cl["Cell_ID_Cellosaur"].astype(str)
        present = set(cid)
        altered = set(cid[cl["Driver_Gene_Symbol"].astype(str).str.strip().str.upper() == "TP53"])
        return np.where(ids.isin(altered), "altered", np.where(ids.isin(present), "wild type", "unknown")), "metadata"
    drv = lines["drivers"].fillna("").astype(str) if "drivers" in lines else pd.Series([""] * len(lines))
    st = np.where(drv.str.contains(r"(?:^|; )TP53\(", regex=True), "altered",
                  np.where(drv.str.len() > 0, "wild type", "unknown"))
    return st, "lines.csv drivers"


def _lowest_active(doses, nsig, min_genes=MIN_ACTIVE_GENES):
    """The lowest dose such that it and every higher dose have >= min_genes significant genes (ascending conc);
    'low dose only (noise?)' when only lower doses do; '' when no dose does (as the old atlas drug summary)."""
    act = np.asarray(nsig) >= min_genes
    if not act.any():
        return ""
    if not act[-1]:
        return "low dose only (noise?)"
    k = len(act) - 1
    while k > 0 and act[k - 1]:
        k -= 1
    return str(doses[k])


# ----------------------------------------------------------------------------- schema of the streamed table
DRUG_EFFECTS_SCHEMA = pa.schema([
    ("col", pa.int32()), ("symbol", pa.string()), ("dd", pa.int32()), ("drug", pa.string()), ("dose", pa.string()),
    ("conc", pa.float64()), ("lfc", pa.float32()), ("fold", pa.float32()), ("z", pa.float32()),
    ("q_up", pa.float32()), ("q_down", pa.float32()), ("flags", pa.string()), ("clean", pa.bool_()),
    ("n_lines_measured", pa.int16()), ("n_lines_up", pa.int16()), ("n_lines_down", pa.int16()),
    ("lines_up", pa.string()), ("lines_down", pa.string()), ("pattern_up", pa.string()),
    ("pattern_down", pa.string()), ("cc_share", pa.float32())])


# ----------------------------------------------------------------------------- the stage
def run(out, chunk=None, mem_gb=1.5):
    """out = the tahoemap output folder (atlas in out/atlas, tensor in out/tensor). Writes out/tables/.
    chunk = genes per block of the per-line tensor (default: sized so one block's work stays near mem_gb GB)."""
    t0 = time.time()
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        info = _run(out, chunk, mem_gb, t0)
    stamp_stage(out, "tables", VERSION, info)
    log(f"Tables done -> {os.path.join(out, 'tables')} ({info['minutes']} min)")
    return info


def _run(out, chunk, mem_gb, t0):
    atl = os.path.join(out, "atlas")
    fxd = os.path.join(atl, "effects")
    tdir = os.path.join(out, "tensor")
    od = os.path.join(out, "tables")
    os.makedirs(od, exist_ok=True)
    ix = read_effects_index(fxd)
    genes, wells, dd, lines = ix["genes"], ix["wells"], ix["drugdose"].copy(), ix["lines"].copy()
    gK = int((genes["kind"] == "gene").sum())
    Dn, L, N = len(dd), len(lines), len(wells)
    fi = _file_index(atl)
    unreliable = list(ix["info"].get("unreliable_plates", []))
    for p in ("DDL_z.npy", "DDL_lfc.npy"):
        if not os.path.exists(os.path.join(tdir, p)):
            raise SystemExit(f"tables: {os.path.join(tdir, p)} is missing; run the 'tensor' stage first")
    DZ = np.load(os.path.join(tdir, "DDL_z.npy"), mmap_mode="r")
    DL = np.load(os.path.join(tdir, "DDL_lfc.npy"), mmap_mode="r")
    if DZ.shape != (gK, Dn, L) or DL.shape != (gK, Dn, L):
        raise SystemExit(f"tables: tensor shape {DZ.shape} does not match the effects ({gK}, {Dn}, {L}); "
                         "rerun 'tensor'")
    log(f"Tables: {gK:,} genes x {Dn:,} drug-doses x {L} lines ({N:,} wells)")
    line_cpm = np.load(os.path.join(fxd, "line_cpm.npy"), mmap_mode="r")
    expr = np.load(os.path.join(fxd, "expr_mask.npy"), mmap_mode="r")
    p = os.path.join(tdir, "line_measured.npy")
    if os.path.exists(p) and np.load(p, mmap_mode="r").shape == (L, gK):
        measured = np.asarray(np.load(p), dtype=bool)          # lines x genes: the line truly expresses the gene
    else:                                                      # an older tensor: the same rule, applied here
        measured = measured_mask(expr[:, :gK], line_cpm[:, :gK], genes["pooled_cpm"].to_numpy()[:gK])
        log(f"  {p} missing (tensor from an older version): ambient-only lines (< {AMB_FRAC:g} x the pooled CPM) "
            "are masked here; low-count profiles are not - rerun 'tensor'")

    # ---- index vectors
    gsub = genes.iloc[:gK]
    label = gsub["label"].fillna("").astype(str).to_numpy(dtype=object)
    symbol = gsub["symbol"].fillna("").astype(str).to_numpy(dtype=object)
    symbol = np.where(symbol == "", label, symbol)
    names = lines["cell_name"].fillna("").astype(str) if "cell_name" in lines else lines["cell_line_id"]
    line_name = np.where(names == "", lines["cell_line_id"].astype(str), names).astype(object)
    line_id = lines["cell_line_id"].astype(str).to_numpy(dtype=object)
    dd_drug = dd["drug"].astype(str).to_numpy(dtype=object)
    dd_dose = dd["dose"].astype(str).to_numpy(dtype=object)
    dd_conc = dd["conc"].to_numpy(dtype=np.float64)
    dd_flags = dd["flags"].fillna("").astype(str).to_numpy(dtype=object)
    art_dd = np.array([A.has_artifact(f) for f in dd_flags], dtype=bool)
    drugs = list(dict.fromkeys(dd_drug))                       # first-seen order of drugdose.csv (sorted by drug)
    drug_ix = {d: i for i, d in enumerate(drugs)}
    drug_of_dd = np.array([drug_ix[d] for d in dd_drug], dtype=np.int64)
    rows_of_drug = [np.flatnonzero(drug_of_dd == i) for i in range(len(drugs))]
    rows_of_drug = [r[np.argsort(dd_conc[r], kind="stable")] for r in rows_of_drug]
    m_dose = max(len(r) for r in rows_of_drug)
    grid = np.full((len(drugs), m_dose), -1, dtype=np.int64)  # drugs x doses (ascending conc), -1 = none
    for i, r in enumerate(rows_of_drug):
        grid[i, :len(r)] = r
    salt = np.array([T.salt_base(d) for d in dd_drug], dtype=object)
    comp_ix = {c: i for i, c in enumerate(dict.fromkeys(salt))}
    comp_of_dd = np.array([comp_ix[c] for c in salt], dtype=np.int64)

    # ---- pooled drug-dose x gene matrices (gene columns only)
    def load(name, dtype=np.float32):
        return np.array(np.load(os.path.join(fxd, f"{name}.npy"), mmap_mode="r")[:, :gK], dtype=dtype)

    lfc, z, qu, qd = load("DD_lfc"), load("DD_z"), load("DD_qup"), load("DD_qdn")
    pe = load("DD_poseff") if os.path.exists(os.path.join(fxd, "DD_poseff.npy")) else np.zeros((Dn, gK), np.float32)
    pu = load("DD_posunc", bool) if os.path.exists(os.path.join(fxd, "DD_posunc.npy")) \
        else np.zeros((Dn, gK), dtype=bool)
    ps = _dd_gene_scale(wells, fxd, Dn, gK)
    sig_up = (qu < Q_CUT) & (lfc >= LFC_MIN)
    sig_dn = (qd < Q_CUT) & (lfc <= -LFC_MIN)
    s_col, g_col = (f"{m}_lfc" for m in CC_MODULES)
    nanv = np.full(Dn, np.nan)
    cc_dd, cc_share, cc_clear, cc_bS, cc_bG, cc_fit = cell_cycle_share(
        lfc, dd[s_col].to_numpy(dtype=np.float64) if s_col in dd else nanv,
        dd[g_col].to_numpy(dtype=np.float64) if g_col in dd else nanv, dd_flags, pu)
    cc_only = np.array([set(f.split("; ")) & set(A.ARTIFACT_FLAGS) == {CC_FLAG} for f in dd_flags], dtype=bool)
    # clean = no artifact flag for this gene: the drug-dose's flags (its cell-cycle shift only where the shift is the
    # explanation of this gene's change) + this gene's position flag
    clean = (~art_dd[:, None] | (cc_only[:, None] & cc_clear)) & ~pu
    finz = np.isfinite(z)

    def cc_pct(d, g):
        """flag_strings' cc_pct for (drug-dose, gene) items: round(100 x share) where cleared, else -1."""
        return np.where(cc_clear[d, g], np.rint(100.0 * np.nan_to_num(cc_share[d, g])), -1).astype(np.int64)

    cc_info = _cc_summary(ix["genes"], fxd, gK, cc_dd, cc_only, cc_share, cc_clear, lfc, sig_up | sig_dn, cc_bS,
                          cc_bG, cc_fit)
    log(f"  pooled: {int(sig_up.sum()):,} significant gene x drug-dose increases, {int(sig_dn.sum()):,} decreases; "
        f"{int((~art_dd).sum()):,} of {Dn:,} drug-doses without an artifact flag")
    log(f"  cell-cycle shift: {int(cc_dd.sum()):,} drug-doses flagged, {int(cc_only.sum()):,} with no other "
        f"artifact flag; slopes on the S / G2M modules fitted over {cc_fit:,} drug-doses (doubled for the rule); of "
        f"{cc_info['significant_at_cc_only']:,} significant changes at the latter the shift is not the explanation "
        f"of {cc_info['cleared_at_cc_only']:,} (clean for that gene; with the fitted slopes as they are: "
        f"{cc_info['cleared_at_cc_only_x1']:,})")
    for m, v in cc_info["module_genes"].items():
        log(f"    check: {m} module genes ({v['genes']}): {v['significant_at_cc']:,} significant changes at "
            f"cell-cycle-flagged drug-doses, {v['cleared']:,} of them cleared")

    # ---- dose patterns per (drug, gene), both signs
    P_up = np.zeros((len(drugs), gK), dtype=np.int8)
    P_dn = np.zeros((len(drugs), gK), dtype=np.int8)
    gsafe = np.maximum(grid, 0)
    for g0 in range(0, gK, 2048):
        g1 = min(gK, g0 + 2048)
        V = z[:, g0:g1][gsafe].astype(np.float64)                 # drugs x doses x genes
        V[grid < 0] = np.nan
        V = V.transpose(0, 2, 1).reshape(-1, m_dose)
        P_up[:, g0:g1] = dose_shape_codes(V).reshape(len(drugs), g1 - g0)
        P_dn[:, g0:g1] = dose_shape_codes(-V).reshape(len(drugs), g1 - g0)
    del V

    # ---- per-gene pooled summary (genes.parquet, without the per-line counts)
    cols = np.arange(gK)
    gtab = pd.DataFrame({"col": cols.astype(np.int32), "symbol": symbol, "label": label})
    ens = pd.Series([""] * gK, dtype=object)
    gm = _read_meta(fi, "gene", ["token_id", "gene_symbol", "ensembl_id"])
    if gm is not None and {"token_id", "ensembl_id"} <= set(gm.columns):
        emap = gm.dropna(subset=["token_id"]).drop_duplicates("token_id").set_index("token_id")["ensembl_id"]
        ens = gsub["token"].map(emap).fillna("").astype(str).reset_index(drop=True)
    else:
        log("  gene metadata not found: ensembl_id left empty")
    gtab["ensembl_id"] = ens.to_numpy(dtype=object)
    gtab["token"] = gsub["token"].to_numpy(dtype=np.int64)
    for c in ("pooled_cpm", "median_line_cpm"):
        gtab[c] = gsub[c].to_numpy()
    gtab["n_lines_expressing"] = measured.sum(axis=0).astype(np.int32)    # tensor line_measured, not the atlas's
    gtab["noise_rna"] = [bool(A.NOISE_RNA_RE.match(s)) for s in symbol]
    W2 = np.load(os.path.join(fxd, "W2.npy"), mmap_mode="r")
    dw = np.flatnonzero(~wells["is_dmso"].to_numpy(dtype=bool))
    Wd = np.asarray(W2[dw], dtype=np.float32)
    mod_col = {s: int(c) for s, c, k in zip(genes["symbol"], genes["col"], genes["kind"]) if k == "module"}
    for name, mod in (("corr_with_S", "S_PHASE"), ("corr_with_G2M", "G2M_PHASE")):
        gtab[name] = _corr_with(Wd[:, :gK], Wd[:, mod_col[mod]]) if mod in mod_col else np.nan
    del Wd
    gtab["n_dd_up"] = sig_up.sum(axis=0).astype(np.int32)
    gtab["n_dd_down"] = sig_dn.sum(axis=0).astype(np.int32)
    gtab["n_dd_up_clean"] = (sig_up & clean).sum(axis=0).astype(np.int32)
    gtab["n_dd_down_clean"] = (sig_dn & clean).sum(axis=0).astype(np.int32)

    def best(S):
        b = np.argmax(S, axis=0)
        return np.where(np.isfinite(S[b, cols]), b, -1)

    bu = best(np.where(finz, z, -np.inf))
    bd = best(np.where(finz, -z, -np.inf))
    Zc_up = np.where(finz & clean, z, -np.inf)
    bcu = best(Zc_up)
    up_gap = _z_gap(Zc_up, comp_of_dd)
    del Zc_up
    Zc_dn = np.where(finz & clean, -z, -np.inf)
    bcd = best(Zc_dn)
    dn_gap = _z_gap(Zc_dn, comp_of_dd)
    del Zc_dn

    def best_cols(prefix, b, q):
        ok = b >= 0
        bb = np.maximum(b, 0)
        v = {f"{prefix}_dd": b.astype(np.int32), f"{prefix}_drug": _pick(dd_drug, b),
             f"{prefix}_dose": _pick(dd_dose, b),
             f"{prefix}_fold": np.where(ok, 2.0 ** lfc[bb, cols], np.nan).astype(np.float32),
             f"{prefix}_z": np.where(ok, z[bb, cols], np.nan).astype(np.float32),
             f"{prefix}_q": np.where(ok, q[bb, cols], np.nan).astype(np.float32)}
        fl = np.full(gK, None, dtype=object)
        fl[ok] = flag_strings(dd_flags, b[ok], pu[b[ok], cols[ok]], pe[b[ok], cols[ok]], ps[b[ok], cols[ok]],
                              cc_pct(b[ok], cols[ok]))[0]
        v[f"{prefix}_flags"] = fl
        return v

    for prefix, b, q in (("best_up", bu, qu), ("best_down", bd, qd)):
        for k, v in best_cols(prefix, b, q).items():
            gtab[k] = v
    bcu_nl = np.full(gK, -1, dtype=np.int32)                   # filled from the tensor below
    bcd_nl = np.full(gK, -1, dtype=np.int32)

    # ---- the per-line tensor, in gene chunks
    if not chunk:
        chunk = max(1, min(gK, int(mem_gb * 1e9 / (48.0 * Dn * L))))
    cal = calibrate_line_z(DZ, z, clean, measured, chunk)
    t_line = cal["line_z_threshold"]
    log(f"  per-line |z| cut: {t_line:g} (expected chance passes per gene x line over the "
        f"{cal['line_z_n_clean_drugdoses']} clean drug-doses: {cal['line_z_expected_chance']}; null P(|z| >= 3) = "
        f"{cal['line_z_null_tail'].get('3')}, P(|z| >= 4) = {cal['line_z_null_tail'].get('4')})")
    keep = (np.abs(z) >= KEEP_Z) | (qu < Q_CUT) | (qd < Q_CUT)
    log(f"  drug_effects: {int(keep.sum()):,} gene x drug-dose rows (|z| >= {KEEP_Z:g} or q < {Q_CUT:g}); "
        f"per-line tensor in chunks of {chunk} genes ...")
    sd_l = np.full((gK, L), np.nan, dtype=np.float32)

    def per_line():                                            # counts and the strongest per (gene, line)
        return {"n": np.zeros((gK, L), dtype=np.int16), "b": np.full((gK, L), -1, dtype=np.int32),
                "x": np.full((gK, L), np.nan, dtype=np.float32), "z": np.full((gK, L), np.nan, dtype=np.float32)}
    PL = {(scope, sign): per_line() for scope in ("clean", "all") for sign in (1, -1)}
    tops = []
    fx_path = os.path.join(od, "drug_effects.parquet")
    writer = pq.ParquetWriter(fx_path + ".tmp", DRUG_EFFECTS_SCHEMA)
    n_fx, n_clean_rows, mismatch = 0, 0, 0
    try:
        for g0 in range(0, gK, chunk):
            g1 = min(gK, g0 + chunk)
            c = g1 - g0
            loc = np.arange(c)
            Z = np.asarray(DZ[g0:g1], dtype=np.float32)          # genes x drug-doses x lines
            X = np.asarray(DL[g0:g1], dtype=np.float32)
            meas = measured[:, g0:g1].T[:, None, :]                 # genes x 1 x lines (the tensor's NaN already)
            Z = np.where(meas, Z, np.nan)
            X = np.where(meas, X, np.nan)
            upl = (Z >= LINE_Z) & (X >= LFC_MIN)
            dnl = (Z <= -LINE_Z) & (X <= -LFC_MIN)
            n_meas = np.isfinite(Z).sum(axis=2).astype(np.int16)
            n_up = upl.sum(axis=2).astype(np.int16)
            n_dn = dnl.sum(axis=2).astype(np.int16)
            for b, dst, nn in ((bcu, bcu_nl, n_up), (bcd, bcd_nl, n_dn)):
                bb = b[g0:g1]
                ok = bb >= 0
                dst[g0:g1][ok] = nn[loc[ok], bb[ok]]

            # drug_effects rows of this chunk
            gi, di = np.nonzero(keep[:, g0:g1].T)
            if gi.size:
                g = g0 + gi
                fl, cl_s = flag_strings(dd_flags, di, pu[di, g], pe[di, g], ps[di, g], cc_pct(di, g))
                mismatch += int((cl_s != clean[di, g]).sum())
                Zs = Z[gi, di]
                order = np.lexsort((-z[di, g], g))
                lf = lfc[di, g]
                part = pd.DataFrame({
                    "col": g.astype(np.int32), "symbol": symbol[g], "dd": di.astype(np.int32), "drug": dd_drug[di],
                    "dose": dd_dose[di], "conc": dd_conc[di], "lfc": lf, "fold": (2.0 ** lf).astype(np.float32),
                    "z": z[di, g], "q_up": qu[di, g], "q_down": qd[di, g], "flags": fl, "clean": cl_s,
                    "n_lines_measured": n_meas[gi, di], "n_lines_up": n_up[gi, di], "n_lines_down": n_dn[gi, di],
                    "lines_up": _line_lists(line_name, Zs, upl[gi, di], 1),
                    "lines_down": _line_lists(line_name, Zs, dnl[gi, di], -1),
                    "pattern_up": _PAT[P_up[drug_of_dd[di], g]], "pattern_down": _PAT[P_dn[drug_of_dd[di], g]],
                    "cc_share": cc_share[di, g]})
                part = part.iloc[order]
                writer.write_table(pa.Table.from_pandas(part, schema=DRUG_EFFECTS_SCHEMA, preserve_index=False))
                n_fx += len(part)
                n_clean_rows += int(cl_s.sum())
                del part, Zs
            del upl, dnl

            # line_effects: response_sd over the clean drug-doses (the typical spread of a gene's responses in a line:
            # an estimate, so artifacts stay out of it); counts and the strongest over the clean ones and over all
            cl = clean[:, g0:g1].T[:, :, None]                      # genes x drug-doses x 1
            Xc = np.where(cl, X, np.nan).transpose(0, 2, 1)         # genes x lines x drug-doses
            med, k = _nanmedian_last(Xc)
            mad, _ = _nanmedian_last(np.abs(Xc - med[..., None]))
            sd_l[g0:g1] = np.where(k >= MIN_SD_DD, 1.4826 * mad, np.nan)
            del Xc
            for sign in (1, -1):
                sZ = sign * Z
                passz = sZ >= t_line                                 # per-line z beyond the calibrated cut
                hit = passz & (sign * X >= STRONG_LFC)               # ... and fold >= 1.5 that way
                for scope, M in (("all", hit), ("clean", hit & cl)):
                    d_ = PL[(scope, sign)]
                    d_["n"][g0:g1] = M.sum(axis=1)
                    S = np.where(M, sZ, -np.inf)                     # best_*: the strongest of those counted
                    b = S.argmax(axis=1)                             # genes x lines
                    ok = np.isfinite(np.take_along_axis(S, b[:, None, :], axis=1)[:, 0, :])
                    d_["b"][g0:g1] = np.where(ok, b, -1)
                    d_["z"][g0:g1] = np.where(ok, np.take_along_axis(Z, b[:, None, :], axis=1)[:, 0, :], np.nan)
                    d_["x"][g0:g1] = np.where(ok, np.take_along_axis(X, b[:, None, :], axis=1)[:, 0, :], np.nan)
                    del S, M
                del hit
                # drug_line_top: the strongest (drug-dose, line) cells with per-line |z| >= t over all drug-doses,
                # plus any of the strongest clean ones that fall outside them (with their rank over all)
                F = np.where(passz, sZ, -np.inf).reshape(c, Dn * L)
                idx, vals = _top_k(F, TOP_CELLS)
                idc, vlc = _top_k(np.where(passz & cl, sZ, -np.inf).reshape(c, Dn * L), TOP_CELLS)
                new = np.isfinite(vlc) & ~(idc[:, :, None] == idx[:, None, :]).any(axis=2)
                rk = np.zeros(idc.shape, dtype=np.int64)
                for j in range(idc.shape[1]):
                    m = new[:, j]
                    if m.any():
                        rk[m, j] = np.maximum(idx.shape[1] + 1, 1 + (F[m] > vlc[m, j][:, None]).sum(axis=1))
                r_, k_ = np.nonzero(np.isfinite(vals))
                rr, kk = np.nonzero(new)
                rows_g = np.r_[r_, rr]
                flat = np.r_[idx[r_, k_], idc[rr, kk]]
                if rows_g.size:
                    tops.append((g0 + rows_g, np.full(rows_g.size, sign, np.int8), np.r_[k_ + 1, rk[rr, kk]],
                                 flat // L, flat % L, X.reshape(c, -1)[rows_g, flat], Z.reshape(c, -1)[rows_g, flat]))
                del F, passz, sZ, idc, vlc, new
            del Z, X, meas
            if (g0 // chunk) % 10 == 0 or g1 == gK:
                log(f"    genes {g0:,}-{g1:,} of {gK:,} ({(time.time() - t0) / 60:.1f} min; drug_effects rows "
                    f"{n_fx:,})")
    finally:
        writer.close()
    replace_file(fx_path + ".tmp", fx_path)

    # ---- genes.parquet
    for prefix, b, q, nl, nlname, P in (("best_clean_up", bcu, qu, bcu_nl, "n_lines_up", P_up),
                                        ("best_clean_down", bcd, qd, bcd_nl, "n_lines_down", P_dn)):
        for k, v in best_cols(prefix, b, q).items():
            gtab[k] = v
        gtab[f"{prefix}_{nlname}"] = np.where(b >= 0, nl, -1).astype(np.int32)
        gtab[f"{prefix}_pattern"] = np.where(b >= 0, _PAT[P[drug_of_dd[np.maximum(b, 0)], cols]], None)
    gtab["up_specificity_z_gap"] = up_gap
    gtab["down_specificity_z_gap"] = dn_gap
    gtab["cc_slope_S"] = cc_bS
    gtab["cc_slope_G2M"] = cc_bG
    write_parquet(gtab, os.path.join(od, "genes.parquet"))

    # ---- line_effects.parquet
    gg = np.repeat(cols, L)
    ll = np.tile(np.arange(L), gK)
    le = pd.DataFrame({"col": gg.astype(np.int32), "symbol": symbol[gg], "line": ll.astype(np.int16),
                       "cell_line_id": line_id[ll], "cell_name": line_name[ll],
                       "baseline_cpm": np.asarray(line_cpm[:, :gK], dtype=np.float32).T.ravel(),
                       "expressed": measured.T.ravel(), "response_sd": sd_l.ravel(),
                       "n_dd_up": PL[("clean", 1)]["n"].ravel(), "n_dd_down": PL[("clean", -1)]["n"].ravel()})
    for prefix, sign in (("best_up", 1), ("best_down", -1)):
        d_ = PL[("clean", sign)]
        b = d_["b"].ravel()
        le[f"{prefix}_dd"] = b
        le[f"{prefix}_drug"] = _pick(dd_drug, b)
        le[f"{prefix}_dose"] = _pick(dd_dose, b)
        le[f"{prefix}_lfc"] = d_["x"].ravel()
        le[f"{prefix}_z"] = d_["z"].ravel()
    le["n_dd_up_all"] = PL[("all", 1)]["n"].ravel()
    le["n_dd_down_all"] = PL[("all", -1)]["n"].ravel()
    for prefix, sign in (("best_up", 1), ("best_down", -1)):
        d_ = PL[("all", sign)]
        b = d_["b"].ravel()
        ok = b >= 0
        fl = np.full(b.size, None, dtype=object)
        cl_a = np.zeros(b.size, dtype=bool)
        bo, go = b[ok], gg[ok]
        fl[ok], cl_a[ok] = flag_strings(dd_flags, bo, pu[bo, go], pe[bo, go], ps[bo, go], cc_pct(bo, go))
        mismatch += int((cl_a[ok] != clean[bo, go]).sum())
        le[f"{prefix}_dd_all"] = b
        le[f"{prefix}_drug_all"] = _pick(dd_drug, b)
        le[f"{prefix}_dose_all"] = _pick(dd_dose, b)
        le[f"{prefix}_lfc_all"] = d_["x"].ravel()
        le[f"{prefix}_z_all"] = d_["z"].ravel()
        le[f"{prefix}_flags_all"] = fl
        le[f"{prefix}_clean_all"] = cl_a
        le[f"{prefix}_cc_share_all"] = np.where(ok, cc_share[np.maximum(b, 0), gg], np.nan).astype(np.float32)
    write_parquet(le, os.path.join(od, "line_effects.parquet"))
    n_le = len(le)
    le_cols = list(le.columns)
    del le, sd_l, PL

    # ---- drug_line_top.parquet
    if tops:
        tg, ts, tr, td, tl, tx, tz = (np.concatenate(a) for a in zip(*tops))
    else:
        tg = ts = tr = td = tl = np.zeros(0, dtype=np.int64)
        tx = tz = np.zeros(0, dtype=np.float32)
    o = np.lexsort((tr, -ts, tg))
    tg, ts, tr, td, tl, tx, tz = (a[o] for a in (tg, ts, tr, td, tl, tx, tz))
    tf, tc = flag_strings(dd_flags, td, pu[td, tg], pe[td, tg], ps[td, tg], cc_pct(td, tg))
    mismatch += int((tc != clean[td, tg]).sum())
    dlt = pd.DataFrame({"col": tg.astype(np.int32), "symbol": symbol[tg],
                        "direction": np.where(ts > 0, "up", "down").astype(object), "rank": tr.astype(np.int32),
                        "dd": td.astype(np.int32), "drug": dd_drug[td], "dose": dd_dose[td],
                        "line": tl.astype(np.int16), "cell_name": line_name[tl], "lfc": tx.astype(np.float32),
                        "z": tz.astype(np.float32), "pooled_lfc": lfc[td, tg], "pooled_z": z[td, tg],
                        "flags": tf, "clean": tc.astype(bool), "cc_share": cc_share[td, tg]})
    write_parquet(dlt, os.path.join(od, "drug_line_top.parquet"))
    if mismatch:
        raise SystemExit(f"tables: {mismatch} rows whose 'clean' differs between the flag strings and the clean "
                         "matrix (tables.py and atlas_core disagree on the artifact rules)")

    # ---- drugdoses.parquet
    ddt = dd.copy()
    ddt.insert(0, "dd", np.arange(Dn, dtype=np.int32))
    ddt.insert(3, "salt_base", salt)
    for name, sig, sign in (("top_up", sig_up, 1), ("top_down", sig_dn, -1)):
        idx, vals = _top_k(np.where(sig & finz, sign * z, -np.inf), TOP_GENES)
        ddt[name] = ["; ".join(f"{label[g]} ({2.0 ** float(lfc[d, g]):.2f}x)"
                               for g, v in zip(idx[d], vals[d]) if np.isfinite(v)) for d in range(Dn)]
    write_parquet(ddt, os.path.join(od, "drugdoses.parquet"))

    # ---- drugs.parquet
    nsig = dd["n_sig_genes"].to_numpy(dtype=np.int64) if "n_sig_genes" in dd else (sig_up | sig_dn).sum(axis=1)
    resp = np.flatnonzero((sig_up | sig_dn).sum(axis=0) >= RESPONSIVE_MIN_DD)
    if resp.size < 50:
        resp = cols
    zr = np.nan_to_num(z[:, resp].astype(np.float64))
    nrm = np.linalg.norm(zr, axis=1)
    nrm[nrm == 0] = 1.0

    def meta(col, i):
        return str(dd[col].iloc[i]) if col in dd and pd.notna(dd[col].iloc[i]) else ""

    drows = []
    for name in sorted(drugs):
        r = rows_of_drug[drug_ix[name]]
        ns = nsig[r]
        bi = r[np.lexsort((-dd_conc[r], -ns))[0]]               # most significant genes; tie -> higher dose
        sim = [float(zr[a] @ zr[b] / (nrm[a] * nrm[b])) for a, b in zip(r[:-1], r[1:])]
        drows.append({"drug": name, "salt_base": T.salt_base(name), "targets": meta("targets", r[0]),
                      "moa_fine": meta("moa_fine", r[0]), "moa_broad": meta("moa_broad", r[0]),
                      "approved": meta("approved", r[0]), "n_doses": int(len(r)),
                      "doses": " / ".join(dd_dose[r]), "n_sig_by_dose": " / ".join(str(int(x)) for x in ns),
                      "max_sig": int(ns.max()), "best_dose": dd_dose[bi], "best_dd": int(bi),
                      "lowest_active_dose": _lowest_active(dd_dose[r], ns),
                      "flags_by_dose": " / ".join(f or "-" for f in dd_flags[r]),
                      "signature_r_between_doses": T.fmt_list(sim)})
    del zr
    drugs_df = pd.DataFrame(drows)
    write_parquet(drugs_df, os.path.join(od, "drugs.parquet"))

    # ---- lines.parquet
    tp53, tp53_src = _tp53_status(lines, fi)
    lt = lines.copy()
    lt.insert(0, "line", np.arange(L, dtype=np.int16))
    lt["tp53_status"] = tp53
    p = os.path.join(fxd, "DD_Az.npy")
    if os.path.exists(p):
        Az = np.load(p)                                          # drug-doses x lines (NaN: not measured)
        in_ga = (lines["in_growth_analysis"].astype(str).str.lower().isin(["true", "1", "1.0"]).to_numpy()
                 if "in_growth_analysis" in lines else np.ones(L, dtype=bool))
        meas_l = in_ga & np.isfinite(Az).any(axis=0)
        dep = Az <= DEPLETE_Z
        untrusted = np.array([any(u in set(f.split("; ")) for u in ABUNDANCE_UNTRUSTED) for f in dd_flags], dtype=bool)
        lt["n_dd_depleted"] = np.where(meas_l, (dep & ~untrusted[:, None]).sum(axis=0), -1).astype(np.int32)
        lt["n_dd_depleted_clean"] = np.where(meas_l, (dep & ~art_dd[:, None]).sum(axis=0), -1).astype(np.int32)
        del Az, dep
    else:
        lt["n_dd_depleted"] = lt["n_dd_depleted_clean"] = np.full(L, -1, dtype=np.int32)
    p = os.path.join(fxd, "DD_beta.npy")
    lt["median_response"] = np.nanmedian(np.load(p), axis=0).astype(np.float32) if os.path.exists(p) else np.nan
    write_parquet(lt, os.path.join(od, "lines.parquet"))

    # ---- plates.parquet
    p = os.path.join(fxd, "plate_scale.csv")
    pscale = pd.read_csv(p, dtype={"plate": str}) if os.path.exists(p) else pd.DataFrame(columns=["plate", "factor"])
    p = os.path.join(fxd, "failed_wells.csv")
    failed = pd.read_csv(p, dtype={"plate": str, "well": str}) if os.path.exists(p) else pd.DataFrame()
    prow = []
    for pl in ix["plates"]["plate"].astype(str):
        w = wells[wells["plate"] == pl]
        dm = w["is_dmso"].to_numpy(dtype=bool)
        dz = w[~dm].drop_duplicates("dose").sort_values("conc")["dose"].astype(str)
        fac = pd.to_numeric(pscale.loc[pscale["plate"] == pl, "factor"], errors="coerce")
        fw = failed[failed["plate"] == pl] if len(failed) else failed
        prow.append({"plate": pl, "n_wells": int(len(w)), "n_drug_wells": int((~dm).sum()),
                     "doses": " / ".join(dz), "unreliable": pl in unreliable or bool(w["unreliable_plate"].any()),
                     "plate_factor": float(fac.max()) if fac.notna().any() else np.nan,
                     "dmso_wells": ", ".join(sorted(w.loc[dm, "well"].astype(str), key=_well_key)),
                     "n_dmso_wells": int(dm.sum()),
                     "failed_wells": ", ".join(sorted(fw["well"].astype(str), key=_well_key)) if len(fw) else "",
                     "n_failed_wells": int(len(fw)),
                     "median_cells_per_well": float(np.median(w["n_cells"])) if len(w) else np.nan})
    plates_df = pd.DataFrame(prow)
    write_parquet(plates_df, os.path.join(od, "plates.parquet"))

    # ---- wells.parquet
    wt = wells.copy()
    wt.insert(0, "w", np.arange(N, dtype=np.int32))
    p = os.path.join(tdir, "well_umi.npy")
    umi = np.load(p) if os.path.exists(p) else None
    wt["umi_total"] = umi if umi is not None and len(umi) == N else np.nan
    write_parquet(wt, os.path.join(od, "wells.parquet"))

    # ---- README.md
    tables = {"genes.parquet": list(gtab.columns), "drug_effects.parquet": DRUG_EFFECTS_SCHEMA.names,
              "line_effects.parquet": le_cols, "drug_line_top.parquet": list(dlt.columns),
              "drugdoses.parquet": list(ddt.columns), "drugs.parquet": list(drugs_df.columns),
              "lines.parquet": list(lt.columns), "plates.parquet": list(plates_df.columns),
              "wells.parquet": list(wt.columns)}
    text, undocumented = readme(tables, cal, cc_info)
    _write_text(os.path.join(od, "README.md"), text)
    if undocumented:
        log(f"  WARNING: columns without a description in README.md: {', '.join(undocumented)}")

    info = {"version": VERSION, "genes": gK, "drugdoses": Dn, "lines": L, "wells": N, "chunk": int(chunk),
            "rows": {"genes": len(gtab), "drug_effects": n_fx, "drug_effects_clean": n_clean_rows,
                     "line_effects": n_le, "drug_line_top": len(dlt), "drugdoses": len(ddt), "drugs": len(drugs_df),
                     "lines": len(lt), "plates": len(plates_df), "wells": len(wt)},
            "tp53_source": tp53_src, "tp53_counts": {str(k): int(v) for k, v in pd.Series(tp53).value_counts().items()},
            "genes_with_clean_inducer": int(((gtab["best_clean_up_q"] < Q_CUT)
                                             & (gtab["best_clean_up_fold"] >= 2 ** LFC_MIN)).sum()),
            "genes_with_clean_repressor": int(((gtab["best_clean_down_q"] < Q_CUT)
                                               & (gtab["best_clean_down_fold"] <= 2 ** -LFC_MIN)).sum()),
            "n_measured_line_gene_pairs": int(measured.sum()),
            "cell_cycle_rule": cc_info, **cal,
            "undocumented_columns": undocumented, "minutes": round((time.time() - t0) / 60, 2)}
    write_json(info, os.path.join(od, "info.json"))
    log("  rows: " + ", ".join(f"{k} {v:,}" for k, v in info["rows"].items()))
    return info


# ----------------------------------------------------------------------------- README.md
_FC = ("log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the "
       "composition shift and the well-position effect are removed")
_DD_COLS = {
    "drug": "drug name as in Tahoe (salt forms are separate drugs; see salt_base)",
    "dose": "dose key (text): the concentration formatted with %.6g, in the unit of the sample metadata (uM)",
    "conc": "concentration (uM)",
    "dd": "drug-dose row: row of atlas/effects/drugdose.csv and of every DD_* / DDL_* matrix",
    "salt_base": "drug name without the trailing salt / form in brackets (tlib.salt_base): salt forms of one "
                 "compound share it",
}
_BEST = {"dd": "drug-dose row (-1 = none)", "drug": "drug", "dose": "dose key (uM)",
         "fold": "pooled fold change (linear; 2**lfc; " + _FC + ")", "z": "pooled z (DD_z)",
         "q": "BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all "
              "drug-doses)", "flags": "drug-dose flags + this gene's flags (atlas_core.gene_flags), '; '-joined; "
              "'cell-cycle shift (explains ~N% here)' where the drug-dose's shift is not the explanation of this "
              "gene's change (no artifact flag; see 'Cell-cycle shift')"}


def _gene_docs():
    d = {"col": "gene column: row key of genes.csv and column of every gene matrix (0 .. genes-1). Key genes by col",
         "symbol": "gene symbol (can repeat between columns)", "label": "unique label: the symbol, or 'SYM (ENSG...)' "
         "for repeated symbols", "ensembl_id": "Ensembl gene id from the Tahoe gene metadata (joined on token; '' when "
         "missing)", "token": "Tahoe gene token id",
         "pooled_cpm": "level over all wells and lines (counts per million)",
         "median_line_cpm": "median over cell lines of the line's level (CPM)", "n_lines_expressing":
         "lines that truly express the gene (line_effects 'expressed', tensor/line_measured.npy): level >= 25% of the "
         "median line's (the atlas's expr_mask) AND >= 25% of the gene's pooled level (otherwise the line reads only "
         "ambient RNA); atlas/effects/genes.csv keeps the atlas's count", "noise_rna": "True for noise-class "
         "RNAs (atlas NOISE_RNA_RE on the symbol: 7SK, snoRNA, snRNA, mitochondrial, ribosomal-protein pseudogenes, "
         "replication histones, ENSG-only names): read their drug responses with care",
         "corr_with_S": "Pearson r over all drug wells (pairwise complete) of the gene's corrected well effect (W2) "
         "with the S-phase module's: near 1 = the gene moves with the S-phase share of cells", "corr_with_G2M":
         "the same with the G2/M module", "n_dd_up": "drug-doses that raise the gene significantly (q_up < 0.10 and "
         "fold >= 1.2)", "n_dd_down": "drug-doses that lower it significantly (q_down < 0.10 and fold <= 1/1.2)",
         "n_dd_up_clean": "n_dd_up among clean drug-doses (no artifact flag for this gene)", "n_dd_down_clean":
         "n_dd_down among clean drug-doses", "up_specificity_z_gap": "best clean z up minus the best clean z up of any "
         "OTHER compound (salt forms merged): large = one compound stands out; NaN with < 2 compounds",
         "down_specificity_z_gap": "the same for decreases (in units of -z)",
         "cc_slope_S": "the gene's slope bS on the S-phase module's pooled log2 fold change (robust regression of its "
         "pooled lfc on the S_PHASE and G2M_PHASE modules' pooled lfc over the drug-doses without another artifact "
         "flag; see 'Cell-cycle shift'): how much of a cell-cycle shift reaches the gene (~1: it moves like the "
         "module; ~0: unaffected); NaN with < 20 fitted drug-doses",
         "cc_slope_G2M": "the same slope bG on the G2/M module's pooled log2 fold change"}
    for pre, what in (("best_up", "highest pooled z over all drug-doses (flagged ones included; may be "
                                  "non-significant: check q)"),
                      ("best_down", "lowest pooled z over all drug-doses (flagged ones included)"),
                      ("best_clean_up", "highest pooled z over the clean drug-doses for this gene"),
                      ("best_clean_down", "lowest pooled z over the clean drug-doses for this gene")):
        for k, v in _BEST.items():
            d[f"{pre}_{k}"] = f"{what}: {v}"
    d["best_clean_up_n_lines_up"] = ("best clean drug-dose up: lines with per-line z >= 2 and fold >= 1.2 (tensor "
                                     "DDL_z / DDL_lfc; descriptive, not a per-line test: see drug_effects "
                                     "n_lines_up); -1 = no clean drug-dose")
    d["best_clean_down_n_lines_down"] = ("best clean drug-dose down: lines with per-line z <= -2 and fold <= 1/1.2 "
                                         "(descriptive); -1 = none")
    d["best_clean_up_pattern"] = "dose pattern of that drug for this gene (atlas dose_shape over its doses' pooled z)"
    d["best_clean_down_pattern"] = "the same for the decrease (z negated)"
    return d


DOCS = {
    "genes.parquet": ("One row per gene (gene columns of atlas/effects/genes.csv; the S_PHASE, G2M_PHASE and "
                      "PROTEASOME module columns are not here). 'Clean' = the drug-dose's flags plus this gene's "
                      "flags hold none of: toxic, transcription drop, cell-cycle shift (only where the shift is the "
                      "explanation of this gene's change: see 'Cell-cycle shift'), unreliable plate only, position "
                      "not correctable, position correction uncertain, wells disagree. n_dd_up / n_dd_down and "
                      "best_up_* / best_down_* count and rank every drug-dose (flagged ones included: their flags "
                      "are in best_*_flags); the *_clean columns the clean ones only.", _gene_docs()),
    "drug_effects.parquet": (
        "Fold change relative to each drug: one row per gene x drug-dose with |pooled z| >= 3 or q_up < 0.10 or "
        "q_down < 0.10 (sorted by col, then z from high to low). Pooled = over the cell lines (median per well, mean "
        "over the drug-dose's used wells), so a response seen in fewer than about half of the measured lines is not "
        "here: look in line_effects / drug_line_top. Per-line values come from the tensor (DDL_z, DDL_lfc). The "
        "line counts (n_lines_up / n_lines_down / lines_*) are descriptive: per-line z >= 2 is not a per-line test "
        "(see 'Per-line significance' above).",
        {"col": "gene column", "symbol": "gene symbol", "dd": _DD_COLS["dd"], "drug": _DD_COLS["drug"],
         "dose": _DD_COLS["dose"], "conc": _DD_COLS["conc"], "lfc": "pooled " + _FC + " (DD_lfc)",
         "fold": "2**lfc (linear fold change; 1 = no change)", "z": "pooled z (DD_z: Stouffer over the used wells of "
         "the robust z of the corrected well effect, divided by the gene's plate factor)", "q_up": "BH q-value for an "
         "increase (within the gene, over all drug-doses)", "q_down": "BH q-value for a decrease",
         "flags": "drug-dose flags + this gene's flags ('noisy plate (z scaled)' from its own plate factor, 'position "
         "correction uncertain', 'position effect removed'), '; '-joined, the exact strings of the atlas, except that "
         "a drug-dose's 'cell-cycle shift' reads 'cell-cycle shift (explains ~N% here)' where the shift is not the "
         "explanation of this gene's change (N = round(100 x cc_share); no artifact flag)",
         "clean": "True when flags hold no artifact flag (atlas_core.has_artifact; see genes.parquet). Rows that are "
         "not clean are kept: read them with their flags", "n_lines_measured": "lines with a "
         "per-line value (truly expressing the gene, enough cells in the wells, >= 2 expected counts)", "n_lines_up":
         "lines with per-line z >= 2 and fold >= 1.2: where the pooled effect shows up (descriptive; at z >= 2 a "
         "line also passes by chance, at the rate lines_up_chance_rate of tables/info.json)", "n_lines_down":
         "lines with per-line z <= -2 and fold <= 1/1.2 (descriptive, as n_lines_up)", "lines_up":
         "cell names of those lines, strongest per-line z first, at most 12, ', '-joined", "lines_down":
         "cell names of the lines counted in n_lines_down, most negative per-line z first, at most 12",
         "pattern_up": "how the increase behaves over the drug's "
         "doses (atlas dose_shape over the pooled z by ascending dose; the same for every dose of the drug): none / "
         "single dose / all doses, stronger at high dose / all doses, flat / top dose only / rises with dose / two "
         "highest doses / inconsistent across doses", "pattern_down": "the same for the decrease (z negated)",
         "cc_share": "at a drug-dose whose flags include 'cell-cycle shift': the share of this gene's change that the "
         "shift would explain, |bS x S + bG x G| / |lfc| with the gene's slopes (genes.parquet cc_slope_S, "
         "cc_slope_G2M, here fitted again without this drug-dose when it is in the fit: leave-one-out) and the "
         "drug-dose's S_PHASE_lfc / G2M_PHASE_lfc; 0 when that predicted part "
         "goes the other way; at most 1. NaN for drug-doses without the flag (or genes without slopes). The flag "
         "stays an artifact flag unless 2 x cc_share < 0.5 and |lfc| x (1 - 2 x cc_share) >= log2 1.2 (see "
         "'Cell-cycle shift')"}),
    "line_effects.parquet": (
        "Fold change relative to each cell line: one row per gene x cell line (all genes x all lines). Counts and "
        "bests without a suffix use the clean drug-doses for the gene, those ending in '_all' every drug-dose "
        "(flagged ones included, with their flags in best_*_flags_all); both use the per-line tensor values "
        "(DDL_z, DDL_lfc): a per-line fold change is the mean over the drug-dose's used wells of that line's " + _FC
        + "; per-line z = Stouffer over those wells of (value - line centre) / line scale / plate factor.",
        {"col": "gene column", "symbol": "gene symbol", "line": "line index (row of lines.parquet / atlas lines.csv, "
         "last axis of the tensor)", "cell_line_id": "Cellosaurus id", "cell_name": "cell line name",
         "baseline_cpm": "the line's level of the gene over all its wells (CPM; atlas line_cpm)", "expressed":
         "the line truly expresses the gene (tensor/line_measured.npy): the atlas's expr_mask (level >= 25% of the "
         "median line's) AND level >= 25% of the gene's pooled level; below that the line reads only the wells' "
         "ambient RNA, and its per-line values are NaN",
         "response_sd": "1.4826 x MAD over the clean drug-doses of the line's per-line log2 fold change: the typical "
         "spread of this gene's responses in this line (log2; NaN with < 10 measured clean drug-doses)",
         "n_dd_up": "clean drug-doses with per-line z >= line_z_threshold (calibrated; tables/info.json) and fold "
         ">= 1.5 in this line", "n_dd_down": "clean drug-doses with per-line z <= -line_z_threshold and fold <= 1/1.5",
         "best_up_dd": "the drug-dose counted in n_dd_up with the highest per-line z in this line (-1 = none passes)",
         "best_up_drug": "its drug",
         "best_up_dose": "its dose key (uM)", "best_up_lfc": "its per-line log2 fold change", "best_up_z":
         "its per-line z", "best_down_dd": "the drug-dose counted in n_dd_down with the lowest per-line z (-1 = "
         "none passes)", "best_down_drug":
         "its drug", "best_down_dose": "its dose key (uM)", "best_down_lfc": "its per-line log2 fold change",
         "best_down_z": "its per-line z",
         "n_dd_up_all": "n_dd_up over all drug-doses (flagged ones included). Chance passes grow with the number of "
         "drug-doses: line_z_expected_chance_all of tables/info.json",
         "n_dd_down_all": "n_dd_down over all drug-doses (flagged ones included)",
         "best_up_dd_all": "the drug-dose counted in n_dd_up_all with the highest per-line z in this line, flagged or "
         "not (-1 = none passes); equal to best_up_dd when that one is clean",
         "best_up_drug_all": "its drug", "best_up_dose_all": "its dose key (uM)",
         "best_up_lfc_all": "its per-line log2 fold change", "best_up_z_all": "its per-line z",
         "best_up_flags_all": "its flags for this gene (as drug_effects flags; null = none passes)",
         "best_up_clean_all": "True when those flags hold no artifact flag (False when none passes)",
         "best_up_cc_share_all": "its cc_share for this gene (as drug_effects; NaN without the cell-cycle flag)",
         "best_down_dd_all": "the drug-dose counted in n_dd_down_all with the lowest per-line z in this line, flagged "
         "or not (-1 = none passes)", "best_down_drug_all": "its drug", "best_down_dose_all": "its dose key (uM)",
         "best_down_lfc_all": "its per-line log2 fold change", "best_down_z_all": "its per-line z",
         "best_down_flags_all": "its flags for this gene (null = none passes)",
         "best_down_clean_all": "True when those flags hold no artifact flag (False when none passes)",
         "best_down_cc_share_all": "its cc_share for this gene (NaN without the cell-cycle flag)"}),
    "drug_line_top.parquet": (
        "Per gene and direction, the 15 strongest (drug-dose, cell line) cells over ALL drug-doses (flagged ones "
        "included, with their flags) with per-line |z| >= line_z_threshold (calibrated; tables/info.json; no fold "
        "condition), plus any of the 15 strongest among the clean drug-doses for the gene that fall outside them, "
        "so that flagged cells never push the clean ones out: at most 30 rows per gene and direction, fewer when "
        "fewer qualify. Responses confined to a few lines, which the pooled tables miss, show up here.",
        {"col": "gene column", "symbol": "gene symbol", "direction": "up / down", "rank": "rank of the cell's "
         "per-line z in that direction among all the gene's qualifying cells, flagged or not (1 = strongest; a clean "
         "cell kept beyond the 15 strongest has its rank over all, > 15)", "dd": _DD_COLS["dd"],
         "drug": _DD_COLS["drug"], "dose": _DD_COLS["dose"],
         "line": "line index", "cell_name": "cell line name", "lfc": "per-line " + _FC + " (DDL_lfc)",
         "z": "per-line z (DDL_z)", "pooled_lfc": "the drug-dose's pooled log2 fold change for the gene (DD_lfc)",
         "pooled_z": "the drug-dose's pooled z (DD_z)",
         "flags": "the drug-dose's flags for this gene (as drug_effects flags)",
         "clean": "True when flags hold no artifact flag; False = read the cell with its flags",
         "cc_share": "the share of the gene's pooled change the drug-dose's cell-cycle shift would explain (as "
         "drug_effects; NaN without the flag)"}),
    "drugdoses.parquet": (
        "atlas/effects/drugdose.csv (one row per drug and dose) plus dd, salt_base, top_up and top_down.",
        {"dd": _DD_COLS["dd"], "drug": _DD_COLS["drug"], "dose": _DD_COLS["dose"], "salt_base": _DD_COLS["salt_base"],
         "conc": _DD_COLS["conc"], "n_wells": "used wells (those on reliable plates; all of them when the drug-dose "
         "sits only on unreliable plates)", "n_wells_all": "all its wells", "wells": "well names of the used wells",
         "plates": "plates of the used wells", "wells_left_out": "plate:well of wells left out (on unreliable plates)",
         "unreliable_plate_only": "True when every well is on an unreliable plate",
         "cells_log2_vs_plate": "cells per well, log2 vs the plate's median drug well (mean over used wells)",
         "umi_per_cell_log2_vs_plate": "UMIs per cell, log2 vs the plate's median drug well",
         "genes_per_cell_log2_vs_plate": "genes detected per cell, log2 vs the plate's median drug well",
         "row_cells_log2": "the same as cells_log2_vs_plate for the other drug wells in the same plate row (median; "
         "mean over the used wells)", "row_umi_per_cell_log2": "the same for UMIs per cell",
         "row_genes_per_cell_log2": "the same for genes per cell", "composition_shift_log2": "median over the "
         "wells' lines of the profile's composition (library-size) shift (log2)", "cells_log2_best_well":
         "the largest cells_log2_beyond_row of the used wells ('toxic' needs it < -0.5)", "plate_scale":
         "mean plate factor (z divisor) of the used wells", "position_wells_used": "mean number of other-drug wells "
         "at the same position used for the position correction", "position_not_correctable": "True when a used well "
         "had < 3 other-drug wells at its position", "S_PHASE_lfc": "S-phase module log2 fold change",
         "S_PHASE_z": "S-phase module z", "G2M_PHASE_lfc": "G2/M module log2 fold change", "G2M_PHASE_z":
         "G2/M module z", "PROTEASOME_lfc": "proteasome module log2 fold change", "PROTEASOME_z":
         "proteasome module z", "cells_log2_best_higher_dose": "best cells_log2_vs_plate of the same drug at a "
         "higher dose (NaN: none)", "flags": "drug-dose flags, '; '-joined (artifacts: toxic, transcription drop, "
         "cell-cycle shift, unreliable plate only, position not correctable, wells disagree; caveats: low cells "
         "(technical?), plate-row cell shift, composition shift, noisy plate (z scaled))", "n_genes_up":
         "genes raised significantly (q_up < 0.10, fold >= 1.2)", "n_genes_down": "genes lowered significantly",
         "n_sig_genes": "n_genes_up + n_genes_down", "replicate_r": "mean pairwise r of the used wells' z over the "
         "top 500 genes (wells agree?)", "targets": "drug targets (Tahoe drug metadata)", "moa_fine":
         "mechanism of action, fine", "moa_broad": "mechanism of action, broad", "approved": "human-approved (Tahoe "
         "drug metadata)", "top_up": "up to 15 significantly raised genes, highest z first: 'LABEL (fold x)'",
         "top_down": "up to 15 significantly lowered genes, lowest z first: 'LABEL (fold x)'"}),
    "drugs.parquet": (
        "One row per drug (all its doses).",
        {"drug": _DD_COLS["drug"], "salt_base": _DD_COLS["salt_base"], "targets": "drug targets", "moa_fine":
         "mechanism of action, fine", "moa_broad": "mechanism of action, broad", "approved": "human-approved",
         "n_doses": "number of doses", "doses": "dose keys by ascending concentration (uM), ' / '-joined",
         "n_sig_by_dose": "significant genes (n_sig_genes) per dose, same order", "max_sig": "the largest of them",
         "best_dose": "the dose with the most significant genes (tie -> the higher dose)", "best_dd":
         "its drug-dose row", "lowest_active_dose": "the lowest dose such that it and every higher dose have >= 10 "
         "significant genes; 'low dose only (noise?)' when only lower doses do; '' when no dose does",
         "flags_by_dose": "each dose's flags ('-' = none), ' / '-joined by ascending dose",
         "signature_r_between_doses": "cosine similarity of the pooled z signatures (genes significant in >= 3 "
         "drug-doses) of consecutive doses (low-mid / mid-high): near 1 = the same response growing with dose"}),
    "lines.parquet": (
        "atlas/effects/lines.csv (one row per cell line, in the order of the line axis) plus line, tp53_status, "
        "n_dd_depleted, n_dd_depleted_clean, median_response.",
        {"line": "line index (last axis of the tensor)", "cell_line_id": "Cellosaurus id", "n_cells_total":
         "cells of the line over all wells", "cell_name": "cell line name", "Cell_ID_DepMap": "DepMap id",
         "Organ": "organ of origin", "drivers": "driver genes (variant type) from the Tahoe cell-line metadata",
         "driver_changes": "driver protein changes", "in_growth_analysis": "True when the line has enough cells for "
         "the relative-abundance (growth) analysis", "wells_usable": "wells with >= min_cells cells of the line "
         "(usable expression)", "pct_wells_usable": "the same as % of all wells", "tp53_status": "altered (a TP53 "
         "row in the cell-line metadata) / wild type (the line is in the metadata without one) / unknown",
         "n_dd_depleted": "drug-doses that deplete the line: relative-abundance z (DD_Az) <= -3, leaving out only "
         "drug-doses whose cell counts are untrustworthy (unreliable plate only, position not correctable, wells "
         "disagree); toxic, transcription drop and cell-cycle shift drug-doses count (depletion is what makes them "
         "toxic). -1 = not measured: the line is not in the growth analysis (too few cells)",
         "n_dd_depleted_clean": "the same among clean drug-doses only (no artifact flag at all); -1 = not measured",
         "median_response": "median over drug-doses of the line's response strength (DD_beta: "
         "slope of the line's changes on the drug-dose's consensus over its significant genes; 1 = a typical line, "
         "0 = no response; only drug-doses with >= 20 significant genes)"}),
    "plates.parquet": (
        "One row per plate (atlas plate order).",
        {"plate": "plate", "n_wells": "wells analysed (drug + DMSO; failed wells excluded)", "n_drug_wells":
         "drug wells", "doses": "dose keys of the drug wells (uM), ' / '-joined", "unreliable": "True for plates "
         "named unreliable (kept out of pooled drug-doses, centres and plate-factor peers)", "plate_factor":
         "largest plate-group factor of the plate (z divisor; 1 = as noisy as its peers)", "dmso_wells": "DMSO "
         "well names", "n_dmso_wells": "number of DMSO wells", "failed_wells": "well names excluded as technical "
         "failures (< 1/8 of the plate's typical cells while the drug did fine elsewhere)", "n_failed_wells":
         "number of them", "median_cells_per_well": "median cells per analysed well (all lines)"}),
    "wells.parquet": (
        "atlas/effects/wells.csv (one row per analysed well, the row order of W1/W2/Z and of the tensor's well "
        "axis) plus w and umi_total. Per-gene raw counts per well are in tensor/well_counts.npy (wells x genes, UMI "
        "summed over the well's lines), not here.",
        {"w": "well row (axis of W1/W2/Z, tensor R and well_counts)", "sample": "Tahoe sample id", "plate": "plate",
         "drug": "drug (DMSO_TF for vehicle)", "n_cells": "cells in the well (all lines)", "is_dmso": "vehicle well",
         "plate_num": "plate number", "conc": "concentration (uM; 0 for DMSO)", "unit": "concentration unit",
         "mean_gene_count": "mean genes per cell (Tahoe sample metadata)", "mean_tscp_count": "mean transcripts "
         "per cell (Tahoe sample metadata)", "mean_pcnt_mito": "mean mitochondrial fraction (Tahoe sample metadata)",
         "slot": "well position 1-96 (A1 = 1, row-major)", "slot_purity": "share of the well's cells whose barcode "
         "gives that position", "well": "well name (A1 ... H12)", "dose": "dose key (uM)", "cells": "cells of the "
         "analysed lines in the well", "umi_per_cell": "UMIs per cell", "genes_per_cell": "genes per cell",
         "cells_log2_vs_plate": "cells, log2 vs the plate's median drug well", "umi_per_cell_log2_vs_plate":
         "UMIs per cell, log2 vs the plate's median drug well", "genes_per_cell_log2_vs_plate": "genes per cell, "
         "log2 vs the plate's median drug well", "row_cells_log2": "median cells_log2_vs_plate of the other drug "
         "wells in the same plate row", "row_umi_per_cell_log2": "the same for UMIs per cell",
         "row_genes_per_cell_log2": "the same for genes per cell", "cells_log2_beyond_row": "cell loss beyond the "
         "plate row where the row itself moved > 0.8 log2, else cells_log2_vs_plate", "composition_shift_log2":
         "median over the well's lines of the composition shift (log2)", "unreliable_plate": "well on an "
         "unreliable plate", "position_wells_used": "other-drug wells at the same position (position correction "
         "donors)", "position_clean_donors_median": "median over genes of the clean donors used",
         "position_not_correctable": "< 3 donors: no position correction", "plate_scale_group": "plate-and-dose "
         "group of the plate factor", "plate_scale_group_id": "row of atlas plate_scale_gene.npy (-1: none)",
         "plate_scale_pass1": "the group's plate factor, pass 1", "plate_scale": "the group's plate factor (z "
         "divisor)", "drugdose_row": "drug-dose row (dd; -1 = DMSO)", "used_in_drugdose": "the well counts in its "
         "drug-dose", "umi_total": "total UMIs of the well over its analysed lines (tensor well_umi)"}),
}


def _fmt_p(v):
    return "n/a" if v is None else f"{v:.2g}"


def _calibration_text(cal):
    """The 'Per-line significance' paragraph of README.md, with this run's numbers (cal = calibrate_line_z)."""
    cal = cal or {}
    t = cal.get("line_z_threshold", LINE_Z_FLOOR)
    tail = cal.get("line_z_null_tail") or {}
    return [
        "**Pooled vs per line**: the pooled values are the atlas's *median over the measured lines*, so a response "
        "seen in fewer than about half of the measured lines (e.g. a p53 response in the TP53-wild-type lines only) "
        "does not appear in drug_effects or in the n_dd_* / best_* columns of genes.parquet. Such responses are in "
        "line_effects (per gene x line) and drug_line_top (each gene's strongest drug-dose x line cells).", "",
        f"**Per-line significance** (line_effects n_dd_up / n_dd_down / best_*, drug_line_top): per-line |z| >= "
        f"**{t:g}** (`line_z_threshold` in tables/info.json; fold >= 1.5 for line_effects). A per-line z rests on one "
        "or two wells and its tails are heavier than a normal's, so the cut is calibrated on this run: among "
        f"(gene, clean drug-dose) pairs whose pooled |z| < {NULL_POOLED_Z:g} (the null), P(|per-line z| >= 3) = "
        f"{_fmt_p(tail.get('3'))}, >= 4: {_fmt_p(tail.get('4'))}, >= 5: {_fmt_p(tail.get('5'))}, >= 6: "
        f"{_fmt_p(tail.get('6'))}. t is the smallest value >= {LINE_Z_FLOOR:g} at which the expected number of "
        f"chance passes per (gene, line) over the {cal.get('line_z_n_clean_drugdoses', '?')} clean drug-doses is <= "
        f"{LINE_CHANCE_MAX:g}; at t it is {_fmt_p(cal.get('line_z_expected_chance'))} "
        "(`line_z_expected_chance`; over all drug-doses, as line_effects' *_all counts: "
        f"{_fmt_p(cal.get('line_z_expected_chance_all'))}, `line_z_expected_chance_all`). The 'lines up / down' of "
        "drug_effects and genes.parquet (per-line z >= 2 and "
        "fold >= 1.2, given a pooled call) are descriptive: they say where the pooled effect shows up, and a line "
        f"with no effect reaches z >= 2 at a rate of {_fmt_p(cal.get('lines_up_chance_rate'))} and z <= -2 at "
        f"{_fmt_p(cal.get('lines_down_chance_rate'))} (`lines_up_chance_rate`, `lines_down_chance_rate`; the "
        "null's tails per direction are `line_z_null_tail_up` / `_down`: low counts make the lower tail heavier).",
        "",
        f"**Lines that do not express a gene** (line_effects `expressed` = False) have no per-line values: below "
        f"{AMB_FRAC:g} x the gene's pooled level a line reads only the wells' ambient RNA (the average of all the "
        "well's cells), whose 'responses' are other lines' (tensor/line_measured.npy). Profiles with < 2 expected "
        "counts of the gene (few cells or a low level) are not measured either. So re-expression of a gene a line "
        "does not make is not detected here.", ""]


def _cell_cycle_text(cc):
    """The 'Cell-cycle shift' paragraph of README.md, with this run's numbers (cc = _cc_summary)."""
    cc = cc or {}
    k = CC_SAFETY

    def n(key):
        v = cc.get(key)
        return f"{v:,}" if isinstance(v, int) else "?"
    mods = "; ".join(f"{m}: {v['cleared']:,} of {v['significant_at_cc']:,} ({v['genes']} genes)"
                     for m, v in (cc.get("module_genes") or {}).items()) or "modules.json not found"
    return [
        "**Cell-cycle shift** (decided per gene): the atlas flags a drug-dose 'cell-cycle shift' when its cells moved "
        "into or out of S or G2/M (the S_PHASE or G2M_PHASE module's pooled log2 fold change beyond 0.5, or beyond "
        "0.25 at |z| >= 4). That is a property of the drug-dose; whether it explains a given gene's change depends on "
        "how much the gene goes with the cell cycle, and that is measured here: per gene, a robust regression (OLS, "
        f"then one Huber reweighting at {CC_HUBER:g} robust SDs) of its pooled lfc on the two modules' pooled lfc, "
        f"lfc ~ a + bS x S + bG x G, over the {n('drugdoses_fitted')} drug-doses with no other artifact flag "
        f"(genes.parquet cc_slope_S / cc_slope_G2M; >= {CC_MIN_FIT} drug-doses with a value for the gene). At a "
        "flagged drug-dose the shift predicts bS x S + bG x G of the gene's change, with the slopes fitted again "
        "without that drug-dose when it is among the fitted ones (leave-one-out: the drug-doses being judged have "
        "the largest module changes, so a strong change of the gene's own there would otherwise pull the slopes "
        "toward explaining it), and `cc_share` (drug_effects, "
        "drug_line_top) is that part's share of the observed change (0 when it points the other way). Fitted slopes "
        "are attenuated by measurement noise (the modules' lfc are measured with error too), so the rule doubles "
        f"them to be safe: the plain artifact flag 'cell-cycle shift' stays unless {k:g} x cc_share < "
        f"{CC_SHARE_MAX:g} and the change left after the doubled prediction, |lfc| x (1 - {k:g} x cc_share), is at "
        "least the 1.2x floor; then the gene's flags read 'cell-cycle shift (explains ~N% here)', which is no "
        "artifact flag, and the value is clean unless another flag says otherwise (other artifact flags of the "
        f"drug-dose still apply). This run: {n('drugdoses_flagged')} drug-doses carry the flag, "
        f"{n('drugdoses_cc_only')} of them no other artifact flag; there the rule clears {n('cleared_at_cc_only')} of "
        f"{n('significant_at_cc_only')} significant changes ({n('cleared_at_cc_only_x1')} with the slopes as "
        "fitted). Check, the genes of the atlas's cell-cycle modules at every flagged drug-dose (the shift is what "
        f"moves them, so few should be cleared): significant changes cleared {mods}.", "",
        "Example from the full Tahoe-100M run: TRIM72 (MG53) has slopes bS +0.50, bG +0.47. Idarubicin 5 uM raises "
        "it 12.2x (z +15.9, in 37 of 37 lines) and its cell-cycle shift would explain ~4% of that; homoharringtonine "
        "5 uM ~18%, 0.5 uM ~8%; epirubicin 5 uM ~14%: all cleared (clean). At panobinostat 0.5 uM (~87%) and TAK-901 "
        "5 uM (~75%) the flag stays. Classic cell-cycle genes have large slopes (PCNA bS +1.50, CCNE2 bS +1.55, "
        "TOP2A bG +1.51, CCNB1 bG +1.38), so at a real shift the flag stays for them. Over the 46 drug-doses whose "
        "only artifact flag is the shift, the rule clears 131,683 of 193,346 significant changes (163,786 with the "
        "slopes as fitted).", ""]


def readme(tables, cal=None, cc=None):
    """README.md text for the written tables ({file: [columns]}) and the columns lacking a description; cal = the
    per-line |z| calibration (calibrate_line_z) and cc = the cell-cycle rule's counts (_cc_summary), whose numbers
    the text quotes."""
    missing = []
    out = ["# tables/ - the fold-change tables", "",
           "Written by `tahoemap tables` (tahoemap/tables.py). Keys: `col` = gene column (0 .. genes-1, the order of "
           "atlas/effects/genes.csv), `dd` = drug-dose row (atlas/effects/drugdose.csv), `line` = cell-line index "
           "(atlas/effects/lines.csv), `w` = well row (atlas/effects/wells.csv). Join on these, not on names: "
           "symbols can repeat.", "",
           "**Baseline of every fold change**: the same cell line's median over the plate's *drug* wells (the typical "
           "treated well; most drugs leave most genes alone), **not DMSO**. For each line and well the atlas takes "
           "log2 CPM minus that line's plate median, minus the profile's composition (library-size) shift, minus the "
           "well-position effect. Pooled values (`lfc`, `z`, `q_*`, `pooled_*`) take the median over lines per well "
           "and then the mean (lfc) or Stouffer sum (z) over the drug-dose's used wells; per-line values (tensor "
           "DDL_lfc / DDL_z) keep each line. `lfc` is log2; `fold` = 2**lfc (1 = no change, 2 = doubled, 0.5 = "
           "halved). z is a robust z (median / 1.4826 MAD of the drug wells), widened on noisy plates.", "",
           f"**Significant** (as the atlas): q_up < {Q_CUT:g} and fold >= 1.2 (up), q_down < {Q_CUT:g} and fold <= "
           "1/1.2 (down); q = Benjamini-Hochberg within each gene over all drug-doses. **Clean** = no artifact flag "
           "(" + ", ".join(A.ARTIFACT_FLAGS) + ") in the drug-dose's flags plus the gene's own flags (a cell-cycle "
           "shift counts only where it is the explanation of the gene's change: see below). Soft caveats "
           "that do not make a value unclean: low cells (technical?), plate-row cell shift, composition shift, noisy "
           "plate (z scaled), position effect removed. **Flagged values are kept**: every table lists flagged "
           "drug-doses in their ranked place with their flags (and `clean` = False); only estimates (the per-line "
           "|z| calibration, response_sd, the cell-cycle slopes) leave artifact-flagged drug-doses out.", "",
           "Missing values: NaN / null = not measured (line not expressing, too few cells or counts) or no "
           "candidate; -1 in an index or count column = none / not measured.", ""] + _calibration_text(cal) \
        + _cell_cycle_text(cc)
    for name, cols in tables.items():
        intro, docs = DOCS[name]
        out += [f"## {name}", "", intro, "", "| column | meaning |", "|---|---|"]
        for c in cols:
            d = docs.get(c)
            if d is None:
                missing.append(f"{name}:{c}")
                d = "(see atlas/effects/README_effects.md)"
            out.append(f"| `{c}` | {d.replace('|', '/')} |")
        out.append("")
    out += ["The gene x gene table ('relative to each gene') is relations/gene_relations.parquet.", ""]
    return "\n".join(out), missing
