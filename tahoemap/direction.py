"""direction - probable DIRECTION between genes (which one acts upstream of the other), from the screen's cell lines.

The relations stage links genes symmetrically (two genes respond alike: a cosine). This stage adds directed edges
SOURCE -> TARGET. Each edge comes from a statistical test (a p-value and a Benjamini-Hochberg q), carries an evidence
grade (A, B or C) and its alerts in plain words ('' or '⚠ ' + every reason, '; '-joined, as the relations stage writes
them). The rule for everything shown: nothing that passes its test is dropped because of doubt - a doubtful edge keeps
its place with its alerts and a lower grade - but a pair without a test result at q < 0.10 is not an edge (it is not a
result). Everything is computed by this code from the run's own tables; no edge is edited by hand.

What "direction" means here: the SOURCE is the gene whose state (a recorded mutation, its absence, its level, or a
drug that targets it) is the variable the test conditions on, and the TARGET's level, drug response or the cells'
growth is what changes with it. A recorded mutation of the source is fixed before the experiment, so it cannot be a
consequence of the target: that is what makes the arrow point one way. It is not proof of direct regulation (A -> B
-> C looks like A -> C; another alteration of the same lines can be the cause), there is one time point (~24 h), and
drugs act on proteins, not on mRNA.

Inputs: tensor/DDL_z.npy, DDL_lfc.npy (genes x drug-doses x lines; read in gene chunks), tensor/line_measured.npy;
atlas/effects line_cpm, drugdose.csv, genes.csv, lines.csv, DD_z / DD_qup / DD_qdn / DD_lfc (pooled), DD_A / DD_Az
(each line's log2 relative abundance per drug-dose, and its z: what tables.py counts for lines.n_dd_depleted); the
Tahoe cell-line metadata (Driver_* columns, and Organ where lines.csv has none; found with --data DATA, else through
atlas/file_index.json as tables.py does); relations/gene_relations.parquet (related pairs; optional);
tables/drugdoses.parquet (salt forms; optional).

Per gene Y, its RESPONSE (used by every response test):
  drug-doses   Y's K = 10 drug-doses with the largest pooled |z| (atlas DD_z), artifact-flagged ones included (their
               flags go into the alerts). The atlas's significance (q < 0.1 and >= 1.2x, or |z| >= 3) is not required:
               the pooled value is the median line, so a response that only part of the lines show - exactly what a
               genotype explains, e.g. a p53 response in the TP53-wild-type lines only - rarely reaches it, while it
               still ranks among the gene's strongest. A gene none of whose K drug-doses is significant is tested and
               says so ('none of its drug-doses is significant pooled'). The choice uses no line labels, so the
               permutation tests below stay valid.
  per line     r[Y, d, l] = per-line z (DDL_z) x sign of the pooled z, clipped at +-10; NaN where the line does not
               express Y (line_measured) or has no value at d.
  global       a line may respond less to a drug in general (TP53-mutant lines resist DNA damage; a line with an
  sensitivity  efflux pump takes up less drug; the per-line z grows with the cells a line contributes, so a line with
               fewer cells responds less everywhere), and then every gene that responds there looks dependent on what
               those lines carry. Y is judged against the line's relative responsiveness s[Y, d, l], at every one of
               its K drug-doses (whether or not Y is significant there pooled; no labels are used):
               - drug-specific (adj_kind 2): the mean over the drug-dose's responsive genes (pooled q < 0.1 and >=
                 1.2x, or |z| >= 3; its REF_MAX = 500 strongest) of their r in line l (each signed by its own pooled
                 direction), leaving out Y and Y's related genes (relations: its top partners, either way) - with Y's
                 own programme left in, a drug-dose whose response is mostly that programme would cancel it -, used
                 when >= 50 such genes remain in more than half the lines and their mean is >= 0.5; s = that mean /
                 its mean over the lines;
               - line-wide (adj_kind 1), elsewhere: per drug-dose with >= REF_LINE_GENES = 10 responsive genes whose
                 mean response is >= 0.5, their mean per line / its mean over the lines; s = the median of that over
                 those drug-doses (robust to one drug class or one programme dominating), normalised to mean 1 -
                 used only when reliable: >= REF_LINE_DD = 20 such drug-doses of >= 20 compounds, and either a
                 negligible spread (SD < 0.1) or reproduced by two random halves of the compounds (correlation of
                 their medians across lines >= 0.5; a median of a few drug-doses that all carry line-dependent
                 programmes would follow those, not the lines' responsiveness; info.json global_sensitivity_correction);
               - none (adj_kind 0) when neither exists.
               The model is multiplicative: Y's expected response in line l scales with s, so the corrected response
               is a = r - b (s - 1), b = Y's mean response over the lines: a line that responds 0.3x as strongly
               overall is expected to show 0.3x of Y's typical response, and only the rest counts.
  summary      no imputation: R[Y, l] = mean of a over the drug-doses with a value in line l (R_raw: of r); lines
               that do not express Y stay out of every mean (mask M).
The correction has a blind spot, which the edges report: when most of a drug-dose's other responsive genes are
themselves one programme that depends on the genotype, their damping in the altered lines looks like general
resistance, and a gene that responds the same everywhere comes out as 'responds more where X is altered'. So each
response edge also carries the evidence without the correction (raw_share = sum over Y's drug-doses of the squared
uncorrected scores in the edge's direction / the same corrected): below RAW_SHARE_MIN = 0.25 the edge rests on the
correction - it is kept, alerted with how much the reference itself differs between the sides, and not graded A.
Drug-doses carrying the difference without any correction are counted in the alerts; when they carry >= half of the
evidence the edge is not graded A.

Evidence kinds (edge kind = column 'kind'):
1. genotype_response, genotype_baseline, genotype_sensitivity (grade A, B or C). Groups: per driver gene X recorded
   in the metadata, the screened lines with a loss-of-function record (Driver_Mech_InferDM LoF), with a gain-of-
   function record (GoF), and 'altered (any record)' when some records carry no mechanism or both occur, each tested
   when >= 3 lines carry it and >= 3 recorded lines have no record of X at all ('not recorded' - which is not proof
   of wild type: a line may carry an unlisted variant). Lines with another kind of X record are left out of that
   comparison.
   - response: per drug-dose k of Y's K, the two-sample t of a between the intact and the altered lines (each
     side over the lines measured there, >= 2 each; pooled within-side variance floored at 0.1 x the variance over
     the group's lines) as a normal score z_k = sign(t) sqrt((nu - 1/2) ln(1 + t^2 / nu)), nu = n - 2 (within ~0.05
     of the exact normal quantile for nu >= 4, so rows with different numbers of lines share one null shape). The
     statistic is S = sum over k of z_k^2: an omnibus over Y's drug-doses, so a dependence carried by one drug class
     counts as much as one spread over all of them. One-sided (S is large when the sides differ either way); the
     sign is the dominant direction, sign(sum z_k |z_k|), with an alert when >= 25% of the evidence goes the other
     way. Effects reported: D(X, Y) = mean over the intact lines - mean over the altered lines of R (>= 3 measured
     lines each side; D > 0: Y responds less where X is altered), D_raw (the same on R_raw), retained_fraction =
     altered / intact mean of R_raw, raw_share, and per drug-dose the contrast and the folds on each side
     (top_drugdoses: fold in the altered lines vs fold in the other lines).
   - baseline: the same t / z on Y's baseline level log2(line CPM + 1) (all lines of the group); two-sided.
   - sensitivity: the same on each drug-dose's log2 relative abundance (DD_A), target 'cells under DRUG DOSE'.
   Null: the group labels are permuted P = 200 times (no permutation equal to the observed labels), within organ
   strata when the strata allow >= 100 distinct arrangements (else across organs, alerted). Sums and sums of squares
   are linear in the labels, so all permutations of all targets are a few matrix products. Each target's statistic
   is standardised by its own permutation mean and SD (T = (S - mean) / SD; under stratified permutation the mean
   absorbs the organ composition); the permutation T of all targets of the group form one pooled null (up to
   2,000,000 values); T is first divided by the group's inflation (genomic control: the interquartile range of the
   observed T over all >= 200 tested targets / that of the null, when > 1 - a grouping that coincides with broad
   structure among the lines shifts many genes together). p = (1 + #{T_null >= T}) / (1 + #null) (on |T| when two-
   sided) where >= 10 null values reach T; beyond, a generalized-Pareto tail fitted to the 250 largest null values
   (shape >= 0, never lighter than exponential), so p has no floor at 1 / #null. The pooled null assumes every
   target's standardised statistic has the same null shape; per target this is checked against its own 200
   permutations, and its own permutation p is used instead when larger and (a) its own permutations contradict the
   pooled p (binomial P(X >= its exceedances) < 0.01) or (b) it has few arrangements (< 1,000 over its lines, or its
   permutation values take < half distinct values: a target measured in few lines, or few lines per organ) - then p
   is also kept >= 1 / its arrangements (alert: its own permutation p is used).
   q: BH over every test of the kind across ALL genotype groups (one family per kind: the share of false edges is
   controlled over the table, not group by group) and q_group: BH within the group. An edge is written when q_group
   < 0.10 (a test significant over the table only because other groups have many hits is not significant in its own
   family); grade A / B also need q < 0.10, else the edge is grade C with an alert giving the number of such edges
   random pseudo-groups give. Sign (column sign, the effect of X's ACTIVITY): LoF +direction, GoF -direction, 'any'
   0 (not inferred).
2. null_response, null_baseline, null_sensitivity (no mutation needed; grade B or C). Lines where X is not expressed
   at all - line_measured False and line CPM below tensor.AMB_FRAC x the pooled CPM, i.e. they read only ambient RNA -
   are natural knockouts when >= 3 lines lack X and >= 3 express it. The same tests as 1 (lack = altered, express =
   intact, sign as for LoF), but response and baseline only for the related pairs (X, Y) of relations (both
   orientations). Baseline levels and responses of related genes are dominated by tissue programmes, so a gene
   absent from (nearly) whole organs - no within-organ permutation possible - is compared across organs as a
   separate BH family, alerted, and grade C when its lines are concentrated in organs (tissue-confounded).
   Sensitivity is tested for the drug-doses whose effect on cell numbers differs between lines more than chance (sum
   over lines of DD_Az^2, chi-square p < 0.05). Genes absent from exactly the same lines are tested once and share
   the result (alert: any of them could be the cause). Null pooled over all tests of the kind (with its fitted
   tail), the same per-target guard; BH over all tests of the kind (within-organ and across-organ comparisons
   apart). A recorded deletion of X in the same lines is reported (genotype evidence too).
3. level, level_sensitivity (no mutation; grade C, a glimpse). X's baseline level as a continuous modulator: the
   correlation across lines between X's lineage-adjusted level (log2(CPM + 1) over the lines that express X, residuals
   on an intercept, organ indicators for organs with >= 2 lines and the top 3 principal components of the lines'
   baseline profiles) and Y's lineage-adjusted response strength (R, residualised the same way) - or, for
   level_sensitivity, a drug-dose's lineage-adjusted relative abundance (variable drug-doses as in 2). >= 8 lines.
   T = r sqrt(dof / (1 - r^2)), dof = n - k - 1 (k = covariates); p two-sided from the t distribution (no floor),
   calibrated by a Freedman-Lane null (X's residuals permuted over the lines and residualised again, for a random
   set of the tests): when its 99th percentile of |normal score| exceeds the normal's, the normal scores are divided
   by that ratio (info.json: level_calibration). level: both directions of every related pair, BH over all of them;
   the edge X -> Y is written when q < 0.10 (both ways when both pass; the direction is a flag, not a filter);
   direction_clear when |r(X level, Y response)| > |r(Y level, X response)| and p_direction < 0.05, a test that
   allows for the selection: the edge was written because its |r| passed the cut on these lines, which inflates it
   (the winner's curse), so the null is two equally strong directions with the forward drawn conditional on passing
   the same cut (Fisher z with their sampling spread and the correlation of their errors from a bootstrap over lines;
   the largest p over the common strength, from none to 0.95). A missing reverse is unclear. Every level edge
   carries the alert that a stronger correlation one way can reflect how precisely, or how closely to a shared cause,
   each gene's level is measured, rather than which gene acts first. level_sensitivity: q = BH over every (gene,
   drug-dose) test of the run, q_group = within the drug-dose; written when q_group < 0.10, alerted when q >= 0.10.
   Computed in blocks of 64 drug-doses (float32), keeping only the candidates p < 0.10 (BH with the family size is
   exact below 0.10). Controls: the same tests with every gene's level permuted over its lines (Freedman-Lane, one
   permutation), counted at the real BH cut.
4. drug_target (no mutation; grade B). A target X annotated for >= 2 distinct compounds (one molecule counts once:
   salt forms merged with tlib.salt_base, then letter case and trailing salt words - 'Ixazomib' / 'Ixazomib
   citrate', 'crizotinib' / 'Crizotinib (hydrochloride)'; its names ' / '-joined) of one mechanism class
   (moa-broad: inhibitor/antagonist, activator/agonist, unclear): Y is
   significant (pooled q < 0.1 and >= 1.2x, at any dose) in the same direction for k >= 2 of X's N compounds;
   one-sided hypergeometric test against Y's rate over all compounds (Fisher's exact test); BH over all such tests.
   Sign relative to X's activity: inhibitors raising Y -> -1 (X activity lowers Y), activators raising Y -> +1.
   Sign of the response kinds (genotype_response, null_response, level): how STRONGLY Y responds in its own pooled
   direction (r = per-line z x the sign of the pooled z), so +1 reads 'strengthens Y's drug response' - for a Y that
   falls under the drugs, a deeper fall - and -1 'weakens'.
   Columns compounds (the class's compounds, '; '-joined), compounds_supporting (those moving Y that way) and
   drug_effect ('raises' / 'lowers': what the compounds do to Y) record it for the look-ups (direction_view.py).
5. The sensitivity kinds above are the gene -> phenotype edges: the target is 'cells under DRUG DOSE' (target_dd).

Organs: from lines.csv, else the cell-line metadata. A group is compared within organs when the labels have >= 100
arrangements there; then the organ composition is the same in every permutation and no tissue alert is raised, but
only the lines in organs holding both sides carry the comparison (alerted when not all; grade A needs >= 5 on each
side). Compared across organs, the group is tissue-confounded when the sides' organs differ more than chance
(Monte Carlo p < 0.05 of the chi-square statistic of the organs x sides table over 2,000 label permutations); the
alert names the most over-represented organ with its counts. Unknown organs: no strata, no tissue alert, an alert.

Grades. A: a recorded genotype with >= 5 lines on each side (measured lines, for a response; within organs: those
sharing an organ with the other side), q < 0.05 (and q_group < 0.10), compared within organs, no co-occurrence alert
(another gene's altered lines overlapping the altered side, or sitting on the other side: anti-occurrence), and for a
response not resting on the correction nor mostly uncorrected. B: any other genotype edge with q < 0.10 (alerts, or
3-4 lines) that is not tissue-confounded; expression-null with >= 5 lines lacking X and >= 5 expressing it, not
tissue-confounded; drug_target. C: level and level_sensitivity; a genotype edge significant only within its group, or
tissue-confounded; expression-null with 3-4 lines, tissue-confounded, co-absent, or resting on the correction. Alerts
(each in plain words): few lines, tissue-confounded, compared across organs, compared within organs on part of the
lines, co-occurrence (Jaccard >= 0.5 with another gene's altered lines), anti-occurrence (another gene's altered lines
on the other side, phi <= -0.5: a confounder with the opposite sign), Y much lower at baseline in the altered lines (a
lost response may be lost expression), X's own expression lost in altered lines (deletion), lines where Y is not
measured, the global-sensitivity correction (resting on it, the reference differing between the sides, drug-doses
without any or only a line-wide correction), the difference going both ways, its own permutation p used, artifact
flags of the supporting drug-doses, mechanism not recorded, significant only within its group, for expression-null
the genes absent from overlapping line sets (Jaccard >= 0.5: co-deleted neighbours), and per kind the caveats in its
section.

Alerts in tiers (VERSION 3). Every reason is kept and written in full, in one of four tiers (reason_tier, applied to
the finished table; alerts_all keeps all of them in the original order): alerts (⚠: a doubt about this arrow),
notes (a graded reason below its threshold), caveats (KIND_CAVEATS: the same on every arrow of a kind) and support
(evidence for it: 'consistent across N compounds', a recorded loss of a gene missing from the same lines). Graded:
'Y measured in a of the A and i of the I lines' is an alert when a or i < FULL_SIDE or a < NOTE_MEASURED_FRAC = 0.75
x A or i < 0.75 x I; the artifact flags of the supporting drug-doses when they carry >= NOTE_ART_SHARE = 0.5 of the
evidence (art_share: sum |contrast| over the target's K drug-doses; drug_target: of the supporting compounds) or the
strongest supporting drug-dose is flagged - the reason lists every flagged drug-dose among the K; 'compared within
organs: a of A ... i of I' when a < NOTE_WITHIN_ORGAN_FRAC = 0.5 x A or i < 0.5 x I; 'other genes are absent from
most of these lines too' when <= NOTE_COABSENT_SETS = 10 line sets overlap (a candidate co-deletion; more is a tissue
programme); 'X itself is not expressed in k of the n altered lines' when k > NOTE_NOT_EXPRESSED_FRAC = 0.25 x n.
Otherwise each is a note. Every other reason is an alert. The tiers change no edge, grade, sign or number (the grade
rules read the groups and tests, not the texts). drugdoses_all lists every drug-dose behind an edge with its flags.

Controls (controls.json). Positive: TP53 groups -> p53 target genes (recovered with the right sign, their ranks),
TP53 -> cells under DNA-damaging drugs, KEAP1 -> NRF2 target genes (baseline) when KEAP1 is recorded in enough lines.
Negative: N_PSEUDO = 60 random pseudo-genotype groups with sizes spread over the real groups' size distribution
(quantiles; lines drawn at random, rejected while they resemble a recorded group, |phi| >= 0.3, or an expression-null
line set with >= 5 lines on each side, |phi| >= 0.5: a random set overlapping a real effect would find it), tested
exactly as the real groups; a pseudo test counts as an edge at the real family's BH cut (and q_group < 0.10).
Their edges per group x the number of real groups = the expected false edges of the table (an upper bound when a
random set still overlaps an unrecorded effect), reported per kind next to the real counts (info.json, README; the
README alerts when pseudo-groups give as many edges as the real ones), each with its 95% upper bound (Poisson: 0
edges in 60 pseudo-groups still allows ~3 per 60 groups). Level kinds: the permuted-level controls (one permutation;
the same upper bound). The estimates can be low when real groups overlap other alterations or tissue programmes,
which random groups do not. Pseudo-group edges are not written.

Outputs in OUT/direction/: edges.parquet, groups.parquet, controls.json, info.json, README.md (every column).
Memory: the tensor is read in gene chunks sized by mem_gb (plain file reads, not a memory map, so the pages read do
not stay resident); what is kept is genes x K x lines (a few float32 arrays, ~35 MB each at full scale) plus the
pooled matrices (~75 MB each); level_sensitivity runs in drug-dose blocks. info.json peak_rss_mb is the stage's own
peak (peak_rss_how says how it was measured: under `tahoe run` the stages share one process). Measured on a generated
output of the
full size (16,643 genes, 751 drug-doses with line-to-line differences in cell numbers): peak 1.75 GB with the
default mem_gb = 1, 6.4 minutes on 4 CPUs (tests/test_direction.py --scale-genes 16643). The response tests run in a
few threads.
"""

import argparse
import glob
import json
import math
import os
import re
import sys
import time
import warnings

import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy import stats

from . import atlas_core as A
from . import tlib as T
from .common import folder, log, replace_file, stable_seed, stamp_stage, write_json, write_parquet
from .tensor import AMB_FRAC

VERSION = 3

K_DD = 10                      # drug-doses per gene (its strongest by pooled |z|)
Z_CLIP = 10.0                  # per-line z clipped at +-this before any mean
Q_SIG = 0.10                   # the atlas significance (pooled) and the edge cut
LFC_MIN = math.log2(1.2)
Z_SIG = 3.0
Q_A = 0.05                     # grade A needs q < this
MIN_SIDE = 3                   # lines on each side for a test
FULL_SIDE = 5                  # lines on each side for grade A (genotype) / B (expression-null)
PERMS = 200                    # label permutations per genotype group
RESP_BLOCK = 256               # genes per block of the response test (x K rows)
THREADS = 4                    # threads for the response test
PERMS_NULL = 200               # per expression-null line set
MIN_ARRANGEMENTS = 100         # within-organ permutation needs this many distinct arrangements
NULL_MAX = 2_000_000           # pooled-null values kept
TAIL_N = 250                   # pooled null: its largest TAIL_N values fit a generalized-Pareto tail ...
TAIL_MIN_COUNT = 10            # ... used where fewer than this many null values reach T (no p floor)
OWN_ALPHA = 0.01               # a target's own permutations contradict the pooled p at this level -> own p
DISTINCT_MIN = 0.5             # ... or its permutation values take fewer than this share of distinct values
FEW_ARRANGEMENTS = 1000        # ... or the labels have fewer arrangements than this over its lines
REF_MAX = 500                  # global-sensitivity reference: a drug-dose's strongest responsive genes
REF_MIN_GENES = 50             # ... at least this many left per line (after Y and its partners are left out)
REF_MEAN_MIN = 0.5             # ... whose mean response over the lines is at least this (z units)
REF_LINE_GENES = 10            # line-wide responsiveness: from drug-doses with >= this many responsive genes ...
REF_LINE_DD = 20               # ... at least this many of them (median over them) ...
REF_LINE_COMPOUNDS = 20        # ... from at least this many compounds ...
REF_LINE_R = 0.5               # ... and reproduced by two halves of the compounds (or SD < 0.1 across lines)
RAW_SHARE_MIN = 0.25           # response: raw evidence / corrected evidence below this = rests on the correction
UNCHECKED_MAX = 0.5            # response: grade A needs < this share of the evidence without any correction
JACCARD_CO = 0.5               # co-occurrence alert
TISSUE_P = 0.05                # tissue-confounded: organ enrichment of the sides (Monte Carlo p) below this
TISSUE_PERMS = 2000
BASE_LOW = 1.0                 # response alert: Y >= 2x lower at baseline in the altered lines (log2)
LEVEL_MIN_LINES = 8
LEVEL_PCS = 3
LEVEL_NULL_PAIRS = 2000        # Freedman-Lane permutations (calibration of the t distribution's p)
LEVEL_NULL_PERMS = 100
LEVEL_SENS_NULL_GENES = 400
LEVEL_SENS_NULL_PERMS = 50
LEVEL_SENS_NULL_DD = 50        # drug-doses per null gene
LEVEL_DIR_BOOT = 1000          # direction of a level edge: bootstrap over lines (the two directions' error correlation)
LEVEL_DIR_DRAWS = 2000         # ... draws per common strength of the selection-aware null
LEVEL_DIR_GRID = np.linspace(0.0, 0.95, 20)    # ... the common strengths (|rho|) the null is evaluated at
LEVEL_DIR_P = 0.05
LEVEL_BLOCK = 64               # level_sensitivity: drug-doses per block
VAR_FLOOR = 0.1                # Welch t: a side's variance is at least this x the row's variance over the group
VAR_P = 0.05                   # variable drug-doses (sensitivity of null / level): chi-square p of sum Az^2
N_PSEUDO = 60                  # negative-control pseudo-groups
PSEUDO_PHI = 0.3               # ... resembling no recorded group (|phi| below this)
PSEUDO_PHI_NULL = 0.5          # ... nor an expression-null line set with >= FULL_SIDE lines each side
TOP_DD = 3                     # supporting drug-doses listed per edge
MIXED = 0.25                   # a response target rises and falls: each direction carries >= this share
GC_MIN = 200                   # inflation correction needs this many tested targets
ALERT = "⚠"

KINDS = ("genotype_response", "genotype_baseline", "genotype_sensitivity", "null_response", "null_baseline",
         "null_sensitivity", "drug_target", "level", "level_sensitivity")
TISSUE_ALERT = "from natural expression differences between lines; tissue and other differences can mimic it"
DRUG_ALERT = "drugs can act on other proteins too"
PRECISION_ALERT = ("a stronger correlation one way can reflect how precisely, or how closely to a shared cause, each "
                   "gene's level is measured, rather than which gene acts first")
# Every reason an edge carries is kept, in one of four tiers (module docstring, 'Alerts in tiers'; README):
#   alerts  (⚠)  a doubt about this arrow, or a graded reason at or past its threshold;
#   notes        a graded reason below its threshold (shown muted, in full);
#   caveats      the same text on every arrow of a kind (stated once per list);
#   support      evidence for the arrow.
TIERS = ("alerts", "notes", "caveats", "support")
KIND_CAVEATS = {"drug_target": (DRUG_ALERT,), "level": (TISSUE_ALERT, PRECISION_ALERT),
                "level_sensitivity": (TISSUE_ALERT,)}
NOTE_MEASURED_FRAC = 0.75      # 'Y measured in a of the A and i of the I lines': an alert when a or i < FULL_SIDE, or
                               # a < this x A, or i < this x I; else a note
NOTE_ART_SHARE = 0.5           # supporting drug-doses with artifact flags: an alert when they carry >= this share of
                               # the evidence (art_share; drug_target: of the supporting compounds) or the strongest
                               # supporting drug-dose is one of them; else a note
NOTE_WITHIN_ORGAN_FRAC = 0.5   # 'compared within organs: a of the A ... and i of the I others': an alert when a < this
                               # x A or i < this x I; else a note (a within-organ comparison costs lines, not validity)
NOTE_COABSENT_SETS = 10        # 'other genes are absent from most of these lines too': an alert when <= this many line
                               # sets overlap (a candidate co-deletion); else a note (a tissue programme)
NOTE_NOT_EXPRESSED_FRAC = 0.25  # 'X itself is not expressed in k of the n altered lines': an alert when k > this x n
P53_TARGETS = ("CDKN1A MDM2 FDXR ZMAT3 SESN1 SESN2 BBC3 BAX TP53I3 RRM2B AEN DDB2 XPC TNFRSF10B PHLDA3 SPATA18 "
               "TRIAP1 RPS27L ACER2 TP53INP1 PLK3 POLH EDA2R GADD45A TIGAR BTG2 CCNG1 GDF15 FAS APAF1 PPM1D DRAM1 "
               "SUSD6 TNFRSF10D ASCC3 ZNF79 KITLG SERPINB5 PMAIP1").split()
NRF2_TARGETS = ("NQO1 HMOX1 AKR1C1 AKR1C2 AKR1C3 TXNRD1 GCLM GCLC SRXN1 OSGIN1 G6PD PGD ME1 AKR1B10 ABCC2 ABCC3 "
                "SLC7A11 CBR1 TALDO1 CYP4F11").split()
DNA_DAMAGE_TARGETS = {"TOP1", "TOP2A", "TOP2B", "TYMS", "RRM1", "RRM2", "POLA1", "DHFR"}
META_COLS = ["cell_name", "Cell_ID_DepMap", "Cell_ID_Cellosaur", "Organ", "Driver_Gene_Symbol", "Driver_VarZyg",
             "Driver_VarType", "Driver_ProtEffect_or_CdnaEffect", "Driver_Mech_InferDM", "Driver_GeneType_DM"]
MECH_WORDS = {"LoF": "loss of function", "GoF": "gain of function", "any": "altered (any record)",
              "null": "not expressed", "pseudo": "pseudo-group"}


# ----------------------------------------------------------------------------- small helpers
def _bh(p, m=None):
    """Benjamini-Hochberg q-values (NaN stays NaN). m: the family's size when p holds only its smallest values
    (every left-out test has p >= Q_SIG): the q-values below Q_SIG are then exact."""
    p = np.asarray(p, dtype=np.float64)
    q = np.full(p.shape, np.nan)
    ok = np.isfinite(p)
    n = int(ok.sum())
    if not n:
        return q
    m = max(n, int(m or 0))
    pv = p[ok]
    o = np.argsort(pv, kind="stable")
    r = pv[o] * m / np.arange(1, n + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    qq = np.empty(n)
    qq[o] = np.minimum(r, 1.0)
    q[ok] = qq
    return q


def _bh_cut(p, m=None):
    """The p at or below which a test of the family reaches BH q < Q_SIG (Q_SIG / m when none does: the cut one more
    test would need)."""
    p = np.asarray(p, dtype=np.float64)
    p = p[np.isfinite(p)]
    m = max(int(p.size), int(m or 0))
    if not m:
        return 0.0
    q = _bh(p, m)
    hit = q < Q_SIG
    return float(p[hit].max()) if hit.any() else Q_SIG / m


class _Null:
    """A pooled permutation null (finite values, absolute when two-sided, sorted) and its p: the empirical
    (1 + #null >= T) / (1 + #null) where at least TAIL_MIN_COUNT null values reach T; beyond, a generalized-Pareto
    tail fitted to the TAIL_N largest null values (shape >= 0: never lighter than exponential), so that p has no
    floor at 1 / #null (a single strong effect among a large family can still pass BH)."""

    def __init__(self, values, two_sided=True, presorted=False):
        a = np.asarray(values, dtype=np.float64).ravel()
        if not presorted:
            a = np.abs(a) if two_sided else a
            a = np.sort(a[np.isfinite(a)])
        self.a, self.two_sided, self.n = a, two_sided, int(a.size)
        self.u = self.xi = self.beta = self.pu = np.nan
        if self.n >= 4 * TAIL_N:
            u = float(a[self.n - TAIL_N - 1])
            exc = a[self.n - TAIL_N:] - u
            exc = exc[exc > 0]
            if exc.size >= 50:
                try:
                    xi, _, beta = stats.genpareto.fit(exc, floc=0)
                except Exception:  # noqa: BLE001  (a failed fit: exponential tail)
                    xi, beta = np.nan, np.nan
                if not (np.isfinite(xi) and np.isfinite(beta) and beta > 0) or xi < 0:
                    xi, beta = 0.0, float(exc.mean())
                self.u, self.xi, self.beta = u, float(min(xi, 1.0)), float(beta)
                self.pu = exc.size / (self.n + 1.0)

    def p(self, T):
        T = np.asarray(T, dtype=np.float64)
        p = np.full(T.shape, np.nan)
        ok = np.isfinite(T)
        if not self.n:
            return p
        t = np.abs(T[ok]) if self.two_sided else T[ok]
        cnt = self.n - np.searchsorted(self.a, t, side="left")
        pe = (1.0 + cnt) / (1.0 + self.n)
        if np.isfinite(self.u):
            tail = (cnt < TAIL_MIN_COUNT) & (t > self.u)
            if tail.any():
                pt = self.pu * stats.genpareto.sf(t[tail] - self.u, self.xi, scale=self.beta)
                pe[tail] = np.minimum(pe[tail], np.maximum(pt, 1e-300))
        p[ok] = pe
        return p

    def describe(self):
        return {"values": self.n, "tail_from": None if not np.isfinite(self.u) else round(self.u, 3),
                "tail_shape": None if not np.isfinite(self.xi) else round(self.xi, 4),
                "tail_scale": None if not np.isfinite(self.beta) else round(self.beta, 4)}


def _own_stats(Tobs, Tp, two_sided, sort_rows=None):
    """Per target, against its own permutation values only: the number reaching T (on |T| when two-sided), the
    number of finite values, and the number of distinct values (a target measured in few lines, or permuted within
    small organs, has few distinct arrangements and a discrete null of its own). sort_rows (bool): count distinct
    values only there (a sort per row), elsewhere taken as all distinct."""
    Tp = np.asarray(Tp, dtype=np.float64)
    t = np.asarray(Tobs, dtype=np.float64)
    a = np.abs(Tp) if two_sided else Tp
    tt = np.abs(t) if two_sided else t
    fin = np.isfinite(a)
    n = fin.sum(axis=1)
    with np.errstate(invalid="ignore"):
        k = (np.where(fin, a, -np.inf) >= tt[:, None] - 1e-9 * np.maximum(1.0, np.abs(tt[:, None]))).sum(axis=1)
    nd = n.copy()
    rows = np.arange(a.shape[0]) if sort_rows is None else np.flatnonzero(sort_rows)
    if rows.size:
        srt = np.sort(np.where(fin[rows], a[rows], np.inf), axis=1)
        d = np.diff(srt, axis=1)
        tol = 1e-7 * np.maximum(1.0, np.abs(srt[:, :-1]))
        nd[rows] = np.minimum(1 + ((d > tol) & np.isfinite(d)).sum(axis=1), n[rows])
    nd = np.where(n > 0, nd, 0)
    return k.astype(np.int32), n.astype(np.int32), nd.astype(np.int32)


def _guard_p(p, own, n_arr):
    """p of the pooled null, made safe per target. The pooled null assumes every target's standardised statistic
    has the same null shape; where a target's own permutations show it does not, its own permutation p is used when
    larger: (1) they contradict the pooled p (more of them reach T than it allows: binomial P(X >= k) < OWN_ALPHA),
    or (2) the target has few distinct arrangements of the labels over its lines (< FEW_ARRANGEMENTS, or its
    permutation values take < DISTINCT_MIN of distinct values): its null is then discrete, and p is also kept at or
    above 1 / its arrangements, which no permutation test can go below. Returns (p, own_used)."""
    p = np.asarray(p, dtype=np.float64).copy()
    k, n, nd = own
    n_arr = np.asarray(n_arr, dtype=np.float64)
    ok = np.isfinite(p) & (n > 0)
    po = np.where(n > 0, (1.0 + k) / (1.0 + n), np.nan)
    with np.errstate(invalid="ignore", divide="ignore"):
        contra = np.zeros(p.shape, dtype=bool)
        contra[ok] = stats.binom.sf(k[ok] - 1, n[ok], np.clip(p[ok], 0.0, 1.0)) < OWN_ALPHA
        few = ok & ((nd < DISTINCT_MIN * n) | ((n_arr > 0) & (n_arr < FEW_ARRANGEMENTS)))
        use = (contra | few) & ok & (po > p)
        p[use] = po[use]
        floor = np.where(few & (n_arr > 0), 1.0 / np.maximum(n_arr, 1.0), 0.0)
    p = np.where(ok, np.maximum(p, floor), p)
    return p, use


def _subsample(x, n, seed):
    x = np.asarray(x).ravel()
    x = x[np.isfinite(x)]
    if x.size <= n:
        return x.astype(np.float32)
    rng = np.random.default_rng(seed)
    return x[rng.choice(x.size, size=n, replace=False)].astype(np.float32)


def _parallel(fn, items):
    """fn over items in a few threads (numpy releases the GIL), BLAS kept to one thread inside them when
    threadpoolctl is installed (else the threads and BLAS's own would compete)."""
    items = list(items)
    nt = max(1, min(THREADS, os.cpu_count() or 1, len(items)))
    if nt == 1:
        for x in items:
            fn(x)
        return
    from concurrent.futures import ThreadPoolExecutor
    try:
        from threadpoolctl import threadpool_limits
        lim = threadpool_limits(1)
    except Exception:  # noqa: BLE001  (optional)
        lim = None
    try:
        with ThreadPoolExecutor(nt) as ex:
            for _ in ex.map(fn, items):
                pass
    finally:
        if lim is not None:
            lim.restore_original_limits()


def _dd_label(drug, dose):
    s = str(dose).strip()
    return f"{drug} {s} µM" if s and s != "nan" else str(drug)


def _q2(x):
    """A q in two significant digits, never rounded up to the 0.10 cut: 0.09999 prints '0.0999', not '0.1'."""
    x = float(x)
    if not np.isfinite(x):
        return "NA"
    s = f"{x:.2g}"
    if x < Q_SIG and float(s) >= Q_SIG:
        s = f"{math.floor(x * 1e4) / 1e4:.4f}"
    return s


def _fmt_fold(v):
    return "NA" if not np.isfinite(v) else (f"{v:.2f}x" if v < 10 else f"{v:.0f}x")


def _peak_rss_mb():
    """Peak resident memory of this process in MB: Linux VmHWM (reset at exec, unlike getrusage's maxrss, which keeps
    the forking parent's), else psutil's peak working set (Windows), else getrusage."""
    try:
        with open("/proc/self/status", encoding="ascii") as fh:
            for line in fh:
                if line.startswith("VmHWM:"):
                    return round(int(line.split()[1]) / 1024.0, 1)
    except (OSError, ValueError, IndexError):
        pass
    try:
        import psutil
        mi = psutil.Process().memory_info()
        if hasattr(mi, "peak_wset"):
            return round(mi.peak_wset / 1048576.0, 1)
    except Exception:  # noqa: BLE001  (optional)
        pass
    try:
        import resource
        r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return round(r / (1048576.0 if sys.platform == "darwin" else 1024.0), 1)
    except Exception:  # noqa: BLE001
        return None


class _PeakMeter:
    """The direction stage's own peak memory, not the process's: under `tahoe run` every stage runs in one process,
    so the process's high-water mark includes the earlier stages (embed's, say). Linux: VmHWM reset at the start of
    the stage (/proc/self/clear_refs '5'), so it is exact. Elsewhere: if the process's peak rose during the stage,
    that peak is the stage's; else the largest resident size sampled every 0.2 s during the stage (psutil). how says
    which."""

    def __init__(self):
        self.reset = False
        try:
            with open("/proc/self/clear_refs", "w", encoding="ascii") as fh:
                fh.write("5")
            self.reset = True
        except OSError:
            pass
        self.start = _peak_rss_mb()
        self.samples, self._stop, self._thread = [], None, None
        if not self.reset:
            try:
                import threading
                import psutil
                proc = psutil.Process()
                self._stop = threading.Event()

                def sample():
                    while not self._stop.is_set():
                        try:
                            self.samples.append(proc.memory_info().rss / 1048576.0)
                        except Exception:  # noqa: BLE001  (a failed sample is skipped)
                            pass
                        self._stop.wait(0.2)
                self._thread = threading.Thread(target=sample, daemon=True)
                self._thread.start()
            except Exception:  # noqa: BLE001  (no psutil: the process peak, said so)
                self._stop = None

    def stop(self):
        """(peak MB, how it was measured)."""
        if self._stop is not None:
            self._stop.set()
            self._thread.join(timeout=2)
        end = _peak_rss_mb()
        if self.reset:
            return end, "this stage's own peak (the process's high-water mark reset at its start)"
        if end is not None and self.start is not None and end > self.start + 1.0:
            return end, "this stage's own peak (the process's peak rose during it)"
        if self.samples:
            return round(max(self.samples), 1), "this stage's largest resident size, sampled every 0.2 s"
        return end, "the process's peak (it may include earlier stages of the same run)"


def _join(alerts):
    """Alerts as one text, as the relations stage writes them: '' or '⚠ ' + every reason, '; '-joined (a '; ' inside
    one reason, a list of flags, becomes ', ')."""
    t = "; ".join(str(a).replace("; ", ", ") for a in alerts if a)
    return f"{ALERT} {t}" if t else ""


def _n_alerts(s):
    return 0 if not s else str(s).count("; ") + 1


def _plain(reasons):
    """Reasons as one text without the warning sign: '' or every reason, '; '-joined (as _join, without '⚠ ')."""
    return "; ".join(str(a).replace("; ", ", ") for a in reasons if a)


def split_reasons(text):
    """The reasons of an alerts text ('' or '⚠ ' + '; '-joined reasons, or the same without the sign)."""
    t = str(text or "").strip()
    if t.startswith(ALERT):
        t = t[len(ALERT):].strip()
    return [x.strip() for x in t.split("; ") if x.strip()]


# the texts of the reasons as the edges hold them (a '; ' inside one reason is written ', ': _join)
_CAVEAT_TEXTS = {x.replace("; ", ", ") for v in KIND_CAVEATS.values() for x in v}
_RX_SUPPORT = (re.compile(r"^consistent across \d+ compounds \("),
               re.compile(r"^the lines lacking \S+ carry a recorded loss of \S+ \(overlap [0-9.]+\): genotype evidence "
                          r"too$"))
_RX_MEASURED = re.compile(r"^\S+ measured in (\d+) of the (\d+) and (\d+) of the (\d+) lines$")
_RX_WITHIN = re.compile(r"^compared within organs: (\d+) of the (\d+) .+? and (\d+) of the (\d+) others share an organ")
_RX_COABSENT = re.compile(r"^other genes are absent from most of these lines too: (.*): any of them could be the "
                          r"cause$")
_RX_MORE_SETS = re.compile(r" \(and (\d+) more line sets\)$")
_RX_NOT_EXPR = re.compile(r"^\S+ itself is not expressed in (\d+) of the (\d+) altered lines")
_RX_ART = re.compile(r"^supporting drug-doses with artifact flags \((?:\d+% of the evidence|share of the evidence not "
                     r"measurable|(\d+) of the (\d+) supporting compounds)(, the strongest among them)?\): ")


def reason_tier(reason, art_share=np.nan):
    """The tier of one reason (TIERS): 'caveats' (KIND_CAVEATS: the same on every arrow of a kind), 'support'
    (evidence for the arrow), 'notes' (a graded reason below its threshold: the NOTE_* constants) or 'alerts' (every
    other reason, and a graded one at or past its threshold). Graded reasons are read from their own words (their
    counts are whole numbers in the text); the artifact-flag reason of a response edge from art_share (the stored
    float32), of a drug_target edge from its share of the supporting compounds. A reason this code does not know stays
    an alert."""
    r = str(reason)
    if r in _CAVEAT_TEXTS:
        return "caveats"
    if any(rx.search(r) for rx in _RX_SUPPORT):
        return "support"
    m = _RX_MEASURED.search(r)
    if m:
        a, na, i, ni = (int(x) for x in m.groups())
        low = (a < FULL_SIDE or i < FULL_SIDE or a < NOTE_MEASURED_FRAC * na or i < NOTE_MEASURED_FRAC * ni)
        return "alerts" if low else "notes"
    m = _RX_ART.search(r)
    if m:
        if m.group(3):                                        # the strongest supporting drug-dose is flagged
            return "alerts"
        if m.group(1):                                        # drug_target: k of the n supporting compounds
            return "alerts" if int(m.group(1)) >= NOTE_ART_SHARE * int(m.group(2)) else "notes"
        a = float(art_share) if art_share is not None else np.nan
        return "alerts" if not np.isfinite(a) or a >= NOTE_ART_SHARE else "notes"
    m = _RX_WITHIN.search(r)
    if m:
        a, na, i, ni = (int(x) for x in m.groups())
        return "alerts" if (a < NOTE_WITHIN_ORGAN_FRAC * na or i < NOTE_WITHIN_ORGAN_FRAC * ni) else "notes"
    m = _RX_COABSENT.search(r)
    if m:
        names = m.group(1)
        more = _RX_MORE_SETS.search(names)
        total = names.count(" (overlap ") + (int(more.group(1)) if more else 0)
        return "alerts" if total <= NOTE_COABSENT_SETS else "notes"
    m = _RX_NOT_EXPR.search(r)
    if m:
        k, n = int(m.group(1)), int(m.group(2))
        return "alerts" if k > NOTE_NOT_EXPRESSED_FRAC * n else "notes"
    return "alerts"


def tiers(reasons, art_share=np.nan):
    """{tier: its reasons, in their original order} (TIERS) of a list of reasons."""
    out = {t: [] for t in TIERS}
    for r in reasons:
        out[reason_tier(r, art_share)].append(r)
    return out


def tier_columns(texts, art_share=None):
    """The tier columns of a table from its full reason texts (one per row: '' or '⚠ ' + '; '-joined, every reason;
    art_share: per row, NaN or the edge's float32 artifact share): alerts ('' or '⚠ ' + its reasons, as _join),
    notes, caveats, support, alerts_all (every reason in the original order; '; '-joined, no sign) and the counts
    n_alerts, n_notes, n_caveats, n_support (int16). Rows with the same text and share are classified once."""
    texts = [str(t or "") for t in texts]
    arts = np.full(len(texts), np.nan) if art_share is None else np.asarray(art_share, dtype=np.float64)
    cols = {k: [] for k in ("alerts", "notes", "caveats", "support", "alerts_all")}
    cnt = {f"n_{k}": np.zeros(len(texts), dtype=np.int16) for k in TIERS}
    memo = {}
    for i, (t, a) in enumerate(zip(texts, arts)):
        key = (t, float(a) if np.isfinite(a) else None)
        if key not in memo:
            rs = split_reasons(t)
            tr = tiers(rs, a)
            memo[key] = (_join(tr["alerts"]), _plain(tr["notes"]), _plain(tr["caveats"]), _plain(tr["support"]),
                         _plain(rs), tuple(len(tr[k]) for k in TIERS))
        al, no, ca, su, every, ns = memo[key]
        for k, v in zip(("alerts", "notes", "caveats", "support", "alerts_all"), (al, no, ca, su, every)):
            cols[k].append(v)
        for k, v in zip(TIERS, ns):
            cnt[f"n_{k}"][i] = v
    return {**cols, **cnt}


def _write_text(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    replace_file(tmp, path)


def _split_targets(s):
    if s is None or (isinstance(s, float) and not np.isfinite(s)):
        return []
    s = str(s)
    for ch in "[]'\"":
        s = s.replace(ch, "")
    out = []
    for part in s.replace(";", ",").replace("|", ",").split(","):
        t = part.strip().upper()
        if t and t not in ("NAN", "NONE", "NA", "-"):
            out.append(t)
    return out


def _moa_class(s):
    s = str(s or "").lower()
    if "inhibitor" in s or "antagonist" in s or "blocker" in s:
        return "inhibitor"
    if "activator" in s or "agonist" in s or "inducer" in s:
        return "activator"
    return "unclear"


# ----------------------------------------------------------------------------- inputs
def _read_index(fxd):
    """genes.csv, drugdose.csv, lines.csv with the dtypes common.read_effects_index gives them."""
    genes = pd.read_csv(os.path.join(fxd, "genes.csv"), dtype={"symbol": str, "label": str, "kind": str})
    dd = pd.read_csv(os.path.join(fxd, "drugdose.csv"), dtype={"drug": str, "dose": str, "plates": str,
                                                                "wells": str, "flags": str},
                     keep_default_na=False, na_values=[""])
    dd["flags"] = dd["flags"].fillna("").astype(str) if "flags" in dd else ""
    lines = pd.read_csv(os.path.join(fxd, "lines.csv"), dtype={"cell_line_id": str})
    return genes, dd, lines


def _cell_line_meta(out, data):
    """The Tahoe cell-line metadata (Driver_* rows): DATA/metadata/cell_line_metadata*.parquet, or the file
    atlas/file_index.json lists (as tables.py reads it). (DataFrame or None, source text)."""
    files = []
    if data:
        for pat in ("cell_line_metadata*.parquet", os.path.join("metadata", "cell_line_metadata*.parquet"),
                    os.path.join("*", "cell_line_metadata*.parquet")):
            files = sorted(glob.glob(os.path.join(data, pat)))
            if files:
                break
    if not files:
        p = os.path.join(out, "atlas", "file_index.json")
        try:
            with open(p, encoding="utf-8") as fh:
                files = [f for f in (json.load(fh).get("cell_line") or []) if os.path.exists(f)]
        except (OSError, ValueError):
            files = []
    if not files:
        return None, "none"
    try:
        return T.read_tables(files, META_COLS), files[0]
    except Exception as e:  # noqa: BLE001  (metadata is optional: log and go on)
        log(f"  could not read the cell-line metadata ({e}); genotype evidence from lines.csv drivers only")
        return None, "unreadable"


class _NpyRows:
    """Rows (first axis) of a C-ordered .npy read with plain file reads: unlike a memory map, the pages read do not
    stay mapped into the process, so the resident memory stays at one chunk whatever the file's size."""

    def __init__(self, path):
        self.path = path
        with open(path, "rb") as fh:
            ver = np.lib.format.read_magic(fh)
            rd = np.lib.format.read_array_header_1_0 if ver == (1, 0) else np.lib.format.read_array_header_2_0
            self.shape, fortran, self.dtype = rd(fh)
            self.offset = fh.tell()
        if fortran:
            raise SystemExit(f"direction: {path} is stored in Fortran order; rerun the 'tensor' stage")
        self.row = int(np.prod(self.shape[1:], dtype=np.int64))

    def read(self, r0, r1):
        with open(self.path, "rb") as fh:
            fh.seek(self.offset + r0 * self.row * self.dtype.itemsize)
            a = np.fromfile(fh, dtype=self.dtype, count=(r1 - r0) * self.row)
        return a.reshape((r1 - r0,) + tuple(self.shape[1:]))


class Ctx:
    """Everything the tests share (filled by _load and _responses)."""


def _load(out, data):
    c = Ctx()
    c.out = out
    fxd = os.path.join(out, "atlas", "effects")
    tdir = os.path.join(out, "tensor")
    genes, dd, lines = _read_index(fxd)
    gK = int((genes["kind"] == "gene").sum())
    Dn, L = len(dd), len(lines)
    c.gK, c.Dn, c.L = gK, Dn, L
    g = genes.iloc[:gK]
    sym = g["symbol"].fillna("").astype(str).to_numpy(dtype=object)
    lab = g["label"].fillna("").astype(str).to_numpy(dtype=object) if "label" in g else sym
    c.sym = np.where(sym == "", lab, sym)
    c.col_of = {}
    for i, s in enumerate(c.sym):
        c.col_of.setdefault(str(s).upper(), i)
    c.pooled_cpm = g["pooled_cpm"].to_numpy(dtype=np.float64)
    c.dd = dd
    c.drug = dd["drug"].astype(str).to_numpy(dtype=object)
    c.dose = dd["dose"].astype(str).to_numpy(dtype=object)
    c.dd_flags = dd["flags"].fillna("").astype(str).to_numpy(dtype=object)
    c.dd_art = np.array([A.has_artifact(f) for f in c.dd_flags], dtype=bool)
    c.dd_label = np.array([_dd_label(a, b) for a, b in zip(c.drug, c.dose)], dtype=object)
    p = os.path.join(out, "tables", "drugdoses.parquet")
    salt = None
    if os.path.exists(p):
        try:
            t = pd.read_parquet(p, columns=["salt_base"])
            if len(t) == Dn:
                salt = t["salt_base"].astype(str).to_numpy(dtype=object)
        except Exception:  # noqa: BLE001
            salt = None
    c.salt = salt if salt is not None else np.array([T.salt_base(d) for d in c.drug], dtype=object)
    c.lines = lines
    c.line_id = lines["cell_line_id"].astype(str).to_numpy(dtype=object)
    nm = lines["cell_name"].fillna("").astype(str) if "cell_name" in lines else lines["cell_line_id"]
    c.line_name = np.where(nm == "", c.line_id, nm).astype(object)
    org = lines["Organ"].fillna("").astype(str).to_numpy(dtype=object) if "Organ" in lines \
        else np.array([""] * L, dtype=object)
    c.meta, c.meta_src = _cell_line_meta(out, data)
    c.organ_src = "lines.csv"
    miss = np.array([not str(o).strip() for o in org])
    if miss.any() and c.meta is not None and "Organ" in c.meta:          # the metadata's Organ as the fallback
        m = c.meta
        o_id, o_nm = {}, {}
        for a, b, o in zip(m.get("Cell_ID_Cellosaur", pd.Series([""] * len(m))).astype(str),
                           m.get("cell_name", pd.Series([""] * len(m))).astype(str), m["Organ"].astype(str)):
            if o.strip() and o.lower() != "nan":
                o_id.setdefault(a, o.strip())
                o_nm.setdefault(b.strip().upper(), o.strip())
        for i in np.flatnonzero(miss):
            org[i] = o_id.get(str(c.line_id[i]), o_nm.get(str(c.line_name[i]).strip().upper(), ""))
        c.organ_src = "lines.csv, else the cell-line metadata"
    c.organ_known = np.array([bool(str(o).strip()) for o in org])
    c.organ = np.array([o if str(o).strip() else f"unknown:{i}" for i, o in enumerate(org)], dtype=object)
    for f in ("DDL_z.npy", "DDL_lfc.npy"):
        if not os.path.exists(os.path.join(tdir, f)):
            raise SystemExit(f"direction: {os.path.join(tdir, f)} is missing; run the 'tensor' stage first")
    c.DZ = _NpyRows(os.path.join(tdir, "DDL_z.npy"))
    c.DL = _NpyRows(os.path.join(tdir, "DDL_lfc.npy"))
    if tuple(c.DZ.shape) != (gK, Dn, L) or tuple(c.DL.shape) != (gK, Dn, L):
        raise SystemExit(f"direction: tensor shape {c.DZ.shape} does not match the effects ({gK}, {Dn}, {L})")
    lc = np.asarray(np.load(os.path.join(fxd, "line_cpm.npy"), mmap_mode="r")[:, :gK], dtype=np.float64)
    c.line_cpm = lc
    p = os.path.join(tdir, "line_measured.npy")
    if os.path.exists(p):
        c.measured = np.asarray(np.load(p), dtype=bool)
    else:
        em = np.asarray(np.load(os.path.join(fxd, "expr_mask.npy"), mmap_mode="r")[:, :gK], dtype=bool)
        c.measured = em & (lc >= AMB_FRAC * c.pooled_cpm[None, :])
    c.null = ~c.measured & (lc < AMB_FRAC * c.pooled_cpm[None, :])           # lines x genes: reads ambient only

    def pooled(name):
        return np.array(np.load(os.path.join(fxd, f"{name}.npy"), mmap_mode="r")[:, :gK], dtype=np.float32)
    c.Zp = pooled("DD_z")
    lfc = pooled("DD_lfc")
    qu, qd = pooled("DD_qup"), pooled("DD_qdn")
    c.sig_up = (qu < Q_SIG) & (lfc >= LFC_MIN)
    c.sig_dn = (qd < Q_SIG) & (lfc <= -LFC_MIN)
    c.lfc_p = lfc
    del qu, qd
    c.Aab = np.load(os.path.join(fxd, "DD_A.npy")).astype(np.float64) if os.path.exists(
        os.path.join(fxd, "DD_A.npy")) else np.full((Dn, L), np.nan)
    c.Az = np.load(os.path.join(fxd, "DD_Az.npy")).astype(np.float64) if os.path.exists(
        os.path.join(fxd, "DD_Az.npy")) else np.full((Dn, L), np.nan)
    if "in_growth_analysis" in lines:
        ga = lines["in_growth_analysis"].astype(str).str.lower().isin(["true", "1", "1.0"]).to_numpy()
        c.Aab[:, ~ga] = np.nan
        c.Az[:, ~ga] = np.nan
    c.B = np.log2(np.maximum(lc, 0.0) + 1.0).T.astype(np.float64)               # genes x lines baseline level
    # related pairs (relations stage); a gene's partners in either direction
    c.rel = None
    p = os.path.join(out, "relations", "gene_relations.parquet")
    if os.path.exists(p):
        try:
            r = pd.read_parquet(p, columns=["col_a", "col_b", "cos"])
            r = r[(r["col_a"] < gK) & (r["col_b"] < gK) & (r["col_a"] != r["col_b"])]
            c.rel = r
        except Exception as e:  # noqa: BLE001
            log(f"  relations not readable ({e}): expression-null and level evidence skipped")
    if c.rel is not None and len(c.rel):
        a = c.rel["col_a"].to_numpy(np.int64)
        b = c.rel["col_b"].to_numpy(np.int64)
        m = sp.coo_matrix((np.ones(a.size * 2, np.float32), (np.r_[a, b], np.r_[b, a])), shape=(gK, gK)).tocsr()
        m.data[:] = 1.0
        c.partners = m
    else:
        c.partners = sp.csr_matrix((gK, gK), dtype=np.float32)
    return c


def _line_wide(c, srows, sdd):
    """The lines' overall responsiveness (module docstring): the median over the qualifying drug-doses of their
    relative responsiveness per line, used only when it is reliable - from >= REF_LINE_DD drug-doses of >=
    REF_LINE_COMPOUNDS distinct compounds, and either negligible (SD < 0.1: the correction is then ~nil) or
    reproduced by two halves of the compounds (median of each half, correlation across lines >= REF_LINE_R): a
    median of a few drug-doses that all carry line-dependent programmes of their own would follow those programmes,
    not the lines' general responsiveness. Sets c.wline (or None) and returns the check."""
    out = {"drugdoses": len(sdd), "compounds": 0, "sd": None, "split_half_r": None, "used": False}
    if len(sdd) < REF_LINE_DD:
        out["why"] = f"{len(sdd)} drug-doses with a broad response, < {REF_LINE_DD}"
        return out
    Sd = np.vstack(srows)
    comp = c.salt[np.asarray(sdd)]
    uc = np.unique(comp)
    out["compounds"] = int(uc.size)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        w = np.nanmedian(Sd, axis=0)
        if not (np.isfinite(w).sum() >= 2 and np.nanmean(w) > 0):
            out["why"] = "no finite responsiveness"
            return out
        w = w / np.nanmean(w)
        sd = float(np.nanstd(w))
        rng = np.random.default_rng(stable_seed("line-wide", c.L, len(sdd)))
        half = np.isin(comp, uc[rng.permutation(uc.size)[:uc.size // 2]])
        w1, w2 = np.nanmedian(Sd[half], axis=0), np.nanmedian(Sd[~half], axis=0)
        m = np.isfinite(w1) & np.isfinite(w2)
        r = float(np.corrcoef(w1[m], w2[m])[0, 1]) if m.sum() >= 3 and np.std(w1[m]) > 0 and np.std(
            w2[m]) > 0 else np.nan
    out.update({"sd": round(sd, 4), "split_half_r": None if not np.isfinite(r) else round(r, 4)})
    if uc.size < REF_LINE_COMPOUNDS:
        out["why"] = f"{len(sdd)} drug-doses from {uc.size} compounds, < {REF_LINE_COMPOUNDS}"
    elif sd < 0.1 or (np.isfinite(r) and r >= REF_LINE_R):
        out["used"] = True
        out["why"] = (f"{len(sdd)} drug-doses of {uc.size} compounds; SD {sd:.2f} across lines, split-half r "
                      f"{r:.2f}")
    else:
        out["why"] = (f"not reproducible: SD {sd:.2f} across lines but the two halves of the {uc.size} compounds "
                      f"agree only r {r:.2f} < {REF_LINE_R}")
    if out["used"]:
        c.wline = np.where(np.isfinite(w), w, np.nan).astype(np.float32)
        c.n_wline_dd = len(sdd)
    return out


# ----------------------------------------------------------------------------- per-gene responses
def _responses(c, chunk, mem_gb, k):
    """Y's K drug-doses, the per-line responses r (clipped z, signed), the per-line lfc, the global-sensitivity
    reference (module docstring) and the per-gene line summaries R, R_raw, Lbar and the mask M."""
    gK, Dn, L = c.gK, c.Dn, c.L
    k = int(min(k, Dn))
    az = np.abs(np.nan_to_num(c.Zp, nan=0.0)).T                                # genes x drug-doses
    sel = np.argpartition(-az, k - 1, axis=1)[:, :k] if k < Dn else np.tile(np.arange(Dn), (gK, 1))
    o = np.argsort(-np.take_along_axis(az, sel, axis=1), axis=1, kind="stable")
    sel = np.take_along_axis(sel, o, axis=1).astype(np.int64)                  # strongest first
    del az
    zsel = c.Zp.T[np.arange(gK)[:, None], sel]
    sgn = np.where(zsel < 0, -1.0, 1.0).astype(np.float32)
    sig = (c.sig_up | c.sig_dn | (np.abs(np.nan_to_num(c.Zp)) >= Z_SIG))      # drug-doses x genes
    c.sel, c.sgn = sel, sgn
    c.sel_sig = sig.T[np.arange(gK)[:, None], sel]
    # the share of each gene's response from drug-doses where it rises: |pooled z| over its significant K drug-doses
    # (all K when none is), so that weak drug-doses of the other sign (noise) do not make a one-way target look mixed
    azs = np.abs(np.nan_to_num(zsel, nan=0.0))
    azs = np.where(c.sel_sig.any(axis=1, keepdims=True), azs * c.sel_sig, azs)
    with np.errstate(invalid="ignore", divide="ignore"):
        c.rise_all = np.where(azs.sum(axis=1) > 0, (azs * (sgn > 0)).sum(axis=1) / azs.sum(axis=1), np.nan)
    del azs
    # reference members: per drug-dose its responsive genes (strongest REF_MAX), sorted by gene for the stream
    mg, md, ms = [], [], []
    for d in range(Dn):
        gg = np.flatnonzero(sig[d])
        if gg.size > REF_MAX:
            gg = gg[np.argsort(-np.abs(c.Zp[d, gg]), kind="stable")[:REF_MAX]]
        mg.append(gg)
        md.append(np.full(gg.size, d, np.int64))
        ms.append(np.where(c.Zp[d, gg] < 0, -1.0, 1.0))
    mg, md, ms = np.concatenate(mg), np.concatenate(md), np.concatenate(ms).astype(np.float32)
    o = np.lexsort((md, mg))
    mg, md, ms = mg[o], md[o], ms[o]
    refv = np.full((mg.size, L), np.nan, dtype=np.float32)
    Rz = np.full((gK, k, L), np.nan, dtype=np.float32)
    Rl = np.full((gK, k, L), np.nan, dtype=np.float32)
    if not chunk:
        chunk = max(1, min(gK, int(mem_gb * 1e9 / (Dn * L * 4.0 * 3.0))))
    c.chunk = int(chunk)
    meas = c.measured.T                                                        # genes x lines
    log(f"  streaming the per-line tensor: {gK:,} genes in chunks of {chunk} (K = {k} drug-doses per gene; "
        f"{mg.size:,} reference values)")
    t0 = time.time()
    for g0 in range(0, gK, chunk):
        g1 = min(gK, g0 + chunk)
        rows = np.arange(g1 - g0)[:, None]
        Z = c.DZ.read(g0, g1).astype(np.float32, copy=False)                  # c x Dn x L
        Z = np.where(meas[g0:g1, None, :], Z, np.nan)
        np.clip(Z, -Z_CLIP, Z_CLIP, out=Z)
        Rz[g0:g1] = Z[rows, sel[g0:g1]] * sgn[g0:g1, :, None]
        i0, i1 = np.searchsorted(mg, g0), np.searchsorted(mg, g1)
        if i1 > i0:
            refv[i0:i1] = Z[mg[i0:i1] - g0, md[i0:i1]] * ms[i0:i1, None]
        del Z
        X = c.DL.read(g0, g1).astype(np.float32, copy=False)
        Rl[g0:g1] = np.where(meas[g0:g1, None, :], X[rows, sel[g0:g1]], np.nan) * sgn[g0:g1, :, None]
        del X
        if (g0 // chunk) % 20 == 0 or g1 == gK:
            log(f"    genes {g0:,}-{g1:,} of {gK:,} ({(time.time() - t0) / 60:.1f} min)")
    # global-sensitivity reference per (Y, k): mean over the drug-dose's responsive genes minus Y and its partners
    Pm = (c.partners + sp.identity(gK, dtype=np.float32, format="csr")).tocsr()
    Pm.data[:] = 1.0
    ent_d = sel.ravel()
    order = np.argsort(ent_d, kind="stable")
    bounds = np.searchsorted(ent_d[order], np.arange(Dn + 1))
    mord = np.argsort(md, kind="stable")
    mb = np.searchsorted(md[mord], np.arange(Dn + 1))
    REF = np.full((gK * k, L), np.nan, dtype=np.float32)
    for d in range(Dn):
        ents = order[bounds[d]:bounds[d + 1]]
        rows = mord[mb[d]:mb[d + 1]]
        if not ents.size or not rows.size:
            continue
        V = refv[rows]
        F = np.isfinite(V)
        V0 = np.where(F, V, 0.0).astype(np.float32)
        tot, cnt = V0.sum(axis=0), F.sum(axis=0).astype(np.float32)
        sub = Pm[ents // k][:, mg[rows]]
        exs = np.asarray(sub @ V0)
        exc = np.asarray(sub @ F.astype(np.float32))
        n = cnt[None, :] - exc
        with np.errstate(invalid="ignore", divide="ignore"):
            REF[ents] = np.where(n >= REF_MIN_GENES, (tot[None, :] - exs) / np.maximum(n, 1.0), np.nan)
    # line-wide responsiveness (fallback where a drug-dose moves too few other genes): per drug-dose with >=
    # REF_LINE_GENES responsive genes, their mean response per line / its mean over the lines; the median over those
    # drug-doses (robust to one drug class, or one programme, dominating) is the line's overall responsiveness - the
    # per-line z grows with the cells a line contributes, so lines with fewer cells respond less everywhere.
    c.wline, c.n_wline_dd = None, 0
    srows, sdd = [], []
    for d in range(Dn):
        rows = mord[mb[d]:mb[d + 1]]
        if rows.size < REF_LINE_GENES:
            continue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            md_ = np.nanmean(refv[rows], axis=0)
        mbar = np.nanmean(md_) if np.isfinite(md_).mean() > 0.5 else np.nan
        if np.isfinite(mbar) and mbar >= REF_MEAN_MIN:
            srows.append(md_ / mbar)
            sdd.append(d)
    c.wline_check = _line_wide(c, srows, sdd)
    del refv, srows
    # multiplicative model: line l's relative sensitivity to the drug-dose s = ref / (ref's mean over lines); Y's
    # expected response there scales with it: a = r - b (s - 1), b = Y's mean response over the lines (no labels).
    # At every one of Y's K drug-doses: the drug-dose's own reference where it qualifies (a reference in more than
    # half the lines, mean >= REF_MEAN_MIN), else the line-wide responsiveness, else none (adj_kind 2 / 1 / 0).
    fin = np.isfinite(REF)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        rbar = np.nanmean(REF, axis=1)
        b = np.nanmean(Rz.reshape(gK * k, L), axis=1)
    own = (fin.mean(axis=1) > 0.5) & (rbar >= REF_MEAN_MIN) & np.isfinite(b)
    kind = np.where(own, 2, 1 if c.wline is not None else 0).astype(np.int8)
    kind[~np.isfinite(b)] = 0
    with np.errstate(invalid="ignore", divide="ignore"):
        S = np.where(fin, REF / rbar[:, None], np.nan).astype(np.float32)
        del REF
        if c.wline is not None:
            line = (kind == 1)
            S[line] = np.broadcast_to(c.wline[None, :], (int(line.sum()), L))
        S[kind == 0] = np.nan
        ADJ = np.where(np.isfinite(S), b[:, None] * (S - 1.0), 0.0).astype(np.float32)
    c.adj_kind = kind.reshape(gK, k)
    c.S = S.reshape(gK, k, L)                                                 # the s used (NaN: no correction)
    del S
    ADJ = ADJ.reshape(gK, k, L)
    c.M = meas & np.isfinite(Rz).any(axis=1)                                  # genes x lines: usable lines

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        c.Ra = Rz - ADJ                                                        # NaN where no value (not imputed)
        c.Rz = Rz
        c.Rl = Rl
        c.R = np.nanmean(c.Ra, axis=1)                                         # per line over its available ones
        c.R_raw = np.nanmean(Rz, axis=1)
    del ADJ
    nk = {v: int((c.adj_kind == v).sum()) for v in (0, 1, 2)}
    c.adj_counts = {"drug_specific": nk[2], "line_wide": nk[1], "none": nk[0],
                    "line_wide_from_drugdoses": int(c.n_wline_dd), "line_wide_check": c.wline_check}
    wc = c.wline_check
    log(f"  global-sensitivity correction of the {c.adj_kind.size:,} (gene, drug-dose) responses: {nk[2]:,} against "
        f"the drug-dose's other responsive genes, {nk[1]:,} line-wide only, {nk[0]:,} none; line-wide "
        f"responsiveness {'used' if wc['used'] else 'NOT used'} ({wc['why']}); {int(c.M.any(axis=1).sum()):,} genes "
        "with usable lines")


# ----------------------------------------------------------------------------- permutation machinery
def _perm_labels(lab, strata, P, seed):
    """P x n permuted 0/1 labels (within strata when given), none equal to the observed labels (when another
    arrangement exists): with few arrangements a shared permutation would otherwise reproduce the observed one and
    count as an exceedance for every target."""
    rng = np.random.default_rng(seed)
    n = lab.size
    out = np.empty((P, n), dtype=np.float32)
    groups = [np.arange(n)] if strata is None else [np.flatnonzero(strata == s) for s in np.unique(strata)]

    def draw(rows):
        for idx in groups:
            if idx.size == 1:
                out[np.ix_(rows, idx)] = lab[idx]
                continue
            o = np.argsort(rng.random((rows.size, idx.size)), axis=1)
            out[np.ix_(rows, idx)] = lab[idx][o]
    draw(np.arange(P))
    for _ in range(20):
        same = np.flatnonzero((out == lab[None, :]).all(axis=1))
        if not same.size:
            break
        draw(same)
    return out


def _design(L, idx, lab, plab):
    """L x (1 + P) indicators of the altered and the intact lines: column 0 = the observed labels."""
    P1 = plab.shape[0] + 1
    alt = np.zeros((L, P1), dtype=np.float32)
    inn = np.zeros((L, P1), dtype=np.float32)
    alt[idx, 0] = lab
    inn[idx, 0] = 1.0 - lab
    alt[idx, 1:] = plab.T
    inn[idx, 1:] = 1.0 - plab.T
    return alt, inn


def _contrast(V, Mk, alt, inn, block=4096, square=False):
    """Per row of V (targets x lines), for every column of the designs (column 0 = observed): the difference D = mean
    over the intact lines - mean over the altered lines, its two-sample t with the pooled within-side variance
    (floored at VAR_FLOOR x the row's variance over the group's lines, so that sides of near-identical values cannot
    make t explode), and that t as a normal score z = sign(t) sqrt((nu - 1/2) ln(1 + t^2 / nu)), nu = n - 2 (within
    ~0.05 of the exact normal quantile for nu >= 4): rows with different numbers of lines then share one null
    shape, which the pooled null needs. Sums and sums of squares are linear in the labels: the altered side's are
    matrix products with the designs, the intact side's the group's totals minus them. Mk (targets x lines, bool)
    restricts each row to its measured lines (None: its finite values). Returns D of the observed labels, z (or z^2
    when square; targets x (1 + P)) and the observed counts (altered, intact)."""
    nT = V.shape[0]
    D0 = np.full(nT, np.nan, dtype=np.float32)
    Z = np.full((nT, alt.shape[1]), np.nan, dtype=np.float32)
    na0 = np.zeros(nT, dtype=np.int32)
    ni0 = np.zeros(nT, dtype=np.int32)
    grp = (alt[:, 0] + inn[:, 0]) > 0
    a32 = np.ascontiguousarray(alt, dtype=np.float32)
    for b0 in range(0, nT, block):
        b1 = min(nT, b0 + block)
        v = np.asarray(V[b0:b1], dtype=np.float32)
        m = np.isfinite(v) & grp[None, :]
        if Mk is not None:
            m &= np.asarray(Mk[b0:b1], dtype=bool)
        vm = np.where(m, v, np.float32(0.0))
        mf = m.astype(np.float32)
        v2 = vm * vm
        ng, sg, qg = mf.sum(axis=1)[:, None], vm.sum(axis=1)[:, None], v2.sum(axis=1)[:, None]
        na = mf @ a32
        sa = vm @ a32
        qa = v2 @ a32
        del vm, mf, v2
        with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
            ni = ng - na
            si = sg - sa
            vrow = np.maximum(qg - sg * sg / ng, 0.0) / np.maximum(ng - 1.0, 1.0)
            ma = sa / na
            mi = si / ni
            ss = np.maximum(qa - sa * ma, 0.0) + np.maximum((qg - qa) - si * mi, 0.0)
            nu = ng - 2.0
            sp2 = np.maximum(ss / np.maximum(nu, 1.0), np.float32(VAR_FLOOR) * vrow)
            d = mi - ma
            t2 = d * d / (sp2 * (1.0 / na + 1.0 / ni))
            z2 = np.maximum(nu - 0.5, 0.5) * np.log1p(t2 / np.maximum(nu, 1.0))
        bad = (na < 2) | (ni < 2) | ~np.isfinite(z2)
        z2[bad] = np.nan
        Z[b0:b1] = z2 if square else np.sign(d) * np.sqrt(z2)
        D0[b0:b1] = np.where(bad[:, 0], np.nan, d[:, 0])
        na0[b0:b1] = np.rint(na[:, 0]).astype(np.int32)
        ni0[b0:b1] = np.rint(ni[:, 0]).astype(np.int32)
    return D0, Z, na0, ni0


def _standardise(D):
    """T of the observed column and of every permutation column, by each row's permutation mean and SD (rows whose
    permuted statistics spread more - outlier lines, correlated drug-doses - are not over-trusted in the pooled
    null; under within-organ permutation the mean also absorbs the organ composition)."""
    with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        mu = np.nanmean(D[:, 1:], axis=1)
        sd = np.nanstd(D[:, 1:], axis=1)
        sd = np.where(sd > 1e-9, sd, np.nan)
        Tobs = (D[:, 0] - mu) / sd
        Tp = (D[:, 1:] - mu[:, None]) / sd[:, None]
    return Tobs, Tp


def _counts(x):
    """[(value, count)] by count (descending), then value."""
    u, n = np.unique(np.asarray(x, dtype=str), return_counts=True)
    o = np.lexsort((u, -n))
    return [(str(u[i]), int(n[i])) for i in o]


def _n_arrangements(strata, lab):
    n = 1
    for s in np.unique(strata):
        m = strata == s
        n *= math.comb(int(m.sum()), int(lab[m].sum()))
        if n > 10 ** 9:
            break
    return n


# ----------------------------------------------------------------------------- groups
def _group_common(c, gid, kind, gene, mech, alt, inn, desc):
    """A group record: lines, organs, the permutation plan and the group-level alerts."""
    idx = np.flatnonzero(alt | inn)
    lab = alt[idx].astype(np.float32)
    org = c.organ[idx]
    known_any = bool(c.organ_known[idx].any())
    narr_strat = _n_arrangements(org, lab)
    strat = known_any and narr_strat >= MIN_ARRANGEMENTS
    narr = narr_strat if strat else math.comb(int(idx.size), int(lab.sum()))
    oa, oi = c.organ[alt], c.organ[inn]
    mixed = np.intersect1d(oa, oi)                         # organs holding lines of both sides
    n_alt_mixed, n_inn_mixed = int(np.isin(oa, mixed).sum()), int(np.isin(oi, mixed).sum())
    vc = _counts(oa)
    enrich_p, top = (np.nan, ("?", 0, 0)) if strat else _organ_enrichment(c, idx, lab, stable_seed("tissue", gid))
    # tissue-confounded: only for a comparison across organs (a within-organ permutation compares lines of the same
    # organ, the organ composition is the same in every permutation) whose sides' organs differ more than chance
    tissue = bool(not strat and known_any and np.isfinite(enrich_p) and enrich_p < TISSUE_P)
    g = {"gid": gid, "kind": kind, "gene": gene, "col": c.col_of.get(str(gene).upper(), -1), "mech": mech,
         "alt": alt, "inn": inn, "idx": idx, "lab": lab, "strata": org if strat else None, "stratified": strat,
         "n_arr": int(min(narr, 10 ** 9)), "tissue": tissue, "desc": desc, "n_alt": int(alt.sum()),
         "n_inn": int(inn.sum()), "cooccur": [], "alerts": [], "organ_p": enrich_p,
         "n_alt_mixed": n_alt_mixed if strat else int(alt.sum()), "n_inn_mixed": n_inn_mixed if strat else int(
             inn.sum()),
         "sign_factor": {"LoF": 1, "null": 1, "GoF": -1}.get(mech, 0),
         "organs_alt": "; ".join(f"{k} {v}" for k, v in vc),
         "organs_inn": "; ".join(f"{k} {v}" for k, v in _counts(oi))}
    side = f"lines without {gene}" if mech == "null" else f"{gene}-altered lines"
    alerts = []
    if g["n_alt"] < FULL_SIDE or g["n_inn"] < FULL_SIDE:
        alerts.append(f"few lines ({g['n_alt']} vs {g['n_inn']})")
    if not known_any:
        alerts.append("the lines' organs are not known: tissue differences could not be checked")
    elif tissue:
        o, ka, ki = top
        alerts.append(f"tissue-confounded: the organs of the {side} differ from the other lines' ({o}: {ka} of the "
                      f"{g['n_alt']} {side} vs {ki} of the {g['n_inn']} others, organ-enrichment p {enrich_p:.2g}): "
                      "the comparison cannot separate the gene from the tissue")
    if known_any and not strat:
        alerts.append("compared across organs (too few lines of the same organ on both sides for a within-organ "
                      "comparison)")
    if strat and (n_alt_mixed < g["n_alt"] or n_inn_mixed < g["n_inn"]):
        alerts.append(f"compared within organs: {n_alt_mixed} of the {g['n_alt']} {side} and {n_inn_mixed} of the "
                      f"{g['n_inn']} others share an organ with lines of the other side (the comparison rests on "
                      "those)")
    g["alerts"] = alerts
    return g


def _organ_enrichment(c, idx, lab, seed):
    """Do the two sides' organs differ more than chance? Monte Carlo p (TISSUE_PERMS label permutations over the
    group's lines of known organ) of the chi-square statistic of the organs x sides table; and the organ most
    over-represented on the altered side (organ, altered lines there, other lines there)."""
    kn = c.organ_known[idx]
    org = c.organ[idx][kn]
    y = np.asarray(lab, dtype=np.float64)[kn]
    if y.size < 4 or y.sum() < 1 or y.sum() >= y.size:
        return np.nan, ("?", 0, 0)
    u, inv = np.unique(org, return_inverse=True)
    if u.size < 2:
        return 1.0, (str(u[0]), int(y.sum()), int((1 - y).sum()))
    X = np.zeros((y.size, u.size))
    X[np.arange(y.size), inv] = 1.0
    tot = X.sum(axis=0)
    pa = y.mean()
    exp_a, exp_i = tot * pa, tot * (1 - pa)

    def chi(Y):
        a = Y @ X
        i = tot[None, :] - a
        return (((a - exp_a) ** 2) / exp_a + ((i - exp_i) ** 2) / exp_i).sum(axis=1)
    rng = np.random.default_rng(seed)
    Yp = y[np.argsort(rng.random((TISSUE_PERMS, y.size)), axis=1)]
    c0 = chi(y[None, :])[0]
    p = (1.0 + float((chi(Yp) >= c0 - 1e-9).sum())) / (1.0 + TISSUE_PERMS)
    a = y @ X
    j = int(np.argmax((a / max(1.0, y.sum())) - ((tot - a) / max(1.0, (1 - y).sum()))))
    return p, (str(u[j]), int(a[j]), int(tot[j] - a[j]))


def _genotype_groups(c):
    """Groups from the recorded driver alterations (module docstring, 1). Returns (groups, records), records =
    {gene: {line index: set of (mechanism, variant type)}}."""
    L = c.L
    rec = {}
    recorded = np.zeros(L, dtype=bool)
    src = c.meta_src
    if c.meta is not None and "Driver_Gene_Symbol" in c.meta:
        m = c.meta
        by_id = {str(x): i for i, x in enumerate(c.line_id)}
        by_name = {str(x).strip().upper(): i for i, x in enumerate(c.line_name)}
        ids = m["Cell_ID_Cellosaur"].astype(str) if "Cell_ID_Cellosaur" in m else pd.Series([""] * len(m))
        names = m["cell_name"].astype(str) if "cell_name" in m else pd.Series([""] * len(m))
        li = np.array([by_id.get(a, by_name.get(b.strip().upper(), -1)) for a, b in zip(ids, names)])
        recorded[li[li >= 0]] = True
        gs = m["Driver_Gene_Symbol"].astype(str).str.strip().str.upper().to_numpy()
        mech = m["Driver_Mech_InferDM"].astype(str).to_numpy() if "Driver_Mech_InferDM" in m else \
            np.array(["nan"] * len(m))
        vt = m["Driver_VarType"].astype(str).to_numpy() if "Driver_VarType" in m else np.array(["nan"] * len(m))
        for i in range(len(m)):
            if li[i] < 0 or gs[i] in ("", "NAN", "NONE"):
                continue
            mm = mech[i] if mech[i] in ("LoF", "GoF") else "?"
            rec.setdefault(gs[i], {}).setdefault(int(li[i]), set()).add((mm, vt[i]))
    elif "drivers" in c.lines:
        src = "lines.csv drivers (no mechanism)"
        for i, s in enumerate(c.lines["drivers"].fillna("").astype(str)):
            parts = [p.strip() for p in s.split(";") if p.strip()]
            if parts:
                recorded[i] = True
            for p in parts:
                gname = p.split("(")[0].strip().upper()
                vt = p.split("(")[1].rstrip(")") if "(" in p else "nan"
                rec.setdefault(gname, {}).setdefault(i, set()).add(("?", vt))
    groups = []
    for gene in sorted(rec):
        lines_of = rec[gene]
        anyl = np.zeros(L, dtype=bool)
        anyl[list(lines_of)] = True
        lof = np.zeros(L, dtype=bool)
        gof = np.zeros(L, dtype=bool)
        for li_, s in lines_of.items():
            lof[li_] = any(x[0] == "LoF" for x in s)
            gof[li_] = any(x[0] == "GoF" for x in s)
        inn = recorded & ~anyl
        if inn.sum() < MIN_SIDE:
            continue
        cands = []
        if lof.sum() >= MIN_SIDE:
            cands.append(("LoF", lof))
        if gof.sum() >= MIN_SIDE:
            cands.append(("GoF", gof))
        if anyl.sum() >= MIN_SIDE and not any(np.array_equal(anyl, x) for _, x in cands):
            cands.append(("any", anyl))
        for mech, alt in cands:
            inn_g = inn.copy()
            desc = f"{gene} {MECH_WORDS[mech]} ({int(alt.sum())} lines) vs not recorded ({int(inn_g.sum())})"
            g = _group_common(c, f"genotype:{gene}:{mech}", "genotype", gene, mech, alt, inn_g, desc)
            vts = pd.Series([v for li_ in np.flatnonzero(alt) for (_, v) in lines_of[li_]]).value_counts()
            g["variants"] = "; ".join(f"{k} {v}" for k, v in vts.items())
            n_unknown = sum(all(x[0] == "?" for x in lines_of[li_]) for li_ in np.flatnonzero(alt))
            n_mixed = int((lof & gof & alt).sum())
            if mech == "any":
                g["alerts"].append(f"mechanism not recorded for {n_unknown} of the {int(alt.sum())} lines"
                                   + (f" and {n_mixed} carry both loss- and gain-of-function records" if n_mixed
                                      else "") + ": the sign of the gene's activity is not inferred")
            elif n_mixed:
                g["alerts"].append(f"{n_mixed} of the lines also carry a {'gain' if mech == 'LoF' else 'loss'}-of-"
                                   f"function record of {gene}")
            g["deleted"] = np.array([any(x[1] == "Deletion" for x in lines_of.get(i, ())) for i in range(L)])
            groups.append(g)
    # co-occurrence between the altered sets of different genes (Jaccard), and anti-occurrence: another gene's
    # altered lines sit on the OTHER side of the comparison (phi <= -JACCARD_CO over the lines both compare) - as
    # much a confounder as co-occurrence, with the opposite sign; both block grade A
    for g in groups:
        best, anti = [], []
        for h in groups:
            if h["gene"] == g["gene"]:
                continue
            inter = int((g["alt"] & h["alt"]).sum())
            j = inter / max(1, int((g["alt"] | h["alt"]).sum()))
            if j >= JACCARD_CO:
                best.append((j, h["gene"]))
                continue
            both = (g["alt"] | g["inn"]) & (h["alt"] | h["inn"])
            x, y = g["alt"][both].astype(float), h["alt"][both].astype(float)
            if both.sum() >= 6 and x.std() > 0 and y.std() > 0:
                phi = float(np.corrcoef(x, y)[0, 1])
                if phi <= -JACCARD_CO:
                    anti.append((-phi, h["gene"], int((h["alt"] & g["inn"]).sum()), int((h["alt"] & g["alt"]).sum())))
        seen = {}
        for j, h in sorted(best, reverse=True):
            seen.setdefault(h, j)
        g["cooccur"] = [(h, j) for h, j in seen.items()]
        if g["cooccur"]:
            g["alerts"].append("co-occurs with " + ", ".join(f"{h}-altered lines (overlap {j:.2f})"
                                                              for h, j in g["cooccur"][:3]))
        seen_a = {}
        for v, h, ni_, na_ in sorted(anti, reverse=True):
            seen_a.setdefault(h, (v, ni_, na_))
        g["anti"] = [(h, v[0]) for h, v in seen_a.items()]
        if seen_a:
            n_al, n_in = int(g["alt"].sum()), int(g["inn"].sum())
            g["alerts"].append("another gene's alterations sit on the other side of the comparison: " + ", ".join(
                f"{h} alterations are in {ni_} of the {n_in} comparison lines and {na_} of the {n_al} "
                f"{g['gene']}-altered lines (phi -{v:.2f})" for h, (v, ni_, na_) in list(seen_a.items())[:3])
                + (f" (and {len(seen_a) - 3} more genes)" if len(seen_a) > 3 else "")
                + ": that alteration may be the cause, with the opposite sign")
        x = g["col"]
        if x >= 0:
            na = int(g["alt"].sum())
            lost = int((~c.measured[g["alt"], x]).sum())
            kept_i = float(c.measured[g["inn"], x].mean()) if g["inn"].any() else 0.0
            g["x_lost"] = lost
            g["x_base_diff"] = float(c.B[x, g["inn"]].mean() - c.B[x, g["alt"]].mean())
            if lost and kept_i >= 0.5:
                g["alerts"].append(f"{g['gene']} itself is not expressed in {lost} of the {na} altered lines "
                                   "(deletion or silencing)")
        else:
            g["x_lost"], g["x_base_diff"] = -1, np.nan
    return groups, rec, src, recorded


def _null_groups(c, geno_groups, records):
    """Expression-null groups: per gene, the lines that read only ambient RNA vs the lines that express it. Genes
    with the same line set share one group record (one test)."""
    nn = c.null.sum(axis=0)
    ne = c.measured.sum(axis=0)
    cand = np.flatnonzero((nn >= MIN_SIDE) & (ne >= MIN_SIDE))
    sets = {}
    for x in cand:
        key = c.null[:, x].tobytes() + c.measured[:, x].tobytes()
        sets.setdefault(key, []).append(int(x))
    out = []
    for genes in sets.values():
        x0 = genes[0]
        alt = c.null[:, x0].copy()
        inn = c.measured[:, x0].copy()
        name = c.sym[x0] if len(genes) == 1 else f"{c.sym[x0]} (+{len(genes) - 1})"
        desc = f"{name} not expressed ({int(alt.sum())} lines) vs expressed ({int(inn.sum())})"
        g = _group_common(c, f"null:{c.sym[x0]}", "null", str(c.sym[x0]), "null", alt, inn, desc)
        g["genes"] = genes
        g["level_ratio"] = float(np.median(c.line_cpm[alt][:, genes].mean(axis=1) /
                                           np.maximum(c.pooled_cpm[genes].mean(), 1e-9)))
        co = []
        for h in geno_groups:
            inter = int((alt & h["alt"]).sum())
            if inter and inter / int((alt | h["alt"]).sum()) >= JACCARD_CO:
                co.append((inter / int((alt | h["alt"]).sum()), h["gene"]))
        seen = {}
        for j, h in sorted(co, reverse=True):
            seen.setdefault(h, j)
        g["cooccur"] = list(seen.items())
        out.append(g)
    # genes absent from overlapping (not identical) line sets - co-deleted neighbours, e.g. MTAP and CDKN2A: the
    # other sets whose lines overlap this set's (Jaccard >= JACCARD_CO), strongest first, for the alerts
    if len(out) > 1:
        A = np.array([g["alt"] for g in out], dtype=np.float32)
        na_ = A.sum(axis=1)
        for b0 in range(0, len(out), 2000):
            b1 = min(len(out), b0 + 2000)
            inter = A[b0:b1] @ A.T
            jac = inter / np.maximum(na_[b0:b1, None] + na_[None, :] - inter, 1.0)
            for i in range(b0, b1):
                jac[i - b0, i] = 0.0
                hit = np.flatnonzero(jac[i - b0] >= JACCARD_CO)
                hit = hit[np.lexsort((hit, -jac[i - b0, hit]))]
                out[i]["null_co"] = [(_set_name(c, out[h]["genes"]), float(jac[i - b0, h])) for h in hit[:3]]
                out[i]["null_co_n"] = int(hit.size)
    return out


def _set_name(c, genes):
    """A line set's genes in a few words: 'MTAP', or 'MTAP (+2 absent from the same lines)'."""
    return str(c.sym[genes[0]]) + (f" (+{len(genes) - 1} absent from the same lines)" if len(genes) > 1 else "")


def _null_gene_alerts(c, g, x, records):
    """Edge alerts specific to gene x of a null group (its deletion records, genes absent from the same lines)."""
    al = list(g["alerts"])
    others = [c.sym[y] for y in g["genes"] if y != x]
    if others:
        al.append(f"{len(others)} other gene(s) are absent from exactly these lines ({', '.join(others[:4])}"
                  f"{', ...' if len(others) > 4 else ''}): any of them could be the cause")
    rx = records.get(str(c.sym[x]).upper(), {})
    dele = np.array([any(v[1] == "Deletion" or v[0] == "LoF" for v in rx.get(i, ())) for i in range(c.L)])
    if dele.any():
        j = float((dele & g["alt"]).sum() / max(1, (dele | g["alt"]).sum()))
        if j >= JACCARD_CO:
            al.append(f"the lines lacking {c.sym[x]} carry a recorded loss of {c.sym[x]} (overlap {j:.2f}): "
                      "genotype evidence too")
    co = [(h, j) for h, j in g["cooccur"] if h != str(c.sym[x]).upper()]     # its own records: 'deletion recorded'
    if co:
        al.append("co-occurs with " + ", ".join(f"{h}-altered lines (overlap {j:.2f})" for h, j in co[:3]))
    nco, nn = g.get("null_co") or [], int(g.get("null_co_n", 0))
    if nco:
        al.append("other genes are absent from most of these lines too: " + ", ".join(
            f"{h} (overlap {j:.2f})" for h, j in nco) + (f" (and {nn - len(nco)} more line sets)" if nn > len(nco)
                                                        else "") + ": any of them could be the cause")
    if g.get("level_ratio", 0) > 0.15:
        al.append(f"the lines counted as lacking it still read {g['level_ratio']:.2f}x its pooled level "
                  "(maybe low rather than absent)")
    return al


def _phi_max(X, refs):
    """For each candidate row of X (0/1 over all lines), the largest |phi| with any reference (alt, inn: lines of
    its two sides; other lines left out), over the lines both compare."""
    if not refs:
        return np.zeros(X.shape[0])
    Y = np.array([r[0] for r in refs], dtype=np.float64)
    Mk = np.array([r[0] | r[1] for r in refs], dtype=np.float64)
    n = Mk.sum(axis=1)[None, :]
    sx = X @ Mk.T
    sy = Y.sum(axis=1)[None, :]
    sxy = X @ Y.T
    with np.errstate(invalid="ignore", divide="ignore"):
        cov = sxy / n - (sx / n) * (sy / n)
        vx = sx / n - (sx / n) ** 2
        vy = sy / n - (sy / n) ** 2
        phi = np.abs(cov / np.sqrt(vx * vy))
    phi = np.where(np.isfinite(phi) & (n >= 4), phi, 0.0)
    return phi.max(axis=1)


def _pseudo_groups(c, real, n_pseudo, null_sets=()):
    """Random line sets that resemble no real structure - |phi| < PSEUDO_PHI to every recorded group and <
    PSEUDO_PHI_NULL to every expression-null line set with >= FULL_SIDE lines on each side (a random set that
    overlaps a real effect would find it, which is not a false positive of the test) -, with sizes spread evenly
    over the real groups' size distribution (quantiles of the real groups ordered by size: small and large alike).
    The best of 200 draws is kept when none qualifies (its max_phi is reported)."""
    L = c.L
    sizes = sorted([(g["n_alt"], g["n_inn"]) for g in real]) or [(min(5, L // 3), min(10, L - L // 3))]
    pick = np.rint(np.linspace(0, len(sizes) - 1, max(1, n_pseudo))).astype(int) if n_pseudo > 1 else [0]
    refs_g = [(g["alt"], g["inn"]) for g in real]
    refs_n = [(g["alt"], g["inn"]) for g in null_sets if g["n_alt"] >= FULL_SIDE and g["n_inn"] >= FULL_SIDE]
    out = []
    rng = np.random.default_rng(stable_seed("pseudo", L))
    for i in range(n_pseudo):
        na, ni = sizes[int(pick[i])]
        if na + ni > L:
            continue
        perm = np.argsort(rng.random((200, L)), axis=1)
        alt = np.zeros((200, L), dtype=bool)
        inn = np.zeros((200, L), dtype=bool)
        np.put_along_axis(alt, perm[:, :na], True, axis=1)
        np.put_along_axis(inn, perm[:, na:na + ni], True, axis=1)
        X = alt.astype(np.float64)
        pg, pn = _phi_max(X, refs_g), _phi_max(X, refs_n)
        score = np.maximum(pg / PSEUDO_PHI, pn / PSEUDO_PHI_NULL)
        ok = np.flatnonzero(score < 1.0)
        j = int(ok[0]) if ok.size else int(np.argmin(score))
        g = _group_common(c, f"pseudo:{i + 1}", "pseudo", f"PSEUDO{i + 1}", "pseudo", alt[j], inn[j],
                          f"random pseudo-group {i + 1} ({na} lines) vs ({ni})")
        g["max_phi"] = round(float(pg[j]), 3)
        g["max_phi_null"] = round(float(pn[j]), 3)
        out.append(g)
    return out


# ----------------------------------------------------------------------------- tests of one group
def _test_group(c, g, kinds, P, targets=None, dd_mask=None):
    """Permutation tests of one group. kinds: subset of ('response', 'baseline', 'sensitivity'). targets: gene cols
    to test (None: all). Returns {kind: dict of arrays over the tested targets} with T and the permutation T."""
    plab = _perm_labels(g["lab"], g["strata"], P, stable_seed(g["gid"]))
    alt, inn = _design(c.L, g["idx"], g["lab"], plab)
    res = {}
    tg = np.arange(c.gK) if targets is None else np.asarray(targets, dtype=np.int64)
    if "response" in kinds and tg.size:
        n, K = tg.size, c.Ra.shape[1]
        S = np.full((n, alt.shape[1]), np.nan, dtype=np.float32)
        zbest = np.full(n, np.nan, dtype=np.float32)
        kbest = np.full(n, -1, dtype=np.int64)
        dirn = np.zeros(n, dtype=np.float32)
        opp = np.zeros(n, dtype=np.float32)
        rise = np.full(n, np.nan, dtype=np.float32)
        raw_share = np.full(n, np.nan, dtype=np.float32)
        sh_none = np.zeros(n, dtype=np.float32)
        sh_line = np.zeros(n, dtype=np.float32)
        n_none = np.zeros(n, dtype=np.int16)
        n_line = np.zeros(n, dtype=np.int16)
        n_carry = np.zeros(n, dtype=np.int16)

        def block(b0):
            b1 = min(n, b0 + RESP_BLOCK)
            gg = tg[b0:b1]
            Mk = np.repeat(c.M[gg], K, axis=0)
            d0, Z2, _, _ = _contrast(c.Ra[gg].reshape(-1, c.L), Mk, alt, inn, block=2048, square=True)
            Z2 = np.nan_to_num(Z2.reshape(b1 - b0, K, -1), nan=0.0)
            S[b0:b1] = Z2.sum(axis=1)                                          # omnibus over Y's drug-doses
            z0 = np.sign(np.nan_to_num(d0.reshape(b1 - b0, K))) * np.sqrt(Z2[:, :, 0])
            del Z2
            # the same contrast without the global-sensitivity correction (observed labels only)
            zr = np.nan_to_num(_contrast(c.Rz[gg].reshape(-1, c.L), Mk, alt[:, :1], inn[:, :1],
                                         block=2048)[1].reshape(b1 - b0, K), nan=0.0)
            dd_ = (z0 * np.abs(z0)).sum(axis=1)                                # dominant direction
            sd = np.sign(dd_)[:, None]
            dirn[b0:b1] = sd[:, 0]
            tot = (z0 * z0).sum(axis=1)
            ev = np.where(np.sign(z0) == sd, z0 * z0, 0.0)                     # evidence in the edge's direction
            evr = np.where(np.sign(zr) == sd, zr * zr, 0.0)
            evs = ev.sum(axis=1)
            ak = c.adj_kind[gg]
            carry = ev >= 1.0                                                  # drug-doses carrying the difference
            with np.errstate(invalid="ignore", divide="ignore"):
                opp[b0:b1] = np.where(tot > 0, (np.where(np.sign(z0) == -sd, z0 * z0, 0.0).sum(axis=1)) / tot, 0.0)
                raw_share[b0:b1] = np.where(evs > 0, evr.sum(axis=1) / evs, np.nan)
                rise[b0:b1] = np.where(evs > 0, (ev * (c.sgn[gg] > 0)).sum(axis=1) / evs, np.nan)
                sh_none[b0:b1] = np.where(evs > 0, (ev * (ak == 0)).sum(axis=1) / evs, 0.0)
                sh_line[b0:b1] = np.where(evs > 0, (ev * (ak == 1)).sum(axis=1) / evs, 0.0)
            n_none[b0:b1] = (carry & (ak == 0)).sum(axis=1)
            n_line[b0:b1] = (carry & (ak == 1)).sum(axis=1)
            n_carry[b0:b1] = carry.sum(axis=1)
            kb = np.argmax(np.where(np.sign(z0) == sd, np.abs(z0), -1.0), axis=1)
            kbest[b0:b1] = kb
            zbest[b0:b1] = z0[np.arange(b1 - b0), kb]
        _parallel(block, range(0, n, RESP_BLOCK))
        Tobs, Tp = _standardise(S)
        del S
        D, _, na, ni = _contrast(c.R[tg], c.M[tg], alt[:, :1], inn[:, :1])
        ok = (na >= MIN_SIDE) & (ni >= MIN_SIDE) & np.isfinite(Tobs) & (dirn != 0)
        Draw = _contrast(c.R_raw[tg], c.M[tg], alt[:, :1], inn[:, :1])[0]
        mi = _side_mean(c.R_raw[tg], c.M[tg], g["inn"])
        ma = _side_mean(c.R_raw[tg], c.M[tg], g["alt"])
        with np.errstate(invalid="ignore", divide="ignore"):
            ret = np.where(mi > 0, ma / mi, np.nan)
        Tp[~ok] = np.nan
        res["response"] = {"t": tg, "T": np.where(ok, Tobs, np.nan), "Tp": Tp, "D": D, "na": na, "ni": ni,
                           "D_raw": Draw, "ret": ret, "zbest": zbest, "kbest": kbest, "dir": dirn, "opp": opp,
                           "rise": rise,
                           "raw_share": raw_share, "sh_none": sh_none, "sh_line": sh_line, "n_none": n_none,
                           "n_line": n_line, "n_carry": n_carry, "one_sided": True,
                           "n_arr": _row_arrangements(g, c.M[tg])}
    if "baseline" in kinds and tg.size:
        D, Zt, na, ni = _contrast(c.B[tg], None, alt, inn)
        Tobs, Tp = _standardise(Zt)
        ok = (na >= MIN_SIDE) & (ni >= MIN_SIDE) & np.isfinite(Tobs)
        Tp[~ok] = np.nan
        res["baseline"] = {"t": tg, "T": np.where(ok, Tobs, np.nan), "Tp": Tp, "D": D, "na": na, "ni": ni,
                           "n_arr": _row_arrangements(g, np.isfinite(c.B[tg]))}
    if "sensitivity" in kinds:
        dsel = np.arange(c.Dn) if dd_mask is None else np.flatnonzero(dd_mask)
        if dsel.size:
            D, Zt, na, ni = _contrast(c.Aab[dsel], None, alt, inn)
            Tobs, Tp = _standardise(Zt)
            ok = (na >= MIN_SIDE) & (ni >= MIN_SIDE) & np.isfinite(Tobs)
            Tp[~ok] = np.nan
            res["sensitivity"] = {"t": dsel, "T": np.where(ok, Tobs, np.nan), "Tp": Tp, "D": D,
                                  "na": na, "ni": ni, "n_arr": _row_arrangements(g, np.isfinite(c.Aab[dsel]))}
    return res


def _row_arrangements(g, masks):
    """Per target (a row of masks: targets x lines, its usable lines), the number of distinct arrangements of the
    group's labels over the group lines it has (within organs when the group is permuted within organs): the
    smallest p a permutation test of that target can give is 1 / this (capped at 1e12). Once per distinct line set,
    from log-binomials of the organ counts."""
    from scipy.special import gammaln
    idx = g["idx"]
    m = np.asarray(masks, dtype=bool)[:, idx]
    out = np.zeros(m.shape[0], dtype=np.float64)
    if not m.shape[0]:
        return out
    key = np.packbits(m, axis=1)
    u, inv = np.unique(key, axis=0, return_inverse=True)
    U = np.unpackbits(u, axis=1)[:, :idx.size].astype(np.float64)
    lab = np.asarray(g["lab"], dtype=np.float64)
    if g["strata"] is None:
        H = np.ones((idx.size, 1))
    else:
        _, sidx = np.unique(g["strata"], return_inverse=True)
        H = np.zeros((idx.size, int(sidx.max()) + 1))
        H[np.arange(idx.size), sidx] = 1.0
    tot = U @ H
    alt = (U * lab[None, :]) @ H
    lg = (gammaln(tot + 1) - gammaln(alt + 1) - gammaln(tot - alt + 1)).sum(axis=1)
    out[:] = np.exp(np.minimum(lg, math.log(1e12)))[np.asarray(inv).ravel()]
    return out


def _side_mean(V, Mk, side):
    m = Mk[:, side] & np.isfinite(V[:, side])
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(m.sum(axis=1) > 0, np.where(m, V[:, side], 0.0).sum(axis=1) / m.sum(axis=1), np.nan)


def _inflation(Tobs, Tp):
    """Genomic-control style inflation of one group's statistics: the interquartile range of the observed T over all
    tested targets / that of the permutation null (>= 1; 1 with fewer than GC_MIN targets). A grouping that coincides
    with broad structure among the lines (many genes shifted together) spreads the bulk of the observed statistics
    wider than the null; they are divided by this factor."""
    t = np.asarray(Tobs, dtype=np.float64)
    t = t[np.isfinite(t)]
    n = _subsample(Tp, 200_000, 17).astype(np.float64)
    if t.size < GC_MIN or n.size < GC_MIN:
        return 1.0
    iq = np.subtract(*np.percentile(t, [75, 25]))
    iqn = np.subtract(*np.percentile(n, [75, 25]))
    return float(max(1.0, iq / iqn)) if iqn > 0 else 1.0


def _finish(res, seed):
    """Per kind of one genotype group: inflation-corrected T and p (the group's pooled null with its fitted tail,
    guarded per target by its own permutations and its arrangements: _guard_p). q is set over the whole family
    of the kind (_family_q), after _trim."""
    for kind, r in res.items():
        two = not r.get("one_sided")
        lam = _inflation(r["T"], r["Tp"])
        r["lambda"] = lam
        null = _Null(_subsample(r["Tp"], NULL_MAX, seed), two_sided=two)
        r["p"], r["own"] = _guarded(null.p(r["T"] / lam), r["T"], r["Tp"], two, r["n_arr"])
        r["T"] = r["T"] / lam
        r["n_null"] = null.n
        r.pop("Tp", None)
    return res


def _guarded(p, Tobs, Tp, two_sided, n_arr):
    """_guard_p for the candidate targets only (p < 2 Q_SIG; the guard can only raise p, and a target above that
    can never become an edge): their own permutation statistics against Tobs (before any inflation division)."""
    p = np.asarray(p, dtype=np.float64)
    out = p.copy()
    use = np.zeros(p.shape, dtype=bool)
    cand = np.flatnonzero(np.isfinite(p) & (p < 2 * Q_SIG))
    if cand.size:
        own = _own_stats(np.asarray(Tobs)[cand], np.asarray(Tp)[cand], two_sided)
        out[cand], use[cand] = _guard_p(p[cand], own, np.asarray(n_arr)[cand])
    return out, use


# ----------------------------------------------------------------------------- edge rows
def _mixed(rise):
    return bool(np.isfinite(rise) and MIXED <= rise <= 1.0 - MIXED)


def _response_dd(c, g, y, sign_d):
    """Per drug-dose k of Y's K (c.sel[y]) of a response edge: the contrast of the adjusted response (intact - altered,
    z units), the folds on each side (2 ** mean lfc over the side's measured lines, in Y's own direction), the score
    in the edge's direction (contrast x its sign, NaN last) and the order strongest first. None when a side has no
    measured line."""
    m = c.M[y]
    ii = g["inn"] & m
    aa = g["alt"] & m
    if not ii.any() or not aa.any():
        return None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        ra = c.Ra[y]
        con = np.nanmean(ra[:, ii], axis=1) - np.nanmean(ra[:, aa], axis=1)
        lf = c.Rl[y]
        fi = 2.0 ** (c.sgn[y] * np.nanmean(lf[:, ii], axis=1))
        fa = 2.0 ** (c.sgn[y] * np.nanmean(lf[:, aa], axis=1))
    sc = np.nan_to_num(con * (1 if sign_d >= 0 else -1), nan=-np.inf)
    o = np.argsort(-sc, kind="stable")
    return con, fi, fa, sc, o


def _flags_text(c, d):
    """A drug-dose's flags for a drug-dose list: ' [artifact flags: a, b]' (one of atlas_core.ARTIFACT_FLAGS among
    them), ' [flags: a, b]' (other flags), '' (none)."""
    f = str(c.dd_flags[d] or "").replace("; ", ", ")
    if not f:
        return ""
    return f" [{'artifact flags' if c.dd_art[d] else 'flags'}: {f}]"


def _response_all(c, g, y, sign_d, items):
    """A response edge's drugdoses_all (every one of Y's K drug-doses: contrast, folds and flags; strongest in the
    edge's direction first, those without a value on a side last), its art_share (the share of sum |contrast| over the
    K drug-doses carried by artifact-flagged ones; NaN without any contrast) and its artifact-flag reason ('' when none
    of the K drug-doses with a value is flagged): '(N% of the evidence[, the strongest among them]): every flagged
    one' - the strongest = the first of top_drugdoses (items), the one the reading names."""
    pd_ = _response_dd(c, g, y, sign_d)
    if pd_ is None:
        return "", np.nan, ""
    con, fi, fa, sc, o = pd_
    parts, flagged = [], []
    for k in o:
        d = int(c.sel[y, k])
        if np.isfinite(con[k]):
            parts.append(f"{c.dd_label[d]}: {_fmt_fold(fa[k])} vs {_fmt_fold(fi[k])} (z diff {con[k]:+.1f})"
                         + _flags_text(c, d))
            if c.dd_art[d]:
                flagged.append(d)
        else:
            parts.append(f"{c.dd_label[d]}: no value on one side" + _flags_text(c, d))
    fin = np.isfinite(con)
    tot = float(np.abs(con[fin]).sum())
    art = np.array([c.dd_art[int(c.sel[y, k])] for k in range(con.size)], dtype=bool)
    share = np.float32(np.abs(con[fin & art]).sum() / tot) if tot > 0 else np.float32(np.nan)
    reason = ""
    if flagged:
        head = (f"{int(math.floor(float(share) * 100))}% of the evidence" if np.isfinite(share) else
                "share of the evidence not measurable")
        strong = bool(items) and bool(c.dd_art[items[0][0]])
        reason = (f"supporting drug-doses with artifact flags ({head}{', the strongest among them' if strong else ''}"
                  "): " + "; ".join(f"{c.dd_label[d]} ({c.dd_flags[d]})" for d in flagged))
    return "; ".join(parts), share, reason


def _top_dd_response(c, g, y, sign_d, rise=np.nan):
    """The supporting drug-doses of a response edge: per drug-dose the contrast of the adjusted response (intact -
    altered, z units) and the folds on each side (2 ** mean lfc over the side's measured lines), the TOP_DD strongest.
    rise: the share of the evidence from drug-doses where the target rises. Mixed (_mixed): the list holds the
    strongest of each direction (the last place goes to the other direction's strongest when the top ones all go one
    way). Else the target's main direction comes first (stable), so that the reading's headline drug-dose is not a
    minority one going the other way."""
    pd_ = _response_dd(c, g, y, sign_d)
    if pd_ is None:
        return []
    con, fi, fa, sc, o = pd_
    top = [int(k) for k in o[:TOP_DD]]
    if _mixed(rise):
        if top and len({float(c.sgn[y][k]) for k in top}) == 1:
            other = [int(k) for k in o[TOP_DD:] if c.sgn[y][k] != c.sgn[y][top[0]] and sc[k] > 0]
            if other:
                top = top[:TOP_DD - 1] + other[:1]
    elif np.isfinite(rise):
        main = 1.0 if rise > 0.5 else -1.0
        top = [k for k in top if c.sgn[y][k] == main] + [k for k in top if c.sgn[y][k] != main]
    return [(int(c.sel[y, k]), float(con[k]), float(fi[k]), float(fa[k])) for k in top if np.isfinite(con[k])]


def _sides(g):
    if g["mech"] == "null":
        return f"lines without {g['gene']}", f"lines expressing {g['gene']}"
    tag = g["mech"] if g["mech"] in ("LoF", "GoF") else "altered"
    return f"{g['gene']}-{tag} lines", "the other lines"


def _activity_words(sign, what, response=False):
    """'X activity raises' / 'lowers'; for a drug response (response=True) 'strengthens' / 'weakens': the sign of a
    response edge is about how strongly the target responds in its own direction (r = per-line z x the sign of its
    pooled z), so for a target that falls under the drugs, 'strengthens' means a deeper fall."""
    if sign > 0:
        return f"{what} {'strengthens' if response else 'raises'}"
    if sign < 0:
        return f"{what} {'weakens' if response else 'lowers'}"
    return ""


def _grade_genotype(g, na, ni, q, block=False):
    """A: >= FULL_SIDE lines on each side (measured; within organs: those sharing an organ with the other side),
    q < Q_A, compared within organs, no co-occurrence alert (another gene's altered lines overlapping the altered
    side, or sitting on the other side: anti-occurrence), and nothing kind-specific that blocks it (block: a response
    edge that rests on the global-sensitivity correction, or whose evidence comes mostly from drug-doses without any
    correction). C when tissue-confounded (compared across organs and the sides' organs differ: the comparison
    cannot separate the gene from the tissue - graded as for a natural knockout). Else B."""
    if g["tissue"]:
        return "C"
    ok = (na >= FULL_SIDE and ni >= FULL_SIDE and q < Q_A and not g["cooccur"] and not g.get("anti")
          and g["stratified"] and g["n_alt_mixed"] >= FULL_SIDE and g["n_inn_mixed"] >= FULL_SIDE and not block)
    return "A" if ok else "B"


def _ref_ratio(c, g, y, k):
    """At Y's k-th drug-dose: the mean relative responsiveness s of the altered lines / that of the other lines (the
    reference Y was judged against), over Y's measured lines; NaN without a correction there."""
    s = c.S[y, k]
    m = c.M[y] & np.isfinite(s)
    a, i = m & g["alt"], m & g["inn"]
    if not a.any() or not i.any():
        return np.nan
    mi = float(s[i].mean())
    return float(s[a].mean()) / mi if mi > 0 else np.nan


def _correction_alerts(c, g, r, i, y, alt_w):
    """Alerts (and whether grade A is blocked) from the global-sensitivity correction of a response edge."""
    al, block = [], False
    kb = int(r["kbest"][i])
    lab = c.dd_label[c.sel[y, kb]] if kb >= 0 else "?"
    rs = float(r["raw_share"][i])
    if np.isfinite(rs) and rs < RAW_SHARE_MIN:
        rr = _ref_ratio(c, g, y, kb) if kb >= 0 else np.nan
        ref = (f" (at {lab} the reference responds {rr:.2f}x as strongly in the {alt_w} as in the others)"
               if np.isfinite(rr) else "")
        al.append(f"the difference exists only relative to the other genes responding at these drug-doses, which "
                  f"themselves differ between the two sides{ref}: either those lines respond differently to the drugs "
                  f"in general, or most of those genes depend on {g['gene']} themselves; without the correction "
                  f"{c.sym[y]}'s response differs little (raw contrast {float(r['D_raw'][i]):+.2f})")
        block = True
    elif kb >= 0:
        rr = _ref_ratio(c, g, y, kb)
        if np.isfinite(rr) and (rr < 0.8 or rr > 1.25):
            al.append(f"the reference genes at {lab} respond {rr:.2f}x as strongly in the {alt_w} as in the others "
                      "(the correction removed that part of the difference)")
    nn, sn = int(r["n_none"][i]), float(r["sh_none"][i])
    if nn or sn > 0:
        al.append(f"no global-sensitivity correction at {nn} of the {int(r['n_carry'][i])} drug-doses carrying the "
                  f"difference ({sn:.0%} of the evidence): too few other genes respond there and the lines' overall "
                  "responsiveness could not be estimated reliably; part of the difference may be the lines' general "
                  "sensitivity to those drugs")
        block = block or sn >= UNCHECKED_MAX
    nl, sl = int(r["n_line"][i]), float(r["sh_line"][i])
    if nl and sl >= 0.5:
        al.append(f"at {nl} of the {int(r['n_carry'][i])} drug-doses carrying the difference ({sl:.0%} of the "
                  "evidence) too few other genes respond to check for a resistance specific to those drugs: only the "
                  "lines' overall responsiveness was corrected there")
    return al, block


def _rise_word(up):
    return "a rise" if up else "a fall"


def _mixed_alert(target, rise, where):
    """A response target that rises at some drug-doses and falls at others: the sign of a response edge says how
    strongly it responds (in each drug-dose's own direction), not whether the source induces or represses it."""
    return (f"{target} rises at some {where} and falls at others ({rise:.0%} of the evidence from rises): the sign "
            "says how strongly it responds, not whether the source induces or represses it")


def _grade_null(g, na, ni, extra_c=False):
    return "B" if (na >= FULL_SIDE and ni >= FULL_SIDE and not g["tissue"] and not extra_c) else "C"


def _base_row():
    return {"source": "", "source_col": -1, "target": "", "target_col": -1, "target_dd": -1, "target_type": "gene",
            "kind": "", "grade": "", "sign": 0, "reading": "", "group": "", "mechanism": "", "n_altered": -1,
            "n_intact": -1, "n_lines": -1, "contrast": np.nan, "D_raw": np.nan, "retained_fraction": np.nan,
            "raw_share": np.nan, "rise_share": np.nan, "baseline_log2_diff": np.nan, "r": np.nan, "r_reverse": np.nan,
            "direction_clear": None, "p_direction": np.nan, "n_compounds": -1, "n_supporting": -1,
            "background_rate": np.nan, "compounds": "", "compounds_supporting": "", "drug_effect": "", "T": np.nan,
            "p": np.nan, "q": np.nan, "q_group": np.nan, "alerts": "", "top_drugdoses": "", "art_share": np.nan,
            "drugdoses_all": ""}


def _empty_edges():
    """An edges table with no rows but the column types of a filled one (str / float64 / int32 / bool)."""
    b = _base_row()
    cols = {}
    for k, v in b.items():
        if k == "direction_clear":
            cols[k] = pd.Series(dtype="boolean")
        elif isinstance(v, str):
            cols[k] = pd.Series(dtype="string")
        elif isinstance(v, (int, np.integer)):
            cols[k] = pd.Series(dtype=np.int32)
        else:
            cols[k] = pd.Series(dtype=np.float64)
    return pd.DataFrame(cols)


def _hits(r):
    """Targets written as edges: (genotype groups) q_group < Q_SIG within the group - a test significant over the
    table only because other groups have many hits is not significant in its own family -, else q < Q_SIG over the
    kind's family."""
    q = r["q_group"] if "q_group" in r else r["q"]
    return np.flatnonzero(np.isfinite(q) & (q < Q_SIG))


def _table_check(c, g, r, i, kind):
    """(within the table's family?, q_group, alert): an edge significant only within its own group gets grade C and
    an alert with the expected number of such false edges."""
    q = float(r["q"][i])
    qg = float(r["q_group"][i]) if "q_group" in r else np.nan
    if np.isfinite(q) and q < Q_SIG and (not np.isfinite(qg) or qg < Q_SIG):
        return True, qg, None
    kk = kind.split("_", 1)[1]
    rate = (getattr(c, "pseudo_group_rate", {}) or {}).get(kk)
    exp = (f" (random pseudo-groups give {rate:.2f} such edges per group, about {rate * c.n_geno_groups:.1f} over "
           f"the {c.n_geno_groups} groups)" if rate is not None else "")
    return False, qg, (f"significant within this group (q {_q2(qg)} over its {int(r['m'])} tests) but not over the "
                       f"whole table of genotype groups (q {_q2(q)}): a lead, not a finding{exp}")


def _response_rows(c, g, r, kind, base_res, x_for_alerts, extra_alerts_fn=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    for i in hit:
        y = int(r["t"][i])
        if y == x_for_alerts:
            continue
        D = float(r["D"][i])
        sgn_z = float(r["dir"][i])
        table, qg, tal = _table_check(c, g, r, i, kind)
        sf = g["sign_factor"]
        sign = int(sgn_z * sf) if sf else 0
        rise = float(r["rise"][i]) if "rise" in r else np.nan
        mixed = _mixed(rise)
        items = _top_dd_response(c, g, y, sgn_z, rise)
        al = list(extra_alerts_fn(y) if extra_alerts_fn else g["alerts"])
        na, ni = int(r["na"][i]), int(r["ni"][i])
        if na < g["n_alt"] or ni < g["n_inn"]:
            al.append(f"{c.sym[y]} measured in {na} of the {g['n_alt']} and {ni} of the {g['n_inn']} lines")
        bd = np.nan
        if base_res is not None:
            j = np.flatnonzero(base_res["t"] == y)
            bd = float(base_res["D"][j[0]]) if j.size else np.nan
        if np.isfinite(bd) and sgn_z > 0 and bd >= BASE_LOW:
            al.append(f"{c.sym[y]} is {2 ** bd:.1f}x lower at baseline in the {alt_w}: a weaker response may be "
                      "lower expression")
        if r["opp"][i] >= 0.25:
            al.append(f"the difference goes the other way at some of its drug-doses ({r['opp'][i]:.0%} of the "
                      "evidence)")
        if mixed:
            al.append(_mixed_alert(c.sym[y], rise, "of the drug-doses carrying the difference"))
        cal, block = _correction_alerts(c, g, r, i, y, alt_w)
        al.extend(cal)
        if not c.sel_sig[y].any():
            al.append("none of its drug-doses is significant pooled (a response only part of the lines show)")
        if r.get("own") is not None and bool(r["own"][i]):
            al.append(f"{c.sym[y]}'s own shuffles of the labels spread differently from the other genes': its own "
                      "permutation p is used")
        dd_all, art_share, art_reason = _response_all(c, g, y, sgn_z, items)
        if art_reason:
            al.append(art_reason)
        if tal:
            al.insert(0, tal)
        row = _base_row()
        top = "; ".join(f"{c.dd_label[d]}: {_fmt_fold(fa)} vs {_fmt_fold(fi)} (z diff {con:+.1f})"
                        for d, con, fi, fa in items)
        verb = "less" if sgn_z > 0 else "more"
        rd = f"{c.sym[y]} responds {verb} in the {alt_w} than in {inn_w}"
        if items:
            d, _, fi, fa = items[0]
            rd += f": {_fmt_fold(fa)} vs {_fmt_fold(fi)} at {c.dd_label[d]}"
            if mixed:
                up0 = c.Zp[d, y] > 0
                oth = [it for it in items[1:] if (c.Zp[it[0], y] > 0) != up0]
                if oth:
                    d2, _, fi2, fa2 = oth[0]
                    rd += f" ({_rise_word(up0)}), {_fmt_fold(fa2)} vs {_fmt_fold(fi2)} at {c.dd_label[d2]} " \
                          f"({_rise_word(not up0)})"
        aw = _activity_words(sign, f"{g['gene']} activity", response=True)
        if aw:
            rd += f"; {aw} {c.sym[y]}'s drug response"
        grade = _grade_genotype(g, na, ni, float(r["q"][i]), block) if g["kind"] == "genotype" else \
            _grade_null(g, na, ni, block)
        grade = grade if table else "C"
        row.update({"source": g["gene"] if g["kind"] != "null" else str(c.sym[x_for_alerts]),
                    "source_col": int(g["col"] if g["kind"] != "null" else x_for_alerts),
                    "target": str(c.sym[y]), "target_col": y, "kind": kind, "grade": grade, "sign": sign,
                    "reading": rd, "group": g["desc"], "mechanism": MECH_WORDS[g["mech"]], "n_altered": na,
                    "n_intact": ni, "contrast": D, "D_raw": float(r["D_raw"][i]),
                    "retained_fraction": float(r["ret"][i]), "raw_share": float(r["raw_share"][i]),
                    "rise_share": rise,
                    "baseline_log2_diff": bd, "T": float(r["T"][i]), "p": float(r["p"][i]), "q": float(r["q"][i]),
                    "q_group": qg, "alerts": _join(al), "top_drugdoses": top, "art_share": art_share,
                    "drugdoses_all": dd_all})
        rows.append(row)
    return rows


def _baseline_rows(c, g, r, kind, x_for_alerts, extra_alerts_fn=None, coabsent=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    for i in hit:
        y = int(r["t"][i])
        if y == x_for_alerts:
            continue
        D = float(r["D"][i])
        sf = g["sign_factor"]
        sign = int(np.sign(D) * sf) if sf else 0
        table, qg, tal = _table_check(c, g, r, i, kind)
        al = ([tal] if tal else []) + list(extra_alerts_fn(y) if extra_alerts_fn else g["alerts"])
        co = bool(coabsent(y)) if coabsent else False
        if co:
            al.append(f"{c.sym[y]} is also absent from most of these lines: which of the two drives the other cannot "
                      "be told")
        if r.get("own") is not None and bool(r["own"][i]):
            al.append(f"{c.sym[y]}'s own shuffles of the labels spread differently from the other genes': its own "
                      "permutation p is used")
        rd = f"{c.sym[y]} is {_fmt_fold(2 ** abs(D))} {'lower' if D > 0 else 'higher'} at baseline in the {alt_w} " \
             f"than in {inn_w}"
        aw = _activity_words(sign, f"{g['gene']} activity")
        if aw:
            rd += f"; {aw} {c.sym[y]}'s level"
        na, ni = int(r["na"][i]), int(r["ni"][i])
        grade = _grade_genotype(g, na, ni, float(r["q"][i])) if g["kind"] == "genotype" else \
            _grade_null(g, na, ni, co)
        grade = grade if table else "C"
        row = _base_row()
        row.update({"source": g["gene"] if g["kind"] != "null" else str(c.sym[x_for_alerts]),
                    "source_col": int(g["col"] if g["kind"] != "null" else x_for_alerts),
                    "target": str(c.sym[y]), "target_col": y, "kind": kind, "grade": grade, "sign": sign,
                    "reading": rd, "group": g["desc"], "mechanism": MECH_WORDS[g["mech"]], "n_altered": na,
                    "n_intact": ni, "contrast": D, "baseline_log2_diff": D, "T": float(r["T"][i]),
                    "p": float(r["p"][i]), "q": float(r["q"][i]), "q_group": qg, "alerts": _join(al)})
        rows.append(row)
    return rows


def _sens_rows(c, g, r, kind, x_for_alerts, extra_alerts_fn=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    for i in hit:
        d = int(r["t"][i])
        D = float(r["D"][i])
        sf = g["sign_factor"]
        sign = int(np.sign(D) * sf) if sf else 0
        table, qg, tal = _table_check(c, g, r, i, kind)
        al = ([tal] if tal else []) + list(extra_alerts_fn(None) if extra_alerts_fn else g["alerts"])
        fl = set(c.dd_flags[d].split("; "))
        bad = [f for f in ("unreliable plate only", "position not correctable", "wells disagree") if f in fl]
        if bad:
            al.append(f"the drug-dose's cell counts are less trustworthy ({', '.join(bad)})")
        if r.get("own") is not None and bool(r["own"][i]):
            al.append("this drug-dose's own shuffles of the labels spread differently from the other drug-doses': its "
                      "own permutation p is used")
        mi = _nanmean_side(c.Aab[d], g["inn"])
        ma = _nanmean_side(c.Aab[d], g["alt"])
        rd = f"cells under {c.dd_label[d]}: {_fmt_fold(2 ** ma)} in the {alt_w} vs {_fmt_fold(2 ** mi)} in " \
             f"{inn_w} (relative to the other lines in the same wells)"
        if sign:
            rd += f"; {g['gene']} activity {'protects the cells' if sign > 0 else 'makes the cells more sensitive'}"
        na, ni = int(r["na"][i]), int(r["ni"][i])
        grade = _grade_genotype(g, na, ni, float(r["q"][i])) if g["kind"] == "genotype" else _grade_null(g, na, ni)
        grade = grade if table else "C"
        row = _base_row()
        row.update({"source": g["gene"] if g["kind"] != "null" else str(c.sym[x_for_alerts]),
                    "source_col": int(g["col"] if g["kind"] != "null" else x_for_alerts),
                    "target": f"cells under {c.dd_label[d]}", "target_dd": d, "target_type": "cells",
                    "kind": kind, "grade": grade, "sign": sign, "reading": rd, "group": g["desc"],
                    "mechanism": MECH_WORDS[g["mech"]], "n_altered": na, "n_intact": ni, "contrast": D,
                    "T": float(r["T"][i]), "p": float(r["p"][i]), "q": float(r["q"][i]), "q_group": qg,
                    "alerts": _join(al),
                    "top_drugdoses": c.dd_label[d], "drugdoses_all": c.dd_label[d] + _flags_text(c, d)})
        rows.append(row)
    return rows


def _level_dd(c, y):
    """A level edge's drugdoses_all: the target's K drug-doses (the response the correlation uses), each with its pooled
    fold and z and its flags, strongest first."""
    out = []
    for d in c.sel[y]:
        d = int(d)
        out.append(f"{c.dd_label[d]}: {_fmt_fold(2 ** float(c.lfc_p[d, y]))} (z {float(c.Zp[d, y]):+.1f})"
                   + _flags_text(c, d))
    return "; ".join(out)


def _nanmean_side(v, side):
    x = v[side]
    x = x[np.isfinite(x)]
    return float(x.mean()) if x.size else np.nan


# ----------------------------------------------------------------------------- level (continuous modulator)
def _covariates(c):
    """Intercept, organ indicators (organs with >= 2 lines) and the top LEVEL_PCS principal components of the lines'
    baseline profiles (genes measured in every line, standardised)."""
    L = c.L
    cols = [np.ones(L)]
    names = ["intercept"]
    vc = pd.Series(c.organ).value_counts()
    for o, n in vc.items():
        if 2 <= n < L:
            cols.append((c.organ == o).astype(np.float64))
            names.append(f"organ {o}")
    full = c.measured.all(axis=0)
    X = c.B[full].T if full.sum() >= 10 else c.B.T
    X = X - X.mean(axis=0)
    sd = X.std(axis=0)
    X = X[:, sd > 0] / sd[sd > 0]
    if X.shape[1] >= 2:
        U, s, _ = np.linalg.svd(X, full_matrices=False)
        for j in range(min(LEVEL_PCS, U.shape[1] - 1)):
            cols.append(U[:, j])
            names.append(f"PC{j + 1}")
    C = np.column_stack(cols)
    return C, names, int(np.linalg.matrix_rank(C))


def _residualise(V, Mk, C):
    """Rows of V residualised on C over each row's own lines (Mk True); NaN elsewhere."""
    out = np.full(V.shape, np.nan)
    keys = {}
    for i in range(V.shape[0]):
        keys.setdefault(Mk[i].tobytes(), []).append(i)
    for key, rows in keys.items():
        m = np.frombuffer(key, dtype=bool)
        if m.sum() < 3:
            continue
        Cs = C[m]
        H = Cs @ np.linalg.pinv(Cs)
        Vs = V[np.asarray(rows)][:, m]
        out[np.asarray(rows)[:, None], np.flatnonzero(m)[None, :]] = Vs - Vs @ H.T
    return out


def _masked_corr(X, Y):
    """Row-wise correlation of X[i] and Y[i] over the lines where both are finite (recentred there)."""
    m = np.isfinite(X) & np.isfinite(Y)
    n = m.sum(axis=1)
    x = np.where(m, X, 0.0)
    y = np.where(m, Y, 0.0)
    with np.errstate(invalid="ignore", divide="ignore"):
        mx = x.sum(axis=1) / n
        my = y.sum(axis=1) / n
        xc = np.where(m, x - mx[:, None], 0.0)
        yc = np.where(m, y - my[:, None], 0.0)
        r = (xc * yc).sum(axis=1) / np.sqrt((xc ** 2).sum(axis=1) * (yc ** 2).sum(axis=1))
    return r, n


def _r_to_t(r, dof):
    """t = r sqrt(dof / (1 - r^2)) (monotone in r; unbounded, unlike r itself)."""
    r = np.clip(np.asarray(r, dtype=np.float64), -0.999999, 0.999999)
    return r * np.sqrt(dof / (1.0 - r ** 2))


def _fl_null(Xr, Yr, C, P, seed):
    """Freedman-Lane null of t = r sqrt((n - k - 1) / (1 - r^2)): Xr's residuals permuted over the common lines and
    residualised again on C there, correlated with Yr. Xr, Yr: pairs x lines (NaN outside each row's lines).
    Returns (t values, their degrees of freedom)."""
    rng = np.random.default_rng(seed)
    vals, dofs = [], []
    for i in range(Xr.shape[0]):
        m = np.isfinite(Xr[i]) & np.isfinite(Yr[i])
        n = int(m.sum())
        if n < LEVEL_MIN_LINES:
            continue
        Cs = C[m]
        k = int(np.linalg.matrix_rank(Cs))
        if n - k < 3:
            continue
        H = Cs @ np.linalg.pinv(Cs)
        x = Xr[i, m]
        y = Yr[i, m] - Yr[i, m].mean()
        perm = np.argsort(rng.random((P, n)), axis=1)
        xp = x[perm]
        xp = xp - xp @ H.T
        xp = xp - xp.mean(axis=1, keepdims=True)
        with np.errstate(invalid="ignore", divide="ignore"):
            r = (xp @ y) / np.sqrt((xp ** 2).sum(axis=1) * (y ** 2).sum())
        vals.append(_r_to_t(r, n - k - 1))
        dofs.append(np.full(P, n - k - 1, dtype=np.float64))
    if not vals:
        return np.zeros(0), np.zeros(0)
    return np.concatenate(vals), np.concatenate(dofs)


def _t_pvalue(T, dof, lam=1.0):
    """Two-sided p of t = r sqrt(dof / (1 - r^2)) from the t distribution with dof degrees of freedom (no floor).
    lam > 1 (the Freedman-Lane null spreads wider than the t distribution): each t's normal score is divided by lam
    first."""
    T = np.asarray(T, dtype=np.float64)
    dof = np.broadcast_to(np.asarray(dof, dtype=np.float64), T.shape)
    p = np.full(T.shape, np.nan)
    ok = np.isfinite(T) & (dof > 0)
    if not ok.any():
        return p
    pt = 2.0 * stats.t.sf(np.abs(T[ok]), dof[ok])
    if lam > 1.0:
        z = stats.norm.isf(np.clip(pt / 2.0, 1e-300, 0.5)) / lam
        pt = 2.0 * stats.norm.sf(z)
    p[ok] = np.clip(pt, 1e-300, 1.0)
    return p


def _t_calibration(Tnull, dofnull):
    """The Freedman-Lane permutation null against the t distribution: lam = its 99th percentile of |normal score| /
    the normal's (>= 1: p is made more conservative when the permutations spread wider), and its share of p below
    0.01 and 0.001 (expected 0.01 and 0.001)."""
    T = np.asarray(Tnull, dtype=np.float64)
    ok = np.isfinite(T)
    if ok.sum() < 1000:
        return 1.0, {"values": int(ok.sum()), "lambda": 1.0}
    pt = 2.0 * stats.t.sf(np.abs(T[ok]), np.asarray(dofnull, dtype=np.float64)[ok])
    z = stats.norm.isf(np.clip(pt / 2.0, 1e-300, 0.5))
    lam = float(max(1.0, np.percentile(z, 99) / stats.norm.isf(0.005)))
    return lam, {"values": int(ok.sum()), "lambda": round(lam, 4),
                 "share_p_below_0.01": round(float(np.mean(pt < 0.01)), 5),
                 "share_p_below_0.001": round(float(np.mean(pt < 0.001)), 6)}


def _fl_permute(V, C, seed):
    """Freedman-Lane permutation of every row of V (residuals; NaN outside each row's lines): the row's values
    shuffled among its own lines (one random permutation per row) and residualised again on C there."""
    rng = np.random.default_rng(seed)
    V = np.asarray(V, dtype=np.float64)
    m = np.isfinite(V)
    G, L = V.shape
    keys = rng.random((G, L))
    keys[~m] = np.inf
    order = np.argsort(keys, axis=1)                       # finite positions first, in random order
    pos = np.argsort(np.where(m, np.arange(L)[None, :], L + 1), axis=1, kind="stable")
    vals = np.take_along_axis(V, order, axis=1)
    out = np.full(V.shape, np.nan)
    np.put_along_axis(out, pos, vals, axis=1)
    return _residualise(out, np.isfinite(out), C)


def _level_prep(c, C):
    """Lineage-adjusted levels (over each gene's expressing lines) and response strengths (over its usable lines)."""
    Mx = c.measured.T
    okx = Mx.sum(axis=1) >= LEVEL_MIN_LINES
    c.Xres = _residualise(c.B, Mx & okx[:, None], C)
    okr = c.M.sum(axis=1) >= LEVEL_MIN_LINES
    c.Yres = _residualise(c.R, c.M & okr[:, None], C)


def _pair_corr(Xres, Yres, xi, yi, k_cov):
    """r, n and t over the common lines of each directed pair (X's level, Y's response), in blocks."""
    r = np.full(xi.size, np.nan)
    n = np.zeros(xi.size, dtype=np.int64)
    for s0 in range(0, xi.size, 50_000):
        s1 = min(xi.size, s0 + 50_000)
        r[s0:s1], n[s0:s1] = _masked_corr(Xres[xi[s0:s1]], Yres[yi[s0:s1]])
    dof = n - k_cov - 1
    ok = (n >= LEVEL_MIN_LINES) & (dof >= 3) & np.isfinite(r)
    return r, n, dof, ok, np.where(ok, _r_to_t(r, np.maximum(dof, 1)), np.nan)


def _r_cut(cut, dof, lam):
    """The smallest |r| whose calibrated p (_t_pvalue with lam) is at or below the BH cut, at dof degrees of
    freedom: the selection a level edge passed."""
    u = stats.norm.isf(min(max(cut, 1e-300), 1.0) / 2.0) * max(lam, 1.0)
    t = float(stats.t.isf(stats.norm.sf(u), max(dof, 1)))
    return t / math.sqrt(max(dof, 1) + t * t)


def _trunc_draws(m, s, a, U, V):
    """Draws of N(m, s) truncated to |Z| >= a (m: column of means, U and V: uniforms of the draws' shape): the
    upper tail with the probability of its mass, by the inverse of the normal's tail (no rejection, so a tail of
    1e-200 is drawn as well as a large one)."""
    lpu = stats.norm.logsf((a - m) / s)
    lpl = stats.norm.logcdf((-a - m) / s)
    mx = np.maximum(lpu, lpl)
    pu, pl = np.exp(lpu - mx), np.exp(lpl - mx)
    up = V < pu / (pu + pl)
    zu = m + s * stats.norm.isf(np.clip(U * np.exp(lpu), 1e-300, 1.0))
    zl = m + s * stats.norm.ppf(np.clip(U * np.exp(lpl), 1e-300, 1.0))
    zu = np.where(np.isfinite(zu), np.maximum(zu, a), a)
    zl = np.where(np.isfinite(zl), np.minimum(zl, -a), -a)
    return np.where(up, zu, zl)


def _level_direction(Xres, Yres, x, y, seed, r_f, r_r, dof_f, dof_r, r_cut, lam=1.0):
    """Is X -> Y clearly the stronger direction, beyond what selecting it would give? The edge X -> Y was written
    because |r(X level, Y response)| passed the BH cut on these lines, so its |r| is inflated by that selection (the
    winner's curse) and a plain comparison with the reverse |r(Y level, X response)| favours it. The test: under the
    null both directions are equally strong (|rho_f| = |rho_r| = rho), the two Fisher z have their sampling spread
    (lam / sqrt(dof - 1)) and the correlation of their errors (kappa: a bootstrap over lines, LEVEL_DIR_BOOT
    resamples), and the forward is drawn conditional on passing the same cut (|r| >= r_cut); p(rho) = the share of
    those draws whose |r_f| - |r_r| reaches the observed one (LEVEL_DIR_DRAWS each), and p_direction = its largest
    value over rho in LEVEL_DIR_GRID (the least favourable common strength, from none to 0.95). One-sided; 1 when
    the reverse is at least as strong. Returns (p_direction, kappa); NaN without a reverse (too few lines)."""
    if not (np.isfinite(r_f) and np.isfinite(r_r)) or dof_r < 3 or \
            np.isfinite(Xres[y]).sum() < LEVEL_MIN_LINES or np.isfinite(Yres[x]).sum() < LEVEL_MIN_LINES:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    L = Xres.shape[1]
    idx = rng.integers(0, L, (LEVEL_DIR_BOOT, L))
    bf, _ = _masked_corr(Xres[x][idx], Yres[y][idx])
    br, _ = _masked_corr(Xres[y][idx], Yres[x][idx])
    ok = np.isfinite(bf) & np.isfinite(br)
    kappa = np.nan
    if ok.sum() >= LEVEL_DIR_BOOT // 2:
        zf_, zr_ = (np.arctanh(np.clip(v[ok], -0.999999, 0.999999)) for v in (bf, br))
        if zf_.std() > 0 and zr_.std() > 0:
            kappa = float(np.corrcoef(zf_, zr_)[0, 1])
    d_obs = abs(r_f) - abs(r_r)
    if d_obs <= 0:
        return 1.0, kappa
    k = float(np.clip(kappa, -0.99, 0.99)) if np.isfinite(kappa) else 0.0
    sf = max(lam, 1.0) / math.sqrt(max(dof_f - 1, 1))
    sr = max(lam, 1.0) / math.sqrt(max(dof_r - 1, 1))
    a = float(np.arctanh(min(max(r_cut, 0.0), 0.999999)))
    G, B = LEVEL_DIR_GRID.size, LEVEL_DIR_DRAWS
    U, V, N = rng.random((G, B)), rng.random((G, B)), rng.standard_normal((G, B))
    mu = np.arctanh(np.minimum(LEVEL_DIR_GRID, 0.999))[:, None]
    mf = (1.0 if r_f >= 0 else -1.0) * mu
    zf = _trunc_draws(mf, sf, a, U, V)
    zr = (1.0 if r_r >= 0 else -1.0) * mu + sr * (k * (zf - mf) / sf + math.sqrt(1.0 - k * k) * N)
    d = np.abs(np.tanh(zf)) - np.abs(np.tanh(zr))
    p = (1.0 + (d >= d_obs).sum(axis=1)) / (1.0 + B)
    return float(min(1.0, p.max())), kappa


def _level_tests(c, C, k_cov, seed=0):
    """level: both directions of every related pair; p from the t distribution (calibrated by a Freedman-Lane null),
    BH over all directed pairs. Returns (DataFrame of the hits with r_reverse and the direction test, info), or None
    without relations. info: tests, calibration, and the permuted-level control (the same tests with X's level
    residuals permuted over its lines: how many would pass the real cut - the expected false edges)."""
    if c.rel is None or not len(c.rel):
        return None
    a = c.rel["col_a"].to_numpy(np.int64)
    b = c.rel["col_b"].to_numpy(np.int64)
    lo, hi = np.minimum(a, b), np.maximum(a, b)
    und = np.unique(np.c_[lo, hi], axis=0)
    xi = np.r_[und[:, 0], und[:, 1]]
    yi = np.r_[und[:, 1], und[:, 0]]
    nu = und.shape[0]                                            # row i's reverse is row i +- nu
    r, n, dof, ok, Tv = _pair_corr(c.Xres, c.Yres, xi, yi, k_cov)
    rng = np.random.default_rng(stable_seed("level-null", seed))
    pick = np.flatnonzero(ok)
    if pick.size > LEVEL_NULL_PAIRS:
        pick = rng.choice(pick, size=LEVEL_NULL_PAIRS, replace=False)
    null, ndof = _fl_null(c.Xres[xi[pick]], c.Yres[yi[pick]], C, LEVEL_NULL_PERMS, stable_seed("level-fl", seed))
    lam, cal = _t_calibration(null, ndof)
    p = _t_pvalue(Tv, dof, lam)
    q = _bh(p)
    cut = _bh_cut(p)
    hit = np.flatnonzero(np.isfinite(q) & (q < Q_SIG))
    rrev = np.r_[r[nu:], r[:nu]]
    drev = np.r_[dof[nu:], dof[:nu]]
    df = pd.DataFrame({"x": xi[hit], "y": yi[hit], "r": r[hit], "n": n[hit], "T": Tv[hit], "p": p[hit],
                       "q": q[hit], "r_rev": rrev[hit]})
    dirs = [_level_direction(c.Xres, c.Yres, int(xi[h]), int(yi[h]), stable_seed("level-dir", int(xi[h]), int(yi[h])),
                             float(r[h]), float(rrev[h]), int(dof[h]), int(drev[h]), _r_cut(cut, int(dof[h]), lam),
                             lam) for h in hit]
    df["p_dir"] = [d[0] for d in dirs]
    n_tests = int(ok.sum())
    del r, n, dof, Tv, p, q, rrev, drev
    Xp = _fl_permute(c.Xres, C, stable_seed("level-ctrl", seed))
    _, _, dofc, okc, Tc = _pair_corr(Xp, c.Yres, xi, yi, k_cov)
    pc = _t_pvalue(Tc, dofc, lam)
    ctrl = int(np.nansum(pc <= cut))
    info = {"tests": n_tests, "calibration": cal, "edges": int(hit.size), "p_cut": cut,
            "control_permuted_levels_edges": ctrl,
            "control_how": "every gene's lineage-adjusted level permuted over its lines (Freedman-Lane, one "
                           "permutation), the same tests, counted at the real run's BH cut: the edges a run without "
                           "any real level effect would give (expected false edges)"}
    return df, info


def _variable_dd(c):
    chi = np.nansum(c.Az ** 2, axis=1)
    n = np.isfinite(c.Az).sum(axis=1)
    with np.errstate(invalid="ignore"):
        p = np.where(n >= MIN_SIDE * 2, stats.chi2.sf(chi, np.maximum(n, 1)), np.nan)
    return np.isfinite(p) & (p < VAR_P), p


def _corr_genes_dd(Xg, Ab):
    """Masked correlations of every row of Xg (genes x lines) with every row of Ab (drug-doses x lines) over the
    lines both have: (r float32, n int32), genes x drug-doses."""
    ma = np.isfinite(Ab).astype(np.float64)
    a0 = np.nan_to_num(Ab)
    mx = np.isfinite(Xg).astype(np.float64)
    x0 = np.nan_to_num(Xg)
    nn = mx @ ma.T
    sx = x0 @ ma.T
    sa = mx @ a0.T
    with np.errstate(invalid="ignore", divide="ignore"):
        cov = x0 @ a0.T - sx * sa / nn
        vx = (x0 ** 2) @ ma.T - sx ** 2 / nn
        va = mx @ (a0 ** 2).T - sa ** 2 / nn
        r = (cov / np.sqrt(vx * va)).astype(np.float32)
    return r, np.rint(nn).astype(np.int32)


def _level_sensitivity(c, C, k_cov, dvar, seed=0):
    """Correlation of every gene's lineage-adjusted level with each variable drug-dose's lineage-adjusted relative
    abundance; p from the t distribution (calibrated by a Freedman-Lane null), BH over every (gene, drug-dose) test
    of the run. In blocks of LEVEL_BLOCK drug-doses (float32; only the candidates p < Q_SIG are kept). Returns
    (DataFrame of the hits, info) with the permuted-level control as in _level_tests."""
    ds = np.flatnonzero(dvar)
    info = {"tests": 0, "variable_drugdoses": int(ds.size)}
    if not ds.size:
        return None, info
    Ar = _residualise(c.Aab[ds], np.isfinite(c.Aab[ds]), C)            # drug-doses x lines
    gk = np.flatnonzero(np.isfinite(c.Xres).sum(axis=1) >= LEVEL_MIN_LINES)
    Xg = c.Xres[gk]
    # Freedman-Lane null on a random subset of genes with every line, against a random subset of drug-doses
    rng = np.random.default_rng(stable_seed("levsens-null", seed))
    full = np.flatnonzero(np.isfinite(Xg).all(axis=1))
    pool = full if full.size >= 20 else np.arange(gk.size)
    pick = rng.choice(pool, size=min(LEVEL_SENS_NULL_GENES, pool.size), replace=False) if pool.size else pool
    afull = np.flatnonzero(np.isfinite(Ar).all(axis=1))
    vals = []
    if afull.size and pick.size:
        Af = Ar[rng.choice(afull, size=min(LEVEL_SENS_NULL_DD, afull.size), replace=False)]
        H = C @ np.linalg.pinv(C)
        Afc = Af - Af.mean(axis=1, keepdims=True)
        na_ = np.sqrt((Afc ** 2).sum(axis=1))
        for gi in pick:
            x = np.nan_to_num(Xg[gi])
            perm = np.argsort(rng.random((LEVEL_SENS_NULL_PERMS, c.L)), axis=1)
            xp = x[perm]
            xp = xp - xp @ H.T
            xp = xp - xp.mean(axis=1, keepdims=True)
            with np.errstate(invalid="ignore", divide="ignore"):
                rr = (xp @ Afc.T) / (np.sqrt((xp ** 2).sum(axis=1))[:, None] * na_[None, :])
            vals.append(_r_to_t(rr, max(c.L - k_cov - 1, 1)).ravel())
    null = np.concatenate(vals) if vals else np.zeros(0)
    lam, cal = _t_calibration(null, np.full(null.size, max(c.L - k_cov - 1, 1), dtype=np.float64))
    del vals, null

    def scan(X):
        """(tests per drug-dose, candidates: gene idx, drug-dose idx, r, n, T, p with p < Q_SIG)"""
        m, out = np.zeros(ds.size, dtype=np.int64), []
        for b0 in range(0, ds.size, LEVEL_BLOCK):
            b1 = min(ds.size, b0 + LEVEL_BLOCK)
            r, n = _corr_genes_dd(X, Ar[b0:b1])
            dof = n - k_cov - 1
            ok = (n >= LEVEL_MIN_LINES) & (dof >= 3) & np.isfinite(r)
            m[b0:b1] = ok.sum(axis=0)
            gi, dj = np.nonzero(ok)
            T = _r_to_t(r[gi, dj], dof[gi, dj]).astype(np.float64)
            p = _t_pvalue(T, dof[gi, dj], lam)
            keep = p < Q_SIG
            out.append((gi[keep], dj[keep] + b0, r[gi, dj][keep], n[gi, dj][keep], T[keep], p[keep]))
            del r, n, dof, ok, gi, dj, T, p
        cat = [np.concatenate([o[j] for o in out]) for j in range(6)] if out else [np.zeros(0)] * 6
        return m, cat

    def per_dd_q(dj, p, m):
        qg = np.full(p.shape, np.nan)
        for j in np.unique(dj.astype(np.int64)):
            w = dj == j
            qg[w] = _bh(p[w], m[int(j)])
        return qg
    m, (gi, dj, r, n, T, p) = scan(Xg)
    q = _bh(p, int(m.sum()))
    qg = per_dd_q(dj, p, m)
    cut = _bh_cut(p, int(m.sum()))
    hit = np.isfinite(qg) & (qg < Q_SIG)
    both = hit & np.isfinite(q) & (q < Q_SIG)
    rows = pd.DataFrame({"x": gk[gi[hit].astype(np.int64)], "d": ds[dj[hit].astype(np.int64)],
                         "r": r[hit].astype(np.float64), "n": n[hit].astype(int), "T": T[hit], "p": p[hit],
                         "q": q[hit], "q_group": qg[hit]})
    mc, (_, djc, _, _, _, pc) = scan(_fl_permute(Xg, C, stable_seed("levsens-ctrl", seed)))
    qgc = per_dd_q(djc, pc, mc)
    ctrl = int(((qgc < Q_SIG) & (pc <= cut)).sum())
    ctrl_g = int(((qgc < Q_SIG) & ~(pc <= cut)).sum())
    info.update({"tests": int(m.sum()), "calibration": cal, "edges": int(both.sum()),
                 "edges_within_drugdose_only": int(hit.sum() - both.sum()),
                 "p_cut": cut, "control_permuted_levels_edges": ctrl,
                 "control_permuted_levels_within_drugdose_only": ctrl_g,
                 "control_how": "every gene's lineage-adjusted level permuted over its lines (Freedman-Lane, one "
                                "permutation), the same tests: the edges a run without any real level effect would "
                                "give at the real run's BH cut (expected false edges), and those significant only "
                                "within their drug-dose"})
    return rows, info


# ----------------------------------------------------------------------------- drug targets
def _drug_target(c):
    """Edges 'inhibiting / activating X raises / lowers Y' (module docstring, 4). Returns (rows, n_tests)."""
    dd = c.dd
    tcol = "targets" if "targets" in dd else None
    mcol = next((x for x in ("moa_broad", "moa-broad") if x in dd), None)
    # one compound = one molecule: names that differ only in letter case or a trailing salt word ('Ixazomib' /
    # 'Ixazomib citrate', 'crizotinib' / 'Crizotinib (hydrochloride)') count once; its names, ' / '-joined, name it
    keys = [_molecule_key(x) for x in c.salt]
    kn = {}
    for k_, nm in zip(keys, c.salt):
        kn.setdefault(k_, [])
        if str(nm) not in kn[k_]:
            kn[k_].append(str(nm))
    order_k = list(dict.fromkeys(keys))
    comps = [" / ".join(kn[k_]) for k_ in order_k]
    ci = {x: i for i, x in enumerate(order_k)}
    comp_of = np.array([ci[k_] for k_ in keys], dtype=np.int64)
    nC = len(comps)
    targets = [set() for _ in range(nC)]
    moa = ["unclear"] * nC
    for d in range(c.Dn):
        k = comp_of[d]
        if tcol:
            targets[k].update(_split_targets(dd[tcol].iloc[d]))
        if mcol and moa[k] == "unclear":
            moa[k] = _moa_class(dd[mcol].iloc[d])
    up = np.zeros((nC, c.gK), dtype=bool)
    dn = np.zeros((nC, c.gK), dtype=bool)
    np.logical_or.at(up, comp_of, c.sig_up)
    np.logical_or.at(dn, comp_of, c.sig_dn)
    Kup, Kdn = up.sum(axis=0), dn.sum(axis=0)
    by_t = {}
    for k in range(nC):
        for t in targets[k]:
            by_t.setdefault((t, moa[k]), []).append(k)
    tests = []
    for (t, cls), ks in sorted(by_t.items()):
        if len(ks) < 2:
            continue
        N = len(ks)
        for direction, M_, K_ in (("up", up, Kup), ("down", dn, Kdn)):
            kk = M_[ks].sum(axis=0)
            test = K_ >= 2
            p = np.ones(c.gK)
            p[test] = stats.hypergeom.sf(kk[test] - 1, nC, K_[test], N)
            p[~test] = np.nan
            p[test & (kk < 2)] = 1.0
            tests.append((t, cls, ks, direction, kk, K_, p))
    if not tests:
        return [], 0
    allp = np.concatenate([x[-1] for x in tests])
    allq = _bh(allp)
    rows = []
    off = 0
    for t, cls, ks, direction, kk, K_, p in tests:
        q = allq[off:off + c.gK]
        off += c.gK
        hit = np.flatnonzero(np.isfinite(q) & (q < Q_SIG) & (kk >= 2))
        names = [comps[k] for k in ks]
        for y in hit:
            if str(c.sym[y]).upper() == t:
                continue
            sup = [k for k in ks if (up if direction == "up" else dn)[k, y]]
            share = set.intersection(*[targets[k] for k in sup]) - {t} if sup else set()
            sign = {("inhibitor", "up"): -1, ("inhibitor", "down"): 1, ("activator", "up"): 1,
                    ("activator", "down"): -1}.get((cls, direction), 0)
            al = [DRUG_ALERT, f"consistent across {len(sup)} compounds ({', '.join(comps[k] for k in sup)})"]
            if share:
                al.append(f"the supporting compounds also share {', '.join(sorted(share)[:4])}: "
                          f"{'it' if len(share) == 1 else 'any of them'} could be the cause instead")
            if cls == "unclear":
                al.append("the compounds' mechanism (inhibitor or activator) is not recorded: sign not inferred")
            # the strongest drug-dose of each supporting compound; every significant one (drugdoses_all)
            tops, flagged, every, best = [], [], [], (-1.0, -1)
            M_ = c.sig_up if direction == "up" else c.sig_dn
            for k in sup:
                ds = np.flatnonzero((comp_of == k) & M_[:, y])
                if not ds.size:
                    continue
                az = np.abs(c.Zp[ds, y])
                d = ds[np.argmax(az)]
                tops.append(f"{c.dd_label[d]} {_fmt_fold(2 ** float(c.lfc_p[d, y]))}")
                if float(np.max(az)) > best[0]:
                    best = (float(np.max(az)), int(d))
                if c.dd_art[d]:
                    flagged.append(f"{c.dd_label[d]} ({c.dd_flags[d]})")
                for d2 in ds[np.argsort(-az, kind="stable")]:
                    every.append(f"{c.dd_label[d2]} {_fmt_fold(2 ** float(c.lfc_p[d2, y]))} (z "
                                 f"{float(c.Zp[d2, y]):+.1f})" + _flags_text(c, int(d2)))
            if flagged:
                strong = best[1] >= 0 and bool(c.dd_art[best[1]])
                al.append(f"supporting drug-doses with artifact flags ({len(flagged)} of the {len(tops)} supporting "
                          f"compounds{', the strongest among them' if strong else ''}): " + "; ".join(flagged))
            verb = {"inhibitor": "inhibiting", "activator": "activating"}.get(cls, "drugs targeting")
            rd = f"{verb} {t} {'raises' if direction == 'up' else 'lowers'} {c.sym[y]} ({int(kk[y])} of {len(ks)} " \
                 f"compounds; {K_[y] / nC:.0%} of all compounds)"
            row = _base_row()
            row.update({"source": t, "source_col": c.col_of.get(t, -1), "target": str(c.sym[y]), "target_col": int(y),
                        "kind": "drug_target", "grade": "B", "sign": sign, "reading": rd,
                        "group": f"{t} {cls}s: {', '.join(names)} ({len(ks)} compounds)", "mechanism": cls,
                        "n_compounds": len(ks), "n_supporting": int(kk[y]), "background_rate": float(K_[y] / nC),
                        "compounds": "; ".join(names), "compounds_supporting": "; ".join(comps[k] for k in sup),
                        "drug_effect": "raises" if direction == "up" else "lowers",
                        "contrast": float(kk[y] / len(ks)), "p": float(p[y]), "q": float(q[y]),
                        "alerts": _join(al), "top_drugdoses": "; ".join(tops), "drugdoses_all": "; ".join(every)})
            rows.append(row)
    return rows, int(np.isfinite(allp).sum())


SALT_WORDS = ("acetate", "besylate", "bitartrate", "bromide", "calcium", "chloride", "citrate", "dihydrochloride",
              "dimaleate", "dimesylate", "disodium", "ditosylate", "fumarate", "hemifumarate", "hydrobromide",
              "hydrochloride", "hydrate", "lactate", "maleate", "malate", "mesylate", "monohydrate", "phosphate",
              "potassium", "sesquihydrate", "sodium", "succinate", "sulfate", "tartrate", "tosylate",
              "trifluoroacetate", "trihydrochloride", "hcl", "tfa")


def _molecule_key(name):
    """A compound's molecule: its salt base (tlib.salt_base: a trailing bracketed salt removed), case-folded, with
    trailing salt and hydrate words removed ('Ixazomib citrate' -> 'ixazomib', 'Crizotinib (hydrochloride)' ->
    'crizotinib'). '(S)-Crizotinib' stays apart (another molecule)."""
    w = str(T.salt_base(name)).casefold().split()
    while len(w) > 1 and w[-1].strip(",.") in SALT_WORDS:
        w.pop()
    return " ".join(w)


# ----------------------------------------------------------------------------- the stage
def run(out, data=None, chunk=None, mem_gb=1.0, perms=PERMS, k=K_DD, pseudo=N_PSEUDO):
    """out = the tahoemap output folder. Writes out/direction/. data = the Tahoe-100M folder (for the cell-line
    metadata; default: the files atlas/file_index.json lists)."""
    t0 = time.time()
    meter = _PeakMeter()
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        info = _run(out, data, chunk, mem_gb, perms, k, pseudo, t0, meter)
    stamp_stage(out, "direction", VERSION, info)
    log(f"Direction done -> {os.path.join(out, 'direction')} ({info['minutes']} min; {info['edges']:,} edges)")
    return info


def _trim(r):
    """Keep only a kind's candidate targets (p < Q_SIG: no other can reach q < Q_SIG) and the family size m."""
    p = r["p"]
    n = p.size
    r["m"] = int(np.isfinite(p).sum())
    keep = np.isfinite(p) & (p < Q_SIG)
    for k_, v in list(r.items()):
        if isinstance(v, np.ndarray) and v.ndim >= 1 and v.shape[0] == n:
            r[k_] = v[keep]
    return r


def _family_q(items, kind):
    """BH q over every test of the kind in items (trimmed result dicts, e.g. all genotype groups): one family, so the
    share of false edges among the written ones is controlled over the whole table, not group by group. Uses the
    family size m (every finite test), so the q of the kept candidates are exact below Q_SIG. Returns (m, the BH
    p cut)."""
    rs = [r[kind] for r in items if kind in r]
    if not rs:
        return 0, Q_SIG
    m = int(sum(r["m"] for r in rs))
    p = np.concatenate([r["p"] for r in rs])
    q = _bh(p, m)
    off = 0
    for r in rs:
        n = r["p"].size
        r["q"] = q[off:off + n]
        off += n
    return m, _bh_cut(p, m)


GENO_KINDS = ("response", "baseline", "sensitivity")
EXPECTED_FALSE_HOW = (
    "expected_false: the controls' estimate of the false edges among the written ones; expected_false_upper: its 95% "
    "upper bound (Poisson: the controls are a small sample - 0 edges in 60 pseudo-groups still allows about 3 per 60 "
    "groups, and the level controls are one permutation each). The estimate can be low when real groups overlap "
    "other recorded or unrecorded alterations, tissue programmes or each other, which random groups do not.")


def _poisson_upper(k, conf=0.95):
    """One-sided upper confidence bound of a Poisson mean after observing k events (k = 0: about 3.0)."""
    return float(stats.chi2.ppf(conf, 2 * (int(k) + 1)) / 2.0)


def _run(out, data, chunk, mem_gb, perms, k, n_pseudo, t0, meter=None):
    od = folder(out, "direction")
    c = _load(out, data)
    log(f"Direction: {c.gK:,} genes x {c.Dn:,} drug-doses x {c.L} lines; cell-line genetics: {c.meta_src}")
    _responses(c, chunk, mem_gb, k)
    geno, records, gsrc, recorded = _genotype_groups(c)
    log(f"  genotype groups: {len(geno)} (driver genes recorded in >= {MIN_SIDE} lines, LoF / GoF / any)")
    rows = []

    # ---- 1. genotype groups: p per group (its pooled null), q over the family of each kind (every group), rows
    def test_all(groups):
        res_all = []
        for g in groups:
            res = _finish(_test_group(c, g, GENO_KINDS, perms), stable_seed(g["gid"], 1))
            g["lambda"] = {kk: round(float(v["lambda"]), 3) for kk, v in res.items()}
            g["res"] = None
            if g["kind"] == "genotype" and g["gene"] in ("TP53", "KEAP1"):
                g["res"] = {kk: {a: (b.copy() if isinstance(b, np.ndarray) else b) for a, b in v.items()}
                            for kk, v in res.items()}
            for v in res.values():
                _trim(v)
            res_all.append((g, res))
        return res_all
    real = test_all(geno)
    fam = {kk: _family_q([r for _, r in real], kk) for kk in GENO_KINDS}
    cuts = {kk: fam[kk][1] for kk in GENO_KINDS}
    for _, res in real:                                       # and within each group (q_group)
        for v in res.values():
            v["q_group"] = _bh(v["p"], v["m"])
    log(f"    tested in {(time.time() - t0) / 60:.1f} min")
    ngroups = _null_groups(c, geno, records)
    pseudo = _pseudo_groups(c, geno, n_pseudo, ngroups) if n_pseudo else []
    log(f"  negative controls: {len(pseudo)} random pseudo-groups of the real groups' sizes ...")
    pseudo_counts = []
    for g, res in test_all(pseudo):
        nr, ng = {}, {}
        for kk, v in res.items():
            qg = _bh(v["p"], v["m"])
            ing = np.isfinite(qg) & (qg < Q_SIG)
            ng[kk] = int(ing.sum())                           # within the group (written, grade C at least)
            # ... and also at the real family's cut (grade A / B); no real group: within the group alone
            nr[kk] = int((ing & (v["p"] <= cuts[kk])).sum()) if fam[kk][0] else ng[kk]
        nt = {kk: int(v["m"]) for kk, v in res.items()}
        g["n_edges"], g["n_tested"], g["n_edges_group"] = nr, nt, ng
        pseudo_counts.append((g, nr, nt, ng))
    c.pseudo_group_rate = {kk: (float(np.mean([x[3].get(kk, 0) for x in pseudo_counts if kk in x[2]]))
                                if any(kk in x[2] for x in pseudo_counts) else None) for kk in GENO_KINDS}
    c.n_geno_groups = len(geno)
    real_counts = []
    for g, res in real:
        nr = {kk: int(np.nansum((v["q"] < Q_SIG) & (v["q_group"] < Q_SIG))) for kk, v in res.items()}
        ng = {kk: int(np.nansum(v["q_group"] < Q_SIG)) for kk, v in res.items()}
        nt = {kk: int(v["m"]) for kk, v in res.items()}
        g["n_edges"], g["n_tested"], g["n_edges_group"] = nr, nt, ng
        real_counts.append((g, nr, nt, ng))
        if g.get("res"):                                      # full results (controls): q of the family
            for kk, v in g["res"].items():
                q = np.full(v["p"].shape, np.nan)
                qg = np.full(v["p"].shape, np.nan)
                pos = {int(t): j for j, t in enumerate(res[kk]["t"])}
                for j, t in enumerate(v["t"]):
                    if int(t) in pos:
                        q[j] = res[kk]["q"][pos[int(t)]]
                        qg[j] = res[kk]["q_group"][pos[int(t)]]
                v["q"], v["q_group"] = q, qg
        x = g["col"]
        g["n_written"] = {}                                   # groups.parquet: the edges written (any grade)
        for kk, fn in (("response", lambda v: _response_rows(c, g, v, "genotype_response", res.get("baseline"), x)),
                       ("baseline", lambda v: _baseline_rows(c, g, v, "genotype_baseline", x)),
                       ("sensitivity", lambda v: _sens_rows(c, g, v, "genotype_sensitivity", x))):
            if kk in res:
                new = fn(res[kk])
                g["n_written"][kk] = len(new)
                rows.extend(new)
    quiet = 0
    for g, nr, nt, ng in real_counts:
        if not sum(nr.values()) and not sum(ng.values()):
            quiet += 1
            continue
        extra = {kk: ng.get(kk, 0) - nr.get(kk, 0) for kk in GENO_KINDS}
        log(f"    {g['desc']}: edges response {nr.get('response', 0)} (+{extra['response']} within the group only), "
            f"baseline {nr.get('baseline', 0)} (+{extra['baseline']}), sensitivity {nr.get('sensitivity', 0)} "
            f"(+{extra['sensitivity']})" + ("" if g["stratified"] else " (across organs)"))
    log(f"    ({quiet} of {len(real_counts)} groups without an edge; q over every group of a kind: "
        + ", ".join(f"{kk} {fam[kk][0]:,} tests" for kk in GENO_KINDS) + ")")

    # ---- 2. expression-null groups (related pairs; variable drug-doses)
    log(f"    ({(time.time() - t0) / 60:.1f} min so far)")
    dvar, dvar_p = _variable_dd(c)
    log(f"  expression-null groups: {len(ngroups)} line sets ({sum(len(g['genes']) for g in ngroups)} genes); "
        f"{int(dvar.sum())} drug-doses with line-to-line differences in cell numbers (chi-square p < {VAR_P})")
    Pm = c.partners
    null_res = []
    pools = {kk: [] for kk in GENO_KINDS}
    cap = max(500, NULL_MAX // max(1, len(ngroups)))
    for g in ngroups:
        part = set()
        for x in g["genes"]:
            part.update(Pm.indices[Pm.indptr[x]:Pm.indptr[x + 1]].tolist())
        part -= set(g["genes"])
        tg = np.array(sorted(part), dtype=np.int64)
        # baseline / response of the partners: within organs; across organs (a separate BH family) only when the
        # lines lacking X are not concentrated in organs - else X's absence cannot be told from the tissue there
        across_ok = g["stratified"] or not g["tissue"]
        kinds = GENO_KINDS if tg.size and across_ok else ("sensitivity",)
        g["partners_withheld"] = bool(tg.size and not across_ok)
        if tg.size and not g["stratified"]:
            g["note"] = ("baseline and response compared across organs (no within-organ comparison possible; the "
                         "lines lacking it are not concentrated in organs): a separate BH family" if across_ok else
                         f"baseline and response not tested: the lines lacking it are concentrated in organs "
                         f"(organ-enrichment p {g['organ_p']:.2g}) and cannot be compared within organs, so its "
                         "absence cannot be told from the tissue; cell numbers are tested across organs")
        res = _test_group(c, g, kinds, PERMS_NULL, targets=tg, dd_mask=dvar)
        for kk, v in res.items():
            two = not v.get("one_sided")
            pools[kk].append(_subsample(v["Tp"], cap, stable_seed(g["gid"], kk)))
            with np.errstate(invalid="ignore"):
                big = np.isfinite(v["T"]) & ((np.abs(v["T"]) if two else v["T"]) > 1.0)
            v["own_s"] = _own_stats(v["T"], v["Tp"], two, sort_rows=big)
            v.pop("Tp", None)
        null_res.append((g, res))
    nulls = {kk: _Null(np.concatenate(v) if v else np.zeros(0), two_sided=(kk != "response"))
             for kk, v in pools.items()}
    del pools
    for g, res in null_res:
        for kk, v in res.items():
            v["p"], v["own"] = _guard_p(nulls[kk].p(v["T"]), v.pop("own_s"), v["n_arr"])
            _trim(v)
    n_null_tests = {}
    for kk in GENO_KINDS:                                      # BH over the kind: within / across organs apart
        for st in (True, False):
            m, _ = _family_q([r for g, r in null_res if bool(g["stratified"]) == st], kk)
            n_null_tests[f"{kk}_{'within' if st else 'across'}_organs"] = m
    null_absent = c.null.T                                       # genes x lines
    for g, res in null_res:
        g["n_edges"] = {}
        for x in g["genes"]:
            def alerts_fn(_y, g=g, x=x):
                return _null_gene_alerts(c, g, x, records)
            px = set(Pm.indices[Pm.indptr[x]:Pm.indptr[x + 1]].tolist())

            def coab(y, g=g):
                inter = int((null_absent[y] & g["alt"]).sum())
                return inter and inter / int((null_absent[y] | g["alt"]).sum()) >= JACCARD_CO
            for kk, v in res.items():
                if kk == "sensitivity":
                    new = _sens_rows(c, g, v, "null_sensitivity", x, alerts_fn)
                else:
                    keep = np.isin(v["t"], list(px))
                    vv = {a: (b[keep] if isinstance(b, np.ndarray) and b.shape[:1] == keep.shape else b)
                          for a, b in v.items()}
                    if kk == "response":
                        new = _response_rows(c, g, vv, "null_response", None, x, alerts_fn)
                    else:
                        new = _baseline_rows(c, g, vv, "null_baseline", x, alerts_fn, coab)
                g["n_edges"][kk] = g["n_edges"].get(kk, 0) + len(new)
                rows.extend(new)

    log(f"    expression-null tests done ({(time.time() - t0) / 60:.1f} min so far)")

    # ---- 3. level (related pairs) and level_sensitivity
    C, cov_names, k_cov = _covariates(c)
    _level_prep(c, C)
    lev = _level_tests(c, C, k_cov)
    level_info = {"tests": 0}
    if lev is not None:
        ldf, level_info = lev
        for t in ldf.itertuples(index=False):
            x, y = int(t.x), int(t.y)
            rr = float(t.r_rev) if np.isfinite(t.r_rev) else np.nan
            pdir = float(t.p_dir) if np.isfinite(t.p_dir) else np.nan
            clear = bool(np.isfinite(rr) and np.isfinite(pdir) and abs(t.r) > abs(rr) and pdir < LEVEL_DIR_P)
            al = [TISSUE_ALERT, PRECISION_ALERT]
            rise = float(c.rise_all[y])
            if _mixed(rise):
                al.append(_mixed_alert(c.sym[y], rise, "of its drug-doses"))
            if not np.isfinite(rr) or not np.isfinite(pdir):
                al.append(f"the reverse ({c.sym[y]}'s level and {c.sym[x]}'s response) could not be tested (too few "
                          "lines): the direction is unclear")
            elif not clear:
                al.append(f"the reverse ({c.sym[y]}'s level and {c.sym[x]}'s response, r {rr:+.2f}) is not clearly "
                          "weaker once it is allowed for that this arrow was written because it is strong, which "
                          f"alone makes it look the stronger (p {pdir:.2g}): the direction is unclear")
            row = _base_row()
            row.update({"source": str(c.sym[x]), "source_col": x, "target": str(c.sym[y]), "target_col": y,
                        "kind": "level", "grade": "C", "sign": int(np.sign(t.r)),
                        "reading": f"lines with more {c.sym[x]} (lineage-adjusted) show a "
                                   f"{'stronger' if t.r > 0 else 'weaker'} {c.sym[y]} drug response "
                                   f"(r {t.r:+.2f}; reverse {rr:+.2f})",
                        "group": f"{c.sym[x]} level across {int(t.n)} lines (lineage-adjusted)",
                        "mechanism": "level", "n_lines": int(t.n), "contrast": float(t.r), "r": float(t.r),
                        "r_reverse": rr, "rise_share": rise, "direction_clear": clear, "p_direction": pdir,
                        "T": float(t.T),
                        "p": float(t.p), "q": float(t.q), "alerts": _join(al), "drugdoses_all": _level_dd(c, y)})
            rows.append(row)
    log(f"  level: {level_info.get('tests', 0):,} directed related pairs, {level_info.get('edges', 0)} edges "
        f"({(time.time() - t0) / 60:.1f} min so far)")
    ls, ls_info = _level_sensitivity(c, C, k_cov, dvar)
    log(f"  level_sensitivity: {ls_info.get('tests', 0):,} (gene, drug-dose) tests, {ls_info.get('edges', 0)} "
        f"edges over the table, {ls_info.get('edges_within_drugdose_only', 0)} within their drug-dose only")
    if ls is not None:
        tset = {}
        for t in ls.itertuples(index=False):
            x, d = int(t.x), int(t.d)
            if d not in tset:
                tset[d] = set(_split_targets(c.dd["targets"].iloc[d])) if "targets" in c.dd else set()
            note = f" ({c.sym[x]} is a listed target of the drug)" if str(c.sym[x]).upper() in tset[d] else ""
            al = [TISSUE_ALERT]
            if not (np.isfinite(t.q) and t.q < Q_SIG):     # within its drug-dose only
                nc = ls_info['control_permuted_levels_within_drugdose_only']
                al.insert(0, f"significant among the genes tested for this drug-dose (q {_q2(t.q_group)}) but not "
                             f"over all {ls_info['tests']:,} (gene, drug-dose) tests (q {_q2(t.q)}): a lead (the same "
                             f"tests with the levels permuted give {nc} such edge{'' if nc == 1 else 's'})")
            row = _base_row()
            row.update({"source": str(c.sym[x]), "source_col": x, "target": f"cells under {c.dd_label[d]}",
                        "target_dd": d, "target_type": "cells", "kind": "level_sensitivity", "grade": "C",
                        "sign": int(np.sign(t.r)),
                        "reading": f"lines with more {c.sym[x]} (lineage-adjusted) have "
                                   f"{'more' if t.r > 0 else 'fewer'} cells under {c.dd_label[d]} "
                                   f"(r {t.r:+.2f}){note}",
                        "group": f"{c.sym[x]} level across {int(t.n)} lines (lineage-adjusted)",
                        "mechanism": "level", "n_lines": int(t.n), "contrast": float(t.r), "r": float(t.r),
                        "T": float(t.T), "p": float(t.p), "q": float(t.q), "q_group": float(t.q_group),
                        "alerts": _join(al), "top_drugdoses": c.dd_label[d],
                        "drugdoses_all": c.dd_label[d] + _flags_text(c, d)})
            rows.append(row)

    # ---- 4. drug targets
    drows, n_dt_tests = _drug_target(c)
    rows.extend(drows)

    # ---- tables
    if rows:
        edges = pd.DataFrame(rows, columns=list(_base_row()))
        ko = {kk: i for i, kk in enumerate(KINDS)}
        edges["_k"] = edges["kind"].map(ko)
        edges = edges.sort_values(["_k", "grade", "q", "p", "source", "target"], kind="stable").drop(columns="_k")
        edges = edges.reset_index(drop=True)
        for cname in ("source_col", "target_col", "target_dd", "n_altered", "n_intact", "n_lines", "n_compounds",
                      "n_supporting", "sign"):
            edges[cname] = edges[cname].astype(np.int32)
        edges["direction_clear"] = edges["direction_clear"].astype(object)
    else:
        edges = _empty_edges()
    edges = _add_tiers(edges)
    write_parquet(edges, os.path.join(od, "edges.parquet"))

    group_rows = [_group_row(c, g) for g in geno + ngroups + pseudo]
    groups_df = pd.DataFrame(group_rows) if group_rows else pd.DataFrame(columns=list(GROUP_DOCS))
    groups_df = _add_group_tiers(groups_df)
    write_parquet(groups_df, os.path.join(od, "groups.parquet"))

    controls = _controls(c, geno, real_counts, pseudo_counts, edges, cuts, fam, level_info, ls_info)
    write_json(controls, os.path.join(od, "controls.json"))
    counts = {kk: {gr: int(((edges["kind"] == kk) & (edges["grade"] == gr)).sum()) for gr in ("A", "B", "C")}
              for kk in KINDS}
    n_across = sum(1 for g in ngroups if not g["stratified"])
    nt_sets = [g for g in ngroups if g.get("partners_withheld")]       # partners existed, not tested (note says why)
    info = {"version": VERSION, "genes": c.gK, "drugdoses": c.Dn, "lines": c.L, "k_drugdoses": int(c.sel.shape[1]),
            "chunk": c.chunk, "permutations": int(perms), "permutations_null_groups": PERMS_NULL,
            "cell_line_genetics": gsrc, "lines_with_genetics_record": int(recorded.sum()),
            "organs_from": c.organ_src, "lines_with_organ": int(c.organ_known.sum()),
            "groups_tested": {"genotype": len(geno), "expression_null_line_sets": len(ngroups),
                              "expression_null_line_sets_across_organs": n_across,
                              "expression_null_genes": int(sum(len(g["genes"]) for g in ngroups)),
                              "expression_null_genes_across_organs": int(sum(len(g["genes"]) for g in ngroups
                                                                             if not g["stratified"])),
                              "expression_null_line_sets_not_tested_partners": len(nt_sets),
                              "expression_null_genes_not_tested_partners": int(sum(len(g["genes"])
                                                                                   for g in nt_sets)),
                              "pseudo_controls": len(pseudo)},
            "global_sensitivity_correction": c.adj_counts,
            "tests": {"genotype": {kk: fam[kk][0] for kk in GENO_KINDS},
                      "genotype_p_cut": {kk: cuts[kk] for kk in GENO_KINDS},
                      "expression_null": n_null_tests, "level_pairs": level_info.get("tests", 0),
                      "level_sensitivity": ls_info.get("tests", 0), "drug_target": n_dt_tests},
            "null_tail": {kk: v.describe() for kk, v in nulls.items()},
            "level_calibration": {"level": level_info.get("calibration"),
                                  "level_sensitivity": ls_info.get("calibration")},
            "variable_drugdoses": int(dvar.sum()), "level_covariates": cov_names,
            "relations": c.rel is not None and len(c.rel) > 0, "edges": int(len(edges)),
            "edges_by_kind_and_grade": counts,
            "edges_by_kind": {kk: int((edges["kind"] == kk).sum()) for kk in KINDS},
            "reason_tiers": {"edges_with_alert": int((edges["n_alerts"] > 0).sum()),
                             "edges_with_note": int((edges["n_notes"] > 0).sum()),
                             "edges_with_caveat": int((edges["n_caveats"] > 0).sum()),
                             "edges_with_support": int((edges["n_support"] > 0).sum()),
                             "edges_without_alert_by_kind": {
                                 kk: int(((edges["kind"] == kk) & (edges["n_alerts"] == 0)).sum()) for kk in KINDS},
                             "thresholds": {"NOTE_MEASURED_FRAC": NOTE_MEASURED_FRAC, "NOTE_ART_SHARE": NOTE_ART_SHARE,
                                            "NOTE_WITHIN_ORGAN_FRAC": NOTE_WITHIN_ORGAN_FRAC,
                                            "NOTE_COABSENT_SETS": NOTE_COABSENT_SETS,
                                            "NOTE_NOT_EXPRESSED_FRAC": NOTE_NOT_EXPRESSED_FRAC,
                                            "FULL_SIDE": FULL_SIDE}},
            "false_positive_rate": controls["negative"]["summary"],
            "expected_false_edges": controls["expected_false_edges"],
            "minutes": round((time.time() - t0) / 60, 2)}
    info["peak_rss_mb"], info["peak_rss_how"] = meter.stop() if meter is not None else (
        _peak_rss_mb(), "the process's peak (it may include earlier stages of the same run)")
    write_json(info, os.path.join(od, "info.json"))
    text, undocumented = readme(edges, groups_df, info)
    _write_text(os.path.join(od, "README.md"), text)
    if undocumented:
        log(f"  WARNING: columns without a description in README.md: {', '.join(undocumented)}")
    return info


TIER_COLS = ("n_alerts", "notes", "caveats", "support", "alerts_all", "n_notes", "n_caveats", "n_support")


def _add_tiers(edges):
    """The edges with every reason in its tier (tier_columns): 'alerts' keeps only the reasons that carry the warning
    sign, the others move to notes / caveats / support, and alerts_all keeps every reason in the original order.
    art_share is stored as float32 (reason_tier reads that value). Nothing else changes."""
    e = edges.copy()
    e["art_share"] = pd.to_numeric(e["art_share"], errors="coerce").astype(np.float32)
    e["drugdoses_all"] = e["drugdoses_all"].fillna("").astype(str) if len(e) else e["drugdoses_all"].astype("string")
    t = tier_columns(e["alerts"].fillna("").astype(str).tolist(), e["art_share"].to_numpy())
    for k in ("alerts", "notes", "caveats", "support", "alerts_all"):
        e[k] = pd.array(t[k], dtype="string") if not len(e) else t[k]
    for k in TIERS:
        e[f"n_{k}"] = np.asarray(t[f"n_{k}"], dtype=np.int16)
    return e[[x for x in e.columns if x not in TIER_COLS] + list(TIER_COLS)]


def _add_group_tiers(groups):
    """groups.parquet with its reasons in tiers: alerts (the warning sign), notes (graded reasons below their
    thresholds) and alerts_all (every reason, in order). A group has no caveats or support of its own."""
    gdf = groups.copy()
    if "alerts" not in gdf:
        gdf["alerts"] = ""
    al, no, every = [], [], []
    for txt in gdf["alerts"].fillna("").astype(str):
        rs = split_reasons(txt)
        tr = [reason_tier(r) for r in rs]
        al.append(_join([r for r, t in zip(rs, tr) if t != "notes"]))     # (a group has no caveat or support)
        no.append(_plain([r for r, t in zip(rs, tr) if t == "notes"]))
        every.append(_plain(rs))
    gdf["alerts"] = al if len(gdf) else pd.Series(dtype="string")
    pos = list(gdf.columns).index("alerts") + 1
    for k, v in (("notes", no), ("alerts_all", every)):
        if k in gdf:
            gdf = gdf.drop(columns=k)
        gdf.insert(pos, k, v if len(gdf) else pd.Series(dtype="string"))
        pos += 1
    return gdf


def _group_row(c, g):
    nm = c.line_name
    ne = g["n_written"] if "n_written" in g else (g.get("n_edges") or {})
    return {"group_id": g["gid"], "kind": g["kind"], "gene": g["gene"], "gene_col": int(g["col"]),
            "mechanism": MECH_WORDS[g["mech"]], "description": g["desc"], "n_altered": g["n_alt"],
            "n_intact": g["n_inn"], "altered_lines": ", ".join(nm[g["alt"]]), "intact_lines": ", ".join(nm[g["inn"]]),
            "organs_altered": g["organs_alt"], "organs_intact": g["organs_inn"], "stratified": bool(g["stratified"]),
            "n_arrangements": int(g["n_arr"]), "n_altered_shared_organs": int(g["n_alt_mixed"]),
            "n_intact_shared_organs": int(g["n_inn_mixed"]),
            "organ_enrichment_p": float(g["organ_p"]) if np.isfinite(g["organ_p"]) else np.nan,
            "tissue_confounded": bool(g["tissue"]),
            "cooccurs_with": "; ".join(f"{h} ({j:.2f})" for h, j in g["cooccur"]),
            "anti_occurs_with": "; ".join(f"{h} (phi -{v:.2f})" for h, v in g.get("anti", [])),
            "variants": g.get("variants", ""), "x_not_expressed_in_altered": int(g.get("x_lost", -1)),
            "x_baseline_log2_diff": float(g.get("x_base_diff", np.nan)),
            "genes_same_lines": ", ".join(str(c.sym[x]) for x in g.get("genes", [])) if g["kind"] == "null" else "",
            "max_phi_to_real": float(g.get("max_phi", np.nan)),
            "max_phi_to_null_sets": float(g.get("max_phi_null", np.nan)), "alerts": _join(g["alerts"]),
            "inflation": "; ".join(f"{k} {v:.2f}" for k, v in (g.get("lambda") or {}).items()),
            "note": g.get("note", ""), "n_edges_response": int(ne.get("response", 0)),
            "n_edges_baseline": int(ne.get("baseline", 0)),
            "n_edges_sensitivity": int(ne.get("sensitivity", 0))}


def _controls(c, geno, real_counts, pseudo_counts, edges, cuts, fam, level_info, ls_info):
    """controls.json: positive controls (TP53 -> p53 targets and DNA-damage sensitivity; KEAP1 -> NRF2 targets),
    the negative controls (pseudo-groups, counted at the real family's BH cut) next to the real groups' counts, and
    the expected false edges per kind (pseudo rate x real groups; permuted-level controls for the level kinds)."""
    pos = {}
    tp = [g for g in geno if g["gene"] == "TP53"]
    present = [s for s in P53_TARGETS if s in c.col_of]
    for g in tp:
        r = g.get("res", {}).get("response") if g.get("res") else None
        if r is None:
            continue
        order = np.argsort(-np.nan_to_num(r["T"], nan=-np.inf))
        rank = np.empty(order.size, dtype=np.int64)
        rank[order] = np.arange(1, order.size + 1)
        per = []
        for s in present:
            y = c.col_of[s]
            j = np.flatnonzero(r["t"] == y)
            if not j.size:
                continue
            j = j[0]
            e = edges[(edges["kind"] == "genotype_response") & (edges["source"] == "TP53") &
                      (edges["target"] == str(c.sym[y])) & (edges["group"] == g["desc"])]
            per.append({"gene": s, "tested": bool(np.isfinite(r["T"][j])), "T": float(r["T"][j]),
                        "p": float(r["p"][j]), "q": float(r["q"][j]), "rank": int(rank[j]), "D": float(r["D"][j]),
                        "edge": bool(len(e)), "grade": e["grade"].iloc[0] if len(e) else "",
                        "sign": int(e["sign"].iloc[0]) if len(e) else 0,
                        "alert": bool(len(e) and str(e["alerts"].iloc[0] or ""))})
        rec = [x for x in per if x["edge"] and x["sign"] == 1]
        pos[f"TP53 ({g['desc']}) -> p53 targets (response)"] = {
            "expected": "sign +1: the targets respond less where TP53 is lost", "targets_present": len(per),
            "recovered_right_sign": len(rec), "wrong_sign": sum(x["edge"] and x["sign"] == -1 for x in per),
            "median_rank": float(np.median([x["rank"] for x in per])) if per else None,
            "genes_ranked": int(np.isfinite(r["T"]).sum()), "per_gene": per,
            "note": "q is null where it is >= 0.10 (only candidates p < 0.10 enter the family's BH)"}
        dmg = [d for d in range(c.Dn) if set(_split_targets(c.dd["targets"].iloc[d]) if "targets" in c.dd else [])
               & DNA_DAMAGE_TARGETS]
        e = edges[(edges["kind"] == "genotype_sensitivity") & (edges["source"] == "TP53") &
                  (edges["group"] == g["desc"]) & (edges["target_dd"].isin(dmg))]
        pos[f"TP53 ({g['desc']}) -> cells under DNA-damaging drugs (sensitivity)"] = {
            "expected": "sign -1: TP53 activity makes the cells more sensitive", "drugdoses_tested": len(dmg),
            "edges": int(len(e)), "right_sign": int((e["sign"] == -1).sum()),
            "drugdoses": e["target"].tolist()[:30], "drugdoses_alert": (e["alerts"] != "").tolist()[:30]}
    kp = [g for g in geno if g["gene"] == "KEAP1"]
    if not kp:
        pos["KEAP1 -> NRF2 targets (baseline)"] = {"assessable": False,
                                                   "why": f"KEAP1 is not recorded as altered in >= {MIN_SIDE} lines"}
    for g in kp:
        e = edges[(edges["kind"] == "genotype_baseline") & (edges["source"] == "KEAP1") & (edges["group"] == g["desc"])]
        present = [s for s in NRF2_TARGETS if s in c.col_of]
        hit = e[e["target"].isin(present)]
        pos[f"KEAP1 ({g['desc']}) -> NRF2 targets (baseline)"] = {
            "assessable": True, "expected": "sign -1 (loss of KEAP1 raises them)", "targets_present": len(present),
            "recovered_right_sign": int((hit["sign"] == -1).sum()), "wrong_sign": int((hit["sign"] == 1).sum()),
            "genes": hit["target"].tolist(), "genes_alert": (hit["alerts"] != "").tolist()}

    def summary(cnts):
        out = {}
        for kk in GENO_KINDS:
            e = [nr.get(kk, 0) for _, nr, nt, _ in cnts if kk in nt]
            eg = [ng.get(kk, 0) for _, _, nt, ng in cnts if kk in nt]
            t = [nt.get(kk, 0) for _, _, nt, _ in cnts if kk in nt]
            out[kk] = {"groups": len(e), "edges_total": int(sum(e)), "edges_mean_per_group": round(float(
                np.mean(e)), 4) if e else None, "edges_median_per_group": float(np.median(e)) if e else None,
                "groups_with_any_edge": int(sum(x > 0 for x in e)),
                "share_groups_with_any_edge": round(float(np.mean([x > 0 for x in e])), 4) if e else None,
                "edges_per_tested": float(sum(e) / max(1, sum(t))) if t else None,
                "within_group_edges_mean_per_group": round(float(np.mean(eg)), 4) if eg else None,
                "within_group_share_groups_with_any_edge": round(float(np.mean([x > 0 for x in eg])), 4) if eg
                else None}
        return out
    neg = {"how": f"{len(pseudo_counts)} random pseudo-genotype groups with sizes spread over the real groups' size "
                  f"distribution (lines drawn at random, |phi| < {PSEUDO_PHI} to every recorded group and < "
                  f"{PSEUDO_PHI_NULL} to every expression-null line set with >= {FULL_SIDE} lines each side), tested "
                  "exactly as the real groups; a pseudo test counts as an edge when its p is at or below the real "
                  "family's BH cut (the p at which a real test reaches q < 0.10) and it passes BH within its own "
                  "group: what a group without any real effect, added to the table, would contribute. A random "
                  "group can still overlap an effect of something unrecorded; the estimate is then an upper bound",
           "p_cut": {kk: cuts[kk] for kk in GENO_KINDS}, "family_tests": {kk: fam[kk][0] for kk in GENO_KINDS},
           "pseudo": summary(pseudo_counts), "real": summary(real_counts),
           "per_pseudo_group": [{"group": g["desc"], "max_phi_to_real": g.get("max_phi"),
                                 "stratified": bool(g["stratified"]), **{f"edges_{k}": v for k, v in nr.items()},
                                 **{f"within_group_edges_{k}": v for k, v in ng.items()}}
                                for g, nr, _, ng in pseudo_counts]}
    neg["summary"] = {}
    exp = {}
    for kk in GENO_KINDS:
        ps, rl = neg["pseudo"][kk], neg["real"][kk]
        pm, rm = ps["edges_mean_per_group"], rl["edges_mean_per_group"]
        n_real = rl["groups"]
        e_false = None if pm is None else round(pm * n_real, 2)
        n_ps = ps["groups"]
        tot = ps["edges_total"]
        tot_g = int(round((ps["within_group_edges_mean_per_group"] or 0.0) * n_ps)) if n_ps else 0
        up = None if pm is None or not n_ps else round(_poisson_upper(tot) / n_ps * n_real, 2)
        up_g = None if pm is None or not n_ps else round(_poisson_upper(max(0, tot_g - tot)) / n_ps * n_real, 2)
        sel = (edges["kind"] == f"genotype_{kk}") if len(edges) else np.zeros(0, dtype=bool)
        n_edges = int(sel.sum()) if len(edges) else 0
        n_tab = int((sel & (edges["q"] < Q_SIG)).sum()) if len(edges) else 0
        pg, rg = ps["within_group_edges_mean_per_group"], rl["within_group_edges_mean_per_group"]
        e_false_g = None if pg is None else round(pg * n_real, 2)
        neg["summary"][kk] = {"pseudo_edges_mean_per_group": pm, "real_edges_mean_per_group": rm,
                              "pseudo_edges_per_tested": ps["edges_per_tested"],
                              "pseudo_share_groups_with_any_edge": ps["share_groups_with_any_edge"],
                              "pseudo_within_group_edges_mean_per_group": pg,
                              "real_within_group_edges_mean_per_group": rg,
                              "real_groups": n_real, "expected_false_edges": e_false,
                              "expected_false_edges_within_group": e_false_g, "edges": n_edges,
                              "edges_table_wide": n_tab,
                              "pseudo_at_or_above_real": bool(pm is not None and rm is not None and pm >= rm
                                                              and pm > 0)}
        exp[f"genotype_{kk}"] = {"edges": n_tab, "expected_false": e_false, "expected_false_upper": up,
                                 "how": "edges significant over the table (q < 0.10, grades A/B): pseudo-group edges "
                                        f"per group at the real BH cut x the real groups ({tot} edges in {n_ps} "
                                        "pseudo-groups)"}
        exp[f"genotype_{kk}_within_group_only"] = {
            "edges": n_edges - n_tab, "expected_false": None if e_false_g is None else round(max(
                0.0, e_false_g - (e_false or 0.0)), 2), "expected_false_upper": up_g,
            "how": "edges significant only within their group (grade C): pseudo-group within-group edges per group "
                   f"x the real groups, minus the table-wide ones ({max(0, tot_g - tot)} edges in {n_ps} "
                   "pseudo-groups)"}
    for kk, inf in (("level", level_info), ("level_sensitivity", ls_info)):
        cn = inf.get("control_permuted_levels_edges")
        exp[kk] = {"edges": int(inf.get("edges", 0)), "expected_false": cn,
                   "expected_false_upper": None if cn is None else round(_poisson_upper(cn), 2),
                   "how": "the same tests with every gene's level permuted over its lines (one permutation), at the "
                          "real BH cut"}
    cg = ls_info.get("control_permuted_levels_within_drugdose_only")
    exp["level_sensitivity_within_drugdose_only"] = {
        "edges": int(ls_info.get("edges_within_drugdose_only", 0)), "expected_false": cg,
        "expected_false_upper": None if cg is None else round(_poisson_upper(cg), 2),
        "how": "edges significant only among the genes tested for their drug-dose: the same count with the levels "
               "permuted (one permutation)"}
    return {"positive": pos, "negative": neg, "level_controls": {"level": level_info,
                                                                 "level_sensitivity": ls_info},
            "expected_false_edges": exp, "expected_false_how": EXPECTED_FALSE_HOW}


# ----------------------------------------------------------------------------- README
EDGE_DOCS = {
    "source": "the upstream gene: the genotype's gene, the gene that is absent, whose level varies, or that the "
              "compounds target",
    "source_col": "its gene col (genes.csv; -1 = a drug target that is not a measured gene)",
    "target": "the gene that changes, or 'cells under DRUG DOSE' (the cells' growth: sensitivity kinds)",
    "target_col": "the target gene's col (-1 for cells)", "target_dd": "the drug-dose row for a cells target (-1)",
    "target_type": "gene or cells",
    "kind": "the evidence: genotype_response / genotype_baseline / genotype_sensitivity (recorded mutation), "
            "null_response / null_baseline / null_sensitivity (the gene is not expressed in some lines), "
            "drug_target (compounds that target it), level / level_sensitivity (its natural level)",
    "grade": "A (recorded genotype, >= 5 lines each side, q < 0.05, compared within organs, no co-occurrence or "
             "anti-occurrence alert, and for a response not resting on the global-sensitivity correction), B, C (a "
             "glimpse; also a tissue-confounded genotype edge) - see 'How to read a grade'",
    "sign": "+1: the source's activity raises the target's level or the cell numbers, or strengthens the target's "
            "drug response in its own direction (for a target that falls under the drugs: a deeper fall); -1: lowers "
            "it / weakens it; 0: not inferred (mechanism unknown) - see 'How to read a sign'",
    "reading": "the edge in words", "group": "the comparison ('TP53 loss of function (10 lines) vs not recorded (8)')",
    "mechanism": "loss of function / gain of function / altered (any record) / not expressed / level / inhibitor ...",
    "n_altered": "lines on the altered (or lacking) side with a value for the target (-1: not applicable)",
    "n_intact": "lines on the other side with a value", "n_lines": "lines in a level correlation",
    "contrast": "the tested effect: response kinds mean corrected response (z units) intact - altered; baseline "
                "log2 level intact - altered; sensitivity log2 relative cell number intact - altered; level r; "
                "drug_target the share of the compounds that move the target",
    "D_raw": "response kinds: the same contrast without the global-sensitivity correction",
    "retained_fraction": "response kinds: the altered lines' mean raw response / the intact lines' (1 = unchanged, "
                         "0 = lost, < 0 = reversed)",
    "raw_share": "response kinds: the evidence in the edge's direction without the global-sensitivity correction / "
                 "with it (sum of squared per-drug-dose scores); below 0.25 the edge rests on the correction "
                 "(alerted, not grade A)",
    "rise_share": "response kinds and level: the share of the target's response from drug-doses where it rises (the "
                  "rest: where it falls) - of the evidence carrying the difference (genotype / null response), or "
                  "of its own response over its significant drug-doses, weighted by |pooled z| (level). Between "
                  "0.25 and 0.75 it is alerted: the sign then says how strongly it responds, not whether the source "
                  "induces or represses it",
    "baseline_log2_diff": "the target's baseline log2 level intact - altered (for response edges: context)",
    "r": "level kinds: correlation of the lineage-adjusted level with the response / cell number",
    "r_reverse": "level: the same with the roles of the two genes swapped",
    "direction_clear": "level: |r| > |r_reverse| and p_direction < 0.05; False when the reverse is not clearly "
                       "weaker or could not be tested",
    "p_direction": "level: one-sided p that |r| - |r_reverse| is no larger than two equally strong directions give "
                   "once the forward has passed the same cut (the edge was selected because |r| is large, which "
                   "inflates it; the largest p over the common strength); 1 when the reverse is at least as strong",
    "n_compounds": "drug_target: compounds of the class",
    "n_supporting": "drug_target: of them, those that move the target that way",
    "background_rate": "drug_target: share of all compounds that move the target that way",
    "compounds": "drug_target: every compound of the class, '; '-joined; one molecule counts once (salt forms, "
                 "letter case and salt words merged; its names ' / '-joined) ('' for other kinds)",
    "compounds_supporting": "drug_target: those of them that move the target that way, '; '-joined",
    "drug_effect": "drug_target: what the compounds do to the target's level, 'raises' or 'lowers' (sign is relative "
                   "to the source's activity: an inhibitor that raises the target gives sign -1)",
    "T": "the tested statistic: permutation-standardised (and divided by the group's inflation) for the group "
         "kinds; t = r sqrt(dof / (1 - r^2)) for the level kinds; empty for drug_target",
    "p": "group kinds: from the pooled permutation null with a fitted generalized-Pareto tail (no floor), never "
         "below the target's own permutation p where its own shuffles disagree with the pool, nor below 1 / its "
         "number of label arrangements; two-sided, except the response kinds (one-sided upper tail of the omnibus "
         "S). Level kinds: two-sided, from the t distribution (calibrated by a Freedman-Lane null). drug_target: "
         "one-sided hypergeometric",
    "q": "BH q over the kind's whole family: every genotype group of the kind; every expression-null test of the "
         "kind (within-organ and across-organ comparisons as two families); every level pair; every (gene, "
         "drug-dose) level_sensitivity test; every drug_target test",
    "q_group": "genotype kinds: BH q within the edge's own group (its tests of the kind); level_sensitivity: within "
               "the drug-dose (the genes tested for it). These edges are written when q_group < 0.10 (significant in "
               "their own family); grade A / B also need q < 0.10 over the whole table; with q >= 0.10 the edge is "
               "grade C (a lead) and its alert says so, with the expected number of such false edges",
    "alerts": "the reasons to doubt this arrow (they carry the warning sign), in plain words: '' or '⚠ ' + the "
              "reasons, '; '-joined. Every reason of the edge is in exactly one of alerts, notes, caveats and "
              "support (see 'Alerts, notes, caveats and support')",
    "top_drugdoses": "response: the drug-doses carrying the difference, each as 'fold in the altered lines vs fold in "
                     "the other lines (z diff: corrected contrast)', the strongest first within the target's main "
                     "direction (rise_share), then the other direction; when mixed, the strongest of each; "
                     "drug_target: each supporting compound's "
                     "strongest drug-dose",
    "art_share": "response kinds (genotype_response, null_response): the share of the evidence (sum of |contrast| over "
                 "the target's 10 drug-doses) carried by drug-doses with an artifact flag (toxic, transcription drop, "
                 "cell-cycle shift, ...); float32; empty for the other kinds",
    "drugdoses_all": "every drug-dose behind the edge, each with its flags ('[artifact flags: ...]' or '[flags: "
                     "...]'): response kinds - all 10 of the target's drug-doses, as in top_drugdoses (fold in the "
                     "altered lines vs the other lines, z diff), strongest in the edge's direction first; drug_target "
                     "- every significant drug-dose of each supporting compound (pooled fold and z); sensitivity kinds "
                     "- the drug-dose of the cells; level - the target's 10 drug-doses (pooled fold and z); '' for the "
                     "baseline kinds. top_drugdoses keeps the first few",
    "n_alerts": "number of reasons in alerts (int16; an edge with 0 carries no warning sign)",
    "notes": "reasons kept below their thresholds (see 'Alerts, notes, caveats and support'), '; '-joined, no sign: "
             "read them, they are context rather than doubt about this arrow",
    "caveats": "the reasons every edge of its kind carries (drug_target: drugs can act on other proteins too; level: "
               "tissue can mimic it, and the precision caveat; level_sensitivity: tissue can mimic it), '; '-joined",
    "support": "reasons that support the edge (drug_target: the supporting compounds; expression-null: a recorded loss "
               "of the gene in the same lines), '; '-joined",
    "alerts_all": "every reason of the edge (alerts, notes, caveats and support together) in the order the stage wrote "
                  "them, '; '-joined, no sign",
    "n_notes": "number of notes (int16)", "n_caveats": "number of caveats (int16)",
    "n_support": "number of support reasons (int16)",
}
GROUP_DOCS = {
    "group_id": "kind:gene:mechanism", "kind": "genotype, null (expression-null line set) or pseudo (control)",
    "gene": "the gene", "gene_col": "its col (-1 = not measured)", "mechanism": "as in edges",
    "description": "the comparison", "n_altered": "lines altered / lacking the gene", "n_intact": "lines compared",
    "altered_lines": "their names", "intact_lines": "their names", "organs_altered": "organs (count)",
    "organs_intact": "organs (count)", "stratified": "permuted within organs",
    "n_arrangements": "distinct arrangements of the labels the permutations draw from (within organs when "
                      "stratified)",
    "n_altered_shared_organs": "altered lines in organs that also hold lines of the other side (within organs only "
                               "those carry the comparison; grade A needs >= 5)",
    "n_intact_shared_organs": "the same for the other side",
    "organ_enrichment_p": "compared across organs: Monte Carlo p that the two sides' organs differ (chi-square over "
                          "label permutations; empty when compared within organs)",
    "tissue_confounded": "compared across organs and the sides' organs differ (organ_enrichment_p < 0.05)",
    "cooccurs_with": "other genes' altered sets overlapping this one (Jaccard >= 0.5; blocks grade A)",
    "anti_occurs_with": "genes whose altered lines sit on the other side of the comparison (phi <= -0.5): a "
                        "confounder with the opposite sign (an alert; blocks grade A)",
    "variants": "variant types of the altered lines' records", "x_not_expressed_in_altered":
        "altered lines where the gene itself is not expressed (-1: not measured)",
    "x_baseline_log2_diff": "the gene's own level, intact - altered (log2)",
    "genes_same_lines": "null: every gene absent from exactly these lines", "max_phi_to_real":
        "pseudo: largest |phi| to a recorded group (drawn below 0.3)",
    "max_phi_to_null_sets": "pseudo: largest |phi| to an expression-null line set with >= 5 lines each side (drawn "
                            "below 0.5)",
    "alerts": "the group's reasons to doubt its comparison (warning sign; '' or '⚠ ' + '; '-joined); every edge of "
              "the group carries them too",
    "notes": "the group's reasons kept below their thresholds (within organs on most lines; the gene itself not "
             "expressed in a few altered lines), '; '-joined",
    "alerts_all": "every reason of the group, alerts and notes, in the original order, '; '-joined",
    "inflation": "per test, the genomic-control factor its statistics were divided by (>= 1; how much wider than the "
                 "permutation null the bulk of all targets' statistics spread for this grouping)",
    "note": "null: how its partners' baseline and response were compared (across organs: a separate BH family), or "
            "why they were not tested (lines concentrated in organs)",
    "n_edges_response": "edges written (pseudo: tests at or below the real family's BH cut, counted, not written)",
    "n_edges_baseline": "same", "n_edges_sensitivity": "same",
}


def tier_rules_lines():
    """The README section on the four tiers of reasons and the thresholds of the graded ones (from the code
    constants)."""
    return [
        "## Alerts, notes, caveats and support", "",
        "Every reason an edge carries is kept and written out in full, in exactly one of four columns. `alerts_all` "
        "holds all of them in the original order. Which reasons go where is fixed by code (direction.py: "
        "reason_tier); nothing is removed.", "",
        "- **alerts** (⚠): a doubt about this arrow, or a graded reason at or past its threshold. An arrow with no "
        "alert carries no warning sign.",
        "- **notes**: a graded reason below its threshold, and context. Shown muted, in full: read them.",
        "- **caveats**: the same text on every arrow of a kind (drug_target: drugs can act on other proteins too; "
        "level: tissue and other differences between lines can mimic it, and a stronger correlation one way can "
        "reflect how precisely each level is measured; level_sensitivity: tissue can mimic it). Stated once above "
        "each list.",
        "- **support**: evidence for the arrow ('consistent across N compounds'; for a gene missing from some lines: "
        "'the lines lacking X carry a recorded loss of X: genotype evidence too').",
        "", "The graded reasons, and when each is an alert rather than a note:",
        f"- 'Y measured in a of the A and i of the I lines': an alert when a or i is below {FULL_SIDE}, or a is below "
        f"{NOTE_MEASURED_FRAC:g} x A, or i is below {NOTE_MEASURED_FRAC:g} x I (NOTE_MEASURED_FRAC); else a note.",
        f"- 'supporting drug-doses with artifact flags (N% of the evidence)': an alert when the flagged drug-doses "
        f"carry at least {NOTE_ART_SHARE:.0%} of the evidence (art_share, NOTE_ART_SHARE), or the strongest "
        "supporting drug-dose (the first of top_drugdoses) is one of them ('the strongest among them'); else a note. "
        "It lists every flagged drug-dose among the target's 10. For drug_target: the share of the supporting "
        "compounds whose strongest drug-dose is flagged, or the strongest of all is.",
        f"- 'compared within organs: a of the A ... and i of the I others share an organ': an alert when a is below "
        f"{NOTE_WITHIN_ORGAN_FRAC:g} x A or i is below {NOTE_WITHIN_ORGAN_FRAC:g} x I (NOTE_WITHIN_ORGAN_FRAC); else a "
        "note (a within-organ comparison costs lines, not validity).",
        f"- 'other genes are absent from most of these lines too ... (and N more line sets)': an alert when "
        f"{NOTE_COABSENT_SETS} or fewer line sets overlap in all (NOTE_COABSENT_SETS: a candidate co-deletion); else "
        "a note (many genes share the pattern: a tissue programme rather than one deletion).",
        f"- 'X itself is not expressed in k of the n altered lines': an alert when k is above "
        f"{NOTE_NOT_EXPRESSED_FRAC:g} x n (NOTE_NOT_EXPRESSED_FRAC); else a note.",
        "- Every other reason is an alert, among them: tissue-confounded; co-occurs or another gene's alterations on "
        "the other side; compared across organs; few lines; organs not known; significant within its group or "
        "drug-dose only (a lead); direction unclear; both ways; rises at some drug-doses and falls at others; lower "
        "baseline; the correction alerts; its own permutation p; 'any of them could be the cause'; maybe low rather "
        "than absent; cell counts less trustworthy."]


def _tier_run_line(info):
    """README 'This run': how many edges carry an alert, a note, a caveat, support."""
    t = info.get("reason_tiers") or {}
    if not t:
        return "- reasons in tiers: not recorded"
    return (f"- reasons: {t['edges_with_alert']:,} of {info['edges']:,} edges carry an alert (⚠), "
            f"{t['edges_with_note']:,} a note, {t['edges_with_caveat']:,} their kind's caveat and "
            f"{t['edges_with_support']:,} support; without an alert, by kind: " + ", ".join(
                f"{k} {v:,}" for k, v in t["edges_without_alert_by_kind"].items() if info["edges_by_kind"].get(k)))


def readme(edges, groups, info):
    und = [x for x in edges.columns if x not in EDGE_DOCS] + [x for x in groups.columns if x not in GROUP_DOCS]
    cnt = info["edges_by_kind_and_grade"]
    fp = info["false_positive_rate"]
    ef = info["expected_false_edges"]
    gt = info["groups_tested"]
    adj = info["global_sensitivity_correction"]
    lines = [
        "# direction/ - probable direction between genes", "",
        "Directed edges SOURCE -> TARGET, each from a statistical test (p, BH q < 0.10), with an evidence grade and "
        "its reasons for doubt. Nothing that passes is dropped because of doubt: it keeps its place with its alerts "
        "(the `alerts` text starts with ⚠) and a lower grade. A pair without such a test result is not an edge. "
        "Every reason is kept, in one of four tiers (next section). Method: tahoemap/direction.py (module "
        "docstring); a user-facing explanation: docs/direction.md.", "",
        *tier_rules_lines(), "",
        "## What direction means here - and what it does not", "",
        "- The source is what the test conditions on: a recorded mutation of the source gene (fixed before the "
        "experiment, so not a consequence of the target), its absence from some lines, its natural level, or "
        "compounds that target its protein. The target is what differs with it: its level, its drug response, or the "
        "cells' growth under a drug.",
        "- It is not proof of direct regulation: A -> B -> C looks like A -> C; another alteration carried by the "
        "same lines can be the cause (see the co-occurrence alerts); 'not recorded' is not proof of wild type.",
        "- One time point (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.",
        "- Drugs act on proteins, not on mRNA; a compound can act on other proteins than its listed target.",
        "- Level edges come from natural differences between lines; tissue and other differences can mimic them, "
        "and a stronger correlation one way can reflect how precisely each gene's level is measured.", "",
        "## How to read a grade", "",
        "- **A**: a recorded genotype, >= 5 lines on each side (within organs: lines sharing an organ with the other "
        "side), q < 0.05, compared within organs, no co-occurrence alert (another gene's altered lines on the same "
        "side, or on the other side); for a response, not resting on the global-sensitivity correction and not "
        "mostly from drug-doses without any correction.",
        "- **B**: other genotype edges (with alerts, or 3-4 lines) that are not tissue-confounded; expression-null "
        "with >= 5 lines lacking the gene (not tissue-confounded); drug_target.",
        "- **C**: a glimpse: level and level_sensitivity; expression-null with 3-4 lines, tissue-confounded, co-"
        "absent, or resting on the correction; a genotype edge that is tissue-confounded or significant only within "
        "its own group (q_group < 0.10, table-wide q >= 0.10).", "",
        "## How to read a sign", "",
        "- The sign is the effect of the SOURCE's activity. For a level or the cells: +1 raises it, -1 lowers it.",
        "- For a drug response (genotype_response, null_response, level): +1 strengthens the target's response, -1 "
        "weakens it, in the target's own direction at each drug-dose - where the target falls under the drugs, "
        "'strengthens' means it falls further (the source deepens the fall). Read which from all of top_drugdoses "
        "and from rise_share; a target that rises at some drug-doses and falls at others is alerted, and the sign "
        "then says how strongly it responds, not whether the source induces or represses it.", "",
        "## This run", "",
        f"- {info['edges']:,} edges; groups tested: {gt['genotype']} genotype groups, {gt['pseudo_controls']} "
        f"pseudo-groups, {gt['expression_null_line_sets']:,} expression-null line sets "
        f"({gt['expression_null_genes']:,} genes; {gt['expression_null_line_sets_across_organs']:,} sets / "
        f"{gt['expression_null_genes_across_organs']:,} genes could not be compared within organs)",
        (f"- ⚠ expression-null: for {gt['expression_null_genes_not_tested_partners']:,} genes "
         f"({gt['expression_null_line_sets_not_tested_partners']:,} line sets) absent from lines concentrated in "
         "organs, their partners' baseline and response were not tested (absence and tissue cannot be told apart "
         "there; groups.parquet note says so for each); their effect on cell numbers was. The other sets without a "
         "within-organ comparison were compared across organs as a separate BH family"
         if gt['expression_null_genes_not_tested_partners'] else
         "- expression-null: every gene with related partners had their baseline and response tested (sets without a "
         "within-organ comparison across organs, as a separate BH family; sets whose lines are concentrated in organs "
         "would have been left out, and groups.parquet's note would say so)"),
        "- by kind and grade: " + "; ".join(f"{k} " + "/".join(f"{g}{v[g]}" for g in "ABC") for k, v in cnt.items()),
        _tier_run_line(info),
        f"- global-sensitivity correction of the (gene, drug-dose) responses: {adj['drug_specific']:,} against the "
        f"drug-dose's other responsive genes, {adj['line_wide']:,} line-wide only, {adj['none']:,} without; the "
        f"lines' overall responsiveness was {'used' if adj['line_wide_check']['used'] else 'not used'} "
        f"({adj['line_wide_check']['why']})",
        "- expected false edges (negative controls; in brackets the 95% upper bound): " + "; ".join(
            f"{k} {v['expected_false']} (up to {v.get('expected_false_upper')}) of {v['edges']}"
            for k, v in ef.items()) + ". " + EXPECTED_FALSE_HOW,
        "- pseudo-groups, edges per group vs real groups: " + "; ".join(
            f"{k} {v['pseudo_edges_mean_per_group']} vs {v['real_edges_mean_per_group']}" for k, v in fp.items())]
    for k, v in fp.items():
        if v.get("pseudo_at_or_above_real"):
            lines.append(f"- ⚠ genotype_{k}: random pseudo-groups give as many edges per group as the real groups "
                         f"({v['pseudo_edges_mean_per_group']} vs {v['real_edges_mean_per_group']}): most of these "
                         "edges may be false; read them as leads")
    for k, v in ef.items():
        if v["expected_false"] is not None and v["edges"] and v["expected_false"] >= 0.5 * v["edges"]:
            lines.append(f"- ⚠ {k}: the controls expect {v['expected_false']} false edges among the {v['edges']} "
                         "written")
    lines += ["", "## edges.parquet", ""]
    lines += [f"- `{k}`: {v}" for k, v in EDGE_DOCS.items()]
    lines += ["", "## groups.parquet", ""]
    lines += [f"- `{k}`: {v}" for k, v in GROUP_DOCS.items()]
    lines += ["", "## controls.json, info.json", "",
              "- controls.json: positive controls (TP53 -> p53 targets with sign and rank; TP53 -> cells under DNA-"
              "damaging drugs; KEAP1 -> NRF2 targets when KEAP1 is recorded in enough lines); negative controls "
              "(pseudo-groups counted at the real family's BH cut: the false edges a group without any effect "
              "adds); permuted-level controls for the level kinds; the expected false edges per kind.",
              "- info.json: counts per kind and grade, groups and tests, the BH cuts, the fitted null tails, the "
              "level kinds' calibration, settings, peak memory, minutes.", ""]
    return "\n".join(lines), und


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tahoemap.direction",
                                 description="probable direction between genes (writes OUT/direction/)")
    ap.add_argument("--out", required=True, help="the tahoemap output folder")
    ap.add_argument("--data", default=None, help="the Tahoe-100M folder (for the cell-line metadata)")
    ap.add_argument("--chunk", type=int, default=0, help="genes per tensor chunk (default: from --mem-gb)")
    ap.add_argument("--mem-gb", type=float, default=1.0, help="memory for one tensor chunk (GB)")
    ap.add_argument("--perms", type=int, default=PERMS, help="label permutations per genotype group")
    ap.add_argument("--k", type=int, default=K_DD, help="drug-doses per gene")
    ap.add_argument("--pseudo", type=int, default=N_PSEUDO, help="negative-control pseudo-groups")
    a = ap.parse_args(argv)
    run(a.out, data=a.data, chunk=a.chunk or None, mem_gb=a.mem_gb, perms=a.perms, k=a.k, pseudo=a.pseudo)


if __name__ == "__main__":
    main()
