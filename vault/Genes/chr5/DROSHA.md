---
symbol: "DROSHA"
type: "gene"
col: 3453
ensembl_id: "ENSG00000113360"
name: "drosha ribonuclease III"
location: "5p13.3"
module: 4
arm: "+"
pooled_cpm: 87.98
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DROSHA

*drosha ribonuclease III* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.33× (z +6.2, q 4e-07, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (COLO 205 2.70×, LoVo 2.18×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A498 2.10×; ⚠ cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.547× (z -18.5, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.506× (z -14.2, q 4e-43, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELAC2]] (+0.78, fdr 7e-06), [[HERC2]] (+0.74, fdr 7e-06), [[NUP205]] (+0.69, fdr 7e-06); moves opposite to [[ACAP1]] (-0.68, fdr 7e-06), [[ZMYM5]] (-0.64, fdr 7e-06), [[PIM3]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (COLO 205 2.70×, LoVo 2.18×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A498 2.10×; ⚠ cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +6.2 | 4e-07 | 31/48 (A498, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.5 | 9e-06 | 32/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +4.5 | 0.001 | 22/48 (A498, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.019 | 18/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.19× | +3.7 | 0.024 | 20/48 (A498, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 1.17× | +3.3 | 0.082 | 19/42 (HT-29, KATO III, …) | rises with dose | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.082 | 8/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +3.2 | 0.089 | 15/48 (HOP62, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.547×** | -18.5 | 0e+00 | 44/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.506×** | -14.2 | 4e-43 | 39/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -12.1 | 2e-31 | 40/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -11.8 | 7e-30 | 41/48 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -11.4 | 3e-28 | 38/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -8.6 | 8e-16 | 37/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -7.9 | 3e-13 | 30/49 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -7.7 | 1e-12 | 34/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -7.5 | 4e-12 | 27/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -7.4 | 8e-12 | 35/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.720×** | -7.1 | 6e-11 | 32/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -6.0 | 7e-08 | 25/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.783×** | -5.1 | 2e-05 | 23/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.7 | 0.010 | 23/48 (SW 1088, BT-474, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.900× | -3.2 | 0.050 | 7/49 (A-172, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 73.5 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.340× (z -15.4) |
| [[A498 (line)]] | wt | 84.2 | 2 (2 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -30.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.181× (z -22.2) |
| [[NCI-H2030 (line)]] | alt | 96.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -16.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -14.3) |
| [[HOP62 (line)]] | alt | 87.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -12.0) |
| [[A-172 (line)]] | wt | 83.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -22.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -14.0) |
| [[A549 (line)]] | wt | 86.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.258× (z -14.1) |
| [[BT-474 (line)]] | alt | 102 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -18.7) |
| [[PANC-1 (line)]] | alt | 87.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -21.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 48.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.5) |
| [[C32 (line)]] | wt | 57.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -12.6) |
| [[HS-578T (line)]] | alt | 76.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 65.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 100 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 146 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.434× (z -10.7) |
| [[SW 900 (line)]] | alt | 86.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -9.5) |
| [[SW1417 (line)]] | alt | 94.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -11.0) |
| [[COLO 205 (line)]] | alt | 69.6 | 2 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +9.6) | [[XRK3F2 (drug)]] 0.5 µM 0.274× (z -8.9) |
| [[J82 (line)]] | alt | 142 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -37.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -15.9) |
| [[RKO (line)]] | wt | 73.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -11.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -8.8) |
| [[SW480 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.517× (z -10.3) |
| [[A-427 (line)]] | wt | 120 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -14.5) |
| [[HCT15 (line)]] | alt | 71.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -9.0) |
| [[KATO III (line)]] | alt | 58.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 85.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.18× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 79.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 68.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -17.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.362× (z -10.7) |
| [[SW 1088 (line)]] | alt | 81.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0824× (z -8.8) |
| [[H4 (line)]] | wt | 85.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 59.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | — |
| [[NCI-H2347 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.479× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAC2]] | +0.78 | +0.66 / +0.76 | both halves | 7e-06 | same gene group; pathway: Gene Silencing by RNA; STRING 512 |
| [[HERC2]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NUP205]] | +0.69 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[NUP155]] | +0.69 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[IPO11]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PHB1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[WDR5]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP1]] | -0.68 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[PIM3]] | -0.62 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[KDM5B]] | -0.62 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.62 | -0.67 / -0.55 | both halves | 1e-05 | pathway: Gene Silencing by RNA |
| [[NPHS1]] | -0.61 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.60 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[LITAF]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RNF19A]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[GPRC5C]] | -0.60 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[GLIS2]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity lowers DROSHA's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.24× higher at baseline in the lines without AGR2 | 0.029 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[ITGA1]] | B | ITGA1 activity lowers DROSHA's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.15× higher at baseline in the lines without ITGA1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.1, -31.6); signed map (-15.8, -50.4). **Vector** length 118, 34.4% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.8 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.6 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.1 | -18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.5 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | drosha ribonuclease III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:31,400,494-31,532,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNASE3L, Etohi2, HSA242976, RN3; previously RNASEN |
| Gene groups (HGNC) | Endoribonucleases; Microprocessor complex |
| Reactome | 2 pathways, smallest: MicroRNA (miRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRR4](https://www.uniprot.org/uniprotkb/Q9NRR4) (Ribonuclease 3):

> Ribonuclease III double-stranded (ds) RNA-specific endoribonuclease that is involved in the initial step of microRNA (miRNA) biogenesis. Component of the microprocessor complex that is required to process primary miRNA transcripts (pri-miRNAs) to release precursor miRNA (pre-miRNA) in the nucleus. Within the microprocessor complex, DROSHA cleaves the 3' and 5' strands of a stem-loop in pri-miRNAs (processing center 11 bp from the dsRNA-ssRNA junction) to release hairpin-shaped pre-miRNAs that …

**Summary**, from NCBI Gene [29102](https://www.ncbi.nlm.nih.gov/gene/29102):

> This gene encodes a ribonuclease (RNase) III double-stranded RNA-specific ribonuclease and subunit of the microprocessor protein complex, which catalyzes the initial processing step of microRNA (miRNA) synthesis. The encoded protein cleaves the stem loop structure from the primary microRNA (pri-miRNA) in the nucleus, yielding the precursor miRNA (pre-miRNA), which is then exported to the cytoplasm for further processing. In a human cell line lacking a functional copy of this gene, canonical …

**Accessions** — [HGNC:17904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17904) · Entrez [29102](https://www.ncbi.nlm.nih.gov/gene/29102) · UniProt [Q9NRR4](https://www.uniprot.org/uniprotkb/Q9NRR4) · Ensembl [ENSG00000113360](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113360)

## Data

Gene col 3453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3453); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3453]; `tensor/DDL_lfc|DDL_z.npy` [3453]; `embed/gene_vectors.npy` [3453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3453 or target_col == 3453). Every well: [[DROSHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DROSHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
