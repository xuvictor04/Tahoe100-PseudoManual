---
symbol: "TAOK3"
type: "gene"
col: 5650
ensembl_id: "ENSG00000135090"
name: "TAO kinase 3"
location: "12q24.23"
module: 48
arm: "+"
pooled_cpm: 180.1
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# TAOK3

*TAO kinase 3* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.99× (z +32.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.707× (z -9.5, q 1e-18, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.678× (z -6.0, q 4e-07, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.517×, LOX-IMVI 0.564×, BT-474 0.497×, NCI-H2347 0.491×; ⚠ cell-cycle shift, explains ~1% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0823×, RKO 0.101×, AsPC-1 0.348×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.135×, AsPC-1 0.411×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (A498 0.318×, A549 0.243×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 0.422×); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.495×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL2]] (+0.61, fdr 2e-05), [[SNX6]] (+0.57, fdr 3e-05), [[GIPC1]] (+0.54, fdr 6e-05); moves opposite to [[PIGW]] (-0.58, fdr 9e-05), [[U2AF2]] (-0.57, fdr 2e-05), [[PNPO]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +32.3 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.79×** | +30.3 | 0e+00 | 48/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +29.9 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +13.6 | 8e-40 | 43/48 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +11.8 | 3e-30 | 40/48 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +11.1 | 1e-26 | 43/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +8.9 | 3e-17 | 28/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.28×** | +7.1 | 1e-10 | 29/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +6.6 | 2e-09 | 22/48 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +5.7 | 6e-07 | 20/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +5.5 | 2e-06 | 21/48 (C32, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +5.5 | 2e-06 | 19/48 (C32, SW480, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +5.0 | 3e-05 | 22/49 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.13× | +4.7 | 1e-04 | 15/48 (CFPAC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.6 | 1e-04 | 20/48 (BT-474, LoVo, …) | rises with dose | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +4.6 | 2e-04 | 12/49 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +4.5 | 2e-04 | 20/49 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +4.4 | 3e-04 | 23/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.3 | 6e-04 | 17/48 (C32, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +4.2 | 7e-04 | 17/49 (SW480, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5650.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.517×, LOX-IMVI 0.564×, BT-474 0.497×, NCI-H2347 0.491×; ⚠ cell-cycle shift, explains ~1% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0823×, RKO 0.101×, AsPC-1 0.348×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.135×, AsPC-1 0.411×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (A498 0.318×, A549 0.243×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 0.422×); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.495×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -9.5 | 1e-18 | 29/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.812×** | -6.2 | 2e-07 | 26/48 (J82, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -6.0 | 4e-07 | 31/48 (COLO 205, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.837× | -5.1 | 6e-05 | 23/47 (CFPAC-1, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 0.847× | -4.9 | 8e-05 | 19/49 (AsPC-1, COLO 205, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.727×** | -4.9 | 8e-05 | 23/49 (A498, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -4.6 | 3e-04 | 17/48 (J82, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.858× | -4.4 | 9e-04 | 18/44 (NCI-H23, AsPC-1, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.764×** | -4.2 | 0.002 | 19/38 (Panc 03.27, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.923× | -3.3 | 0.048 | 19/49 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.898× | -3.2 | 0.075 | 15/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 282 | 7 (5 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.89× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.8) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -9.8) |
| [[LoVo (line)]] | wt | 219 | 7 (2 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +25.7) | [[Dinaciclib (drug)]] 5 µM 0.569× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 266 | 7 (2 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.486× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 182 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.422× (z -11.0) |
| [[C32 (line)]] | wt | 225 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +10.2) | — |
| [[A498 (line)]] | wt | 221 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +12.3) | [[TAK-901 (drug)]] 5 µM 0.318× (z -9.9) |
| [[J82 (line)]] | alt | 286 | 3 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.02× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.549× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 150 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.8) | [[Harringtonine (drug)]] 0.5 µM 0.433× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 120 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 126 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -25.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 161 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 289 | 1 | 4 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 1.62× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 95.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +19.3) | — |
| [[Hs 766T (line)]] | wt | 232 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.576× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 235 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -16.4) ⚠ cell-cycle shift, explains ~1% of this change |
| [[SW480 (line)]] | alt | 116 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +26.5) | — |
| [[A-172 (line)]] | wt | 121 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +14.1) | — |
| [[A-427 (line)]] | wt | 110 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.17× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -30.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 549 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -15.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.49× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 406 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 75.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +20.1) | — |
| [[HepG2_C3A (line)]] | wt | 134 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +17.8) | — |
| [[HS-578T (line)]] | alt | 156 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -9.5) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HT-29 (line)]] | alt | 124 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.28× (z +19.8) | — |
| [[LOX-IMVI (line)]] | wt | 255 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +18.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -15.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[MIA PaCa-2 (line)]] | alt | 76.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +20.7) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H2347 (line)]] | alt | 170 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[Panc 03.27 (line)]] | alt | 219 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +13.0) | [[Lonafarnib (drug)]] 5 µM 0.221× (z -13.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 188 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +15.8) | — |
| [[H4 (line)]] | wt | 112 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +14.6) | — |
| [[HCT15 (line)]] | alt | 152 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 170 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +13.1) | — |
| [[KATO III (line)]] | alt | 159 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +20.5) | — |
| [[LS 180 (line)]] | wt | 224 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 127 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +22.9) | — |
| [[PANC-1 (line)]] | alt | 214 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.12× (z +14.5) | — |
| [[RPMI-7951 (line)]] | alt | 173 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 124 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +16.6) | — |
| [[SK-MEL-2 (line)]] | alt | 174 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 73.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +13.5) | — |
| [[SW48 (line)]] | wt | 85.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.14× (z +15.0) | — |
| [[CHP-212 (line)]] | wt | 122 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 156 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.2) | — |
| [[NCI-H2122 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 271 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL2]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SNX6]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GIPC1]] | +0.54 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[GABARAPL2]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RAPGEF2]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ROCK1]] | +0.54 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[C4orf48]] | +0.53 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[DUSP18]] | +0.52 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ELOB]] | +0.51 | +0.38 / +0.36 | both halves | 1e-04 |  |
| [[PGM2L1]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[POLR2J]] ⚠ | +0.51 | +0.49 / +0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC2]] | +0.50 | +0.48 / +0.29 | both halves | 2e-04 |  |
| [[WDR44]] | +0.50 | +0.40 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGW]] | -0.58 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[U2AF2]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PNPO]] | -0.56 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[DPY19L3-DT]] | -0.53 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[NIPBL-DT]] | -0.52 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[ATP13A1]] | -0.51 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[QTRT1]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[FOXP4-AS1]] | -0.50 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[SNX5]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[SAMD10]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[DDX39B]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[IPO4]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.8, -56.7); signed map (36.5, -35.0). **Vector** length 124, 38.6% of its response variance represented; |z| ≥ 3 in 1,539 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +30.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.7 | +7.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +11.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +11.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -11.2 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.7 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -9.2 | -5.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.5 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | TAO kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,149,801-118,372,907 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JIK, DPK, MAP3K18 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; TAO kinase family |
| Reactome | 6 pathways, smallest: RAC2 GTPase cycle; RAC3 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2K8](https://www.uniprot.org/uniprotkb/Q9H2K8) (Serine/threonine-protein kinase TAO3):

> Serine/threonine-protein kinase that acts as a regulator of the p38/MAPK14 stress-activated MAPK cascade and of the MAPK8/JNK cascade. In response to DNA damage, involved in the G2/M transition DNA damage checkpoint by activating the p38/MAPK14 stress-activated MAPK cascade, probably by mediating phosphorylation of upstream MAP2K3 and MAP2K6 kinases. Inhibits basal activity of the MAPK8/JNK cascade and diminishes its activation in response to epidermal growth factor (EGF). Positively regulates …

**Summary**, from NCBI Gene [51347](https://www.ncbi.nlm.nih.gov/gene/51347):

> The protein encoded by this gene is a serine/threonine protein kinase that activates the p38/MAPK14 stress-activated MAPK cascade but inhibits the basal activity of the MAPK8/JNK cascade. The encoded protein is a member of the GCK subfamily of STE20-like kinases. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:18133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18133) · Entrez [51347](https://www.ncbi.nlm.nih.gov/gene/51347) · UniProt [Q9H2K8](https://www.uniprot.org/uniprotkb/Q9H2K8) · Ensembl [ENSG00000135090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135090)

## Data

Gene col 5650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5650); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5650]; `tensor/DDL_lfc|DDL_z.npy` [5650]; `embed/gene_vectors.npy` [5650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5650 or target_col == 5650). Every well: [[TAOK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAOK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
