Tables of two_way.py (re-created by: python3 two_way.py --data <Tahoe-100M folder>). Associations only: Tahoe
has no MG53 perturbation and measures mRNA; p53 activity = transcription of p53 target genes.

PRIMARY TEST (the first row of key_results.csv): fe ddxg, variant i_all (all 1,132 drug-doses), covariate set
full, read-out P53_SCORE; estimand b_WT - b_alt; p and 95% CI from the conservative two-way SE. Declared in the
verifier round, after a first run, as the design the step specified from the start (the data set as specified, the
FE structure already named the preferred reading, the specified covariates): not preregistered. The other read-outs
of that model are 'secondary'; every other fe x variant x covariate-set row is 'sensitivity' (column role in
d1_two_way_models.csv and key_results.csv). For a claim from any of the 9 variants, P53_SCORE has a Holm adjustment
over the variants (p_holm_variants_*). An ii_active result is a sensitivity result, read with the Holm column.

Headline numbers of this run (P53_SCORE, b_WT - b_alt, fe ddxg, full covariates; key_results.csv):
  primary (i_all)  -0.0032 (95% CI -0.0085 to +0.0022; conservative two-way p 0.24; label-permutation p 0.26).
  ii_active        -0.030 (CI -0.054 to -0.006; two-way p 0.015, label p 0.018; Holm over the 9 variants 0.12 and
                   0.14). Not robust: with the line FE from all drug-doses (d1_active_joint_model.csv) -0.018 (p 0.22),
                   difference-in-differences active minus inactive -0.015 (p 0.29). Every single drug or line left
                   out keeps two-way p < 0.05 (largest 0.039 and 0.046). Line slopes: mean WT - altered -0.024
                   (Welch p 0.040), Hodges-Lehmann -0.018 (Mann-Whitney p 0.064). The 21 members as a set vs the
                   background genes: camera-style p 0.013 (i_all: 0.31).
  readthrough      FUS and PYCARD-AS1 r2 as covariates: i_all -0.0031 (p 0.19), ii_active -0.029 (p 0.032).

Unit: one drug-dose x cell line cell. Values are method-v3 corrected log2 effects r2 (plate x line baseline ->
composition shift -> two-pass position correction) per (well, line), averaged over the drug-dose's used wells
(profiles with >= 30 cells): panel genes from the panel's T.expression_effects (downstream_p53's cache builder), other
genes from upstream_coregulation.corrected_effects() on atlas/pseudobulk. P53_SCORE = mean r2 of the 21 P53_ACTIVITY
members the line expresses. TP53 groups: the panel's (17 WT, 33 altered). NCI-H661 (altered) does not express
TRIM72 by the panel's rule, so it has no TRIM72 value: models have at most 17 WT + 32 altered lines; NCI-H2122 and
NCI-H596 have no DD_A (too few cells for the atlas growth analysis) and drop out of every model with covariates
(17 WT + 30 altered lines).

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
        (WT lines, altered lines) sharing nothing. The FE of the primary test; dd rows are sensitivity rows.
Covariate sets: full = DD_beta (0 where the drug-dose has no consensus response, < 20 significant genes), DD_A
(relative abundance), S and G2M per-line effects (DD_r2_modules), bg_abs_r2 (mean |r2| over the 78 panel genes that
are not p53-related, not screen genes, not TRIM72; checks.csv lists them); no_cycle = full without S and G2M (for
cell-cycle read-outs, which overlap those modules); none = fixed effects only; full_base = full + trim72_base_x_dd
(the line's untreated TRIM72 level, log2 DMSO CPM z-scored over lines, x the drug-dose's TRIM72 log2FC from the
atlas: low-baseline lines get larger TRIM72 folds under a raiser); full_p53resp = full + p53resp_x_dd (the line's
p53 responsiveness from gene_panel/results/p53_functional_status.csv, z over lines, x the drug-dose's P53_ACTIVITY
z: a line that answers p53 activators strongly does so in every such drug-dose, whatever its TRIM72); full_rt =
full + FUS r2 + PYCARD-AS1 r2 (readthrough from FUS, each x TP53 group like the other covariates). Units: b = log2
change in the read-out per log2 change in TRIM72 (both corrected effects); *_per_sd_TRIM72 = per SD of the
residual TRIM72 (FE and covariates out).
Inference for diff = b_WT - b_alt (negative = more TRIM72 goes with less p53 output only where p53 works):
p_diff_twoway / ci_diff_*_twoway use the conservative two-way cluster SE, sqrt(max(V_drug + V_line - V_inter,
V_drug, V_line)) (drug compound and line clusters, CR1; t with min(G)-1 df): the plain two-way variance V_drug +
V_line - V_inter can fall below a one-way variance (for diff in 106 of the 270 D1 rows: 86 below V_line, 20 below
V_drug; e.g. P53_SCORE ii_active ddxg full: SE 0.0101 -> 0.0118, p 0.0054 -> 0.015, Holm over the variants 0.12),
so the larger of the three is used for every two-way SE, CI, p and q in these tables (also b_WT, b_alt, b_common,
the D2 q-values, the gene-level null, leave-one-out and joint-model tables). se_diff_twoway_from says which term
gave it; se_diff_twoway_cgm / p_diff_twoway_cgm keep the plain two-way value (the earlier p_diff_twoway, with the
larger one-way SE only where V2 <= 0), for comparison only. p_diff_tp53_label_perm permutes the TP53 labels over
the analysed lines (group sizes kept, whole model refitted, FE included for ddxg; statistic t = diff / line-cluster
SE, studentised) and is the design-based line-level test, conditional on the drug-doses analysed (it ignores
drug-to-drug variation, so in the 62 active drug-doses from 37 drugs it can be far smaller than the two-way p: fe
dd, P53_SCORE ii_active full, label p 0.028 vs two-way p 0.53). Read
a diff as supported only when both are small under fe ddxg. MDE: mde_diff_80 = 2.80 x the SD of the
label-permutation null of diff (smallest |b_WT - b_alt| detected with 80% power, two-sided 5%).

d1_two_way_models.csv     one row per read-out (P53_SCORE, MDM2, CDKN1A, FDXR, ZMAT3, DDB2, TP53I3, BBC3, TP53) x
                          fe x variant x covariate set; role = primary / secondary / sensitivity (above). Variants:
                          i_all (all drug-doses; covariates full, none, full_base, full_p53resp), ii_active (TRIM72
                          |z| >= 3 or P53_ACTIVITY z >= 3, 62 drug-doses; full, none, full_base, full_p53resp),
                          ii_trim72 (TRIM72 |z| >= 3 only, 23), ii_p53 (P53_ACTIVITY z >= 3 only, 50),
                          ii_active_no_plate3_13 (ii_active without the plate-3 / plate-13 wells, 58),
                          iii_readthrough_cov (all drug-doses, covariates full_rt: FUS and PYCARD-AS1 r2 in the
                          model), iii_readthrough_cov_active (ii_active, full_rt), iii_readthrough_subtracted (the
                          earlier readthrough variant: X = TRIM72_rt = TRIM72 r2 minus its pooled fit on FUS and
                          PYCARD-AS1 r2, readthrough_correction_fit.csv; covariates full), iv_no_plate3_13 (wells of
                          plates 3 and 13 left out, drug-dose means and covariates recomputed; 999 drug-doses);
                          drugdose_sets.csv. Columns: n_rows / n_drugdoses / n_fe_cells / n_drugs / n_lines_WT /
                          n_lines_alt; b_WT, b_alt with drug-cluster SE (CR1), 95% CI (t, G-1 df), p_*_drug,
                          conservative two-way SE/p; within-cell permutation p (TRIM72 shuffled across lines within
                          each FE cell: drug-dose for dd, drug-dose x group for ddxg; tests b = 0 and rejects
                          whenever slopes vary across drugs, even with a zero mean); diff with drug-cluster,
                          line-cluster and conservative two-way SE/CI/p (+ se_diff_twoway_from, *_cgm),
                          p_diff_perm_within_dd and its null SD, t_diff_line, p_diff_tp53_label_perm (studentised),
                          the unstudentised version, the null SD of diff (ci_diff_*_labelsd = diff +- 1.96 SD),
                          mde_diff_80, mde_diff_80_line_se = 2.80 x line-cluster SE, mde_diff_80_within_dd from the
                          within-cell null; b_common (one slope for all lines) with CI/p; sd_TRIM72_resid_*,
                          sd_Y_resid; attenuation_lambda_split_half (split-half reliability of the residual TRIM72 for
                          that variant, fe and covariate set; trim72_reliability.csv) and
                          mde_diff_80_attenuation_corrected = mde_diff_80 / lambda; q_bh_diff_label and
                          q_bh_diff_twoway = BH over the 9 read-outs within fe x variant x covariate set;
                          p_holm_variants_twoway / p_holm_variants_label = Holm over the 9 variants (each at its main
                          covariate set: full, full_rt for the iii_readthrough_cov variants) for P53_SCORE, within
                          fe (empty for the other rows); check_label_engine_minus_main and
                          check_label_engine_t_minus_main (the permutation engine at the true labels minus the main
                          fit: ~1e-16).
d1_line_slopes.csv        i_all and ii_active (full covariates), both fe: per line, the TRIM72 slope from one model with
                          line-specific TRIM72 AND covariate slopes (both FE), drug-cluster SE.
d1_line_slope_tests.csv   per read-out x variant x fe: line slopes WT vs altered (lines with >= 20 drug-dose rows):
                          mean difference with Welch t / CI / p, TP53-label permutation p of the Welch t (and of the
                          plain difference), MDE from the permutation SD of the difference; rank-based next to it:
                          median WT minus median altered, Hodges-Lehmann shift (median of all WT - altered slope
                          differences), Mann-Whitney U, AUC (P(WT slope > altered slope)) and p_mannwhitney; counts
                          of negative slopes. For fe ddxg the slopes are not refitted per permutation (the FE depend
                          on the labels): approximate.
d1_per_drugdose_contributions.csv.gz  i_all and ii_active (full covariates), both fe: per drug-dose and read-out, its
                          rows' share of the WT / altered TRIM72 variation (weight_share_*), its own slope on the
                          partialled data (slope_*_in_drugdose) and its contribution to b_WT, b_alt and diff (contrib_*:
                          sum over its rows of x~ y~ / total sum of x~^2). They add up to b_WT / b_alt exactly for
                          ddxg; for dd they leave out the WT-altered cross term (the two partialled TRIM72 columns
                          are correlated through the shared drug-dose FE), which is not small in the active set:
                          summed contrib_diff minus diff is at most 0.002 over the 9 read-outs in i_all (P53_SCORE
                          +0.0054 summed vs diff +0.0050) but up to 0.023 in ii_active (P53_SCORE -0.0278 vs
                          -0.0228); checks.csv rows 'per drug-dose contributions'. Read the dd contributions as a
                          ranking of drug-doses, not an exact decomposition.
d1_active_leave_one_drug_out.csv  ii_active (full), both fe: the model refitted without each drug (all its doses):
                          b_WT, b_alt, diff, line-cluster and conservative two-way p, next to the all-drug diff and p.
d1_active_leave_one_line_out.csv  ii_active (full), both fe: the model refitted without each line (dropped line, its
                          TP53 group): b_WT, b_alt, diff, line-cluster and conservative two-way p, next to the
                          all-line diff and p.
d1_active_joint_model.csv ii_active estimated inside one model over all drug-doses (full covariates, both fe): TRIM72
                          x TP53 group x (active, inactive) slopes and every covariate x group x (active, inactive),
                          so the line FE are estimated from all drug-doses (in ii_active alone they come from the 62
                          active drug-doses only). Contrasts: active b_WT - b_alt, inactive b_WT - b_alt, the
                          difference-in-differences active minus inactive (is the active-set diff different from
                          the rest, or the same slope gap with less noise?), and the four slopes; drug- and
                          line-cluster SE and p, the plain two-way SE (se_twoway_cgm) and the conservative two-way
                          SE (se_twoway, se_twoway_from), CI and p (min(G)-1 df).
d1_gene_null_genes.csv    gene-level null (is the pattern specific to p53 targets?): i_all and ii_active, full
                          covariates, both fe: the same model (b_WT, b_alt, diff, conservative two-way SE, t, p; no
                          permutations) for the D1 read-outs, each of the 21 P53_ACTIVITY members, each of the 78
                          non-p53 background panel genes and 500 random modules of 21 background genes (set column).
d1_gene_null_summary.csv  each D1 read-out's two-way t placed in its reference: P53_SCORE among the random background
                          modules, single genes among the background genes (reference mean / SD of diff and t,
                          fraction of reference t <= observed, empirical two-sided p). The modules share genes, lines
                          and drug-doses, so this is a competitive (specificity) test, not a test of a non-zero diff:
                          a read-out can sit outside the module null while its own CI includes 0. The row 'the 21
                          P53_ACTIVITY members as a set' is a camera-style competitive test (replaces the earlier
                          Mann-Whitney of member t vs background t, which treated the genes as independent): statistic
                          = mean member t minus mean background t (set_stat_*), variance = pooled within-set variance
                          of the t x a'Ra (a = 1/21 for members, -1/78 for background genes; R = correlation between
                          the genes' diff estimates from their drug-, line- and two-way cluster scores, the version
                          giving the largest variance used, never below independence), t with 97 df: p_set_camera;
                          set_vif_effective = a'Ra / (1/21 + 1/78) (variance inflation over independent genes),
                          set_vif_drug / _line / _twoway, rho_mean_members (mean correlation between two members'
                          estimates), rho_mean_members_background, rho_mean_background; p_set_independent = the same
                          test without the inflation. Caveat: the background genes also make up bg_abs_r2 (a
                          covariate).
d2_screen_models.csv      the same model (variant i_all, both fe) for each MG53-linked gene and module (module = mean
                          r2 of the members a line expresses) of mg53_perturbation/assay_panel/panel.csv: NF-kB
                          (NFKBIA, TNFAIP3, CXCL8 + module), ferroptosis (SLC7A11, GPX4, CHAC1), apoptosis (BAX,
                          MCL1, PMAIP1), stress (ATF3, DDIT3 + module), PI3K-AKT/FOXO/FAK (TXNIP, IRS1, PTK2), cell
                          cycle (CCND1, KIF11), E2F targets (E2F1, CCNE1, CDT1, MCM3, MCM7, MYBL2, CDC25A + module;
                          none in the S_PHASE module), RAC1. primary = the covariate set of the BH family (no_cycle for
                          the cell-cycle and E2F read-outs, full otherwise); q_bh_* = BH over the primary rows within
                          each fe: diff (label-permutation p and conservative two-way p), b_common, b_WT and b_alt
                          (conservative two-way p). Non-primary rows (full covariates for the cell-cycle read-outs)
                          are sensitivity rows (no q). source = panel (T.expression_effects), pseudobulk
                          (corrected_effects) or module. The whole screen is secondary to the D1 primary test.
readthrough_correction_fit.csv  TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line FE (all drug-doses):
                          slopes, drug-cluster SE, within-R2 (share of TRIM72's within variation explained);
                          PYCARD-AS1 r2 is kept in every line (it is below the atlas gene list). Used by
                          iii_readthrough_subtracted only.
trim72_reliability.csv    (v) measurement error of TRIM72, per variant, fe and covariate set (covset full / none):
                          split-half (each well x line's cells split at random into two halves, the panel's method
                          run on each half, halves averaged per drug-dose like the main data) and replicate wells
                          (drug-doses with 2+ used wells on different plates: first two wells; split-half is also given
                          for those drug-doses alone: the gap between the two is well- or plate-specific line
                          variation that both halves of a well share but another well does not). r_halves =
                          correlation of the residual TRIM72 (FE + covariates x group out, and FUS / PYCARD-AS1 x
                          group for the iii_readthrough rows) between the halves / wells;
                          reliability_full_spearman_brown = 2r/(1+r) (the full-data measure from two halves);
                          attenuation: observed b ~= lambda x true b for classical, independent measurement error.
drugdose_sets.csv         per drug-dose: TRIM72 z, P53_ACTIVITY z (panel), plates, membership of ii_trim72, ii_p53,
                          ii_active and iv_no_plate3_13.
analysis_cells.csv.gz     the per (drug-dose, line) values of the main data (all used wells): TRIM72 r2, TRIM72_rt,
                          D1 read-outs, screen read-outs, covariates (incl. trim72_base_x_dd, p53resp_x_dd, FUS and
                          PYCARD-AS1 r2), TRIM72 halves A and B.
checks.csv                pseudobulk vs gene_panel counts; corrected_effects vs the panel r2 and the atlas DD_lfc;
                          idarubicin per-line TRIM72 vs trim72_idarubicin/corrected; split-half bookkeeping; the
                          permutation engines (fast within-cell refit vs explicit projection; label engines at the
                          true labels vs the main fit) for both fe.
key_results.csv           the headline numbers, the primary test first. role = primary, secondary (other read-outs of
                          the primary model), sensitivity (every other fe x variant x covariate set, the line-slope
                          tests, leave-one-drug-out and leave-one-line-out ranges, the active set in the
                          all-drug-dose model), check (the gene-level null: P53_SCORE and the members as a set),
                          screen (D2) (rows with q < 0.1 and the D2 MDE range), context (reliability, readthrough
                          fit). Columns p_twoway (conservative), p_label_perm, q_twoway, q_label,
                          p_holm_variants_twoway, p_holm_variants_label, p_set_camera, mde_80 as defined above.

Runtime (4 CPUs, 15 GB RAM): the caches are keyed to the inputs (cache/manifest.json: real path of --data, sizes and
mtimes of atlas/effects/wells.csv, atlas/pseudobulk/group*, gene_panel/well_line.parquet and gene_panel/cells) and
rebuilt when they do not match (or with --recompute). Measured from scratch (empty cache/ and tables/, cold page
cache 11 min after a boot, another 4-process job running on the machine): 29.4 min wall, peak RSS 1.43 GB.
Caches 13.8 min: panel effects 1.6 min; the pseudobulk pass 11.3 min (it reads 20 GB of atlas/pseudobulk and is
I/O-bound: ~30 MB/s here; 12.9 min in the verifier's earlier cold run; faster when the files are in the page
cache); split-half counts 0.8 min. Models 15.6 min: D1 12 min (mostly the permutations), leave-one-out and joint
models 0.5 min, gene-level null 0.3 min, D2 2.7 min. With the caches in place ~15 min.
