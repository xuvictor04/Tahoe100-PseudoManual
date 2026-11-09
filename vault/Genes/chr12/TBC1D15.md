---
symbol: "TBC1D15"
type: "gene"
col: 4292
ensembl_id: "ENSG00000121749"
name: "TBC1 domain family member 15"
location: "12q21.1"
module: 69
arm: "+"
pooled_cpm: 136.03
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TBC1D15

*TBC1 domain family member 15* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +17.1, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.386× (z -19.6, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.337× (z -11.7, q 3e-29, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RB1CC1]] (+0.79, fdr 7e-06), [[HBP1]] (+0.73, fdr 1e-05), [[SLU7]] (+0.73, fdr 1e-05); moves opposite to [[MICAL3]] (-0.50, fdr 3e-05), [[HEATR3]] (-0.50, fdr 4e-05), [[BOP1]] (-0.46, fdr 5e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +17.1 | 0e+00 | 38/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +14.7 | 0e+00 | 48/49 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +14.4 | 1e-44 | 44/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.03×** | +12.0 | 6e-31 | 43/48 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +11.6 | 4e-29 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +11.3 | 2e-27 | 46/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +11.1 | 2e-26 | 46/48 (HT-29, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +8.2 | 2e-14 | 37/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +8.0 | 1e-13 | 37/48 (C32, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.8 | 3e-13 | 33/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.7 | 1e-12 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.0 | 2e-10 | 32/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +6.0 | 1e-07 | 31/48 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.9 | 2e-07 | 30/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 3e-05 | 38/49 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.52×** | +4.5 | 2e-04 | 34/49 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 26/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.386×** | -19.6 | 0e+00 | 48/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.337×** | -11.7 | 3e-29 | 47/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.353×** | -11.2 | 7e-27 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.375×** | -10.6 | 6e-24 | 47/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.394×** | -10.0 | 1e-21 | 45/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.429×** | -9.1 | 7e-18 | 48/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.709×** | -6.8 | 8e-10 | 32/44 (HCT15, NCI-H1573, …) | rises with dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.556×** | -6.3 | 2e-08 | 42/47 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.656×** | -6.2 | 4e-08 | 38/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.751×** | -5.9 | 2e-07 | 27/49 (COLO 205, SNU-1, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.678×** | -5.7 | 6e-07 | 42/49 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.760×** | -5.3 | 5e-06 | 34/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.810×** | -4.3 | 7e-04 | 27/48 (LS 180, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 1e-03 | 30/48 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.847× | -3.4 | 0.026 | 18/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.035 | 13/49 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.856× | -3.2 | 0.051 | 19/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.058 | 17/49 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 16 (5 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +25.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -15.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.267× (z -10.1) |
| [[RKO (line)]] | wt | 152 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +17.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.402× (z -11.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 106 | 5 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.01× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -19.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.292× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 197 | 2 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.154× (z -23.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0775× (z -17.1) |
| [[HT-29 (line)]] | alt | 140 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.523× (z -8.7) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 271 | 3 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.62× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -16.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.221× (z -10.8) |
| [[COLO 205 (line)]] | alt | 161 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 85.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.403× (z -11.4) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 101 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.452× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 150 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -17.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.208× (z -11.6) |
| [[SNU-1 (line)]] | wt | 179 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -12.1) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 104 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -9.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 147 | 6 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.400× (z -12.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 88.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +20.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -10.4) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 131 | 4 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.04× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -13.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.249× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 148 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 132 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -19.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.274× (z -9.2) |
| [[SW48 (line)]] | wt | 154 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.87× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -17.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.172× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 111 | 3 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.95× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -15.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.249× (z -9.6) |
| [[LoVo (line)]] | wt | 192 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -11.8) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 130 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -9.3) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 94.2 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +8.8) | [[TAK-733 (drug)]] 5 µM 0.199× (z -10.7) |
| [[PANC-1 (line)]] | alt | 143 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.515× (z -8.9) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 147 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.438× (z -8.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 116 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -9.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.239× (z -8.8) |
| [[A498 (line)]] | wt | 129 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.344× (z -14.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.290× (z -8.8) |
| [[A549 (line)]] | wt | 119 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -11.6) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -17.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.237× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 71.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 96.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -10.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.220× (z -8.6) |
| [[SNU-423 (line)]] | alt | 186 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.05× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -9.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 150 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -9.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.210× (z -9.2) |
| [[A-427 (line)]] | wt | 139 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.95× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -9.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 162 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +16.0) | — |
| [[KATO III (line)]] | alt | 159 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.265× (z -12.8) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 106 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.96× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.283× (z -16.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.230× (z -9.9) |
| [[H4 (line)]] | wt | 172 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -9.3) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -10.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 131 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 177 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.99× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -14.1) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Everolimus (drug)]] 5 µM 0.104× (z -8.9) |
| [[C-33 A (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.416× (z -8.6) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -9.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.475× (z -9.6) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0341× (z -13.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RB1CC1]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 | STRING 491 |
| [[HBP1]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[SLU7]] | +0.73 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.69 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[ING4]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PAIP2]] | +0.68 | +0.38 / +0.79 | both halves | 7e-05 |  |
| [[JMY]] | +0.67 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[PDCD4]] | +0.66 | +0.38 / +0.77 | both halves | 7e-05 | **novel candidate** |
| [[KLHL24]] | +0.66 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[OTUD5]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.65 | +0.38 / +0.75 | both halves | 6e-05 |  |
| [[OSER1]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL3]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[HEATR3]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[BOP1]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[OTUD3]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[IDH3A]] | -0.46 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[BOLA3]] | -0.46 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ZBED4]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PDSS1]] | -0.46 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, -45.1); signed map (-14.5, 9.7). **Vector** length 130, 48.4% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.4 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.6 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.2 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.8 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -20.1 | -19.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -12.6 | -11.7 |
|  | [[EX229 (drug)]] 5 µM |  | -12.5 | -11.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -12.0 | -10.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -11.5 | -9.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -11.2 | -10.0 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,839,707-71,927,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12085, DKFZp761D0223 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC07](https://www.uniprot.org/uniprotkb/Q8TC07) (TBC1 domain family member 15):

> Acts as a GTPase activating protein for RAB7A. Does not act on RAB4, RAB5 or RAB6 (By similarity).

**Summary**, from NCBI Gene [64786](https://www.ncbi.nlm.nih.gov/gene/64786):

> This gene encodes a member of the Ras-like proteins in brain-GTPase activating protein superfamily that share a conserved Tre-2/Bub2/Cdc16 domain. The encoded protein interacts with Ras-like protein in brain 5A and may function as a regulator of intracellular trafficking. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:25694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25694) · Entrez [64786](https://www.ncbi.nlm.nih.gov/gene/64786) · UniProt [Q8TC07](https://www.uniprot.org/uniprotkb/Q8TC07) · Ensembl [ENSG00000121749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121749)

## Data

Gene col 4292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4292); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4292]; `tensor/DDL_lfc|DDL_z.npy` [4292]; `embed/gene_vectors.npy` [4292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4292 or target_col == 4292). Every well: [[TBC1D15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
