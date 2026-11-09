---
symbol: "OSBPL8"
type: "gene"
col: 1649
ensembl_id: "ENSG00000091039"
name: "oxysterol binding protein like 8"
location: "12q21.2"
module: 78
arm: "+"
pooled_cpm: 301.27
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# OSBPL8

*oxysterol binding protein like 8* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.58× (z +26.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.716× (z -8.8, q 5e-16, down in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.833× (z -7.1, q 4e-10, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK4]] (+0.60, fdr 1e-05), [[CAP1]] (+0.59, fdr 1e-05), [[HPCAL1]] (+0.57, fdr 7e-05); moves opposite to [[TRAPPC13]] (-0.59, fdr 1e-05), [[SMAD1]] (-0.59, fdr 3e-05), [[MAIP1]] (-0.56, fdr 9e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.58×** | +26.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +21.6 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +19.3 | 0e+00 | 48/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +17.8 | 0e+00 | 48/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +16.8 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.80×** | +16.2 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +15.9 | 0e+00 | 48/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +14.9 | 0e+00 | 37/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +11.0 | 2e-26 | 40/47 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +10.3 | 3e-23 | 38/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +7.3 | 1e-11 | 32/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +7.0 | 9e-11 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.28×** | +6.9 | 2e-10 | 31/49 (HS-578T, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +6.5 | 4e-09 | 30/48 (LOX-IMVI, SW 900, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.27×** | +6.2 | 2e-08 | 26/45 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.2 | 9e-04 | 31/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 27/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.15× | +3.7 | 0.006 | 10/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.007 | 26/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.015 | 12/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.020 | 25/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -8.8 | 5e-16 | 40/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -7.1 | 4e-10 | 25/49 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.833× | -6.0 | 4e-07 | 21/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.837× | -5.9 | 5e-07 | 23/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.857× | -5.9 | 5e-07 | 18/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -5.7 | 9e-07 | 26/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.811×** | -5.5 | 2e-06 | 28/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -5.5 | 3e-06 | 26/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.814×** | -5.3 | 6e-06 | 26/50 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.815×** | -5.3 | 8e-06 | 26/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.828×** | -5.2 | 1e-05 | 25/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.873× | -5.1 | 2e-05 | 16/49 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.830×** | -4.7 | 9e-05 | 24/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.846× | -4.6 | 2e-04 | 20/49 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.846× | -4.6 | 2e-04 | 19/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.848× | -4.3 | 7e-04 | 22/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.852× | -4.1 | 0.002 | 12/47 (BT-474, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 233 | 16 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +31.6) | — |
| [[SW480 (line)]] | alt | 360 | 13 (6 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +29.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -13.4) |
| [[PANC-1 (line)]] | alt | 277 | 10 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +30.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 339 | 8 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.20× (z +28.0) | [[Trametinib (drug)]] 5 µM 0.553× (z -9.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.647× (z -8.9) |
| [[C32 (line)]] | wt | 231 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.0) | — |
| [[NCI-H1792 (line)]] | alt | 371 | 9 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -19.0) |
| [[BT-474 (line)]] | alt | 204 | 9 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.62× (z +21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +19.6) | — |
| [[H4 (line)]] | wt | 248 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 233 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +18.5) | — |
| [[HT-29 (line)]] | alt | 214 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +21.3) | — |
| [[LoVo (line)]] | wt | 348 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +27.2) | — |
| [[LOX-IMVI (line)]] | wt | 546 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +17.1) | — |
| [[NCI-H1573 (line)]] | alt | 230 | 8 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +25.6) | [[Cobimetinib (drug)]] 5 µM 0.583× (z -8.8) |
| [[SW1417 (line)]] | alt | 316 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +21.4) | — |
| [[A-427 (line)]] | wt | 496 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.630× (z -9.3) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HS-578T (line)]] | alt | 318 | 7 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.26× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -13.2) |
| [[J82 (line)]] | alt | 306 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +18.4) | — |
| [[KATO III (line)]] | alt | 152 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 415 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +13.9) | [[Adagrasib (drug)]] 0.05 µM 0.666× (z -20.8) ⚠ position not correctable · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.478× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 296 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +17.8) | — |
| [[SNU-1 (line)]] | wt | 301 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 468 | 7 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -10.6) |
| [[A549 (line)]] | wt | 248 | 6 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.47× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -13.7) |
| [[HOP62 (line)]] | alt | 273 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +16.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.556× (z -9.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 306 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 311 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +18.3) | — |
| [[RKO (line)]] | wt | 575 | 4 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 183 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +23.4) | — |
| [[SW48 (line)]] | wt | 283 | 6 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.2) | — |
| [[A498 (line)]] | wt | 252 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 270 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 253 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +14.6) | — |
| [[A-172 (line)]] | wt | 318 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 193 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 330 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +19.6) | — |
| [[SNU-423 (line)]] | alt | 469 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 169 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 182 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.62× (z +18.6) | — |
| [[HEC-1-A (line)]] | alt | 279 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 319 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 233 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.6) |
| [[HCT15 (line)]] | alt | 279 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.09× (z +10.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.85× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 315 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 362 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[NCI-H2122 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 321 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK4]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CAP1]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.57 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[ITGB1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FAM3C2P]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FMNL2]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[AKAP13]] | +0.55 | +0.57 / +0.39 | both halves | 6e-05 | same gene group |
| [[MYADM]] | +0.55 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[EMP1]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[LYPLA1]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[KANK2]] | +0.52 | +0.52 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SMAD1]] | -0.59 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[MAIP1]] | -0.56 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[C14orf93]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MOV10]] | -0.55 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[LINC02100]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[PPP1R8]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PEF1]] | -0.54 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[C2orf42]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MTG2]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[C5orf15]] | -0.53 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[PSMC2]] | -0.53 | -0.57 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity lowers OSBPL8's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.63× higher at baseline in the lines without TBC1D8 | 0.002 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises OSBPL8's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[ITGA6]] | B | ITGA6 activity lowers OSBPL8's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without ITGA6 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises OSBPL8's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 5.0); signed map (-8.1, 40.0). **Vector** length 120, 44.9% of its response variance represented; |z| ≥ 3 in 1,774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +7.9 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +7.1 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.9 | +1.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.9 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.4 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.2 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:76,351,797-76,559,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSBP10, ORP8, MST120, MSTP120 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PS; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZF1](https://www.uniprot.org/uniprotkb/Q9BZF1) (Oxysterol-binding protein-related protein 8):

> Lipid transporter involved in lipid countertransport between the endoplasmic reticulum and the plasma membrane: specifically exchanges phosphatidylserine with phosphatidylinositol 4-phosphate (PI4P), delivering phosphatidylserine to the plasma membrane in exchange for PI4P, which is degraded by the SAC1/SACM1L phosphatase in the endoplasmic reticulum. Binds phosphatidylserine and PI4P in a mutually exclusive manner. Binds oxysterol, 25-hydroxycholesterol and cholesterol.

**Summary**, from NCBI Gene [114882](https://www.ncbi.nlm.nih.gov/gene/114882):

> This gene encodes a member of a family of proteins containing an N-terminal pleckstrin homology domain and a highly conserved C-terminal oxysterol-binding protein-like sterol-binding domain. It binds mutliple lipid-containing molecules, including phosphatidylserine, phosphatidylinositol 4-phosphate (PI4P) and oxysterol, and promotes their exchange between the endoplasmic reticulum and the plasma membrane. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb …

**Accessions** — [HGNC:16396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16396) · Entrez [114882](https://www.ncbi.nlm.nih.gov/gene/114882) · UniProt [Q9BZF1](https://www.uniprot.org/uniprotkb/Q9BZF1) · Ensembl [ENSG00000091039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091039)

## Data

Gene col 1649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1649); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1649]; `tensor/DDL_lfc|DDL_z.npy` [1649]; `embed/gene_vectors.npy` [1649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1649 or target_col == 1649). Every well: [[OSBPL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
