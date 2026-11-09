---
symbol: "DDX52"
type: "gene"
col: 15903
ensembl_id: "ENSG00000278053"
name: "DExD-box helicase 52"
location: "17q12"
module: 11
arm: "+"
pooled_cpm: 83.64
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DDX52

*DExD-box helicase 52* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.25× (z +23.6, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.43× (z +18.3, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.624×; ⚠ cell-cycle shift, explains ~33% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.791×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC4]] (+0.66, fdr 7e-06), [[RPL7L1]] (+0.64, fdr 7e-06), [[JPX]] (+0.62, fdr 1e-05); moves opposite to [[DDB1]] (-0.63, fdr 7e-06), [[CALU]] (-0.59, fdr 1e-05), [[FKBP10]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.25×** | +23.6 | 0e+00 | 43/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +18.3 | 0e+00 | 46/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +17.6 | 0e+00 | 45/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +13.8 | 3e-41 | 44/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.92×** | +13.4 | 5e-39 | 46/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.92×** | +13.4 | 7e-39 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +10.7 | 1e-24 | 43/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +9.1 | 5e-18 | 35/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +8.3 | 4e-15 | 39/47 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +8.1 | 2e-14 | 36/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +8.1 | 2e-14 | 37/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +8.0 | 7e-14 | 37/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +7.6 | 2e-12 | 32/48 (NCI-H1792, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 2e-09 | 29/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.5 | 3e-09 | 34/49 (CFPAC-1, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 3e-06 | 24/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 4e-06 | 25/48 (H4, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 4e-06 | 31/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.5 | 0.010 | 7/48 (HOP62, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.020 | 8/49 (CFPAC-1, LOX-IMVI, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.038 | 15/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.054 | 12/48 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15903.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.624×; ⚠ cell-cycle shift, explains ~33% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.791×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.839× | -3.5 | 0.28 | 16/49 (A-172, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.3 | 0.28 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.38 | 9/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 122 | 10 (5 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.36× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 57.1 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 187 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.43× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 63.6 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.75× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.15× (z +11.1) | — |
| [[LoVo (line)]] | wt | 66.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.85× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 32.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +13.7) | — |
| [[A-172 (line)]] | wt | 68.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +12.6) | — |
| [[A498 (line)]] | wt | 93.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +14.7) | — |
| [[A549 (line)]] | wt | 91.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 62.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 77.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 60.2 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +12.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 334 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 83.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +12.6) | — |
| [[KATO III (line)]] | alt | 85.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 101 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.17× (z +9.1) | — |
| [[A-427 (line)]] | wt | 90.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 59.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 170 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 74.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 55.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.69× (z +9.4) | — |
| [[C32 (line)]] | wt | 50.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.6) | — |
| [[H4 (line)]] | wt | 42.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 90.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.90× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~56% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.05× (z +8.6) | — |
| [[RKO (line)]] | wt | 89.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 70.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 82.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +8.6) | — |
| [[SW48 (line)]] | wt | 73.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C-33 A (line)]] | alt | 87.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[COLO 205 (line)]] | alt | 64.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 73.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HepG2_C3A (line)]] | wt | 54.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[J82 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 | STRING 533 |
| [[JPX]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZNF594]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZNF302]] | +0.60 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[CMTR2]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 | STRING 477 |
| [[GSPT2]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UBE3A]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[POLR1F]] | +0.58 | +0.71 / +0.51 | both halves | 1e-05 | same gene group; STRING 565 |
| [[OTUD6B-AS1]] | +0.57 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[TMEM17]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDB1]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CALU]] | -0.59 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[FKBP10]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[P3H1]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ESYT1]] | -0.58 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[PDIA4]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.57 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[P4HB]] | -0.57 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SEC23A]] | -0.57 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[PIK3R2]] | -0.56 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[OAT]] | -0.56 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[COPA]] | -0.56 | -0.67 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.3, 7.1); signed map (0.6, -21.3). **Vector** length 75.4, 19.0% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +18.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +8.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | +6.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | DExD-box helicase 52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,609,739-37,643,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ROK1 |
| Gene groups (HGNC) | DEAD-box helicases; SSU processome; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2R4](https://www.uniprot.org/uniprotkb/Q9Y2R4) (Probable ATP-dependent RNA helicase DDX52):

> Required for efficient ribosome biogenesis (By similarity). May control cell cycle progression by regulating translation of mRNAs that contain a terminal oligo pyrimidine (TOP) motif in their 5' UTRs, such as GTPBP4 (By similarity).

**Summary**, from NCBI Gene [11056](https://www.ncbi.nlm.nih.gov/gene/11056):

> Enables RNA binding activity. Predicted to be involved in maturation of SSU-rRNA. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20038) · Entrez [11056](https://www.ncbi.nlm.nih.gov/gene/11056) · UniProt [Q9Y2R4](https://www.uniprot.org/uniprotkb/Q9Y2R4) · Ensembl [ENSG00000278053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278053)

## Data

Gene col 15903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15903); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15903]; `tensor/DDL_lfc|DDL_z.npy` [15903]; `embed/gene_vectors.npy` [15903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15903 or target_col == 15903). Every well: [[DDX52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
