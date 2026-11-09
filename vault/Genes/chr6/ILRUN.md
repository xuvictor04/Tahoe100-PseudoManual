---
symbol: "ILRUN"
type: "gene"
col: 12289
ensembl_id: "ENSG00000196821"
name: "inflammation and lipid regulator with UBA-like and NBR1-like domains"
location: "6p21.31"
module: 11
arm: "-"
pooled_cpm: 99.53
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ILRUN

*inflammation and lipid regulator with UBA-like and NBR1-like domains* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.08× (z +16.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.787× (z -7.5, q 3e-11, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.313×, C-33 A 0.355×, SHP-77 0.450×, NCI-H2347 0.481×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 0.504×, C32 0.529×, hTERT-HPNE 0.494×, CFPAC-1 0.600×; ⚠ cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.380×, NCI-H2347 0.421×, AN3 CA 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (Trihydrate) (drug)]] 5 µM in 1 line (SW 1088 0.0675×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.489×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRN]] (+0.69, fdr 2e-05), [[SEC11A]] (+0.67, fdr 3e-05), [[LMTK2]] (+0.66, fdr 6e-05); moves opposite to [[HMGXB4]] (-0.68, fdr 7e-06), [[NAIF1]] (-0.64, fdr 1e-05), [[HELQ]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[GORAB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +16.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +15.2 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +13.8 | 6e-41 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +12.2 | 6e-32 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +11.7 | 2e-29 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +11.6 | 6e-29 | 46/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +11.5 | 2e-28 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +11.0 | 2e-26 | 42/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +10.2 | 2e-22 | 39/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +10.0 | 9e-22 | 43/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +7.8 | 3e-13 | 35/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.5 | 4e-09 | 38/48 (SW480, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.8 | 2e-07 | 30/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +5.1 | 1e-05 | 28/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 3e-04 | 24/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12289.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.313×, C-33 A 0.355×, SHP-77 0.450×, NCI-H2347 0.481×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 0.504×, C32 0.529×, hTERT-HPNE 0.494×, CFPAC-1 0.600×; ⚠ cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.380×, NCI-H2347 0.421×, AN3 CA 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (Trihydrate) (drug)]] 5 µM in 1 line (SW 1088 0.0675×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.489×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.787×** | -7.5 | 3e-11 | 33/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.778×** | -5.6 | 7e-06 | 29/48 (A-427, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.805× | -3.4 | 0.11 | 18/48 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.820× | -3.1 | 0.23 | 14/48 (NCI-H661, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.870× | -3.1 | 0.23 | 20/48 (NCI-H2347, LoVo, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.24 | 18/48 (CFPAC-1, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 63.2 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.85× (z +23.6) | — |
| [[PANC-1 (line)]] | alt | 81.2 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +15.6) | — |
| [[SW480 (line)]] | alt | 90.4 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +15.3) | — |
| [[A-427 (line)]] | wt | 81.9 | 4 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.90× (z +13.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -20.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.489× (z -9.1) |
| [[HOP62 (line)]] | alt | 114 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.0) | — |
| [[LoVo (line)]] | wt | 85.9 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 72.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 109 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.49× (z +10.2) | — |
| [[C32 (line)]] | wt | 92.9 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.26× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 83.3 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.58× (z +10.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 82.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 106 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 105 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 75.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 136 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 92.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 83.4 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 149 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +10.9) | — |
| [[J82 (line)]] | alt | 100 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 48.9 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 85.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 134 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.30× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 137 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 91.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 133 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +11.6) | — |
| [[RKO (line)]] | wt | 116 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +11.1) | — |
| [[SW48 (line)]] | wt | 99.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.4) | — |
| [[A549 (line)]] | wt | 66.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 217 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[H4 (line)]] | wt | 81.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 106 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.05× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -8.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 86.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.23× (z +8.5) ⚠ toxic | — |
| [[SW 1088 (line)]] | alt | 81.1 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 5 µM 0.0675× (z -9.6) |
| [[A-172 (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN]] | +0.69 | +0.79 / +0.48 | both halves | 2e-05 |  |
| [[SEC11A]] | +0.67 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[LMTK2]] | +0.66 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[GRB2]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.66 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[SUMO1]] | +0.65 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ARHGEF7]] | +0.65 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[LAPTM4A]] | +0.64 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[GNPTG]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PLEKHB2]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TECR]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGXB4]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[NAIF1]] | -0.64 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[HELQ]] | -0.63 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.63 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.63 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.63 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.62 | -0.72 / -0.46 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.62 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[RRP8]] | -0.61 | -0.78 / -0.45 | both halves | 3e-05 |  |
| [[MRPL38]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.61 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.61 | -0.69 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GORAB]] | C | ILRUN's natural level weakens GORAB's drug response | ILRUN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.05; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-14.4, -17.1); signed map (-48.9, -8.5). **Vector** length 106, 32.5% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +15.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +13.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -14.2 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -12.5 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.3 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.5 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | inflammation and lipid regulator with UBA-like and NBR1-like domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,587,288-34,696,859 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22195, dJ391O22.4; previously C6orf106 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6K1](https://www.uniprot.org/uniprotkb/Q9H6K1) (Protein ILRUN):

> Negative regulator of innate antiviral response. Blocks IRF3-dependent cytokine production such as IFNA, IFNB and TNF. Interacts with IRF3 and inhibits IRF3 recruitment to type I IFN promoter sequences while also reducing nuclear levels of the coactivators EP300 and CREBBP.

**Summary**, from NCBI Gene [64771](https://www.ncbi.nlm.nih.gov/gene/64771):

> This gene encodes a protein with N-terminal ubiquitin-associated (UBA)-like and central neighbor of BRCA1 gene 1 (NBR1)-like domains. The protein acts an inhibitor of antiviral and proinflammatory cytokine transcription and as a regulator of the renin-angiotensin-aldosterone system (RAAS). [provided by RefSeq, Jul 2021]

**Accessions** — [HGNC:21215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21215) · Entrez [64771](https://www.ncbi.nlm.nih.gov/gene/64771) · UniProt [Q9H6K1](https://www.uniprot.org/uniprotkb/Q9H6K1) · Ensembl [ENSG00000196821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196821)

## Data

Gene col 12289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12289); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12289]; `tensor/DDL_lfc|DDL_z.npy` [12289]; `embed/gene_vectors.npy` [12289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12289 or target_col == 12289). Every well: [[ILRUN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILRUN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
