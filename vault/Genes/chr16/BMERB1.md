---
symbol: "BMERB1"
type: "gene"
col: 9354
ensembl_id: "ENSG00000166780"
name: "bMERB domain containing 1"
location: "16p13.11"
module: 136
arm: "+"
pooled_cpm: 125.1
n_lines_expressing: 33
n_dd_up: 15
n_dd_down: 39
n_dd_up_clean: 14
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# BMERB1

*bMERB domain containing 1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.80× (z +13.2, q 4e-37, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.259× (z -42.8, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.70, fdr 1e-05), [[STC1]] (+0.69, fdr 7e-06), [[SMOX]] (+0.65, fdr 7e-06); moves opposite to [[DERA]] (-0.56, fdr 6e-05), [[DECR1]] (-0.54, fdr 2e-04), [[ARHGEF17]] (-0.54, fdr 1e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00869-1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PTPRS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +13.2 | 4e-37 | 21/31 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +13.0 | 3e-36 | 21/31 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +12.4 | 5e-33 | 20/31 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +11.1 | 1e-26 | 24/31 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +10.6 | 2e-24 | 18/31 (C32, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +8.3 | 1e-14 | 22/32 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +7.4 | 1e-11 | 18/31 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.9 | 4e-10 | 19/31 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +6.4 | 9e-09 | 17/31 (PANC-1, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.9 | 2e-07 | 15/31 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.3 | 6e-06 | 17/32 (A-172, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +4.3 | 8e-04 | 16/32 (NCI-H1573, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 12/31 (BT-474, HS-578T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.8 | 0.006 | 14/30 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.019 | 15/30 (NCI-H23, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.026 | 8/32 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.047 | 10/31 (Hs 766T, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.259×** | -42.8 | 0e+00 | 29/31 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.395×** | -29.4 | 0e+00 | 30/32 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -20.1 | 0e+00 | 25/31 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -16.8 | 0e+00 | 26/31 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -14.7 | 0e+00 | 26/31 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -13.4 | 8e-39 | 26/32 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -11.6 | 2e-29 | 25/29 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -10.7 | 4e-25 | 23/31 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -10.7 | 9e-25 | 23/29 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -10.3 | 5e-23 | 20/31 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -10.2 | 9e-23 | 20/31 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -9.7 | 1e-20 | 23/31 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -9.6 | 4e-20 | 21/31 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -9.5 | 1e-19 | 25/30 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -9.0 | 6e-18 | 21/32 (HS-578T, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -8.8 | 7e-17 | 21/31 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.721×** | -8.2 | 6e-15 | 20/33 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.750×** | -7.8 | 2e-13 | 21/31 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -7.6 | 1e-12 | 19/31 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.721×** | -7.0 | 5e-11 | 20/30 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 122 | 0 | 22 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 518 | 0 | 17 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -26.1) |
| [[MIA PaCa-2 (line)]] | alt | 356 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -31.0) |
| [[HOP62 (line)]] | alt | 82.5 | 4 | 9 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -24.6) |
| [[A-172 (line)]] | wt | 109 | 4 | 8 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.76× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -33.8) |
| [[AsPC-1 (line)]] | alt | 232 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -25.1) |
| [[C32 (line)]] | wt | 83.1 | 4 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -24.2) |
| [[H4 (line)]] | wt | 176 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.1) |
| [[NCI-H1792 (line)]] | alt | 247 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -30.5) |
| [[PANC-1 (line)]] | alt | 335 | 3 (2 ⚠) | 8 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.58× (z +8.9) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.59× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -31.4) |
| [[LOX-IMVI (line)]] | wt | 90.2 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.7) |
| [[A-427 (line)]] | wt | 109 | 5 (1 ⚠) | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.23× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -20.7) |
| [[HepG2_C3A (line)]] | wt | 148 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.2) |
| [[Hs 766T (line)]] | wt | 108 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.31× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -25.8) |
| [[hTERT-HPNE (line)]] | wt | 138 | 3 | 5 | [[Tucidinostat (drug)]] 5 µM 1.81× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -21.4) |
| [[SW 900 (line)]] | alt | 137 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -23.6) |
| [[A549 (line)]] | wt | 258 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.0) |
| [[HS-578T (line)]] | alt | 174 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -31.6) |
| [[J82 (line)]] | alt | 32.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 4.79× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 200 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -30.0) |
| [[SHP-77 (line)]] | alt | 248 | 3 (1 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.86× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.3) |
| [[BT-474 (line)]] | alt | 37.0 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 3.61× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.3) |
| [[C-33 A (line)]] | alt | 95.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.5) |
| [[SNU-1 (line)]] | wt | 81.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -9.5) |
| [[CHP-212 (line)]] | wt | 191 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -14.3) |
| [[SW 1088 (line)]] | alt | 215 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.0) |
| [[SW 1271 (line)]] | alt | 150 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.6) |
| [[A498 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 19.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[STC1]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SMOX]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CACNG7]] | +0.64 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ETV5]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ETHE1]] | +0.63 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ARID3B]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MMP1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[BMP6]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CIB1]] | +0.59 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DERA]] | -0.56 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[DECR1]] | -0.54 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[ARHGEF17]] | -0.54 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[C5orf15]] | -0.54 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[LINC00869-1]] | -0.53 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[AJUBA]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD18B]] | -0.51 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[FUBP1]] | -0.51 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TAPBPL]] | -0.51 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ZXDA]] | -0.50 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[PM20D2]] | -0.50 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[HMGN2]] | -0.50 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ZFX]] | -0.50 | -0.44 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00869-1]] | B | LINC00869-1 activity lowers BMERB1's level | lines that do not express LINC00869-1 (7) vs lines expressing it (43) | 3.10× higher at baseline in the lines without LINC00869-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: OSBPL10, STPG2, EIF4E3; maybe low, not absent |
| [[RASSF8]] | C | RASSF8 activity raises BMERB1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 3.63× lower at baseline in the lines without RASSF8 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRS]] | B | BMERB1 activity raises PTPRS's level | lines that do not express BMERB1 (17) vs lines expressing it (33) | 3.36× lower at baseline in the lines without BMERB1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000259363, NRG1, NPTX1 |
| [[NPAS2]] | B | BMERB1 activity raises NPAS2's level | lines that do not express BMERB1 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without BMERB1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000259363, NRG1, NPTX1 |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 2.8); signed map (3.5, 48.8). **Vector** length 132, 39.7% of its response variance represented; |z| ≥ 3 in 1,429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.4 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.1 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.9 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.8 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.3 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.2 | -8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.5 | -7.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.2 | -6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.9 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.9 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | bMERB domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,434,475-15,625,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32618; previously C16orf45 |
| Gene groups (HGNC) | Bivalent Mical/EHBP Rab binding domain containing |
| Matched by | ensembl_id |

UniProt [Q96MC5](https://www.uniprot.org/uniprotkb/Q96MC5) carries no function annotation.

**Summary**, from NCBI Gene [89927](https://www.ncbi.nlm.nih.gov/gene/89927):

> Predicted to be involved in negative regulation of microtubule depolymerization. Predicted to act upstream of or within negative regulation of cell motility involved in cerebral cortex radial glia guided migration. Predicted to be active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19213) · Entrez [89927](https://www.ncbi.nlm.nih.gov/gene/89927) · UniProt [Q96MC5](https://www.uniprot.org/uniprotkb/Q96MC5) · Ensembl [ENSG00000166780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166780)

## Data

Gene col 9354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9354); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9354]; `tensor/DDL_lfc|DDL_z.npy` [9354]; `embed/gene_vectors.npy` [9354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9354 or target_col == 9354). Every well: [[BMERB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMERB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
