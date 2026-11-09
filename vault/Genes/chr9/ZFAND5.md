---
symbol: "ZFAND5"
type: "gene"
col: 2849
ensembl_id: "ENSG00000107372"
name: "zinc finger AN1-type containing 5"
location: "9q21.13"
module: 106
arm: "+"
pooled_cpm: 104.73
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# ZFAND5

*zinc finger AN1-type containing 5* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +29.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.693× (z -7.6, q 1e-11, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LoVo 0.242×, Panc 03.27 0.208×, SW 900 0.136×, NCI-H23 0.164×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.481×, HT-29 0.538×, NCI-H23 0.417×, NCI-H2347 0.576×; ⚠ cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.237×, HCT15 0.381×, Panc 03.27 0.437×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP1]] (+0.63, fdr 1e-05), [[AKR1C1]] (+0.62, fdr 1e-05), [[GCLC]] (+0.61, fdr 1e-05); moves opposite to [[CEP43]] (-0.55, fdr 1e-05), [[NSD2]] (-0.52, fdr 1e-05), [[ODF2]] (-0.50, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ADGRF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +29.2 | 0e+00 | 44/48 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +18.5 | 0e+00 | 45/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.21×** | +17.2 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.18×** | +16.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +15.9 | 0e+00 | 44/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +14.1 | 3e-43 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +13.9 | 7e-42 | 40/48 (A-172, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +12.5 | 4e-34 | 45/48 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +11.4 | 2e-28 | 38/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +9.9 | 2e-21 | 42/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.8 | 5e-21 | 33/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +9.4 | 2e-19 | 42/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.0 | 8e-18 | 38/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +8.9 | 3e-17 | 43/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.3 | 1e-11 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +7.1 | 6e-11 | 36/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 1e-05 | 30/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LoVo 0.242×, Panc 03.27 0.208×, SW 900 0.136×, NCI-H23 0.164×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.481×, HT-29 0.538×, NCI-H23 0.417×, NCI-H2347 0.576×; ⚠ cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.237×, HCT15 0.381×, Panc 03.27 0.437×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -7.6 | 1e-11 | 26/44 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.743×** | -6.4 | 4e-08 | 29/49 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.841× | -5.3 | 2e-05 | 24/49 (A498, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.7 | 4e-04 | 2/50 (NCI-H23, SW 1271) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.801×** | -4.6 | 4e-04 | 25/48 (HT-29, SNU-423, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.902× | -3.2 | 0.13 | 5/48 (NCI-H661, NCI-H1573, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.13 | 17/48 (LS 180, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 197 | 24 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +24.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -14.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 93.9 | 24 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.87× (z +21.7) | — |
| [[HT-29 (line)]] | alt | 174 | 6 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 138 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +18.4) | — |
| [[SW480 (line)]] | alt | 91.1 | 12 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +16.1) | — |
| [[LoVo (line)]] | wt | 132 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +24.4) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -18.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 118 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 51.1 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +19.7) | — |
| [[A-172 (line)]] | wt | 100 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +20.6) | — |
| [[BT-474 (line)]] | alt | 92.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 94.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +22.1) | — |
| [[NCI-H1573 (line)]] | alt | 98.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +19.3) | — |
| [[A-427 (line)]] | wt | 59.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.1) | — |
| [[C32 (line)]] | wt | 105 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +25.5) | — |
| [[HOP62 (line)]] | alt | 70.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +24.0) | — |
| [[HS-578T (line)]] | alt | 75.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 62.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.1) | — |
| [[LS 180 (line)]] | wt | 124 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 101 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.4) | — |
| [[SK-MEL-2 (line)]] | alt | 90.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 91.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +24.8) | — |
| [[COLO 205 (line)]] | alt | 120 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +22.9) | — |
| [[SW48 (line)]] | wt | 118 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +10.5) | — |
| [[A549 (line)]] | wt | 102 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 106 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 118 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 159 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 94.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 139 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -18.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 84.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.96× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -11.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[RKO (line)]] | wt | 77.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 176 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +20.9) | — |
| [[Hs 766T (line)]] | wt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 73.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.07× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 98.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 88.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -17.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP1]] | +0.63 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[AKR1C1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GCLC]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZFHX3]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MAP2]] | +0.57 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[JAGN1]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TIPARP]] | +0.57 | +0.48 / +0.62 | both halves | 2e-05 | STRING 449 |
| [[MRFAP1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[UBC]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 | STRING 657 |
| [[IL1R1]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[AKR1C3]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[NSD2]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ODF2]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SFXN2]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[IFI27L1]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TMEM158]] | -0.48 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[BCL7C]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R14B]] | -0.46 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB11]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PIGN]] | -0.46 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[TDP1]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SUGP2]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF4]] | B | ADGRF4 activity raises ZFAND5's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.27× lower at baseline in the lines without ADGRF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[LINC02967]] | B | LINC02967 activity raises ZFAND5's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.29× lower at baseline in the lines without LINC02967 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[SAA1]] | B | SAA1 activity raises ZFAND5's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.26× lower at baseline in the lines without SAA1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises ZFAND5's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without NMRAL2P-1 | 0.028 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[MAFB]] | B | MAFB activity raises ZFAND5's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without MAFB | 0.037 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[NMRAL2P]] | B | NMRAL2P activity raises ZFAND5's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.27× lower at baseline in the lines without NMRAL2P | 0.047 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[LNX1]] | B | LNX1 activity raises ZFAND5's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without LNX1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[KLF4]] | B | KLF4 activity raises ZFAND5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without KLF4 | 0.050 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[SAA2-SAA4]] | B | SAA2-SAA4 activity raises ZFAND5's level | lines that do not express SAA2-SAA4 (22) vs lines expressing it (28) | 1.24× lower at baseline in the lines without SAA2-SAA4 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[A4GALT]] | B | A4GALT activity raises ZFAND5's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.09× lower at baseline in the lines without A4GALT | 0.058 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[ZC3H12A]] | B | ZC3H12A activity raises ZFAND5's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without ZC3H12A | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[RNASEL]] | B | RNASEL activity raises ZFAND5's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.34× lower at baseline in the lines without RNASEL | 0.091 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.8, 47.2); signed map (52.7, -9.9). **Vector** length 112, 34.9% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.5 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +17.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +16.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.0 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.3 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.1 | -4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.3 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.1 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:72,351,413-72,365,235 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFAND5A; previously ZNF216, ZA20D2 |
| Gene groups (HGNC) | Zinc fingers AN1-type; Zinc fingers A20-type |
| Matched by | ensembl_id |

**Function**, from UniProt [O76080](https://www.uniprot.org/uniprotkb/O76080) (AN1-type zinc finger protein 5):

> Involved in protein degradation via the ubiquitin-proteasome system. May act by anchoring ubiquitinated proteins to the proteasome. Plays a role in ubiquitin-mediated protein degradation during muscle atrophy. Plays a role in the regulation of NF-kappa-B activation and apoptosis. Inhibits NF-kappa-B activation triggered by overexpression of RIPK1 and TRAF6 but not of RELA. Also inhibits tumor necrosis factor (TNF), IL-1 and TLR4-induced NF-kappa-B activation in a dose-dependent manner. …

**Summary**, from NCBI Gene [7763](https://www.ncbi.nlm.nih.gov/gene/7763):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to act upstream of or within several processes, including face development; fibroblast migration; and respiratory system process. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13008) · Entrez [7763](https://www.ncbi.nlm.nih.gov/gene/7763) · UniProt [O76080](https://www.uniprot.org/uniprotkb/O76080) · Ensembl [ENSG00000107372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107372)

## Data

Gene col 2849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2849); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2849]; `tensor/DDL_lfc|DDL_z.npy` [2849]; `embed/gene_vectors.npy` [2849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2849 or target_col == 2849). Every well: [[ZFAND5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
