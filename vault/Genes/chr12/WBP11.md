---
symbol: "WBP11"
type: "gene"
col: 1400
ensembl_id: "ENSG00000084463"
name: "WW domain binding protein 11"
location: "12p12.3"
module: 160
arm: "-"
pooled_cpm: 115.0
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# WBP11

*WW domain binding protein 11* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.83× (z +14.1, q 1e-42, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -5.5, q 2e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2]] (+0.62, fdr 7e-06), [[RAF1]] (+0.61, fdr 7e-06), [[LUC7L2]] (+0.61, fdr 1e-05); moves opposite to [[STK40]] (-0.59, fdr 1e-05), [[R3HDM4]] (-0.59, fdr 2e-05), [[OSBP2]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MMP17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.83×** | +14.1 | 1e-42 | 48/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.31×** | +12.8 | 4e-35 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.10×** | +11.4 | 1e-27 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.40×** | +9.8 | 1e-20 | 43/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.77×** | +8.4 | 6e-15 | 43/47 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.72×** | +8.3 | 1e-14 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.71×** | +8.3 | 1e-14 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +7.5 | 5e-12 | 35/48 (A549, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.62×** | +7.1 | 8e-11 | 36/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.57×** | +6.9 | 3e-10 | 36/49 (NCI-H23, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +6.5 | 3e-09 | 41/48 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +6.1 | 5e-08 | 39/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.7 | 7e-07 | 29/49 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.41×** | +5.3 | 6e-06 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.39×** | +4.6 | 1e-04 | 27/45 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 19/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Goserelin (acetate) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.019 | 28/49 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.031 | 25/48 (SW480, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Aliskiren (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.037 | 26/49 (SW480, HOP62, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.092 | 21/48 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.20×** | +2.8 | 0.099 | 17/49 (HEC-1-A, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -5.5 | 2e-05 | 34/48 (SW 900, SW480, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -3.6 | 0.075 | 26/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -3.5 | 0.080 | 28/48 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.819× | -3.1 | 0.31 | 21/48 (NCI-H2030, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.4 | 11 (10 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.45× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.50× (z +10.6) | — |
| [[LoVo (line)]] | wt | 111 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +17.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.46× (z +14.2) | — |
| [[SW480 (line)]] | alt | 150 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +16.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.69× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 129 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +13.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.83× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 86.4 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +15.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.4× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 222 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +12.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.42× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 72.0 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +15.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.46× (z +11.4) | — |
| [[A549 (line)]] | wt | 97.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +18.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.46× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 104 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.73× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 109 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +13.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.70× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 98.9 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.61× (z +11.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.94× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 117 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.60× (z +9.9) | — |
| [[KATO III (line)]] | alt | 130 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +12.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.64× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 199 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +11.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.47× (z +9.9) | — |
| [[SW48 (line)]] | wt | 104 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 8.67× (z +9.3) | — |
| [[A498 (line)]] | wt | 137 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 83.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +10.2) | — |
| [[C32 (line)]] | wt | 104 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 8.90× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 121 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.86× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 90.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.86× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 168 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.41× (z +12.0) | — |
| [[RKO (line)]] | wt | 145 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.54× (z +9.5) | — |
| [[A-427 (line)]] | wt | 161 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 85.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.0× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 86.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 71.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.94× (z +9.3) | — |
| [[J82 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 138 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.68× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 169 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.00× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.42× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 98.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 129 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.51× (z +9.3) | — |
| [[A-172 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 231 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2]] | +0.62 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[RAF1]] | +0.61 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LUC7L2]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RPRD1B]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RAD21]] | +0.59 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[RBM33]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CAND1]] | +0.56 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CNOT1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CHASERR]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF148]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CDC5L]] | +0.55 | +0.60 / +0.54 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 974 |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK40]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[R3HDM4]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[OSBP2]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ARHGEF4]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CLN8]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[EIF5A2]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PFDN2]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DLGAP4]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CMIP]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[HMGA1]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP17]] | B | MMP17 activity strengthens WBP11's drug response | lines that do not express MMP17 (17) vs lines expressing it (32) | the lines without MMP17 respond 0.93× as strongly (z diff +0.61); strongest at Digitoxin 0.5 µM: 1.46x vs 1.86x (z diff +1.7) | 0.013 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; target measured in part of the lines; artifact flags |
| [[LINC02220]] | B | LINC02220 activity lowers WBP11's level | lines that do not express LINC02220 (22) vs lines expressing it (28) | 1.32× higher at baseline in the lines without LINC02220 | 0.028 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WBP11's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **-** arm (projection on the module's main direction -0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (18.6, -5.7); signed map (29.4, -25.5). **Vector** length 75.9, 24.6% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +3.6 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | -0.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | WW domain binding protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:14,784,582-14,803,486 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPWBP, SIPP1, PPP1R165, BUG13 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Cilia and flagella associated; Spliceosomal B complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2W2](https://www.uniprot.org/uniprotkb/Q9Y2W2) (WW domain-binding protein 11):

> Activates pre-mRNA splicing. May inhibit PP1 phosphatase activity.

**Summary**, from NCBI Gene [51729](https://www.ncbi.nlm.nih.gov/gene/51729):

> This gene encodes a nuclear protein, which colocalizes with mRNA splicing factors and intermediate filament-containing perinuclear networks. This protein has 95% amino acid sequence identity to the mouse Wbp11 protein. It contains two proline-rich regions that bind to the WW domain of Npw38, a nuclear protein, and thus this protein is also called Npw38-binding protein NpwBP. The Npw38-NpwBP complex may function as a component of an mRNA factory in the nucleus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16461) · Entrez [51729](https://www.ncbi.nlm.nih.gov/gene/51729) · UniProt [Q9Y2W2](https://www.uniprot.org/uniprotkb/Q9Y2W2) · Ensembl [ENSG00000084463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084463)

## Data

Gene col 1400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1400); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1400]; `tensor/DDL_lfc|DDL_z.npy` [1400]; `embed/gene_vectors.npy` [1400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1400 or target_col == 1400). Every well: [[WBP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
