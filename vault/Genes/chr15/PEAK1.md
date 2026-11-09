---
symbol: "PEAK1"
type: "gene"
col: 10396
ensembl_id: "ENSG00000173517"
name: "pseudopodium enriched atypical kinase 1"
location: "15q24.3"
module: 107
arm: "+"
pooled_cpm: 203.38
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# PEAK1

*pseudopodium enriched atypical kinase 1* — 15q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +21.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.498× (z -15.8, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 0.314×, HT-29 0.284×, NCI-H1792 0.317×, CFPAC-1 0.327×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.188×, LS 180 0.261×, SW480 0.347×, CFPAC-1 0.358×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.287×, SW480 0.405×, NCI-H1573 0.347×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW480 0.560×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW480 0.548×); [[Trametinib (drug)]] 0.5 µM in 1 line (SW480 0.639×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L5]] (+0.65, fdr 7e-06), [[MAGI3]] (+0.59, fdr 1e-05), [[RAPGEF2]] (+0.58, fdr 1e-05); moves opposite to [[TOP3B]] (-0.62, fdr 1e-05), [[ZNF2]] (-0.60, fdr 2e-05), [[ZNF16]] (-0.60, fdr 1e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +21.7 | 0e+00 | 42/48 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +16.7 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +12.2 | 8e-32 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +11.5 | 2e-28 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +10.6 | 2e-24 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +10.2 | 2e-22 | 38/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.3 | 1e-14 | 33/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +7.3 | 2e-11 | 33/48 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +5.5 | 2e-06 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.5 | 2e-06 | 23/48 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +5.5 | 2e-06 | 26/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +5.1 | 2e-05 | 22/49 (A498, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.22×** | +4.4 | 4e-04 | 23/48 (BT-474, SW48, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +4.3 | 6e-04 | 26/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +4.1 | 0.002 | 23/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.008 | 24/48 (CFPAC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.016 | 22/49 (LS 180, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.026 | 20/48 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.083 | 13/48 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 0.314×, HT-29 0.284×, NCI-H1792 0.317×, CFPAC-1 0.327×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.188×, LS 180 0.261×, SW480 0.347×, CFPAC-1 0.358×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.287×, SW480 0.405×, NCI-H1573 0.347×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW480 0.560×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW480 0.548×); [[Trametinib (drug)]] 0.5 µM in 1 line (SW480 0.639×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -15.8 | 0e+00 | 47/49 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -14.7 | 0e+00 | 40/44 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -11.4 | 6e-28 | 34/45 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.724×** | -7.3 | 3e-11 | 34/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -4.1 | 0.005 | 24/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.902× | -3.4 | 0.071 | 8/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.752×** | -3.3 | 0.071 | 20/38 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.866× | -3.3 | 0.072 | 13/48 (COLO 205, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 297 | 1 | 10 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.560× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 109 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 218 | 7 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.544× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 275 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +19.8) | — |
| [[KATO III (line)]] | alt | 217 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -12.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 336 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 144 | 4 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -14.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 157 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 466 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.551× (z -8.6) |
| [[SNU-1 (line)]] | wt | 171 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 137 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 254 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -15.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 163 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 133 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.9) | — |
| [[A498 (line)]] | wt | 87.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +28.2) | — |
| [[A549 (line)]] | wt | 294 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -15.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 128 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 166 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.485× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 267 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 144 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +21.2) | — |
| [[NCI-H1573 (line)]] | alt | 138 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -22.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 105 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 303 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -15.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 130 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 168 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 216 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 95.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 297 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 209 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 214 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.7) | — |
| [[LOX-IMVI (line)]] | wt | 324 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 321 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -16.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 334 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 165 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -11.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 123 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 205 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -19.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 168 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 324 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -13.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 277 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.4) | — |
| [[SK-MEL-2 (line)]] | alt | 276 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 292 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +9.5) | — |
| [[SW48 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*20 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L5]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MAGI3]] | +0.59 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[RAPGEF2]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ARL15]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R13B]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[KLF12]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MYO1D]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[ABI1]] | +0.52 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[DENND4A]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SERINC5]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TLE4]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TRIM36]] | +0.51 | +0.38 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*80 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3B]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ZNF2]] | -0.60 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[ZNF16]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[ZSCAN25]] | -0.58 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SF3A3]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[DDX55]] | -0.57 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[DNAAF5]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FASTKD3]] | -0.56 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[RNF25]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[SF3A2]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GTF3C2]] | -0.56 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[MTERF4]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction -0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-51.1, 7.9); signed map (-15.3, 28.6). **Vector** length 95.8, 30.7% of its response variance represented; |z| ≥ 3 in 1,429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +5.7 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -10.3 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.7 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.9 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | pseudopodium enriched atypical kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3 — chr15:77,100,656-77,420,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2002, sgk269 |
| Gene groups (HGNC) | Pseudokinases; PEAK pseudokinase family |
| Reactome | 5 pathways, smallest: RHOV GTPase cycle; RHOU GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H792](https://www.uniprot.org/uniprotkb/Q9H792) (Inactive tyrosine-protein kinase PEAK1):

> Probable catalytically inactive kinase. Scaffolding protein that regulates the cytoskeleton to control cell spreading and migration by modulating focal adhesion dynamics. Acts as a scaffold for mediating EGFR signaling.

**Summary**, from NCBI Gene [79834](https://www.ncbi.nlm.nih.gov/gene/79834):

> This gene encodes a non-receptor tyrosine kinase that is a member of the new kinase family three (NFK3) family. In migrating cells, the encoded protein is associated with the actin cytoskeleton and focal adhesions and promotes developing focal adhesion elongation. This protein may play a role in the regulation of cell migration, proliferation and cancer metastasis. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:29431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29431) · Entrez [79834](https://www.ncbi.nlm.nih.gov/gene/79834) · UniProt [Q9H792](https://www.uniprot.org/uniprotkb/Q9H792) · Ensembl [ENSG00000173517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173517)

## Data

Gene col 10396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10396); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10396]; `tensor/DDL_lfc|DDL_z.npy` [10396]; `embed/gene_vectors.npy` [10396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10396 or target_col == 10396). Every well: [[PEAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
