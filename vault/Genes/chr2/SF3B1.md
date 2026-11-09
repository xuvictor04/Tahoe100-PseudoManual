---
symbol: "SF3B1"
type: "gene"
col: 3688
ensembl_id: "ENSG00000115524"
name: "splicing factor 3b subunit 1"
location: "2q33.1"
module: 28
arm: "+"
pooled_cpm: 286.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SF3B1

*splicing factor 3b subunit 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +22.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +13.9, q 3e-41, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.750× (z -9.2, q 2e-17, down in 32 of 49 measured lines) ⚠ cell-cycle shift, explains ~18% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.807× (z -4.8, q 1e-04, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.580×, NCI-H460 0.592×, SW480 0.603×, A498 0.567×, …; ⚠ cell-cycle shift, explains ~18% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.500×, CFPAC-1 0.519×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.516×; ⚠ cell-cycle shift, explains ~22% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA5]] (+0.67, fdr 7e-06), [[BROX]] (+0.67, fdr 7e-06), [[ARCN1]] (+0.65, fdr 7e-06); moves opposite to [[FOXK2]] (-0.62, fdr 1e-05), [[SLC27A4]] (-0.61, fdr 1e-05), [[ATOX1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.05×** | +22.9 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +13.9 | 3e-41 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +13.6 | 7e-40 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +13.3 | 6e-38 | 48/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.64×** | +10.7 | 1e-24 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 9e-16 | 38/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.46×** | +8.5 | 1e-15 | 31/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +8.1 | 5e-14 | 39/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +7.3 | 2e-11 | 32/45 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.6 | 2e-09 | 35/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +6.3 | 1e-08 | 39/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +6.1 | 5e-08 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.6 | 1e-06 | 32/48 (C32, A-172, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.7 | 9e-05 | 24/38 (NCI-H1573, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 3e-04 | 24/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.014 | 18/48 (PANC-1, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.580×, NCI-H460 0.592×, SW480 0.603×, A498 0.567×, …; ⚠ cell-cycle shift, explains ~18% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.500×, CFPAC-1 0.519×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.516×; ⚠ cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.750×** | -9.2 | 2e-17 | 32/49 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.656×** | -9.1 | 2e-17 | 44/47 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.761×** | -6.1 | 1e-07 | 31/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.789×** | -5.3 | 1e-05 | 28/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.798×** | -5.1 | 5e-05 | 27/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.799×** | -4.9 | 1e-04 | 28/48 (H4, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.807×** | -4.8 | 1e-04 | 31/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.812×** | -4.7 | 2e-04 | 30/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -4.3 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Cilostazol (drug)]] 5 µM |  | 0.838× | -3.8 | 0.008 | 19/48 (NCI-H23, SNU-423, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.849× | -3.7 | 0.012 | 19/48 (SW48, A498, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.850× | -3.7 | 0.012 | 17/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -3.6 | 0.012 | 15/48 (LS 180, A549, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.871× | -3.1 | 0.080 | 11/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 241 | 13 (7 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +24.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -13.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[PANC-1 (line)]] | alt | 286 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +27.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +20.0) | — |
| [[SW480 (line)]] | alt | 309 | 11 (5 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -13.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[LoVo (line)]] | wt | 301 | 10 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +22.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -13.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H1573 (line)]] | alt | 295 | 9 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +30.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.601× (z -8.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A549 (line)]] | wt | 279 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +22.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -10.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[LOX-IMVI (line)]] | wt | 246 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +23.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 284 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 240 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +14.8) | — |
| [[KATO III (line)]] | alt | 259 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +17.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 264 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H23 (line)]] | alt | 349 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +22.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 264 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 230 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +24.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 273 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +18.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.18× (z +13.6) | — |
| [[NCI-H1792 (line)]] | alt | 226 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +21.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.07× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[Panc 03.27 (line)]] | alt | 280 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.80× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.662× (z -10.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[RKO (line)]] | wt | 289 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -11.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 245 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +14.7) | — |
| [[A-427 (line)]] | wt | 237 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +16.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +12.7) | — |
| [[C32 (line)]] | wt | 180 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +22.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +15.6) | — |
| [[COLO 205 (line)]] | alt | 273 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.40× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 249 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 215 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.18× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 275 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.71× (z +9.8) | — |
| [[A498 (line)]] | wt | 390 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +14.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.91× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 442 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.516× (z -10.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 379 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -10.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[H4 (line)]] | wt | 274 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +11.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 284 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H2030 (line)]] | alt | 336 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 342 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.75× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 298 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +12.8) | — |
| [[SW48 (line)]] | wt | 317 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 270 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 320 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 215 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.46× (z +11.3) | — |
| [[J82 (line)]] | alt | 321 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 332 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 258 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 337 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 278 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 320 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 555 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 306 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[BROX]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ARCN1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | STRING 509 |
| [[CCDC25]] | +0.64 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZC3H11A]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 400 |
| [[STAG2]] | +0.63 | +0.46 / +0.73 | both halves | 2e-05 | same gene group; STRING 469 |
| [[SMARCA5]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | same gene group; pathway: B-WICH complex positively regulates rRNA expression; STRING 905 |
| [[DDX1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | STRING 428 |
| [[ATRX]] | +0.61 | +0.40 / +0.68 | both halves | 4e-05 | STRING 400 |
| [[SPDYA]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MORF4L1P1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PHF3]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SLC27A4]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[COPS9]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ZNF710]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[CORO7]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[HIRA]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.57 | -0.40 / -0.62 | both halves | 4e-05 |  |
| [[ESRRA]] | -0.57 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[CCT6P3-1]] | -0.56 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PAM16]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SF3B1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.4, 7.2); signed map (10.8, -27.7). **Vector** length 103, 38.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +5.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.9 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.5 | +22.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -8.0 | -9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.0 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -4.4 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,388,515-197,435,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP155, SF3b155, PRPF10, Prp10, Hsh155 |
| Gene groups (HGNC) | Armadillo like helical domain containing; SF3b complex; B-WICH chromatin-remodelling complex subunits |
| Reactome | 17 pathways, smallest: B-WICH complex positively regulates rRNA expression; mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [O75533](https://www.uniprot.org/uniprotkb/O75533) (Splicing factor 3B subunit 1):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B1 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [23451](https://www.ncbi.nlm.nih.gov/gene/23451):

> This gene encodes subunit 1 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also a component of the minor U12-type spliceosome. The carboxy-terminal two-thirds of subunit 1 have …

**Accessions** — [HGNC:10768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10768) · Entrez [23451](https://www.ncbi.nlm.nih.gov/gene/23451) · UniProt [O75533](https://www.uniprot.org/uniprotkb/O75533) · Ensembl [ENSG00000115524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115524)

## Data

Gene col 3688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3688); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3688]; `tensor/DDL_lfc|DDL_z.npy` [3688]; `embed/gene_vectors.npy` [3688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3688 or target_col == 3688). Every well: [[SF3B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
