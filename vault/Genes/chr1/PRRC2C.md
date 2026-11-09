---
symbol: "PRRC2C"
type: "gene"
col: 3920
ensembl_id: "ENSG00000117523"
name: "proline rich coiled-coil 2C"
location: "1q24.3"
module: 12
arm: "+"
pooled_cpm: 755.32
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PRRC2C

*proline rich coiled-coil 2C* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +30.0, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.31× (z +19.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.742× (z -6.5, q 5e-08, down in 37 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 7 lines (SW1417 0.584×, SW 900 0.550×, NCI-H2347 0.602×, HT-29 0.560×, …; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.495×, A498 0.646×; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.530×, A-427 0.644×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H13]] (+0.71, fdr 7e-06), [[SNW1]] (+0.71, fdr 7e-06), [[PPP1R12A]] (+0.69, fdr 7e-06); moves opposite to [[TXNDC5]] (-0.58, fdr 1e-05), [[MDH2]] (-0.58, fdr 2e-05), [[PRPS2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.55×** | +30.0 | 0e+00 | 48/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +19.0 | 0e+00 | 48/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +18.8 | 0e+00 | 48/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +13.2 | 7e-38 | 47/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +11.8 | 4e-30 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +11.3 | 1e-27 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +8.9 | 6e-17 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.6 | 2e-12 | 43/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +7.5 | 4e-12 | 36/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +7.3 | 2e-11 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +7.2 | 3e-11 | 45/49 (Hs 766T, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.38×** | +7.0 | 1e-10 | 39/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.0 | 9e-08 | 38/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.9 | 4e-05 | 37/45 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.7 | 1e-04 | 29/48 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.7 | 1e-04 | 27/48 (C32, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 1e-04 | 32/48 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +4.6 | 1e-04 | 36/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.3 | 5e-04 | 8/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.006 | 32/49 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.036 | 25/48 (SW1417, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 7 lines (SW1417 0.584×, SW 900 0.550×, NCI-H2347 0.602×, HT-29 0.560×, …; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.495×, A498 0.646×; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.530×, A-427 0.644×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.742×** | -6.5 | 5e-08 | 37/47 (SW1417, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.799×** | -5.1 | 1e-04 | 32/48 (AsPC-1, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.817×** | -4.6 | 9e-04 | 30/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.872× | -3.1 | 0.27 | 17/48 (BT-474, CHP-212, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 968 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +27.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +19.2) | — |
| [[LoVo (line)]] | wt | 761 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +21.1) | — |
| [[LS 180 (line)]] | wt | 621 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +26.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +21.3) | — |
| [[NCI-H1573 (line)]] | alt | 1,022 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +16.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 960 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +35.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.12× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.530× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 619 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +40.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.91× (z +27.0) | — |
| [[BT-474 (line)]] | alt | 941 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +24.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.25× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.579× (z -11.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[H4 (line)]] | wt | 657 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 530 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +28.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 826 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +24.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 693 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +22.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.560× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 726 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +26.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.69× (z +20.3) | — |
| [[RKO (line)]] | wt | 743 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +26.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.63× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 553 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +26.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +18.1) | — |
| [[SW 900 (line)]] | alt | 1,298 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +26.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +19.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.550× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 781 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +24.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 769 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +28.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.88× (z +17.8) | — |
| [[LOX-IMVI (line)]] | wt | 703 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +24.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 588 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +24.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.30× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 961 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +32.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.42× (z +19.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.602× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 684 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.89× (z +11.7) | — |
| [[A-172 (line)]] | wt | 849 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +33.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +22.3) | — |
| [[A-427 (line)]] | wt | 694 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +21.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.72× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.644× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1,045 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +30.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A549 (line)]] | wt | 824 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +29.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.99× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -18.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[C32 (line)]] | wt | 537 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 858 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +29.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +14.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.582× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 843 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.73× (z +15.7) | — |
| [[HepG2_C3A (line)]] | wt | 668 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 721 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +25.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +16.1) | — |
| [[hTERT-HPNE (line)]] | wt | 789 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +27.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.05× (z +20.1) | — |
| [[KATO III (line)]] | alt | 570 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +14.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.571× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 584 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +20.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.32× (z +18.9) | — |
| [[SNU-423 (line)]] | alt | 595 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +28.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.91× (z +17.0) | — |
| [[SW1417 (line)]] | alt | 663 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.584× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 527 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.96× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 801 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.82× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 517 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +32.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +22.0) | — |
| [[J82 (line)]] | alt | 702 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +25.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.29× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 732 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +22.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +15.6) | — |
| [[AN3 CA (line)]] | alt | 745 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 667 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 813 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +19.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.95× (z +13.2) | — |
| [[CHP-212 (line)]] | wt | 1,034 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 551 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.61× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 633 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2122 (line)]] | alt | 710 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 790 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 802 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 666 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H13]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[SNW1]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R12A]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[PPIG]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ZC3H15]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[SEC62]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[YTHDC1]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[RBM25]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 | STRING 999 |
| [[RSF1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[GPBP1]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[MDH2]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[PRPS2]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[CDK2]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[COLGALT1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[RBM14-RBM4]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ADAM15]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CNPY3]] | -0.55 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[SIGMAR1]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PMPCA]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GPAA1]] | -0.54 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[CHID1]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.7, 2.7); signed map (2.3, -15.8). **Vector** length 102, 47.0% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +19.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | -0.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -7.9 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.8 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | +13.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | proline rich coiled-coil 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,485,530-171,593,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1096, XTP2; previously BAT2D1, BAT2L2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y520](https://www.uniprot.org/uniprotkb/Q9Y520) (Translational regulator PRRC2C):

> Promotes leaky scanning, allowing ribosomes to bypass the translation start codons of upstream open reading frames (ORFs) in mRNAs and facilitating efficient translation of the downstream main ORF. Required for efficient formation of stress granules.

**Summary**, from NCBI Gene [23215](https://www.ncbi.nlm.nih.gov/gene/23215):

> Enables RNA binding activity. Involved in stress granule assembly. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24903) · Entrez [23215](https://www.ncbi.nlm.nih.gov/gene/23215) · UniProt [Q9Y520](https://www.uniprot.org/uniprotkb/Q9Y520) · Ensembl [ENSG00000117523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117523)

## Data

Gene col 3920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3920); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3920]; `tensor/DDL_lfc|DDL_z.npy` [3920]; `embed/gene_vectors.npy` [3920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3920 or target_col == 3920). Every well: [[PRRC2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRC2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
