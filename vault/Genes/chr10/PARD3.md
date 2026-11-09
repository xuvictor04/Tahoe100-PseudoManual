---
symbol: "PARD3"
type: "gene"
col: 7292
ensembl_id: "ENSG00000148498"
name: "par-3 family cell polarity regulator"
location: "10p11.22-p11.21"
module: 222
arm: "+"
pooled_cpm: 583.66
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# PARD3

*par-3 family cell polarity regulator* — 10p11.22-p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +10.1, q 2e-21, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.395× (z -23.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RICTOR]] (+0.54, fdr 1e-05), [[RAPGEF2]] (+0.53, fdr 2e-05), [[STK3]] (+0.53, fdr 2e-05); moves opposite to [[COPG1]] (-0.56, fdr 3e-04), [[ZNF550]] (-0.51, fdr 6e-05), [[ZNF17]] (-0.51, fdr 7e-05).
> It is in [[Module 222]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +10.1 | 2e-21 | 37/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +10.1 | 2e-21 | 32/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.8 | 2e-16 | 40/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +8.6 | 1e-15 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +7.1 | 1e-10 | 25/46 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.004 | 29/47 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.011 | 19/47 (RPMI-7951, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.025 | 19/46 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.4 | 0.036 | 18/48 (J82, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.041 | 27/47 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.2 | 0.081 | 0/47 | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.083 | 15/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.0 | 0.11 | 16/47 (CFPAC-1, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.395×** | -23.3 | 0e+00 | 46/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -23.1 | 0e+00 | 46/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.431×** | -20.3 | 0e+00 | 46/46 (CFPAC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -20.1 | 0e+00 | 42/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.480×** | -17.7 | 0e+00 | 40/43 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.499×** | -17.5 | 0e+00 | 44/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.516×** | -16.6 | 0e+00 | 44/47 (A549, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.610×** | -11.5 | 1e-28 | 36/44 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -10.7 | 1e-24 | 43/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -8.3 | 7e-15 | 36/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.720×** | -8.2 | 1e-14 | 40/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.567×** | -7.5 | 4e-12 | 46/47 (A-172, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.738×** | -7.3 | 1e-11 | 33/49 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -7.0 | 1e-10 | 35/47 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.647×** | -5.7 | 4e-07 | 42/47 (MIA PaCa-2, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.660×** | -5.5 | 2e-06 | 42/47 (A-172, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.664×** | -5.4 | 2e-06 | 38/47 (RPMI-7951, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.675×** | -5.2 | 8e-06 | 33/47 (A549, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.692×** | -4.8 | 4e-05 | 32/46 (NCI-H23, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -4.3 | 4e-04 | 23/47 (C-33 A, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.726×** | -4.2 | 6e-04 | 30/48 (HepG2/C3A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.858× | -3.8 | 0.003 | 18/48 (SNU-423, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.850× | -3.8 | 0.004 | 14/46 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 339 | 4 (1 ⚠) | 11 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.313× (z -25.8) |
| [[A549 (line)]] | wt | 1,017 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -35.3) |
| [[NCI-H460 (line)]] | wt | 463 | 7 (4 ⚠) | 6 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.14× (z +13.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.89× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -17.6) |
| [[PANC-1 (line)]] | alt | 315 | 3 (1 ⚠) | 10 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -24.6) |
| [[SW1417 (line)]] | alt | 500 | 3 | 10 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -21.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 1,618 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -25.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -20.8) |
| [[HT-29 (line)]] | alt | 516 | 2 (1 ⚠) | 10 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.331× (z -19.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 790 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 491 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -30.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.236× (z -23.8) |
| [[NCI-H2347 (line)]] | alt | 775 | 2 | 10 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -23.6) |
| [[MIA PaCa-2 (line)]] | alt | 468 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -26.7) |
| [[NCI-H1792 (line)]] | alt | 801 | 5 (2 ⚠) | 6 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.25× (z +11.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 1,416 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -22.1) |
| [[SNU-423 (line)]] | alt | 432 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -18.8) |
| [[SW48 (line)]] | wt | 654 | 3 (1 ⚠) | 8 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.37× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.327× (z -14.1) |
| [[BT-474 (line)]] | alt | 549 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -22.0) |
| [[Panc 03.27 (line)]] | alt | 570 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -20.2) |
| [[A-172 (line)]] | wt | 441 | 2 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.456× (z -13.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -13.7) |
| [[C-33 A (line)]] | alt | 599 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 759 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -19.8) |
| [[HepG2_C3A (line)]] | wt | 987 | 2 | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -16.5) |
| [[LoVo (line)]] | wt | 644 | 1 (1 ⚠) | 8 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.90× (z +11.3) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.262× (z -24.4) |
| [[NCI-H23 (line)]] | alt | 488 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -26.3) |
| [[SW 900 (line)]] | alt | 452 | 5 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -13.2) |
| [[A-427 (line)]] | wt | 500 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -20.2) |
| [[A498 (line)]] | wt | 569 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 1,267 | 1 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.288× (z -17.1) |
| [[COLO 205 (line)]] | alt | 357 | 3 (2 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +10.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.384× (z -13.1) |
| [[KATO III (line)]] | alt | 447 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -21.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -17.2) |
| [[LS 180 (line)]] | wt | 632 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -17.6) |
| [[H4 (line)]] | wt | 279 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 329 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -14.4) |
| [[HS-578T (line)]] | alt | 378 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -17.8) |
| [[J82 (line)]] | alt | 487 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -16.1) |
| [[RKO (line)]] | wt | 991 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.207× (z -24.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -17.7) |
| [[SNU-1 (line)]] | wt | 707 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -14.2) |
| [[HCT15 (line)]] | alt | 610 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.8) |
| [[SHP-77 (line)]] | alt | 421 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.526× (z -10.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 642 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.9) |
| [[C32 (line)]] | wt | 200 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.83× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.547× (z -8.6) |
| [[CHP-212 (line)]] | wt | 433 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.431× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 361 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.90× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -11.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 237 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -9.5) |
| [[SW 1271 (line)]] | alt | 509 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 284 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.514× (z -8.5) ⚠ toxic |
| [[NCI-H2122 (line)]] | alt | 699 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 543 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 297 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RICTOR]] | +0.54 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RAPGEF2]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 | same gene group |
| [[STK3]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MED13L]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[TBL1X]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DENND5B]] | +0.53 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[PPM1L]] | +0.52 | +0.29 / +0.35 | both halves | 3e-04 |  |
| [[MAGI1]] | +0.52 | +0.43 / +0.51 | both halves | 4e-05 | same gene group; STRING 945 |
| [[STAU2]] | +0.51 | +0.32 / +0.34 | both halves | 2e-04 |  |
| [[ZFAND6]] | +0.51 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[PTK2]] | +0.51 | +0.61 / +0.50 | both halves | 1e-05 | same gene group; pathway: Cell-Cell communication |
| [[PLEKHA5]] | +0.51 | +0.53 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG1]] | -0.56 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[ZNF550]] | -0.51 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ZNF17]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[PLXNB3]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[FAM220A]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RARS1]] | -0.50 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[KRBOX4]] | -0.49 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[PRPF3]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[GMPPA]] | -0.48 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ZNF526]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[TRMU]] | -0.48 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[TBC1D8B]] | -0.47 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.0, 15.2); signed map (4.4, 11.6). **Vector** length 108, 43.1% of its response variance represented; |z| ≥ 3 in 1,849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.2 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.6 | +1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.9 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -20.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.6 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -7.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.5 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | par-3 family cell polarity regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22-p11.21 — chr10:34,109,560-34,815,325 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PARD-3, PAR-3, PAR3, PARD3A, Bazooka, Baz, ASIP, PPP1R118 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; PDZ domain containing; Par-3 family cell polarity regulators |
| Reactome | 7 pathways, smallest: TGF-beta receptor signaling in EMT (epithelial to mesenchymal transition); Tight junction interactions; Signaling by TGF-beta Receptor Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEW0](https://www.uniprot.org/uniprotkb/Q8TEW0) (Partitioning defective 3 homolog):

> Adapter protein involved in asymmetrical cell division and cell polarization processes. Seems to play a central role in the formation of epithelial tight junctions. Targets the phosphatase PTEN to cell junctions (By similarity). Involved in Schwann cell peripheral myelination (By similarity). Association with PARD6B may prevent the interaction of PARD3 with F11R/JAM1, thereby preventing tight junction assembly (By similarity). The PARD6-PARD3 complex links GTP-bound Rho small GTPases to …

**Summary**, from NCBI Gene [56288](https://www.ncbi.nlm.nih.gov/gene/56288):

> This gene encodes a member of the PARD protein family. PARD family members interact with other PARD family members and other proteins; they affect asymmetrical cell division and direct polarized cell growth. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:16051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16051) · Entrez [56288](https://www.ncbi.nlm.nih.gov/gene/56288) · UniProt [Q8TEW0](https://www.uniprot.org/uniprotkb/Q8TEW0) · Ensembl [ENSG00000148498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148498)

## Data

Gene col 7292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7292); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7292]; `tensor/DDL_lfc|DDL_z.npy` [7292]; `embed/gene_vectors.npy` [7292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7292 or target_col == 7292). Every well: [[PARD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
