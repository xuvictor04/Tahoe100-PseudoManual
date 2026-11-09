---
symbol: "CCDC88A"
type: "gene"
col: 3663
ensembl_id: "ENSG00000115355"
name: "coiled-coil and HOOK domain protein 88A"
location: "2p16.1"
module: 22
arm: "+"
pooled_cpm: 259.75
n_lines_expressing: 42
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 12
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCDC88A

*coiled-coil and HOOK domain protein 88A* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +27.7, q 0e+00, up in 38 of 40 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +13.4, q 9e-39, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -14.8, q 0e+00, down in 34 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (A549 0.281×, NCI-H1792 0.413×, SW480 0.643×, PANC-1 0.600×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.472×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.523×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF9]] (+0.56, fdr 8e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[CENPE]] (+0.55, fdr 2e-05), [[EIF5A2]] (+0.55, fdr 3e-05), [[PAG1]] (+0.54, fdr 1e-04); moves opposite to [[SUPV3L1]] (-0.63, fdr 1e-05), [[NAXD]] (-0.58, fdr 4e-05), [[ZNF343]] (-0.58, fdr 2e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 12 go from it, the strongest it → [[MTRR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.13×** | +27.7 | 0e+00 | 38/40 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.99×** | +17.4 | 0e+00 | 35/40 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +14.5 | 1e-45 | 36/40 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +13.4 | 9e-39 | 32/40 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +12.9 | 4e-36 | 37/40 (SW1417, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.60×** | +12.3 | 1e-32 | 32/40 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.58×** | +11.9 | 6e-31 | 33/40 (SW480, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +11.0 | 3e-26 | 32/40 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.49×** | +10.4 | 2e-23 | 28/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +10.3 | 6e-23 | 33/40 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +9.4 | 3e-19 | 34/40 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.42×** | +8.9 | 2e-17 | 25/37 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.39×** | +8.7 | 2e-16 | 26/40 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +7.7 | 8e-13 | 26/40 (C32, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +7.6 | 1e-12 | 29/40 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.8 | 3e-10 | 33/41 (SW1417, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +5.3 | 3e-06 | 23/41 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 22/40 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.005 | 15/40 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.044 | 13/40 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.056 | 18/40 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.059 | 6/40 (HepG2/C3A, NCI-H460, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | 1.12× | +2.8 | 0.098 | 0/40 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (A549 0.281×, NCI-H1792 0.413×, SW480 0.643×, PANC-1 0.600×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.441×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.472×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.523×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -14.8 | 0e+00 | 34/41 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -8.0 | 3e-13 | 1/42 (NCI-H2122) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.827×** | -5.0 | 1e-04 | 22/40 (A549, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.839× | -4.4 | 0.002 | 19/40 (A549, SW 900, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.734×** | -4.2 | 0.002 | 21/40 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -4.1 | 0.004 | 16/40 (A549, LoVo, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.768×** | -3.6 | 0.023 | 17/34 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.877× | -3.3 | 0.064 | 14/40 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.878× | -3.3 | 0.064 | 5/40 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.799× | -3.1 | 0.11 | 15/42 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.801× | -3.0 | 0.12 | 16/41 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 428 | 6 (5 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +12.0) | [[Binimetinib (drug)]] 5 µM 0.472× (z -11.2) |
| [[LoVo (line)]] | wt | 168 | 12 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +18.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.84× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 93.2 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +23.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 95.6 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +28.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.08× (z +18.4) | — |
| [[CFPAC-1 (line)]] | alt | 155 | 9 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +19.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.26× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.5) |
| [[C32 (line)]] | wt | 197 | 8 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +23.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.1) |
| [[J82 (line)]] | alt | 147 | 9 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.87× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 309 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +11.6) | [[PH-797804 (drug)]] 5 µM 0.369× (z -8.6) |
| [[PANC-1 (line)]] | alt | 422 | 8 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +23.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.75× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -13.8) |
| [[RKO (line)]] | wt | 289 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +27.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +15.5) | — |
| [[A498 (line)]] | wt | 305 | 6 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.662× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 169 | 6 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.95× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 257 | 6 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.68× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 112 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +26.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 384 | 6 (6 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 317 | 6 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.60× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 381 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +21.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.58× (z +9.2) | — |
| [[SW480 (line)]] | alt | 304 | 5 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +29.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 277 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 273 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.4) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 209 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +19.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 283 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +17.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 588 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -23.1) |
| [[H4 (line)]] | wt | 330 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.3) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HS-578T (line)]] | alt | 230 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +17.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 334 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 304 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -10.5) |
| [[A-427 (line)]] | wt | 511 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.79× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 368 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +21.2) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -11.8) |
| [[Hs 766T (line)]] | wt | 217 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 384 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.9) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -8.8) |
| [[SNU-423 (line)]] | alt | 193 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 81.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 432 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 459 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -20.6) |
| [[SW 1271 (line)]] | alt | 381 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 44.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 38.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 432 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 524 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF9]] ⚠ | +0.56 | +0.49 / +0.37 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CENPE]] | +0.55 | +0.53 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[EIF5A2]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PAG1]] | +0.54 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[KIAA0586]] | +0.53 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC00540]] | +0.52 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[SMC4]] | +0.52 | +0.55 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CALM1]] | +0.51 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[CALM2]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[GAS2L3]] | +0.50 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[PICALM]] | +0.50 | +0.30 / +0.43 | both halves | 2e-04 | pathway: RND3 GTPase cycle |
| [[THOC2]] | +0.49 | +0.37 / +0.48 | both halves | 9e-05 |  |
| [[KNL1]] | +0.49 | +0.49 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPV3L1]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[NAXD]] | -0.58 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ZNF343]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A38]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MAF1]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PCMTD1]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MLYCD]] | -0.51 | -0.16 / -0.50 | ⚠ one half (not replicated) | 0.001 |  |
| [[LRRC47]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[USF1]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | -0.49 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[OTUB1]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NADSYN1]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CCT6P1]] | -0.49 | -0.43 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTRR]] | B | CCDC88A activity raises MTRR's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CCDC88A | 0.012 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[ZNF343]] | B | CCDC88A activity raises ZNF343's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without CCDC88A | 0.012 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[SLC25A38]] | B | CCDC88A activity raises SLC25A38's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.22× lower at baseline in the lines without CCDC88A | 0.024 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[CCT6P1]] | B | CCDC88A activity raises CCT6P1's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without CCDC88A | 0.025 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[EIF5A2]] | B | CCDC88A activity raises EIF5A2's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without CCDC88A | 0.037 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[MMAA]] | B | CCDC88A activity lowers MMAA's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.60× higher at baseline in the lines without CCDC88A | 0.037 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | CCDC88A activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express CCDC88A (8) vs lines expressing it (40) | the lines without CCDC88A: 0.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | CCDC88A activity raises the cells' numbers under Apalutamide 0.5 µM (protects the cells) | lines that do not express CCDC88A (8) vs lines expressing it (40) | the lines without CCDC88A: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| cells under [[Afatinib (drug)]] 0.05 µM | B | CCDC88A activity raises the cells' numbers under Afatinib 0.05 µM (protects the cells) | lines that do not express CCDC88A (8) vs lines expressing it (40) | the lines without CCDC88A: 0.85× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[STARD7-AS1]] | B | CCDC88A activity raises STARD7-AS1's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without CCDC88A | 0.084 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[CUL2]] | B | CCDC88A activity raises CUL2's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CCDC88A | 0.087 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[BCAP29]] | B | CCDC88A activity raises BCAP29's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without CCDC88A | 0.089 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.366). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, -16.0); signed map (3.1, 24.9). **Vector** length 134, 43.5% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.8 | +12.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.6 | +11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.1 | -14.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | -6.2 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and HOOK domain protein 88A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,287,842-55,419,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10392, APE, GIV, HkRP1, GRDN; previously KIAA1212 |
| Gene groups (HGNC) | HOOK related protein family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: RND1 GTPase cycle; RND3 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3V6T2](https://www.uniprot.org/uniprotkb/Q3V6T2) (Girdin):

> Bifunctional modulator of guanine nucleotide-binding proteins (G proteins). Acts as a non-receptor guanine nucleotide exchange factor which binds to and activates guanine nucleotide-binding protein G(i) alpha subunits. Also acts as a guanine nucleotide dissociation inhibitor for guanine nucleotide-binding protein G(s) subunit alpha GNAS. Essential for cell migration. Interacts in complex with G(i) alpha subunits with the EGFR receptor, retaining EGFR at the cell membrane following ligand …

**Summary**, from NCBI Gene [55704](https://www.ncbi.nlm.nih.gov/gene/55704):

> This gene encodes a member of the Girdin family of coiled-coil domain containing proteins. The encoded protein is an actin-binding protein that is activated by the serine/threonine kinase Akt and plays a role in cytoskeleton remodeling and cell migration. The encoded protein also enhances Akt signaling by mediating phosphoinositide 3-kinase (PI3K)-dependent activation of Akt by growth factor receptor tyrosine kinases and G protein-coupled receptors. Increased expression of this gene and …

**Accessions** — [HGNC:25523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25523) · Entrez [55704](https://www.ncbi.nlm.nih.gov/gene/55704) · UniProt [Q3V6T2](https://www.uniprot.org/uniprotkb/Q3V6T2) · Ensembl [ENSG00000115355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115355)

## Data

Gene col 3663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3663); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3663]; `tensor/DDL_lfc|DDL_z.npy` [3663]; `embed/gene_vectors.npy` [3663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3663 or target_col == 3663). Every well: [[CCDC88A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC88A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
