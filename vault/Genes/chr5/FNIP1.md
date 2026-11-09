---
symbol: "FNIP1"
type: "gene"
col: 13284
ensembl_id: "ENSG00000217128"
name: "folliculin interacting protein 1"
location: "5q31.1"
module: 59
arm: "+"
pooled_cpm: 409.79
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# FNIP1

*folliculin interacting protein 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +24.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.335× (z -17.0, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.183×, A-427 0.177×, SNU-423 0.178×, MIA PaCa-2 0.188×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.134×, SNU-423 0.207×, Hs 766T 0.195×, HepG2/C3A 0.241×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.375×, SNU-423 0.378×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLCN]] (+0.69, fdr 7e-06), [[TSC1]] (+0.64, fdr 1e-05), [[RRAGC-DT]] (+0.62, fdr 7e-06); moves opposite to [[UBP1]] (-0.61, fdr 1e-05), [[CHUK]] (-0.59, fdr 1e-05), [[NUP93]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02154]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.93×** | +24.6 | 0e+00 | 47/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +13.3 | 5e-38 | 47/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +9.4 | 7e-19 | 48/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.6 | 1e-15 | 42/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +7.8 | 9e-13 | 46/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.5 | 6e-12 | 41/48 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-10 | 38/48 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +6.9 | 5e-10 | 39/49 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +5.0 | 4e-05 | 33/48 (NCI-H23, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 31/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 27/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.012 | 42/49 (J82, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.048 | 34/50 (J82, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.048 | 29/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.073 | 23/48 (J82, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13284.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.183×, A-427 0.177×, SNU-423 0.178×, MIA PaCa-2 0.188×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.134×, SNU-423 0.207×, Hs 766T 0.195×, HepG2/C3A 0.241×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.375×, SNU-423 0.378×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.335×** | -17.0 | 0e+00 | 44/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.351×** | -17.0 | 0e+00 | 47/49 (COLO 205, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.496×** | -10.5 | 1e-23 | 44/45 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -7.0 | 5e-10 | 41/47 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.770×** | -6.0 | 2e-07 | 34/49 (A549, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.738×** | -4.9 | 8e-05 | 37/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.756×** | -4.5 | 4e-04 | 36/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 413 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +33.6) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 441 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 465 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 310 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +31.1) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 493 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +24.1) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 429 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 407 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +24.8) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 432 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +27.3) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 452 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +28.4) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 384 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 760 | 1 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -20.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 364 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -20.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 667 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +27.9) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 625 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 406 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 377 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 373 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 266 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +24.2) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 750 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -19.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 494 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 362 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 201 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.2) | — |
| [[H4 (line)]] | wt | 611 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 442 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 410 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 407 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 442 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -21.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 350 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 404 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -15.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 341 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -17.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 488 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 294 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 638 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 403 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 421 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 333 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 215 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +36.2) | — |
| [[SW48 (line)]] | wt | 293 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 439 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 345 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 369 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 585 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 283 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 268 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 443 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 586 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLCN]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[TSC1]] | +0.64 | +0.69 / +0.57 | both halves | 1e-05 | STRING 610 |
| [[RRAGC-DT]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NEU1]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[RABGAP1]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[RRAGC]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 | pathway: Amino acids regulate mTORC1; STRING 969 |
| [[RNF103-CHMP3]] | +0.56 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MITD1]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TRPM7]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBP1]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[CHUK]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NUP93]] | -0.53 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[LOXL1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MFSD14B]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[FAR1]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[POMGNT2]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MTRR]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[KLHL2]] | -0.50 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[MCMBP]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[OLA1]] | -0.49 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[TRAPPC10]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02154]] | B | LINC02154 activity raises FNIP1's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 1.36× lower at baseline in the lines without LINC02154 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.4, 15.6); signed map (-1.5, -6.2). **Vector** length 116, 53.7% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.0 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +24.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.7 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.6 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.6 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | folliculin interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:131,641,714-131,797,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1961 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF40](https://www.uniprot.org/uniprotkb/Q8TF40) (Folliculin-interacting protein 1):

> Binding partner of the GTPase-activating protein FLCN: involved in the cellular response to amino acid availability by regulating the non-canonical mTORC1 signaling cascade controlling the MiT/TFE factors TFEB and TFE3. Required to promote FLCN recruitment to lysosomes and interaction with Rag GTPases, leading to activation of the non-canonical mTORC1 signaling. In low-amino acid conditions, component of the lysosomal folliculin complex (LFC) on the membrane of lysosomes, which inhibits the …

**Summary**, from NCBI Gene [96459](https://www.ncbi.nlm.nih.gov/gene/96459):

> This gene encodes a protein that binds to the tumor suppressor protein folliculin and to AMP-activated protein kinase (AMPK). The encoded protein participates in the regulation of cellular metabolism and nutrient sensing by modulating the AMPK and target of rapamycin signaling pathways. This gene has a closely related paralog that encodes a protein with similar binding activities. Both related proteins also associate with the molecular chaperone heat shock protein-90 (Hsp90) and negatively …

**Accessions** — [HGNC:29418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29418) · Entrez [96459](https://www.ncbi.nlm.nih.gov/gene/96459) · UniProt [Q8TF40](https://www.uniprot.org/uniprotkb/Q8TF40) · Ensembl [ENSG00000217128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000217128)

## Data

Gene col 13284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13284); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13284]; `tensor/DDL_lfc|DDL_z.npy` [13284]; `embed/gene_vectors.npy` [13284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13284 or target_col == 13284). Every well: [[FNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
