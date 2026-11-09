---
symbol: "MED13L"
type: "gene"
col: 4395
ensembl_id: "ENSG00000123066"
name: "mediator complex subunit 13L"
location: "12q24.21"
module: 52
arm: "-"
pooled_cpm: 424.21
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# MED13L

*mediator complex subunit 13L* — 12q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +16.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.427× (z -18.9, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.727× (z -10.4, q 2e-23, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KAT6A]] (+0.69, fdr 8e-06), [[SPPL3]] (+0.59, fdr 1e-05), [[SCAF8]] (+0.59, fdr 1e-05); moves opposite to [[PMM2]] (-0.57, fdr 2e-05), [[DHDDS]] (-0.57, fdr 7e-05), [[TRMT44]] (-0.56, fdr 2e-05).
> It sits in the **-** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +16.3 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +11.9 | 2e-30 | 41/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +10.9 | 2e-25 | 43/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +10.6 | 3e-24 | 30/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +10.4 | 3e-23 | 46/49 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +10.0 | 1e-21 | 41/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +8.6 | 5e-16 | 35/48 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +7.7 | 1e-12 | 42/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.3 | 2e-08 | 34/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.14× | +4.4 | 6e-04 | 2/48 (J82, CHP-212) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.20× | +4.1 | 0.002 | 18/48 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.041 | 21/49 (RKO, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.1 | 0.072 | 7/48 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.073 | 23/50 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.073 | 17/48 (AsPC-1, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.075 | 13/49 (A498, SHP-77, …) | top dose only |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.079 | 5/48 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.085 | 2/48 (J82, HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.427×** | -18.9 | 0e+00 | 42/44 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.471×** | -17.4 | 0e+00 | 45/49 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.518×** | -14.1 | 9e-43 | 36/45 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -11.8 | 4e-30 | 42/47 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -10.4 | 2e-23 | 37/49 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.723×** | -7.5 | 6e-12 | 34/48 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -7.1 | 1e-10 | 40/48 (SW48, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.746×** | -6.8 | 9e-10 | 37/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.769×** | -6.1 | 8e-08 | 30/48 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.785×** | -5.6 | 1e-06 | 26/48 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.630×** | -5.4 | 4e-06 | 39/48 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.647×** | -5.0 | 2e-05 | 39/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.656×** | -4.9 | 4e-05 | 35/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -4.7 | 1e-04 | 28/48 (SW480, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.827×** | -4.4 | 4e-04 | 24/48 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.006 | 24/48 (SW48, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.737×** | -3.5 | 0.011 | 28/47 (HepG2/C3A, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.904× | -3.3 | 0.026 | 3/49 (A-172, SW 1088, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.037 | 21/48 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 400 | 6 (1 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +17.2) | [[Auranofin (drug)]] 5 µM 0.530× (z -12.6) |
| [[C32 (line)]] | wt | 434 | 10 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.12× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -15.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 448 | 6 (1 ⚠) | 7 (6 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.11× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -21.7) |
| [[LOX-IMVI (line)]] | wt | 721 | 3 | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 300 | 11 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.99× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 771 | 2 | 10 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -16.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -14.0) |
| [[HT-29 (line)]] | alt | 369 | 5 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 481 | 5 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -15.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 610 | 4 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.94× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.437× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 404 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 275 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.8) |
| [[PANC-1 (line)]] | alt | 610 | 5 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 634 | 2 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -10.3) |
| [[LoVo (line)]] | wt | 621 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 369 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -8.5) |
| [[A-427 (line)]] | wt | 719 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.66× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -17.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 319 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -16.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 486 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -21.2) |
| [[CFPAC-1 (line)]] | alt | 315 | 2 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 414 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -11.4) |
| [[J82 (line)]] | alt | 389 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 319 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -16.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 583 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -11.8) |
| [[SW 900 (line)]] | alt | 202 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.00× (z +16.2) | — |
| [[A498 (line)]] | wt | 124 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +19.5) | — |
| [[AN3 CA (line)]] | alt | 1,004 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.5) |
| [[H4 (line)]] | wt | 285 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.70× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 666 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -17.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 207 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.95× (z +14.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -12.6) ⚠ toxic |
| [[RKO (line)]] | wt | 398 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -15.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 456 | 1 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.07× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 401 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -11.7) |
| [[SNU-1 (line)]] | wt | 402 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -16.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 444 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.0) |
| [[COLO 205 (line)]] | alt | 374 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +16.2) | — |
| [[Hs 766T (line)]] | wt | 283 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 606 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 478 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -9.0) |
| [[C-33 A (line)]] | alt | 382 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 289 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 426 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 749 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.2) |
| [[A-172 (line)]] | wt | 317 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.8) |
| [[NCI-H661 (line)]] | alt | 715 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 393 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 532 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 500 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 328 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6A]] | +0.69 | +0.58 / +0.67 | both halves | 8e-06 | STRING 529 |
| [[SPPL3]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MTMR3]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 | same gene group |
| [[PPP6R3]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ARID1B]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 | STRING 572 |
| [[PUM2]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[WAC]] | +0.55 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TCF12]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[YAP1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ZFHX3]] | +0.54 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[KDM6A]] | +0.54 | +0.35 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMM2]] | -0.57 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[DHDDS]] | -0.57 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[TRMT44]] | -0.56 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TAF13]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[BET1L]] | -0.54 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[RABGEF1P3]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NANS]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PGM3]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[SLC30A6]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZNF587]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF215]] | -0.53 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[SGSM3]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.8, -29.0); signed map (7.4, -13.4). **Vector** length 111, 44.0% of its response variance represented; |z| ≥ 3 in 1,588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | -17.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | -18.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.3 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 13L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.21 — chr12:115,957,905-116,277,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1025, TRAP240L; previously THRAP2 |
| Gene groups (HGNC) | Mediator complex; MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71F56](https://www.uniprot.org/uniprotkb/Q71F56) (Mediator of RNA polymerase II transcription subunit 13-like):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [23389](https://www.ncbi.nlm.nih.gov/gene/23389):

> The protein encoded by this gene is a subunit of the Mediator complex, a large complex of proteins that functions as a transcriptional coactivator for most RNA polymerase II-transcribed genes. The encoded protein is involved in early development of the heart and brain. Defects in this gene are a cause of transposition of the great arteries, dextro-looped (DTGA).[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:22962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22962) · Entrez [23389](https://www.ncbi.nlm.nih.gov/gene/23389) · UniProt [Q71F56](https://www.uniprot.org/uniprotkb/Q71F56) · Ensembl [ENSG00000123066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123066)

## Data

Gene col 4395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4395); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4395]; `tensor/DDL_lfc|DDL_z.npy` [4395]; `embed/gene_vectors.npy` [4395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4395 or target_col == 4395). Every well: [[MED13L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED13L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
