---
symbol: "GPATCH2L"
type: "gene"
col: 1605
ensembl_id: "ENSG00000089916"
name: "G-patch domain containing 2 like"
location: "14q24.3"
module: 101
arm: "+"
pooled_cpm: 227.07
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# GPATCH2L

*G-patch domain containing 2 like* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +27.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.657× (z -11.8, q 1e-29, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.816× (z -7.0, q 4e-10, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD5]] (+0.74, fdr 7e-06), [[SPRED3]] (+0.73, fdr 7e-06), [[ZNF432]] (+0.71, fdr 7e-06); moves opposite to [[KCTD3]] (-0.64, fdr 7e-06), [[EHMT2]] (-0.63, fdr 1e-05), [[HSF2]] (-0.63, fdr 8e-06).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TM4SF19]], [[TM4SF19-DYNLT2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +27.8 | 0e+00 | 48/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +19.4 | 0e+00 | 43/49 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +13.4 | 1e-38 | 41/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +13.0 | 3e-36 | 39/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +11.7 | 2e-29 | 46/49 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +9.8 | 7e-21 | 39/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +9.8 | 1e-20 | 39/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +9.4 | 5e-19 | 38/48 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.0 | 2e-17 | 34/48 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +8.8 | 5e-17 | 35/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +8.4 | 3e-15 | 35/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +8.1 | 3e-14 | 31/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +7.9 | 1e-13 | 41/48 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +7.2 | 2e-11 | 25/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +7.1 | 5e-11 | 30/50 (Panc 03.27, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.6 | 7e-07 | 35/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.8 | 4e-05 | 17/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +4.7 | 8e-05 | 34/48 (SNU-1, SHP-77, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -11.8 | 1e-29 | 39/49 (A549, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -10.1 | 1e-21 | 31/44 (NCI-H23, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -9.8 | 1e-20 | 34/45 (SNU-423, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.816×** | -7.0 | 4e-10 | 27/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.783×** | -6.6 | 4e-09 | 31/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.794×** | -6.3 | 4e-08 | 27/48 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.811×** | -5.9 | 3e-07 | 29/49 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.829×** | -5.7 | 7e-07 | 27/50 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.867× | -5.7 | 8e-07 | 14/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.849× | -5.3 | 6e-06 | 20/48 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.825×** | -5.2 | 1e-05 | 24/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.835× | -5.1 | 2e-05 | 23/48 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.875× | -5.0 | 2e-05 | 16/48 (MIA PaCa-2, A549, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.691×** | -4.9 | 5e-05 | 27/47 (A549, C32, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.842× | -4.9 | 5e-05 | 20/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.855× | -4.6 | 2e-04 | 17/49 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.002 | 28/49 (A549, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.892× | -3.9 | 0.003 | 12/49 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.839× | -3.7 | 0.006 | 19/48 (A549, A498, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 264 | 11 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +22.9) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 163 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +20.1) | — |
| [[COLO 205 (line)]] | alt | 175 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +20.4) | — |
| [[NCI-H2347 (line)]] | alt | 142 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +30.0) | — |
| [[SW48 (line)]] | wt | 256 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 229 | 9 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +15.7) | — |
| [[NCI-H1573 (line)]] | alt | 421 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.459× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 325 | 5 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 235 | 7 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.24× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.481× (z -8.7) |
| [[HT-29 (line)]] | alt | 114 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 243 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.570× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 178 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +33.2) | — |
| [[SNU-423 (line)]] | alt | 196 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 156 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.3) | — |
| [[A549 (line)]] | wt | 340 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -16.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 186 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +25.6) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.517× (z -9.5) |
| [[BT-474 (line)]] | alt | 208 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.6) | — |
| [[C32 (line)]] | wt | 262 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.8) | — |
| [[KATO III (line)]] | alt | 135 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 185 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 255 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.4) | [[Trametinib (drug)]] 0.5 µM 0.622× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 286 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +27.2) | [[Dinaciclib (drug)]] 0.5 µM 0.577× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 207 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +16.7) | — |
| [[SW1417 (line)]] | alt | 160 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +19.8) | — |
| [[A-172 (line)]] | wt | 160 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.6) | — |
| [[A-427 (line)]] | wt | 149 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 275 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +23.9) | [[Dinaciclib (drug)]] 0.5 µM 0.565× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 166 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +20.1) | — |
| [[J82 (line)]] | alt | 186 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -13.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 196 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +23.2) | — |
| [[CFPAC-1 (line)]] | alt | 270 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.567× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 188 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.6) | — |
| [[hTERT-HPNE (line)]] | wt | 411 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 259 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -16.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 178 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 245 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -13.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 379 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.2) | [[Radotinib (drug)]] 5 µM 0.632× (z -8.8) |
| [[CHP-212 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 367 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 282 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 335 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -15.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 402 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.2) | — |
| [[AN3 CA (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD5]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SPRED3]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LUCAT1]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SAP30BP]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[BLZF2P]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TUT7]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[STK10]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[EHMT2]] | -0.63 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[HSF2]] | -0.63 | -0.57 / -0.69 | both halves | 8e-06 |  |
| [[SORT1]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CXADR]] | -0.59 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.58 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[KDM1A]] | -0.58 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MPP7]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LRIG3]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.57 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ZNF592]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises GPATCH2L's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.32× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises GPATCH2L's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CLDN14-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[KCNMA1]] | B | KCNMA1 activity weakens GPATCH2L's drug response | lines that do not express KCNMA1 (26) vs lines expressing it (23) | the lines without KCNMA1 respond 1.04× as strongly (z diff -0.28); strongest at Auranofin 5 µM: 1.79x vs 1.41x (z diff -2.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; target measured in part of the lines; artifact flags |
| [[MYH15]] | B | MYH15 activity raises GPATCH2L's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without MYH15 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNMA1]] | B | KCNMA1 activity raises GPATCH2L's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without KCNMA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, -20.3); signed map (9.7, 14.2). **Vector** length 131, 48.6% of its response variance represented; |z| ≥ 3 in 1,670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +13.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +19.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.1 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +9.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +3.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.6 | -5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.2 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.6 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.5 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:76,151,916-76,254,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20689, FLJ10033; previously C14orf118 |
| Matched by | ensembl_id |

UniProt [Q9NWQ4](https://www.uniprot.org/uniprotkb/Q9NWQ4) carries no function annotation.

**Summary**, from NCBI Gene [55668](https://www.ncbi.nlm.nih.gov/gene/55668):

> Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20210) · Entrez [55668](https://www.ncbi.nlm.nih.gov/gene/55668) · UniProt [Q9NWQ4](https://www.uniprot.org/uniprotkb/Q9NWQ4) · Ensembl [ENSG00000089916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089916)

## Data

Gene col 1605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1605); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1605]; `tensor/DDL_lfc|DDL_z.npy` [1605]; `embed/gene_vectors.npy` [1605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1605 or target_col == 1605). Every well: [[GPATCH2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
