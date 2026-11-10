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
strings (drug-dose flags + atlas_core.gene_flags per gene), dose patterns (atlas_core.dose_shape, here vectorised by
dose_shape_codes and checked against it), noise-class RNAs (atlas_core.NOISE_RNA_RE) and salt forms (tlib.salt_base).
"clean" = no common.ARTIFACT_FLAGS flag (the atlas's seven plus 'like a neighbouring well'; common.has_artifact) in
the drug-dose's flags of record plus the gene's own flags. Refinements: the cell-cycle shift, the neighbouring wells
and the translation-inhibitor caveat (below).

Flags of record (tables version 5): drugdose.csv's flags (drugdoses.parquet atlas_flags), then 'like a neighbouring
well' or 'like a neighbouring well (top dose)' (neighbour_wells), then 'translation inhibitor' for a drug in a class
whose effect is 'translation' (tahoemap/data/drug_classes.json via mechanisms.py). Every table here, and every later
stage (dd_flags_of_record), uses them. Per gene, flag_strings reads them: the neighbouring-well tokens read 'like a
neighbouring well (not this gene)' where no partner moves the gene the same way (nb_gene_mask), and 'translation
inhibitor' reads 'rise under a translation inhibitor' where the gene rises and is left out where it does not: the
pooled change (DD_lfc > 0) for the pooled tables, the cell's own per-line change for a per-line cell (drug_line_top,
line_effects best_*). Old rule (version 5): every per-line cell read the pooled sign, so a per-line fall under a
translation inhibitor could read 'rise under a translation inhibitor' and a per-line rise could lose it. New rule
(version 6): each cell reads its own sign.

Neighbouring wells (neighbour_wells; README 'Neighbouring wells'). Touching wells share signatures 3.5 to 4 times more
often than wells 3 or more apart on the real plates (e.g. Citalopram 0.05 uM next to Clobetasol propionate on
plate10). A drug-dose whose significant genes are mostly moved the same way by a touching well of another compound,
while its own higher doses do not move them, gets the artifact flag 'like a neighbouring well' for the genes that
neighbour moves; at the drug's top dose (no higher dose to check) it gets the caveat 'like a neighbouring well (top
dose)', or a note when the two share an annotated mechanism. Old rule (version 4): clean = no atlas artifact flag.
New rule: also not like a neighbouring well for that gene.

Dose and plate. Each dose of a drug sits on its own plate (for most drugs the same well on three plates) and most
drug-doses are one well, so a dose pattern compares plates as much as doses, and the lines of a drug-dose are not
replicate treatments (drugs.parquet dose_plates, drug_effects n_wells). drug_effects lfc_vs_dmso adds the plate's DMSO
offset (atlas plate_offset) to lfc: a sign check against DMSO, not a replacement baseline.

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
                           fold change, z, q, flags, clean, how many / which lines move, dose pattern, cc_share,
                           the drug-dose's used wells (n_wells), a rough DMSO-referenced lfc (lfc_vs_dmso)
    line_effects.parquet   gene x line: baseline level, whether the line expresses it, spread of the line's
                           responses, drug-doses moving the gene >= 1.5x at per-line |z| >= t (calibrated, >= 4) and
                           the strongest of them up / down in that line, over the clean drug-doses and (*_all, with
                           the flags) over all drug-doses
    drug_line_top.parquet  per gene: the 15 strongest (drug-dose, line) cells up and down over all drug-doses (with
                           flags and clean), plus any of the 15 strongest clean ones beyond them (per-line |z| >= t)
    drugdoses.parquet      drugdose.csv + dd, salt_base, top 15 significant genes up / down, the flags of record
                           (atlas_flags = drugdose.csv's), the neighbouring-well rule (nb_*), mechanism classes and
                           the lines where the drug-dose is selective
    drugs.parquet          per drug: doses, significant genes by dose, best dose, lowest active dose, flags, signature
                           similarity between doses, where each dose sits (dose_plates), Tahoe's and ChEMBL's
                           annotations side by side, mechanism classes
    lines.parquet          lines.csv + TP53 status ('altered' / 'not recorded' / 'unknown'), drug-doses that deplete
                           the line (-1 = not measured), median response strength
    drug_line_response.parquet  one row per drug-dose x line: genes beyond the per-line cut, rms z, line selectivity
                           (rel_log2, sel_z, selective), relative abundance and response strength from the atlas
    drugdose_signatures.gmt  every drug-dose's up and down call sets (no cap), for gene-set tools
    plates.parquet         per plate: wells, doses, reliability, plate factor, DMSO and failed wells, cells per well
    wells.parquet          wells.csv + total UMI per well (per-gene counts stay in tensor/well_counts.npy)
    info.json              row counts, the per-line |z| calibration (line_z_threshold, line_fold_min, ...), the
                           cell-cycle rule's counts (cell_cycle_rule), neighbour_rule, translation_inhibitors,
                           dmso_sign_changes, dose_and_plate, annotations, drug_line_response, gmt

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
from . import mechanisms as M
from . import tlib as T
from .common import (ARTIFACT_FLAGS, FLAG_TEXT, NB_CLEARED, NB_FLAG, NB_TOP, TL_DD, TL_RISE, has_artifact, log,
                     read_effects_index, read_stamp, replace_file, stamp_stage, write_json, write_parquet)
from .tensor import AMB_FRAC, measured_mask

VERSION = 6                         # 3: a cell-cycle shift blocks a gene only when it explains its change;
#                                     4: each cell-cycle-flagged drug-dose is judged with slopes fitted without it;
#                                     5: neighbouring wells; flags of record; translation-inhibitor caveat;
#                                        annotations; drug_line_response; lfc_vs_dmso; n_wells; dose_plates;
#                                        TP53 'not recorded'
#                                     6: per-line cells (drug_line_top, line_effects best_*) read the translation-
#                                        inhibitor token from their own per-line sign, not the pooled one; line_effects
#                                        best_up_flags / best_down_flags (the clean best's caveats); neighbouring
#                                        wells: tier 'dose response' and the chance rate in the top-dose alert

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

# Neighbouring wells (neighbour_wells; README 'Neighbouring wells'). A drug-dose whose signature is mostly that of a
# well right next to it on the same plate (another compound) may carry that well's signal.
NB_MIN_SIG = 30                     # a judged drug-dose needs >= this many significant genes (noise RNAs left out);
#                                     below this the hits were weak drug-doses next to neighbours with > 1,800 genes
NB_Z = 3.0                          # 'moves a gene the same way': pooled |z| >= this, with the same sign
NB_SHARE = 0.5                      # J: share of its significant genes the neighbour moves the same way, >= this
NB_TOPK = 30                        # the neighbour's strongest significant genes (largest |z|) ...
NB_TOP_SHARE = 0.3                  # ... of which the judged drug-dose moves >= this share the same way (T)
NB_MIN_SHARED = 10                  # and >= this many shared genes
NB_OTHER = 0.2                      # its other doses move < this share of the shared genes (the gap 0.13 -> 0.39
#                                     between carry-over and true class neighbours on the real data)
NB_GENE_Z = 2.0                     # per gene: the token holds where a partner moves the gene the same way at |z| >=
NB_DOSE_TOPK = 10                   # at a top dose: the judged drug-dose's strongest shared genes (largest |z|) ...
NB_DOSE_MIN = 3                     # ... of which >= this many move the same way at |z| >= NB_Z at one of its lower
#                                     doses: a dose response of the drug's own effect (tier 'dose response', no token).
#                                     Version 5 had no such tier: RMC-6236 5 uM (next to Trametinib 5 uM) carried the
#                                     top-dose caveat on 498 genes although ETV5, SPRY4 and EGR1 already fell at 0.5 uM
NB_TIERS = ("artifact", "top dose", "same mechanism", "dose response")   # strongest first; the first two carry a
#                                     token
NB_TOKEN = {"artifact": NB_FLAG, "top dose": NB_TOP}
NB_ORIENT = ("side by side", "above/below", "diagonal", "two apart", "3+ apart")
WELL_ROWS = "ABCDEFGH"
# drug_line_response.parquet: how strongly each line responds to each drug-dose, and in which lines it is selective
SEL_Z = 3.0                         # selective: sel_z >= this ...
SEL_MIN_GENES = 20                  # ... and n_genes >= this
SEL_MAD_FLOOR = 0.25                # sel_z divides by max(1.4826 x MAD over the drug-dose's lines, this)
RMS_CLIP = 10.0                     # rms_z clips each per-line z at +-this
T_UNREL = "unreliable plate only"   # the atlas flag of a drug-dose whose every well is on an unreliable plate
UM = "µM"


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


def flag_strings(base, d, posunc, poseff, pscale, cc_pct=None, nb=None, rise=None):
    """Per (drug-dose d, gene) item: atlas_core.gene_flags(base[d], posunc, poseff, pscale=pscale) and whether it is
    clean (no artifact flag: common.has_artifact). base = the drug-doses' flags of record (dd_flags_of_record).
    Then three per-gene readings of drug-dose tokens, in this order:
    cc_pct (int per item; -1 = no change): where the drug-dose's 'cell-cycle shift' is not the explanation of this
        gene's change (cell_cycle_share), the percentage of the change it explains; the token then reads CC_CLEARED,
        which is no artifact flag.
    nb (bool per item, or None = no per-gene reading): where False, the neighbouring-well tokens (NB_FLAG and NB_TOP)
        read NB_CLEARED: no partner moves this gene the same way (nb_gene_mask), so this value is not under that
        suspicion.
    rise (bool per item, or None): the translation-inhibitor token TL_DD reads TL_RISE where True (the gene rises:
        DD_lfc > 0) and is dropped where False.
    gene_flags only thresholds its inputs, so each distinct (d, cc_pct, noisy, uncertain, removed, nb, rise)
    combination is formatted once."""
    d = np.asarray(d, dtype=np.int64)
    if d.size == 0:
        return np.array([], dtype=object), np.array([], dtype=bool)
    posunc = np.asarray(posunc, dtype=bool)
    poseff = np.asarray(poseff, dtype=np.float64)
    pscale = np.asarray(pscale, dtype=np.float64)
    pct = np.full(d.size, -1, dtype=np.int64) if cc_pct is None else np.clip(np.asarray(cc_pct, np.int64), -1, 100)
    # 0 = no per-gene reading, 1 = False, 2 = True
    nbv = np.zeros(d.size, np.int64) if nb is None else np.asarray(nb, dtype=bool).astype(np.int64) + 1
    rsv = np.zeros(d.size, np.int64) if rise is None else np.asarray(rise, dtype=bool).astype(np.int64) + 1
    noisy = np.isfinite(pscale) & (pscale > A.PLATE_SCALE_FLAG)
    moved = np.isfinite(poseff) & (np.abs(poseff) > 0.2)
    key = ((((d * 102 + pct + 1) * 8 + noisy * 4 + posunc * 2 + moved) * 3 + nbv) * 3 + rsv)
    _, first, inv = np.unique(key, return_index=True, return_inverse=True)
    strs = []
    for i in first:
        f = A.gene_flags(base[d[i]], bool(posunc[i]), float(poseff[i]), pscale=float(pscale[i]))
        if f:
            toks = f.split("; ")
            if pct[i] >= 0:
                toks = [CC_CLEARED.format(pct=int(pct[i])) if x == CC_FLAG else x for x in toks]
            if nbv[i] == 1:
                toks = [NB_CLEARED if x in (NB_FLAG, NB_TOP) else x for x in toks]
            if rsv[i] == 2:
                toks = [TL_RISE if x == TL_DD else x for x in toks]
            elif rsv[i] == 1:
                toks = [x for x in toks if x != TL_DD]
            f = "; ".join(toks)
        strs.append(f)
    clean = np.array([not has_artifact(s) for s in strs], dtype=bool)
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
    fit = np.array([(t & set(ARTIFACT_FLAGS)) <= {CC_FLAG} for t in toks], dtype=bool) & np.isfinite(S) \
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


# ----------------------------------------------------------------------------- neighbouring wells
def _as_bool(s):
    """A table column as a bool array (True / 'True' / 1 -> True)."""
    s = pd.Series(s)
    if s.dtype == bool:
        return s.to_numpy()
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "1.0"]).to_numpy()


def well_rc(well):
    """(row, column) of a well name, 0-based: 'F1' -> (5, 0); (-1, -1) when it is not a plate well."""
    w = str(well or "").strip()
    if len(w) < 2 or w[0].upper() not in WELL_ROWS or not w[1:].isdigit():
        return -1, -1
    return WELL_ROWS.index(w[0].upper()), int(w[1:]) - 1


def _orient(dr, dc):
    """NB_ORIENT index of two wells dr rows and dc columns apart."""
    m = max(dr, dc)
    if m >= 3:
        return 4
    if m == 2:
        return 3
    return 0 if dr == 0 else (1 if dc == 0 else 2)


def well_pairs(wells, salt, plate_order=None):
    """Ordered pairs (a, b) of drug-doses whose wells sit on the same plate. Wells: not DMSO, used in their drug-dose
    (drugdose_row >= 0), not on an unreliable plate; a and b of different compounds (salt[a] != salt[b], salt =
    the salt_base per drug-dose). Per pair the closest placement over the plates they share: cheb (Chebyshev
    distance; 1 = touching: side by side, above/below or at a corner), orient (index into NB_ORIENT) and places: every
    touching placement as 'plate10 F1 next to G1' (a's well first; plates in plate_order, then by name).
    Returns a DataFrame with a, b, cheb, orient, places (list of str), plates (list of str)."""
    w = wells
    ok = ~_as_bool(w["is_dmso"]) & _as_bool(w["used_in_drugdose"]) & (pd.to_numeric(
        w["drugdose_row"], errors="coerce").fillna(-1).to_numpy(np.int64) >= 0)
    if "unreliable_plate" in w:
        ok &= ~_as_bool(w["unreliable_plate"])
    w = w[ok]
    rc = np.array([well_rc(x) for x in w["well"].astype(str)], dtype=np.int64).reshape(-1, 2)
    keep = rc[:, 0] >= 0
    w, rc = w[keep], rc[keep]
    d = w["drugdose_row"].to_numpy(dtype=np.int64)
    pl = w["plate"].astype(str).to_numpy()
    wl = w["well"].astype(str).to_numpy()
    order = {p: i for i, p in enumerate(plate_order or [])}
    plates = sorted(set(pl), key=lambda p: (order.get(p, len(order)), len(p), p))
    parts = []
    for pi, p in enumerate(plates):
        i = np.flatnonzero(pl == p)
        if i.size < 2:
            continue
        x, y = np.meshgrid(i, i, indexing="ij")
        x, y = x.ravel(), y.ravel()
        m = (d[x] != d[y]) & (np.asarray(salt, dtype=object)[d[x]] != np.asarray(salt, dtype=object)[d[y]])
        x, y = x[m], y[m]
        dr = np.abs(rc[x, 0] - rc[y, 0])
        dc = np.abs(rc[x, 1] - rc[y, 1])
        parts.append(pd.DataFrame({"a": d[x], "b": d[y], "cheb": np.maximum(dr, dc),
                                   "orient": [_orient(u, v) for u, v in zip(dr, dc)], "pi": pi,
                                   "place": [f"{p} {wl[u]} next to {wl[v]}" for u, v in zip(x, y)], "plate": p}))
    if not parts:
        return pd.DataFrame({"a": np.zeros(0, np.int64), "b": np.zeros(0, np.int64), "cheb": np.zeros(0, np.int64),
                             "orient": np.zeros(0, np.int64), "places": [], "plates": []})
    F = pd.concat(parts, ignore_index=True)
    F = F.sort_values(["a", "b", "cheb", "orient", "pi"], kind="stable")
    touch = F[F["cheb"] == 1]
    places = touch.groupby(["a", "b"], sort=False)["place"].agg(list)
    tplates = touch.groupby(["a", "b"], sort=False)["plate"].agg(lambda s: list(dict.fromkeys(s)))
    P = F.drop_duplicates(["a", "b"], keep="first")[["a", "b", "cheb", "orient"]].reset_index(drop=True)
    key = list(zip(P["a"], P["b"]))
    P["places"] = [places.get(k, []) for k in key]
    P["plates"] = [tplates.get(k, []) for k in key]
    return P


def _target_set(t):
    return {x.strip().upper() for x in str(t or "").replace(";", ",").split(",")
            if x.strip() and x.strip().upper() not in ("NAN", "NONE", "-")}


def same_mechanism(a, b, moa, targets, drug, classes=None):
    """(what, source) when drug-doses a and b share an annotated mechanism, else None: Tahoe moa_fine (not '' or
    'unclear'), Tahoe targets (a target in common), or a mechanism class (classes = {drug: [class keys]},
    mechanisms.classes_by_drug). Checked in that order; the first match is named with its source."""
    ma, mb = str(moa[a] or "").strip(), str(moa[b] or "").strip()
    if ma and ma.lower() not in ("unclear", "nan", "none") and ma.lower() == mb.lower():
        return ma, "Tahoe moa_fine"
    common = sorted(_target_set(targets[a]) & _target_set(targets[b]))
    if common:
        return ", ".join(common), "Tahoe targets"
    if classes:
        cb = set(classes.get(str(drug[b]), []))
        common = [k for k in classes.get(str(drug[a]), []) if k in cb]
        if common:
            return ("; ".join(M.class_info(k).get("label", k) for k in common),
                    "drug class, tahoemap/data/drug_classes.json")
    return None


def parse_partners(partners, n=None):
    """{drug-dose: [partner drug-doses]} from a mapping, a sequence of lists, or the ','-joined text of
    drugdoses.parquet nb_partners (one entry per drug-dose; '' = none)."""
    if isinstance(partners, dict):
        items = partners.items()
    else:
        items = enumerate(partners)
    out = {}
    for d, ps in items:
        if ps is None or (isinstance(ps, float) and not np.isfinite(ps)):
            continue
        if isinstance(ps, str):
            ps = [int(x) for x in ps.split(",") if x.strip().lstrip("-").isdigit()]
        ps = [int(p) for p in ps if int(p) >= 0 and (n is None or int(p) < n)]
        if ps:
            out[int(d)] = ps
    return out


def nb_gene_mask(z, partners, gene_z=NB_GENE_Z):
    """The genes that carry a drug-dose's neighbouring-well token: gene g of drug-dose d (with partners) is marked
    when sign(z[d, g]) != 0 and some partner p has the same sign with |z[p, g]| >= gene_z. z = pooled z (drug-doses x
    genes; any subset of gene columns, e.g. one gene's column); partners: see parse_partners. Returns a bool array of
    z's shape (False for drug-doses without partners)."""
    z = np.asarray(z)
    mask = np.zeros(z.shape, dtype=bool)
    for d, ps in parse_partners(partners, z.shape[0]).items():
        sd = np.sign(np.nan_to_num(np.asarray(z[d], dtype=np.float64)))
        hit = np.zeros(z.shape[1:], dtype=bool)
        for p in ps:
            zp = np.nan_to_num(np.asarray(z[p], dtype=np.float64))
            hit |= (np.sign(zp) == sd) & (np.abs(zp) >= gene_z)
        mask[d] = hit & (sd != 0)
    return mask


def _pct(x):
    return f"{int(round(100.0 * float(x)))}"


def _dose_list(doses):
    """'0.5 and 5 µM' ('' for none)."""
    return _and(doses) + " " + UM if len(doses) else ""


def _and(xs):
    """'a', 'a and b', 'a, b and c' ('' for none)."""
    xs = [str(x) for x in xs]
    if len(xs) <= 1:
        return "".join(xs)
    return ", ".join(xs[:-1]) + " and " + xs[-1]


def _chance_text(chance):
    """' Pairs 3 or more wells apart pass this test too: ...' for a top-dose alert ('' without far pairs). chance =
    (expected passes from the far pairs, touching pairs passing at this tier, far pairs judged)."""
    if not chance or chance[0] is None or not chance[2]:
        return ""
    exp, n_pass, _n_far = chance
    share = f" (about {_pct(exp / n_pass)}%)" if n_pass else ""
    return (f" Pairs 3 or more wells apart pass this test too: at their rate, about {exp:.1f} of the {n_pass} "
            f"touching pairs that pass at a top dose are expected by chance{share}.")


def nb_alert(rec):
    """The plain-words alert of one drug-dose's neighbouring-well record (neighbour_wells' per-tier templates; % rounded
    to integers). rec: tier, role ('judged': the weaker drug-dose of the pair, 'partner': the stronger one, which
    gets the tier only when its own other doses do not show the shared genes either), k, n, n_b, where, plates,
    partner, other, own, doses (the other doses compared), top (this is the drug's top dose), has_other (it has other
    doses to compare), mech ((what, source) or None), g (genes carrying the token), dose_k and dose_at (tier 'dose
    response': how many of its NB_DOSE_TOPK strongest shared genes its lower dose dose_at moves the same way), chance
    ((expected passes from the far pairs, touching pairs passing, far pairs judged) of its tier: the top-dose alert
    states it)."""
    k, n, partner = rec["k"], rec["n"], rec["partner"]
    places = rec.get("places") or [p for p in str(rec["where"]).split("; ") if p]
    head = (f"{k} of its {n} significant genes move the same way in the neighbouring well"
            f"{'s' if len(places) > 1 else ''} {_and(places)}")
    tier, role = rec["tier"], rec["role"]
    if tier == "artifact":
        if role == "judged" and rec["own"] >= NB_OTHER:
            return (f"{head} ({partner}, {rec['n_b']} significant genes), which shows them at its other doses too "
                    f"({_pct(rec['own'])}%). This drug's higher doses ({_dose_list(rec['doses'])}) move "
                    f"{_pct(rec['other'])}% of them. The signal probably came from the neighbouring well. Flagged on "
                    f"{rec['g']} genes: those the neighbour moves the same way.")
        return (f"{head} ({partner}), and neither compound moves them at its other doses ({_pct(rec['other'])}% and "
                f"{_pct(rec['own'])}%). Probably a local problem on this part of {_and(rec['plates'])}. Flagged on "
                f"{rec['g']} genes.")
    if tier == "top dose":
        ch = _chance_text(rec.get("chance"))
        if role == "judged":
            low = (f"and its lower doses move {_pct(rec['other'])}% of them" if rec["has_other"]
                   else "and it has no lower dose to compare")
            return (f"This is the drug's top dose. {head} ({partner}), {low}. The data cannot tell a carried-over "
                    f"signal from a real effect: shown with this alert, not flagged.{ch}")
        return (f"{head} ({partner}, at that drug's top dose), and neither compound moves them at its other doses "
                f"({_pct(rec['other'])}% and {_pct(rec['own'])}%). The data cannot tell a carried-over signal from a "
                f"real effect: shown with this alert, not flagged.{ch}")
    if tier == "dose response":
        return (f"This is the drug's top dose. {head} ({partner}), and its lower doses move {_pct(rec['other'])}% "
                f"of them. But its {rec['dose_at']} {UM} dose already moves {rec['dose_k']} of its "
                f"{NB_DOSE_TOPK} strongest shared genes the same way (|z| >= {NB_Z:g}): the drug's own effect grows "
                "with the dose. Probably a real effect, not a carried-over signal. Not flagged.")
    what, src = rec["mech"] or ("", "")
    pre = "This is the drug's top dose. " if rec["top"] else ""
    return (f"{pre}{head} ({partner}), which has the same annotated mechanism ({what}, {src}): probably a real class "
            "effect. Not flagged.")


def neighbour_wells(wells, dd, sig, z, classes=None, plate_order=None, gene_z=NB_GENE_Z):
    """The neighbouring-well rule (README 'Neighbouring wells'): is a drug-dose's signature mostly that of a well right
    next to it on the same plate (another compound), which its own other doses do not show?

    a. Wells (well_pairs): not DMSO, used in their drug-dose, not on an unreliable plate. Ordered pairs (a, b) of
       drug-doses of different compounds with wells on the same plate at Chebyshev distance 1 (side by side,
       above/below, corner); the place text is kept per plate ('plate10 F1 next to G1').
    b. sig = +1 / -1 / 0: the atlas significance call (noise RNAs 0); s3 = sign(z) where |z| >= NB_Z; nsig = the
       significant genes; top_b = b's NB_TOPK significant genes with the largest |z| (stable sort).
    c. (a, b) is judged when nsig[a] >= NB_MIN_SIG, nsig[b] >= nsig[a] and len(top_b) >= 10. shared = a's
       significant genes that b moves the same way (s3[b] == sig[a]); J = |shared| / nsig[a]; T = the share of top_b
       that a moves the same way. It resembles b when |shared| >= NB_MIN_SHARED, J >= NB_SHARE, T >= NB_TOP_SHARE.
    d. Other doses = the same drug name at another concentration, leaving out drug-doses flagged 'unreliable plate
       only'. share(y) = the share of the shared genes that y moves the same way. If a has higher doses: r_other =
       the largest share over them; tier 'artifact' when r_other < NB_OTHER. At the top dose: r_other = the largest
       share over the lower doses (0 if none); when r_other < NB_OTHER: 'same mechanism' (a note, no token) when a
       and b share Tahoe moa_fine, Tahoe targets or a mechanism class (same_mechanism); else 'dose response' (a note,
       no token) when one of a's lower doses already moves >= NB_DOSE_MIN of a's NB_DOSE_TOPK strongest shared genes
       (largest |z[a]|) the same way at |z| >= NB_Z (the drug's own effect growing with the dose; b then gets no
       tier from this pair); else 'top dose'. Lower doses are never exempted: a true class member shows the
       signature at its higher doses.
    e. r_own = the largest share over b's other doses (0 if none); when r_own < NB_OTHER neither compound shows the
       genes elsewhere, and b gets the same tier with partner a. A drug-dose keeps its strongest tier (NB_TIERS
       order) and lists every partner.
    f. mask = nb_gene_mask(z, partners, gene_z): the genes that carry the token.

    wells: wells.csv; dd: drugdose.csv (drug, dose, conc, flags = the atlas flags; moa_fine, targets when present);
    sig: drug-doses x genes int8; z: pooled z (DD_z); classes: {drug: [class keys]} (mechanisms.classes_by_drug).
    Every judged pair at every distance is scored: the far pairs (3+ wells apart) give the chance rate.
    Returns a dict: per drug-dose arrays tier, partner_dd, partner, where, partners (','-joined dd rows), n_sig,
    shared, share, top_share, other_share, partner_own_share, genes, alert; mask (drug-doses x genes bool); pairs
    (the judged pairs with their statistics: a DataFrame); info (tables/info.json 'neighbour_rule')."""
    sig = np.asarray(sig, dtype=np.int8)
    Dn, gK = sig.shape
    drug = dd["drug"].astype(str).to_numpy(dtype=object)
    dose = dd["dose"].astype(str).to_numpy(dtype=object)
    conc = pd.to_numeric(dd["conc"], errors="coerce").to_numpy(dtype=np.float64)
    aflags = dd["flags"].fillna("").astype(str).to_numpy(dtype=object) if "flags" in dd else np.full(Dn, "", object)
    moa = dd["moa_fine"].fillna("").astype(str).to_numpy(dtype=object) if "moa_fine" in dd else np.full(Dn, "", object)
    tgt = dd["targets"].fillna("").astype(str).to_numpy(dtype=object) if "targets" in dd else np.full(Dn, "", object)
    salt = np.array([T.salt_base(x) for x in drug], dtype=object)
    name = np.array([f"{a} {b} {UM}" for a, b in zip(drug, dose)], dtype=object)
    P = well_pairs(wells, salt, plate_order)

    zz = np.nan_to_num(np.asarray(z, dtype=np.float32))
    s3 = (np.sign(zz) * (np.abs(zz) >= NB_Z)).astype(np.int8)
    nsig = (sig != 0).sum(axis=1).astype(np.int64)
    idx = np.flatnonzero(nsig >= NB_MIN_SIG)
    pos = np.full(Dn, -1, dtype=np.int64)
    pos[idx] = np.arange(idx.size)
    ntop = np.zeros(Dn, dtype=np.int64)
    TopP = np.zeros((idx.size, gK), dtype=np.float32)
    TopN = np.zeros((idx.size, gK), dtype=np.float32)
    for k, b in enumerate(idx):
        s = np.flatnonzero(sig[b])
        t = s[np.argsort(-np.abs(zz[b, s]), kind="stable")][:NB_TOPK]
        ntop[b] = t.size
        TopP[k, t[sig[b, t] > 0]] = 1.0
        TopN[k, t[sig[b, t] < 0]] = 1.0
    Pf, Nf = (sig[idx] > 0).astype(np.float32), (sig[idx] < 0).astype(np.float32)
    P3, N3 = (s3[idx] > 0).astype(np.float32), (s3[idx] < 0).astype(np.float32)
    SH = Pf @ P3.T + Nf @ N3.T                     # SH[a, b]: a's significant genes that b moves the same way
    TM = P3 @ TopP.T + N3 @ TopN.T                 # TM[a, b]: b's top genes that a moves the same way
    del Pf, Nf, P3, N3, TopP, TopN

    a_, b_ = P["a"].to_numpy(np.int64), P["b"].to_numpy(np.int64)
    judged = (nsig[a_] >= NB_MIN_SIG) & (nsig[b_] >= nsig[a_]) & (ntop[b_] >= 10)
    J = P[judged].reset_index(drop=True)
    a_, b_ = J["a"].to_numpy(np.int64), J["b"].to_numpy(np.int64)
    J["shared"] = SH[pos[a_], pos[b_]].astype(np.int64) if a_.size else np.zeros(0, np.int64)
    J["share"] = J["shared"] / np.maximum(nsig[a_], 1)
    J["top_share"] = (TM[pos[a_], pos[b_]] / np.maximum(ntop[b_], 1)) if a_.size else np.zeros(0)
    J["resembles"] = (J["shared"] >= NB_MIN_SHARED) & (J["share"] >= NB_SHARE) & (J["top_share"] >= NB_TOP_SHARE)

    rows_of = {}
    usable = np.array([T_UNREL not in str(f).split("; ") for f in aflags], dtype=bool)
    for i, x in enumerate(drug):
        rows_of.setdefault(x, []).append(i)
    top_dose = np.array([conc[i] >= max(conc[j] for j in rows_of[drug[i]] if usable[j] or j == i)
                         for i in range(Dn)], dtype=bool)
    ext = {c: np.full(len(J), np.nan) for c in ("other_share", "partner_own_share")}
    tiers = np.full(len(J), "", dtype=object)
    partner_tier = np.zeros(len(J), dtype=bool)
    detail = {}
    for i in np.flatnonzero(J["resembles"].to_numpy()):
        a, b = int(J.at[i, "a"]), int(J.at[i, "b"])
        sh = (sig[a] != 0) & (s3[b] == sig[a])

        def share(y):
            return float(np.mean(s3[y, sh] == sig[a, sh])) if sh.any() else 0.0
        others = [y for y in rows_of[drug[a]] if y != a and conc[y] != conc[a] and usable[y]]
        hi = sorted((y for y in others if conc[y] > conc[a]), key=lambda y: conc[y])
        lo = sorted((y for y in others if conc[y] < conc[a]), key=lambda y: conc[y])
        comp = hi if hi else lo
        r_other = max((share(y) for y in comp), default=0.0)
        own = [y for y in rows_of[drug[b]] if y != b and conc[y] != conc[b] and usable[y]]
        r_own = max((share(y) for y in own), default=0.0)
        ext["other_share"][i], ext["partner_own_share"][i] = r_other, r_own
        mech, dose_k, dose_at = None, 0, ""
        if r_other < NB_OTHER:
            if hi:
                tiers[i] = "artifact"
            else:
                mech = same_mechanism(a, b, moa, tgt, drug, classes)
                if not mech and lo:                    # its strongest shared genes at its lower doses
                    gs = np.flatnonzero(sh)
                    top = gs[np.argsort(-np.abs(zz[a, gs]), kind="stable")][:NB_DOSE_TOPK]
                    for y in lo:
                        k_ = int(np.sum(s3[y, top] == sig[a, top]))
                        if k_ > dose_k:
                            dose_k, dose_at = k_, dose[y]
                tiers[i] = ("same mechanism" if mech else "dose response" if dose_k >= NB_DOSE_MIN
                            else "top dose")
            partner_tier[i] = r_own < NB_OTHER and tiers[i] != "dose response"
        detail[i] = {"comp": comp, "has_hi": bool(hi), "own": own, "mech": mech, "r_other": r_other, "r_own": r_own,
                     "dose_k": dose_k, "dose_at": dose_at}
    J["other_share"], J["partner_own_share"] = ext["other_share"], ext["partner_own_share"]
    J["tier"] = tiers
    J["partner_tier"] = partner_tier

    # ---- per drug-dose: every touching pair with a tier gives the judged drug-dose (and, when its own other doses do
    # not show the genes either, the partner) a record; each keeps its strongest tier and lists every partner
    recs = {}
    place_of = {(int(x), int(y)): (pl, pls) for x, y, pl, pls in zip(P["a"], P["b"], P["places"], P["plates"])}
    for i in np.flatnonzero((J["cheb"].to_numpy() == 1) & (J["tier"].to_numpy() != "")):
        a, b = int(J.at[i, "a"]), int(J.at[i, "b"])
        det, tier = detail[i], J.at[i, "tier"]
        pl_a, plates = place_of.get((a, b), ([], []))
        recs.setdefault(a, []).append({
            "tier": tier, "role": "judged", "p": b, "k": int(J.at[i, "shared"]), "n": int(nsig[a]),
            "n_b": int(nsig[b]), "J": float(J.at[i, "share"]), "T": float(J.at[i, "top_share"]),
            "other": det["r_other"], "own": det["r_own"], "doses": [dose[y] for y in det["comp"]],
            "has_other": bool(det["comp"]), "top": bool(not det["has_hi"]), "mech": det["mech"],
            "where": "; ".join(pl_a), "places": list(pl_a), "plates": plates, "partner": name[b],
            "dose_k": det["dose_k"], "dose_at": det["dose_at"]})
        if J.at[i, "partner_tier"]:
            pl_b, plates_b = place_of.get((b, a), ([], []))
            kb = int(SH[pos[b], pos[a]]) if pos[b] >= 0 and pos[a] >= 0 else 0
            tb = float(TM[pos[b], pos[a]] / max(ntop[a], 1)) if pos[b] >= 0 and pos[a] >= 0 else 0.0
            mech_b = same_mechanism(b, a, moa, tgt, drug, classes) if tier == "same mechanism" else None
            recs.setdefault(b, []).append({
                "tier": tier, "role": "partner", "p": a, "k": kb, "n": int(nsig[b]), "n_b": int(nsig[a]),
                "J": kb / max(int(nsig[b]), 1), "T": tb, "other": det["r_own"], "own": det["r_other"],
                "doses": [dose[y] for y in det["own"]], "has_other": bool(det["own"]), "top": bool(top_dose[b]),
                "mech": mech_b, "where": "; ".join(pl_b), "places": list(pl_b), "plates": plates_b,
                "partner": name[a]})
    rank = {t: i for i, t in enumerate(NB_TIERS)}
    res = {"tier": np.full(Dn, "", dtype=object), "partner_dd": np.full(Dn, -1, dtype=np.int32),
           "partner": np.full(Dn, "", dtype=object), "where": np.full(Dn, "", dtype=object),
           "partners": np.full(Dn, "", dtype=object), "n_sig": nsig.astype(np.int32),
           "shared": np.full(Dn, -1, dtype=np.int32), "share": np.full(Dn, np.nan, dtype=np.float32),
           "top_share": np.full(Dn, np.nan, dtype=np.float32), "other_share": np.full(Dn, np.nan, dtype=np.float32),
           "partner_own_share": np.full(Dn, np.nan, dtype=np.float32), "genes": np.zeros(Dn, dtype=np.int32),
           "alert": np.full(Dn, "", dtype=object)}
    plist = {}
    for d, rs in recs.items():
        rs.sort(key=lambda r: (rank[r["tier"]], -r["J"], r["p"]))
        seen, ps = set(), []
        for r in rs:
            if r["p"] not in seen:
                seen.add(r["p"])
                ps.append(r["p"])
        r = rs[0]
        res["tier"][d] = r["tier"]
        res["partner_dd"][d] = r["p"]
        res["partner"][d] = r["partner"]
        res["where"][d] = r["where"]
        res["partners"][d] = ",".join(str(p) for p in ps)
        res["shared"][d] = r["k"]
        res["share"][d], res["top_share"][d] = r["J"], r["T"]
        res["other_share"][d], res["partner_own_share"][d] = r["other"], r["own"]
        plist[d] = ps
    mask = nb_gene_mask(z, plist, gene_z)
    # the chance rate (far pairs, 3+ wells apart: the same rule and tiers) x the touching pairs judged, per tier;
    # the top-dose alert states it
    cheb, orient = J["cheb"].to_numpy(), J["orient"].to_numpy()
    near, far = cheb == 1, orient == 4
    n_near, n_far = int(near.sum()), int(far.sum())
    tcol = J["tier"].to_numpy()
    passing = {t: int((near & (tcol == t)).sum()) for t in NB_TIERS}
    expected = {t: (round(float((far & (tcol == t)).sum()) / n_far * n_near, 2) if n_far else None) for t in NB_TIERS}
    for d, rs in recs.items():
        tok = rs[0]["tier"] in NB_TOKEN
        g = int(mask[d].sum()) if tok else 0
        res["genes"][d] = g
        main = dict(rs[0], g=g, chance=(expected.get(rs[0]["tier"]), passing.get(rs[0]["tier"], 0), n_far))
        txt = nb_alert(main)
        rest, seen = [], {rs[0]["p"]}
        for r in rs[1:]:
            if r["p"] in seen:
                continue
            seen.add(r["p"])
            rest.append(f"{r['partner']} ({r['where']}; {r['tier']})")
        if rest:
            more = {"artifact": " The genes they move the same way are flagged too.",
                    "top dose": " The genes they move the same way carry this alert too."}.get(rs[0]["tier"], "")
            txt += (f" It is also like {len(rest)} other neighbouring well{'s' if len(rest) > 1 else ''}: "
                    + "; ".join(rest) + "." + more)
        res["alert"][d] = txt
    res["mask"] = mask

    # ---- info.json 'neighbour_rule': counts, the chance rate from the far pairs, and the orientation table
    resm = J["resembles"].to_numpy()
    far_share = float(resm[far].mean()) if n_far else float("nan")
    orient_tab = []
    for k, o in enumerate(NB_ORIENT):
        m = orient == k
        nj, nr = int(m.sum()), int((m & resm).sum())
        sh = nr / nj if nj else float("nan")
        orient_tab.append({"orientation": o, "judged": nj, "resembling": nr, "share": round(sh, 4) if nj else None,
                           "x_far_share": round(sh / far_share, 2) if nj and far_share > 0 else None})
    dd_counts = {t: int((res["tier"] == t).sum()) for t in NB_TIERS}
    res["pairs"] = J
    res["info"] = {
        "constants": {"NB_MIN_SIG": NB_MIN_SIG, "NB_Z": NB_Z, "NB_SHARE": NB_SHARE, "NB_TOPK": NB_TOPK,
                      "NB_TOP_SHARE": NB_TOP_SHARE, "NB_MIN_SHARED": NB_MIN_SHARED, "NB_OTHER": NB_OTHER,
                      "NB_GENE_Z": gene_z, "NB_DOSE_TOPK": NB_DOSE_TOPK, "NB_DOSE_MIN": NB_DOSE_MIN},
        "pairs_judged": n_near, "pairs_passing": passing, "drugdoses": dd_counts,
        "expected_passes": expected,
        "expected_passes_rule": ("pass rate of the judged pairs 3 or more wells apart (same rule, same tiers) x the "
                                 f"{n_near} touching pairs judged: an upper bound of the chance passes, since far "
                                 "pairs include real class copies"),
        "far_pairs_judged": n_far, "orientation": orient_tab,
        "tier_drugdoses": [{"dd": int(d), "drug": str(drug[d]), "dose": str(dose[d]), "tier": res["tier"][d],
                            "partner": res["partner"][d], "partner_dd": int(res["partner_dd"][d]),
                            "where": res["where"][d], "genes": int(res["genes"][d])}
                           for d in np.flatnonzero(res["tier"] != "")]}
    return res


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


def cc_pct(share, cleared):
    """flag_strings' cc_pct for (drug-dose, gene) items: round(100 x share) where the drug-dose's cell-cycle shift is
    not the explanation of the gene's change (cleared, from cell_cycle_share), else -1. share, cleared: the items'
    values (cell_cycle_share's share and cleared at those items)."""
    return np.where(cleared, np.rint(100.0 * np.nan_to_num(share)), -1).astype(np.int64)


def line_counts(Lz, Ll, t, measured=None, masks=False):
    """The per-line counts of drug_effects and line_effects, from per-line z and log2 fold change Lz, Ll (genes x
    drug-doses x lines, float32, NaN = no value: the tensor's DDL_z / DDL_lfc). measured (lines x genes bool,
    tensor/line_measured): lines that do not truly express a gene are set to NaN first (as _run does; the tensor holds
    NaN there already). Returns (measured, up2, dn2, upT, dnT):
        measured  the line has a value (drug_effects n_lines_measured)
        up2, dn2  per-line z >= LINE_Z and lfc >= LFC_MIN, or z <= -LINE_Z and lfc <= -LFC_MIN (drug_effects
                  n_lines_up / n_lines_down: descriptive)
        upT, dnT  per-line z >= t and lfc >= STRONG_LFC, or -z >= t and -lfc >= STRONG_LFC (the line_effects rule,
                  t = the calibrated cut tables/info.json line_z_threshold; line_effects n_dd_*_all count them over
                  the drug-doses)
    as counts over the lines (int16, genes x drug-doses), or with masks=True the boolean masks themselves."""
    if measured is not None:
        meas = np.asarray(measured, dtype=bool).T[:, None, :]
        Lz = np.where(meas, Lz, np.nan)
        Ll = np.where(meas, Ll, np.nan)
    out = (np.isfinite(Lz), (Lz >= LINE_Z) & (Ll >= LFC_MIN), (Lz <= -LINE_Z) & (Ll <= -LFC_MIN),
           (Lz >= t) & (Ll >= STRONG_LFC), (-Lz >= t) & (-Ll >= STRONG_LFC))
    if masks:
        return out
    return tuple(m.sum(axis=2).astype(np.int16) for m in out)


def drug_grid(dd_drug, dd_conc):
    """The drugs of drugdose.csv in first-seen order, the drug of each drug-dose (index into them), each drug's
    drug-dose rows by ascending conc, and the grid drugs x doses (ascending conc; -1 = none) that dose patterns use."""
    drugs = list(dict.fromkeys(dd_drug))                       # first-seen order of drugdose.csv (sorted by drug)
    drug_ix = {d: i for i, d in enumerate(drugs)}
    drug_of_dd = np.array([drug_ix[d] for d in dd_drug], dtype=np.int64)
    rows_of_drug = [np.flatnonzero(drug_of_dd == i) for i in range(len(drugs))]
    rows_of_drug = [r[np.argsort(dd_conc[r], kind="stable")] for r in rows_of_drug]
    m_dose = max(len(r) for r in rows_of_drug)
    grid = np.full((len(drugs), m_dose), -1, dtype=np.int64)  # drugs x doses (ascending conc), -1 = none
    for i, r in enumerate(rows_of_drug):
        grid[i, :len(r)] = r
    return drugs, drug_of_dd, rows_of_drug, grid


def dose_patterns(z, grid, chunk=2048):
    """Dose pattern codes (into PATTERNS) per (drug, gene), both signs: dose_shape_codes over each drug's pooled z by
    ascending dose (grid from drug_grid; z = DD_z, drug-doses x genes). Returns (P_up, P_dn), int8 drugs x genes."""
    nd, m_dose = grid.shape
    gK = z.shape[1]
    P_up = np.zeros((nd, gK), dtype=np.int8)
    P_dn = np.zeros((nd, gK), dtype=np.int8)
    gsafe = np.maximum(grid, 0)
    for g0 in range(0, gK, chunk):
        g1 = min(gK, g0 + chunk)
        V = z[:, g0:g1][gsafe].astype(np.float64)                 # drugs x doses x genes
        V[grid < 0] = np.nan
        V = V.transpose(0, 2, 1).reshape(-1, m_dose)
        P_up[:, g0:g1] = dose_shape_codes(V).reshape(nd, g1 - g0)
        P_dn[:, g0:g1] = dose_shape_codes(-V).reshape(nd, g1 - g0)
    return P_up, P_dn


def _load_pooled(fxd, name, gK, dtype=np.float32):
    """atlas/effects/<name>.npy, gene columns only (drug-doses x genes), in memory."""
    return np.array(np.load(os.path.join(fxd, f"{name}.npy"), mmap_mode="r")[:, :gK], dtype=dtype)


def _flag_parts(fxd, wells, dd, gK, lfc, dd_flags):
    """The per-(drug-dose, gene) inputs of the gene-level flags, as _run uses them: poseff (DD_poseff), posunc
    (DD_posunc), pscale (_dd_gene_scale) and the cell-cycle rule (cell_cycle_share's tuple)."""
    Dn = len(dd)
    pe = _load_pooled(fxd, "DD_poseff", gK) if os.path.exists(os.path.join(fxd, "DD_poseff.npy")) \
        else np.zeros((Dn, gK), np.float32)
    pu = _load_pooled(fxd, "DD_posunc", gK, bool) if os.path.exists(os.path.join(fxd, "DD_posunc.npy")) \
        else np.zeros((Dn, gK), dtype=bool)
    ps = _dd_gene_scale(wells, fxd, Dn, gK)
    s_col, g_col = (f"{m}_lfc" for m in CC_MODULES)
    nanv = np.full(Dn, np.nan)
    cc = cell_cycle_share(lfc, dd[s_col].to_numpy(dtype=np.float64) if s_col in dd else nanv,
                          dd[g_col].to_numpy(dtype=np.float64) if g_col in dd else nanv, dd_flags, pu)
    return pe, pu, ps, cc


def translation_members(out, classes=None):
    """The drugs in a mechanism class whose effect is 'translation' (they stop protein synthesis): {drug: [class
    keys]} from mechanisms.classes_by_drug and class_info (tahoemap/data/drug_classes.json)."""
    classes = M.classes_by_drug(out) if classes is None else classes
    res = {}
    for d, ks in classes.items():
        tl = [k for k in ks if M.class_info(k).get("effect") == "translation"]
        if tl:
            res[str(d)] = tl
    return res


def flags_of_record(atlas_flags, nb_tier, tl_dd):
    """The drug-doses' flags of record: the atlas flags (drugdose.csv, verbatim), then NB_FLAG (tier 'artifact') or
    NB_TOP (tier 'top dose') of the neighbouring-well rule, then TL_DD for a translation inhibitor; '; '-joined.
    Every reader uses these (dd_flags_of_record)."""
    res = []
    for f, t, tl in zip(atlas_flags, nb_tier, tl_dd):
        toks = [x for x in str(f or "").split("; ") if x]
        if t in NB_TOKEN:
            toks.append(NB_TOKEN[t])
        if tl:
            toks.append(TL_DD)
        res.append("; ".join(toks))
    return np.array(res, dtype=object)


def _tables_v5(out, n):
    """tables/drugdoses.parquet (flags, nb_partners) when the tables stage's stamp is version >= 5 and the table has
    one row per drugdose.csv row (n), else None."""
    st = read_stamp(out, "tables")
    p = os.path.join(out, "tables", "drugdoses.parquet")
    try:
        if not st or int(st.get("version", 0) or 0) < 5 or not os.path.exists(p):
            return None
        t = pd.read_parquet(p, columns=["flags", "nb_partners"])
    except (OSError, ValueError, KeyError, TypeError):
        return None
    return t if len(t) == n else None


def dd_flags_of_record(out):
    """The drug-doses' flags of record, one string per atlas/effects/drugdose.csv row: tables/drugdoses.parquet
    'flags' when the tables stage's stamp is version >= 5 and its row count equals drugdose.csv's; else drugdose.csv's
    flags (an output made before tables version 5, which had no neighbouring-well or translation tokens)."""
    dd = pd.read_csv(os.path.join(out, "atlas", "effects", "drugdose.csv"), usecols=["flags"], dtype={"flags": str},
                     keep_default_na=False, na_values=[""])
    base = dd["flags"].fillna("").astype(str).to_numpy(dtype=object)
    t = _tables_v5(out, len(base))
    return base if t is None else t["flags"].fillna("").astype(str).to_numpy(dtype=object)


def gene_flag_inputs(out, lfc=None):
    """The inputs of flag_strings for every (drug-dose, gene) of a finished run, computed as the tables stage computes
    them (same functions, same order): a dict with dd_flags (the drug-doses' flags of record, object array:
    dd_flags_of_record), posunc (bool, drug-doses x genes), poseff and pscale (float32), cc_share (float32; NaN outside
    the cell-cycle-flagged drug-doses) and cc_cleared (bool), nb (bool: the genes that carry a drug-dose's
    neighbouring-well token, nb_gene_mask over drugdoses.parquet nb_partners and DD_z), rise (bool: DD_lfc > 0), plus
    cc_dd (bool per drug-dose: flagged 'cell-cycle shift' by the atlas) and gK.
    flag_strings(dd_flags, d, posunc[d, g], poseff[d, g], pscale[d, g], cc_pct(cc_share[d, g], cc_cleared[d, g]),
    nb[d, g], rise[d, g]) is then the 'flags' of drug_effects at (d, g) (and its clean). lfc: DD_lfc[:, :gK] when the
    caller holds it."""
    fxd = os.path.join(out, "atlas", "effects")
    ix = read_effects_index(fxd)
    genes, wells, dd = ix["genes"], ix["wells"], ix["drugdose"]
    gK = int((genes["kind"] == "gene").sum())
    Dn = len(dd)
    atlas_flags = dd["flags"].fillna("").astype(str).to_numpy(dtype=object)
    t = _tables_v5(out, Dn)
    dd_flags = atlas_flags if t is None else t["flags"].fillna("").astype(str).to_numpy(dtype=object)
    partners = {} if t is None else parse_partners(t["nb_partners"].fillna("").astype(str).tolist(), Dn)
    if lfc is None:
        lfc = _load_pooled(fxd, "DD_lfc", gK)
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        pe, pu, ps, (cc_dd, share, cleared, _bS, _bG, _nf) = _flag_parts(fxd, wells, dd, gK, lfc, atlas_flags)
        nbm = nb_gene_mask(_load_pooled(fxd, "DD_z", gK), partners) if partners else np.zeros((Dn, gK), bool)
        rise = np.asarray(lfc[:, :gK]) > 0
    return {"dd_flags": dd_flags, "posunc": pu, "poseff": pe, "pscale": ps, "cc_share": share, "cc_cleared": cleared,
            "nb": nbm, "rise": rise, "cc_dd": cc_dd, "gK": gK}


def _used_wells(wells, plates):
    """The used wells of every drug-dose: (drug-dose row, plate index in plates.csv order, well name) per well that is
    used in its drug-dose (wells.csv used_in_drugdose, drugdose_row >= 0), as three arrays."""
    ddr = pd.to_numeric(wells["drugdose_row"], errors="coerce").fillna(-1).to_numpy(np.int64)
    pix = {p: i for i, p in enumerate(plates["plate"].astype(str))}
    wp = wells["plate"].astype(str).map(pix).fillna(-1).to_numpy(np.int64)
    m = _as_bool(wells["used_in_drugdose"]) & (ddr >= 0) & (wp >= 0)
    return ddr[m], wp[m], wells["well"].astype(str).to_numpy(dtype=object)[m]


def _dmso_offset(fxd, wells, plates, dd, gK):
    """The DMSO sign check's offset: off[d, g] = the mean over drug-dose d's used wells of atlas/effects/
    plate_offset.npy[plate of the well, g] (how far the plate's DMSO wells sit below its drug-well median; NaN when
    any of them is NaN, or without plate_offset.npy), so that lfc + off is a rough DMSO-referenced log2 fold change.
    Returns off (drug-doses x genes float32), the used wells per drug-dose (drugdose.csv n_wells when present) and
    the plate indices (plates.csv order) of each drug-dose's used wells."""
    Dn = len(dd)
    d_, p_, _w = _used_wells(wells, plates)
    nw = np.bincount(d_, minlength=Dn)
    n_wells = pd.to_numeric(dd["n_wells"], errors="coerce").fillna(0).to_numpy(np.int64) if "n_wells" in dd else nw
    dd_plates = [[] for _ in range(Dn)]
    for d, p in sorted(set(zip(d_.tolist(), p_.tolist()))):
        dd_plates[d].append(p)
    off = np.full((Dn, gK), np.nan, dtype=np.float32)
    path = os.path.join(fxd, "plate_offset.npy")
    if os.path.exists(path):
        PO = np.load(path, mmap_mode="r")
        if PO.shape[0] == len(plates) and d_.size:
            agg = sp.csr_matrix((1.0 / nw[d_], (d_, p_)), shape=(Dn, len(plates)))
            off = np.asarray(agg @ np.asarray(PO[:, :gK], dtype=np.float64), dtype=np.float32)
            off[nw == 0] = np.nan
        else:
            log(f"  {path} has {PO.shape[0]} rows, plates.csv {len(plates)}: lfc_vs_dmso left NaN")
    else:
        log(f"  {path} not found: lfc_vs_dmso left NaN")
    return off, n_wells, dd_plates


def dose_plates_text(doses, wells_of_dose):
    """drugs.parquet dose_plates: '0.05: plate10 G1 / 0.5: plate11 G1 / 5: plate12 G1' (ascending dose; per dose its
    used wells as 'plate well', ', '-joined; 'no used well' when none). wells_of_dose: per dose a list of (plate,
    well)."""
    parts = []
    for dz, ws in zip(doses, wells_of_dose):
        parts.append(f"{dz}: " + (", ".join(f"{p} {w}" for p, w in ws) if ws else "no used well"))
    return " / ".join(parts)


def line_selectivity(n_genes, measured):
    """drug_line_response's rel_log2 and sel_z from n_genes (drug-doses x lines; genes with |per-line z| >= the
    calibrated cut) and measured (bool, the same shape: a per-line profile exists):
        rel_log2 = log2((n_genes + 1) / (median over the line's measured drug-doses of n_genes + 1)): how many genes
                   this drug-dose moves in the line, against what the line's typical drug-dose moves there
        sel_z    = (rel_log2 - median over the drug-dose's measured lines) / max(1.4826 x MAD over those lines,
                   SEL_MAD_FLOOR): how far the line stands out among the lines of this drug-dose
    NaN where not measured. Returns (rel_log2, sel_z), float64."""
    ng = np.where(measured, np.asarray(n_genes, dtype=np.float64), np.nan)
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        line_med = np.nanmedian(ng, axis=0)
        rel = np.log2((ng + 1.0) / (line_med[None, :] + 1.0))
        med = np.nanmedian(rel, axis=1)
        mad = np.nanmedian(np.abs(rel - med[:, None]), axis=1)
    sel = (rel - med[:, None]) / np.maximum(1.4826 * np.nan_to_num(mad), SEL_MAD_FLOOR)[:, None]
    return rel, np.where(measured, sel, np.nan)


def selective_mask(sel_z, n_genes):
    """drug_line_response 'selective': sel_z >= SEL_Z and n_genes >= SEL_MIN_GENES."""
    with np.errstate(invalid="ignore"):
        return (np.nan_to_num(np.asarray(sel_z, np.float64), nan=-np.inf) >= SEL_Z) & \
            (np.asarray(n_genes) >= SEL_MIN_GENES)


def chembl_release(out):
    """'ChEMBL 37' from reference/sources.json (the ChEMBL release the drug annotations came from), else 'ChEMBL'."""
    p = os.path.join(out, "reference", "sources.json")
    try:
        with open(p, encoding="utf-8") as fh:
            src = json.load(fh)
    except (OSError, ValueError):
        return "ChEMBL"
    rel = str(((src.get("sources") or {}).get("chembl") or {}).get("chembl_release") or "")
    rel = rel.replace("ChEMBL_", "").replace("chembl_", "").strip()
    return f"ChEMBL {rel}" if rel else "ChEMBL"


def annotation_counts(drugs_df):
    """README / info.json counts of the drug annotations in drugs.parquet."""
    def ne(c):
        return int((drugs_df[c].fillna("").astype(str) != "").sum()) if c in drugs_df else 0
    st = drugs_df["annotation_status"].fillna("").astype(str).str.split("; ").explode() \
        if "annotation_status" in drugs_df else pd.Series([], dtype=object)
    known = int(sum(M.known_mechanism(x) for x in drugs_df["chembl_mechanisms"])) if "chembl_mechanisms" in drugs_df \
        else 0
    return {"drugs": int(len(drugs_df)), "chembl_matched": ne("chembl_id"), "with_chembl_mechanism": known,
            "with_mechanism_class": ne("mechanism_classes"), "alerts": ne("annotation_alert"),
            "notes": ne("annotation_note"),
            "status": {str(k): int(v) for k, v in st[st != ""].value_counts().items()}}


def _not_members_tl():
    """{class: {molecule key: reason}} of tahoemap/data/drug_classes.json not_members for the classes whose effect is
    'translation'."""
    rules = M.load_rules()
    nm = rules.get("not_members", {}) or {}
    return {k: dict(v) for k, v in nm.items() if not k.startswith("_") and isinstance(v, dict)
            and M.class_info(k).get("effect") == "translation"}


def replicate_plates(wells, plate_names):
    """Replicate plates: pairs of plates that share at least half of the drug-doses (used wells) of one of them:
    [{'plates': [p, q], 'drugdoses_shared', 'drugdoses': [on p, on q]}] in plate order."""
    d_, p_, _w = _used_wells(wells, pd.DataFrame({"plate": plate_names}))
    sets = [set(d_[p_ == i].tolist()) for i in range(len(plate_names))]
    res = []
    for i, si in enumerate(sets):
        for j in range(i + 1, len(sets)):
            k = len(si & sets[j])
            if k and k >= 0.5 * min(len(si), len(sets[j])):
                res.append({"plates": [plate_names[i], plate_names[j]], "drugdoses_shared": int(k),
                            "drugdoses": [len(si), len(sets[j])]})
    return res


def write_gmt(path, drug, dose, flags, symbol, sig_up, sig_dn):
    """tables/drugdose_signatures.gmt: per drug-dose two gene sets, '<drug> <dose> µM up' and '... down', holding every
    gene whose call is up / down (q < Q_CUT and fold >= 1.2 that way; no cap; symbols, each once). The description
    field gives the drug-dose row, the rule and the flags of record. A set with no gene is not written (an empty line
    breaks some tools); the counts say how many. Returns the counts for info.json."""
    rows, n_empty = [], 0
    for d in range(len(drug)):
        for word, S, rule in (("up", sig_up, "fold >= 1.2"), ("down", sig_dn, "fold <= 1/1.2")):
            g = np.flatnonzero(S[d])
            if not g.size:
                n_empty += 1
                continue
            genes = list(dict.fromkeys(str(symbol[i]) for i in g if str(symbol[i])))
            desc = (f"dd {d}: {len(genes)} genes with q < {Q_CUT:g} and {rule} (tables/drug_effects.parquet); flags: "
                    f"{flags[d] or 'none'}")
            rows.append("\t".join([f"{drug[d]} {dose[d]} {UM} {word}", desc] + genes))
    _write_text(path, "\n".join(rows) + ("\n" if rows else ""))
    return {"file": "drugdose_signatures.gmt", "sets": 2 * len(drug), "written": len(rows),
            "empty_not_written": n_empty}


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


TP53_NOT_RECORDED = "not recorded"     # no TP53 alteration in the metadata (driver alterations only): presumed wild
#                                         type, not confirmed. Before tables version 5 this read 'wild type'.


def _tp53_status(lines, fi):
    """'altered' (a TP53 row in the Tahoe cell-line metadata), 'not recorded' (the line is there without one: the
    metadata lists driver alterations only, so this is presumed wild type, not confirmed), 'unknown' (the line is not
    in the metadata). Without the metadata file, lines.csv's drivers list is read the same way."""
    cl = _read_meta(fi, "cell_line", ["Cell_ID_Cellosaur", "Driver_Gene_Symbol"])
    ids = lines["cell_line_id"].astype(str)
    if cl is not None and "Cell_ID_Cellosaur" in cl and "Driver_Gene_Symbol" in cl:
        cid = cl["Cell_ID_Cellosaur"].astype(str)
        present = set(cid)
        altered = set(cid[cl["Driver_Gene_Symbol"].astype(str).str.strip().str.upper() == "TP53"])
        return (np.where(ids.isin(altered), "altered", np.where(ids.isin(present), TP53_NOT_RECORDED, "unknown")),
                "metadata")
    drv = lines["drivers"].fillna("").astype(str) if "drivers" in lines else pd.Series([""] * len(lines))
    st = np.where(drv.str.contains(r"(?:^|; )TP53\(", regex=True), "altered",
                  np.where(drv.str.len() > 0, TP53_NOT_RECORDED, "unknown"))
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
    ("pattern_down", pa.string()), ("cc_share", pa.float32()), ("n_wells", pa.int8()),
    ("lfc_vs_dmso", pa.float32())])


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
    atlas_flags = dd["flags"].fillna("").astype(str).to_numpy(dtype=object)     # drugdose.csv, verbatim
    drugs, drug_of_dd, rows_of_drug, grid = drug_grid(dd_drug, dd_conc)
    drug_ix = {d: i for i, d in enumerate(drugs)}
    salt = np.array([T.salt_base(d) for d in dd_drug], dtype=object)
    comp_ix = {c: i for i, c in enumerate(dict.fromkeys(salt))}
    comp_of_dd = np.array([comp_ix[c] for c in salt], dtype=np.int64)
    noise = np.array([bool(A.NOISE_RNA_RE.match(s)) for s in symbol], dtype=bool)
    plate_names = ix["plates"]["plate"].astype(str).tolist()
    classes = M.classes_by_drug(out)

    # ---- pooled drug-dose x gene matrices (gene columns only)
    lfc, z, qu, qd = (_load_pooled(fxd, n, gK) for n in ("DD_lfc", "DD_z", "DD_qup", "DD_qdn"))
    # the cell-cycle rule reads the atlas flags: a neighbouring-well or translation token does not change it
    pe, pu, ps, (cc_dd, cc_share, cc_clear, cc_bS, cc_bG, cc_fit) = _flag_parts(fxd, wells, dd, gK, lfc, atlas_flags)
    sig_up = (qu < Q_CUT) & (lfc >= LFC_MIN)
    sig_dn = (qd < Q_CUT) & (lfc <= -LFC_MIN)

    # ---- neighbouring wells and the translation-inhibitor caveat: the flags of record
    sig3 = sig_up.astype(np.int8) - sig_dn.astype(np.int8)
    sig3[:, noise] = 0
    nb = neighbour_wells(wells, dd, sig3, z, classes, plate_order=plate_names)
    del sig3
    nb_mask = nb["mask"]
    tl_members = translation_members(out, classes)
    tl_dd = np.array([d in tl_members for d in dd_drug], dtype=bool)
    dd_flags = flags_of_record(atlas_flags, nb["tier"], tl_dd)
    art_dd = np.array([has_artifact(f) for f in dd_flags], dtype=bool)
    nb_art = nb["tier"] == "artifact"
    cc_only = np.array([set(f.split("; ")) & set(ARTIFACT_FLAGS) == {CC_FLAG} for f in atlas_flags], dtype=bool)
    other_art = np.array([bool(set(f.split("; ")) & (set(ARTIFACT_FLAGS) - {CC_FLAG, NB_FLAG})) for f in dd_flags],
                         dtype=bool)
    # clean = no artifact flag for this gene: the drug-dose's flags of record (its cell-cycle shift only where the
    # shift is the explanation of this gene's change; its neighbouring-well flag only where a partner moves this gene
    # the same way) + this gene's position flag
    clean = ~pu & ~other_art[:, None] & (~cc_dd[:, None] | cc_clear) & (~nb_art[:, None] | ~nb_mask)
    finz = np.isfinite(z)
    for t in NB_TIERS:
        m = nb["tier"] == t
        if m.any():
            log(f"  neighbouring wells, {t}: " + "; ".join(f"{dd_drug[d]} {dd_dose[d]} (next to {nb['partner'][d]}, "
                                                           f"{nb['where'][d]})" for d in np.flatnonzero(m)))
    log(f"  neighbouring wells: {nb['info']['pairs_judged']:,} touching pairs judged; passing per tier "
        f"{nb['info']['pairs_passing']}; expected by chance (far pairs) {nb['info']['expected_passes']}")
    if tl_dd.any():
        log(f"  translation inhibitors ({TL_DD!r} caveat): {', '.join(sorted(tl_members))} "
            f"({int(tl_dd.sum())} drug-doses)")

    def cc_pct_at(d, g):
        """flag_strings' cc_pct for (drug-dose, gene) items (cc_pct)."""
        return cc_pct(cc_share[d, g], cc_clear[d, g])

    def gflags(d, g, rise=None):
        """flag_strings for (drug-dose, gene) items: the flags of record read per gene (cell-cycle share,
        neighbouring-well genes, rise under a translation inhibitor). rise: the sign the translation-inhibitor token
        reads (None = the pooled change, DD_lfc > 0; a per-line cell passes its own per-line change, lfc > 0)."""
        return flag_strings(dd_flags, d, pu[d, g], pe[d, g], ps[d, g], cc_pct_at(d, g), nb_mask[d, g],
                            lfc[d, g] > 0 if rise is None else rise)

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
    P_up, P_dn = dose_patterns(z, grid)

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
    gtab["noise_rna"] = noise
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
        fl[ok] = gflags(b[ok], cols[ok])[0]
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
    # drug_line_response: per (drug-dose, line) counts of genes beyond the per-line cut, and the sums for rms_z
    rl_up = np.zeros((Dn, L), dtype=np.int32)
    rl_dn = np.zeros((Dn, L), dtype=np.int32)
    rl_n = np.zeros((Dn, L), dtype=np.int64)
    rl_ss = np.zeros((Dn, L), dtype=np.float64)
    # the DMSO sign check: lfc_vs_dmso = lfc + the mean plate_offset of the drug-dose's plates
    off, dd_n_wells, dd_plates = _dmso_offset(fxd, wells, ix["plates"], dd, gK)
    sc_rows = np.zeros(Dn, dtype=np.int64)
    sc_flip = np.zeros(Dn, dtype=np.int64)
    sc_nan = np.zeros(Dn, dtype=np.int64)
    n_tl_rise = 0

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
            fin, upl, dnl, hit_up, hit_dn = line_counts(Z, X, t_line, masks=True)
            n_meas = fin.sum(axis=2).astype(np.int16)
            n_up = upl.sum(axis=2).astype(np.int16)
            n_dn = dnl.sum(axis=2).astype(np.int16)
            rl_n += fin.sum(axis=0)
            rl_ss += np.square(np.clip(np.where(fin, Z, 0.0), -RMS_CLIP, RMS_CLIP)).sum(axis=0, dtype=np.float64)
            rl_up += (Z >= t_line).sum(axis=0, dtype=np.int32)
            rl_dn += (Z <= -t_line).sum(axis=0, dtype=np.int32)
            del fin
            for b, dst, nn in ((bcu, bcu_nl, n_up), (bcd, bcd_nl, n_dn)):
                bb = b[g0:g1]
                ok = bb >= 0
                dst[g0:g1][ok] = nn[loc[ok], bb[ok]]

            # drug_effects rows of this chunk
            gi, di = np.nonzero(keep[:, g0:g1].T)
            if gi.size:
                g = g0 + gi
                fl, cl_s = gflags(di, g)
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
                    "cc_share": cc_share[di, g], "n_wells": dd_n_wells[di].astype(np.int8),
                    "lfc_vs_dmso": (lf + off[di, g]).astype(np.float32)})
                vd = part["lfc_vs_dmso"].to_numpy(dtype=np.float64)
                flip = np.isfinite(vd) & (np.sign(lf) != np.sign(vd)) & (np.abs(vd) >= LFC_MIN)
                sc_rows += np.bincount(di, minlength=Dn)
                sc_flip += np.bincount(di[flip], minlength=Dn)
                sc_nan += np.bincount(di[~np.isfinite(vd)], minlength=Dn)
                n_tl_rise += int(sum(TL_RISE in str(f).split("; ") for f in fl[tl_dd[di]]))
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
                hit = hit_up if sign > 0 else hit_dn                 # ... and fold >= 1.5 that way (line_counts)
                for scope, Mh in (("all", hit), ("clean", hit & cl)):
                    d_ = PL[(scope, sign)]
                    d_["n"][g0:g1] = Mh.sum(axis=1)
                    S = np.where(Mh, sZ, -np.inf)                    # best_*: the strongest of those counted
                    b = S.argmax(axis=1)                             # genes x lines
                    ok = np.isfinite(np.take_along_axis(S, b[:, None, :], axis=1)[:, 0, :])
                    d_["b"][g0:g1] = np.where(ok, b, -1)
                    d_["z"][g0:g1] = np.where(ok, np.take_along_axis(Z, b[:, None, :], axis=1)[:, 0, :], np.nan)
                    d_["x"][g0:g1] = np.where(ok, np.take_along_axis(X, b[:, None, :], axis=1)[:, 0, :], np.nan)
                    del S, Mh
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
            del Z, X, meas, hit_up, hit_dn
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
        x_ = d_["x"].ravel()
        ok = b >= 0
        fl = np.full(b.size, None, dtype=object)       # its gene-level flags (caveats only: it is clean), the
        if ok.any():                                    # translation-inhibitor token read from the per-line sign
            fl[ok] = gflags(b[ok], gg[ok], np.asarray(x_[ok]) > 0)[0]
        le[f"{prefix}_dd"] = b
        le[f"{prefix}_drug"] = _pick(dd_drug, b)
        le[f"{prefix}_dose"] = _pick(dd_dose, b)
        le[f"{prefix}_lfc"] = x_
        le[f"{prefix}_z"] = d_["z"].ravel()
        le[f"{prefix}_flags"] = fl
    le["n_dd_up_all"] = PL[("all", 1)]["n"].ravel()
    le["n_dd_down_all"] = PL[("all", -1)]["n"].ravel()
    for prefix, sign in (("best_up", 1), ("best_down", -1)):
        d_ = PL[("all", sign)]
        b = d_["b"].ravel()
        ok = b >= 0
        fl = np.full(b.size, None, dtype=object)
        cl_a = np.zeros(b.size, dtype=bool)
        bo, go = b[ok], gg[ok]
        fl[ok], cl_a[ok] = gflags(bo, go, np.asarray(d_["x"].ravel()[ok]) > 0)    # per-line sign (version 6)
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
    tf, tc = gflags(td, tg, np.asarray(tx) > 0)          # the cell's own per-line sign (version 6)
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

    # ---- drug_line_response: per (drug-dose, line) response, growth and selectivity
    rl_meas = rl_n > 0
    n_genes = np.where(rl_meas, rl_up + rl_dn, -1).astype(np.int32)
    with np.errstate(invalid="ignore", divide="ignore"):
        rms_z = np.where(rl_meas, np.sqrt(rl_ss / np.maximum(rl_n, 1)), np.nan).astype(np.float32)
    rel_log2, sel_z = line_selectivity(n_genes, rl_meas)
    selective = selective_mask(sel_z, n_genes) & rl_meas

    def dl_mat(name):                                          # atlas/effects DD_* (drug-doses x lines), else NaN
        q = os.path.join(fxd, f"{name}.npy")
        if os.path.exists(q):
            a = np.load(q)
            if a.shape == (Dn, L):
                return np.asarray(a, dtype=np.float32)
            log(f"  {q} has shape {a.shape}, not ({Dn}, {L}): left NaN")
        return np.full((Dn, L), np.nan, dtype=np.float32)
    DA, DAz, DB, DR = (dl_mat(n) for n in ("DD_A", "DD_Az", "DD_beta", "DD_rcor"))
    in_ga = (_as_bool(lines["in_growth_analysis"]) if "in_growth_analysis" in lines else np.ones(L, dtype=bool))
    untrusted = np.array([any(u in set(f.split("; ")) for u in ABUNDANCE_UNTRUSTED) for f in dd_flags], dtype=bool)
    depleted = np.nan_to_num(DAz, nan=np.inf) <= DEPLETE_Z

    # ---- drugdoses.parquet
    ddt = dd.copy()
    ddt.insert(0, "dd", np.arange(Dn, dtype=np.int32))
    ddt.insert(3, "salt_base", salt)
    ddt["atlas_flags"] = atlas_flags
    ddt["flags"] = dd_flags                                    # the flags of record
    for name, sig, sign in (("top_up", sig_up, 1), ("top_down", sig_dn, -1)):
        idx, vals = _top_k(np.where(sig & finz, sign * z, -np.inf), TOP_GENES)
        ddt[name] = ["; ".join(f"{label[g]} ({2.0 ** float(lfc[d, g]):.2f}x)"
                               for g, v in zip(idx[d], vals[d]) if np.isfinite(v)) for d in range(Dn)]
    ddt["nb_tier"] = nb["tier"]
    ddt["nb_partner_dd"] = nb["partner_dd"].astype(np.int32)
    for k in ("partner", "where", "partners"):
        ddt[f"nb_{k}"] = nb[k]
    ddt["nb_n_sig"] = nb["n_sig"].astype(np.int32)
    ddt["nb_shared"] = nb["shared"].astype(np.int32)
    for k in ("share", "top_share", "other_share", "partner_own_share"):
        ddt[f"nb_{k}" if k != "other_share" else "nb_other_doses_share"] = nb[k].astype(np.float32)
    ddt["nb_genes"] = nb["genes"].astype(np.int32)
    ddt["nb_alert"] = nb["alert"]
    cls_text = {d: M.class_text(out, d) for d in drugs}
    ddt["mechanism_classes"] = [cls_text[d] for d in dd_drug]
    ddt["n_selective_lines"] = selective.sum(axis=1).astype(np.int32)
    sel_txt = []
    for d in range(Dn):
        ls = np.flatnonzero(selective[d])
        ls = ls[np.argsort(-sel_z[d, ls], kind="stable")]
        sel_txt.append(", ".join(f"{line_name[x]} ({sel_z[d, x]:.1f})" for x in ls))
    ddt["selective_lines"] = sel_txt
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

    ann = M.drug_annotations(out)
    ann = ann.assign(drug=ann["drug"].astype(str)).drop_duplicates("drug").set_index("drug", drop=False)
    ud, up_, uw = _used_wells(wells, ix["plates"])
    wells_of_dd = [[] for _ in range(Dn)]
    for d, p, w in sorted(zip(ud.tolist(), up_.tolist(), uw.tolist()), key=lambda x: (x[0], x[1], _well_key(x[2]))):
        wells_of_dd[d].append((plate_names[p], w))
    drows = []
    n_dose_plates = {}
    for name in sorted(drugs):
        r = rows_of_drug[drug_ix[name]]
        ns = nsig[r]
        bi = r[np.lexsort((-dd_conc[r], -ns))[0]]               # most significant genes; tie -> higher dose
        sim = [float(zr[a] @ zr[b] / (nrm[a] * nrm[b])) for a, b in zip(r[:-1], r[1:])]
        plates_by_dose = [{p for p, _w in wells_of_dd[d]} for d in r]
        shared = any(plates_by_dose[i] & plates_by_dose[j] for i in range(len(r)) for j in range(i + 1, len(r)))
        n_dose_plates[name] = (len(r), len(set().union(*plates_by_dose)) if plates_by_dose else 0)
        a = ann.loc[name] if len(ann) and name in ann.index else None

        def av(col):
            return "" if a is None or col not in a or pd.isna(a[col]) else str(a[col])
        drows.append({"drug": name, "salt_base": T.salt_base(name), "targets": meta("targets", r[0]),
                      "moa_fine": meta("moa_fine", r[0]), "moa_broad": meta("moa_broad", r[0]),
                      "approved": meta("approved", r[0]), "n_doses": int(len(r)),
                      "doses": " / ".join(dd_dose[r]), "n_sig_by_dose": " / ".join(str(int(x)) for x in ns),
                      "max_sig": int(ns.max()), "best_dose": dd_dose[bi], "best_dd": int(bi),
                      "lowest_active_dose": _lowest_active(dd_dose[r], ns),
                      "flags_by_dose": " / ".join(f or "-" for f in dd_flags[r]),
                      "signature_r_between_doses": T.fmt_list(sim),
                      "dose_plates": dose_plates_text(dd_dose[r], [wells_of_dd[d] for d in r]),
                      "doses_share_a_plate": bool(shared),
                      "mechanism_classes": cls_text[name],
                      **{c: av(c) for c in ("chembl_id", "chembl_name", "chembl_mechanisms", "chembl_actions",
                                            "chembl_targets", "chembl_matched_by")},
                      "annotation_status": av("annotation_status") or M.NOT_LOADED,
                      "annotation_alert": av("annotation_alert"), "annotation_note": av("annotation_note")})
    del zr
    drugs_df = pd.DataFrame(drows)
    write_parquet(drugs_df, os.path.join(od, "drugs.parquet"))

    # ---- lines.parquet
    tp53, tp53_src = _tp53_status(lines, fi)
    lt = lines.copy()
    lt.insert(0, "line", np.arange(L, dtype=np.int16))
    lt["tp53_status"] = tp53
    meas_l = in_ga & np.isfinite(DAz).any(axis=0)
    in_ga_dl = np.broadcast_to(meas_l[None, :], (Dn, L))
    lt["n_dd_depleted"] = np.where(meas_l, (depleted & ~untrusted[:, None]).sum(axis=0), -1).astype(np.int32)
    lt["n_dd_depleted_clean"] = np.where(meas_l, (depleted & ~art_dd[:, None]).sum(axis=0), -1).astype(np.int32)
    lt["median_response"] = np.nanmedian(DB, axis=0).astype(np.float32)
    write_parquet(lt, os.path.join(od, "lines.parquet"))

    # ---- drug_line_response.parquet (one row per drug-dose x line, every row kept)
    dl_d = np.repeat(np.arange(Dn), L)
    dl_l = np.tile(np.arange(L), Dn)
    dlr = pd.DataFrame({
        "dd": dl_d.astype(np.int32), "drug": dd_drug[dl_d], "dose": dd_dose[dl_d], "conc": dd_conc[dl_d],
        "line": dl_l.astype(np.int16), "cell_line_id": line_id[dl_l], "cell_name": line_name[dl_l],
        "measured": rl_meas.ravel(), "n_genes": n_genes.ravel(),
        "n_up": np.where(rl_meas, rl_up, -1).astype(np.int32).ravel(),
        "n_down": np.where(rl_meas, rl_dn, -1).astype(np.int32).ravel(), "rms_z": rms_z.ravel(),
        "rel_log2": rel_log2.astype(np.float32).ravel(), "sel_z": sel_z.astype(np.float32).ravel(),
        "selective": selective.ravel(), "in_growth_analysis": np.asarray(in_ga_dl).ravel(),
        "log2_rel_abundance": DA.ravel(), "abundance_z": DAz.ravel(), "depleted": depleted.ravel(),
        "abundance_trusted": np.repeat(~untrusted, L), "response_strength": DB.ravel(), "response_r": DR.ravel(),
        "flags": dd_flags[dl_d], "clean": np.repeat(~art_dd, L)})
    write_parquet(dlr, os.path.join(od, "drug_line_response.parquet"))
    dlr_cols = list(dlr.columns)
    n_dlr = len(dlr)
    del dlr

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

    # ---- drugdose_signatures.gmt: every drug-dose's up and down call sets (no cap)
    gmt = write_gmt(os.path.join(od, "drugdose_signatures.gmt"), dd_drug, dd_dose, dd_flags, symbol, sig_up, sig_dn)

    # ---- counts for README.md and info.json
    dmso = {}
    for pi, pl in enumerate(plate_names):
        on = np.array([pi in dd_plates[d] for d in range(Dn)], dtype=bool)
        dmso[pl] = {"rows": int(sc_rows[on].sum()), "sign_changes": int(sc_flip[on].sum()),
                    "no_dmso_value": int(sc_nan[on].sum())}
    nw_counts = {str(k): int(v) for k, v in sorted(pd.Series(dd_n_wells).value_counts().items())}
    three = [v for v in n_dose_plates.values() if v[0] == 3]
    ann_counts = annotation_counts(drugs_df)
    counts = {
        "neighbour_rule": nb["info"],
        "translation_inhibitors": {
            "class_effect": "translation", "members": {d: k for d, k in sorted(tl_members.items())},
            "drugdoses": int(tl_dd.sum()), "drug_effects_rows_rise": n_tl_rise,
            "class_text": {d: cls_text.get(d, "") for d in sorted(tl_members)},
            "not_members": _not_members_tl()},
        "dmso_sign_changes": {"rule": "drug_effects rows with sign(lfc) != sign(lfc_vs_dmso) and |lfc_vs_dmso| >= "
                                      "log2(1.2); a drug-dose on two plates counts on both",
                              "plates": dmso, "rows": int(sc_rows.sum()), "sign_changes": int(sc_flip.sum()),
                              "no_dmso_value": int(sc_nan.sum())},
        "dose_and_plate": {"n_wells": nw_counts, "drugs": len(drugs), "three_dose_drugs": len(three),
                           "three_dose_drugs_on_3_plus_plates": int(sum(v[1] >= 3 for v in three)),
                           "drugs_with_doses_sharing_a_plate": int(drugs_df["doses_share_a_plate"].sum()),
                           "replicate_plates": replicate_plates(wells, plate_names)},
        "annotations": ann_counts, "chembl_release": chembl_release(out),
        "drug_line_response": {"rows": n_dlr, "measured": int(rl_meas.sum()), "selective": int(selective.sum()),
                               "drugdoses_with_a_selective_line": int((selective.sum(axis=1) > 0).sum()),
                               "SEL_Z": SEL_Z, "SEL_MIN_GENES": SEL_MIN_GENES, "SEL_MAD_FLOOR": SEL_MAD_FLOOR,
                               "RMS_CLIP": RMS_CLIP, "line_z_threshold": t_line},
        "gmt": gmt}

    # ---- README.md
    tables = {"genes.parquet": list(gtab.columns), "drug_effects.parquet": DRUG_EFFECTS_SCHEMA.names,
              "line_effects.parquet": le_cols, "drug_line_top.parquet": list(dlt.columns),
              "drugdoses.parquet": list(ddt.columns), "drugs.parquet": list(drugs_df.columns),
              "lines.parquet": list(lt.columns), "drug_line_response.parquet": dlr_cols,
              "plates.parquet": list(plates_df.columns), "wells.parquet": list(wt.columns)}
    text, undocumented = readme(tables, cal, cc_info, counts)
    _write_text(os.path.join(od, "README.md"), text)
    if undocumented:
        log(f"  WARNING: columns without a description in README.md: {', '.join(undocumented)}")

    info = {"version": VERSION, "genes": gK, "drugdoses": Dn, "lines": L, "wells": N, "chunk": int(chunk),
            "rows": {"genes": len(gtab), "drug_effects": n_fx, "drug_effects_clean": n_clean_rows,
                     "line_effects": n_le, "drug_line_top": len(dlt), "drugdoses": len(ddt), "drugs": len(drugs_df),
                     "lines": len(lt), "drug_line_response": n_dlr, "plates": len(plates_df), "wells": len(wt)},
            "tp53_source": tp53_src, "tp53_counts": {str(k): int(v) for k, v in pd.Series(tp53).value_counts().items()},
            "genes_with_clean_inducer": int(((gtab["best_clean_up_q"] < Q_CUT)
                                             & (gtab["best_clean_up_fold"] >= 2 ** LFC_MIN)).sum()),
            "genes_with_clean_repressor": int(((gtab["best_clean_down_q"] < Q_CUT)
                                               & (gtab["best_clean_down_fold"] <= 2 ** -LFC_MIN)).sum()),
            "n_measured_line_gene_pairs": int(measured.sum()),
            "cell_cycle_rule": cc_info, **cal, **counts,
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
DOSE_PLATE = ("Each dose of a drug sits on its own plate (drugs.parquet dose_plates; for most drugs the same well on "
              "three plates), so the pattern compares plates as much as doses.")
ONE_WELL = ("Lines are counted inside the drug-dose's well(s). Most drug-doses are one well (n_wells), so the lines "
            "are not replicate treatments.")
DMSO_DOC = ("rough DMSO-referenced log2 fold change: lfc plus how far the plate's two DMSO wells sit below its "
            "drug-well median (atlas plate_offset; DMSO wells are always H11/H12, plate13 B11/B12, and are not "
            "corrected for position or composition). A sign check, not a replacement: when most drugs on a plate "
            "raise a gene, lfc reads lower than lfc_vs_dmso. NaN when the plate has no usable DMSO value for the "
            "gene.")
TAHOE_ANN = "Tahoe's annotation, verbatim (Tahoe drug metadata): "
CHEMBL_ANN = "ChEMBL (reference/drug_annotations.parquet; the release is in reference/sources.json): "
FLAGS_DOC = ("drug-dose flags of record (drugdoses.parquet flags) + this gene's flags ('noisy plate (z scaled)' from "
             "its own plate factor, 'position correction uncertain', 'position effect removed'), '; '-joined: the "
             "exact strings of the atlas and of the tables stage, with three per-gene readings. 'cell-cycle shift' "
             "reads 'cell-cycle shift (explains ~N% here)' where the shift is not the explanation of this gene's "
             "change (N = round(100 x cc_share); no artifact flag). 'like a neighbouring well' and 'like a "
             "neighbouring well (top dose)' read 'like a neighbouring well (not this gene)' where no neighbour moves "
             "this gene the same way (no artifact flag; see 'Neighbouring wells'). 'translation inhibitor' reads "
             "'rise under a translation inhibitor' where the gene rises (lfc > 0; a per-line cell: its own per-line "
             "lfc > 0) and is left out where it does not (a class caveat; see 'Drug classes used by rules')")
CLEAN_DOC = ("True when flags hold no artifact flag (common.has_artifact: toxic, transcription drop, cell-cycle shift, "
             "unreliable plate only, position not correctable, position correction uncertain, wells disagree, like a "
             "neighbouring well). The caveats never change it. Rows that are not clean are kept: read them with their "
             "flags")
_BEST = {"dd": "drug-dose row (-1 = none)", "drug": "drug", "dose": "dose key (uM)",
         "fold": "pooled fold change (linear; 2**lfc; " + _FC + ")", "z": "pooled z (DD_z)",
         "q": "BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all "
              "drug-doses)", "flags": "the drug-dose's flags of record + this gene's flags, read per gene as in "
              "drug_effects flags (e.g. 'cell-cycle shift (explains ~N% here)', 'like a neighbouring well (not this "
              "gene)', 'rise under a translation inhibitor'), '; '-joined"}


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
                      "PROTEASOME module columns are not here). 'Clean' = the drug-dose's flags of record plus this "
                      "gene's flags hold none of: toxic, transcription drop, cell-cycle shift (only where the shift is "
                      "the explanation of this gene's change: see 'Cell-cycle shift'), unreliable plate only, position "
                      "not correctable, position correction uncertain, wells disagree, like a neighbouring well (only "
                      "for the genes a neighbouring well moves the same way: see 'Neighbouring wells'). n_dd_up / "
                      "n_dd_down and "
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
         "flags": FLAGS_DOC, "clean": CLEAN_DOC, "n_lines_measured": "lines with a "
         "per-line value (truly expressing the gene, enough cells in the wells, >= 2 expected counts)", "n_lines_up":
         "lines with per-line z >= 2 and fold >= 1.2: where the pooled effect shows up (descriptive; at z >= 2 a "
         "line also passes by chance, at the rate lines_up_chance_rate of tables/info.json). " + ONE_WELL,
         "n_lines_down": "lines with per-line z <= -2 and fold <= 1/1.2 (descriptive, as n_lines_up). " + ONE_WELL,
         "lines_up":
         "cell names of those lines, strongest per-line z first, at most 12, ', '-joined", "lines_down":
         "cell names of the lines counted in n_lines_down, most negative per-line z first, at most 12",
         "pattern_up": "how the increase behaves over the drug's "
         "doses (atlas dose_shape over the pooled z by ascending dose; the same for every dose of the drug): none / "
         "single dose / all doses, stronger at high dose / all doses, flat / top dose only / rises with dose / two "
         "highest doses / inconsistent across doses. " + DOSE_PLATE,
         "pattern_down": "the same for the decrease (z negated). " + DOSE_PLATE,
         "cc_share": "at a drug-dose whose flags include 'cell-cycle shift': the share of this gene's change that the "
         "shift would explain, |bS x S + bG x G| / |lfc| with the gene's slopes (genes.parquet cc_slope_S, "
         "cc_slope_G2M, here fitted again without this drug-dose when it is in the fit: leave-one-out) and the "
         "drug-dose's S_PHASE_lfc / G2M_PHASE_lfc; 0 when that predicted part "
         "goes the other way; at most 1. NaN for drug-doses without the flag (or genes without slopes). The flag "
         "stays an artifact flag unless 2 x cc_share < 0.5 and |lfc| x (1 - 2 x cc_share) >= log2 1.2 (see "
         "'Cell-cycle shift')",
         "n_wells": "the drug-dose's used wells (drugdoses.parquet n_wells). Most drug-doses are one well, so the "
         "per-line values of one drug-dose come from one treatment",
         "lfc_vs_dmso": DMSO_DOC}),
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
         "best_up_flags": "best_up_dd's flags for this gene (clean, so only caveats: e.g. 'rise under a translation "
         "inhibitor', read from the per-line change; 'like a neighbouring well (top dose)'; null = none passes or no "
         "flag)",
         "best_down_flags": "best_down_dd's flags for this gene (caveats only; null = none passes or no flag)",
         "n_dd_up_all": "n_dd_up over all drug-doses (flagged ones included). Chance passes grow with the number of "
         "drug-doses: line_z_expected_chance_all of tables/info.json",
         "n_dd_down_all": "n_dd_down over all drug-doses (flagged ones included)",
         "best_up_dd_all": "the drug-dose counted in n_dd_up_all with the highest per-line z in this line, flagged or "
         "not (-1 = none passes); equal to best_up_dd when that one is clean",
         "best_up_drug_all": "its drug", "best_up_dose_all": "its dose key (uM)",
         "best_up_lfc_all": "its per-line log2 fold change", "best_up_z_all": "its per-line z",
         "best_up_flags_all": "its flags for this gene (as drug_effects flags, but 'rise under a translation "
         "inhibitor' read from this per-line change; null = none passes)",
         "best_up_clean_all": "True when those flags hold no artifact flag (False when none passes)",
         "best_up_cc_share_all": "its cc_share for this gene (as drug_effects; NaN without the cell-cycle flag)",
         "best_down_dd_all": "the drug-dose counted in n_dd_down_all with the lowest per-line z in this line, flagged "
         "or not (-1 = none passes)", "best_down_drug_all": "its drug", "best_down_dose_all": "its dose key (uM)",
         "best_down_lfc_all": "its per-line log2 fold change", "best_down_z_all": "its per-line z",
         "best_down_flags_all": "its flags for this gene (the translation-inhibitor token read from this per-line "
         "change; null = none passes)",
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
         "flags": "the drug-dose's flags for this gene (as drug_effects flags, but 'rise under a translation "
         "inhibitor' read from this cell's own per-line change, lfc > 0, not the pooled one)",
         "clean": "True when flags hold no artifact flag (as drug_effects clean); False = read the cell with its "
         "flags",
         "cc_share": "the share of the gene's pooled change the drug-dose's cell-cycle shift would explain (as "
         "drug_effects; NaN without the flag)"}),
    "drugdoses.parquet": (
        "atlas/effects/drugdose.csv (one row per drug and dose) plus dd, salt_base, top_up and top_down, the flags of "
        "record (flags; drugdose.csv's own are atlas_flags), the neighbouring-well rule (nb_*), the drug's mechanism "
        "classes and the lines where the drug-dose is selective.",
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
         "higher dose (NaN: none)",
         "flags": "the flags of record, '; '-joined: atlas_flags, then 'like a neighbouring well' (nb_tier "
         "'artifact': an artifact flag for the nb_genes genes a neighbour moves the same way) or 'like a "
         "neighbouring well (top dose)' (nb_tier 'top dose': a caveat), then 'translation inhibitor' (a class "
         "caveat, not a technical or artifact flag: mechanism_classes). Every table and reader uses these "
         "(tables.dd_flags_of_record)",
         "atlas_flags": "drugdose.csv's flags, verbatim (artifacts: toxic, transcription drop, cell-cycle shift, "
         "unreliable plate only, position not correctable, wells disagree; caveats: low cells (technical?), "
         "plate-row cell shift, composition shift, noisy plate (z scaled))", "n_genes_up":
         "genes raised significantly (q_up < 0.10, fold >= 1.2)", "n_genes_down": "genes lowered significantly",
         "n_sig_genes": "n_genes_up + n_genes_down", "replicate_r": "mean pairwise r of the used wells' z over the "
         "top 500 genes (wells agree?)", "targets": TAHOE_ANN + "drug targets", "moa_fine":
         TAHOE_ANN + "mechanism of action, fine", "moa_broad": TAHOE_ANN + "mechanism of action, broad",
         "approved": "human-approved (Tahoe drug metadata)", "top_up": "up to 15 significantly raised genes, highest "
         "z first: 'LABEL (fold x)' (all of them: drug_effects.parquet and drugdose_signatures.gmt)",
         "top_down": "up to 15 significantly lowered genes, lowest z first: 'LABEL (fold x)' (all of them: "
         "drug_effects.parquet and drugdose_signatures.gmt)",
         "nb_tier": "the neighbouring-well rule (see 'Neighbouring wells'): '' = none; 'artifact' (flagged on the "
         "nb_genes genes); 'top dose' (an alert at the drug's top dose, not flagged); 'same mechanism' (a note: the "
         "neighbour has the same annotated mechanism, probably a real class effect; not flagged); 'dose response' (a "
         "note: the drug's lower doses already move its strongest shared genes the same way; not flagged)",
         "nb_partner_dd": "drug-dose row of the main neighbour (strongest tier, then the largest nb_share; -1 = none)",
         "nb_partner": "that neighbour: 'drug dose µM' ('' = none)",
         "nb_where": "where the two wells touch, per plate: 'plate10 F1 next to G1' (this drug-dose's well first), "
         "'; '-joined",
         "nb_partners": "every neighbour that gave this drug-dose a tier (drug-dose rows, ','-joined, the main one "
         "first); the token's genes are those any of them moves the same way",
         "nb_n_sig": "significant genes of this drug-dose with noise RNAs left out (the rule needs >= 30 to judge it)",
         "nb_shared": "of those, the genes the main neighbour moves the same way at |z| >= 3 (-1 = no tier)",
         "nb_share": "nb_shared / nb_n_sig (J; the rule needs >= 0.5; NaN = no tier)",
         "nb_top_share": "share of the neighbour's 30 strongest significant genes that this drug-dose moves the same "
         "way at |z| >= 3 (T; the rule needs >= 0.3; NaN = no tier)",
         "nb_other_doses_share": "the largest share of the shared genes that one of this drug's other doses moves the "
         "same way at |z| >= 3 (its higher doses; at the top dose the lower ones; for a partner every other dose); "
         "a tier needs < 0.2 (NaN = no tier)",
         "nb_partner_own_share": "the same for the neighbour's other doses: >= 0.2 = the neighbour shows these genes "
         "at its other doses too, so they are its own signature (NaN = no tier)",
         "nb_genes": "genes carrying the token: this drug-dose moves them and a neighbour moves them the same way at "
         "|z| >= 2 (0 without a token: no tier or 'same mechanism')",
         "nb_alert": "the rule's finding in plain words ('' = none)",
         "mechanism_classes": "the drug's mechanism classes with their sources (tahoemap/mechanisms.py class_text: "
         "code constants of tahoemap/data/drug_classes.json, ChEMBL mechanisms, WHO ATC codes); '' = none",
         "n_selective_lines": "lines where this drug-dose is selective (drug_line_response.parquet selective)",
         "selective_lines": "every selective line by sel_z, highest first: 'NCI-H23 (6.1), HOP62 (5.4)' (never cut; "
         "'' = none)"}),
    "drugs.parquet": (
        "One row per drug (all its doses), with Tahoe's and ChEMBL's annotations side by side (see 'Drug "
        "annotations: Tahoe and ChEMBL') and where each dose sits (dose_plates; see 'Dose and plate').",
        {"drug": _DD_COLS["drug"], "salt_base": _DD_COLS["salt_base"], "targets": TAHOE_ANN + "drug targets",
         "moa_fine": TAHOE_ANN + "mechanism of action, fine", "moa_broad": TAHOE_ANN + "mechanism of action, broad",
         "approved": "human-approved",
         "n_doses": "number of doses", "doses": "dose keys by ascending concentration (uM), ' / '-joined",
         "n_sig_by_dose": "significant genes (n_sig_genes) per dose, same order", "max_sig": "the largest of them",
         "best_dose": "the dose with the most significant genes (tie -> the higher dose)", "best_dd":
         "its drug-dose row", "lowest_active_dose": "the lowest dose such that it and every higher dose have >= 10 "
         "significant genes; 'low dose only (noise?)' when only lower doses do; '' when no dose does. " + DOSE_PLATE,
         "flags_by_dose": "each dose's flags of record ('-' = none), ' / '-joined by ascending dose",
         "signature_r_between_doses": "cosine similarity of the pooled z signatures (genes significant in >= 3 "
         "drug-doses) of consecutive doses (low-mid / mid-high): near 1 = the same response growing with dose. "
         + DOSE_PLATE,
         "dose_plates": "where each dose sits: '0.05: plate10 G1 / 0.5: plate11 G1 / 5: plate12 G1' (ascending dose; "
         "each dose's used wells as 'plate well')",
         "doses_share_a_plate": "True when two doses of the drug have used wells on the same plate (usually False: "
         "each dose sits on its own plate)",
         "mechanism_classes": "the drug's mechanism classes with their sources (as drugdoses.parquet)",
         "chembl_id": CHEMBL_ANN + "molecule id ('' = not matched; ' + '-joined for combinations)",
         "chembl_name": CHEMBL_ANN + "preferred name",
         "chembl_mechanisms": CHEMBL_ANN + "curated mechanisms of action, '; '-joined",
         "chembl_actions": CHEMBL_ANN + "their action types (INHIBITOR, AGONIST, ...), ', '-joined",
         "chembl_targets": CHEMBL_ANN + "their target genes, ', '-joined",
         "chembl_matched_by": CHEMBL_ANN + "how the Tahoe drug was matched to the ChEMBL molecule",
         "annotation_status": "how Tahoe's and ChEMBL's annotations compare, '; '-joined status words ('ChEMBL not "
         "loaded' when the reference stage had no ChEMBL data)",
         "annotation_alert": "where Tahoe and ChEMBL disagree ('Targets differ', 'Mechanism differs', 'Action "
         "differs', 'Identity unsure'), ' | '-joined. Both are shown; Tahoe's annotation is never changed",
         "annotation_note": "other notes on the two annotations, ' | '-joined"}),
    "lines.parquet": (
        "atlas/effects/lines.csv (one row per cell line, in the order of the line axis) plus line, tp53_status, "
        "n_dd_depleted, n_dd_depleted_clean, median_response.",
        {"line": "line index (last axis of the tensor)", "cell_line_id": "Cellosaurus id", "n_cells_total":
         "cells of the line over all wells", "cell_name": "cell line name", "Cell_ID_DepMap": "DepMap id",
         "Organ": "organ of origin", "drivers": "driver genes with their variant type, GENE(Type), '; '-joined (Tahoe "
         "cell-line metadata)", "driver_changes": "protein changes, GENE p.X123Y, '; '-joined",
         "in_growth_analysis": "True when the line has enough cells for "
         "the relative-abundance (growth) analysis", "wells_usable": "wells with >= min_cells cells of the line "
         "(usable expression)", "pct_wells_usable": "the same as % of all wells", "tp53_status": "altered (a TP53 "
         "row in the Tahoe cell-line metadata) / not recorded (no TP53 alteration in the metadata, which lists "
         "driver alterations only: presumed wild type, not confirmed) / unknown",
         "n_dd_depleted": "drug-doses that deplete the line: relative-abundance z (DD_Az) <= -3, leaving out only "
         "drug-doses whose cell counts are untrustworthy (unreliable plate only, position not correctable, wells "
         "disagree); toxic, transcription drop and cell-cycle shift drug-doses count (depletion is what makes them "
         "toxic). -1 = not measured: the line is not in the growth analysis (too few cells). = the count of "
         "depleted & abundance_trusted & in_growth_analysis in drug_line_response.parquet",
         "n_dd_depleted_clean": "the same among clean drug-doses only (no artifact flag of record at all; "
         "drug_line_response.parquet clean); -1 = not measured",
         "median_response": "median over drug-doses of the line's response strength (DD_beta: "
         "slope of the line's changes on the drug-dose's consensus over its significant genes; 1 = a typical line, "
         "0 = no response; only drug-doses with >= 20 significant genes)"}),
    "drug_line_response.parquet": (
        "One row per drug-dose x cell line (every pair, measured or not): how strongly the line responds (genes "
        "beyond the calibrated per-line |z| cut), whether the drug-dose is selective for the line, and the line's "
        "growth and response strength from the atlas (DD_A, DD_Az, DD_beta, DD_rcor). Lines are counted inside the "
        "drug-dose's well(s); most drug-doses are one well (drugdoses.parquet n_wells), so a line's value is one "
        "treatment, not replicates.",
        {"dd": _DD_COLS["dd"], "drug": _DD_COLS["drug"], "dose": _DD_COLS["dose"], "conc": _DD_COLS["conc"],
         "line": "line index (row of lines.parquet)", "cell_line_id": "Cellosaurus id", "cell_name": "cell line name",
         "measured": "True when the line has a per-line profile for this drug-dose (some gene has a per-line z)",
         "n_genes": "genes with |per-line z| >= line_z_threshold (the calibrated cut of tables/info.json) in this "
         "line: n_up + n_down. -1 = not measured in this line",
         "n_up": "genes with per-line z >= line_z_threshold (-1 = not measured in this line)",
         "n_down": "genes with per-line z <= -line_z_threshold (-1 = not measured in this line)",
         "rms_z": "root mean square of the per-line z over the line's measured genes, each z clipped at +-10: the "
         "overall size of the line's response (NaN = not measured in this line)",
         "rel_log2": "log2((n_genes + 1) / (median n_genes of the line over its measured drug-doses + 1)): how many "
         "genes this drug-dose moves in the line against the line's typical drug-dose (NaN = not measured in this "
         "line)",
         "sel_z": "(rel_log2 - its median over the drug-dose's measured lines) / max(1.4826 x MAD over those lines, "
         "0.25): how far this line stands out among the lines of this drug-dose (NaN = not measured in this line)",
         "selective": "sel_z >= 3 and n_genes >= 20 (False with fewer than 20 significant genes, or not measured "
         "in this line)",
         "in_growth_analysis": "the line is in the atlas's growth analysis (lines.parquet in_growth_analysis) and "
         "has relative-abundance values; False = not in the growth analysis (too few cells)",
         "log2_rel_abundance": "relative abundance after 24 h (atlas DD_A): the line's share of the well's cells "
         "against the plate's drug wells, log2; compositional (when one line dies the others rise); short for "
         "cytostatic drugs. NaN = not in the growth analysis",
         "abundance_z": "its z (atlas DD_Az; NaN = not in the growth analysis)",
         "depleted": "abundance_z <= -3 (the line is depleted against the others)",
         "abundance_trusted": "the drug-dose's cell counts can be trusted: no 'unreliable plate only', 'position not "
         "correctable' or 'wells disagree' flag. lines.parquet n_dd_depleted = the count of depleted & "
         "abundance_trusted & in_growth_analysis per line (n_dd_depleted_clean also needs clean)",
         "response_strength": "how strongly the line shows the drug-dose's consensus response (atlas DD_beta: slope "
         "on the consensus over its significant genes; 1 = a typical line, 0 = no response; NaN with fewer than 20 "
         "significant genes, or not measured in this line)",
         "response_r": "the matching correlation (atlas DD_rcor; NaN as response_strength)",
         "flags": "the drug-dose's flags of record (drugdoses.parquet flags)",
         "clean": "True when flags hold no artifact flag (common.has_artifact)"}),
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


def _n(v):
    return f"{v:,}" if isinstance(v, (int, np.integer)) else ("?" if v is None else str(v))


def _plural(n, word):
    """'1 drug-dose', '3 drug-doses' ('? drug-doses' when n is unknown)."""
    return f"{_n(n)} {word}" + ("" if n == 1 else "s")


def _neighbour_text(info):
    """The 'Neighbouring wells' section of README.md (info = neighbour_wells' info)."""
    info = info or {}
    pp, dn, ex = info.get("pairs_passing") or {}, info.get("drugdoses") or {}, info.get("expected_passes") or {}
    orient = "; ".join(f"{o['orientation']} {_n(o['resembling'])} of {_n(o['judged'])}"
                       + (f" (x{o['x_far_share']:g} the far share)" if o.get("x_far_share") is not None else "")
                       for o in info.get("orientation") or [])
    tiers = "; ".join(f"{r['drug']} {r['dose']} {UM}: {r['tier']}, next to {r['partner']} ({r['where']})"
                      for r in info.get("tier_drugdoses") or []) or "none"
    return [
        "## Neighbouring wells", "",
        "Two wells that touch on a plate (side by side, above/below, or at a corner) can share a signal: liquid "
        "carried over, or a local problem on that part of the plate. The tables stage checks every pair of touching "
        "wells of two different compounds (not DMSO, not on an unreliable plate; drugdoses.parquet nb_* columns, "
        "tahoemap/tables.py neighbour_wells).", "",
        f"- It judges the weaker drug-dose a of the pair when a has at least {NB_MIN_SIG} significant genes (noise "
        "RNAs left out) and its neighbour b has at least as many.",
        f"- a resembles b when b moves at least {NB_SHARE:.0%} of a's significant genes the same way at |z| >= "
        f"{NB_Z:g} (and at least {NB_MIN_SHARED} genes), and a moves at least {NB_TOP_SHARE:.0%} of b's "
        f"{NB_TOPK} strongest significant genes the same way at |z| >= {NB_Z:g}.",
        "- Then a's own other doses decide (doses flagged 'unreliable plate only' are left out). A real drug effect "
        "shows at the drug's higher doses.",
        f"- If a has higher doses and none of them moves {NB_OTHER:.0%} or more of the shared genes the same way, "
        "a gets 'like a neighbouring well'. This is an artifact flag, but only for the genes a neighbour moves the "
        f"same way at |z| >= {NB_GENE_Z:g}. a's other genes read 'like a neighbouring well (not this gene)', which "
        "is no artifact flag.",
        f"- At the drug's top dose there is no higher dose to check. If its lower doses move less than "
        f"{NB_OTHER:.0%} of the shared genes, a gets 'like a neighbouring well (top dose)': an alert, not an "
        "artifact flag. Its alert says how many touching pairs would pass at a top dose by chance (the rate of the "
        "pairs 3 or more wells apart). If the two compounds share an annotated mechanism (Tahoe moa_fine, Tahoe "
        "targets, or a drug class), it is probably a real class effect: a note in nb_alert, no token. If one of "
        f"a's lower doses already moves at least {NB_DOSE_MIN} of a's {NB_DOSE_TOPK} strongest shared genes the "
        f"same way (|z| >= {NB_Z:g}), the drug's own effect grows with the dose: tier 'dose response', a note, no "
        "token. Lower doses are never exempted.",
        "- Old rule (version 5): no 'dose response' tier, and no chance rate in the alert. RMC-6236 5 µM (next to "
        "Trametinib 5 µM) carried the top-dose caveat on 498 genes, although ETV5 (0.85x, 0.67x, 0.18x), SPRY4 and "
        "EGR1 already fell at its lower doses: a dose response, not a carried-over signal. New rule (version 6): "
        "the 'dose response' tier above.",
        f"- If b's own other doses also move less than {NB_OTHER:.0%} of the shared genes, neither compound shows "
        "them elsewhere. b then gets the same tier, with a as its partner.",
        "- Nothing is removed: every value stays in the tables, with its flags and the drug-dose's nb_alert.", "",
        f"This run: {_n(info.get('pairs_judged'))} touching pairs judged. Passing pairs: "
        + ", ".join(f"{t} {_n(pp.get(t))}" for t in NB_TIERS) + ". Drug-doses: "
        + ", ".join(f"{t} {_n(dn.get(t))}" for t in NB_TIERS) + ". Expected by chance, from the pairs 3 or more "
        "wells apart: " + ", ".join(f"{t} {_n(ex.get(t))}" for t in NB_TIERS)
        + " (an upper bound: far pairs include real class copies). Resembling pairs among the judged ones, by "
        f"placement: {orient or 'none'}.", "",
        f"Drug-doses with a tier: {tiers}.", "",
        "Changed in tables version 5. Old rule: clean = no atlas artifact flag. New rule: also not like a "
        "neighbouring well for that gene. Reason: touching wells share signatures 3.5 to 4 times more often than "
        f"wells 3 or more apart (validation report), e.g. Citalopram 0.05 {UM} next to Clobetasol propionate on "
        "plate10.", ""]


def _classes_text(tl):
    """The 'Drug classes used by rules' section of README.md (tl = info.json translation_inhibitors)."""
    tl = tl or {}
    rules = M.load_rules()
    tl_classes = [k for k, v in (rules.get("classes") or {}).items() if v.get("effect") == "translation"]
    out = ["## Drug classes used by rules", "",
           "Some rules need a drug's mechanism class. The classes, their members and their sources are code "
           "constants in tahoemap/data/drug_classes.json (cited), read with ChEMBL's mechanisms and WHO ATC codes "
           "by tahoemap/mechanisms.py. Tahoe's own annotation is never a class rule.", ""]
    for k in tl_classes:
        ci = M.class_info(k)
        out.append(f"**{ci.get('label', k)}** (class {k}; effect '{ci.get('effect')}'): {ci.get('why', '')}. Source: "
                   f"{ci.get('source', '')}.")
    members = tl.get("class_text") or {}
    out += ["", "Members in this run: " + ("; ".join(f"{d} ({t})" for d, t in members.items()) or "none") + ".", ""]
    nm = tl.get("not_members") or {}
    for k, v in nm.items():
        out.append(f"Not members of {k}, with the reason: " + "; ".join(f"{m}: {r}" for m, r in v.items()) + ".")
    out += ["",
            f"Rule: every drug-dose of a member gets '{TL_DD}' in its flags of record. It is a class caveat, not a "
            f"technical or artifact flag. Per gene it reads '{TL_RISE}' where the gene rises (lfc > 0) and is left "
            "out where it does not. A per-line cell (drug_line_top, line_effects best_*) reads its own per-line "
            "change: a fall in one line never reads as a rise there (version 6; version 5 read the pooled sign). It "
            "never changes clean. " + FLAG_TEXT[TL_RISE],
            f"This run: {_n(tl.get('drugdoses'))} drug-doses carry it; {_n(tl.get('drug_effects_rows_rise'))} "
            f"drug_effects rows read '{TL_RISE}'.", ""]
    return out


def _annotation_text(ann, release):
    """The 'Drug annotations: Tahoe and ChEMBL' section of README.md (ann = annotation_counts)."""
    ann = ann or {}
    st = "; ".join(f"{k} {_n(v)}" for k, v in (ann.get("status") or {}).items()) or "none"
    return ["## Drug annotations: Tahoe and ChEMBL", "",
            "drugs.parquet shows two annotations of each drug. targets, moa_fine and moa_broad are Tahoe's annotation, "
            f"verbatim. The chembl_* columns come from {release} (reference/drug_annotations.parquet; the reference "
            "stage fetches them and keeps a cached copy). Both are shown. An alert marks where they disagree. Tahoe's "
            "annotation is never changed.",
            f"This run: {_n(ann.get('drugs'))} drugs; {_n(ann.get('chembl_matched'))} matched in ChEMBL; "
            f"{_n(ann.get('with_chembl_mechanism'))} with a ChEMBL mechanism; {_n(ann.get('alerts'))} with an "
            f"annotation_alert; {_n(ann.get('with_mechanism_class'))} in a mechanism class. Status words: {st}."
            + (" ChEMBL was not loaded in this run (offline and not cached), so the chembl_* columns are empty and the "
               "classes come from the code constants only." if (ann.get("status") or {}).get(M.NOT_LOADED) else ""),
            ""]


def _dose_plate_section(dp):
    """The 'Dose and plate' section of README.md (dp = info.json dose_and_plate)."""
    dp = dp or {}
    nw = "; ".join(f"{_plural(v, 'drug-dose')} with {_plural(int(k), 'well')}"
                   for k, v in (dp.get("n_wells") or {}).items())
    rep_ = "; ".join(f"{r['plates'][0]} and {r['plates'][1]} ({_n(r['drugdoses_shared'])} drug-doses on both; "
                     f"{_n(r['drugdoses'][0])} and {_n(r['drugdoses'][1])} on each)"
                     for r in dp.get("replicate_plates") or []) or "none"
    return ["## Dose and plate", "",
            DOSE_PLATE + " A change between doses can be a plate difference. " + ONE_WELL,
            f"This run: {nw or 'no drug-doses'}. {_n(dp.get('three_dose_drugs_on_3_plus_plates'))} of "
            f"{_n(dp.get('three_dose_drugs'))} three-dose drugs have their doses on 3 or more plates; "
            f"{_plural(dp.get('drugs_with_doses_sharing_a_plate'), 'drug')} with two doses on one plate. Replicate "
            f"plates (two plates that share at least half of one plate's drug-doses): {rep_}.", ""]


def readme(tables, cal=None, cc=None, counts=None):
    """README.md text for the written tables ({file: [columns]}) and the columns lacking a description; cal = the
    per-line |z| calibration (calibrate_line_z), cc = the cell-cycle rule's counts (_cc_summary) and counts = the
    tables stage's other counts (neighbour_rule, translation_inhibitors, dmso_sign_changes, dose_and_plate,
    annotations, drug_line_response, gmt, chembl_release), whose numbers the text quotes."""
    counts = counts or {}
    dm = counts.get("dmso_sign_changes") or {}
    gmt = counts.get("gmt") or {}
    flag_words = [f"- '{k}': {v}" for k, v in FLAG_TEXT.items()]
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
           "**DMSO sign check**: every fold change here is against the typical drug well on the same plate, not "
           "against DMSO. drug_effects `lfc_vs_dmso` is a " + DMSO_DOC + f" This run: {_n(dm.get('sign_changes'))} "
           f"of {_n(dm.get('rows'))} drug_effects rows change sign against DMSO at 1.2x or more "
           f"({_n(dm.get('no_dmso_value'))} rows have no DMSO value; per plate: tables/info.json dmso_sign_changes).",
           "",
           f"**Significant** (as the atlas): q_up < {Q_CUT:g} and fold >= 1.2 (up), q_down < {Q_CUT:g} and fold <= "
           "1/1.2 (down); q = Benjamini-Hochberg within each gene over all drug-doses. **Clean** = no artifact flag "
           "(" + ", ".join(ARTIFACT_FLAGS) + ") in the drug-dose's flags of record plus the gene's own flags (a "
           "cell-cycle shift counts only where it is the explanation of the gene's change, a neighbouring-well flag "
           "only for the genes the neighbour moves the same way: see below). The flags of record "
           "(drugdoses.parquet flags) are the atlas's flags plus the tables stage's neighbouring-well and "
           "translation-inhibitor tokens; drugdoses.parquet atlas_flags keeps the atlas's own. Soft caveats "
           "that do not make a value unclean: low cells (technical?), plate-row cell shift, composition shift, noisy "
           "plate (z scaled), position effect removed, " + ", ".join(f"'{x}'" for x in (NB_TOP, NB_CLEARED, TL_DD,
                                                                                       TL_RISE)) + ". "
           "**Flagged values are kept**: every table lists flagged "
           "drug-doses in their ranked place with their flags (and `clean` = False); only estimates (the per-line "
           "|z| calibration, response_sd, the cell-cycle slopes) leave artifact-flagged drug-doses out.", "",
           "Missing values: NaN / null = not measured (line not expressing, too few cells or counts) or no "
           "candidate; -1 in an index or count column = none / not measured.", "",
           "**Flags added by the tables stage** (their plain words, common.FLAG_TEXT):"] + flag_words + [""] \
        + _calibration_text(cal) + _cell_cycle_text(cc) + _neighbour_text(counts.get("neighbour_rule")) \
        + _classes_text(counts.get("translation_inhibitors")) \
        + _annotation_text(counts.get("annotations"), counts.get("chembl_release") or "ChEMBL") \
        + _dose_plate_section(counts.get("dose_and_plate")) \
        + ["## drugdose_signatures.gmt", "",
           "For every drug-dose two gene sets, '<drug> <dose> µM up' and '<drug> <dose> µM down', with every gene "
           "whose call is up / down (q < 0.10 and fold >= 1.2 that way; no cap), for gene-set tools. The description "
           f"field gives the drug-dose row and its flags of record. This run: {_n(gmt.get('written'))} of "
           f"{_n(gmt.get('sets'))} sets written (a set with no gene is not written).", ""]
    release = counts.get("chembl_release")
    for name, cols in tables.items():
        intro, docs = DOCS[name]
        out += [f"## {name}", "", intro, "", "| column | meaning |", "|---|---|"]
        for c in cols:
            d = docs.get(c)
            if d is None:
                missing.append(f"{name}:{c}")
                d = "(see atlas/effects/README_effects.md)"
            if release:                                     # name this run's ChEMBL release
                d = d.replace(CHEMBL_ANN, f"{release} (reference/drug_annotations.parquet): ")
            out.append(f"| `{c}` | {d.replace('|', '/')} |")
        out.append("")
    out += ["The gene x gene table ('relative to each gene') is relations/gene_relations.parquet.", ""]
    return "\n".join(out), missing
