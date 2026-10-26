Tables of single_cell_all.py (D1b at full scale; re-created by: python3 single_cell_all.py). ASSOCIATIONS ONLY:
Tahoe has no MG53 perturbation and measures mRNA, so 'TRIM72-detected cells carry X% more p53-target mRNA' says nothing
causal about MG53 -> p53, and p53 activity is read from its target genes' mRNA. The TP53 genotype is the control: an MG53
-> p53 effect can only act where p53 works, so the PRIMARY ESTIMAND is the TRIM72 log rate ratio in TP53-WT lines minus
that in TP53-altered lines ('WT minus altered'); what is equal in both groups is not via p53.

Model, per (well, cell line) group: quasi-Poisson GLM (IRLS, log link, dispersion = Pearson chi2/df floored at 1) of an
outcome's per-cell counts on 'predictor gene detected (>= 1 UMI)' + log(total UMI) + log S-phase fraction + log G2M
fraction (fractions = (module counts + 0.5) / total UMI), offset log(total UMI); same model as downstream_p53.py (d).
Groups: >= 50 cells, >= 5 TRIM72-detected and >= 5 undetected cells, line expresses TRIM72 (atlas expr_mask),
TP53 group known, not a failed well. Cells: a uniform random subsample of at most 2000 cells per group (0 = all; Bernoulli,
seed 20261025 per file). A fit (predictor x outcome x group) needs outcome counts >= 20, expected outcome counts in the
predictor-detected cells >= 5.0 and a gene outcome expressed in the line; fits where the outcome is entirely in one arm
(separation) or that did not converge are dropped (checks.csv counts them).
Meta-analysis: two-stage DerSimonian-Laird random effects: stage 1 over the wells of a (line, well class), stage 2 over
lines within a TP53 group (17 WT / 33 altered lines annotated; 17 / 30 have fitted groups: NCI-H661 does not express
TRIM72, NCI-H2122 and NCI-H596 have too few TRIM72-detected cells; lines are the units because the same lines repeat in
every well). WT minus altered = difference of the two stage-2 means, SE = sqrt(sum of squared SEs); p_perm = TP53-label
permutation over lines (10000 permutations; the line-level estimates are fixed and the WT / altered split of the lines
with data is reshuffled). 'paired' = per
well, inverse-variance mean of the WT groups minus that of the altered groups, then DL over wells (compares lines only
within the same well, so drug and well effects cancel); its p (paired_p_perm) comes from reshuffling the TP53 labels of
the lines (1000 permutations; scores, primary outcomes, ATF3, PMAIP1), because a normal p over wells would treat
the same lines in every well as independent.
All p-values are two-sided. Placebo-based empirical p-values cannot go below 1 / (n placebos + 1) (1/17 = 0.059).
Well classes: DMSO; 'TRIM72 raisers' = drug-doses with the gene panel's TRIM72 call 'up' (21); 'p53 activators' =
P53_ACTIVITY z >= 3 and FDR < 0.10 and not a raiser; 'other drugs' = the rest; 'all wells' = all of them.
Outcomes: P53_SCORE = counts of the 21 P53_ACTIVITY members summed; P53_PRIMARY5 = MDM2+CDKN1A+FDXR+ZMAT3+DDB2 summed;
NFKB_SCORE = NFKBIA+TNFAIP3+CXCL8 (panel.csv NF-kB), NFKB8_SCORE = the gene panel's 8 NF-kB targets; FERROPTOSIS_SCORE =
SLC7A11+GPX4+CHAC1; APOPTOSIS_SCORE = BAX+BBC3+PMAIP1; single genes as named. Placebo outcomes: the 66 non-p53-linked,
non-screen panel genes (modules_and_gene_sets.csv). Placebo predictors (detection rate within 1/3.0x-3.0x of TRIM72's in the
fitted groups, not p53-linked, not a screen gene): ABCG2, NLRP3, AIM2, GSDMD, OSGIN1, SDF2L1, IL1B, AKR1B10, NAPEPLD, ABCB1, CDKN2B, AKR1C2, PSPH, HMOX1, GSDME, IRF7.
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
