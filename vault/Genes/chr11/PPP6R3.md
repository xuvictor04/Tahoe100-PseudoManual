---
symbol: "PPP6R3"
type: "gene"
col: 3112
ensembl_id: "ENSG00000110075"
name: "protein phosphatase 6 regulatory subunit 3"
location: "11q13"
module: 52
arm: "-"
pooled_cpm: 344.56
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PPP6R3

*protein phosphatase 6 regulatory subunit 3* — 11q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +23.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.537× (z -13.0, q 1e-35, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.767× (z -7.9, q 6e-13, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (HEC-1-A 0.463×, A549 0.507×, LOX-IMVI 0.542×, C-33 A 0.574×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.200×, J82 0.289×, HEC-1-A 0.387×, KATO III 0.384×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.292×, A-427 0.305×, SW480 0.456×, J82 0.441×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED13L]] (+0.58, fdr 2e-05), [[COQ2]] (+0.56, fdr 6e-04), [[PUM2]] (+0.56, fdr 1e-05); moves opposite to [[RNF139-DT]] (-0.58, fdr 2e-04), [[EEF1AKMT3]] (-0.50, fdr 0.002, ⚠ one half only (not replicated)), [[ZNF841]] (-0.49, fdr 2e-04), [[TAF13]] (-0.48, fdr 1e-04).
> It sits in the **-** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +23.1 | 0e+00 | 48/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +18.8 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +14.8 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +13.5 | 1e-39 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +12.2 | 4e-32 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +11.0 | 2e-26 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +8.6 | 5e-16 | 45/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +8.1 | 3e-14 | 45/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.9 | 3e-10 | 42/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +6.2 | 3e-08 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +6.2 | 4e-08 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 2e-05 | 29/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.8 | 8e-05 | 31/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.018 | 17/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.025 | 19/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.064 | 10/48 (NCI-H1573, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (HEC-1-A 0.463×, A549 0.507×, LOX-IMVI 0.542×, C-33 A 0.574×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.200×, J82 0.289×, HEC-1-A 0.387×, KATO III 0.384×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.292×, A-427 0.305×, SW480 0.456×, J82 0.441×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -13.0 | 1e-35 | 48/49 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -12.1 | 2e-31 | 42/44 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.609×** | -9.6 | 2e-19 | 43/45 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -7.9 | 6e-13 | 33/49 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -6.2 | 8e-08 | 44/47 (SW1417, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -3.7 | 0.019 | 23/48 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.849× | -3.4 | 0.050 | 21/48 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.895× | -3.3 | 0.074 | 6/48 (A-172, A-427, …) | rises with dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.13 | 15/48 (Panc 03.27, SW48, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.866× | -3.0 | 0.15 | 10/47 (AsPC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 213 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +26.3) | — |
| [[SW480 (line)]] | alt | 398 | 10 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -14.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 426 | 9 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +23.8) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 752 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -25.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 297 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.547× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 269 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +23.4) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -14.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 328 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 287 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 324 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +20.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -17.8) |
| [[HT-29 (line)]] | alt | 415 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 375 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -20.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 427 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -14.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 415 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 676 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -17.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 328 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -12.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 489 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 293 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 308 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 312 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 316 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -13.9) |
| [[H4 (line)]] | wt | 289 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 236 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.546× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 219 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +16.9) | — |
| [[Panc 03.27 (line)]] | alt | 460 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 290 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 608 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -17.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 652 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 252 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 288 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 323 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 231 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 349 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 420 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 297 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +17.2) | — |
| [[A-172 (line)]] | wt | 216 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -9.7) |
| [[A498 (line)]] | wt | 172 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +25.0) | — |
| [[C32 (line)]] | wt | 260 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.8) | — |
| [[HepG2_C3A (line)]] | wt | 271 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -11.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 296 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 246 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.7) | — |
| [[SW 1271 (line)]] | alt | 471 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 272 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 367 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 311 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 358 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 162 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.6) | — |
| [[NCI-H2122 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 247 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13L]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[COQ2]] | +0.56 | +0.22 / +0.63 | both halves | 6e-04 |  |
| [[PUM2]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 | STRING 562 |
| [[PHIP]] | +0.53 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[SMCHD1]] | +0.51 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[SCAF8]] | +0.50 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[WAC]] | +0.50 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[NCOR1]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[STK3]] | +0.49 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[NUP98]] | +0.45 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[H2AZ2]] | +0.45 | +0.35 / +0.52 | both halves | 1e-04 | pathway: Chromosome Maintenance |
| [[CLASP2]] | +0.45 | +0.43 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF139-DT]] | -0.58 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[EEF1AKMT3]] | -0.50 | -0.13 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZNF841]] | -0.49 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[TAF13]] | -0.48 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GLUD1P3]] | -0.47 | -0.21 / -0.58 | both halves | 6e-04 |  |
| [[ZNF275]] | -0.46 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[ZNF778]] | -0.45 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[EAF1]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TMEM167A]] | -0.44 | -0.21 / -0.42 | both halves | 7e-04 |  |
| [[RABGEF1P3]] | -0.44 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZFC3H1]] | -0.44 | -0.10 / -0.51 | ⚠ one half (not replicated) | 0.003 |  |
| [[ZNF808]] | -0.43 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[ENTPD7]] | -0.43 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[KHDC1]] | -0.42 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[MTRF1L]] | -0.42 | -0.44 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.320). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-18.0, -46.6); signed map (7.0, -13.4). **Vector** length 71.5, 27.8% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +11.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | -0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.9 | -1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -3.7 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 6 regulatory subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13 — chr11:68,460,731-68,615,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAPLa, DKFZp781E2374, DKFZp781O2362, DKFZp781E17107, SAP190, SAPL, PP6R3, FLJ11058; previously C11orf23, SAPS3 |
| Gene groups (HGNC) | Protein phosphatase 6 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 11 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5H9R7](https://www.uniprot.org/uniprotkb/Q5H9R7) (Serine/threonine-protein phosphatase 6 regulatory subunit 3):

> Regulatory subunit of protein phosphatase 6 (PP6). May function as a scaffolding PP6 subunit. May have an important role in maintaining immune self-tolerance.

**Summary**, from NCBI Gene [55291](https://www.ncbi.nlm.nih.gov/gene/55291):

> Protein phosphatase regulatory subunits, such as SAPS3, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS3 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:1173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1173) · Entrez [55291](https://www.ncbi.nlm.nih.gov/gene/55291) · UniProt [Q5H9R7](https://www.uniprot.org/uniprotkb/Q5H9R7) · Ensembl [ENSG00000110075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110075)

## Data

Gene col 3112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3112); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3112]; `tensor/DDL_lfc|DDL_z.npy` [3112]; `embed/gene_vectors.npy` [3112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3112 or target_col == 3112). Every well: [[PPP6R3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP6R3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
