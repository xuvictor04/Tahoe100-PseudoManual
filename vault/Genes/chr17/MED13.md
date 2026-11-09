---
symbol: "MED13"
type: "gene"
col: 2957
ensembl_id: "ENSG00000108510"
name: "mediator complex subunit 13"
location: "17q23.2"
module: 23
arm: "+"
pooled_cpm: 375.78
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MED13

*mediator complex subunit 13* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.80× (z +40.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.480× (z -19.4, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.500× (z -19.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBBP]] (+0.77, fdr 1e-05), [[ZBED5]] (+0.77, fdr 7e-06), [[ASH1L]] (+0.74, fdr 7e-06); moves opposite to [[ELP1]] (-0.74, fdr 3e-05), [[MAST3]] (-0.68, fdr 3e-05), [[YIF1B]] (-0.64, fdr 0.001, ⚠ one half only (not replicated)), [[RNF216P1]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC122]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.80×** | +40.0 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.80×** | +23.6 | 0e+00 | 48/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +22.7 | 0e+00 | 47/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +20.3 | 0e+00 | 48/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +19.3 | 0e+00 | 48/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +17.3 | 0e+00 | 47/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +17.3 | 0e+00 | 44/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.50×** | +15.5 | 0e+00 | 47/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +9.6 | 6e-20 | 45/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +9.3 | 9e-19 | 43/48 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +9.1 | 6e-18 | 39/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +8.7 | 2e-16 | 32/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +8.1 | 2e-14 | 34/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.1 | 2e-14 | 37/48 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +8.0 | 4e-14 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +7.6 | 1e-12 | 23/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -19.4 | 0e+00 | 43/44 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -19.3 | 0e+00 | 49/49 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.500×** | -19.0 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.494×** | -16.1 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -13.5 | 9e-40 | 47/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.599×** | -13.0 | 1e-36 | 40/45 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.734×** | -8.5 | 2e-15 | 37/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -6.5 | 6e-09 | 21/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.802×** | -6.0 | 1e-07 | 33/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.828×** | -5.2 | 1e-05 | 25/48 (A549, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.823×** | -5.1 | 2e-05 | 26/47 (RKO, SW1417, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.905× | -3.9 | 0.005 | 6/48 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.011 | 25/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.047 | 10/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.920× | -3.2 | 0.051 | 0/48 | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.893× | -3.1 | 0.066 | 9/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.066 | 18/48 (MIA PaCa-2, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.897× | -3.0 | 0.092 | 8/48 (NCI-H1573, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 380 | 14 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 331 | 10 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +27.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -15.8) |
| [[A549 (line)]] | wt | 435 | 9 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +39.4) | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -19.4) |
| [[HEC-1-A (line)]] | alt | 466 | 9 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +27.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -13.2) |
| [[HOP62 (line)]] | alt | 315 | 13 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +32.1) | [[Dinaciclib (drug)]] 0.5 µM 0.548× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.581× (z -10.4) |
| [[SW 900 (line)]] | alt | 315 | 11 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +28.9) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.535× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 374 | 10 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +26.1) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.536× (z -10.2) |
| [[HT-29 (line)]] | alt | 369 | 8 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +25.5) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -18.4) |
| [[hTERT-HPNE (line)]] | wt | 307 | 12 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 429 | 10 (1 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.84× (z +23.0) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 363 | 9 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +29.4) | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.536× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 328 | 8 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +30.3) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 420 | 8 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +30.6) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -15.6) |
| [[BT-474 (line)]] | alt | 366 | 10 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +28.6) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.483× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 407 | 7 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 353 | 9 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -13.8) |
| [[PANC-1 (line)]] | alt | 333 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +42.6) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.570× (z -11.9) |
| [[SW1417 (line)]] | alt | 406 | 7 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +22.4) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 243 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +28.8) | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -15.9) |
| [[SW480 (line)]] | alt | 678 | 4 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -21.1) |
| [[COLO 205 (line)]] | alt | 562 | 8 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -13.6) |
| [[HS-578T (line)]] | alt | 213 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +31.4) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 396 | 7 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.418× (z -13.8) |
| [[RKO (line)]] | wt | 348 | 8 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +24.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -21.9) ⚠ toxic; cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -11.7) |
| [[SNU-423 (line)]] | alt | 377 | 7 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +28.4) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -12.6) |
| [[A-172 (line)]] | wt | 277 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +38.3) | [[Panobinostat (drug)]] 0.5 µM 0.538× (z -10.7) |
| [[H4 (line)]] | wt | 259 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +22.2) | — |
| [[J82 (line)]] | alt | 261 | 8 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +34.1) | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -13.6) |
| [[KATO III (line)]] | alt | 543 | 5 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.53× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -14.9) |
| [[A-427 (line)]] | wt | 384 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.523× (z -12.3) |
| [[HCT15 (line)]] | alt | 447 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 367 | 6 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -12.2) |
| [[SNU-1 (line)]] | wt | 383 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 372 | 6 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.5) |
| [[A498 (line)]] | wt | 273 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +45.3) | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.559× (z -11.1) |
| [[C32 (line)]] | wt | 276 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 638 | 3 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 376 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.500× (z -10.4) |
| [[C-33 A (line)]] | alt | 495 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -15.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 167 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +25.0) | — |
| [[NCI-H2030 (line)]] | alt | 333 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 216 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +22.2) | — |
| [[CHP-212 (line)]] | wt | 772 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -16.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 218 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.08× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.545× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 203 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.0) | [[Radotinib (drug)]] 0.5 µM 0.185× (z -8.9) |
| [[AN3 CA (line)]] | alt | 352 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 461 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 438 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBBP]] | +0.77 | +0.57 / +0.65 | both halves | 1e-05 | pathway: Adipogenesis; STRING 631 |
| [[ZBED5]] | +0.77 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ASH1L]] | +0.74 | +0.65 / +0.62 | both halves | 7e-06 | STRING 464 |
| [[ANKHD1-EIF4EBP3]] | +0.74 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[BAZ2B]] | +0.73 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[CCDC90B-AS1]] | +0.73 | +0.60 / +0.26 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | +0.72 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[PBLD]] | +0.71 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[LINC01004]] | +0.70 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[KANSL1L]] | +0.69 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.68 | +0.51 / +0.28 | both halves | 3e-04 |  |
| [[RNF217-AS1]] | +0.67 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | -0.74 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[MAST3]] | -0.68 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.64 | -0.53 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[RNF216P1]] | -0.64 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[CEP131]] | -0.63 | -0.43 / -0.20 | both halves | 7e-04 |  |
| [[ARRB2]] | -0.63 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[MOCS1]] | -0.63 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.63 | -0.49 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[IMPDH1]] | -0.63 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[MSTO2P]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HACE1]] | -0.62 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.62 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[PIK3R2]] | -0.62 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ACTR5]] | -0.62 | -0.38 / -0.50 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC122]] | B | CCDC122 activity raises MED13's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 1.02× lower at baseline in the lines without CCDC122 | 0.089 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers MED13's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.1, 10.3); signed map (21.8, -9.4). **Vector** length 109, 47.1% of its response variance represented; |z| ≥ 3 in 1,617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.6 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.7 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -9.1 | -13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.2 | -19.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.9 | -16.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.8 | -6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.8 | -8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:61,942,605-62,065,278 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0593, TRAP240; previously THRAP1 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 15 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT); Transcriptional regulation of white adipocyte differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHV7](https://www.uniprot.org/uniprotkb/Q9UHV7) (Mediator of RNA polymerase II transcription subunit 13):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9969](https://www.ncbi.nlm.nih.gov/gene/9969):

> This gene encodes a component of the mediator complex (also known as TRAP, SMCC, DRIP, or ARC), a transcriptional coactivator complex thought to be required for the expression of almost all genes. The mediator complex is recruited by transcriptional activators or nuclear receptors to induce gene expression, possibly by interacting with RNA polymerase II and promoting the formation of a transcriptional pre-initiation complex. The product of this gene is proposed to form a sub-complex with MED12, …

**Accessions** — [HGNC:22474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22474) · Entrez [9969](https://www.ncbi.nlm.nih.gov/gene/9969) · UniProt [Q9UHV7](https://www.uniprot.org/uniprotkb/Q9UHV7) · Ensembl [ENSG00000108510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108510)

## Data

Gene col 2957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2957); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2957]; `tensor/DDL_lfc|DDL_z.npy` [2957]; `embed/gene_vectors.npy` [2957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2957 or target_col == 2957). Every well: [[MED13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
