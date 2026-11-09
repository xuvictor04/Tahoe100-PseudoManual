---
symbol: "RCAN3"
type: "gene"
col: 3931
ensembl_id: "ENSG00000117602"
name: "regulator of calcineurin 3"
location: "1p36.11"
module: 188
arm: "+"
pooled_cpm: 48.85
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# RCAN3

*regulator of calcineurin 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.24× (z +24.6, q 0e+00, up in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (drug)]] 5 µM: 1.26× (z +5.0, q 7e-05, up in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HOP62 7.70×, HS-578T 7.23×, A498 8.43×, SW 900 15.2×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HOP62 5.75×, SW 900 17.2×, HS-578T 6.64×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 5.40×, SW 900 14.9×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 3.14×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -25.0, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A13]] (+0.58, fdr 1e-05), [[CIZ1]] (+0.57, fdr 1e-05), [[CDA]] (+0.57, fdr 1e-05); moves opposite to [[INTS5]] (-0.54, fdr 2e-05), [[EXOSC4]] (-0.50, fdr 2e-04), [[SNRPB]] (-0.50, fdr 3e-05).
> It is in [[Module 188]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3931.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HOP62 7.70×, HS-578T 7.23×, A498 8.43×, SW 900 15.2×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HOP62 5.75×, SW 900 17.2×, HS-578T 6.64×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 5.40×, SW 900 14.9×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 3.14×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +24.6 | 0e+00 | 36/40 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +20.4 | 0e+00 | 41/44 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +16.0 | 0e+00 | 35/41 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +6.0 | 3e-07 | 24/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +5.0 | 7e-05 | 17/46 (HOP62, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.9 | 7e-05 | 19/46 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +4.2 | 0.002 | 9/46 (A-172, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.2 | 0.002 | 12/46 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.9 | 0.006 | 13/34 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.016 | 15/45 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.5 | 0.022 | 16/46 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.023 | 9/46 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.026 | 18/43 (NCI-H2347, NCI-H1573, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.032 | 13/45 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.065 | 9/46 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -25.0 | 0e+00 | 37/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.399×** | -19.1 | 0e+00 | 34/45 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -18.9 | 0e+00 | 39/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -13.4 | 5e-39 | 37/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.8 | 3e-35 | 36/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -11.4 | 4e-28 | 29/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.600×** | -11.1 | 1e-26 | 34/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.615×** | -10.5 | 4e-24 | 26/46 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.627×** | -10.1 | 3e-22 | 29/46 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -8.4 | 2e-15 | 31/46 (HOP62, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -7.5 | 3e-12 | 27/45 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -6.8 | 4e-10 | 26/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.717×** | -6.8 | 4e-10 | 25/45 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -6.7 | 1e-09 | 29/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.758×** | -5.8 | 3e-07 | 20/44 (BT-474, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.760×** | -5.6 | 7e-07 | 25/46 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -5.4 | 2e-06 | 21/46 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.012 | 15/46 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.013 | 11/45 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.023 | 18/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 55.9 | 3 (3 ⚠) | 12 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.23× (z +18.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.158× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 66.1 | 3 (3 ⚠) | 9 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.01× (z +17.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -20.0) |
| [[HOP62 (line)]] | alt | 75.6 | 3 (3 ⚠) | 9 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.70× (z +22.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 50.7 | 1 (1 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -19.1) |
| [[A-172 (line)]] | wt | 51.1 | 1 (1 ⚠) | 9 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -20.2) |
| [[PANC-1 (line)]] | alt | 41.2 | 1 (1 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.79× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -22.2) |
| [[SW480 (line)]] | alt | 32.8 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -13.2) |
| [[A549 (line)]] | wt | 61.7 | 1 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 70.8 | 1 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -26.2) |
| [[LoVo (line)]] | wt | 35.2 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.59× (z +15.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.2) |
| [[HT-29 (line)]] | alt | 54.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.8) |
| [[SW48 (line)]] | wt | 44.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 4.45× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -13.4) |
| [[BT-474 (line)]] | alt | 63.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.26× (z +11.8) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.295× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 71.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.67× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0939× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 99.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +16.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.2) |
| [[SW 900 (line)]] | alt | 66.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.2× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.3) | — |
| [[A-427 (line)]] | wt | 39.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.5) |
| [[A498 (line)]] | wt | 37.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.43× (z +18.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 51.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.71× (z +17.4) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.7) |
| [[H4 (line)]] | wt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 25.8× (z +18.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 80.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.8× (z +18.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 61.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -23.7) |
| [[NCI-H1792 (line)]] | alt | 39.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 24.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.55× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 40.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.230× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 40.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.84× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 48.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 39.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 38.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.9) |
| [[HCT15 (line)]] | alt | 39.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.7× (z +16.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 30.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.9) |
| [[SHP-77 (line)]] | alt | 46.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 45.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +9.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -10.2) |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A13]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CIZ1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CDA]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CTC1]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[MYO5A]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[AKTIP]] | +0.56 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KIF3C]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[MCUR1]] ⚠ | +0.52 | +0.50 / +0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL14]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[KATNAL1]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[UBE2Q2P1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TMOD2]] | +0.51 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[KLKP1-1]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS5]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[EXOSC4]] | -0.50 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[SNRPB]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TIMM10]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CEBPZ]] | -0.49 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[C6orf47]] | -0.49 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[EMC6]] | -0.49 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[NAT10]] | -0.48 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[LBHD1]] | -0.46 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[RAPGEF6]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[GEMIN4]] | -0.46 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[IFT43]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 17.2); signed map (-8.4, 23.2). **Vector** length 105, 27.4% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +24.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +20.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | -0.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -18.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -19.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | regulator of calcineurin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,502,351-24,541,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DSCR1L2 |
| Gene groups (HGNC) | Regulator of calcineurin family |
| Reactome | 5 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; SARS-CoV-1-host interactions; SARS-CoV-1 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKA8](https://www.uniprot.org/uniprotkb/Q9UKA8) (Calcipressin-3):

> Inhibits calcineurin-dependent transcriptional responses by binding to the catalytic domain of calcineurin A. Could play a role during central nervous system development (By similarity).

**Summary**, from NCBI Gene [11123](https://www.ncbi.nlm.nih.gov/gene/11123):

> Enables phosphatase binding activity and troponin I binding activity. Predicted to be involved in calcium-mediated signaling. Predicted to be located in cytosol. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3042) · Entrez [11123](https://www.ncbi.nlm.nih.gov/gene/11123) · UniProt [Q9UKA8](https://www.uniprot.org/uniprotkb/Q9UKA8) · Ensembl [ENSG00000117602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117602)

## Data

Gene col 3931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3931); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3931]; `tensor/DDL_lfc|DDL_z.npy` [3931]; `embed/gene_vectors.npy` [3931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3931 or target_col == 3931). Every well: [[RCAN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCAN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
