---
symbol: "BRD8"
type: "gene"
col: 3422
ensembl_id: "ENSG00000112983"
name: "bromodomain containing 8"
location: "5q31.2"
module: 22
arm: "+"
pooled_cpm: 74.67
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BRD8

*bromodomain containing 8* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +20.9, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +10.8, q 1e-24, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.529× (z -14.7, q 0e+00, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.705× (z -8.1, q 1e-13, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AURKA]] (+0.64, fdr 7e-06), [[HMGB2]] (+0.63, fdr 7e-06), [[RBM15]] (+0.59, fdr 2e-05); moves opposite to [[ST6GALNAC4]] (-0.55, fdr 5e-05), [[TMEM241]] (-0.54, fdr 4e-05), [[UCHL3]] (-0.52, fdr 6e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.89×** | +20.9 | 0e+00 | 42/48 (HS-578T, NCI-H2030, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.8 | 1e-24 | 36/49 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.51×** | +9.1 | 1e-17 | 36/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.47×** | +8.9 | 1e-16 | 37/48 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.92×** | +7.9 | 4e-13 | 37/47 (PANC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.40×** | +7.7 | 1e-12 | 31/48 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.39×** | +7.6 | 3e-12 | 33/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +7.4 | 7e-12 | 32/47 (NCI-H1573, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +7.1 | 8e-11 | 30/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.7 | 7e-07 | 25/48 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.25×** | +5.2 | 1e-05 | 24/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.17× | +5.1 | 2e-05 | 16/48 (C32, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.0 | 2e-05 | 18/48 (SNU-423, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.23×** | +4.7 | 1e-04 | 22/48 (KATO III, LoVo, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.15× | +4.6 | 2e-04 | 12/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.4 | 3e-04 | 22/48 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.21×** | +4.4 | 4e-04 | 18/48 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.006 | 15/48 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.009 | 14/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.009 | 12/49 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.017 | 12/49 (HCT15, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.031 | 11/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.032 | 10/47 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.035 | 19/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.037 | 12/48 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.13× | +2.8 | 0.073 | 9/48 (SNU-423, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.529×** | -14.7 | 0e+00 | 44/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.659×** | -9.3 | 5e-18 | 27/44 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.705×** | -8.1 | 1e-13 | 33/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.713×** | -7.8 | 9e-13 | 32/49 (SW 1271, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.706×** | -7.4 | 1e-11 | 29/45 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -7.3 | 3e-11 | 30/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | **0.607×** | -6.0 | 1e-07 | 28/48 (MIA PaCa-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -5.9 | 3e-07 | 29/48 (SW 1271, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.617×** | -5.8 | 3e-07 | 29/48 (AsPC-1, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.636×** | -5.5 | 3e-06 | 26/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.642×** | -5.4 | 4e-06 | 26/48 (SW1417, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.885× | -4.0 | 0.003 | 10/48 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.842× | -4.0 | 0.003 | 18/48 (HCT15, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.006 | 17/49 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.732×** | -3.7 | 0.007 | 11/48 (MIA PaCa-2, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.864× | -3.4 | 0.022 | 18/48 (A-427, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.022 | 16/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.041 | 10/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.869× | -3.0 | 0.070 | 12/48 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Tomivosertib (drug)]] 5 µM |  | **0.789×** | -2.9 | 0.098 | 9/48 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 74.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.65× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.478× (z -8.6) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 73.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +20.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -8.9) ⚠ toxic; transcription drop; position correction uncertain |
| [[KATO III (line)]] | alt | 65.1 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +16.3) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 99.4 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -10.4) ⚠ toxic; transcription drop; position correction uncertain |
| [[HEC-1-A (line)]] | alt | 82.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 109 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.8) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.7) ⚠ toxic; transcription drop; position correction uncertain |
| [[NCI-H2347 (line)]] | alt | 60.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.8) | — |
| [[RKO (line)]] | wt | 75.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +17.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -17.7) ⚠ toxic; transcription drop; position correction uncertain |
| [[SW1417 (line)]] | alt | 117 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -10.3) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 73.8 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0666× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 70.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.314× (z -12.3) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[J82 (line)]] | alt | 48.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.5) ⚠ toxic; transcription drop; position correction uncertain |
| [[NCI-H1573 (line)]] | alt | 50.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1792 (line)]] | alt | 52.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.9) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -9.8) ⚠ toxic; transcription drop; position correction uncertain |
| [[Panc 03.27 (line)]] | alt | 83.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 97.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0866× (z -23.7) ⚠ toxic; transcription drop; position correction uncertain |
| [[SK-MEL-2 (line)]] | alt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.9) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.103× (z -26.2) ⚠ toxic; transcription drop; position correction uncertain |
| [[SW 1271 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0756× (z -13.7) ⚠ toxic; transcription drop; position correction uncertain · without an alert: [[TAK-733 (drug)]] 5 µM 0.0434× (z -8.7) |
| [[SW480 (line)]] | alt | 93.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -11.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -9.6) ⚠ toxic; transcription drop; position correction uncertain |
| [[A498 (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.4) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A549 (line)]] | wt | 61.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HT-29 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.30× (z +8.6) ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 74.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LS 180 (line)]] | wt | 63.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -12.3) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 83.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H460 (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -9.8) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SNU-1 (line)]] | wt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.9) ⚠ toxic; transcription drop; position correction uncertain |
| [[A-172 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AURKA]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HMGB2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RBM15]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CCNB2]] | +0.58 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MAU2]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[EAPP]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CDC25C]] | +0.57 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[KNSTRN]] | +0.57 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.56 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[UBALD2]] | +0.56 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[CNTRL]] | +0.56 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RXRB]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.55 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[TMEM241]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[UCHL3]] | -0.52 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[DPM2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RSU1]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.0, -54.8); signed map (-51.4, -46.7). **Vector** length 142, 45.3% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of NIMA Kinases NEK9, NEK6, NEK7* (reactome, mean cos +0.51 to 4); *Golgi Cisternae Pericentriolar Stack Reorganization* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +8.6 | +20.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | +7.9 | +8.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +7.4 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.9 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -14.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.7 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | -6.2 | -6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,139,770-138,178,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMAP, p120 |
| Gene groups (HGNC) | Bromodomain containing; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0E9](https://www.uniprot.org/uniprotkb/Q9H0E9) (Bromodomain-containing protein 8):

> May act as a coactivator during transcriptional activation by hormone-activated nuclear receptors (NR). Isoform 2 stimulates transcriptional activation by AR/DHTR, ESR1/NR3A1, RXRA/NR2B1 and THRB/ERBA2. At least isoform 1 and isoform 2 are components of the NuA4 histone acetyltransferase (HAT) complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome - DNA interactions and …

**Summary**, from NCBI Gene [10902](https://www.ncbi.nlm.nih.gov/gene/10902):

> The protein encoded by this gene interacts with thyroid hormone receptor in a ligand-dependent manner and enhances thyroid hormone-dependent activation from thyroid response elements. This protein contains a bromodomain and is thought to be a nuclear receptor coactivator. Multiple alternatively spliced transcript variants that encode distinct isoforms have been identified. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:19874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19874) · Entrez [10902](https://www.ncbi.nlm.nih.gov/gene/10902) · UniProt [Q9H0E9](https://www.uniprot.org/uniprotkb/Q9H0E9) · Ensembl [ENSG00000112983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112983)

## Data

Gene col 3422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3422); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3422]; `tensor/DDL_lfc|DDL_z.npy` [3422]; `embed/gene_vectors.npy` [3422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3422 or target_col == 3422). Every well: [[BRD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
