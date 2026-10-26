Tables of two_way.py (re-created by: python3 two_way.py --data <Tahoe-100M folder>). Associations only: Tahoe
has no MG53 perturbation and measures mRNA; p53 activity = transcription of p53 target genes.

Unit: one drug-dose x cell line cell. Values are method-v3 corrected log2 effects r2 (plate x line baseline ->
composition shift -> two-pass position correction) per (well, line), averaged over the drug-dose's used wells
(profiles with >= 30 cells): panel genes from the panel's T.expression_effects (downstream_p53's cache builder), other
genes from upstream_coregulation.corrected_effects() on atlas/pseudobulk. P53_SCORE = mean r2 of the 21 P53_ACTIVITY
members the line expresses. TP53 groups: the panel's (17 WT, 33 altered).
Model per read-out Y: Y = drug-dose FE + line FE + b_WT TRIM72 x WT + b_alt TRIM72 x altered + covariates x TP53
group. Covariate sets: full = DD_beta (0 where the drug-dose has no consensus response, < 20 significant genes),
DD_A (relative abundance), S and G2M per-line effects (DD_r2_modules), bg_abs_r2 (mean |r2| over the panel genes
that are not p53-related, not screen genes, not TRIM72); no_cycle = full without S and G2M (for cell-cycle read-outs,
which overlap those modules); none = fixed effects only. Units: b = log2 change in the read-out per log2 change in
TRIM72 (both corrected effects); *_per_sd_TRIM72 = per SD of the residual TRIM72 (FE and covariates out).
full_base = full + trim72_base_x_dd (the line's untreated TRIM72 level, log2 DMSO CPM z-scored over lines, x the
drug-dose's TRIM72 log2FC from the atlas: low-baseline lines get larger TRIM72 folds under a raiser).
NCI-H2122 and NCI-H596 have no DD_A (too few cells for the atlas growth analysis) and drop out of models with
covariates.
Primary estimand diff = b_WT - b_alt (negative = more TRIM72 with less p53 output only where p53 works); primary
p = p_diff_tp53_label_perm: TP53 labels permuted over lines (group sizes kept, the whole model refitted), statistic
t = diff / line-cluster SE (studentised, so a WT group with a larger spread than the altered group does not inflate
it); p_diff_tp53_label_perm_unstudentised permutes diff itself.

d1_two_way_models.csv     one row per read-out (P53_SCORE, MDM2, CDKN1A, FDXR, ZMAT3, DDB2, TP53I3, BBC3, TP53) x
                          variant x covariate set (full, none, full_base). Variants: i_all (all drug-doses),
                          ii_active (TRIM72 |z| >= 3 or
                          P53_ACTIVITY z >= 3; drugdose_sets.csv), ii_active_no_plate3_13 (the same without the
                          plate-3 / plate-13 wells), iii_readthrough (X = TRIM72_rt), iv_no_plate3_13 (wells of
                          plates 3 and 13 left out, drug-dose means and covariates recomputed).
                          Columns: n_rows / n_drugdoses / n_drugs / n_lines_WT / n_lines_alt; b_WT, b_alt with drug-
                          cluster SE (CR1), 95% CI (t, G-1 df), p_*_drug, two-way (drug, line) cluster SE/p, within-
                          drug-dose permutation p (TRIM72 shuffled across lines within each drug-dose); diff with
                          drug-cluster, line-cluster and two-way SE/CI/p, p_diff_perm_within_dd and its null SD,
                          t_diff_line, p_diff_tp53_label_perm (studentised; primary), the unstudentised version and
                          the null SD of diff (ci_diff_*_labelsd = diff +- 1.96 SD), mde_diff_80 = 2.80 x label-
                          permutation SD (smallest |b_WT - b_alt| detectable with 80% power, two-sided 5%),
                          mde_diff_80_line_se = 2.80 x line-cluster SE, mde_diff_80_within_dd from the within-drug-
                          dose null; b_common (one
                          slope for all lines); sd_TRIM72_resid_*, sd_Y_resid; attenuation_lambda_split_half (the
                          split-half reliability of the residual TRIM72 for that variant's cells, trim72_reliability.csv)
                          and mde_diff_80_attenuation_corrected = mde_diff_80 / lambda; q_bh_diff_label = BH over the
                          read-outs within variant x covariate set; check_label_engine_minus_main and
                          check_label_engine_t_minus_main (the permutation engine at the observed labels minus the
                          main fit: should be ~0).
d1_line_slopes.csv        variant i_all (full covariates) and ii_active: per line, the TRIM72 slope from one model with
                          line-specific TRIM72 AND covariate slopes (both FE), drug-cluster SE.
d1_line_slope_tests.csv   per read-out: mean line slope WT minus altered (lines with >= 20 cells of data), Welch t,
                          TP53-label permutation p of the Welch t (and of the plain difference), MDE from the
                          permutation SD of the difference; counts of negative slopes.
d1_per_drugdose_contributions.csv  i_all and ii_active (full covariates): per drug-dose and read-out, its rows' share
                          of the WT / altered TRIM72 variation (weight_share_*), its own slope on the partialled data
                          (slope_*_in_drugdose) and its contribution to b_WT, b_alt and diff (contrib_*: sum over its
                          rows of x~ y~ / total sum of x~^2; they add up to b_WT / b_alt up to the WT-altered cross term).
d1_active_leave_one_drug_out.csv  ii_active (full): the model refitted without each drug (all its doses): b_WT, b_alt,
                          diff, line-cluster and two-way p, next to the all-drug diff.
d2_screen_models.csv      the same model (variant i_all) for each MG53-linked gene and module (module = mean r2 of
                          the members a line expresses) of mg53_perturbation/assay_panel/panel.csv: NF-kB (NFKBIA,
                          TNFAIP3, CXCL8 + module), ferroptosis (SLC7A11, GPX4, CHAC1), apoptosis (BAX, MCL1, PMAIP1),
                          stress (ATF3, DDIT3 + module), PI3K-AKT/FOXO/FAK (TXNIP, IRS1, PTK2), cell cycle (CCND1,
                          KIF11), E2F targets (E2F1, CCNE1, CDT1, MCM3, MCM7, MYBL2, CDC25A + module; none in the
                          S_PHASE module), RAC1. primary = the covariate set used for the BH family (no_cycle for the
                          cell-cycle and E2F read-outs, full otherwise); q_bh_* over the primary rows: diff
                          (studentised TP53-label permutation p), b_common, b_WT and b_alt (two-way (drug, line)
                          cluster p; the within-drug-dose permutation p, also given, tests 'no association in any
                          drug-dose' and rejects whenever slopes vary across drugs, even with a zero mean). Non-primary rows
                          (full covariates for the cell-cycle read-outs) are sensitivity rows (no q).
                          source = panel (T.expression_effects) or pseudobulk (corrected_effects).
readthrough_correction_fit.csv  TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (all drug-doses):
                          slopes, drug-cluster SE, within-R2 (share of TRIM72's within variation explained);
                          PYCARD-AS1 r2 is kept in every line (it is below the atlas gene list).
trim72_reliability.csv    (v) measurement error of TRIM72: split-half (each well x line's cells split at random into
                          two halves, the panel's method run on each half, halves averaged per drug-dose like the
                          main data) and replicate wells (drug-doses with 2+ used wells on different plates: first
                          two wells; split-half is also given for those drug-doses alone, for comparison: the gap
                          between the two is plate-specific line variation). r_halves = correlation of the residual
                          TRIM72 (FE + covariates x group out, and
                          FUS / PYCARD-AS1 for the readthrough row) between the halves / wells;
                          reliability_full_spearman_brown = 2r/(1+r) (the full-data measure from two halves);
                          attenuation: observed b ~= lambda x true b for classical, independent measurement error.
drugdose_sets.csv         per drug-dose: TRIM72 z, P53_ACTIVITY z (panel), plates, whether in ii_active and in
                          iv_no_plate3_13.
analysis_cells.csv.gz     the per (drug-dose, line) values of the main data (all used wells): TRIM72 r2, TRIM72_rt,
                          D1 read-outs, screen read-outs, covariates, TRIM72 halves A and B.
checks.csv                pseudobulk vs gene_panel counts; corrected_effects vs the panel r2 and the atlas DD_lfc;
                          idarubicin per-line TRIM72 vs trim72_idarubicin/corrected; split-half bookkeeping.
key_results.csv           the headline numbers (D1 primary rows, line-slope tests, screen hits at q < 0.1,
                          reliability).
