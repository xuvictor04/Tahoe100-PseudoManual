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
4. drug_target (no mutation; grade B, C for trap classes). A target X annotated for >= 2 distinct compounds (one
   molecule counts once: mechanisms.molecule_key - salt forms, letter case and trailing salt words merged, 'Ixazomib' /
   'Ixazomib citrate', 'crizotinib' / 'Crizotinib (hydrochloride)'; its names ' / '-joined) of one class. VERSION 5:
   memberships per (compound, target) from Tahoe (targets, moa_broad: inhibitor/antagonist, activator/agonist,
   unclear) and ChEMBL (drug_mechanisms, target types CHEMBL_MEMBER_TYPES, action types through
   mechanisms.action_direction): one source lists the target - its action; Tahoe 'unclear' and ChEMBL gives one -
   ChEMBL's; different actions - 'unclear', alerted; a member whose two annotations list different targets alerts
   every edge of the class (compounds_source). The class of (compound, target) is a 'trap' class when
   mechanisms.trap_class says so (TOP1 / TOP2 poisons, PARP trappers, microtubule stabilisers: the drugs trap the
   target on DNA or freeze microtubules, so the target gene follows the damage or the arrest, not less of the target:
   sign 0, grade C), 'inhibitor (microtubule destabiliser)' for a tubulin destabiliser, else the action. The test
   (top-j, VERSION 5): per compound its strongest pooled z that way over its drug-doses (E), M = how many compounds
   move Y at least as strongly; for j = 2..k (k: the class's compounds significant that way, pooled q < 0.1 and
   >= 1.2x at any dose), m_j = the j-th smallest M among them and p_j = P(>= j of the N class compounds among the
   m_j strongest of the screen) (hypergeometric); p = min(1, (N - 1) min_j p_j) (topj_p). A test counts where >= 2
   compounds of the screen move Y that way (elsewhere no class can reach k >= 2; DT_BH_ALL); BH over all of them.
   Sign relative to X's activity: inhibitors raising Y -> -1 (X activity lowers Y), activators raising Y -> +1.
   Sign of the response kinds (genotype_response, null_response, level): how STRONGLY Y responds in its own pooled
   direction (r = per-line z x the sign of the pooled z), so +1 reads 'strengthens Y's drug response' - for a Y that
   falls under the drugs, a deeper fall - and -1 'weakens'.
   Columns compounds (the class's compounds, '; '-joined), compounds_supporting (those moving Y that way) and
   drug_effect ('raises' / 'lowers': what the compounds do to Y) record it for the look-ups (direction_view.py).
5. The sensitivity kinds above are the gene -> phenotype edges: the target is 'cells under DRUG DOSE' (target_dd).
6. genotype_selectivity, null_selectivity (VERSION 5): the same groups and test as sensitivity on how strongly each
   line responds to a drug-dose (tables/drug_line_response rel_log2: genes beyond the per-line cut against the line's
   typical drug-dose), for the drug-doses with >= 1 selective line; target 'response to DRUG DOSE' (target_type
   'response'). Per compound the other doses with q_group < 0.10 are support ('also at'); none: 'one dose only' (an
   alert, no grade A). direction/selectivity.parquet: per drug-dose its selective lines, organs and groups.

VERSION 5 groups and rules. Allele groups (D12): exact changes ('KRAS p.G12C'), codons, cited hotspots (HOTSPOTS) and
amplifications recorded in >= MIN_SIDE lines, against every other recorded line; a group whose line set equals the
gene's group is not added (its words gain the composition). Group words (D15) give the altered lines' composition, and
a loss-of-function group where >= 1/3 of the lines carry a missense change has a note. Heavily mutated lines (D7: >=
HYPERMUT_MIN_GENES recorded driver genes) concentrated on the altered side: an alert, no grade A. Same locus (D9):
source and target within SAME_LOCUS_BP (distance_bp): sign 0, grade C; a genotype group's target absent from most
altered lines: grade C when it lies within CODELETION_BP of the source on one chromosome or without coordinates
(VERSION 6; version 5: whatever the distance), else an alert that names lineage or the loss of the source (and a known
target of the source: P53_TARGETS, NRF2_TARGETS). VERSION 6 also blocks a genotype baseline arrow from grade A when the
target is not expressed in >= BASE_ABSENT_A of either side's lines, and writes a note on every arrow that a changed
rule reads differently (_changed_note, _blocked_note: the 'notes' tier). Expression programme (D10): a natural
knockout whose lines overlap > NOTE_COABSENT_SETS other line sets: sign 0, grade C. Natural knockouts and drug
targets are worded 'may' (D16). Translation inhibitors' share of a response's evidence (D17: ti_share). The group's
expected false share from the pseudo-groups (D6: false_share; >= FALSE_SHARE_ALERT blocks A) and the family caveat;
the natural knockouts' random controls (D11: nonspecific_share).
test_id / n_same_test (D2): edges that are one test. gene_tests.parquet (D14): each gene's tests per kind and role.

Organs: from lines.csv, else the cell-line metadata. A group is compared within organs when the labels have >= 100
arrangements there; then the organ composition is the same in every permutation and no tissue alert is raised, but
only the lines in organs holding both sides carry the comparison (alerted when not all; grade A needs >= 5 on each
side). Compared across organs, the group is tissue-confounded when the sides' organs differ more than chance
(Monte Carlo p < 0.05 of the chi-square statistic of the organs x sides table over 2,000 label permutations); the
alert names the most over-represented organ with its counts. Unknown organs: no strata, no tissue alert, an alert.

Grades. A: a recorded genotype with >= 5 lines on each side (measured lines, for a response; within organs: those
sharing an organ with the other side), q < 0.05 (and q_group < 0.10), compared within organs, no co-occurrence alert
(another gene's altered lines overlapping the altered side, or sitting on the other side: anti-occurrence), no heavily
mutated lines concentrated on the altered side, the group's expected false share below FALSE_SHARE_ALERT, and for a
response not resting on the correction nor mostly uncorrected, the mean over all its drug-doses going its way with and
without the correction, less than BOTH_WAYS_A of the evidence the other way, not a floor (mostly falls and >= 2x
lower at baseline in the altered lines), measured in >= MEASURED_A of each side's lines; for a selectivity edge seen
at >= 2 doses (_grade_genotype). B: any other genotype edge with q < 0.10 (alerts, or
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

Controls (controls.json). Positive: TP53 groups -> p53 target genes (counted when sign +1, evidence from rises and the
mean contrast agreeing; the others with why_not), TP53 -> cells under DNA-damaging drugs (a Tahoe target or a poison /
DNA class), TP53 -> response strength to them, KRAS p.G12C -> response to Adagrasib, KEAP1 -> NRF2 target genes
(baseline) when KEAP1 is recorded in enough lines. The natural knockouts (null_controls): random non-partner genes per
overlap bin (baseline, response) and random line sets (cells, response strength).
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

Outputs in OUT/direction/: edges.parquet, groups.parquet, selectivity.parquet, gene_tests.parquet, controls.json,
info.json, README.md (every column).
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

from . import mechanisms as MX
from . import tlib as T
from .common import folder, has_artifact, log, replace_file, stable_seed, stamp_stage, write_json, write_parquet
from .mechanisms import SALT_WORDS, molecule_key  # noqa: F401  (SALT_WORDS: one list, read by direction too)
from .tensor import AMB_FRAC

VERSION = 6                    # 6: a baseline arrow's grade A needs the target expressed in most lines of each side
#                                (BASE_ABSENT_A); a co-absent target reads 'a shared deletion' (grade C) only near the
#                                source on one chromosome; every arrow a changed rule reads differently says so (a note)
#                                5: poison classes, top-j drug_target test, ChEMBL classes, stricter grade A, group
#                                false shares, heavily mutated lines, same-locus and programme rules, null controls,
#                                allele groups, selectivity kinds, gene_tests, plain verbs
#                                (4: alert texts name every shared target and every co-occurring, opposite or co-absent
#                                gene: no list is cut)

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
# ---- VERSION 5 rules (docs/direction.md says for each the old rule, the new rule and the evidence)
BOTH_WAYS_A = 0.5              # response: grade A needs < this share of the evidence going the other way
MEASURED_A = 0.5               # response: grade A needs the target measured in >= this share of each side's lines
FALSE_SHARE_ALERT = 0.2        # a group's expected false share (pseudo-groups) at or above this: an alert, blocks A
HYPERMUT_MIN_GENES = 15        # a line recording alterations in >= this many driver genes is 'heavily mutated'
SAME_LOCUS_BP = 1_000_000      # source and target within this distance on one chromosome: 'same locus' (sign 0, C)
# ---- VERSION 6 rules (docs/direction.md, 'Changed in direction version 6': the old rule, the new rule and why)
BASE_ABSENT_A = 0.25           # baseline (genotype): grade A needs the target expressed in more than (1 - this) of
#                                each side's lines. Version 5 graded TP53 -> GRIN2C (not expressed in 13 of 33 TP53-
#                                altered and 1 of 17 other lines) and TP53 -> ACTA2 (11 of 33 and 0 of 17) A: a level
#                                difference made by lines that lack the gene can be lineage, not regulation
CODELETION_BP = SAME_LOCUS_BP  # a genotype target absent from most altered lines (D9): 'a shared deletion can explain
#                                it' (grade C) only when it lies within this distance of the source on one chromosome.
#                                Version 5 said so whatever the distance: TP53 (17p13) -> EDA2R (Xq12, a p53 target)
CHANGED = "rule changed in direction version {v}"   # a note on every arrow that a changed rule reads differently
NULL_CONTROL_SETS = 200        # null kinds' random-gene control: real null line sets drawn (evenly over NULL_BINS)
NULL_CONTROL_GENES = 300       # ... random non-partner genes per set
N_PSEUDO_NULL = 60             # null_sensitivity / null_selectivity: random pseudo line sets
NULL_BINS = (10, 50, 200, 600)  # overlap bins of a null line set: other sets overlapping it (null_co_n) <= 10, 11-50,
#                                51-200, 201-600, > 600
NOTE_TI_SHARE = 0.5            # response: translation-inhibitor drug-doses carry >= this share: an alert, else a note
# hotspots of the allele groups (D12), cited code constants: (gene) -> (codons or changes, citation)
HOTSPOTS = {
    "PIK3CA": {"changes": ("E542K", "E545K", "H1047R", "H1047L"), "missense_codons": (),
               "source": "Samuels Y et al. 2004, Science 304:554 (doi:10.1126/science.1096502, PMID 15016963)"},
    "TP53": {"changes": (), "missense_codons": ("R175", "G245", "R248", "R249", "R273", "R282"),
             "source": "Baugh EH et al. 2018, Cell Death Differ 25:154 (doi:10.1038/cdd.2017.180, PMID 29099487)"}}
# the variant types read as truncating (with splice and deletion) for the group words (D15); 'Missense' apart
TRUNCATING = ("Frameshift", "Stopgain", "Splice_site", "Deletion", "Synonymous_splicing", "Nonsense")
# trap classes (mechanisms.trap_class): their name in the readings and what follows the drug (D1)
TRAP_NAMES = {"TOP1_POISON": ("TOP1 poison", "TOP1 poisons"), "TOP2_POISON": ("TOP2 poison", "TOP2 poisons"),
              "PARP_TRAPPER": ("PARP trapper", "PARP trappers"),
              "TUBULIN_STABILISER": ("microtubule stabiliser", "microtubule stabilisers")}
TRAP_CAUSE = {"TOP1_POISON": ("the DNA damage they cause", "they trap {t} on DNA and break the DNA",
                              "the target follows the damage"),
              "TOP2_POISON": ("the DNA damage they cause", "they trap {t} on DNA and break the DNA",
                              "the target follows the damage"),
              "PARP_TRAPPER": ("the DNA damage they cause", "they trap {t} on DNA, which harms more than {t} loss",
                               "the target follows the damage"),
              "TUBULIN_STABILISER": ("the frozen microtubules (mitotic arrest)",
                                     "they freeze microtubules and arrest mitosis", "the target follows the arrest")}
DESTAB_CLASS = "inhibitor (microtubule destabiliser)"
# D4: the ChEMBL target types whose genes count as a compound's targets for drug_target. A protein complex (the 26S
# proteasome: 38 subunits; the ribosome: up to 78) lists every subunit, while the drug binds one of them, so complexes
# give no membership (Tahoe's own target list still does).
CHEMBL_MEMBER_TYPES = ("SINGLE PROTEIN", "PROTEIN FAMILY", "CHIMERIC PROTEIN")
ADAGRASIB_REF = "Hallin J et al. 2020, Cancer Discov 10:54 (doi:10.1158/2159-8290.cd-19-1167, PMID 31658955)"

KINDS = ("genotype_response", "genotype_baseline", "genotype_sensitivity", "genotype_selectivity", "null_response",
         "null_baseline", "null_sensitivity", "null_selectivity", "drug_target", "level", "level_sensitivity")
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
# VERSION 5 reasons (a '; ' inside a reason is written ', ' by _join, so both are accepted)
_RX_CAVEAT5 = (re.compile(r"^over the whole table the controls expect "),)
_RX_SUPPORT5 = (re.compile(r"^also at .+ \(q "),)
_RX_NOTE5 = (re.compile(r"^\d+ of the \d+ comparison lines are heavily mutated"),
             re.compile(r"^loss of function is the metadata's inference"),
             re.compile(r"^one test for \d+ (?:targets|genes absent from the same lines) \("))
_RX_FALSE = re.compile(r"^random comparison groups give about [0-9.]+ such (?:within-group )?arrows per group \(up to "
                       r"[0-9.]+\)[;,] this comparison gives \d+: (?:about )?(under 1|\d+)% of them may be false")
_RX_NONSPEC = re.compile(r"would appear for any gene \((under 1|\d+)%\)$")
_RX_NONSPEC_SET = re.compile(r"^random line sets give about [0-9.]+ such arrows per set \(up to [0-9.]+\)[;,] this set "
                             r"gives \d+: (?:about )?(under 1|\d+)% of them would appear for any set of lines")
_RX_CHANGED = re.compile(r"^(?:rule changed in direction version \d+|grade A blocked since direction version \d+)")
_RX_TI = re.compile(r"^drug-doses of translation inhibitors carry (?:(\d+)% of the evidence|a share of the evidence "
                    r"that could not be measured)(, the strongest among them)?")


def reason_tier(reason, art_share=np.nan):
    """The tier of one reason (TIERS): 'caveats' (KIND_CAVEATS: the same on every arrow of a kind), 'support'
    (evidence for the arrow), 'notes' (a graded reason below its threshold: the NOTE_* constants) or 'alerts' (every
    other reason, and a graded one at or past its threshold). Graded reasons are read from their own words (their
    counts are whole numbers in the text); the artifact-flag reason of a response edge from art_share (the stored
    float32), of a drug_target edge from its share of the supporting compounds. A reason this code does not know stays
    an alert."""
    r = str(reason)
    if r in _CAVEAT_TEXTS or any(rx.search(r) for rx in _RX_CAVEAT5):
        return "caveats"
    if any(rx.search(r) for rx in _RX_SUPPORT + _RX_SUPPORT5):
        return "support"
    if any(rx.search(r) for rx in _RX_NOTE5) or _RX_CHANGED.search(r):    # VERSION 6: what a changed rule did
        return "notes"
    for rx in (_RX_FALSE, _RX_NONSPEC, _RX_NONSPEC_SET):          # expected false / non-specific shares (D6, D11)
        m = rx.search(r)
        if m:
            pct = 0 if m.group(1) == "under 1" else int(m.group(1))
            return "alerts" if pct >= round(100 * FALSE_SHARE_ALERT) else "notes"
    m = _RX_TI.search(r)                                         # translation inhibitors (D17)
    if m:
        if m.group(2) or m.group(1) is None:
            return "alerts"
        return "alerts" if int(m.group(1)) >= round(100 * NOTE_TI_SHARE) else "notes"
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
    c.dd_flags = _flags_of_record(out, dd)
    c.dd_art = np.array([has_artifact(f) for f in c.dd_flags], dtype=bool)
    c.n_wells = _n_wells(dd)
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
    _load_mechanisms(c, out)
    _load_coords(c, out)
    _load_selectivity(c, out, lines)
    return c


def _flags_of_record(out, dd):
    """The drug-doses' flags of record (tables.dd_flags_of_record: the atlas flags, the neighbouring-well and the
    translation-inhibitor tokens), else drugdose.csv's own flags (an output without the tables stage)."""
    try:
        from .tables import dd_flags_of_record
        f = dd_flags_of_record(out)
        if len(f) == len(dd):
            return np.asarray(f, dtype=object)
    except Exception as e:  # noqa: BLE001  (an older output: the atlas flags)
        log(f"  flags of record not readable ({e}); the atlas flags are used")
    return dd["flags"].fillna("").astype(str).to_numpy(dtype=object)


def _n_wells(dd):
    """Wells behind each drug-dose (drugdose.csv n_wells, else the ','-joined wells), -1 when unknown."""
    if "n_wells" in dd:
        v = pd.to_numeric(dd["n_wells"], errors="coerce").fillna(-1).to_numpy()
        return v.astype(np.int64)
    if "wells" in dd:
        return np.array([len([w for w in str(x).split(",") if w.strip()]) if str(x).strip() and str(x) != "nan"
                         else -1 for x in dd["wells"]], dtype=np.int64)
    return np.full(len(dd), -1, dtype=np.int64)


def _load_mechanisms(c, out):
    """The mechanism classes (mechanisms.classes_by_drug, drug_classes) and ChEMBL's mechanisms of the drugs
    (drug_mechanisms; no rows without ChEMBL), and per drug-dose: in a translation-inhibitor class (c.ti_dd) with the
    class's words and sources (c.ti_src). Every use names its source."""
    c.cls_by_drug, c.cls_rows, c.mech = {}, pd.DataFrame(columns=MX.CLASS_COLUMNS), pd.DataFrame(
        columns=MX.MECH_COLUMNS)
    try:
        c.cls_by_drug = MX.classes_by_drug(out)
        c.cls_rows = MX.drug_classes(out)
        c.mech = MX.drug_mechanisms(out)
    except Exception as e:  # noqa: BLE001  (no classes: Tahoe's annotation alone)
        log(f"  mechanism classes not readable ({e}): Tahoe's annotation alone")
    c.chembl = bool(len(c.mech))
    # the source of each (drug, class) membership, as the reference stage wrote it
    c.cls_src = {(str(d), str(k)): str(s_ or "") for d, k, s_ in zip(c.cls_rows.get("drug", []),
                                                                      c.cls_rows.get("class", []),
                                                                      c.cls_rows.get("source", []))}
    tl = {d: [k for k in ks if MX.class_info(k).get("effect") == "translation"] for d, ks in c.cls_by_drug.items()}
    c.ti_dd = np.array([bool(tl.get(str(d))) for d in c.drug], dtype=bool)
    c.ti_src_by_drug = {}
    for d in sorted({str(x) for x in c.drug[c.ti_dd]}):
        c.ti_src_by_drug[d] = ", ".join(
            f"{MX.class_info(k).get('label', k)}, {(c.cls_src.get((d, k), '') or 'code constant').replace('; ', ', ')}"
            for k in tl.get(d, []))


def _load_coords(c, out):
    """Gene coordinates (D9 same locus): reference/annotations.parquet by gene col (the measured genes) and
    reference/gene_coords.parquet by symbol (genes Tahoe does not measure, e.g. drivers). c.coord_col: per col
    (chrom, start, end) or None; c.coord_sym: {SYMBOL: (chrom, start, end)}."""
    c.coord_col = [None] * c.gK
    c.loc_col = [""] * c.gK                                  # cytogenetic band (HGNC location), '' when unknown
    c.coord_sym = {}
    rd = os.path.join(out, "reference")
    p = os.path.join(rd, "annotations.parquet")
    if os.path.exists(p):
        try:
            import pyarrow.parquet as pq
            have = set(pq.read_schema(p).names)
            a = pd.read_parquet(p, columns=[x for x in ("col", "chrom", "start", "end", "location") if x in have])
            for col, ch, st, en in zip(a["col"], a["chrom"], a["start"], a["end"]):
                if 0 <= int(col) < c.gK and _coord_ok(ch, st, en):
                    c.coord_col[int(col)] = (str(ch), int(st), int(en))
            if "location" in a:
                for col, lo in zip(a["col"], a["location"].fillna("").astype(str)):
                    if 0 <= int(col) < c.gK and lo.strip() and lo not in ("nan", "<NA>"):
                        c.loc_col[int(col)] = lo.strip()
        except Exception as e:  # noqa: BLE001
            log(f"  gene coordinates (annotations) not readable ({e})")
    p = os.path.join(rd, "gene_coords.parquet")
    if os.path.exists(p):
        try:
            a = pd.read_parquet(p, columns=["symbol", "chrom", "start", "end"])
            for sy, ch, st, en in zip(a["symbol"], a["chrom"], a["start"], a["end"]):
                if _coord_ok(ch, st, en):
                    c.coord_sym.setdefault(str(sy).upper(), (str(ch), int(st), int(en)))
        except Exception as e:  # noqa: BLE001
            log(f"  gene coordinates (gene_coords) not readable ({e})")


def _coord_ok(ch, st, en):
    try:
        return bool(str(ch).strip()) and str(ch) not in ("nan", "None", "<NA>") and np.isfinite(float(st)) and \
            np.isfinite(float(en))
    except (TypeError, ValueError):
        return False


def _load_selectivity(c, out, lines):
    """D13's input: per (drug-dose, line) how strongly the line responds against its typical drug-dose (rel_log2), its
    genes beyond the per-line cut (n_genes) and 'selective', from tables/drug_line_response.parquet; None when the
    table is missing (then _responses computes them from the tensor, as the tables stage does). Lines outside the
    growth analysis are left out (NaN), as for the cell numbers."""
    c.Rsel = c.Nsel = c.sel_line = c.Ssel = None
    c.sel_from = "none"
    p = os.path.join(out, "tables", "drug_line_response.parquet")
    if os.path.exists(p):
        try:
            t = pd.read_parquet(p, columns=["dd", "line", "measured", "n_genes", "rel_log2", "sel_z", "selective"])
            dd_ = t["dd"].to_numpy(np.int64)
            ln = t["line"].to_numpy(np.int64)
            ok = (dd_ >= 0) & (dd_ < c.Dn) & (ln >= 0) & (ln < c.L)
            R = np.full((c.Dn, c.L), np.nan)
            N = np.full((c.Dn, c.L), -1, dtype=np.int64)
            S = np.zeros((c.Dn, c.L), dtype=bool)
            meas = t["measured"].to_numpy(bool)
            R[dd_[ok], ln[ok]] = np.where(meas[ok], t["rel_log2"].to_numpy(np.float64)[ok], np.nan)
            N[dd_[ok], ln[ok]] = t["n_genes"].to_numpy(np.int64)[ok]
            S[dd_[ok], ln[ok]] = t["selective"].to_numpy(bool)[ok] & meas[ok]
            Z = np.full((c.Dn, c.L), np.nan)
            Z[dd_[ok], ln[ok]] = np.where(meas[ok], t["sel_z"].to_numpy(np.float64)[ok], np.nan)
            c.Rsel, c.Nsel, c.sel_line, c.Ssel = R, N, S, Z
            c.sel_from = "tables/drug_line_response.parquet"
        except Exception as e:  # noqa: BLE001  (computed from the tensor instead)
            log(f"  tables/drug_line_response.parquet not readable ({e}): selectivity from the tensor")
    c.in_growth = np.ones(c.L, dtype=bool)
    if "in_growth_analysis" in lines:
        c.in_growth = lines["in_growth_analysis"].astype(str).str.lower().isin(["true", "1", "1.0"]).to_numpy()


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
    sel_fallback = getattr(c, "Rsel", None) is None                            # no drug_line_response table
    if sel_fallback:
        t_line, ng_sel, nm_sel = _line_cut(c.out), np.zeros((Dn, L), np.int64), np.zeros((Dn, L), bool)
    log(f"  streaming the per-line tensor: {gK:,} genes in chunks of {chunk} (K = {k} drug-doses per gene; "
        f"{mg.size:,} reference values)")
    t0 = time.time()
    for g0 in range(0, gK, chunk):
        g1 = min(gK, g0 + chunk)
        rows = np.arange(g1 - g0)[:, None]
        Z = c.DZ.read(g0, g1).astype(np.float32, copy=False)                  # c x Dn x L
        Z = np.where(meas[g0:g1, None, :], Z, np.nan)
        np.clip(Z, -Z_CLIP, Z_CLIP, out=Z)
        if sel_fallback:                                                       # genes beyond the per-line cut
            with np.errstate(invalid="ignore"):
                ng_sel += (np.abs(Z) >= t_line).sum(axis=0)
            nm_sel |= np.isfinite(Z).any(axis=0)
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
    _selectivity_input(c, (t_line, ng_sel, nm_sel) if sel_fallback else None)
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


def _line_cut(out):
    """The per-line |z| cut of the tables stage (tables/info.json line_z_threshold), else Z_SIG."""
    try:
        with open(os.path.join(out, "tables", "info.json"), encoding="utf-8") as fh:
            t = float(json.load(fh).get("line_z_threshold"))
        return t if np.isfinite(t) and t > 0 else Z_SIG
    except (OSError, ValueError, TypeError):
        return Z_SIG


def _selectivity_input(c, fallback=None):
    """D13: c.Rsel (rel_log2, drug-doses x lines; NaN outside the growth analysis), c.Nsel (genes beyond the per-line
    cut; -1 not measured), c.sel_line (selective, growth-analysis lines only) and c.sel_dd (drug-doses with >= 1
    selective line: the ones tested). fallback = (cut, counts, measured) from the tensor when tables/
    drug_line_response.parquet is missing: rel_log2 and 'selective' then come from tables.line_selectivity and
    selective_mask on genes with |per-line z| >= the cut (the tables stage also asks a 1.5x fold)."""
    if fallback is not None:
        from .tables import line_selectivity, selective_mask
        t, ng, nm = fallback
        n_genes = np.where(nm, ng, -1)
        rel, selz = line_selectivity(n_genes, nm)
        c.Rsel, c.Nsel, c.sel_line, c.Ssel = rel, n_genes, selective_mask(selz, n_genes) & nm, selz
        c.sel_from = (f"the per-line tensor (genes with |per-line z| >= {t:g}; tables/drug_line_response.parquet was "
                      "missing)")
    c.Rsel = np.asarray(c.Rsel, dtype=np.float64).copy()
    c.Rsel[:, ~c.in_growth] = np.nan
    c.Ssel = np.where(np.isfinite(c.Rsel), np.asarray(c.Ssel, dtype=np.float64), np.nan)
    c.sel_line = np.asarray(c.sel_line, dtype=bool) & c.in_growth[None, :] & np.isfinite(c.Rsel)
    c.sel_dd = c.sel_line.any(axis=1)


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


def _records(c):
    """The recorded driver alterations: rec = {GENE: {line index: set of (mechanism, variant type, change)}} (mechanism
    'LoF' / 'GoF' / '?'; change = the metadata's Driver_ProtEffect_or_CdnaEffect, '' when absent), recorded (lines with
    any record) and the source text."""
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
        ch = m["Driver_ProtEffect_or_CdnaEffect"].fillna("").astype(str).to_numpy() \
            if "Driver_ProtEffect_or_CdnaEffect" in m else np.array([""] * len(m))
        for i in range(len(m)):
            if li[i] < 0 or gs[i] in ("", "NAN", "NONE"):
                continue
            mm = mech[i] if mech[i] in ("LoF", "GoF") else "?"
            rec.setdefault(gs[i], {}).setdefault(int(li[i]), set()).add((mm, vt[i], ch[i].strip()))
    elif "drivers" in c.lines:
        src = "lines.csv drivers (no mechanism)"
        for i, s in enumerate(c.lines["drivers"].fillna("").astype(str)):
            parts = [p.strip() for p in s.split(";") if p.strip()]
            if parts:
                recorded[i] = True
            for p in parts:
                gname = p.split("(")[0].strip().upper()
                vt = p.split("(")[1].rstrip(")") if "(" in p else "nan"
                rec.setdefault(gname, {}).setdefault(i, set()).add(("?", vt, ""))
    return rec, recorded, src


_RX_SUB = re.compile(r"^([A-Z])(\d+)([A-Z*])$")


def allele_change(x):
    """A recorded protein change as an allele: 'p.G12C' -> 'G12C' (simple substitutions only, '*' a stop); None for a
    synonymous change ('p.T125T'), a frameshift ('p.S90fs'), a deletion ('DEL') or anything else."""
    s = str(x or "").strip()
    if s.startswith("p."):
        s = s[2:]
    m = _RX_SUB.match(s)
    if not m or m.group(1) == m.group(3):
        return None
    return s


def _line_category(recs):
    """A line's records of one gene in the group words (D15): 'missense' (any missense record; a line with missense
    and other records counts as missense), 'truncating' (Frameshift, Stopgain, Splice_site, Deletion,
    Synonymous_splicing, Nonsense), else its variant type in lower case ('promoter')."""
    vts = {str(v[1]) for v in recs}
    if "Missense" in vts:
        return "missense"
    if vts & set(TRUNCATING):
        return "truncating"
    other = sorted(x for x in vts if x and x.lower() != "nan")
    return other[0].lower().replace("_", " ") if other else "type not recorded"


def _composition(lines_of, alt):
    """'8 with a missense change, 2 truncating, splice or deletion only' (categories with a line, in this order:
    missense, truncating, then the others by count) and the counts {category: n}."""
    cats = pd.Series([_line_category(lines_of[i]) for i in np.flatnonzero(alt)], dtype=object).value_counts()
    n = {str(k): int(v) for k, v in cats.items()}
    parts = []
    if n.get("missense"):
        parts.append(f"{n['missense']} with a missense change")
    if n.get("truncating"):
        parts.append(f"{n['truncating']} truncating, splice or deletion only")
    for k, v in sorted(((k, v) for k, v in n.items() if k not in ("missense", "truncating")),
                       key=lambda kv: (-kv[1], kv[0])):
        parts.append(f"{v} {k}")
    return ", ".join(parts), n


def _hotspot_lines(gene, lines_of, idx):
    """The lines (of idx) whose records of the gene hit a hotspot of HOTSPOTS (a listed change, or a missense change at
    a listed codon)."""
    h = HOTSPOTS.get(gene)
    if not h:
        return []
    out = []
    for i in idx:
        chs = [allele_change(v[2]) for v in lines_of.get(int(i), ()) if str(v[1]) == "Missense" or
               allele_change(v[2])]
        if any(a and (a in h["changes"] or a[:-1] in h["missense_codons"]) for a in chs):
            out.append(int(i))
    return out


def _gene_desc(c, gene, mech, alt, inn, lines_of):
    """The words of a gene-level group (D15): 'TP53 recorded as loss of function (10 lines: 8 with a missense change,
    2 truncating, splice or deletion only) vs not recorded (8)'; gain of function the same; 'altered (any record)'."""
    comp, n = _composition(lines_of, alt)
    head = {"LoF": "recorded as loss of function", "GoF": "recorded as gain of function",
            "any": "altered (any record)"}[mech]
    return f"{gene} {head} ({int(alt.sum())} lines: {comp}) vs not recorded ({int(inn.sum())})", n


def _allele_groups(c, rec, recorded, groups):
    """Allele groups (D12): exact changes (gene, 'G12C') recorded in >= MIN_SIDE lines; codons ('G12') in >= MIN_SIDE
    lines whose line set differs from every exact group of the gene; hotspots of HOTSPOTS; amplifications (variant
    type 'Gain', >= MIN_SIDE lines). The comparison: every other recorded line, other alleles of the gene included. A
    group whose line set equals an existing group (gene-level or allele) is not added; a gene-level group then gains
    the composition in its words ('(7 lines: ...; all p.V600E)'). Returns (new groups, not testable texts)."""
    L = c.L
    out, not_testable = [], []
    existing = [(g["alt"], g) for g in groups]
    for gene in sorted(rec):
        lines_of = rec[gene]
        by_change, mech_of = {}, {}
        for li_, s in lines_of.items():
            for (mm, vt, ch) in s:
                a = allele_change(ch)
                if a:
                    by_change.setdefault(a, set()).add(li_)
                    mech_of.setdefault(a, set()).add(mm)
        cands = []
        exact_sets = []
        for a in sorted(by_change, key=lambda x: (int(re.sub(r"\D", "", x) or 0), x)):
            if len(by_change[a]) >= MIN_SIDE:
                cands.append((a, f"p.{a}", sorted(by_change[a]), mech_of[a]))
                exact_sets.append(frozenset(by_change[a]))
        codon = {}
        for a, ls in by_change.items():
            codon.setdefault(a[:-1], set()).update(ls)
        for cd in sorted(codon, key=lambda x: (int(re.sub(r"\D", "", x) or 0), x)):
            ls = codon[cd]
            if len(ls) >= MIN_SIDE and frozenset(ls) not in exact_sets:
                mm = set().union(*[mech_of[a] for a in by_change if a[:-1] == cd])
                cands.append((f"{cd} (codon)", f"codon {cd}", sorted(ls), mm))
        hs = _hotspot_lines(gene, lines_of, list(lines_of))
        if gene in HOTSPOTS and len(hs) >= MIN_SIDE:
            h = HOTSPOTS[gene]
            what = ", ".join(h["changes"]) if h["changes"] else "missense at " + ", ".join(h["missense_codons"])
            mm = {v[0] for i in hs for v in lines_of[i]}
            cands.append(("hotspot", f"hotspot ({what})", hs, mm))
        gain = sorted(i for i, s in lines_of.items() if any(str(v[1]) == "Gain" for v in s))
        if len(gain) >= MIN_SIDE:
            cands.append(("amplification", "amplification", gain, {v[0] for i in gain for v in lines_of[i]}))
        elif gain:
            not_testable.append(f"{gene} amplification: {len(gain)} line{'s' if len(gain) > 1 else ''} "
                                f"({', '.join(str(c.line_name[i]) for i in gain)}), fewer than {MIN_SIDE}")
        for label, words, ls, mm in cands:
            alt = np.zeros(L, dtype=bool)
            alt[ls] = True
            inn = recorded & ~alt
            if inn.sum() < MIN_SIDE:
                continue
            same = [g for a_, g in existing if g["gene"] == gene and np.array_equal(a_, alt)]
            keep = (lambda a_: a_ in HOTSPOTS.get(gene, {}).get("changes", ()) or
                    a_[:-1] in HOTSPOTS.get(gene, {}).get("missense_codons", ())) if label == "hotspot" else \
                (lambda a_: a_[:-1] == label.split(" ")[0]) if label.endswith("(codon)") else None
            comp = _allele_comp(alt, lines_of, keep) if label != "amplification" else "every one amplified"
            if same:
                for g in same:
                    if not g.get("allele") and "composition" not in g and label != "amplification":
                        g["composition"] = comp
                        g["desc"] = re.sub(r"^(.*? \(\d+ lines: [^)]*)\)", lambda m_: f"{m_.group(1)}; {comp})",
                                           g["desc"], count=1)
                continue
            mmc = {x for x in mm if x in ("LoF", "GoF")}
            mech = mmc.pop() if len(mmc) == 1 and "?" not in mm else "any"
            other = int((inn & np.isin(np.arange(L), list(lines_of))).sum())
            # an exact change names itself; a codon or hotspot group gives its alleles
            extra = f": {comp}" if label == "hotspot" or label.endswith("(codon)") else ""
            desc = (f"{gene} {words} ({int(alt.sum())} lines{extra}) vs other lines ({int(inn.sum())}; {other} of "
                    f"them with another {gene} change)")
            g = _group_common(c, f"genotype:{gene}:{label}", "genotype", gene, mech, alt, inn, desc)
            g["allele"] = label
            g["actor"] = gene if label == "amplification" else f"{gene} {words.split(' (')[0]}"
            g["side_words"] = f"{gene}-amplified lines" if label == "amplification" else \
                f"{gene} {words.split(' (')[0]} lines"
            g["composition"] = comp
            g["variants"] = "; ".join(f"{k} {v}" for k, v in pd.Series(
                [v[1] for li_ in ls for v in lines_of[li_]]).value_counts().items())
            if mech == "any":
                g["alerts"].append(f"the {int(alt.sum())} lines' records of {gene} do not agree on one mechanism "
                                   "(loss or gain of function, or none recorded): the sign of the gene's activity is "
                                   "not inferred")
            if label == "hotspot":
                g["note"] = f"hotspot list: {HOTSPOTS[gene]['source']}"
            out.append(g)
            existing.append((alt, g))
    return out, not_testable


def _allele_comp(alt, lines_of, keep=None):
    """The alleles of a group's lines: 'all p.V600E', or 'G12C 2, G12D 2, G12S 1, G12V 1' (keep: only the alleles of
    the group, e.g. its codon or hotspots)."""
    cnt = {}
    for i in np.flatnonzero(alt):
        al = sorted({a for a in (allele_change(v[2]) for v in lines_of.get(int(i), ())) if a and (keep is None or
                                                                                                  keep(a))})
        for a in al or ["no simple change recorded"]:
            cnt[a] = cnt.get(a, 0) + 1
    if len(cnt) == 1:
        a = next(iter(cnt))
        return f"all p.{a}" if a != "no simple change recorded" else a
    return ", ".join(f"{k} {v}" for k, v in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])))


def _genotype_groups(c):
    """Groups from the recorded driver alterations (module docstring, 1): gene-level groups (LoF / GoF / any) and the
    allele groups (D12). Returns (groups, records, source, recorded); records = {gene: {line index: set of (mechanism,
    variant type, change)}}. Sets c.n_driver_genes, c.heavy (D7) and c.allele_not_testable."""
    L = c.L
    rec, recorded, src = _records(c)
    nd = np.zeros(L, dtype=np.int64)
    for gene, lines_of in rec.items():
        for li_ in lines_of:
            nd[li_] += 1
    c.n_driver_genes = nd
    c.heavy = nd >= HYPERMUT_MIN_GENES
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
            desc, comp_n = _gene_desc(c, gene, mech, alt, inn_g, lines_of)
            g = _group_common(c, f"genotype:{gene}:{mech}", "genotype", gene, mech, alt, inn_g, desc)
            g["allele"] = ""
            vts = pd.Series([x[1] for li_ in np.flatnonzero(alt) for x in lines_of[li_]]).value_counts()
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
            nmis = int(comp_n.get("missense", 0))
            if mech == "LoF" and nmis * 3 >= int(alt.sum()) and nmis:
                hs = _hotspot_lines(gene, lines_of, np.flatnonzero(alt))
                hot = (f" ({len(hs)} of them at hotspot codons {', '.join(HOTSPOTS[gene]['missense_codons'])}: "
                       f"{HOTSPOTS[gene]['source']})" if hs and HOTSPOTS.get(gene, {}).get("missense_codons") else "")
                g["alerts"].append(f"loss of function is the metadata's inference; {nmis} of the {int(alt.sum())} "
                                   f"lines carry a missense change{hot}, and missense changes can also act "
                                   "dominant-negative or gain new functions")
            g["deleted"] = np.array([any(x[1] == "Deletion" for x in lines_of.get(i, ())) for i in range(L)])
            groups.append(g)
    alle, c.allele_not_testable = _allele_groups(c, rec, recorded, groups)
    groups.extend(alle)
    # co-occurrence between the altered sets of different genes (Jaccard), and anti-occurrence: another gene's
    # altered lines sit on the OTHER side of the comparison (phi <= -JACCARD_CO over the lines both compare) - as
    # much a confounder as co-occurrence, with the opposite sign; both block grade A. Groups of the same gene (its
    # mechanisms and alleles) are skipped.
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
                                                              for h, j in g["cooccur"]))
        seen_a = {}
        for v, h, ni_, na_ in sorted(anti, reverse=True):
            seen_a.setdefault(h, (v, ni_, na_))
        g["anti"] = [(h, v[0]) for h, v in seen_a.items()]
        if seen_a:
            n_al, n_in = int(g["alt"].sum()), int(g["inn"].sum())
            g["alerts"].append("another gene's alterations sit on the other side of the comparison: " + ", ".join(
                f"{h} alterations are in {ni_} of the {n_in} comparison lines and {na_} of the {n_al} "
                f"{g['gene']}-altered lines (phi -{v:.2f})" for h, (v, ni_, na_) in seen_a.items())
                + ": that alteration may be the cause, with the opposite sign")
        _heavy_alerts(c, g)
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


def _heavy_alerts(c, g):
    """D7: heavily mutated lines (alterations recorded in >= HYPERMUT_MIN_GENES driver genes) concentrated on a side.
    The altered side holding >= 2 of them at >= 2x their share among the other lines: an alert (blocks grade A,
    g['heavy_alert']); the comparison side so enriched: a note."""
    hv = getattr(c, "heavy", None)
    g["n_heavy_alt"], g["n_heavy_inn"], g["heavy_alert"] = 0, 0, False
    if hv is None:
        return
    ha, hi = hv & g["alt"], hv & g["inn"]
    na, ni = int(g["alt"].sum()), int(g["inn"].sum())
    ka, ki = int(ha.sum()), int(hi.sum())
    g["n_heavy_alt"], g["n_heavy_inn"] = ka, ki
    side = _sides(g)[0]
    if ka >= 2 and na and (ki == 0 or ka / na >= 2.0 * ki / max(ni, 1)):
        g["heavy_alert"] = True
        g["alerts"].append(f"heavily mutated lines: {ka} of the {na} {side} ({', '.join(c.line_name[ha])}) record "
                           f"alterations in {HYPERMUT_MIN_GENES} or more driver genes, against {ki} of the {ni} "
                           "others: such lines carry many recorded and unrecorded changes, and any of them, or the "
                           "mutation load itself, could be the cause")
    elif ki >= 2 and ni and (ka == 0 or ki / ni >= 2.0 * ka / max(na, 1)):
        g["alerts"].append(f"{ki} of the {ni} comparison lines are heavily mutated ({', '.join(c.line_name[hi])}): "
                           f"they record alterations in {HYPERMUT_MIN_GENES} or more driver genes")


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
        g["null_co"], g["null_co_n"] = [], 0
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
                # every set is named when they are few (the reason is then an alert: a candidate co-deletion);
                # beyond NOTE_COABSENT_SETS the reason is a note (a tissue programme): the 3 closest, and the count
                keep = hit if hit.size <= NOTE_COABSENT_SETS else hit[:3]
                out[i]["null_co"] = [(_set_name(c, out[h]["genes"]), float(jac[i - b0, h])) for h in keep]
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
        al.append(f"{len(others)} other gene(s) are absent from exactly these lines ({', '.join(others)}): any of "
                  "them could be the cause")
    rx = records.get(str(c.sym[x]).upper(), {})
    dele = np.array([any(v[1] == "Deletion" or v[0] == "LoF" for v in rx.get(i, ())) for i in range(c.L)])
    if dele.any():
        j = float((dele & g["alt"]).sum() / max(1, (dele | g["alt"]).sum()))
        if j >= JACCARD_CO:
            al.append(f"the lines lacking {c.sym[x]} carry a recorded loss of {c.sym[x]} (overlap {j:.2f}): "
                      "genotype evidence too")
    co = [(h, j) for h, j in g["cooccur"] if h != str(c.sym[x]).upper()]     # its own records: 'deletion recorded'
    if co:
        al.append("co-occurs with " + ", ".join(f"{h}-altered lines (overlap {j:.2f})" for h, j in co))
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
    # cells (sensitivity: DD_A, the drug-doses of dd_mask) and response strength (selectivity: rel_log2 of
    # tables/drug_line_response, the drug-doses with >= 1 selective line): the same test on drug-dose rows
    for kk, V, msk in (("sensitivity", c.Aab, dd_mask), ("selectivity", getattr(c, "Rsel", None),
                                                          getattr(c, "sel_dd", None))):
        if kk not in kinds or V is None:
            continue
        dsel = np.arange(c.Dn) if msk is None else np.flatnonzero(msk)
        if dsel.size:
            D, Zt, na, ni = _contrast(V[dsel], None, alt, inn)
            Tobs, Tp = _standardise(Zt)
            ok = (na >= MIN_SIDE) & (ni >= MIN_SIDE) & np.isfinite(Tobs)
            Tp[~ok] = np.nan
            res[kk] = {"t": dsel, "T": np.where(ok, Tobs, np.nan), "Tp": Tp, "D": D,
                       "na": na, "ni": ni, "n_arr": _row_arrangements(g, np.isfinite(V[dsel]))}
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
    """A drug-dose's flags for a drug-dose list: ' [artifact flags: a, b]' (one of common.ARTIFACT_FLAGS among them:
    the atlas's seven and the neighbouring-well flag), ' [flags: a, b]' (other flags), '' (none)."""
    f = str(c.dd_flags[d] or "").replace("; ", ", ")
    if not f:
        return ""
    return f" [{'artifact flags' if c.dd_art[d] else 'flags'}: {f}]"


def _ti_reason(c, labels, share, strong, drugs):
    """D17: the translation-inhibitor reason of a response edge (or of a drug_target edge whose supporting compounds
    are all members: share 1)."""
    head = f"{int(math.floor(float(share) * 100))}% of the evidence" if np.isfinite(share) else \
        "a share of the evidence that could not be measured"
    src = "; ".join(f"{d}: {c.ti_src_by_drug.get(d, 'translation inhibitor')}" for d in dict.fromkeys(drugs))
    return (f"drug-doses of translation inhibitors carry {head}{', the strongest among them' if strong else ''} "
            f"({', '.join(labels)}; {src}): blocking translation stabilises short-lived mRNAs, so a rise there may not "
            "be more transcription")


def _response_all(c, g, y, sign_d, items):
    """A response edge's drugdoses_all (every one of Y's K drug-doses: contrast, folds and flags; strongest in the
    edge's direction first, those without a value on a side last), its art_share (the share of sum |contrast| over the
    K drug-doses carried by artifact-flagged ones; NaN without any contrast), its artifact-flag reason ('' when none
    of the K drug-doses with a value is flagged): '(N% of the evidence[, the strongest among them]): every flagged
    one' - the strongest = the first of top_drugdoses (items), the one the reading names -, and the same for the
    drug-doses of translation inhibitors (D17: ti_share and its reason)."""
    pd_ = _response_dd(c, g, y, sign_d)
    if pd_ is None:
        return "", np.nan, "", np.nan, ""
    con, fi, fa, sc, o = pd_
    parts, flagged, ti = [], [], []
    for k in o:
        d = int(c.sel[y, k])
        if np.isfinite(con[k]):
            parts.append(f"{c.dd_label[d]}: {_fmt_fold(fa[k])} vs {_fmt_fold(fi[k])} (z diff {con[k]:+.1f})"
                         + _flags_text(c, d))
            if c.dd_art[d]:
                flagged.append(d)
            if c.ti_dd[d]:
                ti.append(d)
        else:
            parts.append(f"{c.dd_label[d]}: no value on one side" + _flags_text(c, d))
    fin = np.isfinite(con)
    tot = float(np.abs(con[fin]).sum())
    dds = np.array([int(c.sel[y, k]) for k in range(con.size)])
    art = c.dd_art[dds]
    share = np.float32(np.abs(con[fin & art]).sum() / tot) if tot > 0 else np.float32(np.nan)
    tim = c.ti_dd[dds]
    ti_share = np.float32(np.abs(con[fin & tim]).sum() / tot) if tot > 0 else np.float32(np.nan)
    reason = ""
    if flagged:
        head = (f"{int(math.floor(float(share) * 100))}% of the evidence" if np.isfinite(share) else
                "share of the evidence not measurable")
        strong = bool(items) and bool(c.dd_art[items[0][0]])
        reason = (f"supporting drug-doses with artifact flags ({head}{', the strongest among them' if strong else ''}"
                  "): " + "; ".join(f"{c.dd_label[d]} ({c.dd_flags[d]})" for d in flagged))
    ti_reason = ""
    if ti:
        strong = bool(items) and bool(c.ti_dd[items[0][0]])
        ti_reason = _ti_reason(c, [c.dd_label[d] for d in ti], ti_share, strong, [str(c.drug[d]) for d in ti])
    return "; ".join(parts), share, reason, ti_share, ti_reason


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
    """(the altered side, the other side) in words: 'TP53-LoF lines', 'the other lines'; 'KRAS p.G12C lines'; for a
    natural knockout 'lines without X', 'lines expressing X'."""
    if g["mech"] == "null":
        return f"lines without {g['gene']}", f"lines expressing {g['gene']}"
    if g.get("side_words"):
        return g["side_words"], "the other lines"
    tag = g["mech"] if g["mech"] in ("LoF", "GoF") else "altered"
    return f"{g['gene']}-{tag} lines", "the other lines"


def _actor(g):
    """Whose activity a genotype edge speaks of: 'TP53', or an allele group's 'KRAS p.G12C'."""
    return g.get("actor") or g["gene"]


def _activity_words(sign, what, response=False):
    """'X activity raises' / 'lowers'; for a drug response (response=True) 'strengthens' / 'weakens': the sign of a
    response edge is about how strongly the target responds in its own direction (r = per-line z x the sign of its
    pooled z), so for a target that falls under the drugs, 'strengthens' means a deeper fall."""
    if sign > 0:
        return f"{what} {'strengthens' if response else 'raises'}"
    if sign < 0:
        return f"{what} {'weakens' if response else 'lowers'}"
    return ""


def _may(sign, response=False, cells=False):
    """D16, natural knockouts: 'may raise' / 'may lower' (a level), 'may strengthen' / 'may weaken' (a response),
    'may protect the cells' / 'may make the cells more sensitive' (cells): the lines without X are not an experiment
    on X, so the words say what X may do."""
    if cells:
        return "may protect the cells" if sign > 0 else "may make the cells more sensitive"
    if response:
        return "may strengthen" if sign > 0 else "may weaken"
    return "may raise" if sign > 0 else "may lower"


def _grade_genotype(g, na, ni, q, block=False):
    """A (VERSION 5): >= FULL_SIDE lines on each side (measured; within organs: those sharing an organ with the other
    side), q < Q_A, compared within organs, no co-occurrence alert (another gene's altered lines overlapping the altered
    side, or sitting on the other side: anti-occurrence), no heavily mutated lines concentrated on the altered side
    (D7), and nothing kind-specific that blocks it (block). For a response, block holds: it rests on the global-
    sensitivity correction or its evidence comes mostly from drug-doses without any correction (VERSION 2), and
    (VERSION 5, D5) the mean over all its drug-doses, with and without the correction, goes the edge's way; less than
    BOTH_WAYS_A of the evidence goes the other way; not a floor (a target that mostly falls and is >= 2x lower at
    baseline in the altered lines); the target measured in >= MEASURED_A of each side's lines. A selectivity edge seen
    at one dose only is blocked too (D13). The group's expected false share (D6) is applied after the rows are built
    (_false_shares). C when tissue-confounded (compared across organs and the sides' organs differ: the comparison
    cannot separate the gene from the tissue - graded as for a natural knockout). Else B."""
    if g["tissue"]:
        return "C"
    ok = (na >= FULL_SIDE and ni >= FULL_SIDE and q < Q_A and not g["cooccur"] and not g.get("anti")
          and not g.get("heavy_alert")
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


def _changed_note(v, before, now, why):
    """The note on an arrow that a rule changed in direction version v reads differently (VERSION 6): 'rule changed
    in direction version v: before, <before>; now <now>, because <why>' (no '; ' inside: _join would rewrite it)."""
    return CHANGED.format(v=v) + f": before, {before}. Now {now}, because {why}".replace("; ", ", ")


def _blocked_note(v, why):
    """'grade A blocked since direction version v: <conditions>' for an arrow that the version's stricter grade-A
    rules keep from grade A (without them it would be A)."""
    return (f"grade A blocked since direction version {v}: " + ", ".join(why)
            + " (without this rule the arrow would be grade A)").replace("; ", ", ")


def _absence(c, g, y):
    """(lines of the altered side, of them not expressing y, lines of the other side, of them not expressing y): the
    tensor's line_measured mask (tables line_effects 'expressed')."""
    na, ni = int(g["alt"].sum()), int(g["inn"].sum())
    ka = int((~c.measured[g["alt"], y]).sum()) if na else 0
    ki = int((~c.measured[g["inn"], y]).sum()) if ni else 0
    return na, ka, ni, ki


def _known_target(src, y_sym):
    """' (a known target of SRC: tahoemap/data/control_sets.json ...)' when the target is in the source's curated
    target list of this module (P53_TARGETS for TP53, NRF2_TARGETS for KEAP1), else ''."""
    sets = {"TP53": ("P53_TARGETS", P53_TARGETS), "KEAP1": ("NRF2_TARGETS", NRF2_TARGETS)}
    hit = sets.get(str(src).upper())
    if hit and str(y_sym) in hit[1]:
        return f", a known target of {src} (tahoemap/direction.py {hit[0]})"
    return ""


def _grade_null(g, na, ni, extra_c=False):
    return "B" if (na >= FULL_SIDE and ni >= FULL_SIDE and not g["tissue"] and not extra_c) else "C"


def _programme(g):
    """D10: a natural knockout inside an expression programme: more than NOTE_COABSENT_SETS other line sets overlap
    the lines lacking the gene (Jaccard >= JACCARD_CO). Returns the number of such sets (0 when none)."""
    return int(g.get("null_co_n", 0) or 0) if g["kind"] == "null" else 0


def _programme_alert(g, x_name):
    n = _programme(g)
    return (f"an expression programme: {n} other line sets overlap the lines lacking {x_name} (overlap "
            f"{JACCARD_CO:g} or more): the direction is not identifiable")


def _base_row():
    return {"source": "", "source_col": -1, "target": "", "target_col": -1, "target_dd": -1, "target_type": "gene",
            "kind": "", "grade": "", "sign": 0, "reading": "", "group": "", "mechanism": "", "n_altered": -1,
            "n_intact": -1, "n_lines": -1, "contrast": np.nan, "D_raw": np.nan, "retained_fraction": np.nan,
            "raw_share": np.nan, "rise_share": np.nan, "baseline_log2_diff": np.nan, "r": np.nan, "r_reverse": np.nan,
            "direction_clear": None, "p_direction": np.nan, "n_compounds": -1, "n_supporting": -1,
            "background_rate": np.nan, "compounds": "", "compounds_supporting": "", "drug_effect": "", "T": np.nan,
            "p": np.nan, "q": np.nan, "q_group": np.nan, "alerts": "", "top_drugdoses": "", "art_share": np.nan,
            "drugdoses_all": "",
            # VERSION 5
            "mechanism_class": "", "mechanism_source": "", "compounds_source": "", "n_top": -1, "m_top": -1,
            "class_size": -1, "share_supporting": np.nan, "ti_share": np.nan, "expected_false_group": np.nan,
            "group_edges": -1, "false_share": np.nan, "false_share_upper": np.nan, "distance_bp": np.nan,
            "same_locus": False, "programme_sets": -1, "nonspecific_share": np.nan, "allele": "",
            "doses_supporting": "", "n_doses_supporting": -1, "test_id": -1, "n_same_test": -1}


INT_COLS = ("source_col", "target_col", "target_dd", "n_altered", "n_intact", "n_lines", "n_compounds",
            "n_supporting", "sign", "n_top", "m_top", "class_size", "group_edges", "programme_sets",
            "n_doses_supporting", "test_id")
F32_COLS = ("share_supporting", "ti_share", "expected_false_group", "false_share", "false_share_upper",
            "nonspecific_share")


def _empty_edges():
    """An edges table with no rows but the column types of a filled one (str / float64 / int32 / bool)."""
    b = _base_row()
    cols = {}
    for k, v in b.items():
        if k == "direction_clear":
            cols[k] = pd.Series(dtype="boolean")
        elif isinstance(v, bool):
            cols[k] = pd.Series(dtype=bool)
        elif isinstance(v, str):
            cols[k] = pd.Series(dtype="string")
        elif k == "n_same_test":
            cols[k] = pd.Series(dtype=np.int16)
        elif isinstance(v, (int, np.integer)):
            cols[k] = pd.Series(dtype=np.int32)
        elif k in F32_COLS:
            cols[k] = pd.Series(dtype=np.float32)
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


def _source_of(c, g, x_for_alerts):
    if g["kind"] != "null":
        return g["gene"], int(g["col"])
    return str(c.sym[x_for_alerts]), int(x_for_alerts)


def _response_rows(c, g, r, kind, base_res, x_for_alerts, extra_alerts_fn=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    geno = g["kind"] == "genotype"
    src, scol = _source_of(c, g, x_for_alerts)
    prog_n = _programme(g) if not geno else 0
    prog = prog_n if prog_n > NOTE_COABSENT_SETS else 0
    nK = int(c.sel.shape[1])
    for i in hit:
        y = int(r["t"][i])
        if y == x_for_alerts:
            continue
        D = float(r["D"][i])
        Draw = float(r["D_raw"][i])
        sgn_z = float(r["dir"][i])
        table, qg, tal = _table_check(c, g, r, i, kind)
        sf = g["sign_factor"]
        sign = int(sgn_z * sf) if sf else 0
        rise = float(r["rise"][i]) if "rise" in r else np.nan
        mixed = _mixed(rise)
        items = _top_dd_response(c, g, y, sgn_z, rise)
        al = list(extra_alerts_fn(y) if extra_alerts_fn else g["alerts"])
        na, ni = int(r["na"][i]), int(r["ni"][i])
        block_a, why_a = False, []
        if na < g["n_alt"] or ni < g["n_inn"]:
            al.append(f"{c.sym[y]} measured in {na} of the {g['n_alt']} and {ni} of the {g['n_inn']} lines")
        if na < MEASURED_A * g["n_alt"] or ni < MEASURED_A * g["n_inn"]:
            block_a = True                                                    # D5 (d)
            why_a.append(f"{c.sym[y]} is measured in fewer than {MEASURED_A:.0%} of a side's lines (MEASURED_A)")
        bd = np.nan
        if base_res is not None:
            j = np.flatnonzero(base_res["t"] == y)
            bd = float(base_res["D"][j[0]]) if j.size else np.nan
        if np.isfinite(bd) and sgn_z > 0 and bd >= BASE_LOW:
            if np.isfinite(rise) and rise < 0.5:                              # D5 (c): a floor
                al.append(f"{c.sym[y]} mostly falls under these drugs and is {2 ** bd:.1f}x lower at baseline in the "
                          f"{alt_w}: a smaller fall there can be a floor (less left to lose), not less regulation")
                block_a = True
                why_a.append("a smaller fall in the altered lines can be a floor")
            else:
                al.append(f"{c.sym[y]} is {2 ** bd:.1f}x lower at baseline in the {alt_w}: a weaker response may be "
                          "lower expression")
        if r["opp"][i] >= 0.25:
            al.append(f"the difference goes the other way at some of its drug-doses ({r['opp'][i]:.0%} of the "
                      "evidence)")
        if r["opp"][i] >= BOTH_WAYS_A:                                         # D5 (b)
            block_a = True
            why_a.append(f"{BOTH_WAYS_A:.0%} or more of the evidence goes the other way (BOTH_WAYS_A)")
        if not (np.sign(D) == sgn_z and np.sign(Draw) == sgn_z):              # D5 (a)
            ret = float(r["ret"][i])
            rt = f"; the {alt_w} respond {ret:.2f}x as strongly overall" if np.isfinite(ret) else ""
            al.append(f"the mean over all {nK} of its drug-doses goes the other way (contrast {D:+.2f}, without the "
                      f"correction {Draw:+.2f}{rt}): the arrow rests on its strongest drug-doses ("
                      + ", ".join(c.dd_label[d] for d, _, _, _ in items) + ")")
            block_a = True
            why_a.append("the mean over all its drug-doses goes the other way")
        if mixed:
            al.append(_mixed_alert(c.sym[y], rise, "of the drug-doses carrying the difference"))
        cal, block = _correction_alerts(c, g, r, i, y, alt_w)
        al.extend(cal)
        if not c.sel_sig[y].any():
            al.append("none of its drug-doses is significant pooled (a response only part of the lines show)")
        if r.get("own") is not None and bool(r["own"][i]):
            al.append(f"{c.sym[y]}'s own shuffles of the labels spread differently from the other genes': its own "
                      "permutation p is used")
        dd_all, art_share, art_reason, ti_share, ti_reason = _response_all(c, g, y, sgn_z, items)
        if art_reason:
            al.append(art_reason)
        if ti_reason:
            al.append(ti_reason)
        if prog:
            al.append(_programme_alert(g, src))
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
        rd0 = rd                                                            # without the sign's words (D9)
        if prog:
            sign = 0
            rd += (f"; {src} belongs to an expression programme ({prog} other line sets overlap the lines lacking it; "
                   "genes co-expressed across lines): which gene of it acts cannot be told")
        elif geno:
            aw = _activity_words(sign, f"{_actor(g)} activity", response=True)
            if aw:
                rd += f"; {aw} {c.sym[y]}'s drug response"
        elif sign:
            rd += f" ({src} {_may(sign, response=True)} its drug response)"
        if geno:
            grade = _grade_genotype(g, na, ni, float(r["q"][i]), block or block_a)
            why5 = why_a + (["heavily mutated lines are concentrated on the altered side"] if g.get("heavy_alert")
                            else [])
            if table and grade != "A" and why5 and _grade_genotype(dict(g, heavy_alert=False), na, ni,
                                                                   float(r["q"][i]), block) == "A":
                al.append(_blocked_note(5, why5))                              # what the version 5 rules blocked
        else:
            grade = _grade_null(g, na, ni, block or bool(prog))
            if prog and table and int(sgn_z * sf if sf else 0):
                al.append(_changed_note(5, f"this arrow had sign {int(sgn_z * sf):+d} and grade "
                                        f"{_grade_null(g, na, ni, block)}", "sign 0 and grade C",
                                        f"{src} belongs to an expression programme (more than {NOTE_COABSENT_SETS} "
                                        "other line sets overlap): which gene acts cannot be told"))
        grade = grade if table else "C"
        row.update({"source": src, "source_col": scol,
                    "target": str(c.sym[y]), "target_col": y, "kind": kind, "grade": grade, "sign": sign,
                    "reading": rd, "group": g["desc"], "mechanism": MECH_WORDS[g["mech"]], "n_altered": na,
                    "n_intact": ni, "contrast": D, "D_raw": Draw,
                    "retained_fraction": float(r["ret"][i]), "raw_share": float(r["raw_share"][i]),
                    "rise_share": rise,
                    "baseline_log2_diff": bd, "T": float(r["T"][i]), "p": float(r["p"][i]), "q": float(r["q"][i]),
                    "q_group": qg, "alerts": _join(al), "top_drugdoses": top, "art_share": art_share,
                    "drugdoses_all": dd_all, "ti_share": ti_share, "allele": g.get("allele", ""),
                    "programme_sets": prog_n if not geno else -1, "_rd0": rd0})
        rows.append(row)
    return rows


def _baseline_rows(c, g, r, kind, x_for_alerts, extra_alerts_fn=None, coabsent=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    geno = g["kind"] == "genotype"
    src, scol = _source_of(c, g, x_for_alerts)
    prog_n = _programme(g) if not geno else 0
    prog = prog_n if prog_n > NOTE_COABSENT_SETS else 0
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
        near_co, block_abs, notes6 = False, False, []
        if geno:                                                               # VERSION 6: where the target is absent
            n_a, k_a, n_i, k_i = _absence(c, g, y)
            block_abs = k_a >= BASE_ABSENT_A * max(n_a, 1) or k_i >= BASE_ABSENT_A * max(n_i, 1)
        if co and geno:                                                        # D9: genotype co-absence
            ca, cb = _coord(c, -1 if scol is None else scol, src), _coord(c, y, c.sym[y])
            dist = _gap(ca, cb)
            if ca is None or cb is None:                                       # no coordinates: as in version 5
                near_co = True
                al.append(f"{c.sym[y]} is also absent from most of the {alt_w}: a shared deletion can explain it "
                          "(no coordinates to check how far apart the two genes lie)")
            elif np.isfinite(dist) and dist <= CODELETION_BP:
                near_co = True
                al.append(f"{c.sym[y]} is also absent from most of the {alt_w} and lies {_bp_words(dist)} from "
                          f"{src}: a shared deletion can explain it")
            else:
                where = f"{_bp_words(dist)} apart" if np.isfinite(dist) else "on different chromosomes"
                al.append(f"{c.sym[y]} is also absent from most of the {alt_w} ({k_a} of the {n_a}, and {k_i} of the "
                          f"{n_i} others){_known_target(src, c.sym[y])}: lineage, or the loss of {src} itself, can "
                          f"explain it (the two genes lie {where}: not one shared deletion)")
                notes6.append(_changed_note(6, "version 5 graded every target absent from most altered lines C "
                                            "and read it as a shared deletion", "the grade stays (at most B)",
                                            f"a shared deletion needs the two genes within {_bp_words(CODELETION_BP)} "
                                            "of each other on one chromosome"))
        if block_abs and not co:
            al.append(f"{c.sym[y]} is not expressed in {k_a} of the {n_a} {alt_w} and {k_i} of the {n_i} others: "
                      "present in some lines and absent in others, so the level difference can follow lineage "
                      "rather than regulation")
        elif co and not geno:
            al.append(f"{c.sym[y]} is also absent from most of these lines: which of the two drives the other cannot "
                      "be told")
        if r.get("own") is not None and bool(r["own"][i]):
            al.append(f"{c.sym[y]}'s own shuffles of the labels spread differently from the other genes': its own "
                      "permutation p is used")
        if prog:
            al.append(_programme_alert(g, src))
        fold = _fmt_fold(2 ** abs(D))
        rd0 = f"{c.sym[y]} is {fold} {'lower' if D > 0 else 'higher'} at baseline in the {alt_w} than in {inn_w}"
        if geno:
            rd = f"{c.sym[y]} is {fold} {'lower' if D > 0 else 'higher'} at baseline in the {alt_w} than in {inn_w}"
            aw = _activity_words(sign, f"{_actor(g)} activity")
            if aw:
                rd += f"; {aw} {c.sym[y]}'s level"
        elif prog:
            sign = 0
            rd = (f"{c.sym[y]} is {fold} {'lower' if D > 0 else 'higher'} at baseline in the {alt_w} than in {inn_w}; "
                  f"these lines also lack the genes of {prog} other line sets (a shared expression programme): {src} "
                  f"and {c.sym[y]} are co-expressed across lines, and which acts on which cannot be told")
        else:
            rd = (f"{alt_w} have {fold} {'less' if D > 0 else 'more'} {c.sym[y]} at baseline than {inn_w}"
                  + (f" ({src} {_may(sign)} {c.sym[y]}'s level)" if sign else ""))
        na, ni = int(r["na"][i]), int(r["ni"][i])
        if geno:
            grade = _grade_genotype(g, na, ni, float(r["q"][i]), block_abs)
            if table and grade != "A" and block_abs and _grade_genotype(g, na, ni, float(r["q"][i])) == "A":
                notes6.append(_blocked_note(6, [f"{c.sym[y]} is not expressed in {BASE_ABSENT_A:.0%} or more of a "
                                                "side's lines (BASE_ABSENT_A)"]))
            if table and grade != "A" and g.get("heavy_alert") and _grade_genotype(
                    dict(g, heavy_alert=False), na, ni, float(r["q"][i]), block_abs) == "A":
                notes6.append(_blocked_note(5, ["heavily mutated lines are concentrated on the altered side"]))
            if co and near_co:
                grade = "C"
            al.extend(notes6)
        else:
            grade = _grade_null(g, na, ni, co or bool(prog))
        grade = grade if table else "C"
        row = _base_row()
        row.update({"source": src, "source_col": scol,
                    "target": str(c.sym[y]), "target_col": y, "kind": kind, "grade": grade, "sign": sign,
                    "reading": rd, "group": g["desc"], "mechanism": MECH_WORDS[g["mech"]], "n_altered": na,
                    "n_intact": ni, "contrast": D, "baseline_log2_diff": D, "T": float(r["T"][i]),
                    "p": float(r["p"][i]), "q": float(r["q"][i]), "q_group": qg, "alerts": _join(al),
                    "allele": g.get("allele", ""), "programme_sets": prog_n if not geno else -1, "_rd0": rd0})
        rows.append(row)
    return rows


def _sens_rows(c, g, r, kind, x_for_alerts, extra_alerts_fn=None):
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    geno = g["kind"] == "genotype"
    src, scol = _source_of(c, g, x_for_alerts)
    prog_n = _programme(g) if not geno else 0
    prog = prog_n if prog_n > NOTE_COABSENT_SETS else 0
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
        if prog:
            al.append(_programme_alert(g, src))
        mi = _nanmean_side(c.Aab[d], g["inn"])
        ma = _nanmean_side(c.Aab[d], g["alt"])
        rd = f"cells under {c.dd_label[d]}: {_fmt_fold(2 ** ma)} in the {alt_w} vs {_fmt_fold(2 ** mi)} in " \
             f"{inn_w} (relative to the other lines in the same wells)"
        if prog:
            sign = 0
            rd += (f"; {src} belongs to an expression programme ({prog} other line sets overlap the lines lacking it; "
                   "genes co-expressed across lines): any gene of it, or the lineage, can set the cells' numbers")
        elif geno and sign:
            rd += f"; {_actor(g)} activity {'protects the cells' if sign > 0 else 'makes the cells more sensitive'}"
        elif sign:
            rd += f" ({src} {_may(sign, cells=True)})"
        na, ni = int(r["na"][i]), int(r["ni"][i])
        grade = _grade_genotype(g, na, ni, float(r["q"][i])) if geno else _grade_null(g, na, ni, bool(prog))
        grade = grade if table else "C"
        row = _base_row()
        row.update({"source": src, "source_col": scol,
                    "target": f"cells under {c.dd_label[d]}", "target_dd": d, "target_type": "cells",
                    "kind": kind, "grade": grade, "sign": sign, "reading": rd, "group": g["desc"],
                    "mechanism": MECH_WORDS[g["mech"]], "n_altered": na, "n_intact": ni, "contrast": D,
                    "T": float(r["T"][i]), "p": float(r["p"][i]), "q": float(r["q"][i]), "q_group": qg,
                    "alerts": _join(al), "allele": g.get("allele", ""), "programme_sets": prog_n if not geno else -1,
                    "top_drugdoses": c.dd_label[d], "drugdoses_all": c.dd_label[d] + _flags_text(c, d)})
        rows.append(row)
    return rows


def _dose_words(c, d):
    """'5 µM' of a drug-dose (its dose alone, for 'also at ... 5 µM')."""
    s = str(c.dose[d]).strip()
    return f"{s} µM" if s and s != "nan" else c.dd_label[d]


def _sel_doses(c, g, full, d):
    """D13 dose consistency of a selectivity edge at drug-dose d: the compound's other drug-doses and their result in
    this group (full: {drug-dose: (p, q of the edge's family)}; q_group for a genotype group, q for a natural
    knockout). Returns (doses with q < Q_SIG besides d, the others' (dose, p) or None when not tested)."""
    comp = c.salt[d]
    same = [int(x) for x in np.flatnonzero(c.salt == comp) if int(x) != d]
    sup, other = [], []
    for x in sorted(same, key=lambda x_: float(c.dd["conc"].iloc[x_]) if "conc" in c.dd else x_):
        p_, q_ = full.get(x, (np.nan, np.nan))
        if np.isfinite(q_) and q_ < Q_SIG:
            sup.append((x, q_))
        else:
            other.append((x, p_))
    return sup, other


def _sel_rows(c, g, r, kind, x_for_alerts, full, extra_alerts_fn=None):
    """D13: selectivity edges - how strongly the lines respond to a drug-dose (rel_log2 of tables/
    drug_line_response: genes beyond the per-line cut against the line's typical drug-dose) differs between the
    sides. Target 'response to DRUG DOSE' (target_type 'response'). Dose consistency per compound: the other doses
    with q (q_group for a genotype group) < Q_SIG are support ('also at ...'); none: 'one dose only' (an alert; no
    grade A)."""
    rows = []
    hit = _hits(r)
    alt_w, inn_w = _sides(g)
    geno = g["kind"] == "genotype"
    src, scol = _source_of(c, g, x_for_alerts)
    prog_n = _programme(g) if not geno else 0
    prog = prog_n if prog_n > NOTE_COABSENT_SETS else 0
    for i in hit:
        d = int(r["t"][i])
        D = float(r["D"][i])
        sf = g["sign_factor"]
        sign = int(np.sign(D) * sf) if sf else 0
        table, qg, tal = _table_check(c, g, r, i, kind)
        al = ([tal] if tal else []) + list(extra_alerts_fn(None) if extra_alerts_fn else g["alerts"])
        if r.get("own") is not None and bool(r["own"][i]):
            al.append("this drug-dose's own shuffles of the labels spread differently from the other drug-doses': its "
                      "own permutation p is used")
        sup, other = _sel_doses(c, g, full, d)
        one = not sup
        if sup:
            al.append(f"also at {c.drug[d]} " + " and ".join(f"{_dose_words(c, x)} (q {_q2(q_)})" for x, q_ in sup))
        else:
            nw = int(c.n_wells[d])
            wtxt = "is a single well" if nw == 1 else (f"rests on {nw} wells" if nw > 1 else "has no well count")
            tested = [(x, p_) for x, p_ in other if np.isfinite(p_)]
            untested = [x for x, p_ in other if not np.isfinite(p_)]
            oth = []
            if tested:
                oth.append("its other doses do not show it (" + ", ".join(
                    f"p {p_:.2g} at {_dose_words(c, x)}" for x, p_ in tested) + ")")
            if untested:
                oth.append("not tested at " + ", ".join(_dose_words(c, x) for x in untested)
                           + " (no line responds selectively there)")
            al.append(f"one dose only: {c.dd_label[d]} {wtxt}" + ("; " + "; ".join(oth) if oth else ""))
        if prog:
            al.append(_programme_alert(g, src))
        na_ = np.where(g["alt"] & np.isfinite(c.Rsel[d]) & (c.Nsel[d] >= 0), c.Nsel[d], -1)
        ni_ = np.where(g["inn"] & np.isfinite(c.Rsel[d]) & (c.Nsel[d] >= 0), c.Nsel[d], -1)
        ma = float(np.median(na_[na_ >= 0])) if (na_ >= 0).any() else np.nan
        mi = float(np.median(ni_[ni_ >= 0])) if (ni_ >= 0).any() else np.nan
        how = "more" if D < 0 else "less"
        rd = (f"the {alt_w} respond {how} strongly to {c.dd_label[d]} than {inn_w} (median {ma:.0f} vs {mi:.0f} genes "
              "beyond the per-line cut)")
        if prog:
            sign = 0
            rd += (f"; {src} belongs to an expression programme ({prog} other line sets overlap the lines lacking it; "
                   "genes co-expressed across lines): any gene of it, or the lineage, can set the response")
        elif geno and sign:
            rd += f"; {_actor(g)} activity {'strengthens' if sign > 0 else 'weakens'} the response"
        elif sign:
            rd += f" ({src} {_may(sign, response=True)} the response)"
        na, ni = int(r["na"][i]), int(r["ni"][i])
        if geno:
            grade = _grade_genotype(g, na, ni, float(r["q"][i]), one)
        else:
            grade = _grade_null(g, na, ni, bool(prog))
        grade = grade if table else "C"
        row = _base_row()
        row.update({"source": src, "source_col": scol,
                    "target": f"response to {c.dd_label[d]}", "target_dd": d, "target_type": "response",
                    "kind": kind, "grade": grade, "sign": sign, "reading": rd, "group": g["desc"],
                    "mechanism": MECH_WORDS[g["mech"]], "n_altered": na, "n_intact": ni, "contrast": D,
                    "T": float(r["T"][i]), "p": float(r["p"][i]), "q": float(r["q"][i]), "q_group": qg,
                    "alerts": _join(al), "allele": g.get("allele", ""), "programme_sets": prog_n if not geno else -1,
                    "doses_supporting": "; ".join(f"{c.dd_label[x]} (q {_q2(q_)})" for x, q_ in sup),
                    "n_doses_supporting": len(sup) + 1,
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
    c.level_tested = (xi[ok], yi[ok])                            # D14: the directed pairs tested
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

    per_gene = np.zeros(gk.size, dtype=np.int64)

    def scan(X, count=False):
        """(tests per drug-dose, candidates: gene idx, drug-dose idx, r, n, T, p with p < Q_SIG); count: the tests
        per gene too (D14)"""
        m, out = np.zeros(ds.size, dtype=np.int64), []
        for b0 in range(0, ds.size, LEVEL_BLOCK):
            b1 = min(ds.size, b0 + LEVEL_BLOCK)
            r, n = _corr_genes_dd(X, Ar[b0:b1])
            dof = n - k_cov - 1
            ok = (n >= LEVEL_MIN_LINES) & (dof >= 3) & np.isfinite(r)
            m[b0:b1] = ok.sum(axis=0)
            if count:
                per_gene[:] += ok.sum(axis=1)
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
    m, (gi, dj, r, n, T, p) = scan(Xg, count=True)
    c.levsens_tested = {int(gk[i]): int(per_gene[i]) for i in np.flatnonzero(per_gene)}
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
# drug_target BH family (as before version 5): a (class, direction, gene) test counts where >= 2 compounds of the screen
# move the gene that way (elsewhere no labelling of the compounds can give >= 2: p would be 1 whatever the class).
# True: every gene (p = 1 where fewer than 2 compounds move it) - how the reviewers' numbers were made (50,970 real
# edges); on the synthetic data it leaves no drug_target arrow without ChEMBL (docs/direction.md). Kept for the proxy.
DT_BH_ALL = False
DT_DEDUP = False               # True: each distinct test once (the same compounds for several targets); not used


def _compounds(c):
    """One compound = one molecule: names that differ only in letter case or a trailing salt word ('Ixazomib' /
    'Ixazomib citrate', 'crizotinib' / 'Crizotinib (hydrochloride)') count once; its names, ' / '-joined, name it.
    Returns (compound names, compound of each drug-dose, the Tahoe drug names of each compound)."""
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
    drugs_of = [sorted({str(c.drug[d]) for d in np.flatnonzero(comp_of == k)}) for k in range(len(comps))]
    return comps, comp_of, drugs_of


def _chembl_targets(c, drugs):
    """ChEMBL's targets of a compound (its Tahoe drug names): {GENE: (directions {'up', 'down', ''}, mechanism texts,
    action types)} from mechanisms.drug_mechanisms (target_genes, action_type through mechanisms.action_direction)."""
    out = {}
    m = c.mech
    if m is None or not len(m):
        return out
    sub = m[m["drug"].astype(str).isin(drugs)]
    if "target_type" in sub:                     # a complex's subunits are not each a target (CHEMBL_MEMBER_TYPES)
        sub = sub[sub["target_type"].fillna("").astype(str).str.upper().isin(CHEMBL_MEMBER_TYPES)]
    for genes, act, text in zip(sub["target_genes"].fillna("").astype(str), sub["action_type"].fillna("").astype(str),
                                sub["mechanism_of_action"].fillna("").astype(str)):
        for gname in [x.strip().upper() for x in genes.split(",") if x.strip()]:
            dirs, texts, acts = out.setdefault(gname, (set(), [], []))
            dirs.add(MX.action_direction(act))
            if text and text not in texts:
                texts.append(text)
            if act and act.lower() not in acts:
                acts.append(act.lower())
    return out


def _chembl_action(dirs):
    d = {x for x in dirs if x}
    if d == {"up"}:
        return "activator"
    if d == {"down"}:
        return "inhibitor"
    return "unclear"


def _memberships(c, comps, comp_of, drugs_of):
    """D4: per compound k, its (target, action, source words) from Tahoe (targets, moa_broad as before) and ChEMBL
    (drug_mechanisms target_genes, action_type): one source lists the target - its action, labelled; Tahoe 'unclear'
    and ChEMBL gives one - ChEMBL's ('action from ChEMBL'); both give different actions - 'unclear', with an alert;
    and the disagreements of the compound's two annotations (texts for the alerts). Returns (members: list of
    {target: (action, words)}, tahoe target sets, ChEMBL target dicts, alerts: list of {target: [texts]})."""
    dd = c.dd
    tcol = "targets" if "targets" in dd else None
    mcol = next((x for x in ("moa_broad", "moa-broad") if x in dd), None)
    nC = len(comps)
    t_tg = [[] for _ in range(nC)]
    t_act = ["unclear"] * nC
    for d in range(c.Dn):
        k = comp_of[d]
        if tcol:
            for t in _split_targets(dd[tcol].iloc[d]):
                if t not in t_tg[k]:
                    t_tg[k].append(t)
        if mcol and t_act[k] == "unclear":
            t_act[k] = _moa_class(dd[mcol].iloc[d])
    members, chem, alerts = [], [], []
    for k in range(nC):
        ch = _chembl_targets(c, drugs_of[k])
        chem.append(ch)
        mem, al = {}, {}
        tset = set(t_tg[k])
        ch_names = sorted(ch)
        for t in list(dict.fromkeys(t_tg[k] + ch_names)):
            in_t, in_c = t in tset, t in ch
            if in_t and in_c:
                ca = _chembl_action(ch[t][0])
                if t_act[k] == "unclear" and ca != "unclear":
                    mem[t] = (ca, "Tahoe target, action from ChEMBL")
                elif ca == "unclear" or ca == t_act[k]:
                    mem[t] = (t_act[k], "Tahoe and ChEMBL")
                else:
                    mem[t] = ("unclear", "Tahoe and ChEMBL, actions differ")
                    al.setdefault(t, []).append(
                        f"{comps[k]}: Tahoe and ChEMBL give different actions on {t} (Tahoe: {t_act[k]}, ChEMBL: "
                        f"{', '.join(ch[t][2]) or 'no action type'}): counted as unclear")
            elif in_t:
                mem[t] = (t_act[k], "Tahoe")
            else:
                mem[t] = (_chembl_action(ch[t][0]), f"ChEMBL ({', '.join(ch[t][1]) or 'no mechanism text'})")
            if t_tg[k] and ch and (in_t != in_c):                  # the two annotations list different targets
                acts = sorted({x for v in ch.values() for x in v[2]})
                al.setdefault(t, []).append(
                    f"{comps[k]}: Tahoe lists {', '.join(t_tg[k])} ({t_act[k]}); ChEMBL lists {', '.join(ch_names)} "
                    f"({', '.join(acts) or 'no action type'})")
        members.append(mem)
        alerts.append(al)
    return members, t_tg, chem, alerts


def _class_key(c, drugs, t, action):
    """D1: the class of (compound, target): a 'trap' class (mechanisms.trap_class: TOP1 / TOP2 poisons, PARP trappers,
    microtubule stabilisers) - sign not inferred -; tubulin destabilisers apart ('inhibitor (microtubule
    destabiliser)'); else the action (inhibitor / activator / unclear). Returns (key, class key of mechanisms or '')."""
    keys = []
    for d in drugs:
        for k_ in c.cls_by_drug.get(d, []):
            if k_ not in keys:
                keys.append(k_)
    tc = MX.trap_class(keys, t)
    if tc:
        return TRAP_NAMES.get(tc, (MX.class_info(tc).get("label", tc).split(" (")[0],))[0], tc
    if MX.DESTAB in keys and MX._targets_match(MX.class_info(MX.DESTAB).get("targets"), t):
        return DESTAB_CLASS, MX.DESTAB
    return action, ""


def _class_members_src(c, drugs_of, ks, cls_key, comps):
    """mechanism_source: per compound of a trap or destabiliser class, its membership's sources ('Amsacrine: code
    constant (...), ChEMBL 37: DNA topoisomerase II inhibitor (CHEMBL...)')."""
    if not cls_key:
        return ""
    out = []
    for k in ks:
        src = [c.cls_src.get((d, cls_key), "") for d in drugs_of[k]]
        src = [x.replace("; ", ", ") for x in dict.fromkeys(src) if x]
        out.append(f"{comps[k]}: {', '.join(src) or 'class of the reference stage'}")
    return "; ".join(out)


def _class_effects(c, drugs, effect):
    """[(label, source)] of the compound's classes with this effect ('dna', 'translation')."""
    out = []
    for d in drugs:
        for k_ in c.cls_by_drug.get(d, []):
            info = MX.class_info(k_)
            if info.get("effect") == effect:
                out.append((info.get("label", k_), c.cls_src.get((d, k_), "").replace("; ", ", ")))
    return list(dict.fromkeys(out))


def topj_p(mm, kk, N, nC):
    """D3, the top-j test of one class and direction for a set of genes. mm (N x genes): for each compound of the class,
    M = how many compounds of the screen move the gene at least as strongly (ties counted), nC + 1 where the compound is
    not significant that way; kk: the class's compounds significant that way (>= 2); N the class's compounds, nC the
    screen's. For j = 2..kk, m_j = the j-th smallest M among the significant ones and p_j = the hypergeometric chance
    that >= j of the N class compounds fall among the m_j strongest of the nC; p = min(1, (N - 1) x min_j p_j)
    (Bonferroni over the thresholds). Returns (p, j*, m_j*)."""
    mm = np.sort(np.asarray(mm), axis=0)
    kk = np.asarray(kk)
    n = kk.size
    best = np.ones(n)
    bj = np.zeros(n, dtype=np.int32)
    bm = np.zeros(n, dtype=np.int32)
    for j in range(2, int(N) + 1):
        ok = kk >= j
        if not ok.any():
            break
        mj = mm[j - 1]
        pj = np.ones(n)
        pj[ok] = stats.hypergeom.sf(j - 1, nC, mj[ok], N)
        better = pj < best
        best = np.where(better, pj, best)
        bj = np.where(better, j, bj)
        bm = np.where(better, mj, bm)
    return np.minimum(1.0, best * (N - 1)), bj, bm


def _dt_defaults(c):
    """The VERSION 5 inputs of _drug_target, empty when a caller's context lacks them (no classes, no ChEMBL)."""
    for k_, v in (("cls_by_drug", {}), ("cls_src", {}), ("chembl", False), ("ti_src_by_drug", {})):
        if not hasattr(c, k_):
            setattr(c, k_, v)
    if not hasattr(c, "mech"):
        c.mech = pd.DataFrame(columns=MX.MECH_COLUMNS)
    if not hasattr(c, "ti_dd"):
        c.ti_dd = np.zeros(c.Dn, dtype=bool)
    if not hasattr(c, "drug"):
        c.drug = c.dd["drug"].astype(str).to_numpy(dtype=object)


def _drug_target(c):
    """Edges 'compounds annotated to inhibit / activate X raise / lower Y' (module docstring, 4; VERSION 5: the top-j
    test, poison classes, ChEMBL memberships). Returns (rows, n_tests)."""
    from scipy.stats import rankdata
    _dt_defaults(c)
    comps, comp_of, drugs_of = _compounds(c)
    nC = len(comps)
    members, t_tg, chem, dis_alerts = _memberships(c, comps, comp_of, drugs_of)
    by_t, cls_of = {}, {}
    for k in range(nC):
        for t, (action, _w) in members[k].items():
            key, ckey = _class_key(c, drugs_of[k], t, action)
            by_t.setdefault((t, key), []).append(k)
            cls_of[(t, key)] = ckey
    c.dt_classes = {f"{t} ({key})": len(ks) for (t, key), ks in sorted(by_t.items()) if len(ks) >= 2}
    c.dt_class_members = {f"{t} ({key})": [comps[k] for k in ks] for (t, key), ks in sorted(by_t.items())}
    up = np.zeros((nC, c.gK), dtype=bool)
    dn = np.zeros((nC, c.gK), dtype=bool)
    np.logical_or.at(up, comp_of, c.sig_up)
    np.logical_or.at(dn, comp_of, c.sig_dn)
    # E: each compound's strongest pooled z that way over its drug-doses (NaN -> -inf); M: how many compounds move
    # the gene at least as strongly (ties counted)
    Zf = np.where(np.isfinite(c.Zp), c.Zp, -np.inf).astype(np.float32)
    Zn = np.where(np.isfinite(c.Zp), -c.Zp, -np.inf).astype(np.float32)
    E = {"up": np.full((nC, c.gK), -np.inf, np.float32), "down": np.full((nC, c.gK), -np.inf, np.float32)}
    for k in range(nC):
        ds = np.flatnonzero(comp_of == k)
        E["up"][k] = Zf[ds].max(axis=0)
        E["down"][k] = Zn[ds].max(axis=0)
    del Zf, Zn
    M = {dr: rankdata(-E[dr], axis=0, method="max").astype(np.int32) for dr in ("up", "down")}
    SIG = {"up": up, "down": dn}
    K = {"up": up.sum(axis=0), "down": dn.sum(axis=0)}
    tests = []
    for (t, key), ks in sorted(by_t.items()):
        N = len(ks)
        if N < 2:
            continue
        for dr in ("up", "down"):
            S = SIG[dr][ks]
            kk = S.sum(axis=0)
            p = np.ones(c.gK)
            if not DT_BH_ALL:                    # a gene fewer than 2 compounds of the screen move that way: no test
                p[K[dr] < 2] = np.nan
            bj = np.zeros(c.gK, dtype=np.int32)
            bm = np.zeros(c.gK, dtype=np.int32)
            cand = np.flatnonzero(kk >= 2)
            if cand.size:
                p[cand], bj[cand], bm[cand] = topj_p(np.where(S[:, cand], M[dr][ks][:, cand], nC + 1), kk[cand],
                                                     N, nC)
            tests.append((t, key, ks, dr, kk, p, bj, bm))
    c.dt_tests = tests
    if not tests:
        return [], 0
    # BH over every test (DT_DEDUP: a test repeated for several targets - the same compounds - counted once)
    if DT_DEDUP:
        first = {}
        for i, x in enumerate(tests):
            first.setdefault((tuple(sorted(x[2])), x[3]), i)
        uniq = sorted(set(first.values()))
        upos = {i: j for j, i in enumerate(uniq)}
        uq = _bh(np.concatenate([tests[i][5] for i in uniq]))
        qs = [uq[upos[first[(tuple(sorted(x[2])), x[3])]] * c.gK:(upos[first[(tuple(sorted(x[2])), x[3])]] + 1) * c.gK]
              for x in tests]
        allp = np.concatenate([tests[i][5] for i in uniq])
    else:
        allp = np.concatenate([x[5] for x in tests])
        allq = _bh(allp)
        qs = [allq[i * c.gK:(i + 1) * c.gK] for i in range(len(tests))]
    rows = []
    for (t, key, ks, dr, kk, p, bj, bm), q in zip(tests, qs):
        hit = np.flatnonzero(np.isfinite(q) & (q < Q_SIG) & (kk >= 2))
        for y in hit:
            if str(c.sym[y]).upper() == t:
                continue
            rows.append(_dt_row(c, t, key, cls_of[(t, key)], ks, dr, int(y), kk, p, q, bj, bm, comps, comp_of,
                                drugs_of, members, t_tg, chem, dis_alerts, M, K, nC))
    return rows, int(np.isfinite(allp).sum())


def _dt_row(c, t, key, ckey, ks, dr, y, kk, p, q, bj, bm, comps, comp_of, drugs_of, members, t_tg, chem,
            dis_alerts, M, K, nC):
    """One drug_target edge (VERSION 5)."""
    up = dr == "up"
    SIG = c.sig_up if up else c.sig_dn
    sup = [k for k in ks if SIG[comp_of == k, y].any()]
    sup = sorted(sup, key=lambda k: (int(M[dr][k, y]), sup.index(k)))      # strongest first
    j, m = int(bj[y]), int(bm[y])
    top, rest = sup[:j], sup[j:]
    N = len(ks)
    lf = []
    for k in top:
        v = c.lfc_p[comp_of == k, y]
        v = v[np.isfinite(v)]
        if v.size:
            lf.append(float(v.max() if up else v.min()))
    contrast = float(np.median(lf)) if lf else np.nan
    raise_w = "raise" if up else "lower"
    bg = float(K[dr][y] / nC)
    topj = (f"{int(kk[y])} of {N} compounds, {'all ' + str(j) if j == int(kk[y]) else f'{j} of them'} among the {m} of "
            f"{nC} compounds that {raise_w} it most (median {_fmt_fold(2 ** contrast)}; {bg:.0%} of all compounds "
            f"{raise_w} it)")
    names = [comps[k] for k in ks]
    sign = 0
    if key in ("inhibitor", DESTAB_CLASS):
        sign = -1 if up else 1
    elif key == "activator":
        sign = 1 if up else -1
    act = "" if not sign else f" ({t} activity may {'raise' if sign > 0 else 'lower'} it)"
    if ckey and MX.class_info(ckey).get("effect") == "trap":
        tn = TRAP_NAMES.get(ckey, (key, key + "s"))
        verb = (MX.class_info(ckey).get("verb") or "act on {target}").format(target=t)
        cause = TRAP_CAUSE.get(ckey, ("the damage they cause", "", ""))[0]
        rd = (f"compounds that {verb} ({tn[1]}: {', '.join(names)}) {raise_w} {c.sym[y]} ({topj}): an effect of "
              f"{cause}, not of less {t} activity")
        grade = "C"
    elif key == DESTAB_CLASS:
        rd = f"compounds annotated to inhibit {t} (microtubule destabilisers) {raise_w} {c.sym[y]}: {topj}{act}"
        grade = "B"
    elif key == "inhibitor":
        rd = f"compounds annotated to inhibit {t} {raise_w} {c.sym[y]}: {topj}{act}"
        grade = "B"
    elif key == "activator":
        rd = f"compounds annotated to activate {t} {raise_w} {c.sym[y]}: {topj}{act}"
        grade = "B"
    else:
        rd = f"compounds annotated to target {t} {raise_w} {c.sym[y]}: {topj}"
        grade = "B"
    al = [DRUG_ALERT, f"consistent across {len(sup)} compounds ({', '.join(comps[k] for k in sup)})"]
    tg_all = [set(t_tg[k]) | set(chem[k]) for k in sup]
    share = set.intersection(*tg_all) - {t} if tg_all else set()
    if share:
        al.append(f"the supporting compounds also share {', '.join(sorted(share))}: "
                  f"{'it' if len(share) == 1 else 'any of them'} could be the cause instead")
    if key == "unclear":
        al.append("the compounds' mechanism (inhibitor or activator) is not recorded: sign not inferred")
    if ckey and MX.class_info(ckey).get("effect") == "trap":
        tn = TRAP_NAMES.get(ckey, (key, key + "s"))
        _c, how, follows = TRAP_CAUSE.get(ckey, ("", "they act on {t}", "the target follows them"))
        al.append(f"the compounds are {tn[1]} ({MX.class_info(ckey).get('source', '')}): {how.format(t=t)}, so "
                  f"{follows}, not a loss of {t} activity; the sign of {t}'s own effect is not inferred")
        old = -1 if up else 1                                  # version 4 read them as inhibitors of the target
        al.append(_changed_note(5, f"these compounds were read as inhibitors of {t}: '{t} activity "
                                f"{'lowers' if old < 0 else 'raises'} {c.sym[y]}' (sign {old:+d}, grade B)",
                                "the sign is not inferred (sign 0, grade C)",
                                f"{tn[1]} act through {TRAP_CAUSE.get(ckey, ('the damage they cause',))[0]}, not "
                                f"through less {t}"))
    dna = [(comps[k], _class_effects(c, drugs_of[k], "dna")) for k in sup]
    dna = [(nm, ef) for nm, ef in dna if ef]
    if dna:
        al.append(f"{', '.join(nm for nm, _ in dna)} also act on DNA directly (" + ", ".join(
            f"{nm}: " + ", ".join(f"{lab} ({src})" if src else lab for lab, src in ef) for nm, ef in dna)
            + "): the change can follow DNA damage rather than the listed target")
    if j == 2:
        al.append(f"supported by 2 compounds only ({', '.join(comps[k] for k in top)}): shared chemistry or another "
                  "shared target can explain it")
    for k in ks:
        al.extend(dis_alerts[k].get(t, []))
    tops, flagged, every, best = [], [], [], (-1.0, -1)
    for k in sup:
        ds = np.flatnonzero((comp_of == k) & SIG[:, y])
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
    ti = [k for k in sup if any(c.ti_dd[d] for d in np.flatnonzero(comp_of == k))]
    if sup and len(ti) == len(sup):                                           # D17: every supporting compound
        tdd = [int(d) for k in sup for d in np.flatnonzero((comp_of == k) & SIG[:, y]) if c.ti_dd[d]]
        al.append(_ti_reason(c, [c.dd_label[d] for d in tdd], 1.0, True, [str(c.drug[d]) for d in tdd]))
    words = {"inhibitor": "inhibitors", "activator": "activators", "unclear": "compounds of unclear action",
             DESTAB_CLASS: "microtubule destabilisers (inhibitors)"}
    gname = TRAP_NAMES[ckey][1] if ckey in TRAP_NAMES else words.get(key, key)
    csrc = "; ".join(f"{comps[k]}: {members[k][t][1]}" for k in ks) if c.chembl else ""
    mcl = TRAP_NAMES[ckey][0] if ckey in TRAP_NAMES else ("microtubule destabiliser" if key == DESTAB_CLASS else "")
    sup_txt = "; ".join(comps[k] for k in top) + (f"; also significant: {', '.join(comps[k] for k in rest)}"
                                                    if rest else "")
    row = _base_row()
    row.update({"source": t, "source_col": c.col_of.get(t, -1), "target": str(c.sym[y]), "target_col": int(y),
                "kind": "drug_target", "grade": grade, "sign": sign, "reading": rd,
                "group": f"{t} {gname}: {', '.join(names)} ({N} compounds)", "mechanism": key,
                "n_compounds": N, "n_supporting": int(kk[y]), "background_rate": bg,
                "compounds": "; ".join(names), "compounds_supporting": sup_txt,
                "drug_effect": "raises" if up else "lowers", "contrast": contrast, "p": float(p[y]),
                "q": float(q[y]), "alerts": _join(al), "top_drugdoses": "; ".join(tops),
                "drugdoses_all": "; ".join(every), "mechanism_class": mcl,
                "mechanism_source": _class_members_src(c, drugs_of, ks, ckey, comps), "compounds_source": csrc,
                "n_top": j, "m_top": m, "class_size": N, "share_supporting": float(kk[y] / N)})
    return row


def _molecule_key(name):
    """A compound's molecule (mechanisms.molecule_key, case-folded): its salt base (tlib.salt_base: a trailing
    bracketed salt removed) with trailing salt and hydrate words removed (mechanisms.SALT_WORDS; 'Ixazomib citrate'
    -> 'ixazomib', 'Crizotinib (hydrochloride)' -> 'crizotinib'). '(S)-Crizotinib' stays apart (another molecule)."""
    return molecule_key(name).casefold()


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


GENO_KINDS = ("response", "baseline", "sensitivity", "selectivity")
EXPECTED_FALSE_HOW = (
    "expected_false: the controls' estimate of the false edges among the written ones; expected_false_upper: its 95% "
    "upper bound (Poisson: the controls are a small sample - 0 edges in 60 pseudo-groups still allows about 3 per 60 "
    "groups, and the level controls are one permutation each). The estimate can be low when real groups overlap "
    "other recorded or unrecorded alterations, tissue programmes or each other, which random groups do not. "
    "expected_nonspecific (null_baseline, null_response): the arrows that random genes which are not partners would "
    "give as often (nonspecific_share summed over the written arrows): not false tests, but differences between the "
    "lines that are not specific to the partners.")


def _poisson_upper(k, conf=0.95):
    """One-sided upper confidence bound of a Poisson mean after observing k events (k = 0: about 3.0)."""
    return float(stats.chi2.ppf(conf, 2 * (int(k) + 1)) / 2.0)


def _pct(x, about=False):
    """A share as the readings print it: 'under 1%' below 0.005, else whole percent (rounded); about=True: 'about 20%'
    (never 'about under 1%')."""
    x = float(x)
    if not np.isfinite(x):
        return "NA"
    if x < 0.005:
        return "under 1%"
    return f"{'about ' if about else ''}{int(round(100 * x))}%"


def _pct_alert(x):
    """The printed share (whole percent) is at or above FALSE_SHARE_ALERT: an alert (and no grade A)."""
    x = float(x)
    return bool(np.isfinite(x) and x >= 0.005 and round(100 * x) >= round(100 * FALSE_SHARE_ALERT))


class _GeneTests:
    """D14: per gene and kind, the tests it took part in, as the source (the group's gene, a natural knockout's genes,
    a drug class's target, a level's gene) or as the target (a gene whose level or response was tested); finite p
    only, counted before the candidates are trimmed. Real groups only (not the controls)."""

    def __init__(self, c):
        self.c = c
        self.tgt = {}
        self.src = {}

    def add_src(self, kind, col, sym, n):
        if n:
            d = self.src.setdefault(kind, {})
            key = (int(col), str(sym))
            d[key] = d.get(key, 0) + int(n)

    def add_tgt(self, kind, cols):
        cols = np.asarray(cols, dtype=np.int64)
        if cols.size:
            a = self.tgt.setdefault(kind, np.zeros(self.c.gK, dtype=np.int64))
            np.add.at(a, cols, 1)

    def genotype(self, g, res):
        for kk, v in res.items():
            kind = f"genotype_{kk}"
            fin = np.isfinite(v["p"])
            self.add_src(kind, g["col"], g["gene"], int(fin.sum()))
            if kk in ("response", "baseline"):
                self.add_tgt(kind, v["t"][fin])

    def null(self, g, res, partners_of):
        c = self.c
        for kk, v in res.items():
            kind = f"null_{kk}"
            fin = np.isfinite(v["p"])
            if kk in ("response", "baseline"):
                tf = v["t"][fin]
                for x in g["genes"]:
                    sel = tf[np.isin(tf, list(partners_of(x) - {x}))]
                    self.add_src(kind, x, c.sym[x], sel.size)
                    self.add_tgt(kind, sel)
            else:
                for x in g["genes"]:
                    self.add_src(kind, x, c.sym[x], int(fin.sum()))

    def n_src(self, kind, col, sym):
        return int(self.src.get(kind, {}).get((int(col), str(sym)), 0))

    def table(self, edges, family):
        """direction/gene_tests.parquet (GENE_TESTS_DOCS): one row per (gene, kind, role) with a test."""
        c = self.c
        rows = []
        e = edges
        src_n = e.groupby(["source_col", "source", "kind"]).size().to_dict() if len(e) else {}
        src_ab = e[e["grade"].isin(["A", "B"])].groupby(["source_col", "source", "kind"]).size().to_dict() \
            if len(e) else {}
        gt_ = e[e["target_type"] == "gene"] if len(e) else e
        tgt_n = gt_.groupby(["target_col", "kind"]).size().to_dict() if len(gt_) else {}
        tgt_ab = gt_[gt_["grade"].isin(["A", "B"])].groupby(["target_col", "kind"]).size().to_dict() \
            if len(gt_) else {}
        for kind, d in self.src.items():
            for (col, sym), n in d.items():
                rows.append((col, sym, kind, "source", n, int(src_n.get((col, sym, kind), 0)),
                             int(src_ab.get((col, sym, kind), 0)), int(family.get(kind, 0))))
        for kind, a in self.tgt.items():
            for col in np.flatnonzero(a):
                rows.append((int(col), str(c.sym[col]), kind, "target", int(a[col]),
                             int(tgt_n.get((int(col), kind), 0)), int(tgt_ab.get((int(col), kind), 0)),
                             int(family.get(kind, 0))))
        df = pd.DataFrame(rows, columns=["col", "symbol", "kind", "role", "n_tests", "n_edges", "n_edges_ab",
                                         "family_tests"])
        for k_ in ("col", "n_tests", "n_edges", "n_edges_ab"):
            df[k_] = df[k_].astype(np.int32)
        df["family_tests"] = df["family_tests"].astype(np.int64)
        ko = {k_: i for i, k_ in enumerate(KINDS)}
        df = df.assign(_k=df["kind"].map(ko)).sort_values(["col", "_k", "role", "symbol"], kind="stable")
        return df.drop(columns="_k").reset_index(drop=True)


def _full_of(v):
    """{target or drug-dose: (p, q of the family the edge is written in)} over every test of one group's kind
    (v['full']: its targets and p before the candidates were trimmed)."""
    t, p = v.get("full", (np.zeros(0, np.int64), np.zeros(0)))
    qq = v["q_group"] if "q_group" in v else v["q"]
    pos = {int(x): float(q_) for x, q_ in zip(v["t"], qq)}
    return {int(x): (float(p_), pos.get(int(x), np.nan)) for x, p_ in zip(t, p)}


def _run(out, data, chunk, mem_gb, perms, k, n_pseudo, t0, meter=None):
    od = folder(out, "direction")
    c = _load(out, data)
    log(f"Direction: {c.gK:,} genes x {c.Dn:,} drug-doses x {c.L} lines; cell-line genetics: {c.meta_src}")
    _responses(c, chunk, mem_gb, k)
    log(f"  selectivity (response strength): {int(c.sel_dd.sum())} drug-doses with >= 1 selective line, from "
        f"{c.sel_from}")
    geno, records, gsrc, recorded = _genotype_groups(c)
    n_allele = sum(1 for g in geno if g.get("allele"))
    log(f"  genotype groups: {len(geno)} ({len(geno) - n_allele} by gene: driver genes recorded in >= {MIN_SIDE} "
        f"lines, LoF / GoF / any; {n_allele} by allele, codon, hotspot or amplification); heavily mutated lines: "
        f"{int(c.heavy.sum())}")
    gtests = _GeneTests(c)
    rows = []

    # ---- 1. genotype groups: p per group (its pooled null), q over the family of each kind (every group), rows
    def test_all(groups, count=False):
        res_all = []
        for g in groups:
            res = _finish(_test_group(c, g, GENO_KINDS, perms), stable_seed(g["gid"], 1))
            g["lambda"] = {kk: round(float(v["lambda"]), 3) for kk, v in res.items()}
            g["res"] = None
            if g["kind"] == "genotype" and g["gene"] in ("TP53", "KEAP1") and not g.get("allele"):
                g["res"] = {kk: {a: (b.copy() if isinstance(b, np.ndarray) else b) for a, b in v.items()}
                            for kk, v in res.items()}
            if count:
                gtests.genotype(g, res)
            for kk, v in res.items():
                if kk == "selectivity":
                    v["full"] = (v["t"].copy(), v["p"].copy())
                _trim(v)
            res_all.append((g, res))
        return res_all
    real = test_all(geno, count=True)
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
    c.false_rates = _false_rates(pseudo_counts)
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

        def coab_geno(y, g=g):                                 # D9: the target absent from most altered lines
            na_ = int(g["alt"].sum())
            return na_ > 0 and int((c.null[g["alt"], y]).sum()) >= JACCARD_CO * na_
        for kk, fn in (("response", lambda v: _response_rows(c, g, v, "genotype_response", res.get("baseline"), x)),
                       ("baseline", lambda v: _baseline_rows(c, g, v, "genotype_baseline", x, coabsent=coab_geno)),
                       ("sensitivity", lambda v: _sens_rows(c, g, v, "genotype_sensitivity", x)),
                       ("selectivity", lambda v: _sel_rows(c, g, v, "genotype_selectivity", x, _full_of(v)))):
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
        log(f"    {g['desc']}: edges " + ", ".join(f"{kk} {nr.get(kk, 0)} (+{extra[kk]})" for kk in GENO_KINDS)
            + " (+: within the group only)" + ("" if g["stratified"] else " (across organs)"))
    log(f"    ({quiet} of {len(real_counts)} groups without an edge; q over every group of a kind: "
        + ", ".join(f"{kk} {fam[kk][0]:,} tests" for kk in GENO_KINDS) + ")")

    # ---- 2. expression-null groups (related pairs; variable drug-doses; selective drug-doses)
    log(f"    ({(time.time() - t0) / 60:.1f} min so far)")
    dvar, dvar_p = _variable_dd(c)
    log(f"  expression-null groups: {len(ngroups)} line sets ({sum(len(g['genes']) for g in ngroups)} genes); "
        f"{int(dvar.sum())} drug-doses with line-to-line differences in cell numbers (chi-square p < {VAR_P})")
    Pm = c.partners

    def partners_of(x):
        return set(Pm.indices[Pm.indptr[x]:Pm.indptr[x + 1]].tolist())
    null_res = []
    pools = {kk: [] for kk in GENO_KINDS}
    cap = max(500, NULL_MAX // max(1, len(ngroups)))
    for g in ngroups:
        part = set()
        for x in g["genes"]:
            part.update(partners_of(x))
        part -= set(g["genes"])
        tg = np.array(sorted(part), dtype=np.int64)
        # baseline / response of the partners: within organs; across organs (a separate BH family) only when the
        # lines lacking X are not concentrated in organs - else X's absence cannot be told from the tissue there
        across_ok = g["stratified"] or not g["tissue"]
        kinds = GENO_KINDS if tg.size and across_ok else ("sensitivity", "selectivity")
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
        g["tested"] = {}
        for kk, v in res.items():
            v["p"], v["own"] = _guard_p(nulls[kk].p(v["T"]), v.pop("own_s"), v["n_arr"])
            g["tested"][kk] = v["t"][np.isfinite(v["p"])].copy()
            v["full"] = (v["t"].copy(), v["p"].copy())
        gtests.null(g, res, partners_of)
        for v in res.values():
            _trim(v)
    n_null_tests, null_cut = {}, {}
    for kk in GENO_KINDS:                                      # BH over the kind: within / across organs apart
        for st in (True, False):
            m, cut = _family_q([r for g, r in null_res if bool(g["stratified"]) == st], kk)
            n_null_tests[f"{kk}_{'within' if st else 'across'}_organs"] = m
            null_cut[(kk, st)] = cut
    null_absent = c.null.T                                       # genes x lines
    for g, res in null_res:
        g["n_edges"] = {}
        for x in g["genes"]:
            def alerts_fn(_y, g=g, x=x):
                return _null_gene_alerts(c, g, x, records)
            px = partners_of(x)

            def coab(y, g=g):
                inter = int((null_absent[y] & g["alt"]).sum())
                return inter and inter / int((null_absent[y] | g["alt"]).sum()) >= JACCARD_CO
            for kk, v in res.items():
                if kk == "sensitivity":
                    new = _sens_rows(c, g, v, "null_sensitivity", x, alerts_fn)
                elif kk == "selectivity":
                    new = _sel_rows(c, g, v, "null_selectivity", x, _full_of(v), alerts_fn)
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
    t_nc = time.time()
    nctl = _null_controls(c, ngroups, null_res, nulls, null_cut, partners_of, dvar)
    nctl["minutes"] = round((time.time() - t_nc) / 60, 2)
    log(f"  null controls (random non-partner genes, random line sets): {nctl['minutes']} min")

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
    lx, ly = getattr(c, "level_tested", (np.zeros(0, np.int64), np.zeros(0, np.int64)))
    for x_, n_ in zip(*np.unique(lx, return_counts=True)):
        gtests.add_src("level", int(x_), c.sym[int(x_)], int(n_))
    gtests.add_tgt("level", ly)
    log(f"  level: {level_info.get('tests', 0):,} directed related pairs, {level_info.get('edges', 0)} edges "
        f"({(time.time() - t0) / 60:.1f} min so far)")
    ls, ls_info = _level_sensitivity(c, C, k_cov, dvar)
    for x_, n_ in getattr(c, "levsens_tested", {}).items():
        gtests.add_src("level_sensitivity", x_, c.sym[x_], n_)
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
    for t, key, ks, dr, kk, p, bj, bm in getattr(c, "dt_tests", []):
        fin = np.isfinite(p)
        gtests.add_src("drug_target", c.col_of.get(t, -1), t, int(fin.sum()))
        gtests.add_tgt("drug_target", np.flatnonzero(fin))

    # ---- rules applied over the rows (VERSION 5)
    locus = _same_locus(c, rows)                                # D9
    _false_shares(c, rows)                                      # D6
    _nonspecific(c, rows, nctl, gtests)                         # D11

    # ---- tables
    if rows:
        edges = pd.DataFrame(rows, columns=list(_base_row()))
        ko = {kk: i for i, kk in enumerate(KINDS)}
        edges["_k"] = edges["kind"].map(ko)
        edges["_e"] = -pd.to_numeric(edges["contrast"], errors="coerce").abs().fillna(-np.inf)
        edges = edges.sort_values(["_k", "grade", "q", "_e", "p", "source", "target"], kind="stable")
        edges = edges.drop(columns=["_k", "_e"]).reset_index(drop=True)
        for cname in INT_COLS:
            edges[cname] = edges[cname].astype(np.int32)
        for cname in F32_COLS:
            edges[cname] = pd.to_numeric(edges[cname], errors="coerce").astype(np.float32)
        edges["same_locus"] = edges["same_locus"].astype(bool)
        edges["direction_clear"] = edges["direction_clear"].astype("boolean")   # typed even when all empty
    else:
        edges = _empty_edges()
    edges = _test_ids(edges)                                    # D2
    edges = _add_tiers(edges)
    write_parquet(edges, os.path.join(od, "edges.parquet"))

    group_rows = [_group_row(c, g) for g in geno + ngroups + pseudo]
    groups_df = pd.DataFrame(group_rows) if group_rows else pd.DataFrame(columns=list(GROUP_DOCS))
    groups_df = _add_group_tiers(groups_df)
    write_parquet(groups_df, os.path.join(od, "groups.parquet"))

    sel_df = _selectivity_table(c, real, null_res, edges)
    write_parquet(sel_df, os.path.join(od, "selectivity.parquet"))

    family = {f"genotype_{kk}": fam[kk][0] for kk in GENO_KINDS}
    family.update({f"null_{kk}": n_null_tests[f"{kk}_within_organs"] + n_null_tests[f"{kk}_across_organs"]
                   for kk in GENO_KINDS})
    family.update({"level": level_info.get("tests", 0), "level_sensitivity": ls_info.get("tests", 0),
                   "drug_target": n_dt_tests})
    gt_df = gtests.table(edges, family)
    write_parquet(gt_df, os.path.join(od, "gene_tests.parquet"))

    controls = _controls(c, geno, real_counts, pseudo_counts, edges, cuts, fam, level_info, ls_info, nctl)
    write_json(controls, os.path.join(od, "controls.json"))
    counts = {kk: {gr: int(((edges["kind"] == kk) & (edges["grade"] == gr)).sum()) for gr in ("A", "B", "C")}
              for kk in KINDS}
    n_across = sum(1 for g in ngroups if not g["stratified"])
    nt_sets = [g for g in ngroups if g.get("partners_withheld")]       # partners existed, not tested (note says why)
    tw = {kk: int(edges.loc[edges["kind"] == kk, "test_id"].nunique()) for kk in KINDS}
    info = {"version": VERSION, "genes": c.gK, "drugdoses": c.Dn, "lines": c.L, "k_drugdoses": int(c.sel.shape[1]),
            "chunk": c.chunk, "permutations": int(perms), "permutations_null_groups": PERMS_NULL,
            "cell_line_genetics": gsrc, "lines_with_genetics_record": int(recorded.sum()),
            "heavily_mutated_lines": {str(c.line_name[i]): int(c.n_driver_genes[i]) for i in np.flatnonzero(c.heavy)},
            "organs_from": c.organ_src, "lines_with_organ": int(c.organ_known.sum()),
            "groups_tested": {"genotype": len(geno), "genotype_by_allele": n_allele,
                              "allele_groups_not_testable": list(c.allele_not_testable),
                              "expression_null_line_sets": len(ngroups),
                              "expression_null_line_sets_across_organs": n_across,
                              "expression_null_genes": int(sum(len(g["genes"]) for g in ngroups)),
                              "expression_null_genes_across_organs": int(sum(len(g["genes"]) for g in ngroups
                                                                             if not g["stratified"])),
                              "expression_null_line_sets_not_tested_partners": len(nt_sets),
                              "expression_null_genes_not_tested_partners": int(sum(len(g["genes"])
                                                                                   for g in nt_sets)),
                              "expression_null_line_sets_in_a_programme": int(sum(
                                  1 for g in ngroups if _programme(g) > NOTE_COABSENT_SETS)),
                              "pseudo_controls": len(pseudo)},
            "global_sensitivity_correction": c.adj_counts,
            "selectivity_input": {"from": c.sel_from, "drugdoses_with_a_selective_line": int(c.sel_dd.sum()),
                                  "selective_line_cells": int(c.sel_line.sum())},
            "tests": {"genotype": {kk: fam[kk][0] for kk in GENO_KINDS},
                      "genotype_p_cut": {kk: cuts[kk] for kk in GENO_KINDS},
                      "expression_null": n_null_tests, "level_pairs": level_info.get("tests", 0),
                      "level_sensitivity": ls_info.get("tests", 0), "drug_target": n_dt_tests,
                      "drug_target_classes": len(getattr(c, "dt_classes", {}))},
            "tests_written_by_kind": tw,
            "same_locus_check": locus,
            "gene_tests_rows": int(len(gt_df)),
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
                                            "NOTE_TI_SHARE": NOTE_TI_SHARE, "FALSE_SHARE_ALERT": FALSE_SHARE_ALERT,
                                            "FULL_SIDE": FULL_SIDE}},
            "grade_a_rules": {"BOTH_WAYS_A": BOTH_WAYS_A, "MEASURED_A": MEASURED_A,
                              "FALSE_SHARE_ALERT": FALSE_SHARE_ALERT, "HYPERMUT_MIN_GENES": HYPERMUT_MIN_GENES,
                              "BASE_LOW": BASE_LOW},
            "false_positive_rate": controls["negative"]["summary"],
            "expected_false_edges": controls["expected_false_edges"],
            "null_controls_minutes": nctl["minutes"],
            "minutes": round((time.time() - t0) / 60, 2)}
    info["peak_rss_mb"], info["peak_rss_how"] = meter.stop() if meter is not None else (
        _peak_rss_mb(), "the process's peak (it may include earlier stages of the same run)")
    write_json(info, os.path.join(od, "info.json"))
    text, undocumented = readme(edges, groups_df, info, sel_df, gt_df)
    _write_text(os.path.join(od, "README.md"), text)
    if undocumented:
        log(f"  WARNING: columns without a description in README.md: {', '.join(undocumented)}")
    return info


# ----------------------------------------------------------------------------- rules over the rows (VERSION 5)
LOCUS_KINDS = ("genotype_response", "genotype_baseline", "null_response", "null_baseline")
LOCUS_ENRICHMENT = ("in this screen, genes absent from the same lines are 3 to 109 times more often within 1 Mb of "
                    "each other than by chance")


def _family(r):
    """'table' (q < Q_SIG and q_group < Q_SIG: grades A / B possible) or 'within' (significant within its group
    only)."""
    q, qg = float(r["q"]), float(r["q_group"]) if r["q_group"] is not None else np.nan
    return "table" if np.isfinite(q) and q < Q_SIG and (not np.isfinite(qg) or qg < Q_SIG) else "within"


def _add_reasons(r, reasons):
    r["alerts"] = _join(split_reasons(r["alerts"]) + [x for x in reasons if x])


def _false_rates(pseudo_counts):
    """D6: per genotype kind, the random pseudo-groups' arrows per group - 'table' (at the real family's cut and
    within the group) and 'within' (within the group only) -, each (mean per group, 95% upper bound per group:
    Poisson over all pseudo-groups)."""
    out = {}
    for kk in GENO_KINDS:
        nr = [x[1].get(kk, 0) for x in pseudo_counts if kk in x[2]]
        ng = [x[3].get(kk, 0) for x in pseudo_counts if kk in x[2]]
        n = len(nr)
        if not n:
            out[kk] = None
            continue
        w = [max(0, b - a) for a, b in zip(nr, ng)]
        out[kk] = {"groups": n, "table": (float(np.mean(nr)), _poisson_upper(sum(nr)) / n),
                   "within": (float(np.mean(w)), _poisson_upper(sum(w)) / n), "n_table": int(sum(nr)),
                   "n_within": int(sum(w))}
    return out


def _false_shares(c, rows):
    """D6: per genotype arrow, the share of its group's arrows of the kind (and family: over the whole table, or
    within the group only) that random comparison groups would give: expected_false_group (their arrows per group),
    group_edges, false_share = min(1, expected / group_edges) and its upper bound. The reason is an alert at or above
    FALSE_SHARE_ALERT (as printed, whole percent; and the arrow is then not grade A), else a note. Every genotype
    arrow also carries its family's caveat: the arrows of the kind the controls expect to be false over the table."""
    import collections
    fr = getattr(c, "false_rates", {}) or {}
    G = int(getattr(c, "n_geno_groups", 0))
    gk = [r for r in rows if str(r["kind"]).startswith("genotype_")]
    cnt = collections.Counter((r["group"], r["kind"], _family(r)) for r in gk)
    tot = collections.Counter((r["kind"], _family(r)) for r in gk)
    for r in gk:
        kk = r["kind"].split("_", 1)[1]
        f = _family(r)
        rate = fr.get(kk)
        if not rate:
            continue
        e, u = rate[f]
        n = cnt[(r["group"], r["kind"], f)]
        share, up = min(1.0, e / n), min(1.0, u / n)
        r.update({"expected_false_group": e, "group_edges": n, "false_share": share, "false_share_upper": up})
        what = "such arrows" if f == "table" else "such within-group arrows"
        reason = (f"random comparison groups give about {e:.2f} {what} per group (up to {u:.2f}); this comparison "
                  f"gives {n}: {_pct(share, True)} of them may be false (up to {_pct(up)})")
        N = tot[(r["kind"], f)]
        cav = (f"over the whole table the controls expect {e * G:.1f} (up to {u * G:.1f}) of the {N} arrows of this "
               f"kind{'' if f == 'table' else ' significant only within their group'} to be false "
               f"({_pct(min(1.0, e * G / N))})")
        _add_reasons(r, [reason, cav])
        if _pct_alert(share) and r["grade"] == "A":
            r["grade"] = "B"
            _add_reasons(r, [_blocked_note(5, [f"random groups expect {_pct(share, True)} of this comparison's "
                                               f"arrows to be false ({_pct(FALSE_SHARE_ALERT)} or more: "
                                               "FALSE_SHARE_ALERT)"])])


def _coord(c, col, sym):
    col = int(col)
    if 0 <= col < c.gK and c.coord_col[col] is not None:
        return c.coord_col[col]
    return c.coord_sym.get(str(sym).upper())


def _gap(a, b):
    """Base pairs between two genes on one chromosome (0 when they overlap); NaN on different chromosomes or
    without coordinates."""
    if a is None or b is None or str(a[0]) != str(b[0]):
        return np.nan
    return float(max(0, max(a[1], b[1]) - min(a[2], b[2])))


def _bp_words(d):
    d = int(d)
    if d < 1000:
        return f"{d} bp"
    return f"{d / 1000:.0f} kb" if d < 1_000_000 else f"{d / 1e6:.1f} Mb"


def _same_locus(c, rows):
    """D9: for gene-target arrows of genotype_response, genotype_baseline, null_response, null_baseline: distance_bp
    (the gap between source and target on one chromosome) and same_locus (<= SAME_LOCUS_BP): sign 0, grade C, the
    reading says which acts on which cannot be told, and an alert says why. Returns the check's numbers for info.json
    ('coordinates for N of M genes'; it could not run without coordinates)."""
    genes, have, n_chk, n_same = set(), set(), 0, 0
    for r in rows:
        if r["kind"] not in LOCUS_KINDS or r["target_type"] != "gene":
            continue
        n_chk += 1
        a = _coord(c, r["source_col"], r["source"])
        b = _coord(c, r["target_col"], r["target"])
        for key, x in (((int(r["source_col"]), str(r["source"]).upper()), a),
                       ((int(r["target_col"]), str(r["target"]).upper()), b)):
            genes.add(key)
            if x is not None:
                have.add(key)
        d = _gap(a, b)
        r["distance_bp"] = d
        if np.isfinite(d) and d <= SAME_LOCUS_BP:
            n_same += 1
            before = (r["sign"], r["grade"])
            r["same_locus"] = True
            r["sign"] = 0
            r["grade"] = "C"
            r["reading"] = r.get("_rd0", r["reading"]) + "; same locus: which acts on which cannot be told"
            col = int(r["target_col"])
            band = c.loc_col[col] if 0 <= col < c.gK and c.loc_col[col] else f"chromosome {b[0]}"
            lies = "overlaps" if d == 0 else f"lies {_bp_words(d)} from"
            _add_reasons(r, [f"same locus: {r['target']} {lies} {r['source']} ({band}); genes this close are deleted "
                             f"or gained together ({LOCUS_ENRICHMENT}), so the difference can be a shared deletion, "
                             "not regulation"]
                         + ([_changed_note(5, f"this arrow had sign {int(before[0]):+d} and grade {before[1]}",
                                           "sign 0 and grade C", f"source and target lie within "
                                           f"{_bp_words(SAME_LOCUS_BP)} (same locus)")]
                            if int(before[0]) or before[1] != "C" else []))
    ran = bool(have)
    return {"ran": ran, "genes": len(genes), "genes_with_coordinates": len(have), "edges_checked": n_chk,
            "edges_same_locus": n_same, "max_bp": SAME_LOCUS_BP,
            "text": (f"coordinates for {len(have)} of {len(genes)} genes" if ran else
                     "could not run: no gene coordinates (reference/annotations.parquet, "
                     "reference/gene_coords.parquet)")}


def _null_bin(n):
    """The overlap bin of a null line set (NULL_BINS): 0 for <= 10 overlapping sets, ... 4 for > 600."""
    return int(np.searchsorted(NULL_BINS, int(n), side="left"))


def _bin_names():
    lo = [0] + [b + 1 for b in NULL_BINS]
    return [f"{a}-{b}" for a, b in zip(lo, NULL_BINS)] + [f"more than {NULL_BINS[-1]}"]


def _null_p(nulls, kk, v):
    """p of a control's tests from the real kind's pooled null, guarded per target as the real tests are."""
    two = kk != "response"
    own = _own_stats(v["T"], v["Tp"], two)
    p, _ = _guard_p(nulls[kk].p(v["T"]), own, v["n_arr"])
    return p


def _null_controls(c, ngroups, null_res, nulls, null_cut, partners_of, dvar):
    """D11, the natural knockouts' random controls (controls.json null_controls).
    (a) null_baseline / null_response: NULL_CONTROL_SETS real line sets, drawn evenly over the overlap bins
    (NULL_BINS); per set NULL_CONTROL_GENES random genes that are not partners of any of its genes (nor its genes),
    measured in >= MIN_SIDE lines on each side, matched to its tested partners by pooled-CPM decile, tested exactly as
    the partners (same permutations, the kind's pooled null, the same per-target guard) and counted at the family's BH
    cut: rate[bin, kind] = hits / tests - how often a gene that is not a partner differs as much between these lines.
    (b) null_sensitivity / null_selectivity: N_PSEUDO_NULL random line sets with the real sets' sizes (quantiles),
    |phi| < PSEUDO_PHI_NULL to every real set with >= FULL_SIDE lines on each side, tested on the same drug-doses with
    the pooled null at the family's cut: the arrows a set without any real effect gives."""
    rng = np.random.default_rng(stable_seed("null-controls", c.gK, c.L))
    nb = len(NULL_BINS) + 1
    cands = [[] for _ in range(nb)]
    for g, res in null_res:
        if any(kk in res for kk in ("response", "baseline")):
            cands[_null_bin(g.get("null_co_n", 0))].append(g)
    per = max(1, NULL_CONTROL_SETS // nb)
    logc = np.log10(np.maximum(c.pooled_cpm, 0.0) + 1.0)
    edges_q = np.quantile(logc, np.linspace(0, 1, 11)[1:-1]) if logc.size else np.zeros(9)
    dec = np.digitize(logc, edges_q)
    acc = {kk: {"tests": np.zeros(nb, np.int64), "hits": np.zeros(nb, np.int64), "sets": np.zeros(nb, np.int64)}
           for kk in ("response", "baseline")}
    for b in range(nb):
        gs = cands[b]
        if len(gs) > per:
            gs = [gs[i] for i in sorted(rng.choice(len(gs), size=per, replace=False))]
        for g in gs:
            kinds = tuple(kk for kk in ("response", "baseline") if kk in g.get("tested", {}))
            tested = np.unique(np.concatenate([g["tested"][kk] for kk in kinds])) if kinds else np.zeros(0, int)
            if not tested.size:
                continue
            part = set(g["genes"])
            for x in g["genes"]:
                part |= partners_of(x)
            ok = (c.measured[g["alt"]].sum(axis=0) >= MIN_SIDE) & (c.measured[g["inn"]].sum(axis=0) >= MIN_SIDE)
            ok[np.array(sorted(part), dtype=np.int64)] = False
            want = np.bincount(dec[tested], minlength=10).astype(np.float64)
            want = np.rint(want / want.sum() * NULL_CONTROL_GENES).astype(int)
            pick = []
            for d_ in range(10):
                pool = np.flatnonzero(ok & (dec == d_))
                if want[d_] and pool.size:
                    pick.extend(rng.choice(pool, size=min(int(want[d_]), pool.size), replace=False).tolist())
            if not pick:
                continue
            res = _test_group(c, g, kinds, PERMS_NULL, targets=np.array(sorted(pick), dtype=np.int64))
            for kk, v in res.items():
                p = _null_p(nulls, kk, v)
                fin = np.isfinite(p)
                acc[kk]["tests"][b] += int(fin.sum())
                acc[kk]["hits"][b] += int((fin & (p <= null_cut[(kk, bool(g["stratified"]))])).sum())
                acc[kk]["sets"][b] += 1
    rates = {}
    for kk, a in acc.items():
        pooled = float(a["hits"].sum() / a["tests"].sum()) if a["tests"].sum() else np.nan
        rates[kk] = [float(h / t) if t else pooled for h, t in zip(a["hits"], a["tests"])]
    # (b) random line sets for the drug-dose kinds
    sizes = sorted((g["n_alt"], g["n_inn"]) for g in ngroups) or [(min(5, c.L // 3), min(10, c.L - c.L // 3))]
    pick_i = np.rint(np.linspace(0, len(sizes) - 1, N_PSEUDO_NULL)).astype(int)
    refs = [(g["alt"], g["inn"]) for g in ngroups if g["n_alt"] >= FULL_SIDE and g["n_inn"] >= FULL_SIDE]
    sens = {kk: [] for kk in ("sensitivity", "selectivity")}
    for i in range(N_PSEUDO_NULL if ngroups else 0):
        na, ni = sizes[int(pick_i[i])]
        if na + ni > c.L:
            continue
        perm = np.argsort(rng.random((200, c.L)), axis=1)
        alt = np.zeros((200, c.L), dtype=bool)
        inn = np.zeros((200, c.L), dtype=bool)
        np.put_along_axis(alt, perm[:, :na], True, axis=1)
        np.put_along_axis(inn, perm[:, na:na + ni], True, axis=1)
        ph = _phi_max(alt.astype(np.float64), refs)
        okk = np.flatnonzero(ph < PSEUDO_PHI_NULL)
        j = int(okk[0]) if okk.size else int(np.argmin(ph))
        g = _group_common(c, f"pseudo-null:{i + 1}", "pseudo", f"PSEUDONULL{i + 1}", "pseudo", alt[j], inn[j],
                          f"random line set {i + 1} ({na} lines) vs ({ni})")
        res = _test_group(c, g, ("sensitivity", "selectivity"), PERMS_NULL, dd_mask=dvar)
        for kk, v in res.items():
            p = _null_p(nulls, kk, v)
            sens[kk].append(int((np.isfinite(p) & (p <= null_cut[(kk, bool(g["stratified"]))])).sum()))
    real_sets = {kk: sum(1 for _, res in null_res if kk in res) for kk in sens}
    pls = {}
    for kk, h in sens.items():
        n = len(h)
        rate = float(np.mean(h)) if n else np.nan
        up = _poisson_upper(sum(h)) / n if n else np.nan
        pls[f"null_{kk}"] = {"pseudo_sets": n, "arrows": int(sum(h)), "rate_per_set": rate, "upper_per_set": up,
                             "real_sets_tested": real_sets[kk],
                             "expected_false": None if not n else round(rate * real_sets[kk], 2),
                             "expected_false_upper": None if not n else round(up * real_sets[kk], 2)}
    return {"bins": _bin_names(),
            "sets": {f"null_{kk}": a["sets"].tolist() for kk, a in acc.items()},
            "tests": {f"null_{kk}": a["tests"].tolist() for kk, a in acc.items()},
            "hits": {f"null_{kk}": a["hits"].tolist() for kk, a in acc.items()},
            "rates": {f"null_{kk}": [round(x, 6) if np.isfinite(x) else None for x in v] for kk, v in rates.items()},
            "_rates": {f"null_{kk}": v for kk, v in rates.items()},
            "line_sets": pls,
            "how": (f"(a) null_baseline / null_response: up to {NULL_CONTROL_SETS} real line sets drawn evenly over "
                    f"the overlap bins ({', '.join(_bin_names())} other line sets overlapping), {NULL_CONTROL_GENES} "
                    "random genes per set that are not partners of its genes, measured in at least 3 lines on each "
                    "side and matched to its tested partners by pooled-CPM decile, tested exactly as the partners "
                    "and counted at the family's BH cut: rates = hits / tests per bin (a bin without a set uses the "
                    "pooled rate). "
                    f"(b) null_sensitivity / null_selectivity: {N_PSEUDO_NULL} random line sets with the real sets' "
                    f"sizes (|phi| < {PSEUDO_PHI_NULL} to every real set with at least {FULL_SIDE} lines on each "
                    "side), tested on the same drug-doses and counted at the family's cut")}


def _nonspecific(c, rows, nctl, gtests):
    """D11 per natural-knockout arrow: nonspecific_share and its reason. Baseline / response: rate[bin, kind] x the
    source gene's partner tests of the kind / its written arrows of the kind ('would appear for any gene'). Cells /
    response strength: the random line sets' arrows per set / this set's arrows of the kind ('would appear for any set
    of lines'). An alert at or above FALSE_SHARE_ALERT (printed whole percent), else a note."""
    import collections
    nl = [r for r in rows if str(r["kind"]).startswith("null_")]
    per_src = collections.Counter((r["kind"], int(r["source_col"])) for r in nl)
    per_set = collections.defaultdict(set)
    for r in nl:
        if r["kind"] in ("null_sensitivity", "null_selectivity"):
            per_set[(r["kind"], r["group"])].add(int(r["target_dd"]))
    rates = nctl.get("_rates", {})
    pls = nctl.get("line_sets", {})
    for r in nl:
        kind = r["kind"]
        if kind in ("null_baseline", "null_response"):
            rr = rates.get(kind)
            if not rr:
                continue
            rate = rr[_null_bin(max(0, int(r["programme_sets"])))]
            if not np.isfinite(rate):
                continue
            tests = gtests.n_src(kind, r["source_col"], r["source"])
            n = per_src[(kind, int(r["source_col"]))]
            exp = rate * tests
            share = min(1.0, exp / n) if n else np.nan
            r["nonspecific_share"] = share
            _add_reasons(r, [f"random genes that are not partners differ as much between these lines in "
                             f"{100 * rate:.2g}% of tests: about {exp:.1f} of the {n} arrows of this gene would "
                             f"appear for any gene ({_pct(share)})"])
        else:
            x = pls.get(kind) or {}
            rate, up = x.get("rate_per_set"), x.get("upper_per_set")
            if rate is None or not np.isfinite(rate):
                continue
            n = max(1, len(per_set[(kind, r["group"])]))
            share, sup = min(1.0, rate / n), min(1.0, up / n)
            r["nonspecific_share"] = share
            _add_reasons(r, [f"random line sets give about {rate:.2f} such arrows per set (up to {up:.2f}); this set "
                             f"gives {n}: {_pct(share, True)} of them would appear for any set of lines (up to "
                             f"{_pct(sup)})"])


def _test_ids(e):
    """D2: test_id (one per distinct test: the same kind, compounds or class, mechanism class, drug effect, target and
    p for drug_target; the same group, target and p for the natural knockouts; every other edge its own) and
    n_same_test; an edge whose test stands for several sources gets a note naming them all."""
    if not len(e):
        e["test_id"] = pd.Series(dtype=np.int32)
        e["n_same_test"] = pd.Series(dtype=np.int16)
        return e
    kind = e["kind"].astype(str)
    dt = (kind == "drug_target").to_numpy()
    nl = kind.str.startswith("null").to_numpy()
    own = np.arange(len(e)).astype(str)
    key = pd.DataFrame({
        "k": kind.to_numpy(),
        "a": np.where(dt, e["compounds"].astype(str).to_numpy(), np.where(nl, e["group"].astype(str).to_numpy(), own)),
        "m": np.where(dt, (e["mechanism_class"].astype(str) + "|" + e["mechanism"].astype(str)).to_numpy(), ""),
        "f": np.where(dt, e["drug_effect"].astype(str).to_numpy(), ""),
        "t": e["target"].astype(str).to_numpy(), "d": e["target_dd"].to_numpy(),
        "p": [repr(float(x)) for x in e["p"]]})
    tid = key.groupby(list(key.columns), sort=False).ngroup().to_numpy()
    n = np.bincount(tid)[tid]
    e = e.copy()
    e["test_id"] = tid.astype(np.int32)
    e["n_same_test"] = n.astype(np.int16)
    multi = np.flatnonzero(n > 1)
    if multi.size:
        src = e["source"].astype(str).to_numpy()
        members = {}
        for i in multi:
            members.setdefault(int(tid[i]), []).append(src[i])
        al = e["alerts"].astype(str).to_numpy(dtype=object).copy()
        for i in multi:
            names = sorted(dict.fromkeys(members[int(tid[i])]), key=_natural_key)
            if dt[i]:
                note = (f"one test for {len(names)} targets ({', '.join(names)}): the same compounds give one result "
                        "for each; the arrows are the same evidence, counted once")
            else:
                note = (f"one test for {len(names)} genes absent from the same lines ({', '.join(names)}): the arrows "
                        "are the same evidence, counted once")
            al[i] = _join(split_reasons(al[i]) + [note])
        e["alerts"] = al
    return e


def _natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", str(s))]


def _selectivity_table(c, real, null_res, edges):
    """direction/selectivity.parquet (SELECTIVITY_DOCS): one row per drug-dose - its selective lines, how selective
    it is (the 3rd-largest sel_z), the organs its selective lines concentrate in (Fisher p < 0.05) and every
    comparison group with a selectivity arrow to it (q, and whether other doses agree)."""
    rows = []
    sel = c.sel_line
    S = getattr(c, "Ssel", None)
    org = c.organ
    e = edges[edges["kind"].isin(["genotype_selectivity", "null_selectivity"])] if len(edges) else edges
    by_dd = {}
    for r in e.itertuples(index=False):
        qq = r.q_group if r.kind == "genotype_selectivity" else r.q
        txt = (f"{r.group} [{r.kind}] (q {_q2(qq)}; sign {int(r.sign):+d}; "
               + (f"{int(r.n_doses_supporting)} doses agree" if int(r.n_doses_supporting) > 1 else "one dose only")
               + ")")
        by_dd.setdefault(int(r.target_dd), [])
        if txt not in by_dd[int(r.target_dd)]:
            by_dd[int(r.target_dd)].append(txt)
    for d in range(c.Dn):
        lines_ = np.flatnonzero(sel[d])
        z = S[d] if S is not None else np.full(c.L, np.nan)
        zz = np.sort(z[np.isfinite(z) & c.in_growth])[::-1]
        third = float(zz[2]) if zz.size >= 3 else np.nan
        enr = []
        have = np.isfinite(c.Rsel[d])
        if lines_.size:
            for o in sorted(set(org[have])):
                a = int((sel[d] & (org == o)).sum())
                if not a:
                    continue
                b = int((~sel[d] & have & (org == o)).sum())
                cc = int((sel[d] & (org != o)).sum())
                dd_ = int((~sel[d] & have & (org != o)).sum())
                pv = float(stats.fisher_exact([[a, cc], [b, dd_]], alternative="greater")[1])
                if pv < 0.05:
                    enr.append(f"{o} (p {pv:.2g}; {a} of the {lines_.size} selective lines, {a + b} of the "
                               f"{int(have.sum())} lines)")
        gl = by_dd.get(d, [])
        rows.append({"dd": d, "drug": str(c.drug[d]), "dose": str(c.dose[d]), "n_selective_lines": int(lines_.size),
                     "selective_lines": ", ".join(str(c.line_name[i]) for i in lines_), "selectivity": third,
                     "tested": bool(c.sel_dd[d]), "organs_enriched": "; ".join(enr), "n_groups": len(gl),
                     "groups": "; ".join(gl)})
    df = pd.DataFrame(rows, columns=list(SELECTIVITY_DOCS))
    df["dd"] = df["dd"].astype(np.int32)
    df["n_selective_lines"] = df["n_selective_lines"].astype(np.int32)
    df["n_groups"] = df["n_groups"].astype(np.int32)
    df["selectivity"] = df["selectivity"].astype(np.float32)
    return df


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
            "mechanism": MECH_WORDS[g["mech"]], "allele": g.get("allele", ""), "description": g["desc"],
            "n_altered": g["n_alt"], "n_intact": g["n_inn"], "altered_lines": ", ".join(nm[g["alt"]]),
            "intact_lines": ", ".join(nm[g["inn"]]),
            "organs_altered": g["organs_alt"], "organs_intact": g["organs_inn"], "stratified": bool(g["stratified"]),
            "n_arrangements": int(g["n_arr"]), "n_altered_shared_organs": int(g["n_alt_mixed"]),
            "n_intact_shared_organs": int(g["n_inn_mixed"]),
            "organ_enrichment_p": float(g["organ_p"]) if np.isfinite(g["organ_p"]) else np.nan,
            "tissue_confounded": bool(g["tissue"]),
            "cooccurs_with": "; ".join(f"{h} ({j:.2f})" for h, j in g["cooccur"]),
            "anti_occurs_with": "; ".join(f"{h} (phi -{v:.2f})" for h, v in g.get("anti", [])),
            "n_heavily_mutated_altered": int(g.get("n_heavy_alt", 0)),
            "n_heavily_mutated_intact": int(g.get("n_heavy_inn", 0)),
            "variants": g.get("variants", ""), "x_not_expressed_in_altered": int(g.get("x_lost", -1)),
            "x_baseline_log2_diff": float(g.get("x_base_diff", np.nan)),
            "genes_same_lines": ", ".join(str(c.sym[x]) for x in g.get("genes", [])) if g["kind"] == "null" else "",
            "overlapping_line_sets": int(g.get("null_co_n", 0) or 0) if g["kind"] == "null" else -1,
            "max_phi_to_real": float(g.get("max_phi", np.nan)),
            "max_phi_to_null_sets": float(g.get("max_phi_null", np.nan)), "alerts": _join(g["alerts"]),
            "inflation": "; ".join(f"{k} {v:.2f}" for k, v in (g.get("lambda") or {}).items()),
            "note": g.get("note", ""), "n_edges_response": int(ne.get("response", 0)),
            "n_edges_baseline": int(ne.get("baseline", 0)),
            "n_edges_sensitivity": int(ne.get("sensitivity", 0)),
            "n_edges_selectivity": int(ne.get("selectivity", 0))}


def _dna_damage_dd(c):
    """The drug-doses of DNA-damaging drugs for the positive controls, each with why: a Tahoe target in
    DNA_DAMAGE_TARGETS, or (D4) a TOP1 / TOP2 poison or a class acting on DNA (mechanisms, with its source).
    Returns {drug-dose: reason}."""
    out = {}
    for d in range(c.Dn):
        tg = set(_split_targets(c.dd["targets"].iloc[d])) if "targets" in c.dd else set()
        hit = sorted(tg & DNA_DAMAGE_TARGETS)
        why = [f"Tahoe target {', '.join(hit)}"] if hit else []
        for k_ in c.cls_by_drug.get(str(c.drug[d]), []):
            info = MX.class_info(k_)
            if k_ in ("TOP1_POISON", "TOP2_POISON") or info.get("effect") == "dna":
                why.append(f"{info.get('label', k_)} ({c.cls_src.get((str(c.drug[d]), k_), '') or 'class'})")
        if why:
            out[d] = "; ".join(why)
    return out


def _controls(c, geno, real_counts, pseudo_counts, edges, cuts, fam, level_info, ls_info, nctl=None):
    """controls.json: positive controls (TP53 -> p53 targets and DNA-damage sensitivity; KEAP1 -> NRF2 targets; KRAS
    p.G12C -> response to adagrasib; TP53 -> response strength to DNA-damaging drugs), the negative controls
    (pseudo-groups, counted at the real family's BH cut) next to the real groups' counts, the natural knockouts'
    random controls (null_controls) and the expected false edges per kind (pseudo rate x real groups; permuted-level
    controls for the level kinds; random non-partner genes and random line sets for the natural knockouts)."""
    pos = {}
    tp = [g for g in geno if g["gene"] == "TP53" and not g.get("allele")]
    present = [s for s in P53_TARGETS if s in c.col_of]
    dmg = _dna_damage_dd(c)
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
            rise, con, draw = float(r["rise"][j]), float(r["D"][j]), float(r["D_raw"][j])
            edge = bool(len(e))
            sign = int(e["sign"].iloc[0]) if edge else 0
            why = ""
            if np.isfinite(rise) and rise < 0.5:
                why = f"evidence from falls (rise_share {rise:.2f}): the p53 targets rise under DNA damage"
            elif not (np.isfinite(con) and con > 0):
                why = f"the mean contrast goes the other way ({con:+.2f})"
            elif edge and sign != 1:
                why = "wrong sign" if sign == -1 else "sign not inferred"
            elif not edge:
                why = f"not an edge (q {_q2(r['q'][j])})"
            per.append({"gene": s, "tested": bool(np.isfinite(r["T"][j])), "T": float(r["T"][j]),
                        "p": float(r["p"][j]), "q": float(r["q"][j]), "rank": int(rank[j]), "D": con,
                        "contrast": con, "D_raw": draw, "rise_share": rise,
                        "edge": edge, "grade": e["grade"].iloc[0] if edge else "", "sign": sign,
                        "counted": bool(edge and not why), "why_not": why,
                        "alert": bool(edge and str(e["alerts"].iloc[0] or ""))})
        rec = [x for x in per if x["counted"]]
        pos[f"TP53 ({g['desc']}) -> p53 targets (response)"] = {
            "expected": ("sign +1 and evidence from rises (rise_share >= 0.5) with the mean contrast agreeing: the "
                         "targets rise less where TP53 is lost"), "targets_present": len(per),
            "recovered_right_sign": len(rec), "wrong_sign": sum(x["edge"] and x["sign"] == -1 for x in per),
            "edge_not_counted": [{"gene": x["gene"], "why_not": x["why_not"]} for x in per
                                 if x["edge"] and not x["counted"]],
            "median_rank": float(np.median([x["rank"] for x in per])) if per else None,
            "genes_ranked": int(np.isfinite(r["T"]).sum()), "per_gene": per,
            "note": "q is null where it is >= 0.10 (only candidates p < 0.10 enter the family's BH)"}
        e = edges[(edges["kind"] == "genotype_sensitivity") & (edges["source"] == "TP53") &
                  (edges["group"] == g["desc"]) & (edges["target_dd"].isin(list(dmg)))]
        pos[f"TP53 ({g['desc']}) -> cells under DNA-damaging drugs (sensitivity)"] = {
            "expected": "sign -1: TP53 activity makes the cells more sensitive", "drugdoses_tested": len(dmg),
            "edges": int(len(e)), "right_sign": int((e["sign"] == -1).sum()),
            "drugdoses": e["target"].tolist(), "drugdoses_alert": (e["alerts"] != "").tolist(),
            "drugdoses_why": [dmg[int(d)] for d in e["target_dd"]]}
        es = edges[(edges["kind"] == "genotype_selectivity") & (edges["source"] == "TP53") &
                   (edges["group"] == g["desc"]) & (edges["target_dd"].isin(list(dmg)))]
        pos[f"TP53 ({g['desc']}) -> response strength to DNA-damaging drugs (selectivity)"] = {
            "expected": "sign +1: intact lines respond more", "drugdoses_tested": int(sum(
                1 for d in dmg if c.sel_dd[d])), "edges": int(len(es)), "right_sign": int((es["sign"] == 1).sum()),
            "wrong_sign": int((es["sign"] == -1).sum()), "drugdoses": es["target"].tolist(),
            "drugdoses_alert": (es["alerts"] != "").tolist(), "drugdoses_why": [dmg[int(d)] for d in es["target_dd"]]}
    ada = [d for d in range(c.Dn) if "ADAGRASIB" in molecule_key(c.drug[d])]
    kg = [g for g in geno if g["gid"] == "genotype:KRAS:G12C"]
    key = f"KRAS p.G12C -> response to Adagrasib (selectivity; expected sign +1 at >= 2 doses; {ADAGRASIB_REF})"
    if not ada:
        pos[key] = {"assessable": False, "why": "Adagrasib is not among the screened drugs"}
    elif not kg:
        n = sum(1 for i in range(c.L) if any(allele_change(v[2]) == "G12C"
                                             for v in (_records(c)[0].get("KRAS", {}).get(i, ()))))
        pos[key] = {"assessable": False, "why": f"no KRAS p.G12C group ({n} line{'s' if n != 1 else ''} recorded, "
                                                f"fewer than {MIN_SIDE})"}
    else:
        e = edges[(edges["kind"] == "genotype_selectivity") & (edges["group"] == kg[0]["desc"]) &
                  edges["target_dd"].isin(ada)]
        right = e[e["sign"] == 1]
        pos[key] = {"assessable": True, "drugdoses_tested": int(sum(1 for d in ada if c.sel_dd[d])),
                    "edges": int(len(e)), "right_sign_doses": int(right["target_dd"].nunique()),
                    "recovered": bool(right["target_dd"].nunique() >= 2), "drugdoses": e["target"].tolist(),
                    "signs": e["sign"].astype(int).tolist(), "drugdoses_alert": (e["alerts"] != "").tolist()}
    kp = [g for g in geno if g["gene"] == "KEAP1" and not g.get("allele")]
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
    nctl = nctl or {}
    for kind in ("null_baseline", "null_response"):
        sel = edges[edges["kind"] == kind] if len(edges) else edges
        ns = pd.to_numeric(sel["nonspecific_share"], errors="coerce") if len(sel) else pd.Series(dtype=float)
        exp[kind] = {"edges": int(len(sel)), "expected_nonspecific": round(float(ns.fillna(0).sum()), 2),
                     "how": "the arrows that random genes which are not partners would give as often: per source gene "
                            "the random genes' rate in its overlap bin x its partner tests, at most its arrows "
                            "(nonspecific_share summed); not false tests, but differences between these lines that "
                            "are not specific to the partners"}
    for kind in ("null_sensitivity", "null_selectivity"):
        x = (nctl.get("line_sets") or {}).get(kind) or {}
        n_e = int((edges["kind"] == kind).sum()) if len(edges) else 0
        exp[kind] = {"edges": n_e, "expected_false": x.get("expected_false"),
                     "expected_false_upper": x.get("expected_false_upper"),
                     "how": f"{x.get('pseudo_sets', 0)} random line sets with the real sets' sizes: their arrows per "
                            f"set x the {x.get('real_sets_tested', 0)} real line sets tested (counted at the family's "
                            "cut); per line set, not per gene (genes absent from the same lines share their arrows)"}
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
    nc_out = {k: v for k, v in nctl.items() if not k.startswith("_")}
    return {"positive": pos, "negative": neg, "level_controls": {"level": level_info,
                                                                 "level_sensitivity": ls_info},
            "null_controls": nc_out, "expected_false_edges": exp, "expected_false_how": EXPECTED_FALSE_HOW}


# ----------------------------------------------------------------------------- README
EDGE_DOCS = {
    "source": "the upstream gene: the genotype's gene, the gene that is absent, whose level varies, or that the "
              "compounds target",
    "source_col": "its gene col (genes.csv; -1 = a drug target or driver gene that is not a measured gene)",
    "target": "the gene that changes, 'cells under DRUG DOSE' (the cells' growth: sensitivity kinds) or 'response to "
              "DRUG DOSE' (how strongly the lines respond: selectivity kinds)",
    "target_col": "the target gene's col (-1 for cells and response targets)",
    "target_dd": "the drug-dose row of a cells or response target (-1)",
    "target_type": "gene, cells or response",
    "kind": "the evidence: genotype_response / genotype_baseline / genotype_sensitivity / genotype_selectivity "
            "(recorded mutation), null_response / null_baseline / null_sensitivity / null_selectivity (the gene is "
            "not expressed in some lines), drug_target (compounds that target it), level / level_sensitivity (its "
            "natural level)",
    "grade": "A (recorded genotype, >= 5 lines each side measured, q < 0.05, compared within organs, no co-occurrence, "
             "anti-occurrence or heavily-mutated-lines alert, expected false share of the group below 20%; for a "
             "response also: not resting on the global-sensitivity correction, the mean over all its drug-doses going "
             "its way with and without the correction, under half of the evidence the other way, not a floor, "
             "measured in at least half of each side's lines; for a selectivity arrow: seen at >= 2 doses), B, C (a "
             "glimpse: also tissue-confounded, same locus, co-absent, an expression programme, a drug class that "
             "traps its target) - see 'How to read a grade'",
    "sign": "+1: the source's activity raises the target's level or the cell numbers, or strengthens the target's "
            "drug response in its own direction (for a target that falls under the drugs: a deeper fall) or the lines' "
            "response strength; -1: lowers it / weakens it; 0: not inferred (mechanism unknown, a trap class, same "
            "locus, an expression programme) - see 'How to read a sign'",
    "reading": "the edge in words",
    "group": "the comparison ('TP53 recorded as loss of function (10 lines: ...) vs not recorded (8)')",
    "mechanism": "loss of function / gain of function / altered (any record) / not expressed / level / for drug_target "
                 "the class's action: inhibitor, activator, unclear, 'inhibitor (microtubule destabiliser)' or a trap "
                 "class ('TOP2 poison', ...)",
    "n_altered": "lines on the altered (or lacking) side with a value for the target (-1: not applicable)",
    "n_intact": "lines on the other side with a value", "n_lines": "lines in a level correlation",
    "contrast": "the tested effect: response kinds mean corrected response (z units) intact - altered; baseline "
                "log2 level intact - altered; sensitivity log2 relative cell number intact - altered; selectivity "
                "rel_log2 (genes beyond the per-line cut against the line's typical drug-dose) intact - altered; level "
                "r; drug_target the median log2 fold of the supporting compounds (the n_top strongest; each compound's "
                "strongest fold in the edge's direction, signed)",
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
    "n_supporting": "drug_target: of them, those significant that way (pooled q < 0.1 and >= 1.2x at any dose)",
    "background_rate": "drug_target: share of all compounds significant that way for the target",
    "compounds": "drug_target: every compound of the class, '; '-joined; one molecule counts once (salt forms, "
                 "letter case and salt words merged; its names ' / '-joined) ('' for other kinds)",
    "compounds_supporting": "drug_target: the n_top compounds of the test, strongest first ('; '-joined), then "
                            "'also significant: ...' (', '-joined) for the class's other compounds significant that "
                            "way",
    "drug_effect": "drug_target: what the compounds do to the target's level, 'raises' or 'lowers' (sign is relative "
                   "to the source's activity: an inhibitor that raises the target gives sign -1)",
    "T": "the tested statistic: permutation-standardised (and divided by the group's inflation) for the group "
         "kinds; t = r sqrt(dof / (1 - r^2)) for the level kinds; empty for drug_target",
    "p": "group kinds: from the pooled permutation null with a fitted generalized-Pareto tail (no floor), never "
         "below the target's own permutation p where its own shuffles disagree with the pool, nor below 1 / its "
         "number of label arrangements; two-sided, except the response kinds (one-sided upper tail of the omnibus "
         "S). Level kinds: two-sided, from the t distribution (calibrated by a Freedman-Lane null). drug_target: "
         "the top-j test - for each j from 2 to the class's significant compounds, the hypergeometric chance that j "
         "of the class's N compounds are among the m_j compounds of the screen that move the target at least as "
         "strongly as the class's j-th strongest; the smallest, times N - 1 (Bonferroni over the thresholds)",
    "q": "BH q over the kind's whole family: every genotype group of the kind; every expression-null test of the "
         "kind (within-organ and across-organ comparisons as two families); every level pair; every (gene, "
         "drug-dose) level_sensitivity test; every drug_target test (every class, direction and gene)",
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
                     "drug_target: each supporting compound's strongest drug-dose, strongest compound first; "
                     "sensitivity and selectivity: the drug-dose",
    "art_share": "response kinds (genotype_response, null_response): the share of the evidence (sum of |contrast| over "
                 "the target's 10 drug-doses) carried by drug-doses with an artifact flag (toxic, transcription drop, "
                 "cell-cycle shift, like a neighbouring well, ...); float32; empty for the other kinds",
    "drugdoses_all": "every drug-dose behind the edge, each with its flags ('[artifact flags: ...]' or '[flags: "
                     "...]'): response kinds - all 10 of the target's drug-doses, as in top_drugdoses (fold in the "
                     "altered lines vs the other lines, z diff), strongest in the edge's direction first; drug_target "
                     "- every significant drug-dose of each supporting compound (pooled fold and z); sensitivity and "
                     "selectivity kinds - the drug-dose; level - the target's 10 drug-doses (pooled fold and z); '' "
                     "for the baseline kinds. top_drugdoses keeps the first few",
    "mechanism_class": "drug_target: the mechanism class that set the test's class (D1): 'TOP1 poison', 'TOP2 poison', "
                       "'PARP trapper', 'microtubule stabiliser' (trap classes: sign not inferred, grade C) or "
                       "'microtubule destabiliser'; '' for a class by action (inhibitor / activator / unclear)",
    "mechanism_source": "drug_target with a mechanism class: per compound, the source of its membership "
                        "(tahoemap/data/drug_classes.json code constant with its citation, ChEMBL mechanism, WHO ATC), "
                        "'; '-joined",
    "compounds_source": "drug_target: per compound of the class, where its membership comes from ('Tahoe', 'ChEMBL "
                        "(mechanism)', 'Tahoe and ChEMBL', 'Tahoe target, action from ChEMBL', 'Tahoe and ChEMBL, "
                        "actions differ'), '; '-joined; '' when ChEMBL is not loaded",
    "n_top": "drug_target: j, the number of compounds the test's best threshold uses (the strongest j)",
    "m_top": "drug_target: m_j, how many compounds of the screen move the target at least as strongly as the class's "
             "j-th strongest (ties counted)",
    "class_size": "drug_target: N, the compounds of the class (as n_compounds)",
    "share_supporting": "drug_target: n_supporting / class_size (the old count test's share), float32",
    "ti_share": "response kinds: the share of the evidence carried by drug-doses of translation inhibitors (a class "
                "of tahoemap/data/drug_classes.json with effect 'translation'), float32; empty for the other kinds",
    "expected_false_group": "genotype kinds: random comparison groups' arrows of the kind per group, in the edge's "
                            "family (over the whole table, or within the group only)",
    "group_edges": "genotype kinds: the edge's group's arrows of the kind in the same family (-1 for other kinds)",
    "false_share": "genotype kinds: min(1, expected_false_group / group_edges): the share of the group's arrows of "
                   "this kind that may be false; at or above 20% (as printed) an alert and no grade A; float32",
    "false_share_upper": "the same with the controls' 95% upper bound, float32",
    "distance_bp": "genotype and null response / baseline arrows to a gene: base pairs between source and target on "
                   "one chromosome (0 = they overlap); empty on different chromosomes or without coordinates",
    "same_locus": "distance_bp <= 1,000,000 (SAME_LOCUS_BP): sign 0, grade C (genes this close are deleted or gained "
                  "together)",
    "programme_sets": "natural knockouts: how many other line sets overlap the lines lacking the source (Jaccard >= "
                      "0.5); more than 10 = an expression programme (sign 0, grade C); -1 for other kinds",
    "nonspecific_share": "natural knockouts: the share of the source's arrows of the kind that random genes which are "
                         "not partners (baseline, response) or random line sets (cells, response strength) would give "
                         "as well, float32",
    "allele": "genotype kinds: '' for a gene-level group, else the allele group: a change ('G12C'), a codon "
              "('G12 (codon)'), 'hotspot' or 'amplification'",
    "doses_supporting": "selectivity kinds: the compound's other doses significant in the same group, with their q "
                        "(the 'also at' support)",
    "n_doses_supporting": "selectivity kinds: doses of the compound significant in the group, this one included (1 = "
                          "one dose only: an alert, no grade A); -1 for other kinds",
    "test_id": "one id per distinct test: edges with the same id are the same evidence for several sources (drug "
               "targets sharing compounds; genes absent from the same lines), int32",
    "n_same_test": "edges sharing the test_id (1 = its own test), int16",
    "n_alerts": "number of reasons in alerts (int16; an edge with 0 carries no warning sign)",
    "notes": "reasons kept below their thresholds (see 'Alerts, notes, caveats and support'), '; '-joined, no sign: "
             "read them, they are context rather than doubt about this arrow",
    "caveats": "the reasons every edge of its kind carries (drug_target: drugs can act on other proteins too; level: "
               "tissue can mimic it, and the precision caveat; level_sensitivity: tissue can mimic it; genotype "
               "kinds: the false arrows the controls expect over the whole table), '; '-joined",
    "support": "reasons that support the edge (drug_target: the supporting compounds; expression-null: a recorded loss "
               "of the gene in the same lines; selectivity: the other doses that agree), '; '-joined",
    "alerts_all": "every reason of the edge (alerts, notes, caveats and support together) in the order the stage wrote "
                  "them, '; '-joined, no sign",
    "n_notes": "number of notes (int16)", "n_caveats": "number of caveats (int16)",
    "n_support": "number of support reasons (int16)",
}
GROUP_DOCS = {
    "group_id": "kind:gene:mechanism or kind:gene:allele ('genotype:KRAS:G12C', 'genotype:KRAS:G12 (codon)')",
    "kind": "genotype, null (expression-null line set) or pseudo (control)",
    "gene": "the gene", "gene_col": "its col (-1 = not measured)", "mechanism": "as in edges",
    "allele": "'' (by gene), a change ('G12C'), a codon ('G12 (codon)'), 'hotspot' or 'amplification'",
    "description": "the comparison, in words with the composition of the altered lines (D15)",
    "n_altered": "lines altered / lacking the gene", "n_intact": "lines compared",
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
    "n_heavily_mutated_altered": "altered lines recording alterations in >= 15 driver genes (HYPERMUT_MIN_GENES)",
    "n_heavily_mutated_intact": "the same among the comparison lines",
    "variants": "variant types of the altered lines' records", "x_not_expressed_in_altered":
        "altered lines where the gene itself is not expressed (-1: not measured)",
    "x_baseline_log2_diff": "the gene's own level, intact - altered (log2)",
    "genes_same_lines": "null: every gene absent from exactly these lines",
    "overlapping_line_sets": "null: other line sets overlapping these lines (Jaccard >= 0.5); more than 10 = an "
                             "expression programme; -1 for other kinds",
    "max_phi_to_real": "pseudo: largest |phi| to a recorded group (drawn below 0.3)",
    "max_phi_to_null_sets": "pseudo: largest |phi| to an expression-null line set with >= 5 lines each side (drawn "
                            "below 0.5)",
    "alerts": "the group's reasons to doubt its comparison (warning sign; '' or '⚠ ' + '; '-joined); every edge of "
              "the group carries them too",
    "notes": "the group's reasons kept below their thresholds (within organs on most lines; the gene itself not "
             "expressed in a few altered lines; loss of function inferred from missense changes; heavily mutated "
             "comparison lines), '; '-joined",
    "alerts_all": "every reason of the group, alerts and notes, in the original order, '; '-joined",
    "inflation": "per test, the genomic-control factor its statistics were divided by (>= 1; how much wider than the "
                 "permutation null the bulk of all targets' statistics spread for this grouping)",
    "note": "null: how its partners' baseline and response were compared (across organs: a separate BH family), or "
            "why they were not tested (lines concentrated in organs); a hotspot group: the cited hotspot list",
    "n_edges_response": "edges written (pseudo: tests at or below the real family's BH cut, counted, not written)",
    "n_edges_baseline": "same", "n_edges_sensitivity": "same", "n_edges_selectivity": "same",
}
SELECTIVITY_DOCS = {
    "dd": "the drug-dose row (atlas/effects/drugdose.csv)", "drug": "the drug", "dose": "its dose (µM)",
    "n_selective_lines": "lines where the drug-dose is selective (tables/drug_line_response.parquet selective: sel_z "
                         ">= 3 and >= 20 genes beyond the per-line cut; lines in the growth analysis)",
    "selective_lines": "their names, every one", "selectivity": "the 3rd-largest sel_z over the lines (float32)",
    "tested": "tested by the selectivity kinds (>= 1 selective line)",
    "organs_enriched": "organs its selective lines concentrate in: one-sided Fisher p < 0.05, each with its counts",
    "n_groups": "comparison groups with a selectivity arrow to it",
    "groups": "every such group: description, kind, q (q_group for a genotype group), sign, and whether other doses "
              "agree ('N doses agree') or 'one dose only'",
}
GENE_TESTS_DOCS = {
    "col": "the gene's col (int32; -1 for a source that is not a measured gene, e.g. a drug target or driver)",
    "symbol": "the gene", "kind": "the kind of evidence (as edges.parquet)",
    "role": "'source' (the group's gene, a natural knockout's genes, a drug class's target, a level's gene) or "
            "'target' (a gene whose level or response was tested)",
    "n_tests": "tests with a finite p it took part in, in that role (int32; real groups only, not the controls)",
    "n_edges": "edges written with it in that role (any grade; int32)", "n_edges_ab": "of them grade A or B (int32)",
    "family_tests": "the tests of the kind over the run, its BH families together (int64)",
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
        "reflect how precisely each level is measured; level_sensitivity: tissue can mimic it; genotype kinds: how "
        "many of the kind's arrows the controls expect to be false over the whole table). Stated once above each "
        "list.",
        "- **support**: evidence for the arrow ('consistent across N compounds'; for a gene missing from some lines: "
        "'the lines lacking X carry a recorded loss of X: genotype evidence too'; for a selectivity arrow: 'also at "
        "... (q ...)').",
        "", "The graded reasons, and when each is an alert rather than a note:",
        f"- 'Y measured in a of the A and i of the I lines': an alert when a or i is below {FULL_SIDE}, or a is below "
        f"{NOTE_MEASURED_FRAC:g} x A, or i is below {NOTE_MEASURED_FRAC:g} x I (NOTE_MEASURED_FRAC); else a note.",
        f"- 'supporting drug-doses with artifact flags (N% of the evidence)': an alert when the flagged drug-doses "
        f"carry at least {NOTE_ART_SHARE:.0%} of the evidence (art_share, NOTE_ART_SHARE), or the strongest "
        "supporting drug-dose (the first of top_drugdoses) is one of them ('the strongest among them'); else a note. "
        "It lists every flagged drug-dose among the target's 10. For drug_target: the share of the supporting "
        "compounds whose strongest drug-dose is flagged, or the strongest of all is.",
        f"- 'drug-doses of translation inhibitors carry N% of the evidence': an alert when they carry at least "
        f"{NOTE_TI_SHARE:.0%} (ti_share, NOTE_TI_SHARE) or the strongest supporting drug-dose is one of them; else a "
        "note. A drug_target arrow whose supporting compounds are all translation inhibitors carries it as an alert.",
        f"- 'random comparison groups give about E such arrows per group ... about N% of them may be false' (D6) and "
        f"the natural knockouts' 'would appear for any gene (N%)' / 'would appear for any set of lines' (D11): an "
        f"alert at or above {FALSE_SHARE_ALERT:.0%} as printed (FALSE_SHARE_ALERT), else a note.",
        f"- 'compared within organs: a of the A ... and i of the I others share an organ': an alert when a is below "
        f"{NOTE_WITHIN_ORGAN_FRAC:g} x A or i is below {NOTE_WITHIN_ORGAN_FRAC:g} x I (NOTE_WITHIN_ORGAN_FRAC); else a "
        "note (a within-organ comparison costs lines, not validity).",
        f"- 'other genes are absent from most of these lines too ... (and N more line sets)': an alert when "
        f"{NOTE_COABSENT_SETS} or fewer line sets overlap in all (NOTE_COABSENT_SETS: a candidate co-deletion; every "
        "one of them is then named); else a note (many genes share the pattern: a tissue programme rather than one "
        "deletion; the 3 closest sets are named and the others counted).",
        "- Lists in a reason are never cut: 'the supporting compounds also share ...' names every shared target, "
        "'co-occurs with ...' every co-occurring gene (as groups.parquet cooccurs_with), 'another gene's alterations "
        "sit on the other side ...' every such gene, 'N other gene(s) are absent from exactly these lines (...)' all "
        "N, 'heavily mutated lines: ...' every such line, 'one test for N targets (...)' every target.",
        f"- 'X itself is not expressed in k of the n altered lines': an alert when k is above "
        f"{NOTE_NOT_EXPRESSED_FRAC:g} x n (NOTE_NOT_EXPRESSED_FRAC); else a note.",
        "- Always notes: 'loss of function is the metadata's inference; ... lines carry a missense change ...' (a "
        "loss-of-function group where at least a third of the lines carry a missense change), 'k of the n comparison "
        "lines are heavily mutated (...)', 'one test for N targets (...)' / 'one test for N genes absent from the "
        "same lines (...)' (the arrows are the same evidence, counted once).",
        "- Every other reason is an alert, among them: tissue-confounded; co-occurs or another gene's alterations on "
        "the other side; heavily mutated lines on the altered side; compared across organs; few lines; organs not "
        "known; significant within its group or drug-dose only (a lead); direction unclear; both ways; the mean "
        "over all drug-doses going the other way; a floor; rises at some drug-doses and falls at others; lower "
        "baseline; the correction alerts; its own permutation p; 'any of them could be the cause'; maybe low rather "
        "than absent; cell counts less trustworthy; same locus; co-absent with the target; an expression programme; "
        "the compounds are poisons (trap their target); they also act on DNA; supported by 2 compounds only; the "
        "annotations of Tahoe and ChEMBL disagree; one dose only."]


def _tier_run_line(info):
    """README 'This run': how many edges carry an alert, a note, a caveat, support."""
    t = info.get("reason_tiers") or {}
    if not t:
        return "- reasons in tiers: not recorded"
    return (f"- reasons: {t['edges_with_alert']:,} of {info['edges']:,} edges carry an alert (⚠), "
            f"{t['edges_with_note']:,} a note, {t['edges_with_caveat']:,} their kind's caveat and "
            f"{t['edges_with_support']:,} support; without an alert, by kind: " + ", ".join(
                f"{k} {v:,}" for k, v in t["edges_without_alert_by_kind"].items() if info["edges_by_kind"].get(k)))


def _expected_line(k, v):
    if "expected_nonspecific" in v:
        return f"{k} {v['expected_nonspecific']} of {v['edges']} would appear for any gene (non-specific)"
    return f"{k} {v.get('expected_false')} (up to {v.get('expected_false_upper')}) of {v['edges']}"


def grade_lines():
    """README 'How to read a grade' (VERSION 5: the conditions, the old rule and why)."""
    return [
        "## How to read a grade", "",
        "- **A**: a recorded genotype, >= 5 lines on each side (within organs: lines sharing an organ with the other "
        "side), q < 0.05, compared within organs, no co-occurrence alert (another gene's altered lines on the same "
        "side, or on the other side), no heavily mutated lines concentrated on the altered side (alterations "
        f"recorded in >= {HYPERMUT_MIN_GENES} driver genes), and an expected false share of the group's arrows of the "
        f"kind below {FALSE_SHARE_ALERT:.0%}. For a response also: not resting on the global-sensitivity correction "
        "and not mostly from drug-doses without any correction; the mean over all its drug-doses going the arrow's "
        f"way, with and without the correction; less than {BOTH_WAYS_A:.0%} of the evidence the other way "
        f"(BOTH_WAYS_A); not a floor (a target that mostly falls and is >= 2x lower at baseline in the altered lines); "
        f"measured in at least {MEASURED_A:.0%} of each side's lines (MEASURED_A). For a baseline arrow: the target "
        f"expressed in more than {1 - BASE_ABSENT_A:.0%} of each side's lines (BASE_ABSENT_A, version 6). For a "
        "selectivity arrow: seen at 2 or more doses of the compound.",
        "  Changed in direction version 5. Old rule: the lines, q, within organs, no co-occurrence, and not resting "
        "on the correction. Why: on the real data ZMAT3 and DDB2 were grade A while the mean over all their "
        "drug-doses went the other way (the arrow rested on its strongest drug-doses) or a smaller fall in the "
        "altered lines could be a floor (2.7x lower at baseline), and GRIN2C was measured in fewer than half of a "
        "side's lines; POLE -> PSPC1 came from a comparison whose random-group false share is 20% and whose altered "
        "side holds three heavily mutated lines. Not adopted: '|retained - 1| >= 0.2' and 'other way < 25%' "
        "(they would demote the core p53 targets CDKN1A, RRM2B and FDXR).",
        f"  Changed in direction version 6. Old rule: a baseline arrow had no such condition. New rule: grade A needs "
        f"the target expressed in more than {1 - BASE_ABSENT_A:.0%} of each side's lines. Why: on the real data TP53 "
        "-> GRIN2C (not expressed in 13 of the 33 TP53-altered lines and 1 of the 17 others) and TP53 -> ACTA2 (11 of "
        "33 and 0 of 17) were grade A, although lines that lack a gene altogether can make a level difference by "
        "lineage. An arrow this rule keeps from A says so in its notes ('grade A blocked since direction version "
        "6').",
        "- **B**: other genotype edges (with alerts, or 3-4 lines) that are not tissue-confounded; expression-null "
        "with >= 5 lines lacking the gene (not tissue-confounded, not in an expression programme); drug_target by "
        "action (inhibitor, activator, unclear).",
        "- **C**: a glimpse: level and level_sensitivity; expression-null with 3-4 lines, tissue-confounded, co-"
        f"absent, resting on the correction, or a natural knockout inside an expression programme (more than "
        f"{NOTE_COABSENT_SETS} other line sets overlap: the direction is not identifiable); a genotype edge that is "
        "tissue-confounded, significant only within its own group, or whose target is absent from most altered "
        f"lines and lies within {CODELETION_BP:,} bp of the source on one chromosome (or without coordinates: a "
        f"shared deletion; version 6); any genotype or null arrow whose source and target lie within "
        f"{SAME_LOCUS_BP:,} bp (same locus); a "
        "drug_target class that traps its target (TOP1 / TOP2 poisons, PARP trappers, microtubule stabilisers).", ""]


def sign_lines():
    return [
        "## How to read a sign", "",
        "- The sign is the effect of the SOURCE's activity. For a level or the cells: +1 raises it, -1 lowers it.",
        "- For a drug response (genotype_response, null_response, level): +1 strengthens the target's response, -1 "
        "weakens it, in the target's own direction at each drug-dose - where the target falls under the drugs, "
        "'strengthens' means it falls further (the source deepens the fall). Read which from all of top_drugdoses "
        "and from rise_share; a target that rises at some drug-doses and falls at others is alerted, and the sign "
        "then says how strongly it responds, not whether the source induces or represses it.",
        "- For a response strength (selectivity kinds): +1 = the lines respond more strongly to the drug-dose where "
        "the source is active.",
        "- Natural knockouts and drug targets are worded 'may': 'lines without X have less Y (X may raise Y's level)', "
        "'compounds annotated to inhibit X lower Y (X activity may raise it)'. A natural knockout is not an "
        "experiment on X, and a compound acts on more than its listed target.",
        "- 0 = not inferred: the mechanism is not recorded; the compounds trap their target (a TOP2 poison raises "
        "TP53 through the DNA damage it causes, not through less TOP2A); same locus; an expression programme.", ""]


def readme(edges, groups, info, sel=None, gene_tests=None):
    und = [x for x in edges.columns if x not in EDGE_DOCS] + [x for x in groups.columns if x not in GROUP_DOCS]
    if sel is not None:
        und += [x for x in sel.columns if x not in SELECTIVITY_DOCS]
    if gene_tests is not None:
        und += [x for x in gene_tests.columns if x not in GENE_TESTS_DOCS]
    cnt = info["edges_by_kind_and_grade"]
    fp = info["false_positive_rate"]
    ef = info["expected_false_edges"]
    gt = info["groups_tested"]
    adj = info["global_sensitivity_correction"]
    tw = info.get("tests_written_by_kind") or {}
    ne = info["edges_by_kind"]
    loc = info.get("same_locus_check") or {}
    nd = ne.get("drug_target", 0)
    nt_dt = tw.get("drug_target", 0)
    sel_in = info.get("selectivity_input") or {}
    lines = [
        "# direction/ - probable direction between genes", "",
        "Directed edges SOURCE -> TARGET, each from a statistical test (p, BH q < 0.10), with an evidence grade and "
        "its reasons for doubt. Nothing that passes is dropped because of doubt: it keeps its place with its alerts "
        "(the `alerts` text starts with ⚠) and a lower grade. A pair without such a test result is not an edge. "
        "Every reason is kept, in one of four tiers (next section). Method: tahoemap/direction.py (module "
        "docstring); a user-facing explanation, with every rule changed in version 5 (old rule, new rule, why): "
        "docs/direction.md.", "",
        *tier_rules_lines(), "",
        "## What direction means here - and what it does not", "",
        "- The source is what the test conditions on: a recorded mutation of the source gene (fixed before the "
        "experiment, so not a consequence of the target), its absence from some lines, its natural level, or "
        "compounds that target its protein. The target is what differs with it: its level, its drug response, the "
        "lines' response strength to a drug, or the cells' growth under a drug.",
        "- It is not proof of direct regulation: A -> B -> C looks like A -> C; another alteration carried by the "
        "same lines can be the cause (see the co-occurrence and heavily-mutated-lines alerts); 'not recorded' is not "
        "proof of wild type.",
        "- One time point (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.",
        "- Drugs act on proteins, not on mRNA; a compound can act on other proteins than its listed target, and a "
        "poison that traps its target on DNA acts through the damage, not through less of the target.",
        "- Level edges come from natural differences between lines; tissue and other differences can mimic them, "
        "and a stronger correlation one way can reflect how precisely each gene's level is measured.", "",
        *grade_lines(), *sign_lines(),
        "## Changed in direction version 5", "",
        "- drug_target: the top-j test replaces 'k of N vs all compounds' (it uses how strongly each compound moves "
        "the target, not only whether it is significant); trap classes (TOP1 / TOP2 poisons, PARP trappers, "
        "microtubule stabilisers) are classes of their own with sign 0 and grade C; destabilisers apart from "
        "stabilisers; memberships from Tahoe and ChEMBL side by side; the words say 'compounds annotated to ...' and "
        "'may'.",
        "- genotype: allele, codon, hotspot and amplification groups; group words with the composition of the lines; "
        "stricter grade A; the group's expected false share; heavily mutated lines; same locus and co-absence; the "
        "response-strength kinds (selectivity).",
        "- natural knockouts: an expression programme (more than 10 overlapping line sets) gives sign 0 and grade C; "
        "random non-partner genes and random line sets give each arrow its non-specific share; the words say 'may'.",
        "- every test has an id (test_id); gene_tests.parquet counts each gene's tests.", "",
        "## Changed in direction version 6", "",
        f"- baseline grade A: the target must be expressed in more than {1 - BASE_ABSENT_A:.0%} of each side's lines "
        "(BASE_ABSENT_A). Old rule: no such condition (TP53 -> GRIN2C and TP53 -> ACTA2 were grade A with the gene "
        "absent from a third of the TP53-altered lines). The arrow gets an alert: present in some lines and absent "
        "in others, so the level difference can follow lineage.",
        f"- a genotype target absent from most altered lines reads 'a shared deletion can explain it' and is grade C "
        f"only when it lies within {CODELETION_BP:,} bp of the source on one chromosome (or when coordinates are "
        "missing). Old rule: always, whatever the distance (TP53 on 17p13 -> EDA2R on Xq12, a p53 target, read as a "
        "shared deletion). Now such an arrow says that lineage, or the loss of the source itself, can explain it, "
        "names a known target of the source, and keeps its grade (at most B).",
        "- every arrow that a rule changed in version 5 or 6 reads differently says so in its notes: 'rule changed "
        "in direction version N: before, ... Now ..., because ...' (trap classes, same locus, expression "
        "programmes, co-absence) or 'grade A blocked since direction version N: ...' (the stricter grade-A rules), "
        "with the same constants as this README.", "",
        "## This run", "",
        f"- {info['edges']:,} edges; groups tested: {gt['genotype']} genotype groups ({gt.get('genotype_by_allele', 0)}"
        f" by allele, codon, hotspot or amplification), {gt['pseudo_controls']} "
        f"pseudo-groups, {gt['expression_null_line_sets']:,} expression-null line sets "
        f"({gt['expression_null_genes']:,} genes; {gt['expression_null_line_sets_across_organs']:,} sets / "
        f"{gt['expression_null_genes_across_organs']:,} genes could not be compared within organs; "
        f"{gt.get('expression_null_line_sets_in_a_programme', 0):,} sets in an expression programme)",
        "- allele groups not testable: " + ("; ".join(gt.get("allele_groups_not_testable") or []) or "none"),
        f"- heavily mutated lines (alterations recorded in >= {HYPERMUT_MIN_GENES} driver genes): " + (", ".join(
            f"{k} {v}" for k, v in (info.get("heavily_mutated_lines") or {}).items()) or "none"),
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
        f"- drug_target: {nd:,} edges = {nt_dt:,} distinct tests ({nd - nt_dt:,} edges repeat a test for another "
        f"listed target); {info['tests'].get('drug_target_classes', 0)} classes tested",
        "- distinct tests among the edges, by kind: " + ", ".join(f"{k} {v:,}" for k, v in tw.items() if ne.get(k)),
        (f"- same-locus check: {loc.get('text')}; same locus (source and target within {SAME_LOCUS_BP:,} bp): "
         f"{loc.get('edges_same_locus', 0):,} of the {loc.get('edges_checked', 0):,} genotype and null arrows to a gene"
         if loc.get("ran") else f"- ⚠ same-locus check: {loc.get('text', 'not run')}"),
        f"- response strength (selectivity): {sel_in.get('drugdoses_with_a_selective_line', 0)} drug-doses with a "
        f"selective line tested, from {sel_in.get('from', '?')}",
        _tier_run_line(info),
        f"- global-sensitivity correction of the (gene, drug-dose) responses: {adj['drug_specific']:,} against the "
        f"drug-dose's other responsive genes, {adj['line_wide']:,} line-wide only, {adj['none']:,} without; the "
        f"lines' overall responsiveness was {'used' if adj['line_wide_check']['used'] else 'not used'} "
        f"({adj['line_wide_check']['why']})",
        "- expected false edges (negative controls; in brackets the 95% upper bound): " + "; ".join(
            _expected_line(k, v) for k, v in ef.items()) + ". " + EXPECTED_FALSE_HOW,
        "- drug_target has no random control: each arrow's alerts say what to doubt.",
        f"- the natural knockouts' random controls took {info.get('null_controls_minutes')} min",
        "- pseudo-groups, edges per group vs real groups: " + "; ".join(
            f"{k} {v['pseudo_edges_mean_per_group']} vs {v['real_edges_mean_per_group']}" for k, v in fp.items())]
    for k, v in fp.items():
        if v.get("pseudo_at_or_above_real"):
            lines.append(f"- ⚠ genotype_{k}: random pseudo-groups give as many edges per group as the real groups "
                         f"({v['pseudo_edges_mean_per_group']} vs {v['real_edges_mean_per_group']}): most of these "
                         "edges may be false; read them as leads")
    for k, v in ef.items():
        if v.get("expected_false") is not None and v["edges"] and v["expected_false"] >= 0.5 * v["edges"]:
            lines.append(f"- ⚠ {k}: the controls expect {v['expected_false']} false edges among the {v['edges']} "
                         "written")
    lines += ["", "## edges.parquet", ""]
    lines += [f"- `{k}`: {v}" for k, v in EDGE_DOCS.items()]
    lines += ["", "## groups.parquet", ""]
    lines += [f"- `{k}`: {v}" for k, v in GROUP_DOCS.items()]
    lines += ["", "## selectivity.parquet", "", "One row per drug-dose: which lines respond selectively to it, and "
              "which comparison groups explain how strongly the lines respond.", ""]
    lines += [f"- `{k}`: {v}" for k, v in SELECTIVITY_DOCS.items()]
    lines += ["", "## gene_tests.parquet", "", "One row per gene, kind and role with a test: how often each gene was "
              "tested, so an arrow can be read against the gene's tests (counted before the candidates were "
              f"trimmed; {info.get('gene_tests_rows', 0):,} rows).", ""]
    lines += [f"- `{k}`: {v}" for k, v in GENE_TESTS_DOCS.items()]
    lines += ["", "## controls.json, info.json", "",
              "- controls.json: positive controls (TP53 -> p53 targets with sign, rank, counted or why not; TP53 -> "
              "cells under DNA-damaging drugs; TP53 -> response strength to DNA-damaging drugs; KRAS p.G12C -> "
              "response to Adagrasib; KEAP1 -> NRF2 targets when KEAP1 is recorded in enough lines); negative "
              "controls (pseudo-groups counted at the real family's BH cut: the false edges a group without any "
              "effect adds); null_controls (random non-partner genes per overlap bin, random line sets); "
              "permuted-level controls for the level kinds; the expected false edges per kind.",
              "- info.json: counts per kind and grade, groups and tests, distinct tests by kind, the same-locus "
              "check, the BH cuts, the fitted null tails, the level kinds' calibration, the grade-A constants, "
              "settings, peak memory, minutes.", ""]
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
