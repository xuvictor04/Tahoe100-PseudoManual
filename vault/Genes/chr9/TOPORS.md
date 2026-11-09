---
symbol: "TOPORS"
type: "gene"
col: 12422
ensembl_id: "ENSG00000197579"
name: "TOP1 binding arginine/serine rich protein, E3 ubiquitin ligase"
location: "9p21.1"
module: 11
arm: "+"
pooled_cpm: 41.97
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TOPORS

*TOP1 binding arginine/serine rich protein, E3 ubiquitin ligase* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.72× (z +21.0, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.88× (z +17.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.659× (z -6.6, q 3e-08, down in 25 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.0921×, A498 0.213×, NCI-H460 0.219×, SNU-423 0.198×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.272×, A498 0.348×, C-33 A 0.255×, SNU-1 0.217×, …; ⚠ toxic; transcription drop); [[Orlistat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.201×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCC]] (+0.81, fdr 7e-06), [[EID2]] (+0.77, fdr 7e-06), [[ZCCHC3]] (+0.75, fdr 7e-06); moves opposite to [[EIF2S3]] (-0.71, fdr 7e-06), [[TXNDC5]] (-0.70, fdr 7e-06), [[COLGALT1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.72×** | +21.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.88×** | +17.3 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.41×** | +13.9 | 2e-41 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +11.9 | 2e-30 | 47/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.98×** | +11.2 | 5e-27 | 43/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.90×** | +10.5 | 8e-24 | 38/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.3 | 1e-14 | 37/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +7.7 | 1e-12 | 39/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.7 | 1e-12 | 30/48 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +7.5 | 4e-12 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +5.5 | 1e-06 | 27/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.7 | 1e-04 | 28/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 21/48 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.039 | 17/48 (LS 180, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12422.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.0921×, A498 0.213×, NCI-H460 0.219×, SNU-423 0.198×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.272×, A498 0.348×, C-33 A 0.255×, SNU-1 0.217×, …; ⚠ toxic; transcription drop); [[Orlistat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.201×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -6.6 | 3e-08 | 25/40 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -6.1 | 3e-07 | 29/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.2 | 0.18 | 1/49 (AN3 CA) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.821× | -3.2 | 0.18 | 18/48 (SW 1088, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.811× | -3.2 | 0.18 | 16/43 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.6 | 9 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.32× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.0 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +21.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.34× (z +17.4) | — |
| [[A498 (line)]] | wt | 69.5 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +10.1) | — |
| [[KATO III (line)]] | alt | 47.2 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -23.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 50.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 40.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +16.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.9) | — |
| [[A-172 (line)]] | wt | 40.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Orlistat (drug)]] 0.05 µM 0.201× (z -10.1) |
| [[Hs 766T (line)]] | wt | 49.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +14.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 32.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.62× (z +10.9) | — |
| [[SNU-1 (line)]] | wt | 44.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.30× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.9 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.36× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.04× (z +8.6) | — |
| [[A549 (line)]] | wt | 49.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 47.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCC]] | +0.81 | +0.75 / +0.88 | both halves | 7e-06 |  |
| [[EID2]] | +0.77 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[RSF1]] | +0.73 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[THAP1]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.72 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.71 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[REST]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[RBBP6]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | same gene group |
| [[PDCD7]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S3]] | -0.71 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.70 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.68 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[AGO1]] | -0.67 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[NDRG3]] | -0.66 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.64 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[NUTF2]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[CS]] | -0.64 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[OPA1]] | -0.64 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[TBCD]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[RPSA]] | -0.64 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[PABIR2]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.4, 4.7); signed map (3.4, -16.9). **Vector** length 113, 32.3% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +17.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.4 | +21.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.3 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +7.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.6 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.5 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | TOP1 binding arginine/serine rich protein, E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,540,544-32,552,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TP53BPL, LUN; previously RP31 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: SUMOylation of immune response proteins; SUMOylation of SUMOylation proteins; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS56](https://www.uniprot.org/uniprotkb/Q9NS56) (E3 ubiquitin-protein ligase Topors):

> Functions as an E3 ubiquitin-protein ligase and as an E3 SUMO1-protein ligase. Probable tumor suppressor involved in cell growth, cell proliferation and apoptosis that regulates p53/TP53 stability through ubiquitin-dependent degradation. May regulate chromatin modification through sumoylation of several chromatin modification-associated proteins. May be involved in DNA damage-induced cell death through IKBKE sumoylation.

**Summary**, from NCBI Gene [10210](https://www.ncbi.nlm.nih.gov/gene/10210):

> This gene encodes a nuclear protein which is serine and arginine rich, and contains a RING-type zinc finger domain. It is highly expressed in the testis, and functions as an ubiquitin-protein E3 ligase. Mutations in this gene are associated with retinitis pigmentosa type 31. Alternatively spliced transcript variants, encoding different isoforms, have been observed for this locus. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:21653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21653) · Entrez [10210](https://www.ncbi.nlm.nih.gov/gene/10210) · UniProt [Q9NS56](https://www.uniprot.org/uniprotkb/Q9NS56) · Ensembl [ENSG00000197579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197579)

## Data

Gene col 12422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12422); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12422]; `tensor/DDL_lfc|DDL_z.npy` [12422]; `embed/gene_vectors.npy` [12422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12422 or target_col == 12422). Every well: [[TOPORS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOPORS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
