---
symbol: "VWA5A"
type: "gene"
col: 3098
ensembl_id: "ENSG00000110002"
name: "von Willebrand factor A domain containing 5A"
location: "11q24.2"
module: 5
arm: "-"
pooled_cpm: 5.25
n_lines_expressing: 37
n_dd_up: 32
n_dd_down: 25
n_dd_up_clean: 27
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# VWA5A

*von Willebrand factor A domain containing 5A* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.99× (z +15.7, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.248× (z -14.2, q 1e-42, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPRE2]] (+0.58, fdr 2e-05), [[PRSS16]] (+0.58, fdr 2e-05), [[OAZ2]] (+0.58, fdr 3e-05); moves opposite to [[MACROD1]] (-0.60, fdr 1e-05), [[MYO19]] (-0.58, fdr 1e-05), [[E2F3]] (-0.56, fdr 6e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EYA1]] → it (grade B ⚠); 4 go from it, the strongest it → [[AMOT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.99×** | +15.7 | 0e+00 | 31/34 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.83×** | +13.6 | 1e-39 | 31/33 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.52×** | +12.7 | 7e-35 | 30/33 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +8.9 | 6e-17 | 26/33 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +8.3 | 1e-14 | 26/33 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.75×** | +8.0 | 1e-13 | 17/34 (NCI-H2030, LS 180, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +7.6 | 3e-12 | 23/31 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.5 | 6e-12 | 3/7 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **2.00×** | +6.7 | 1e-09 | 18/31 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.73×** | +5.6 | 2e-06 | 15/31 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.83×** | +5.5 | 2e-06 | 14/34 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.58×** | +5.0 | 3e-05 | 13/34 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 1e-04 | 14/34 (LS 180, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.7 | 1e-04 | 16/33 (KATO III, PANC-1, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.61×** | +4.6 | 1e-04 | 10/31 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.004 | 9/32 (KATO III, PANC-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.005 | 9/34 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.248×** | -14.2 | 1e-42 | 29/33 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.332×** | -11.2 | 1e-26 | 25/28 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.340×** | -11.0 | 1e-25 | 26/32 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.373×** | -10.0 | 2e-21 | 25/32 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.457×** | -7.9 | 2e-13 | 20/33 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.494×** | -7.2 | 7e-11 | 22/33 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.596×** | -5.1 | 3e-05 | 17/34 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -4.7 | 2e-04 | 14/27 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -4.7 | 2e-04 | 16/32 (SW 900, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.618×** | -4.6 | 2e-04 | 16/31 (NCI-H2030, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.431×** | -4.5 | 4e-04 | 10/28 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.454×** | -4.2 | 0.001 | 12/28 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.473×** | -4.0 | 0.003 | 11/30 (SNU-423, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.006 | 11/33 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.692×** | -3.6 | 0.012 | 9/24 (KATO III, SW480, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.710×** | -3.5 | 0.017 | 12/30 (C-33 A, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.714×** | -3.4 | 0.019 | 5/33 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.626×** | -3.4 | 0.020 | 10/34 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.48 | 1 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.80× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.0401× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0731× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 9.01 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.19× (z +8.5) | [[Digitoxin (drug)]] 0.05 µM 0.0437× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.158× (z -9.6) |
| [[PANC-1 (line)]] | alt | 3.81 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 10.6× (z +9.5) | [[Digitoxin (drug)]] 0.05 µM 0.0742× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -11.7) |
| [[H4 (line)]] | wt | 7.73 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0277× (z -10.0) |
| [[KATO III (line)]] | alt | 11.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.57× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.140× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 18.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.10× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.130× (z -8.9) |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0794× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 7.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 1.95 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PRSS16]] | +0.58 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[OAZ2]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[AMOT]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RAB30]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RYBP]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TTC3P1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ALAD]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PJA2]] | +0.54 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[LMBRD1]] | +0.53 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[GSTM4]] | +0.53 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[LINC01273]] | +0.52 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROD1]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[MYO19]] | -0.58 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[E2F3]] | -0.56 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[TRMT1]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CDR2]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.55 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PRMT3]] | -0.55 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[TRNT1]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CAPN15]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TIMM23B-AGAP6]] | -0.55 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[SCLY]] | -0.54 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ATR]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EYA1]] | B | EYA1 activity raises VWA5A's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without EYA1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[ASXL3]] | B | ASXL3 activity raises VWA5A's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 1.55× lower at baseline in the lines without ASXL3 | 0.087 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOT]] | B | VWA5A activity raises AMOT's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without VWA5A | 0.042 | ⚠ within organs, on part of the lines |
| [[MAP2K6]] | B | VWA5A activity raises MAP2K6's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without VWA5A | 0.057 | ⚠ within organs, on part of the lines |
| [[TDRD3]] | B | VWA5A activity raises TDRD3's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without VWA5A | 0.061 | ⚠ within organs, on part of the lines |
| [[TMEM14A]] | B | VWA5A activity raises TMEM14A's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without VWA5A | 0.082 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (18.3, 1.2); signed map (-4.4, 16.9). **Vector** length 57.6, 10.1% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -10.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor A domain containing 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,115,404-124,147,721 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCSC-1; previously LOH11CR2A |
| Hallmark sets | KRAS_SIGNALING_UP, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O00534](https://www.uniprot.org/uniprotkb/O00534) (von Willebrand factor A domain-containing protein 5A):

> May play a role in tumorigenesis as a tumor suppressor. Altered expression of this protein and disruption of the molecular pathway it is involved in, may contribute directly to or modify tumorigenesis.

**Summary**, from NCBI Gene [4013](https://www.ncbi.nlm.nih.gov/gene/4013):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6658) · Entrez [4013](https://www.ncbi.nlm.nih.gov/gene/4013) · UniProt [O00534](https://www.uniprot.org/uniprotkb/O00534) · Ensembl [ENSG00000110002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110002)

## Data

Gene col 3098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3098); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3098]; `tensor/DDL_lfc|DDL_z.npy` [3098]; `embed/gene_vectors.npy` [3098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3098 or target_col == 3098). Every well: [[VWA5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWA5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
