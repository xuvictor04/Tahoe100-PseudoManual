Tables of downstream_p53.py (re-created by: python3 downstream_p53.py). Associations only: Tahoe has no MG53
perturbation and measures mRNA; p53 activity = transcription of its target genes. r2 = the method-v3 corrected log2
effect per (well, cell line) (plate x line baseline -> composition shift -> position correction), per line = mean of
the drug-dose's used wells. P53_SCORE = mean r2 of the panel's 21 P53_ACTIVITY members the line expresses (per cell:
their summed counts). TP53 groups: the panel's (17 WT, 33 altered). rho = Spearman; 'partial' = covariate ranks
regressed out of both ranks. p_perm = two-sided permutation p (residual permutation). q_bh = Benjamini-Hochberg.

(a) across lines in the same wells
a_selected_drugdoses.csv          drug-doses tested: TRIM72 raisers (panel call up, z >= 4) and the panel's 10 p53
                                  reference activators; TRIM72 fold change / z, P53_ACTIVITY z, flags.
a_per_line_effects.csv            per drug-dose x line: TRIM72_r2, TRIM72_level (treated log2 CPM), P53_SCORE, CDKN1A,
                                  MDM2, BBC3, PMAIP1, TP53 r2, bg_abs_r2 (mean |r2| of the non-p53 panel genes),
                                  atlas_beta (DD_beta), atlas_A (DD_A, relative abundance; < 0 = depleted),
                                  TRIM72_base (log2 untreated DMSO CPM of TRIM72, plates pooled).
a_line_correlations.csv           every drug-dose x scope (all used wells / one plate's well) x TP53 group x predictor
                                  (TRIM72_r2, TRIM72_level) x outcome x adjustment (none; beta+A = atlas DD_beta and
                                  DD_A; bg|r2|+A = mean |r2| of non-p53 panel genes and DD_A; beta+A+TRIM72base =
                                  beta+A and the untreated TRIM72 level): n_lines, rho, p (t),
                                  p_perm, q_bh (within scope type x predictor x adjustment x group).
a_line_correlations_WT_vs_altered.csv  the same test in WT vs altered lines: Fisher z difference and p.
a_reference_background_genes.csv  TRIM72_r2 vs each p53 outcome next to TRIM72_r2 vs every non-p53 panel gene
                                  (median, 5th / 95th percentile, percentile of the p53 outcome among them).
a_replicate_reliability.csv       2-well drug-doses: per-line agreement of the plate-6 and plate-14 wells (Spearman).
a_cross_well_correlations.csv     2-well drug-doses: TRIM72_r2 from one well vs outcome r2 from the other well (shared
                                  per-profile noise cannot create these), next to the same-well values.
a_pooled_over_drugdoses.csv       mean rho over a set of drug-doses (Fisher z average) with ONE line-label permutation
                                  applied to all drug-doses at once (they share lines and wells); q within set x group x
                                  adjustment.
a_pooled_WT_vs_altered.csv        the pooled TRIM72_r2 correlations, WT minus altered (mean Fisher z difference), p from
                                  permuting the TP53 labels over lines (residuals recomputed in the permuted groups).

(b) untreated (DMSO wells)
b_baseline_per_line.csv           per line: TRIM72_rel_* = log2(observed / expected counts), expected = the plate's
                                  median expressing line's CPM x the profile's UMIs, summed over the plates of the set
                                  (reliable plates; high-baseline plates 1-3, 14; low-baseline plates 4-12), NaN when
                                  expected < 2 counts; basal_p53_within_plate (mean over the expressed P53_ACTIVITY
                                  members of the same standardised level), the panel's basal_p53_activity_log2 and
                                  p53_responsiveness_log2, CDKN1A/MDM2/BBC3/PMAIP1/TP53 standardised levels.
b_baseline_per_plate_line.csv     the same per plate (long).
b_baseline_tests.csv              Spearman (permutation p, within-organ rho / p as tahoe_gene_panel.spearman_within),
                                  q_bh over the TRIM72-vs-p53 tests; the high- vs low-plate ranking check; Mann-Whitney
                                  of the TRIM72 level WT vs altered (rho column = AUC).
b_baseline_per_plate_correlations.csv  per plate and group: TRIM72 vs within-plate basal p53 (the plates share lines:
                                  not independent replicates).

(c) across drug-doses (all 1,132)
c_drugdose_table.csv              per drug-dose: TRIM72 fold / z / FDR / call, P53_ACTIVITY fold / z / FDR, the panel's
                                  WT-minus-altered p53 contrast (z, log2, pattern), z of every p53 target, activity
                                  covariates (atlas n_sig_genes, cells, S / G2M z, ISR / NRF2 / UPR / heat-shock /
                                  NF-kB z), DNA-damaging (the panel's definition), category.
c_correlations_across_drugdoses.csv  Spearman of TRIM72 z with p53 readouts, raw and with activity partialled out, in
                                  subsets; 95% CI by resampling whole drugs (all doses together); 'MDM2_z |
                                  P53_ACTIVITY_z' = MDM2 beyond the p53 score; within-plate means.
c_trim72_up_vs_p53_activated_enrichment.csv  2x2: TRIM72 call up vs P53_ACTIVITY z >= 3 & FDR < 0.10 (Fisher;
                                  Mantel-Haenszel over deciles of drug activity).
c_category_summary.csv / c_categories_drugdoses.csv  drug-doses that raise TRIM72 with / without p53 activation
                                  (P53_ACTIVITY z < 2) and p53 activators without TRIM72 (TRIM72 z < 2): what each p53
                                  target does there.

(d) single cells (idarubicin 5 uM wells smp_2010 / smp_2778; DMSO wells of plates 6 and 14)
d_single_cell_line_description.csv  per well set x line: cells, TRIM72-detected cells (>= 1 UMI), median UMIs of
                                  detected / not detected cells, S / G2M score differences.
d_single_cell_per_line_fits.csv.gz  per well set x line x outcome: quasi-Poisson GLM log rate ratio of the outcome's
                                  counts for TRIM72-detected cells (offset log UMIs; covariates log UMIs, log S-phase
                                  and G2M module fraction, well indicator for pooled wells), SE, dispersion, and the
                                  unadjusted log rate ratio. Lines need >= 50 cells, >= 5 detected and >= 5 not; outcomes
                                  >= 20 counts in the line and expressed by it.
d_single_cell_meta_all_outcomes.csv  DerSimonian-Laird random-effects over lines per well set x TP53 group x outcome
                                  (p53 outcomes and every non-p53 panel gene = negative controls); percentile of each
                                  outcome among the controls; q_bh over the p53 outcomes.
d_single_cell_meta_main.csv       the p53 outcomes (P53_SCORE, CDKN1A, MDM2, BBC3, PMAIP1, TP53, ATF3) with the WT-minus-
                                  altered difference.
d_single_cell_mh_depth_strata.csv  Mantel-Haenszel rate ratio within UMI-depth quintiles per line; median over lines,
                                  Wilcoxon signed-rank p.

checks.csv                        agreement with the panel's tables and the earlier per-line TRIM72 table.
key_results.csv                   the numbers the summary cites, each with its source table.
