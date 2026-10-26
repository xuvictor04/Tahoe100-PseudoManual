Tables of upstream_tf.py (re-created by: python3 upstream_tf.py --data <Tahoe-100M folder>). Associations only:
Tahoe has no TF or MG53 perturbation and measures mRNA; a TF's activity is read from its targets' mRNA, and a TF whose
activity tracks TRIM72 may be a co-responder to the same drugs rather than a regulator.

Regulons: CollecTRI (OmniPath, decoupler's processing: AP-1 and NF-kB members and dimers merged into AP1 and NFKB;
weight -1 = repression by consensus, else +1); DoRothEA A-C (OmniPath) as a sensitivity source. TRIM72 and the
Ensembl genes within 200 kb of it are out of every regulon and of the gene universe (checks.csv lists them). TFs need
>= 5 targets among the atlas genes outside the locus. Activity = ULM: per sample, the gene vector (DD_z, DD_lfc, or
r2 per well x line) regressed on the TF's weights (0 = non-target) over the sample's genes; t-value (drug-dose level)
or slope (per drug-dose x line: log2 change per unit weight, i.e. ~ the targets' signed mean change relative to the
other genes). TP53 (MDM2, CDKN1A out) = TP53's CollecTRI regulon without the two positive-control targets.
Drug-doses: the atlas's 1,132 minus unreliable-plate-only and position-not-correctable ones (1,086). TP53 groups: the
gene panel's (17 WT, 33 altered). TRIM72 versions: TRIM72 (atlas DD_z; per line: r2), TRIM72_rt (two_way's
readthrough correction: per (well, line) TRIM72 r2 minus its within drug-dose and line fit on FUS r2 and PYCARD-AS1
r2, then well median over lines, robust z over reliable drug wells / the TRIM72 plate factor, Stouffer over the
drug-dose's used wells), TRIM72_rt_across (TRIM72 z with FUS z and PYCARD-AS1 z partialled out of both sides: removes
everything TRIM72 shares with its locus neighbours across drug-doses, genuine co-regulation included).
p = permutation-calibrated normal p (observed / SD of the null), q_bh = Benjamini-Hochberg within the family named.

a0_regulon_sizes.csv      per source and TF: targets in the database, targets among the atlas genes outside the locus
                          (used), TF mRNA in the atlas (median line CPM, lines expressing).
a0_tf_edges_to_trim72_locus.csv  the database edges TF -> TRIM72 or a locus gene (all removed before any test).
a0_readthrough_fit.csv    TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (two_way's correction, here on
                          the 1,086 drug-doses): slopes, drug-cluster SE, within R2.
a1_tf_activity_by_drugdose.csv.gz  CollecTRI ULM t per drug-dose (rows: drug, conc) and TF (columns).
a1_dd_tf_vs_trim72.csv.gz one row per source (CollecTRI_t primary; CollecTRI_lfc_slope; DoRothEA_t; TF_mRNA_z = the
                          TF's own mRNA) x TF x trim72_version x variant (raw; covariates = intercept + log n
                          significant genes, cell loss, UMI / cell, genes / cell, composition shift, S, G2M and
                          proteasome z, RMS z over genes; minus_3pc / minus_10pc = top 3 / 10 PC scores of the
                          standardised DD_z gene matrix partialled). r = partial Pearson r across drug-doses with 95% CI
                          (Fisher), null_sd_drug_block = SD of r when whole drugs are swapped (drugs with the same dose set;
                          keeps a drug's doses together), p (calibrated), p_perm_empirical, q_bh (over TFs within source x
                          version x variant), rho_spearman_partial and p_spearman (ranks; t approximation),
                          pct_vs_matched_genes = percentile of r among the r of 300 random genes of TRIM72's expression
                          level (2x; >= 45 lines; same TF, same variant): ~50 = the TF tracks such genes as much as TRIM72;
                          pct_abs_* the same for |r| (these genes are about as drug-responsive as TRIM72: checks.csv);
                          pct_vs_all_genes / rank_vs_all_genes (CollecTRI_t; TRIM72 and TRIM72_rt; not raw): where
                          TRIM72's r sits among the r of the same TF activity with every gene of the universe (the TF's
                          own targets included): ~100 / rank 1 = TRIM72 tracks the TF like its best-tracking genes.
a1_matched_genes_reference.csv  how strongly the 300 matched random genes themselves track TRIM72 (per version x variant).
a1_pc_variance.csv        the top PCs of the standardised DD_z gene matrix: variance explained, r with TRIM72 z.
a2_within_line_tf_vs_trim72.csv.gz  per TF x trim72_version (TRIM72 r2; TRIM72_rt r2) x covset (full = DD_beta (0 where
                          the drug-dose has no consensus), DD_A, S and G2M per-line effects, mean |r2| over the line's
                          genes, each x TP53 group; none = fixed effects only): Y = TRIM72 per (drug-dose, line), X = the
                          TF's ULM slope per (drug-dose, line) (mean over the used wells), drug-dose and line fixed
                          effects. b (log2 TRIM72 per unit activity), b_per_sd_tf (per SD of the residual activity),
                          r_partial_within, drug-cluster and two-way (drug, line) cluster SE / CI / p, q_bh_twoway (over
                          TFs); b_WT, b_alt and their difference with line-cluster SE (p_diff_line, q_bh_diff_line,
                          mde_diff_80_line) and drug-cluster SE. Rows = drug-dose x line cells with TRIM72 and all
                          covariates present (NCI-H2122 and NCI-H596 have no DD_A and drop out of 'full').
a1a2_tf_summary.csv       one row per CollecTRI TF: the drug-dose results (own, rt, rt_across; raw / covariates / PCs;
                          pct_vs_matched_* and pct_vs_all_genes_* as in a1),
                          DoRothEA and TF-mRNA r (covariates), within-line results (own and rt, full covariates), the
                          WT - altered slope difference, and flags: tracks_TRIM72_all_tests (q < 0.1 and the same sign in
                          the drug-dose covariates, minus_3pc and minus_10pc tests and within lines, own and rt),
                          lists_TRIM72_as_target (CollecTRI / DoRothEA), muscle_TF, tf_gene_in_trim72_locus (the
                          TF's own mRNA sits within 200 kb of TRIM72, so its mRNA r is readthrough-exposed).
a3_tp53_positive_control.csv  TP53 activity (full CollecTRI regulon; MDM2 / CDKN1A out; only its activated targets,
                          MDM2 / CDKN1A out: the repressed targets are mostly cell-cycle genes) vs MDM2 z, CDKN1A z and the
                          panel's P53_ACTIVITY z across drug-doses (partial r, covariates; drug-block null), and within
                          lines (Y = MDM2 / CDKN1A r2, X = the TP53 activities without MDM2 / CDKN1A, same model as a2: b_WT, b_alt,
                          difference); TP53 activity per line in WT minus altered lines across the panel's p53-activating
                          drug-doses (P53_ACTIVITY z >= 5) vs all other drug-doses.
a4_muscle_promoter_tfs.csv  MYOD1, MYOG, MYF5, MYF6, MEF2A-D, SRF: in which source, regulon size, whether the source
                          lists TRIM72 as a target, untreated mRNA (atlas median line CPM / lines expressing, or DMSO CPM
                          from the pseudobulk for genes below the atlas list), drug-dose and within-line association with
                          TRIM72.
b1_line_outcomes.csv      per line: TRIM72 untreated level (log2 observed / expected DMSO counts, reliable plates; also
                          plates 1-3 and 14 vs 4-12 separately), its counts / expected counts, TRIM72 r2 under idarubicin
                          5 uM and homoharringtonine 5 uM (mean of the 2 wells, and each well), the mean induction, each
                          induction adjusted for the untreated level (*_adj_untreated: residual of a linear fit on
                          TRIM72_untreated_rel; low-baseline lines get larger folds), FUS / PYCARD-AS1 untreated level,
                          TP53 group, organ, drivers.
b2_line_feature_tests.csv one row per outcome x feature (tested over the lines where both are present): families tp53, lineage (each organ with >= 3 lines vs the rest;
                          Kruskal-Wallis over all organs), drivers (genes altered in >= 4 lines, cell_line_metadata;
                          TP53 left to the tp53 family; plus the number of driver genes altered, a hypermutation proxy), baseline_tf (ULM t of CollecTRI TFs on the line's untreated
                          within-plate relative expression), locus (FUS, PYCARD-AS1 untreated level). rho = Spearman
                          (binary features: rank-biserial-type r of rank(y) with 0/1) with CI (Fisher, x1.06), p
                          calibrated by 10,000 label permutations, empirical p, organ-adjusted r (organ means out of
                          both; within-organ permutation p), q_bh within outcome x family; binary features also: n and
                          mean / median per group, mean difference with Welch CI, MDE in SD units; mde_rho_80 = smallest
                          |rho| detectable with 80% power at two-sided 5% (one test; with BH over many tests larger).
b3_baseline_tf_activity_per_line.csv  lines x CollecTRI TFs: ULM t of the untreated within-plate relative expression.
checks.csv                pass reconstruction vs the atlas (W1 per plate, TRIM72 drug-dose log2FC and z), DMSO TRIM72 counts
                          vs gene_panel well_line, idarubicin per-line TRIM72 vs trim72_idarubicin/corrected, regulon
                          and locus bookkeeping, untreated TRIM72 line ranking high- vs low-baseline plates.
key_results.csv           the headline numbers.
run_info.json             downloads (status, date), regulon sizes, runtime, peak memory.
