---
symbol: "PPP1R12A"
type: "gene"
col: 659
ensembl_id: "ENSG00000058272"
name: "protein phosphatase 1 regulatory subunit 12A"
location: "12q21.2-q21.31"
module: 12
arm: "+"
pooled_cpm: 292.27
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PPP1R12A

*protein phosphatase 1 regulatory subunit 12A* — 12q21.2-q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +29.8, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.73× (z +23.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.525× (z -28.2, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.728× (z -14.4, q 6e-45, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 10 lines (NCI-H2347 0.530×, HOP62 0.570×, BT-474 0.576×, AsPC-1 0.606×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 0.177×, NCI-H1573 0.253×, HEC-1-A 0.362×, LoVo 0.350×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.205×, LOX-IMVI 0.325×, NCI-H460 0.495×, NCI-H2347 0.484×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSF1]] (+0.73, fdr 7e-06), [[REST]] (+0.71, fdr 7e-06), [[NIPBL]] (+0.70, fdr 7e-06); moves opposite to [[LINC03009]] (-0.66, fdr 1e-05), [[TXNDC5]] (-0.65, fdr 1e-05), [[MAT2A]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +29.8 | 0e+00 | 44/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +23.9 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +20.1 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +19.1 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +16.2 | 0e+00 | 41/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +13.2 | 1e-37 | 34/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +13.2 | 1e-37 | 35/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +10.3 | 6e-23 | 33/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +8.7 | 3e-16 | 34/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +8.6 | 4e-16 | 25/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +7.4 | 7e-12 | 21/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +5.7 | 7e-07 | 14/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +4.8 | 6e-05 | 4/48 (SNU-1, BT-474, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | 1.11× | +4.6 | 2e-04 | 19/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +4.5 | 2e-04 | 7/48 (LoVo, HT-29, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.09× | +4.0 | 0.003 | 2/48 (CFPAC-1, hTERT-HPNE) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.17× | +3.7 | 0.008 | 14/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.07× | +2.9 | 0.097 | 8/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 659.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 10 lines (NCI-H2347 0.530×, HOP62 0.570×, BT-474 0.576×, AsPC-1 0.606×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 0.177×, NCI-H1573 0.253×, HEC-1-A 0.362×, LoVo 0.350×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.205×, LOX-IMVI 0.325×, NCI-H460 0.495×, NCI-H2347 0.484×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -28.2 | 0e+00 | 40/44 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.602×** | -23.1 | 0e+00 | 47/49 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.626×** | -19.7 | 0e+00 | 38/45 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.728×** | -14.4 | 6e-45 | 34/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.747×** | -12.7 | 4e-35 | 36/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.808×** | -9.7 | 3e-20 | 27/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.835× | -8.2 | 2e-14 | 21/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.841× | -7.9 | 2e-13 | 20/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -6.3 | 2e-08 | 0/50 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.886× | -5.5 | 2e-06 | 14/48 (NCI-H1792, HEC-1-A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.933× | -4.4 | 5e-04 | 14/49 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.932× | -3.2 | 0.066 | 6/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 512 | 6 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.74× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -31.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.612× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 358 | 3 (1 ⚠) | 9 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.62× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -16.3) |
| [[HOP62 (line)]] | alt | 298 | 3 | 8 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 1.65× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.570× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 291 | 8 (2 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.52× (z +25.5) | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -22.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 292 | 7 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -16.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 289 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +34.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.28× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.531× (z -18.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 263 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +18.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.79× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -15.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 346 | 5 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -13.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 278 | 7 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.519× (z -16.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 292 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.99× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.606× (z -10.0) |
| [[C32 (line)]] | wt | 268 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +20.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.475× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 278 | 5 (2 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.95× (z +15.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -24.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 342 | 2 | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.07× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.648× (z -9.5) |
| [[A549 (line)]] | wt | 274 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +24.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.53× (z +19.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -23.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 355 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +16.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.71× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.576× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 291 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +25.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.17× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -26.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 267 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +17.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.12× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[NCI-H23 (line)]] | alt | 360 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +23.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.91× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -15.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 229 | 3 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.72× (z +10.0) | [[Lonafarnib (drug)]] 5 µM 0.199× (z -16.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.600× (z -9.9) |
| [[RKO (line)]] | wt | 293 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +24.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.472× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[SW1417 (line)]] | alt | 279 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +19.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.586× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 272 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -34.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 237 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -19.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 345 | 4 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -13.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 309 | 3 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.75× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 269 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +20.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.88× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 289 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +19.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.23× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -29.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 252 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +16.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.67× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.578× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 320 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.70× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.564× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 187 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.81× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.608× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 339 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[hTERT-HPNE (line)]] | wt | 336 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.87× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.466× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 271 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +26.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.34× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 181 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.72× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.616× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[Hs 766T (line)]] | wt | 240 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.562× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 324 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.571× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.659× (z -9.5) |
| [[SW48 (line)]] | wt | 249 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.07× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 259 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.65× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.628× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 289 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 287 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 294 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.71× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -21.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 316 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.516× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[NCI-H661 (line)]] | alt | 783 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[RPMI-7951 (line)]] | alt | 282 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.73× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -11.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 295 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 353 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSF1]] | +0.73 | +0.60 / +0.72 | both halves | 7e-06 | STRING 486 |
| [[REST]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NIPBL]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 | STRING 409 |
| [[PRRC2C]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[EID2]] | +0.67 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PPIG]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SNW1]] | +0.65 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03009]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[RPSA]] | -0.62 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SLC19A1]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.60 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[RPL10]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[AHCY]] | -0.60 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[RPN1]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[NOMO2]] | -0.59 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SMG1P1]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.6, 3.4); signed map (3.3, -15.6). **Vector** length 116, 37.5% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +23.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +20.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +29.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -19.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -7.1 | -12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -28.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -23.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -1.1 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.4 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2-q21.31 — chr12:79,773,563-79,935,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MBS, M130; previously MYPT1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Myosin phosphatase targeting family |
| Reactome | 12 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; RHO GTPases activate PAKs |
| Matched by | ensembl_id |

**Function**, from UniProt [O14974](https://www.uniprot.org/uniprotkb/O14974) (Protein phosphatase 1 regulatory subunit 12A):

> Key regulator of protein phosphatase 1C (PPP1C). Mediates binding to myosin. As part of the PPP1C complex, involved in dephosphorylation of PLK1. Capable of inhibiting HIF1AN-dependent suppression of HIF1A activity.

**Summary**, from NCBI Gene [4659](https://www.ncbi.nlm.nih.gov/gene/4659):

> Myosin phosphatase target subunit 1, which is also called the myosin-binding subunit of myosin phosphatase, is one of the subunits of myosin phosphatase. Myosin phosphatase regulates the interaction of actin and myosin downstream of the guanosine triphosphatase Rho. The small guanosine triphosphatase Rho is implicated in myosin light chain (MLC) phosphorylation, which results in contraction of smooth muscle and interaction of actin and myosin in nonmuscle cells. The guanosine triphosphate …

**Accessions** — [HGNC:7618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7618) · Entrez [4659](https://www.ncbi.nlm.nih.gov/gene/4659) · UniProt [O14974](https://www.uniprot.org/uniprotkb/O14974) · Ensembl [ENSG00000058272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058272)

## Data

Gene col 659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 659); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 659]; `tensor/DDL_lfc|DDL_z.npy` [659]; `embed/gene_vectors.npy` [659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 659 or target_col == 659). Every well: [[PPP1R12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
