# MG53 (TRIM72): what is upstream of it, and does it act on p53? (Tahoe-100M, mRNA)

Scope: TRIM72 mRNA and p53-target mRNA, 24 h after each of 379 drugs at 3 doses, in 50 cancer cell lines (Tahoe-100M,
95.6M cells), with the repo's method-v3 corrections. Tahoe has no MG53 knockdown or overexpression and no protein data, so
every MG53-p53 relation here is an **association in mRNA**, never a causal or protein-level result. TRIM72 is low in these
lines (median line ~4 CPM; muscle is ~140 nTPM), and its untreated level is ~10x lower on plates 4-13 than on plates 1-3
and 14, which inflates fold changes on the low plates.

All tables: [SUMMARY.md](SUMMARY.md) (eight tables, T1-T8; CSVs in `summary/`). The literature evidence map, with every
citation: [literature/evidence_map.md](literature/evidence_map.md).

## Short answers

| Question | Answer | Basis | Strength |
|---|---|---|---|
| Is TRIM72 a p53 target gene? | No | Not in the p53-target census or near TP53 ChIP peaks; behaves like a non-target on 4 metrics in Tahoe (T5) | strong |
| Does TRIM72 induction need p53? | No | Rises in 31/31 TP53-altered lines under idarubicin 5 µM; selinexor activates p53 without raising TRIM72 (T5) | strong |
| Could a small p53 contribution exist? | Not excluded | WT lines lean +0.16 to +0.45 log2 across raisers, also for drugs that do not activate p53 (T5) | moderate |
| What raises TRIM72 mRNA? | Strong stress drugs | Anthracyclines/TOP2 poisons, harringtonines, auranofin, CDK9 and HDAC inhibitors; robust and replicated: idarubicin and homoharringtonine 5 µM (T1, T2) | moderate |
| What moves with it? | AP-1 / immediate-early, ATF3, PMAIP1 | Co-responders across drugs and in single cells, not shown regulators; muscle TFs (MyoD/MEF2, the known promoter TFs) are silent in these lines (T3) | moderate |
| Is it TRIM72's own promoter? | Unresolved | Part of TRIM72's reads look like readthrough from FUS (17-22 kb upstream, same strand); clean for homoharringtonine, not significant for idarubicin after level matching (T4) | moderate |
| Does more TRIM72 go with less p53 output? | No detectable association | Per line, across drugs, untreated and in single cells (T6, T7); scaled up over all 1,132 drug-doses x 50 lines with TP53 genotype as the control: WT − altered slope -0.003 (95% CI -0.009 to 0.002, p 0.24) (T9); in single cells of all wells: no genotype-dependent association, a fall of > 1.2% per doubling of TRIM72 excluded (T10). A -3% slope in the 62 most active drug-doses is not robust (Holm p 0.12; gone when line effects use all drug-doses) | null; small effects not excluded |
| Which transcription factors track TRIM72? | Stress TFs across drugs, none within lines | ATF4/ATF5 r 0.36 across drugs, largely through the shared AP-1/IEG/ATF3 arm (ATF4 0.09 without it); within lines every TF |r| <= 0.08, the noise ceiling; muscle TFs absent (T11) | co-response, not regulation |
| Which line traits predict TRIM72? | Its locus, not TP53 | Untreated TRIM72 follows PYCARD-AS1 (rho 0.82) and FUS (0.57): readthrough or 16p11.2 copy number; TP53 status no (rho 0.07); KMT2D tentative (q 0.12 over all tests) (T12) | moderate |
| Does MG53 lower p53 activity? | Not causally testable in Tahoe | p53 target mRNA is a valid read-out and was tested (row above), but TRIM72 only changes with drugs that also act on p53, and its mRNA may not mean MG53 protein. Needs an MG53 knockdown/overexpression with p53 target mRNA as read-out. Literature: MG53 binds p53 and drives its degradation (cardiomyocytes 2024, trophoblasts 2021) | literature; association only in Tahoe |

## 1. What raises TRIM72 mRNA?

21 of 1,132 drug-doses raise TRIM72 (q < 0.1, >= 1.2x) and only ponatinib 5 µM lowers it. The table lists every change with
|z| >= 4 (T1 in SUMMARY.md has all 22). Only **idarubicin 5 µM and homoharringtonine 5 µM** are replicated on two plates
(and homoharringtonine also at 0.5 µM); the others are single wells, and mitoxantrone 5 µM does not replicate (plate 6 up,
plate 14 not).

| Drug | Dose (µM) | TRIM72 fold (corrected) | z | Fold without pseudocount | Wells | Plates | p53 activity z | Genes changed |
|---|---|---|---|---|---|---|---|---|
| Idarubicin | 5 | 12.2× | 15.9 | 6.0× | replicated (2 wells) | 6, 14 | 18.1 | 11,472 |
| Homoharringtonine | 5 | 10.3× | 14.8 | 5.4× | replicated (2 wells) | 6, 14 | 20.6 | 11,993 |
| Auranofin | 5 | 6.6× | 8.4 | 4.1× | single well | 12 | -7.8 | 8,581 |
| Homoharringtonine | 0.5 | 5.9× | 7.9 | 5.9× | single well | 5 | 17.4 | 10,075 |
| Dinaciclib | 5 | 5.6× | 7.4 | 3.7× | single well | 9 | 0.6 | 13,164 |
| Epirubicin | 5 | 4.5× | 6.5 | 4.8× | single well | 9 | 8.1 | 6,752 |
| Dinaciclib | 0.5 | 3.7× | 5.9 | 2.0× | single well | 8 | 1.6 | 12,822 |
| Dinaciclib | 0.05 | 3.8× | 5.5 | 2.5× | single well | 7 | 7.0 | 11,885 |
| Harringtonine | 5 | 3.6× | 5.5 | 3.2× | single well | 9 | 6.2 | 9,773 |
| Doxorubicin | 5 | 3.0× | 4.7 | 3.2× | single well | 9 | 10.0 | 7,317 |
| Mitoxantrone | 5 | 2.0× | 4.5 | 1.1× | not replicated (1/2 wells) | 6, 14 | 11.3 | 4,951 |
| Panobinostat | 5 | 2.7× | 4.4 | 2.5× | single well | 12 | 1.1 | 10,622 |
| Topotecan | 5 | 2.6× | 4.0 | 2.6× | single well | 9 | 18.3 | 8,958 |
| Ponatinib | 5 | 0.39× | -4.2 | 0.43× | single well | 12 | 3.9 | 3,510 |

- **Drug classes** (T2): anthracyclines / TOP2 poisons and the harringtonines have the highest activity-adjusted TRIM72
  response, but no class survives multiple testing (classes have 2-5 compounds, and plate layout confounds the strata:
  strong drugs on plates 1-3 rarely raise TRIM72). Several tyrosine-kinase inhibitors lean towards lowering it (moa class
  'Other TK inhibitor', q 0.010); trametinib lowers it in all 9 wells. Treat both as hypotheses.
- **Not specific**: the raisers move thousands of genes (idarubicin 5 µM: 11,472). TRIM72 ranks in the top 0.24% (idarubicin)
  to 8.6% (dinaciclib) of genes by fold change, inside programs of ~800-5,900 genes up >= 2x.
- **Fold sizes are inflated on low-baseline plates**: idarubicin 5 µM is 25.7x on plate 6 but 5.8x on plate 14 (12.9x and 4.0x
  without a pseudocount). Compare z or replicated wells, not folds across plates.

## 2. What moves with it, and is it TRIM72's own promoter?

- **Co-responders, not regulators** (T3): across drug-doses (activity and cell loss partialled out) TRIM72 tracks FOS 0.51,
  HEXIM1 0.47, JUN 0.47, heat shock 0.47, ATF3 0.44, PMAIP1 0.40; the 21-gene p53 score only 0.11 (and ~0 among the strongly
  active drug-doses). The known promoter regulators of TRIM72, MyoD/myogenin + MEF2 (muscle; literature), are not expressed
  or do not co-vary in these lines.
- **Readthrough from FUS is a real possibility.** TRIM72 lies 17 kb (Ensembl 116; 22.5 kb in Ensembl 110, the annotation
  Tahoe used) downstream of FUS, a highly expressed gene on the same strand. About half of TRIM72's top co-varying genes
  genome-wide sit in the same geometry (a low gene just downstream of a strong same-strand gene; 4% expected), and this is
  specific to that geometry (57 of the top 100 vs 7, 4 and 1 in the other neighbour geometries). Untreated, TRIM72's best
  partner across the 50 lines is PYCARD-AS1, the lncRNA between FUS and TRIM72 (rho 0.82, 13 of 13 plates), and TRIM72's
  plate batch is shared with readthrough-exposed genes.
- **For idarubicin specifically, unresolved.** The same-strand neighbours rise with TRIM72, but once each gene is compared with
  genes of its own expression level the strand contrast is not significant for idarubicin (p 0.17-0.27); it is for
  homoharringtonine (p 0.04). Idarubicin does not raise readthrough-exposed genes more than other low genes on average, and
  dinaciclib raises TRIM72 without the locus pattern. Tahoe's 3' gene counts cannot separate readthrough from promoter
  activity: that needs read coverage across the FUS-TRIM72 interval, nascent RNA, or a **qPCR assay that spans a TRIM72
  exon-exon junction** (spliced TRIM72 mRNA) next to one placed in the FUS-TRIM72 intergenic region.

| Gene | Strand | Position vs TRIM72 | Distance (kb) | Median line CPM | Idarubicin 5 µM | Homoharringtonine 5 µM | Dinaciclib 5 µM | r with TRIM72 across drug-doses |
|---|---|---|---|---|---|---|---|---|
| BCKDK | + | upstream (5') | 100.6 | 10.3 | 0.40× | 0.31× | 1.9× | -0.32 |
| KAT8 | + | upstream (5') | 82.6 | 19.3 | 1.0× | 0.79× | 1.3× | 0.09 |
| FUS | + | upstream (5') | 17.1 | 259.2 | 1.7× | 2.2× | 1.1× | 0.63 |
| PYCARD-AS1 | + | upstream (5') | 10.6 | 1.2 | 5.7× | 6.1× | 2.5× | 0.72 |
| PYCARD | − | upstream (5') | 10.6 | 0.6 | 0.55× | 0.37× | 2.2× | -0.10 |
| TRIM72 | + | overlapping | 0.0 | 4.1 | 12.2× | 10.3× | 5.6× | 1.00 |
| PYDC1 | − | overlapping | 0.0 | 0.0 | – | – | – | – |
| ITGAM | + | downstream (3') | 28.4 | 0.8 | 6.0× | 35.7× | 2.7× | 0.53 |
| ITGAX | + | downstream (3') | 123.6 | 0.9 | 0.66× | 1.4× | 1.4× | 0.06 |

## 3. Is the induction p53-dependent?

**No requirement, not sufficient, not a p53 target.** Under idarubicin 5 µM, TRIM72 rises 12.0x in TP53 wild-type and 12.1x in
TP53-altered lines of the same wells (31 of 31 altered lines up, including likely-null truncating lines), while MDM2 and the
p53 score in those wells are strongly wild-type-selective. Selinexor activates p53 as strongly and as wild-type-selectively
without raising TRIM72. TRIM72 is not in the p53-target census or near TP53 ChIP peaks (2 of 393 experiments vs CDKN1A 261),
and in Tahoe it behaves like a non-target on four metrics.

TRIM72 induction in TP53 wild-type vs altered lines in the same wells, with p53 targets as positive controls.

| Drug | Dose (µM) | TRIM72 WT lines | TRIM72 altered lines | TRIM72 WT − altered (log2) | 95% CI | p | Altered lines up | MDM2 WT − altered (log2), p | P53 score WT − altered (log2), p |
|---|---|---|---|---|---|---|---|---|---|
| Idarubicin | 5 | 12.0× | 12.1× | -0.02 | -0.60 to 0.93 | 0.89 | 100% | 1.10, 1e-04 | 0.67, 1e-04 |
| Idarubicin | 0.5 | 2.5× | 1.9× | 0.38 | -0.13 to 0.72 | 0.16 | 23% | 2.02, 1e-04 | 1.53, 1e-04 |
| Idarubicin | 0.05 | 1.7× | 2.0× | -0.21 | -0.43 to 0.47 | 0.64 | 20% | 1.07, 1e-04 | 0.78, 1e-04 |
| Homoharringtonine | 5 | 11.7× | 9.3× | 0.33 | -1.23 to 1.45 | 0.59 | 97% | 0.28, 0.43 | -0.23, 0.17 |
| Homoharringtonine | 0.5 | 8.5× | 4.8× | 0.85 | -0.07 to 2.36 | 0.066 | 73% | 0.80, 0.004 | 0.56, 4e-04 |
| Auranofin | 5 | 9.9× | 6.4× | 0.63 | -1.31 to 1.57 | 0.56 | 77% | -1.18, 1e-04 | -0.82, 1e-04 |
| Dinaciclib | 5 | 5.7× | 5.6× | 0.04 | -0.54 to 1.00 | 0.83 | 70% | -1.19, 1e-04 | -0.68, 1e-04 |
| Epirubicin | 5 | 9.8× | 3.8× | 1.35 | 0.74 to 1.77 | 0.020 | 69% | 0.30, 0.003 | 0.50, 1e-04 |
| Doxorubicin | 5 | 4.6× | 2.7× | 0.76 | 0.06 to 1.65 | 0.066 | 47% | 0.63, 1e-04 | 0.72, 1e-04 |
| Topotecan | 5 | 2.7× | 2.4× | 0.19 | -0.21 to 1.41 | 0.37 | 38% | 0.37, 3e-04 | 0.86, 1e-04 |
| Mitoxantrone | 5 | 2.2× | 1.8× | 0.28 | -0.34 to 0.88 | 0.37 | 20% | 1.02, 1e-04 | 0.71, 1e-04 |
| Selinexor | 5 | 0.78× | 0.84× | -0.11 | -0.80 to 0.37 | 0.65 | 0% | 1.19, 1e-04 | 0.72, 1e-04 |
| Selinexor | 0.5 | 1.0× | 1.0× | 0.05 | -0.97 to 0.58 | 0.90 | 3% | 0.91, 1e-04 | 0.56, 1e-04 |

**Not excluded**: a modest wild-type lean across the raisers (+0.16 to +0.45 log2, clearest for epirubicin 9.8x vs 3.8x). It
also appears for drugs that do not activate p53 (auranofin, homoharringtonine), so it may be line background rather than
p53; the test cannot exclude a contribution the size of an average p53 target's (80% power needs ~0.9 log2).

## 4. Does more TRIM72 go with less (or more) p53 output?

**No detectable association, in any of four designs** (T7): per line in the same wells (idarubicin 5 µM and 13 raisers pooled),
untreated across lines, across all drug-doses, and in single cells (cells with detected TRIM72 vs not, adjusted for depth and
cell cycle). What does co-vary with TRIM72 in single cells is ATF3 and PMAIP1, in both TP53 groups: a shared stress state.

| Test | Lines / cells | Estimate | p | n |
|---|---|---|---|---|
| Idarubicin 5 µM, per line: TRIM72 induction vs p53-score induction (drug response and cell loss out) | TP53-WT | rho -0.22 | 0.40 | 17 lines |
| Idarubicin 5 µM, per line: TRIM72 induction vs p53-score induction (drug response and cell loss out) | TP53-altered | rho -0.28 | 0.13 | 30 lines |
| 13 TRIM72 raisers pooled, per line: TRIM72 vs P53 score (drug response and cell loss out) | TP53-WT | mean rho -0.08 | 0.40 | 13 drug-doses |
| 13 TRIM72 raisers pooled, per line: TRIM72 vs P53 score (drug response and cell loss out) | TP53-altered | mean rho 0.04 | 0.53 | 13 drug-doses |
| Untreated, per line (within plates): TRIM72 level vs basal p53 activity | TP53-WT | rho -0.19 | 0.48 | 17 lines |
| Untreated, per line (within plates): TRIM72 level vs TP53 mRNA | TP53-WT | rho -0.45 | 0.071 | 17 lines |
| Untreated, per line (within plates): TRIM72 level vs basal p53 activity | TP53-altered | rho -0.16 | 0.38 | 31 lines |
| Untreated, per line (within plates): TRIM72 level vs TP53 mRNA | TP53-altered | rho 0.24 | 0.22 | 28 lines |
| Across all drug-doses: TRIM72 z vs P53_ACTIVITY z (activity out) | all lines pooled | rho 0.12 (CI 0.05 to 0.19) | 5e-05 | 1132 drug-doses |
| Across all drug-doses: TRIM72 z vs p53_WT_minus_altered z (activity out) | all lines pooled | rho 0.03 (CI -0.04 to 0.09) | 0.35 | 1132 drug-doses |
| Single cells, idarubicin 5 µM: P53 score counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-WT | rate ratio 1.020 | 0.30 | 16 lines |
| Single cells, idarubicin 5 µM: ATF3 counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-WT | rate ratio 1.117 | 0.006 | 15 lines |
| Single cells, idarubicin 5 µM: P53 score counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-altered | rate ratio 0.983 | 0.29 | 30 lines |
| Single cells, idarubicin 5 µM: ATF3 counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-altered | rate ratio 1.195 | 1e-10 | 30 lines |

Power is limited: only strong associations (|rho| > ~0.5 in the 17 wild-type lines) are excluded, and the single-cell test
excludes more than ~7% change in p53-target counts per doubling of a cell's TRIM72. In untreated wild-type lines the point
estimates lean negative (basal p53 -0.19, TP53 mRNA -0.45, not significant), the direction an MG53-degrades-p53 mechanism
would predict.

**The literature** describes the link at the protein level: MG53 binds p53 and promotes its ubiquitination and degradation
(Jiang et al. 2024, cardiomyocytes and doxorubicin cardiotoxicity, reported MDM2-independent; Li et al. 2021, trophoblasts),
while a lung study found no direct binding and an indirect, membrane-repair route (Cong et al. 2020). Mechanisms of other TRIMs
(TRIM24, 25, 28, 32, 39, 59, 65) should not be carried over to MG53. 

**Why Tahoe cannot settle it, although p53 target mRNA is a good read-out of p53 activity.** The tests above use exactly that
read-out. What Tahoe lacks is a way to change MG53 alone: TRIM72 only rises with drugs that also act on p53 directly
(idarubicin damages DNA), so in those wells the p53 targets mix the drug's own effect with any MG53 effect, and the
across-line comparison within the same wells can only exclude a strong MG53 effect. Second, MG53 acts as a protein, and TRIM72
mRNA at ~4 CPM in cancer lines (part of it possibly readthrough from FUS) may carry little MG53 protein. Third, one 24 h
time point may come before an MG53 protein effect shows in target transcription.

**The direct test, still with mRNA read-outs:** perturb MG53 (TRIM72 knockdown or overexpression, or recombinant MG53) in a
TP53-wild-type line, with a TP53-null line as control, with and without a p53 activator, and measure the p53 targets that
separate wild-type from altered lines most clearly here (MDM2, TP53I3, FDXR, CDKN1A, BBC3). If MG53 lowers p53, these fall
in the wild-type line only. A western blot for MG53 and p53 confirms the perturbation took. Cardiomyocytes are the most
relevant cells for the anthracycline question (MG53 is expressed in rodent heart; it is scant in human heart).

## 5. Scaled up with Tahoe's own data: TRIM72 and p53 output, with TP53 genotype as the control

Tahoe has no MG53 perturbation, so these tests use the natural variation of TRIM72 and read p53 activity from its target
mRNA. The control is TP53 genotype: an MG53 -> p53 effect can only act where p53 works, so the estimand is the TRIM72 effect in
the 17 TP53-wild-type lines minus that in the 33 altered lines; anything equal in both groups (stress, cell size, transcription
shutdown) is not via p53.

**Across all drug-doses x lines** (`two_way/`, T9): each line is compared with lines of its own TP53 group in the same wells
(drug-dose x TP53-group and line fixed effects; covariates for drug response, cell loss and cell cycle). Primary test declared
as the originally specified design (not preregistered): the p53 score over all 1,132 drug-doses.

| Read-out | Drug-doses | Role | WT − altered slope | 95% CI | p | p (TP53-label permutation) | Holm over variants |
|---|---|---|---|---|---|---|---|
| p53 score (21 targets) | all 1,132 drug-doses | primary | -0.0032 | -0.0085 to 0.0022 | 0.24 | 0.26 | 0.94 |
| MDM2 | all 1,132 drug-doses | secondary | -0.0002 | -0.0096 to 0.0092 | 0.97 | 0.97 | – |
| CDKN1A | all 1,132 drug-doses | secondary | -0.0035 | -0.0163 to 0.0092 | 0.58 | 0.60 | – |
| FDXR | all 1,132 drug-doses | secondary | -0.0215 | -0.0376 to -0.0055 | 0.010 | 0.007 | – |
| ZMAT3 | all 1,132 drug-doses | secondary | -0.0007 | -0.0136 to 0.0122 | 0.92 | 0.91 | – |
| DDB2 | all 1,132 drug-doses | secondary | 0.0059 | -0.0063 to 0.0181 | 0.33 | 0.37 | – |
| BBC3 | all 1,132 drug-doses | secondary | -0.0065 | -0.0194 to 0.0064 | 0.31 | 0.29 | – |
| TP53 mRNA (not a target) | all 1,132 drug-doses | secondary | 0.0021 | -0.0079 to 0.0120 | 0.68 | 0.69 | – |
| p53 score | all; + p53 responsiveness covariate | sensitivity | -0.0038 | -0.0087 to 0.0012 | 0.13 | 0.12 | – |
| p53 score | all; FUS / PYCARD-AS1 (readthrough) in the model | sensitivity | -0.0031 | -0.0077 to 0.0016 | 0.19 | 0.21 | 0.94 |
| p53 score | all; without plates 3 and 13 | sensitivity | -0.0038 | -0.0096 to 0.0020 | 0.19 | 0.21 | 0.94 |
| p53 score | 62 active drug-doses (TRIM72 or p53 z >= 3) | sensitivity | -0.0300 | -0.0538 to -0.0062 | 0.015 | 0.018 | 0.12 |
| p53 score | 62 active; readthrough in the model | sensitivity | -0.0294 | -0.0562 to -0.0026 | 0.032 | 0.036 | 0.19 |
| p53 score | 62 active, line effects from all drug-doses | sensitivity | -0.0178 | -0.0466 to 0.0110 | 0.22 | – | – |
| p53 score | active minus inactive drug-doses | sensitivity | -0.0154 | -0.0446 to 0.0138 | 0.29 | – | – |

No WT-specific association (primary -0.003, CI -0.009 to 0.002). On the observed scale, differences above ~0.009 are excluded;
TRIM72's line-to-line variation is mostly counting noise (split-half reliability ~0.3), so a true slope up to ~0.03 per
doubling of TRIM72 is not excluded. The -0.030 in the 62 most active drug-doses is in the predicted direction but not robust:
Holm over the variants 0.12, gone when line effects come from all drug-doses (-0.018, p 0.22), and not different from the
inactive drug-doses (p 0.29). FDXR's nominal slope (p 0.01) does not survive correction over the 21 targets and vanishes under
the other fixed-effects model.

**Single cells of all wells** (`single_cell_all/`, T10; 803,499 TRIM72-detected cells in 30,803 well x line groups): in each
well and line, cells with TRIM72 reads vs without, adjusted for depth and cell cycle, with 16 other rare genes as placebo
predictors.

| Outcome | Wells | RR, WT lines | RR, altered lines | WT − altered (log RR) | 95% CI | p | p (permutation) | Placebo percentile | Per doubling of TRIM72 (95% CI) | p53-functional − non-functional lines (p perm) |
|---|---|---|---|---|---|---|---|---|---|---|
| p53 score (21 targets) | all wells | 1.091 | 1.048 | 0.041 | -0.030 to 0.111 | 0.24 | 0.15 | 81 | 0.988 to 1.059 | 0.081 (0.010) |
| MDM2 | all wells | 1.071 | 1.011 | 0.058 | -0.039 to 0.155 | 0.23 | 0.16 | 88 | 0.982 to 1.080 | 0.110 (0.012) |
| ATF3 (stress) | all wells | 1.379 | 1.348 | 0.022 | -0.073 to 0.117 | 0.64 | 0.66 | 75 | 0.980 to 1.074 | 0.063 (0.30) |
| NF-κB score | all wells | 1.106 | 1.099 | 0.007 | -0.084 to 0.098 | 0.88 | 0.89 | 44 | 0.965 to 1.052 | -0.025 (0.67) |
| ferroptosis score | all wells | 1.033 | 1.060 | -0.026 | -0.106 to 0.055 | 0.52 | 0.51 | 19 | 0.953 to 1.029 | -0.014 (0.75) |

No genotype-dependent association (p 0.24); a fall of more than ~1.2% in p53-target counts per doubling of a cell's TRIM72 is
excluded (1.8% if half of TRIM72's overdispersion is technical). TRIM72-detected cells carry more ATF3 in both groups (a
stressed state). Grouping lines by Tahoe's measured p53 function instead of genotype (not pre-specified) gives a small
**positive** difference (+0.08, permutation p 0.01): more p53-target mRNA in TRIM72-detected cells of p53-competent lines, the
opposite of MG53 suppressing p53, and consistent with stress activating both. Because that stress coupling pushes the estimate
up, a WT-specific fall of a few percent could be masked.

**Upstream: transcription-factor activity** (`upstream_tf/`, T11; CollecTRI regulons with TRIM72 and its locus left out):

| TF | r across drug-doses | 95% CI | q | r without AP-1/IEG/ATF3 arm | r within lines (q) | WT − altered within lines, q | TF mRNA (median line CPM) |
|---|---|---|---|---|---|---|---|
| ATF4 | 0.36 | 0.28 to 0.44 | 9e-26 | 0.09 | -0.008 (0.78) | 0.97 | 188.0 |
| ATF5 | 0.36 | 0.29 to 0.43 | 3e-26 | 0.07 | -0.007 (0.83) | 0.97 | 23.3 |
| XBP1 | 0.29 | 0.22 to 0.37 | 3e-17 | 0.04 | 0.005 (0.88) | 0.97 | 61.1 |
| SRF | 0.31 | 0.23 to 0.38 | 1e-19 | 0.17 | 0.030 (0.13) | 0.97 | 23.9 |
| TP53 | 0.12 | 0.03 to 0.21 | 5e-04 | -0.18 | -0.060 (0.005) | 0.97 | 60.1 |
| E2F4 | 0.03 | -0.10 to 0.16 | 0.44 | -0.05 | -0.080 (4e-07) | 0.97 | 13.7 |
| MEF2A (muscle; known TRIM72 promoter TF) | 0.13 | 0.06 to 0.19 | 2e-04 | -0.01 | 0.007 (0.70) | 1.00 | 298.5 |
| MYOD1 (muscle; known TRIM72 promoter TF) | 0.09 | 0.01 to 0.16 | 0.015 | -0.04 | 0.004 (0.83) | 0.97 | – |

Across drugs TRIM72 tracks hundreds of TF activities, led by the integrated stress response (ATF4, ATF5, XBP1), but most of it
runs through the shared AP-1/IEG/ATF3 arm (ATF4 0.36 -> 0.09 without it). Within lines no TF exceeds TRIM72's noise ceiling
(|r| <= 0.08, the same as its r with FOS); the stress TFs are ~0. TP53 activity is the positive control (it tracks MDM2 and
CDKN1A, WT-selectively). The known muscle promoter TFs (MyoD, myogenin) are not expressed. These are co-responders, not
regulators.

**Upstream: cell-line traits** (T12, untreated level):

| Outcome | Trait | Kind | Lines | rho | Difference (log2), with − without | p | q (all tests) | q (this outcome) |
|---|---|---|---|---|---|---|---|---|
| untreated level (within plate) | PYCARD-AS1_untreated_rel | locus | 48 | 0.82 | – | 2e-08 | 9e-05 | 1e-05 |
| untreated level (within plate) | FUS_untreated_rel | locus | 49 | 0.57 | – | 8e-05 | 0.079 | 0.028 |
| untreated level (within plate) | KMT2D | drivers | 49 | 0.54 | 1.48 | 2e-04 | 0.12 | 0.046 |
| untreated level (within plate) | TP53 WT (vs altered) | tp53 | 49 | 0.07 | 0.18 | 0.64 | 0.89 | 0.92 |

Only TRIM72's own locus predicts its untreated level (PYCARD-AS1 rho 0.82, FUS 0.57): readthrough or 16p11.2 copy number.
TP53 status does not. KMT2D-mutant lines read higher (q 0.046 within this outcome, 0.12 over all line tests; not explained by
the number of driver mutations): a lead, not a finding. Idarubicin's induction per line is mostly the inverse of the untreated
level (rho -0.79).

**Bottom line from Tahoe's own data:** TRIM72 mRNA rises with a p53-independent stress response and does not go with lower
p53 output, by genotype or by measured p53 function, at the line or the cell level. Small effects (a few percent per doubling)
cannot be excluded, because TRIM72 is barely expressed in these lines.

## Running it on your system

Needs the computed atlas (`tahoe_atlas.py compute`, keeping `atlas/pseudobulk`) and gene panel (`tahoe_gene_panel.py all`) in
your Tahoe-100M folder; the 340 GB of cells are not read again, and nothing is written into `atlas/` or `gene_panel/`.

```bash
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M            # ~2 h cold; tables in ~/Tahoe-100M/mg53_p53/
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps summary      # rebuild SUMMARY.md only
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps literature   # optional; needs internet
```

Steps: `perturbations`, `coregulation` (one pass over `atlas/pseudobulk`, ~25 min the first time; downloads a TF list,
HGNC and Ensembl coordinates once), `p53_dependence` (~3 min), `downstream` (~8-14 min), `two_way` (~30 min cold: a pass over
`atlas/pseudobulk`, then the models), `single_cell_all` (two passes over `gene_panel/cells`, ~13 min each: the main run and an
ATF3-adjusted sensitivity run), `upstream_tf` (~5 min; downloads CollecTRI/DoRothEA once; `--offline` uses cached files),
`summary`. Each step's tables go to `<out>/<step folder>/tables` (caches in `cache/`, keyed to the data folder), then
`summary_tables.py` writes `<out>/SUMMARY.md` and `<out>/summary/*.csv` (T1-T12). The log is `<out>/run_mg53_p53.log`.
Reproducibility: a from-scratch run of `run_mg53_p53.py` (all eight steps) into an empty folder took 60 min here and
reproduced all 168 step tables and the 12 summary tables of this folder exactly (on a cold disk expect ~2 h: the
passes over `atlas/pseudobulk` and `gene_panel/cells` are I/O-bound).

| Folder / file | What it holds |
|---|---|
| `run_mg53_p53.py` | Runs the steps below on a Tahoe-100M folder, then `summary_tables.py`. |
| `summary_tables.py`, `SUMMARY.md`, `summary/` | The summary tables (T1-T12) built from the step tables. |
| `gene_modules.csv` | p53 primary targets and the pathway read-outs of the screen, with the literature for each MG53 link. |
| `upstream_perturbations/` | `trim72_upstream_landscape.py`: TRIM72 by drug-dose, plate batch, classes, specificity, programs. |
| `upstream_coregulation/` | `upstream_coregulation.py`: genome-wide co-regulation, untreated partners, the FUS-TRIM72 locus. |
| `p53_dependence/` | `p53_dependence.py`: TP53 wild-type vs altered induction, selinexor, target-likeness. |
| `downstream_p53/` | `downstream_p53.py`: TRIM72 vs p53 output per line, untreated, across drugs, single cells. |
| `two_way/` | `two_way.py`: TRIM72 vs p53 output and pathway read-outs over all drug-doses x lines, TP53 genotype as control. |
| `single_cell_all/` | `single_cell_all.py`: the same contrast in single cells of all wells, placebo genes, functional p53 grouping. |
| `upstream_tf/` | `upstream_tf.py`: transcription-factor activities and cell-line traits vs TRIM72. |
| `literature/` | `evidence_map.md` plus the PubMed / Europe PMC / p53-census / ChIP-Atlas checks that back it. |
| `*/verify/` | The adversarial verifiers' independent scripts and outputs for each workstream (this run's paths). |

## How it was checked

Five workstreams (literature; drug landscape; co-regulation; p53 dependence; downstream p53) each produced findings with
scripts, and an independent verifier per workstream recomputed the key numbers with its own code and tried to break each
claim. Everything above uses the verifiers' corrected wording. What they changed: mitoxantrone dropped from the robust
raisers; class enrichments marked fragile (plate-layout confound); 'equal in WT and altered lines' softened to 'no
requirement, modest WT lean not excluded'; the readthrough claim narrowed (clean for homoharringtonine, unresolved for
idarubicin; Ensembl 110 vs 116 distance); the downstream nulls marked low-power, with the negative-leaning untreated point
estimates reported. The literature citations were all confirmed against the sources.

The three scaled-up steps (section 5) went through the same loop: each was built, then an independent verifier re-derived
it with its own code (fixed-effects fits, per-cell GLMs on raw cells, TF activities), and its code fixes were applied and the
step rerun from scratch. What that changed: the two-way p-values now use the most conservative cluster variance (the active-
subset result went from p 0.005 to 0.015 and became a sensitivity result); the primary test was declared; single-cell CIs use
Hartung-Knapp (the excluded fall per doubling went from 0.6% to 1.2%); the functional-p53 grouping and ambient-RNA controls
were added; the TF analysis gained the AP-1/IEG overlap control and the within-line noise ceiling; caches are keyed to the
data folder; the offline fallback and platform issues were fixed.

Limits: mRNA only, one time point, cancer lines without a muscle program; TP53 status from the annotation (17 WT / 33
altered); most drug-doses are single wells; TRIM72 counts are low (~5 per well x line profile).
