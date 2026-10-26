Tables of two_way.py (re-created by: python3 two_way.py --data <Tahoe-100M folder>). Associations only: Tahoe
has no MG53 perturbation and measures mRNA; p53 activity = transcription of p53 target genes.

Unit: one drug-dose x cell line cell. Values are method-v3 corrected log2 effects r2 (plate x line baseline ->
composition shift -> two-pass position correction) per (well, line), averaged over the drug-dose's used wells
(profiles with >= 30 cells): panel genes from the panel's T.expression_effects (downstream_p53's cache builder), other
genes from upstream_coregulation.corrected_effects() on atlas/pseudobulk. P53_SCORE = mean r2 of the 21 P53_ACTIVITY
members the line expresses. TP53 groups: the panel's (17 WT, 33 altered).

Model per read-out Y: Y = FE + b_WT TRIM72 x WT + b_alt TRIM72 x altered + covariates x TP53 group. Two FE
structures (column fe):
  dd    drug-dose FE + line FE, as specified. Its drug-dose effect is shared by both TP53 groups, so the WT-only p53
        response of a drug-dose (what every p53 activator produces) stays in the WT residuals; wherever the
        drug-dose's TRIM72 response also differs between the groups (a WT lean among the raisers: p53_dependence)
        that drug-level gap enters b_WT - b_alt. The TP53-label permutation does not protect against it (it breaks
        the gap). Example: ii_active without covariates, P53_SCORE t_diff_line -10.4 with fe dd, -3.2 with ddxg.
  ddxg  drug-dose x TP53-group FE + line FE: each drug-dose has its own WT mean and its own altered mean, so
        b_WT and b_alt come only from line-to-line variation inside the same group and the same wells (more TRIM72
        than the other WT lines of that well, more or less p53 output than them). Exactly two separate regressions
        (WT lines, altered lines) sharing nothing. Preferred for the D1 question; both are reported.
Covariate sets: full = DD_beta (0 where the drug-dose has no consensus response, < 20 significant genes), DD_A
(relative abundance), S and G2M per-line effects (DD_r2_modules), bg_abs_r2 (mean |r2| over the 78 panel genes that
are not p53-related, not screen genes, not TRIM72; checks.csv lists them); no_cycle = full without S and G2M (for
cell-cycle read-outs, which overlap those modules); none = fixed effects only; full_base = full + trim72_base_x_dd
(the line's untreated TRIM72 level, log2 DMSO CPM z-scored over lines, x the drug-dose's TRIM72 log2FC from the
atlas: low-baseline lines get larger TRIM72 folds under a raiser); full_p53resp = full + p53resp_x_dd (the line's
p53 responsiveness from gene_panel/results/p53_functional_status.csv, z over lines, x the drug-dose's P53_ACTIVITY
z: a line that answers p53 activators strongly does so in every such drug-dose, whatever its TRIM72).
NCI-H2122 and NCI-H596 have no DD_A (too few cells for the atlas growth analysis) and drop out of models with
covariates. Units: b = log2 change in the read-out per log2 change in TRIM72 (both corrected effects);
*_per_sd_TRIM72 = per SD of the residual TRIM72 (FE and covariates out).
Inference for diff = b_WT - b_alt (negative = more TRIM72 goes with less p53 output only where p53 works):
p_diff_twoway (two-way (drug compound, line) cluster-robust SE, t with min(G)-1 df) allows for both drug-level and
line-level dependence; p_diff_tp53_label_perm permutes the TP53 labels over the analysed lines (group sizes kept,
whole model refitted, FE included for ddxg; statistic t = diff / line-cluster SE, studentised) and is the
design-based line-level test, conditional on the drug-doses analysed (it ignores drug-to-drug variation, so in the
62 active drug-doses from 37 drugs it can be far smaller than the two-way p). Read a diff as supported only when
both are small under fe ddxg. MDE: mde_diff_80 = 2.80 x the SD of the label-permutation null of diff (smallest
|b_WT - b_alt| detected with 80% power, two-sided 5%).

d1_two_way_models.csv     one row per read-out (P53_SCORE, MDM2, CDKN1A, FDXR, ZMAT3, DDB2, TP53I3, BBC3, TP53) x
                          fe x variant x covariate set. Variants: i_all (all drug-doses; covariates full, none,
                          full_base, full_p53resp), ii_active (TRIM72 |z| >= 3 or P53_ACTIVITY z >= 3, 62 drug-doses;
                          full, none, full_base, full_p53resp), ii_trim72 (TRIM72 |z| >= 3 only, 23), ii_p53 (P53_ACTIVITY
                          z >= 3 only, 50), ii_active_no_plate3_13 (ii_active without the plate-3 / plate-13 wells),
                          iii_readthrough (X = TRIM72_rt, readthrough_correction_fit.csv), iv_no_plate3_13 (wells of
                          plates 3 and 13 left out, drug-dose means and covariates recomputed); drugdose_sets.csv.
                          Columns: n_rows / n_drugdoses / n_fe_cells / n_drugs / n_lines_WT / n_lines_alt; b_WT, b_alt
                          with drug-cluster SE (CR1), 95% CI (t, G-1 df), p_*_drug, two-way (drug, line) cluster SE/p,
                          within-cell permutation p (TRIM72 shuffled across lines within each FE cell: drug-dose for
                          dd, drug-dose x group for ddxg; tests b = 0 and rejects whenever slopes vary across drugs,
                          even with a zero mean); diff with drug-cluster, line-cluster and two-way SE/CI/p,
                          p_diff_perm_within_dd and its null SD, t_diff_line, p_diff_tp53_label_perm (studentised),
                          the unstudentised version, the null SD of diff (ci_diff_*_labelsd = diff +- 1.96 SD),
                          mde_diff_80, mde_diff_80_line_se = 2.80 x line-cluster SE, mde_diff_80_within_dd from the
                          within-cell null; b_common (one slope for all lines) with CI/p; sd_TRIM72_resid_*,
                          sd_Y_resid; attenuation_lambda_split_half (split-half reliability of the residual TRIM72 for
                          that variant, fe and covariate set; trim72_reliability.csv) and
                          mde_diff_80_attenuation_corrected = mde_diff_80 / lambda; q_bh_diff_label and
                          q_bh_diff_twoway = BH over the 9 read-outs within fe x variant x covariate set;
                          check_label_engine_minus_main and check_label_engine_t_minus_main (the permutation engine at
                          the true labels minus the main fit: ~1e-16).
d1_line_slopes.csv        i_all and ii_active (full covariates), both fe: per line, the TRIM72 slope from one model with
                          line-specific TRIM72 AND covariate slopes (both FE), drug-cluster SE.
d1_line_slope_tests.csv   per read-out x variant x fe: mean line slope WT minus altered (lines with >= 20 cells of
                          data), Welch t, TP53-label permutation p of the Welch t (and of the plain difference), MDE
                          from the permutation SD of the difference; counts of negative slopes. For fe ddxg the slopes
                          are not refitted per permutation (the FE depend on the labels): approximate.
d1_per_drugdose_contributions.csv.gz  i_all and ii_active (full covariates), both fe: per drug-dose and read-out, its
                          rows' share of the WT / altered TRIM72 variation (weight_share_*), its own slope on the
                          partialled data (slope_*_in_drugdose) and its contribution to b_WT, b_alt and diff (contrib_*:
                          sum over its rows of x~ y~ / total sum of x~^2; they add up to b_WT / b_alt, exactly for
                          ddxg, up to the small WT-altered cross term for dd).
d1_active_leave_one_drug_out.csv  ii_active (full), both fe: the model refitted without each drug (all its doses):
                          b_WT, b_alt, diff, line-cluster and two-way p, next to the all-drug diff.
d1_gene_null_genes.csv    gene-level null (is the pattern specific to p53 targets?): i_all and ii_active, full
                          covariates, both fe: the same model (b_WT, b_alt, diff, two-way SE, t, p; no permutations)
                          for the D1 read-outs, each of the 21 P53_ACTIVITY members, each of the 78 non-p53
                          background panel genes and 500 random modules of 21 background genes (set column).
d1_gene_null_summary.csv  each D1 read-out's two-way t placed in its reference: P53_SCORE among the random background
                          modules, single genes among the background genes (reference mean / SD of diff and t,
                          fraction of reference t <= observed, empirical two-sided p); and the 21 members' t vs the
                          background genes' t (Mann-Whitney p). The modules share genes, lines and drug-doses, so
                          this is a competitive (specificity) test, not a test of a non-zero diff: a read-out can sit
                          outside the module null while its own CI includes 0. Caveat: the background genes also
                          make up bg_abs_r2 (a covariate).
d2_screen_models.csv      the same model (variant i_all, both fe) for each MG53-linked gene and module (module = mean
                          r2 of the members a line expresses) of mg53_perturbation/assay_panel/panel.csv: NF-kB
                          (NFKBIA, TNFAIP3, CXCL8 + module), ferroptosis (SLC7A11, GPX4, CHAC1), apoptosis (BAX,
                          MCL1, PMAIP1), stress (ATF3, DDIT3 + module), PI3K-AKT/FOXO/FAK (TXNIP, IRS1, PTK2), cell
                          cycle (CCND1, KIF11), E2F targets (E2F1, CCNE1, CDT1, MCM3, MCM7, MYBL2, CDC25A + module;
                          none in the S_PHASE module), RAC1. primary = the covariate set of the BH family (no_cycle for
                          the cell-cycle and E2F read-outs, full otherwise); q_bh_* = BH over the primary rows within
                          each fe: diff (label-permutation p and two-way p), b_common, b_WT and b_alt (two-way p).
                          Non-primary rows (full covariates for the cell-cycle read-outs) are sensitivity rows (no q).
                          source = panel (T.expression_effects), pseudobulk (corrected_effects) or module.
readthrough_correction_fit.csv  TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line FE (all drug-doses):
                          slopes, drug-cluster SE, within-R2 (share of TRIM72's within variation explained);
                          PYCARD-AS1 r2 is kept in every line (it is below the atlas gene list).
trim72_reliability.csv    (v) measurement error of TRIM72, per variant, fe and covariate set (covset full / none):
                          split-half (each well x line's cells split at random into two halves, the panel's method
                          run on each half, halves averaged per drug-dose like the main data) and replicate wells
                          (drug-doses with 2+ used wells on different plates: first two wells; split-half is also given
                          for those drug-doses alone: the gap between the two is well- or plate-specific line
                          variation that both halves of a well share but another well does not). r_halves =
                          correlation of the residual TRIM72 (FE + covariates x group out, and FUS / PYCARD-AS1 for
                          the readthrough row) between the halves / wells; reliability_full_spearman_brown =
                          2r/(1+r) (the full-data measure from two halves); attenuation: observed b ~= lambda x true
                          b for classical, independent measurement error.
drugdose_sets.csv         per drug-dose: TRIM72 z, P53_ACTIVITY z (panel), plates, membership of ii_trim72, ii_p53,
                          ii_active and iv_no_plate3_13.
analysis_cells.csv.gz     the per (drug-dose, line) values of the main data (all used wells): TRIM72 r2, TRIM72_rt,
                          D1 read-outs, screen read-outs, covariates (incl. trim72_base_x_dd, p53resp_x_dd),
                          TRIM72 halves A and B.
checks.csv                pseudobulk vs gene_panel counts; corrected_effects vs the panel r2 and the atlas DD_lfc;
                          idarubicin per-line TRIM72 vs trim72_idarubicin/corrected; split-half bookkeeping; the
                          permutation engines (fast within-cell refit vs explicit projection; label engines at the
                          true labels vs the main fit) for both fe.
key_results.csv           the headline numbers: D1 rows (all read-outs for i_all and ii_active with full covariates,
                          P53_SCORE for every variant), line-slope tests, leave-one-drug-out ranges, the gene-level
                          null (P53_SCORE and the members), D2 rows with
                          q < 0.1 and the D2 MDE range, reliability, readthrough fit. Columns p_twoway, p_label_perm,
                          q_twoway, q_label, mde_80 as defined above.
