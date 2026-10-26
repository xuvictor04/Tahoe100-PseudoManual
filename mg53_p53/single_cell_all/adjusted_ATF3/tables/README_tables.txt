SENSITIVITY RUN: every model also adjusts for log((count + 0.5) / total UMI) of ATF3; outcomes that contain these genes are not fitted.

Tables of single_cell_all.py (D1b at full scale; re-created by: python3 single_cell_all.py). ASSOCIATIONS ONLY:
Tahoe has no MG53 perturbation and measures mRNA, so 'TRIM72-detected cells carry X% more p53-target mRNA' says nothing
causal about MG53 -> p53, and p53 activity is read from its target genes' mRNA. The TP53 genotype is the control: an MG53
-> p53 effect can only act where p53 works, so the PRIMARY ESTIMAND is the TRIM72 log rate ratio in TP53-WT lines minus
that in TP53-altered lines ('WT minus altered'); what is equal in both groups is not via p53.

Model, per (well, cell line) group: quasi-Poisson GLM (IRLS, log link, dispersion = Pearson chi2/df floored at 1) of an
outcome's per-cell counts on 'predictor gene detected (>= 1 UMI)' + log(total UMI) + log S-phase fraction + log G2M
fraction (fractions = (module counts + 0.5) / total UMI), offset log(total UMI); same model as downstream_p53.py (d).
Groups: >= 50 cells, >= 5 TRIM72-detected and >= 5 undetected cells, line expresses TRIM72 (atlas
expr_mask), TP53 group known, not a failed well. Cells: a uniform random subsample of at most 2000 cells per group (0 =
all; Bernoulli, seed 20261025 per file). A fit (predictor x outcome x group) needs outcome counts >= 20, expected outcome
counts in the predictor-detected cells >= 5.0 and a gene outcome expressed in the line; fits where the outcome is
entirely in one arm (separation) or that did not converge are dropped (checks.csv counts them).
Meta-analysis: two-stage DerSimonian-Laird (DL) random effects: stage 1 over the wells of a (line, well class), stage 2
over lines within a TP53 group (17 WT / 33 altered lines annotated; 17 / 30 have fitted groups: NCI-H661 does not express
TRIM72, NCI-H2122 and NCI-H596 have too few TRIM72-detected cells; lines are the units because the same lines repeat in
every well). STAGE-2 INFERENCE (headline): Hartung-Knapp (HK) SE of the DL mean, se = sqrt(max(1, q) / sum w*) with q =
sum w* (b - mean)^2 / (k - 1) (hk_scale = q; the floor at 1 keeps it never narrower than DL), and t on k - 1 df (k =
lines). 'WT minus altered' = difference of the two stage-2 means, se = sqrt(se_WT^2 + se_altered^2) (HK), t on the
Welch-Satterthwaite df (df_diff). CIs use these t quantiles. The DL normal SE / CI / p of the earlier version are kept as
se_DL, ci_lo_DL, ci_hi_DL, p_DL (narrower; secondary). Stage-1 (wells within a line) stays DL normal. p_perm = TP53-label
permutation over lines (10000 permutations; the line-level estimates are fixed and the WT / altered split of the lines
with data is reshuffled; unaffected by the HK change). 'paired' = per well, inverse-variance mean of the WT groups minus
that of the altered groups, then DL over wells (compares lines only within the same well, so drug and well effects
cancel); its p (paired_p_perm) comes from reshuffling the TP53 labels of the lines (1000 permutations; scores,
primary outcomes, ATF3, PMAIP1), because a normal p over wells would treat the same lines in every well as independent.
All p-values are two-sided. Placebo-based empirical p-values cannot go below 1 / (n placebos + 1) (1/17 with 16
placebos).
Well classes: DMSO; 'TRIM72 raisers' = drug-doses with the gene panel's TRIM72 call 'up' (21); 'p53 activators' =
P53_ACTIVITY z >= 3 and FDR < 0.10 and not a raiser; 'other drugs' = the rest; 'all wells' = all of them.
Outcomes: P53_SCORE = counts of the 21 P53_ACTIVITY members summed; P53_PRIMARY5 = MDM2+CDKN1A+FDXR+ZMAT3+DDB2 summed;
NFKB_SCORE = NFKBIA+TNFAIP3+CXCL8 (gene_modules.csv NF-kB), NFKB8_SCORE = the gene panel's 8 NF-kB targets;
FERROPTOSIS_SCORE = SLC7A11+GPX4+CHAC1; APOPTOSIS_SCORE = BAX+BBC3+PMAIP1; single genes as named. The p53 outcomes are 24
unique read-outs (P53_SCORE, P53_PRIMARY5, TP53 and the 21 score members). Placebo outcomes: the 66 non-p53-linked,
non-screen panel genes (modules_and_gene_sets.csv). Placebo predictors (detection rate within 1/3.0x-3.0x of TRIM72's in
the fitted groups, not p53-linked, not a screen gene): ABCG2, NLRP3, AIM2, GSDMD, OSGIN1, SDF2L1, IL1B, AKR1B10, NAPEPLD, ABCB1, CDKN2B, AKR1C2, PSPH, HMOX1, GSDME, IRF7.
Ambient negative controls (predictors fitted only in their lines, same model, same groups): 'CDKN2A detected' in the
CDKN2A-deleted lines and 'MTAP detected' in the MTAP-null lines (gene panel p53_functional_status.csv flags) whose reads of
that gene are < 0.3 x the ambient expectation (ambient_control_lines.csv): CDKN2A: A-172, A-427, A498, A549, H4, LOX-IMVI, MIA PaCa-2, NCI-H460, PANC-1, Panc 03.27, SW 1088, SW 1271, SW 900; MTAP: A-172, H4, MIA PaCa-2, PANC-1, SW 1088, SW 900. Every such read is soup
or cross-contamination, so these show what pure ambient capture does to the outcomes.
Cap-0 sample: groups with a binomial probability > 1e-6 of falling below 5 TRIM72-detected (or undetected) cells
under the cap are 'at risk'; a random 0.2 of them (seeded) is also fitted with all its cells in the same pass. The
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
                           mg53_perturbation/assay_panel/panel.csv); placebo gene lists; ambient-control lines; modules of
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
