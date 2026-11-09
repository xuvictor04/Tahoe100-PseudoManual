---
symbol: "STK3"
type: "gene"
col: 2452
ensembl_id: "ENSG00000104375"
name: "serine/threonine kinase 3"
location: "8q22.2"
module: 216
arm: "+"
pooled_cpm: 325.39
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# STK3

*serine/threonine kinase 3* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.44× (z +8.7, q 2e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.490× (z -16.4, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.682× (z -9.1, q 7e-18, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGAP1L]] (+0.69, fdr 7e-06), [[SPIDR]] (+0.63, fdr 1e-05), [[ZFAND3]] (+0.61, fdr 1e-05); moves opposite to [[ZNF550]] (-0.58, fdr 1e-05), [[EEF1AKMT3]] (-0.54, fdr 5e-05), [[ZNF547]] (-0.54, fdr 3e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +8.7 | 2e-15 | 40/48 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +8.3 | 3e-14 | 38/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 4e-07 | 34/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.8 | 1e-06 | 30/48 (BT-474, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.6 | 2e-06 | 21/48 (MIA PaCa-2, AsPC-1, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.2 | 2e-05 | 29/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.8 | 1e-04 | 29/48 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 5e-04 | 25/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.3 | 0.001 | 23/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.2 | 0.002 | 13/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.9 | 0.005 | 20/47 (AsPC-1, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 24/49 (PANC-1, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.013 | 28/49 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.042 | 3/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +3.1 | 0.072 | 15/50 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.072 | 10/47 (AsPC-1, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.072 | 13/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.082 | 3/48 (AN3 CA, CHP-212, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.082 | 7/48 (AsPC-1, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -16.4 | 0e+00 | 42/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -15.5 | 0e+00 | 47/49 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -13.1 | 8e-37 | 44/47 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -9.2 | 7e-18 | 34/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -9.1 | 7e-18 | 38/48 (RKO, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -8.8 | 8e-17 | 28/49 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.718×** | -7.9 | 2e-13 | 37/48 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -5.7 | 9e-07 | 27/48 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -5.2 | 1e-05 | 18/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.875× | -4.5 | 4e-04 | 16/49 (COLO 205, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.886× | -4.1 | 0.003 | 14/49 (CFPAC-1, C32, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.854× | -3.7 | 0.009 | 20/49 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.7 | 0.011 | 21/48 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.027 | 28/48 (SK-MEL-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.869× | -3.3 | 0.032 | 12/48 (SK-MEL-2, BT-474, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.079 | 12/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.915× | -3.0 | 0.086 | 2/49 (SW 1271, SW 1088) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 453 | 7 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.494× (z -12.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 235 | 6 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 338 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.75× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -13.2) |
| [[BT-474 (line)]] | alt | 523 | 5 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.59× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.5) |
| [[HOP62 (line)]] | alt | 322 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.612× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 499 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -14.8) |
| [[KATO III (line)]] | alt | 334 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -18.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.7) |
| [[C32 (line)]] | wt | 388 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.31× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 257 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.84× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 232 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.511× (z -10.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 383 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -17.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.3) |
| [[SW 900 (line)]] | alt | 211 | 5 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.24× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.494× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 221 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.472× (z -11.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 552 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -10.8) |
| [[HT-29 (line)]] | alt | 373 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -16.5) ⚠ toxic |
| [[J82 (line)]] | alt | 373 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 379 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 530 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -9.8) |
| [[SHP-77 (line)]] | alt | 343 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 333 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.7) |
| [[SW480 (line)]] | alt | 246 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.598× (z -10.5) |
| [[A-172 (line)]] | wt | 190 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.506× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.538× (z -10.9) |
| [[A549 (line)]] | wt | 356 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -19.8) |
| [[AsPC-1 (line)]] | alt | 445 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -12.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 344 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 273 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.524× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 291 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 266 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -12.2) |
| [[SW1417 (line)]] | alt | 398 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -13.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 447 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 223 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -9.3) ⚠ toxic |
| [[RKO (line)]] | wt | 587 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -22.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 259 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 375 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -24.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 198 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.519× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -14.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 362 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 286 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.1) |
| [[CHP-212 (line)]] | wt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 310 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.508× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 248 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 390 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -16.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 308 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 211 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 215 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGAP1L]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SPIDR]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ZFAND3]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[XPR1]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CLEC16A]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MYCBP2]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[PITPNB]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NR6A1]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PARD3]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FAF1]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[C1QTNF3-AMACR]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[USP25]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF550]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[EEF1AKMT3]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[ZNF547]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PPIL3]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.52 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[POMT1]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PPIE]] | -0.50 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ZSWIM3]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[VDAC1P8]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TRMU]] | -0.49 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PMS2CL]] | -0.49 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[ZNF561]] | -0.49 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, 16.1); signed map (-16.8, 31.0). **Vector** length 125, 44.3% of its response variance represented; |z| ≥ 3 in 1,404 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.2 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.8 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.4 | -13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.3 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,371,228-98,942,827 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MST2, KRS1 |
| Gene groups (HGNC) | STK3/STK4 kinase family |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13188](https://www.uniprot.org/uniprotkb/Q13188) (Serine/threonine-protein kinase 3):

> Stress-activated, pro-apoptotic kinase which, following caspase-cleavage, enters the nucleus and induces chromatin condensation followed by internucleosomal DNA fragmentation. Key component of the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and …

**Summary**, from NCBI Gene [6788](https://www.ncbi.nlm.nih.gov/gene/6788):

> This gene encodes a serine/threonine protein kinase activated by proapoptotic molecules indicating the encoded protein functions as a growth suppressor. Cleavage of the protein product by caspase removes the inhibitory C-terminal portion. The N-terminal portion is transported to the nucleus where it homodimerizes to form the active kinase which promotes the condensation of chromatin during apoptosis. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:11406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11406) · Entrez [6788](https://www.ncbi.nlm.nih.gov/gene/6788) · UniProt [Q13188](https://www.uniprot.org/uniprotkb/Q13188) · Ensembl [ENSG00000104375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104375)

## Data

Gene col 2452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2452); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2452]; `tensor/DDL_lfc|DDL_z.npy` [2452]; `embed/gene_vectors.npy` [2452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2452 or target_col == 2452). Every well: [[STK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
