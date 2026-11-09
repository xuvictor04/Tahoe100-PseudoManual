---
symbol: "TFPI2"
type: "gene"
col: 2671
ensembl_id: "ENSG00000105825"
name: "tissue factor pathway inhibitor 2"
location: "7q21.3"
module: 81
arm: "+"
pooled_cpm: 131.15
n_lines_expressing: 28
n_dd_up: 27
n_dd_down: 36
n_dd_up_clean: 8
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TFPI2

*tissue factor pathway inhibitor 2* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.95× (z +13.4, q 3e-38, up in 26 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +10.1, q 3e-21, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.425× (z -6.4, q 7e-08, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL8]] (+0.75, fdr 7e-06), [[BCL2A1]] (+0.68, fdr 7e-06), [[PKIA]] (+0.65, fdr 7e-06); moves opposite to [[CMKLR2]] (-0.50, fdr 2e-05), [[TSC22D3]] (-0.50, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NT5E]] → it (grade B ⚠); 6 go from it, the strongest it → [[CXCL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **4.95×** | +13.4 | 3e-38 | 26/27 (LOX-IMVI, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +10.1 | 3e-21 | 21/27 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.31×** | +9.7 | 8e-20 | 22/24 (Hs 766T, NCI-H23, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.11×** | +9.2 | 7e-18 | 21/26 (NCI-H1573, NCI-H2347, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.16×** | +8.9 | 5e-17 | 21/25 (A549, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +8.8 | 9e-17 | 25/26 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.85×** | +8.8 | 1e-16 | 24/26 (SK-MEL-2, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.79×** | +8.6 | 4e-16 | 24/26 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.75×** | +8.5 | 1e-15 | 23/26 (SK-MEL-2, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.98×** | +8.1 | 3e-14 | 17/26 (CFPAC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.59×** | +8.0 | 6e-14 | 23/26 (SK-MEL-2, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.47×** | +7.6 | 1e-12 | 25/26 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.22×** | +6.7 | 8e-10 | 24/26 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.07×** | +5.9 | 1e-07 | 19/28 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.98×** | +5.7 | 4e-07 | 24/26 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.2 | 7e-06 | 22/27 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +4.6 | 1e-04 | 19/26 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 17/27 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.020 | 20/26 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.74×** | +3.2 | 0.029 | 16/26 (NCI-H661, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.049 | 12/26 (NCI-H1792, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 2 with an alert ⚠; shown: the 15 strongest. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.425×** | -6.4 | 7e-08 | 22/28 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.479×** | -6.1 | 2e-07 | 20/26 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.594×** | -5.9 | 8e-07 | 17/26 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.502×** | -5.3 | 1e-05 | 19/26 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.529×** | -5.3 | 1e-05 | 23/26 (NCI-H460, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.529×** | -5.3 | 1e-05 | 21/26 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.629×** | -4.7 | 2e-04 | 18/26 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Quinestrol (drug)]] 5 µM |  | **0.672×** | -4.7 | 2e-04 | 21/27 (A498, LOX-IMVI, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.672×** | -4.7 | 2e-04 | 17/26 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.562×** | -4.6 | 2e-04 | 19/25 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.582×** | -4.5 | 4e-04 | 18/25 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.571×** | -4.5 | 4e-04 | 20/26 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.585×** | -4.5 | 4e-04 | 17/26 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.589×** | -4.4 | 4e-04 | 20/26 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.593×** | -4.3 | 5e-04 | 22/26 (NCI-H23, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 740 | 7 (6 ⚠) | 14 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.49× (z +12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.78× (z +8.6) | [[Adagrasib (drug)]] 0.05 µM 0.400× (z -18.9) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0663× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 581 | 7 (7 ⚠) | 13 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.4) ⚠ cell-cycle shift, explains ~39% of this change | [[Trametinib (drug)]] 5 µM 0.177× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 67.8 | 14 (14 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +21.8) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[A-172 (line)]] | wt | 35.9 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +17.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 150 | 10 (8 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 28.9× (z +19.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.78× (z +14.5) | [[Binimetinib (drug)]] 0.5 µM 0.283× (z -8.7) |
| [[A549 (line)]] | wt | 140 | 11 (11 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 9.17× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 33.7 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +15.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 6.40× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 175 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +23.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +13.3) | — |
| [[J82 (line)]] | alt | 52.2 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 16.2× (z +16.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.30× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 6 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.347× (z -22.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.133× (z -11.5) |
| [[A498 (line)]] | wt | 292 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +15.0) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[HOP62 (line)]] | alt | 35.7 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 15.6× (z +13.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 72.6 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +13.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 158 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 97.3 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.63× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 36.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 277 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.05× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[H4 (line)]] | wt | 33.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.6× (z +9.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 44.6 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.136× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 687 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.567× (z -12.4) ⚠ position not correctable |
| [[SW 900 (line)]] | alt | 246 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.72× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 30.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 568 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL8]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[BCL2A1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PKIA]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PTGS2]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TM4SF1]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[SERPINE2]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IL13RA2]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[STC1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 | STRING 453 |
| [[ANTXR2]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TSC22D3]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5E]] | B | NT5E activity raises TFPI2's level | lines that do not express NT5E (14) vs lines expressing it (36) | 4.81× lower at baseline in the lines without NT5E | 0.018 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[CD274]] | B | CD274 activity raises TFPI2's level | lines that do not express CD274 (18) vs lines expressing it (32) | 3.19× lower at baseline in the lines without CD274 | 0.055 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[NR3C1]] | B | NR3C1 activity lowers TFPI2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[CYB5R2]] | B | CYB5R2 activity raises TFPI2's level | lines that do not express CYB5R2 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without CYB5R2 | 0.099 | ⚠ within organs, on part of the lines; also absent: RP1, PI3, LINC02968 |
| [[GJA1]] | C | GJA1 activity raises TFPI2's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 6.17× lower at baseline in the lines without GJA1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[IL13RA2]] | C | IL13RA2 activity raises TFPI2's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 4.53× lower at baseline in the lines without IL13RA2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[TUSC3]] | C | TUSC3 activity raises TFPI2's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 6.18× lower at baseline in the lines without TUSC3 | 0.075 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; co-absent with the target |
| [[STC1]] | C | STC1 activity raises TFPI2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 4.83× lower at baseline in the lines without STC1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[GNG11]] | C | GNG11 activity raises TFPI2's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 4.85× lower at baseline in the lines without GNG11 | 0.093 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL1]] | B | TFPI2 activity raises CXCL1's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without TFPI2 | 0.063 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6 |
| [[SHB]] | B | TFPI2 activity raises SHB's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without TFPI2 | 0.078 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6 |
| [[STC1]] | C | TFPI2 activity raises STC1's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 6.47× lower at baseline in the lines without TFPI2 | 0.025 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6; co-absent with the target |
| [[PTHLH]] | C | TFPI2 activity raises PTHLH's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without TFPI2 | 0.048 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6; co-absent with the target |
| [[IL1B]] | C | TFPI2 activity raises IL1B's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 3.46× lower at baseline in the lines without TFPI2 | 0.074 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6; co-absent with the target |
| [[CXCL8]] | C | TFPI2 activity raises CXCL8's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 4.32× lower at baseline in the lines without TFPI2 | 0.080 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 13.9); signed map (3.7, 47.6). **Vector** length 122, 39.8% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +5.7 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.2 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | tissue factor pathway inhibitor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:93,885,396-93,890,753 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP5, TFPI-2, REF1 |
| Hallmark sets | COAGULATION, COMPLEMENT, ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P48307](https://www.uniprot.org/uniprotkb/P48307) (Tissue factor pathway inhibitor 2):

> May play a role in the regulation of plasmin-mediated matrix remodeling. Inhibits trypsin, plasmin, factor VIIa/tissue factor and weakly factor Xa. Has no effect on thrombin.

**Summary**, from NCBI Gene [7980](https://www.ncbi.nlm.nih.gov/gene/7980):

> This gene encodes a member of the Kunitz-type serine proteinase inhibitor family. The protein can inhibit a variety of serine proteases including factor VIIa/tissue factor, factor Xa, plasmin, trypsin, chymotryspin and plasma kallikrein. This gene has been identified as a tumor suppressor gene in several types of cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:11761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11761) · Entrez [7980](https://www.ncbi.nlm.nih.gov/gene/7980) · UniProt [P48307](https://www.uniprot.org/uniprotkb/P48307) · Ensembl [ENSG00000105825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105825)

## Data

Gene col 2671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2671); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2671]; `tensor/DDL_lfc|DDL_z.npy` [2671]; `embed/gene_vectors.npy` [2671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2671 or target_col == 2671). Every well: [[TFPI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFPI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
