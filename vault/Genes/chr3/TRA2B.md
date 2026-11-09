---
symbol: "TRA2B"
type: "gene"
col: 5876
ensembl_id: "ENSG00000136527"
name: "transformer 2 beta homolog"
location: "3q27.2"
module: 109
arm: "+"
pooled_cpm: 195.22
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# TRA2B

*transformer 2 beta homolog* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.26× (z +36.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.555× (z -12.3, q 8e-32, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.750× (z -8.8, q 5e-16, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF2]] (+0.60, fdr 1e-05), [[SRSF7]] (+0.59, fdr 1e-05), [[EGR3]] (+0.58, fdr 1e-05); moves opposite to [[MFSD8]] (-0.52, fdr 2e-05), [[MTM1]] (-0.52, fdr 7e-06), [[SWT1]] (-0.51, fdr 5e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +36.3 | 0e+00 | 48/48 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +21.3 | 0e+00 | 48/48 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.65×** | +17.5 | 0e+00 | 48/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +16.2 | 0e+00 | 46/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +14.8 | 0e+00 | 41/48 (A-172, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.93×** | +14.3 | 2e-44 | 46/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.86×** | +13.5 | 8e-40 | 43/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.13×** | +13.0 | 1e-36 | 46/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +8.4 | 2e-15 | 37/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.38×** | +7.0 | 2e-10 | 36/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.4 | 9e-09 | 34/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.34×** | +6.1 | 4e-08 | 33/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.32×** | +5.6 | 8e-07 | 28/45 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 9e-07 | 33/48 (KATO III, A498, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.7 | 1e-04 | 27/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.004 | 23/49 (SW1417, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 1.18× | +3.4 | 0.018 | 16/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.0 | 0.074 | 9/48 (KATO III, HS-578T, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.080 | 8/48 (KATO III, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.3 | 8e-32 | 36/44 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -8.8 | 5e-16 | 32/49 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.670×** | -8.3 | 2e-14 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.724×** | -7.0 | 4e-10 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.732×** | -6.7 | 2e-09 | 28/49 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.744×** | -6.4 | 1e-08 | 38/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.740×** | -6.4 | 1e-08 | 39/50 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.770×** | -5.6 | 1e-06 | 36/48 (BT-474, A498, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -5.6 | 1e-06 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -5.6 | 1e-06 | 30/48 (H4, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.828×** | -5.5 | 2e-06 | 26/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.820×** | -5.2 | 8e-06 | 28/48 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.790×** | -5.1 | 2e-05 | 34/49 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.819×** | -5.1 | 2e-05 | 29/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.776×** | -5.1 | 2e-05 | 33/48 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.816×** | -4.7 | 8e-05 | 29/49 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.799×** | -4.7 | 1e-04 | 28/48 (NCI-H1573, SW480, …) | all doses, flat | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.675×** | -4.5 | 3e-04 | 33/50 (A-427, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.863× | -4.3 | 5e-04 | 15/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.835× | -3.9 | 0.003 | 22/47 (NCI-H460, AN3 CA, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 223 | 11 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +31.1) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.529× (z -9.0) |
| [[SW480 (line)]] | alt | 289 | 11 (5 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +28.0) | [[Trametinib (drug)]] 5 µM 0.599× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.586× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 121 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +23.7) | — |
| [[PANC-1 (line)]] | alt | 202 | 11 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.550× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 215 | 9 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +32.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 163 | 9 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +30.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 292 | 7 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +24.8) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -11.2) |
| [[A-427 (line)]] | wt | 356 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -17.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 153 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.6) | — |
| [[SW48 (line)]] | wt | 183 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.0) | — |
| [[BT-474 (line)]] | alt | 208 | 7 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 182 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +20.4) | — |
| [[HOP62 (line)]] | alt | 194 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +29.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 247 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +24.4) | — |
| [[Panc 03.27 (line)]] | alt | 253 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 127 | 6 | 0 | [[Auranofin (drug)]] 5 µM 5.39× (z +21.1) | — |
| [[H4 (line)]] | wt | 205 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +18.3) | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +23.4) | — |
| [[SK-MEL-2 (line)]] | alt | 223 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 165 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 149 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.9) | — |
| [[A549 (line)]] | wt | 107 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +22.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.8) |
| [[HS-578T (line)]] | alt | 163 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +31.4) | — |
| [[HT-29 (line)]] | alt | 171 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +22.8) | — |
| [[J82 (line)]] | alt | 261 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +21.3) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +22.0) | — |
| [[AsPC-1 (line)]] | alt | 189 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +17.0) | — |
| [[C32 (line)]] | wt | 188 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 194 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +21.3) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 185 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +18.3) | — |
| [[RPMI-7951 (line)]] | alt | 192 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +20.9) | — |
| [[SNU-1 (line)]] | wt | 195 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 275 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 288 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 130 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 90.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 263 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 208 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.9) | — |
| [[SHP-77 (line)]] | alt | 208 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +23.7) | — |
| [[C-33 A (line)]] | alt | 202 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF2]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 998 |
| [[SRSF7]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 995 |
| [[EGR3]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[EGR1]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SAPCD1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | +0.55 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[EGR2]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[IER2]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[SLC20A1]] | +0.52 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[NR4A1]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ASTL]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MTM1]] | -0.52 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[SWT1]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC24]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[BBS7]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NADSYN1]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DUSP22]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ANKIB1]] | -0.48 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ANXA4]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[STRIP1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TRA2B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C13orf46]] | B | C13orf46 activity lowers TRA2B's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without C13orf46 | 0.071 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[MYO15B]] | B | MYO15B activity raises TRA2B's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without MYO15B | 0.089 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, 6.7); signed map (6.2, 29.2). **Vector** length 107, 40.5% of its response variance represented; |z| ≥ 3 in 1,512 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +36.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | -0.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.4 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -6.2 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.1 | +14.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.0 | +7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | transformer 2 beta homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,914,558-185,938,103 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Htra2-beta, PPP1R156; previously SFRS10 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; RNA binding motif containing |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P62995](https://www.uniprot.org/uniprotkb/P62995) (Transformer-2 protein homolog beta):

> Sequence-specific RNA-binding protein which participates in the control of pre-mRNA splicing. Can either activate or suppress exon inclusion. Acts additively with RBMX to promote exon 7 inclusion of the survival motor neuron SMN2. Activates the splicing of MAPT/Tau exon 10. Alters pre-mRNA splicing patterns by antagonizing the effects of splicing regulators, like RBMX. Binds to the AG-rich SE2 domain in the SMN exon 7 RNA. Binds to pre-mRNA.

**Summary**, from NCBI Gene [6434](https://www.ncbi.nlm.nih.gov/gene/6434):

> This gene encodes a nuclear protein which functions as sequence-specific serine/arginine splicing factor which plays a role in mRNA processing, splicing patterns, and gene expression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:10781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10781) · Entrez [6434](https://www.ncbi.nlm.nih.gov/gene/6434) · UniProt [P62995](https://www.uniprot.org/uniprotkb/P62995) · Ensembl [ENSG00000136527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136527)

## Data

Gene col 5876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5876); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5876]; `tensor/DDL_lfc|DDL_z.npy` [5876]; `embed/gene_vectors.npy` [5876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5876 or target_col == 5876). Every well: [[TRA2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRA2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
