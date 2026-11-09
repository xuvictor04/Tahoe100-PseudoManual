---
symbol: "BRAF"
type: "gene"
col: 8098
ensembl_id: "ENSG00000157764"
name: "B-Raf proto-oncogene, serine/threonine kinase"
location: "7q34"
module: 51
arm: "+"
pooled_cpm: 293.56
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# BRAF

*B-Raf proto-oncogene, serine/threonine kinase* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +31.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.394× (z -24.8, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.504× (z -18.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.69, fdr 7e-06), [[SCAF8]] (+0.69, fdr 1e-05), [[CUTALP]] (+0.68, fdr 7e-06); moves opposite to [[LPCAT1]] (-0.68, fdr 7e-06), [[RNF4]] (-0.63, fdr 1e-05), [[TBC1D24]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +31.2 | 0e+00 | 47/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +14.1 | 1e-42 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +13.5 | 2e-39 | 46/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +8.9 | 1e-16 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +8.6 | 1e-15 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +8.2 | 3e-14 | 44/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.8 | 6e-10 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.5 | 7e-09 | 28/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.049 | 23/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.394×** | -24.8 | 0e+00 | 49/49 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -23.1 | 0e+00 | 44/44 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.454×** | -19.1 | 0e+00 | 42/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -18.3 | 0e+00 | 48/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.514×** | -17.7 | 0e+00 | 48/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -15.7 | 0e+00 | 41/49 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.578×** | -14.6 | 0e+00 | 43/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.596×** | -13.8 | 1e-41 | 48/48 (HOP62, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.671×** | -10.2 | 8e-23 | 35/50 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -9.4 | 2e-19 | 43/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -8.4 | 3e-15 | 37/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -8.2 | 1e-14 | 38/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.765×** | -6.9 | 3e-10 | 31/48 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.783×** | -6.3 | 1e-08 | 32/47 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.855× | -5.9 | 1e-07 | 16/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -5.2 | 6e-06 | 13/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -3.5 | 0.013 | 13/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.049 | 20/48 (SW48, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.065 | 20/47 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.751×** | -3.0 | 0.076 | 16/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.896× | -2.9 | 0.078 | 12/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.756×** | -2.9 | 0.078 | 19/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.756×** | -2.9 | 0.078 | 19/49 (CHP-212, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.853× | -2.8 | 0.094 | 11/48 (AN3 CA, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 277 | 9 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +35.2) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -11.6) |
| [[HOP62 (line)]] | alt | 247 | 3 | 11 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.5) | [[Auranofin (drug)]] 5 µM 0.386× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 286 | 2 | 12 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -14.9) |
| [[C32 (line)]] | wt | 587 | 5 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -17.1) |
| [[SNU-423 (line)]] | alt | 255 | 3 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -16.6) |
| [[A-172 (line)]] | wt | 196 | 4 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +31.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -19.5) |
| [[HS-578T (line)]] | alt | 251 | 1 | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 385 | 3 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +17.9) | [[Auranofin (drug)]] 5 µM 0.344× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 364 | 4 (1 ⚠) | 8 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.32× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -28.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -19.0) |
| [[RKO (line)]] | wt | 439 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -14.1) |
| [[SW 900 (line)]] | alt | 402 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -13.8) |
| [[SW48 (line)]] | wt | 350 | 5 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 330 | 5 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 278 | 3 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +22.1) | [[Auranofin (drug)]] 5 µM 0.498× (z -13.9) |
| [[LoVo (line)]] | wt | 366 | 4 (1 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.557× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 319 | 1 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 266 | 3 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +24.2) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 246 | 2 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -12.6) |
| [[A549 (line)]] | wt | 294 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -18.8) |
| [[H4 (line)]] | wt | 318 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -11.7) |
| [[PANC-1 (line)]] | alt | 292 | 3 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +30.8) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 329 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.365× (z -15.7) |
| [[SW480 (line)]] | alt | 368 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -19.8) |
| [[BT-474 (line)]] | alt | 233 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.6) | [[Auranofin (drug)]] 5 µM 0.484× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 255 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.525× (z -11.8) |
| [[KATO III (line)]] | alt | 333 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -11.1) |
| [[LS 180 (line)]] | wt | 215 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 410 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -19.9) |
| [[SNU-1 (line)]] | wt | 319 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -27.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -11.2) |
| [[SW1417 (line)]] | alt | 331 | 2 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -13.9) |
| [[A498 (line)]] | wt | 266 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +25.8) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -18.5) |
| [[Hs 766T (line)]] | wt | 261 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.458× (z -12.3) |
| [[HT-29 (line)]] | alt | 241 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +25.2) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 201 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +22.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -12.6) |
| [[A-427 (line)]] | wt | 272 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.541× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 214 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 266 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -12.4) |
| [[AN3 CA (line)]] | alt | 396 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -9.9) |
| [[COLO 205 (line)]] | alt | 208 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 257 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 199 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +20.1) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.575× (z -9.5) |
| [[C-33 A (line)]] | alt | 302 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 280 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 220 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 241 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -11.1) |
| [[SW 1088 (line)]] | alt | 352 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 385 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 335 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.69 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[CUTALP]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[EPC2]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ING3]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HELQ]] | +0.67 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NFYC]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BPTF]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LARP7]] | +0.65 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[RELB]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[KMT5B]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.68 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RNF4]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.62 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.62 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RPA1]] | -0.60 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[INTS11]] | -0.59 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.58 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.3, 13.2); signed map (7.8, -17.7). **Vector** length 105, 42.1% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.1 | +14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +31.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | -0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | -0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -14.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.8 | -13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | B-Raf proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,719,327-140,924,929 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRAF1, BRAF-1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; RAF family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 37 pathways, smallest: Signalling to p38 via RIT and RIN; Negative feedback regulation of MAPK pathway; ARMS-mediated activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P15056](https://www.uniprot.org/uniprotkb/P15056) (Serine/threonine-protein kinase B-raf):

> Protein kinase involved in the transduction of mitogenic signals from the cell membrane to the nucleus (Probable). Phosphorylates MAP2K1, and thereby activates the MAP kinase signal transduction pathway. Phosphorylates PFKFB2. May play a role in the postsynaptic responses of hippocampal neurons.

**Summary**, from NCBI Gene [673](https://www.ncbi.nlm.nih.gov/gene/673):

> This gene encodes a protein belonging to the RAF family of serine/threonine protein kinases. This protein plays a role in regulating the MAP kinase/ERK signaling pathway, which affects cell division, differentiation, and secretion. Mutations in this gene, most commonly the V600E mutation, are the most frequently identified cancer-causing mutations in melanoma, and have been identified in various other cancers as well, including non-Hodgkin lymphoma, colorectal cancer, thyroid carcinoma, …

**Accessions** — [HGNC:1097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1097) · Entrez [673](https://www.ncbi.nlm.nih.gov/gene/673) · UniProt [P15056](https://www.uniprot.org/uniprotkb/P15056) · Ensembl [ENSG00000157764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157764)

## Data

Gene col 8098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8098); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8098]; `tensor/DDL_lfc|DDL_z.npy` [8098]; `embed/gene_vectors.npy` [8098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8098 or target_col == 8098). Every well: [[BRAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
