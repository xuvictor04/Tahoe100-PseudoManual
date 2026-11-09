---
symbol: "MED27"
type: "gene"
col: 8356
ensembl_id: "ENSG00000160563"
name: "mediator complex subunit 27"
location: "9q34.13"
module: 36
arm: "+"
pooled_cpm: 94.49
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# MED27

*mediator complex subunit 27* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.64× (z +21.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.432× (z -18.4, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.770× (z -8.1, q 7e-14, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLK]] (+0.60, fdr 1e-05), [[PGP]] (+0.59, fdr 2e-05), [[ABL1]] (+0.57, fdr 1e-05); moves opposite to [[SUGT1P3]] (-0.53, fdr 4e-05), [[AP1AR]] (-0.50, fdr 3e-05), [[CYP2U1]] (-0.49, fdr 7e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.64×** | +21.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.29×** | +19.0 | 0e+00 | 47/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +18.3 | 0e+00 | 38/48 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +16.1 | 0e+00 | 44/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +15.0 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +14.0 | 3e-42 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.28×** | +13.5 | 7e-40 | 46/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +12.3 | 6e-33 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.71×** | +11.6 | 2e-29 | 40/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.6 | 3e-29 | 39/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +10.9 | 5e-26 | 28/49 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +10.7 | 5e-25 | 42/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +10.6 | 9e-25 | 42/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +10.2 | 6e-23 | 37/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +9.6 | 3e-20 | 38/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 8e-11 | 32/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +6.4 | 6e-09 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 3e-07 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.432×** | -18.4 | 0e+00 | 46/49 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -18.3 | 0e+00 | 37/44 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -10.7 | 2e-24 | 33/45 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -8.1 | 7e-14 | 37/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.705×** | -7.7 | 2e-12 | 39/49 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.811×** | -4.6 | 4e-04 | 24/48 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.831×** | -4.1 | 0.004 | 17/48 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.837× | -3.9 | 0.006 | 16/48 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.846× | -3.7 | 0.014 | 16/48 (KATO III, NCI-H1792, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.848× | -3.7 | 0.015 | 17/49 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.858× | -3.4 | 0.037 | 14/48 (KATO III, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.038 | 18/48 (RPMI-7951, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.05 µM |  | 0.894× | -3.3 | 0.046 | 4/49 (AN3 CA, SK-MEL-2, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.868× | -3.1 | 0.072 | 16/48 (AsPC-1, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.095 | 11/48 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 76.6 | 18 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 76.8 | 12 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.3 | 10 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 94.9 | 8 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.37× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 53.9 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.11× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.7 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.85× (z +13.7) | — |
| [[KATO III (line)]] | alt | 61.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 174 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +12.9) | — |
| [[H4 (line)]] | wt | 77.7 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.13× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 86.2 | 6 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.45× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.0 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.4 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.489× (z -9.3) |
| [[RKO (line)]] | wt | 269 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -27.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 87.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 155 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 105 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.36× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 135 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.70× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -14.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 52.5 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.6 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 146 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -14.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 67.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 68.9 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 74.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.9) | — |
| [[C32 (line)]] | wt | 220 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.506× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 87.0 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +11.5) | — |
| [[J82 (line)]] | alt | 147 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -19.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 68.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -14.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 67.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 133 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 97.8 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -13.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 94.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 55.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -16.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 89.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 96.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -11.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0400× (z -28.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -16.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0734× (z -11.5) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -8.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLK]] | +0.60 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PGP]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ABL1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[EMC8]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[VPS53]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[AP4E1]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TOMM22]] | +0.55 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[NPLOC4]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ARPC5L]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PHF5A]] | +0.53 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[RAB5IF]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[HIRA]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P3]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[AP1AR]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CYP2U1]] | -0.49 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[KPNA5]] | -0.47 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SF1]] | -0.47 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[ZNF385C]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CD99P1]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[KIDINS220]] | -0.44 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[IMPA1]] | -0.43 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[HS1BP3]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[PRSS16]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-27.6, -39.9); signed map (-47.6, -23.0). **Vector** length 82.9, 27.4% of its response variance represented; |z| ≥ 3 in 1,597 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +19.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +3.5 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +13.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.3 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:131,852,928-132,079,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP37, CRSP34, MED3; previously CRSP8 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2C8](https://www.uniprot.org/uniprotkb/Q6P2C8) (Mediator of RNA polymerase II transcription subunit 27):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9442](https://www.ncbi.nlm.nih.gov/gene/9442):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2377) · Entrez [9442](https://www.ncbi.nlm.nih.gov/gene/9442) · UniProt [Q6P2C8](https://www.uniprot.org/uniprotkb/Q6P2C8) · Ensembl [ENSG00000160563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160563)

## Data

Gene col 8356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8356); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8356]; `tensor/DDL_lfc|DDL_z.npy` [8356]; `embed/gene_vectors.npy` [8356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8356 or target_col == 8356). Every well: [[MED27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
