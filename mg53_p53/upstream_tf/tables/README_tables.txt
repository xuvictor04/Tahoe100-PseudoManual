Tables of upstream_tf.py (re-created by: python3 upstream_tf.py --data <Tahoe-100M folder>). Associations only:
Tahoe has no TF or MG53 perturbation and measures mRNA; a TF's activity is read from its targets' mRNA, and a TF whose
activity tracks TRIM72 may be a co-responder to the same drugs rather than a regulator.

Regulons: CollecTRI (OmniPath, decoupler's processing: only the COMPLEX sources made of AP-1 members, or of NF-kB
members, are merged into AP1 and NFKB; single-protein sources such as JUN, FOS, RELA or NFKB1 stay TFs of their own;
weight -1 = repression by consensus, else +1); DoRothEA A-C (OmniPath) as a sensitivity source. CollecTRI is required:
without it (no internet and no cache/external/collectri.tsv) the script stops before the pseudobulk pass and says where
to put the file; there is no fallback. TRIM72 and the Ensembl genes within 200 kb of it are out of every regulon and of
the gene universe (checks.csv lists them). TFs need >= 5 targets among the atlas genes outside the locus. Activity =
ULM: per sample, the gene vector (DD_z, DD_lfc, or r2 per well x line) regressed on the TF's weights (0 = non-target)
over the sample's genes; t-value (drug-dose level) or slope (per drug-dose x line: log2 change per unit weight, i.e. ~
the targets' signed mean change relative to the other genes). Second method (drug-dose level only): mean_z = the mean
of weight x DD_z over the TF's targets (no centring, no fit). TP53 (MDM2, CDKN1A out) = TP53's CollecTRI regulon without
the two positive-control targets. Drug-doses: the atlas's 1,132 minus unreliable-plate-only and
position-not-correctable ones (1,086). TP53 groups: the gene panel's (17 WT, 33 altered). TRIM72 versions: TRIM72
(atlas DD_z; per line: r2), TRIM72_rt (two_way's readthrough correction: per (well, line) TRIM72 r2 minus its within
drug-dose and line fit on FUS r2 and PYCARD-AS1 r2, then well median over lines, robust z over reliable drug wells / the
TRIM72 plate factor, Stouffer over the drug-dose's used wells), TRIM72_rt_across (TRIM72 z with FUS z and PYCARD-AS1 z
partialled out of both sides: removes everything TRIM72 shares with its locus neighbours across drug-doses, genuine
co-regulation included). p = permutation-calibrated normal p (observed / SD of the null), q_bh = Benjamini-Hochberg
within the family named. Drug-dose CIs (A1): r +- 1.96 x se_for_ci, se_for_ci = the larger of null_sd_drug_block and
se_jackknife_drug (drug-doses of one drug are correlated; the iid Fisher SE 1/sqrt(n - 3 - k), ~0.031 here, is too
small and is no longer reported). The drug-block null SD is the SD of r under no association, the jackknife SE the
spread of r when one drug's drug-doses are left out (covariates partialled once on all drug-doses); p stays the
permutation-calibrated p (a test of no association), so a CI can be wider than p alone suggests.

a0_regulon_sizes.csv      per source and TF: targets in the database, targets among the atlas genes outside the locus
                          (used), TF mRNA in the atlas (median line CPM, lines expressing).
a0_regulons_used.csv.gz   every (source, TF, target) edge read, with weight, target in the atlas, target in the locus.
a0_tf_edges_to_trim72_locus.csv  the database edges TF -> TRIM72 or a locus gene (all removed before any test).
a0_readthrough_fit.csv    TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (two_way's correction, here on
                          the 1,086 drug-doses): slopes, drug-cluster SE, within R2.
a1_tf_activity_by_drugdose.csv.gz  CollecTRI ULM t per drug-dose (rows: drug, conc) and TF (columns).
a1_dd_tf_vs_trim72.csv.gz one row per source (CollecTRI_t primary; CollecTRI_mean_z = the second method;
                          CollecTRI_lfc_slope; DoRothEA_t; TF_mRNA_z = the TF's own mRNA) x TF x trim72_version x variant
                          (raw; covariates = intercept + log n significant genes, cell loss, UMI / cell, genes / cell,
                          composition shift, S, G2M and proteasome z, RMS z over genes; minus_3pc / minus_10pc = top 3 /
                          10 PC scores of the standardised DD_z gene matrix partialled). r = partial Pearson r across
                          drug-doses; ci_lo / ci_hi = the drug CI above; null_sd_drug_block = SD of r when whole drugs are
                          swapped (drugs with the same dose set; keeps a drug's doses together); se_jackknife_drug; p
                          (calibrated), p_perm_empirical, q_bh (over TFs within source x version x variant),
                          rho_spearman_partial and p_spearman (ranks; t approximation), pct_vs_matched_genes = percentile
                          of r among the r of 300 random genes of TRIM72's expression level (2x; >= 45 lines; same TF,
                          same variant): ~50 = the TF tracks such genes as much as TRIM72; pct_abs_* the same for |r|
                          (these genes are about as drug-responsive as TRIM72: checks.csv); pct_vs_all_genes /
                          rank_vs_all_genes (CollecTRI_t; TRIM72 and TRIM72_rt; not raw): where TRIM72's r sits among
                          the r of the same TF activity with every gene of the universe (the TF's own targets included):
                          ~100 / rank 1 = TRIM72 tracks the TF like its best-tracking genes.
a1_matched_genes_reference.csv  how strongly the 300 matched random genes themselves track TRIM72 (per version x variant).
a1_pc_variance.csv        the top PCs of the standardised DD_z gene matrix: variance explained, r with TRIM72 z.
a1_regulon_overlap_control.csv  TRIM72 z vs each CollecTRI TF's ULM t (covariates, drug-block null, drug CI) in four
                          variants: the reference (full regulon; = a1 covariates), minus_overlap_targets (every target
                          that is also a target of AP1, of the AP-1 single proteins JUN / JUNB / JUND / FOS / FOSB /
                          FOSL1 / FOSL2 or of ATF3, and every immediate-early gene (IEG list in checks.csv), taken out of
                          the TF's regulon; TFs left with < 5 targets drop out), plus_mediators_partialled (ATF3 z,
                          PMAIP1 z, DDIT3 z, the mean z of the IEGs and the AP1 ULM t partialled from both sides, with the
                          covariates), and both; n_targets / n_targets_used, r_reference, q_bh over TFs within variant.
                          It asks whether a TF tracks TRIM72 only through the shared AP-1 / IEG / ATF3 stress arm.
a1_plate_batch_split.csv  TRIM72 z vs CollecTRI_t and CollecTRI_mean_z (covariates) in all 1,086 drug-doses and
                          separately in the drug-doses whose used wells are all on the high-TRIM72 plates (1-3 and 14;
                          in practice 1-3: high_plates_only, 250), all on the low-TRIM72 plates (4-12: low_plates_only,
                          735) or on both (mixed_plates, 101: mostly the plate 6 + plate 14 replicates); each subset
                          with its own drug-block permutations, BH within source x subset; n_drugs. TRIM72's untreated
                          level is ~10x lower on plates 4-13 (13 is unreliable and out), so a TF that tracks TRIM72 only
                          in one batch would point to a plate artefact.
a2_within_line_tf_vs_trim72.csv.gz  per TF x trim72_version (TRIM72 r2; TRIM72_rt r2) x covset (full = DD_beta (0 where
                          the drug-dose has no consensus), DD_A, S and G2M per-line effects, mean |r2| over the line's
                          genes, each x TP53 group: 47 lines, NCI-H2122 and NCI-H596 have no DD_A; none = fixed effects
                          only: 49 lines, NCI-H661 has no TRIM72 r2): Y = TRIM72 per (drug-dose, line), X = the
                          TF's ULM slope per (drug-dose, line) (mean over the used wells), drug-dose and line fixed
                          effects. n_rows / n_lines (they differ by TF: a TF's slope is missing where a line expresses
                          < 5 of its targets), b (log2 TRIM72 per unit activity), b_per_sd_tf (per SD of the residual
                          activity), r_partial_within, drug-cluster and two-way (drug, line) cluster SE / CI / p,
                          q_bh_twoway (over TFs); b_WT, b_alt and their difference with line-cluster SE (p_diff_line,
                          q_bh_diff_line, mde_diff_80_line) and drug-cluster SE. Rows = drug-dose x line cells with TRIM72
                          and all covariates present.
a2_noise_ceiling_genes.csv  the same model with X = a single gene's r2 (FOS, EGR1, JUN, ATF3, FUS, PMAIP1, DDIT3; columns
                          as a2, 'gene' for 'tf'): how large a within-line r TRIM72 reaches with its strongest
                          co-responding genes, i.e. the ceiling against which the TF activities' within-line r are read
                          (TRIM72 has ~5 counts per well x line, so its r2 is noisy). For TRIM72_rt the FUS row is ~0 by
                          construction (FUS is regressed out of it).
a1a2_tf_summary.csv       one row per CollecTRI TF: the drug-dose results (own, rt, rt_across; raw / covariates / PCs;
                          pct_vs_matched_* and pct_vs_all_genes_* as in a1; the drug CI of the covariates r), the second
                          method (r / q_mean_z_dd_TRIM72_covariates) and the ranks: rank_pos_* (1 = largest positive r)
                          and rank_neg_* (1 = most negative r) under ULM (rank_*_ulm) and mean z (rank_*_mean_z), and
                          rank_*_method_robust = the worse (larger) of the two; the overlap control (r / q
                          _dd_TRIM72_minus_overlap, _plus_mediators, _minus_overlap_plus_mediators; n_targets_minus_overlap)
                          and the plate-batch split (r / q _dd_TRIM72_high_plates_only, _low_plates_only), DoRothEA and
                          TF-mRNA r (covariates; DoRothEA has no AP1 / NFKB: their row shows the family member with the
                          largest |r|), within-line results (own and rt, full covariates; within_n_rows / within_n_lines),
                          the WT - altered slope difference, and flags: tracks_TRIM72_all_tests (q < 0.1 and the same sign
                          in the drug-dose covariates, minus_3pc and minus_10pc tests, the drug-dose rt covariates test,
                          and within lines, own and rt), lists_TRIM72_as_target (CollecTRI / DoRothEA), muscle_TF,
                          tf_gene_in_trim72_locus (the TF's own mRNA sits within 200 kb of TRIM72, so its mRNA r is
                          readthrough-exposed).
a3_tp53_positive_control.csv  TP53 activity (full CollecTRI regulon; MDM2 / CDKN1A out; only its activated targets,
                          MDM2 / CDKN1A out: the repressed targets are mostly cell-cycle genes) vs MDM2 z, CDKN1A z and the
                          panel's P53_ACTIVITY z across drug-doses (partial r, covariates; drug-block null), and within
                          lines (Y = MDM2 / CDKN1A r2, X = the TP53 activities without MDM2 / CDKN1A, same model as a2:
                          n, n_lines, b_WT, b_alt, difference); TP53 activity per line in WT minus altered lines across
                          the panel's p53-activating drug-doses (P53_ACTIVITY z >= 5) vs all other drug-doses.
a4_muscle_promoter_tfs.csv  MYOD1, MYOG, MYF5, MYF6, MEF2A-D, SRF: in which source, regulon size, whether the source
                          lists TRIM72 as a target, untreated mRNA (atlas median line CPM / lines expressing, or DMSO CPM
                          from the pseudobulk for genes below the atlas list), drug-dose and within-line association with
                          TRIM72, baseline activity vs the line outcomes (q = the b2 headline q_bh).
b1_line_outcomes.csv      per line: TRIM72 untreated level (log2 observed / expected DMSO counts, reliable plates; also
                          plates 1-3 and 14 vs 4-12 separately), its counts / expected counts, TRIM72 r2 under idarubicin
                          5 uM and homoharringtonine 5 uM (mean of the 2 wells, and each well), the mean induction, each
                          induction adjusted for the untreated level (*_adj_untreated: residual of a linear fit on
                          TRIM72_untreated_rel; how much this removes differs by raiser, see below), FUS / PYCARD-AS1
                          untreated level, TP53 group, organ, drivers.
b2_line_feature_tests.csv one row per outcome x feature (tested over the lines where both are present): families tp53,
                          lineage (each organ with >= 3 lines vs the rest; Kruskal-Wallis over all organs, 2,000
                          permutations), drivers (genes altered in 4 to 46 of the lines, cell_line_metadata; TP53 left
                          to the tp53 family; plus 'n driver genes altered', the number of driver genes a line has
                          altered), baseline_tf (ULM t of CollecTRI TFs on the line's untreated within-plate relative
                          expression), locus (FUS, PYCARD-AS1 untreated level). rho = Spearman (binary features:
                          rank-biserial-type r of rank(y) with 0/1) with CI (Fisher, x1.06), p calibrated by 10,000 label
                          permutations, empirical p, organ-adjusted r (organ means out of both; within-organ permutation
                          p, 5,000 permutations); q_bh = BH over every outcome x feature test of the table (5,075: the
                          headline, the most conservative), q_bh_outcome = BH over every test of the outcome (725, all
                          families), q_bh_family = BH within outcome x family (the q_bh of the earlier version; the least
                          conservative: e.g. KMT2D vs the untreated level 0.007 there, 0.046 within the outcome, 0.12
                          over all line tests); binary features also: n and mean / median per group, mean difference
                          with Welch CI, MDE in SD units; mde_rho_80 = smallest |rho| detectable with 80% power at
                          two-sided 5% (one test; with BH over many tests larger).
b3_baseline_tf_activity_per_line.csv  lines x CollecTRI TFs: ULM t of the untreated within-plate relative expression.
checks.csv                pass reconstruction vs the atlas (W1 per plate, TRIM72 drug-dose log2FC and z), DMSO TRIM72 counts
                          vs gene_panel well_line, idarubicin per-line TRIM72 vs trim72_idarubicin/corrected, regulon
                          and locus bookkeeping (AP1 / NFKB merge, the overlap-control gene set and IEGs, plate-batch
                          subsets), the TP53 controls available, untreated TRIM72 line ranking high- vs low-baseline
                          plates, each raiser's induction vs the untreated level (rho, R2, well-to-well rho after the
                          adjustment), KMT2D vs the untreated level with the driver-count controls.
key_results.csv           the headline numbers (A2 rows give n rows / n lines per TF).
run_info.json             downloads (status, date, md5 of the regulon files), regulon sizes, runtime, peak memory (getrusage
                          or psutil, whichever is larger) and whether the pass came from the cache.

What the tables say (numbers from key_results.csv and the tables named; all associations in mRNA)
- Across drug-doses (a1, CollecTRI ULM t, TRIM72 z, covariates): 348 of 679 TFs track TRIM72 positively and 125
  negatively at q < 0.1; the strongest, ATF5 and ATF4 (r 0.36, drug CI 0.29-0.43 and 0.28-0.44), TWIST1, GCM1, TWIST2,
  sit at the 99th-100th percentile of 300 expression-matched genes. The drug CIs are ~1.3x wider than the iid Fisher
  CIs reported before (median SE 0.040 vs 0.031; the drug jackknife SE is the larger for 626 of 679 TFs): 409 of 679
  TFs have a CI that excludes 0 (459 of 667 with the Fisher CI), and 64 of the 473 TFs at q < 0.1 (either sign) have a
  CI that includes 0 (their p rests on the null SD, which the jackknife SE exceeds); read those as weak.
- Second method (mean signed target z): r across TFs 0.86 with the ULM r. Method-robust top (the worse of the two
  ranks): TWIST2, TWIST1, ATF5, ATF4, CREBBP, APEX1, ASCL1, PBRM1, XBP1, ZNF91; bottom: YBX3, NFIL3, NAB2, MYF6, RB1.
- Regulon overlap (a1_regulon_overlap_control): much of the top associations runs through the shared AP-1 / IEG / ATF3
  stress arm. Taking the AP-1 / ATF3 targets and IEGs out of the regulons lowers r by a median 0.12 over the 50
  highest-r TFs (ATF5 0.36 -> 0.00, ATF4 0.36 -> 0.22; 13 of the 50 keep < 5 targets); with ATF3, PMAIP1, DDIT3, the
  IEG score and AP1 activity also partialled the median drop is 0.18 (ATF4 0.09, XBP1 0.04, HSF1 0.07, CREB1 0.08), and
  22 of the 37 testable ones still track TRIM72 at q < 0.1 (e.g. ZNF91 0.32, TWIST1 0.21, APEX1 0.17, SRF 0.17).
  AP1, NFKB and TP53 activity lose their positive association (TP53 0.12 -> -0.18 with the mediators partialled).
  None of this makes a TF a regulator of TRIM72: these are co-responders to the same drugs.
- Plate batch (a1_plate_batch_split): the top TFs track TRIM72 in both batches (ATF4 0.37 / 0.37, ATF5 0.32 / 0.35,
  ELK4 0.31 / 0.36 on the high- / low-TRIM72 plates), but over all TFs the two batches agree only moderately (r 0.47
  across TFs; 250 drug-doses of 88 drugs vs 735 of 276); AP1 (0.08 / 0.23), ASCL1 (0.14 / 0.33) and CREB1 (0.15 / 0.28)
  come mostly from the low plates.
- Within lines (a2): 187 of 679 TFs at q < 0.1 (57 positive), all with |r| <= 0.08 (MYBL1 0.071, E2F4 -0.080); ATF4,
  ATF5, XBP1, AP1 are ~0 within lines (|r| <= 0.02). The noise ceiling (a2_noise_ceiling_genes) is of the same size:
  TRIM72's within-line r with its best single co-responders is FOS 0.080, EGR1 0.067, FUS 0.066, JUN 0.063, ATF3 0.062,
  so a within-line r of ~0.07 is about as large as TRIM72's noisy per-line values allow; ATF4, ATF5 and XBP1 stay far
  below it (|r| <= 0.01): their drug-dose association does not carry over to line-to-line differences within a
  drug-dose. No TF's slope differs between TP53-WT and altered lines (q_bh_diff_line >= 0.1 for all).
- Inducibility vs the untreated level, per raiser: idarubicin 5 uM induction is strongly tied to a line's untreated
  TRIM72 level (rho -0.79, linear R2 0.34: low-baseline lines get larger folds; the well-to-well rho drops from 0.63 to
  0.38 once it is removed), homoharringtonine 5 uM only weakly (rho -0.33, R2 0.10; well-to-well rho 0.82 raw, 0.81
  after removal): the homoharringtonine induction is a reproducible line property that the untreated level hardly
  explains, while much of the idarubicin per-line fold is the low-baseline effect.
- Line features (b2, headline q over all 5,075 line tests): only the locus (PYCARD-AS1 rho 0.82 and FUS 0.57 with the
  untreated level; PYCARD-AS1 -0.63 with the idarubicin induction) and two baseline TF activities for the idarubicin
  induction (NFKBIB, TP73) reach q < 0.1. KMT2D-altered lines (14) have a higher untreated level (rho 0.54, p 0.0002):
  q 0.046 within the untreated outcome, 0.12 over all line tests (0.007 within the 37 driver tests only). It is not
  explained by the number of altered driver genes (rho partial on that number 0.49; random line sets of the same size
  drawn in proportion to driver count reach it with P 0.0008), so the 'hypermutation marker' reading is not supported;
  it remains an unexplained, unreplicated association. TP53 group: nominal only for the untreated-adjusted idarubicin
  induction (WT ranked higher, rho 0.30, p 0.04; q 0.38 over all line tests), none for the other six outcomes.
- The locus link (TRIM72's untreated level following PYCARD-AS1 and FUS across lines) fits readthrough from FUS, but a
  line's 16p11.2 copy number would raise all genes of the region together and give the same pattern; Tahoe has no
  copy-number data to tell them apart.
