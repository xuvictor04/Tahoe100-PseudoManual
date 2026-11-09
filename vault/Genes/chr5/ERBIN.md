---
symbol: "ERBIN"
type: "gene"
col: 3411
ensembl_id: "ENSG00000112851"
name: "erbb2 interacting protein"
location: "5q12.3"
module: 143
arm: "+"
pooled_cpm: 506.76
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ERBIN

*erbb2 interacting protein* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.61× (z +13.7, q 4e-40, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.395× (z -27.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXP1]] (+0.63, fdr 1e-05), [[PTPRK]] (+0.60, fdr 2e-05), [[LATS2]] (+0.60, fdr 4e-05); moves opposite to [[PLXNB3]] (-0.56, fdr 4e-05), [[NOMO2]] (-0.56, fdr 1e-04), [[PRSS53]] (-0.54, fdr 4e-05).
> It is in [[Module 143]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +13.7 | 4e-40 | 40/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +12.3 | 4e-32 | 30/47 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +9.9 | 7e-21 | 35/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +8.4 | 7e-15 | 37/48 (SK-MEL-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +6.2 | 7e-08 | 27/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +6.2 | 7e-08 | 25/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.4 | 6e-06 | 36/47 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +5.4 | 6e-06 | 24/46 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 1e-04 | 21/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.6 | 0.018 | 15/47 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +3.5 | 0.026 | 7/47 (PANC-1, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.08× | +3.2 | 0.061 | 0/47 | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.11× | +3.2 | 0.068 | 12/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.080 | 16/47 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.395×** | -27.9 | 0e+00 | 47/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.397×** | -27.7 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.510×** | -20.2 | 0e+00 | 44/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.622×** | -14.3 | 6e-44 | 41/48 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.628×** | -13.4 | 6e-39 | 37/43 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.763×** | -11.4 | 3e-28 | 30/48 (A549, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.634×** | -11.3 | 1e-27 | 37/44 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.692×** | -10.6 | 1e-24 | 36/46 (NCI-H2030, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -9.7 | 3e-20 | 39/47 (SW1417, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -7.0 | 2e-10 | 30/47 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.811×** | -6.3 | 2e-08 | 27/47 (SW1417, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.612×** | -6.2 | 3e-08 | 39/47 (SW1417, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.803×** | -6.1 | 6e-08 | 27/47 (NCI-H2030, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.845× | -5.1 | 2e-05 | 22/48 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.840× | -5.0 | 2e-05 | 22/47 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.680×** | -4.9 | 4e-05 | 31/47 (SW1417, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.681×** | -4.8 | 4e-05 | 35/47 (RKO, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.692×** | -4.7 | 1e-04 | 38/47 (SW1417, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.862× | -4.4 | 3e-04 | 16/47 (NCI-H2030, H4, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.005 | 22/47 (SW1417, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.915× | -3.7 | 0.005 | 9/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.839× | -3.5 | 0.012 | 17/47 (LOX-IMVI, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.894× | -3.4 | 0.019 | 10/47 (NCI-H1573, J82, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.019 | 15/47 (LOX-IMVI, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.038 | 20/48 (RKO, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 340 | 10 (5 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.608× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 853 | 0 | 13 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -18.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 671 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -23.4) |
| [[SW480 (line)]] | alt | 538 | 2 | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.276× (z -26.3) |
| [[A-172 (line)]] | wt | 427 | 7 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +30.8) | [[Panobinostat (drug)]] 5 µM 0.515× (z -10.7) |
| [[A549 (line)]] | wt | 386 | 3 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 491 | 1 | 8 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 1.68× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -24.3) |
| [[MIA PaCa-2 (line)]] | alt | 484 | 4 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.315× (z -20.6) |
| [[PANC-1 (line)]] | alt | 557 | 2 | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.83× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.397× (z -23.2) |
| [[SW 900 (line)]] | alt | 489 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -14.1) |
| [[A498 (line)]] | wt | 415 | 5 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +29.8) | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -14.4) |
| [[C32 (line)]] | wt | 383 | 2 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.395× (z -14.9) |
| [[HT-29 (line)]] | alt | 630 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -23.1) |
| [[Panc 03.27 (line)]] | alt | 853 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -25.2) |
| [[RKO (line)]] | wt | 750 | 1 | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.66× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -20.7) |
| [[SNU-423 (line)]] | alt | 642 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +23.1) | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -18.8) |
| [[COLO 205 (line)]] | alt | 1,047 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -18.2) |
| [[Hs 766T (line)]] | wt | 311 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.295× (z -19.9) |
| [[J82 (line)]] | alt | 1,133 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -18.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.380× (z -10.5) |
| [[LS 180 (line)]] | wt | 468 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 385 | 1 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.23× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.340× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 324 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -20.8) |
| [[SW1417 (line)]] | alt | 486 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -26.9) |
| [[A-427 (line)]] | wt | 625 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.01× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.322× (z -21.1) |
| [[AsPC-1 (line)]] | alt | 768 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -23.4) |
| [[CFPAC-1 (line)]] | alt | 541 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -16.7) |
| [[HS-578T (line)]] | alt | 348 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +18.2) | — |
| [[hTERT-HPNE (line)]] | wt | 384 | 3 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.01× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.504× (z -10.5) |
| [[SNU-1 (line)]] | wt | 367 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.524× (z -10.3) |
| [[BT-474 (line)]] | alt | 347 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -21.9) |
| [[CHP-212 (line)]] | wt | 298 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.370× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 348 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -24.4) |
| [[NCI-H2347 (line)]] | alt | 1,017 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 334 | 3 | 2 | [[Harringtonine (drug)]] 5 µM 2.57× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 388 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 677 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -10.4) |
| [[H4 (line)]] | wt | 360 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 331 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -11.0) |
| [[LoVo (line)]] | wt | 503 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.531× (z -13.6) |
| [[SW48 (line)]] | wt | 311 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -15.1) |
| [[HOP62 (line)]] | alt | 185 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -14.9) |
| [[SHP-77 (line)]] | alt | 242 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.578× (z -9.6) |
| [[C-33 A (line)]] | alt | 244 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -11.0) |
| [[SW 1271 (line)]] | alt | 694 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -10.6) |
| [[HCT15 (line)]] | alt | 448 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.580× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 323 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -9.6) |
| [[SW 1088 (line)]] | alt | 515 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 594 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 457 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXP1]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LATS2]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[AMOTL2]] | +0.58 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[NIPBL]] | +0.55 | +0.36 / +0.56 | both halves | 9e-05 | STRING 535 |
| [[IGF2BP2]] | +0.54 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[ARHGEF28]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 | pathway: RHOA GTPase cycle |
| [[CDK6]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[NFAT5]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[HIVEP2]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[LACTB2]] | +0.53 | +0.32 / +0.31 | both halves | 2e-04 |  |
| [[ROCK2]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 | pathway: RHOA GTPase cycle; STRING 579 |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB3]] | -0.56 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NOMO2]] | -0.56 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PRSS53]] | -0.54 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[PMS2P3-1]] | -0.54 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[RINT1]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MSTO2P]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DPH7]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NPRL2]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[INTS11]] | -0.51 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[RNF216P1]] | -0.51 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ZNF70]] | -0.51 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[ACTR5]] | -0.50 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.9, 13.1); signed map (47.7, 14.8). **Vector** length 115, 41.2% of its response variance represented; |z| ≥ 3 in 1,540 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +13.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +4.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +12.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -6.6 | -10.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.7 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | erbb2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,883,128-66,082,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAP2; previously ERBB2IP |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 30 pathways, smallest: Drug resistance in ERBB2 KD mutants; Drug resistance in ERBB2 TMD/JMD mutants; Drug-mediated inhibition of ERBB2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RT1](https://www.uniprot.org/uniprotkb/Q96RT1) (Erbin):

> Acts as an adapter for the receptor ERBB2, in epithelia. By binding the unphosphorylated 'Tyr-1248' of receptor ERBB2, it may contribute to stabilize this unphosphorylated state. Inhibits NOD2-dependent NF-kappa-B signaling and pro-inflammatory cytokine secretion. Acts as a mediator of keratinocyte differentiation by sequestering SHOC2 away from ERK-activating RAS complexes.

**Summary**, from NCBI Gene [55914](https://www.ncbi.nlm.nih.gov/gene/55914):

> This gene is a member of the leucine-rich repeat and PDZ domain (LAP) family. The encoded protein contains 17 leucine-rich repeats and one PDZ domain. It binds to the unphosphorylated form of the ERBB2 protein and regulates ERBB2 function and localization. It has also been shown to affect the Ras signaling pathway by disrupting Ras-Raf interaction. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:15842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15842) · Entrez [55914](https://www.ncbi.nlm.nih.gov/gene/55914) · UniProt [Q96RT1](https://www.uniprot.org/uniprotkb/Q96RT1) · Ensembl [ENSG00000112851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112851)

## Data

Gene col 3411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3411); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3411]; `tensor/DDL_lfc|DDL_z.npy` [3411]; `embed/gene_vectors.npy` [3411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3411 or target_col == 3411). Every well: [[ERBIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERBIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
