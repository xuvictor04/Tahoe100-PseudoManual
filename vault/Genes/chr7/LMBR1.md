---
symbol: "LMBR1"
type: "gene"
col: 2699
ensembl_id: "ENSG00000105983"
name: "limb development membrane protein 1"
location: "7q36.3"
module: 28
arm: "-"
pooled_cpm: 195.4
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LMBR1

*limb development membrane protein 1* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +18.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.515× (z -14.6, q 1e-45, down in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.365× (z -12.5, q 8e-34, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW7]] (+0.64, fdr 7e-06), [[TBC1D16]] (+0.63, fdr 1e-05), [[GAN]] (+0.61, fdr 8e-06); moves opposite to [[NDUFA5]] (-0.64, fdr 9e-06), [[CILK1]] (-0.64, fdr 1e-05), [[CDKN1B]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCAT7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +18.4 | 0e+00 | 46/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +13.2 | 4e-37 | 40/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +10.9 | 4e-25 | 40/48 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +7.0 | 4e-10 | 35/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.9 | 4e-10 | 32/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.4 | 1e-08 | 26/48 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.3 | 2e-08 | 35/48 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +5.1 | 2e-05 | 28/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.011 | 24/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.015 | 17/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.020 | 21/48 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.020 | 18/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.020 | 15/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.022 | 20/49 (HOP62, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.022 | 19/48 (SNU-1, SW480, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.029 | 17/48 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.515×** | -14.6 | 1e-45 | 42/45 (C-33 A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.6 | 2e-39 | 42/49 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -12.5 | 8e-34 | 48/49 (RKO, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -12.1 | 1e-31 | 36/44 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.669×** | -9.2 | 4e-18 | 34/48 (LS 180, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.706×** | -8.3 | 1e-14 | 36/48 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -7.6 | 3e-12 | 36/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.766×** | -6.4 | 1e-08 | 32/48 (HS-578T, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -5.9 | 3e-07 | 28/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.792×** | -5.6 | 1e-06 | 28/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.848× | -5.6 | 1e-06 | 18/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.788×** | -5.5 | 2e-06 | 29/47 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.734×** | -3.8 | 0.005 | 25/47 (SW48, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.861× | -3.6 | 0.014 | 17/48 (H4, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.855× | -3.5 | 0.020 | 23/47 (H4, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.889× | -3.3 | 0.037 | 13/48 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.051 | 18/49 (NCI-H1573, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.877× | -3.1 | 0.054 | 13/48 (SW 1088, NCI-H2347, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.880× | -2.9 | 0.096 | 10/49 (A498, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 245 | 3 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.544× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 147 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 173 | 7 (5 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.16× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.535× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 172 | 6 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -15.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 145 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -11.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.273× (z -8.6) |
| [[LS 180 (line)]] | wt | 218 | 1 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.341× (z -15.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.223× (z -11.5) |
| [[A-427 (line)]] | wt | 214 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.424× (z -13.0) |
| [[A498 (line)]] | wt | 241 | 2 (1 ⚠) | 5 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.7) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.72× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.546× (z -9.1) |
| [[SW1417 (line)]] | alt | 253 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 328 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.426× (z -8.7) |
| [[LoVo (line)]] | wt | 328 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.273× (z -10.9) |
| [[RKO (line)]] | wt | 320 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.139× (z -14.0) |
| [[A549 (line)]] | wt | 180 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 134 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -10.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 138 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 309 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -19.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 289 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.316× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 267 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 250 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 216 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.342× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 94.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.296× (z -9.1) |
| [[A-172 (line)]] | wt | 128 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.397× (z -12.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[CFPAC-1 (line)]] | alt | 93.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 98.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.40× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -14.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 188 | 2 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.49× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0803× (z -24.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 253 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 92.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +12.8) | — |
| [[J82 (line)]] | alt | 123 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.65× (z +13.8) | [[TAK-901 (drug)]] 5 µM 0.314× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 101 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 183 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 227 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0325× (z -40.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 129 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.7) | [[TAK-901 (drug)]] 5 µM 0.294× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 141 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -16.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 138 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +12.7) | — |
| [[SW48 (line)]] | wt | 277 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 141 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.448× (z -9.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2347 (line)]] | alt | 123 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 226 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW7]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TBC1D16]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[GAN]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ARHGAP8]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[KLHL29]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ATP11A]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CMTM8]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ESRRA]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FBRSL1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[DAP3]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[RANBP17]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[WRN]] | +0.56 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.64 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[CILK1]] | -0.64 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[GIN1]] | -0.60 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[KRT10-AS1]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZNF436]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SCRN3]] | -0.58 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[IFT74]] | -0.58 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ZNF44]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[AMACR]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[ACBD5]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCAT7]] | B | PCAT7 activity raises LMBR1's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without PCAT7 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.4, 2.3); signed map (-19.0, 43.4). **Vector** length 131, 45.9% of its response variance represented; |z| ≥ 3 in 1,491 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.5 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.2 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -12.5 | -12.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.3 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.0 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -7.5 | -6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.8 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | limb development membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:156,668,946-156,893,216 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACHP, FLJ11665, ZRS; previously C7orf2 |
| Gene groups (HGNC) | LMBR family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVP7](https://www.uniprot.org/uniprotkb/Q8WVP7) (Limb region 1 protein homolog):

> Putative membrane receptor.

**Summary**, from NCBI Gene [64327](https://www.ncbi.nlm.nih.gov/gene/64327):

> This gene encodes a member of the LMBR1-like membrane protein family. Another member of this protein family has been shown to be a lipocalin transmembrane receptor. A highly conserved, cis-acting regulatory module for the sonic hedgehog gene is located within an intron of this gene. Consequently, disruption of this genic region can alter sonic hedgehog expression and affect limb patterning, but it is not known if this gene functions directly in limb development. Mutations and chromosomal …

**Accessions** — [HGNC:13243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13243) · Entrez [64327](https://www.ncbi.nlm.nih.gov/gene/64327) · UniProt [Q8WVP7](https://www.uniprot.org/uniprotkb/Q8WVP7) · Ensembl [ENSG00000105983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105983)

## Data

Gene col 2699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2699); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2699]; `tensor/DDL_lfc|DDL_z.npy` [2699]; `embed/gene_vectors.npy` [2699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2699 or target_col == 2699). Every well: [[LMBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
