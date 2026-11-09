---
symbol: "RAD18"
type: "gene"
col: 971
ensembl_id: "ENSG00000070950"
name: "RAD18 E3 ubiquitin protein ligase"
location: "3p25.3"
module: 6
arm: "+"
pooled_cpm: 77.87
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RAD18

*RAD18 E3 ubiquitin protein ligase* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.30× (z +21.1, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.02× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.769× (z -7.1, q 6e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFC3]] (+0.75, fdr 7e-06), [[FANCD2]] (+0.75, fdr 7e-06), [[TOPBP1]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +21.1 | 0e+00 | 44/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +13.4 | 2e-38 | 44/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +11.9 | 2e-30 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.8 | 3e-16 | 30/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +7.9 | 4e-13 | 40/49 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +7.1 | 9e-11 | 36/48 (LoVo, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.35×** | +5.7 | 8e-07 | 36/48 (LoVo, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.35×** | +5.7 | 1e-06 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.3 | 7e-06 | 27/38 (SK-MEL-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +5.3 | 7e-06 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.32×** | +5.0 | 3e-05 | 27/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.28×** | +4.7 | 1e-04 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 23/48 (PANC-1, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.24×** | +4.0 | 0.003 | 27/48 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +3.6 | 0.011 | 23/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.012 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.030 | 20/48 (LoVo, SW480, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.043 | 16/49 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.100 | 9/48 (NCI-H2347, SW48, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -7.1 | 6e-10 | 37/48 (C32, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.788×** | -6.5 | 3e-08 | 29/48 (C32, A-172, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -6.2 | 1e-07 | 29/49 (SNU-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.755×** | -5.4 | 1e-05 | 30/48 (C32, HS-578T, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.787×** | -4.6 | 4e-04 | 26/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.786×** | -4.4 | 9e-04 | 22/44 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.816×** | -3.9 | 0.007 | 24/48 (A-172, C32, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.830×** | -3.6 | 0.023 | 23/48 (COLO 205, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.037 | 17/48 (HCT15, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.840× | -3.4 | 0.041 | 17/48 (KATO III, SHP-77, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.041 | 19/47 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.844× | -3.3 | 0.050 | 19/49 (SNU-1, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.789×** | -3.3 | 0.050 | 18/48 (SW48, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.841× | -3.2 | 0.052 | 13/47 (LS 180, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.2 | 0.052 | 19/49 (A-427, COLO 205, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 53.3 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +23.0) | — |
| [[NCI-H460 (line)]] | wt | 65.3 | 9 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 8.62× (z +22.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.0) |
| [[LoVo (line)]] | wt | 45.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.40× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 235 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0667× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.5) |
| [[A-172 (line)]] | wt | 95.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.475× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 69.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.46× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -12.1) |
| [[C32 (line)]] | wt | 102 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.10× (z +15.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.382× (z -14.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.503× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 86.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.87× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.13× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 77.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +21.7) | — |
| [[NCI-H2030 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 90.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.43× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.5) | — |
| [[SW48 (line)]] | wt | 79.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.6) | — |
| [[SW480 (line)]] | alt | 79.8 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +16.1) | — |
| [[A-427 (line)]] | wt | 69.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.99× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 80.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.33× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 84.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.42× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.32× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 87.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 35.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.00× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.55× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.87× (z +9.9) | — |
| [[NCI-H661 (line)]] | alt | 84.2 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0714× (z -12.2) |
| [[SHP-77 (line)]] | alt | 82.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.29× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.43× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 50.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.99× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 71.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.87× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 65.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.57× (z +14.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +9.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 90.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.15× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 86.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 62.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 61.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.64× (z +9.9) | — |
| [[RKO (line)]] | wt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.57× (z +15.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFC3]] | +0.75 | +0.70 / +0.78 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 761 |
| [[FANCD2]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 | STRING 939 |
| [[TOPBP1]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | STRING 528 |
| [[CENPK]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NCAPG2]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[WDR76]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FANCI]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | STRING 754 |
| [[MYBL2]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RRM1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | same gene group; STRING 895 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.9, -46.1); signed map (-40.0, -46.4). **Vector** length 116, 34.7% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.53 to 65); *DNA strand elongation* (reactome, mean cos +0.56 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +21.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.3 | +7.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Acetohexamide (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.1 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.0 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAD18 E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:8,775,402-8,963,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF73 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers UBZ4 CCHC-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; DNA Damage Bypass; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS91](https://www.uniprot.org/uniprotkb/Q9NS91) (E3 ubiquitin-protein ligase RAD18):

> E3 ubiquitin-protein ligase involved in postreplication repair of UV-damaged DNA. Postreplication repair functions in gap-filling of a daughter strand on replication of damaged DNA. Associates to the E2 ubiquitin conjugating enzyme UBE2B to form the UBE2B-RAD18 ubiquitin ligase complex involved in mono-ubiquitination of DNA-associated PCNA on 'Lys-164'. Has ssDNA binding activity.

**Summary**, from NCBI Gene [56852](https://www.ncbi.nlm.nih.gov/gene/56852):

> The protein encoded by this gene is highly similar to S. cerevisiae DNA damage repair protein Rad18. Yeast Rad18 functions through its interaction with Rad6, which is an ubiquitin-conjugating enzyme required for post-replication repair of damaged DNA. Similar to its yeast counterpart, this protein is able to interact with the human homolog of yeast Rad6 protein through a conserved ring-finger motif. Mutation of this motif results in defective replication of UV-damaged DNA and hypersensitivity …

**Accessions** — [HGNC:18278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18278) · Entrez [56852](https://www.ncbi.nlm.nih.gov/gene/56852) · UniProt [Q9NS91](https://www.uniprot.org/uniprotkb/Q9NS91) · Ensembl [ENSG00000070950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070950)

## Data

Gene col 971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 971); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 971]; `tensor/DDL_lfc|DDL_z.npy` [971]; `embed/gene_vectors.npy` [971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 971 or target_col == 971). Every well: [[RAD18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
