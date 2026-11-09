---
symbol: "PAWR"
type: "gene"
col: 10820
ensembl_id: "ENSG00000177425"
name: "pro-apoptotic WT1 regulator"
location: "12q21.2"
module: 40
arm: "-"
pooled_cpm: 183.92
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PAWR

*pro-apoptotic WT1 regulator* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +20.8, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.671× (z -10.4, q 1e-22, down in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 9 lines (HepG2/C3A 0.236×, SW480 0.501×, HT-29 0.419×, LS 180 0.400×, …); [[Panobinostat (drug)]] 0.5 µM in 6 lines (HepG2/C3A 0.270×, LS 180 0.414×, HT-29 0.451×, SW480 0.554×, …); [[Belinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.287×; ⚠ cell-cycle shift, explains ~65% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENAH]] (+0.58, fdr 1e-05), [[GALNT7]] (+0.55, fdr 3e-05), [[CCDC50]] (+0.53, fdr 7e-05); moves opposite to [[DIABLO]] (-0.51, fdr 3e-05), [[NAA80]] (-0.50, fdr 6e-05), [[HAUS3]] (-0.49, fdr 1e-04).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +20.8 | 0e+00 | 39/46 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +17.6 | 0e+00 | 42/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +14.8 | 0e+00 | 45/47 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +14.3 | 4e-44 | 41/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +13.0 | 2e-36 | 32/43 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +12.7 | 4e-35 | 38/46 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +11.7 | 1e-29 | 41/46 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +11.1 | 1e-26 | 34/46 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +10.8 | 3e-25 | 38/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +10.6 | 2e-24 | 30/47 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +10.4 | 1e-23 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +9.9 | 3e-21 | 36/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +9.5 | 6e-20 | 35/46 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +9.5 | 7e-20 | 39/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +8.7 | 2e-16 | 34/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +7.6 | 1e-12 | 24/47 (C32, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +6.5 | 3e-09 | 26/46 (C32, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 3e-05 | 23/46 (C32, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 3e-05 | 24/47 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 9 lines (HepG2/C3A 0.236×, SW480 0.501×, HT-29 0.419×, LS 180 0.400×, …); [[Panobinostat (drug)]] 0.5 µM in 6 lines (HepG2/C3A 0.270×, LS 180 0.414×, HT-29 0.451×, SW480 0.554×, …); [[Belinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.287×; ⚠ cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.671×** | -10.4 | 1e-22 | 31/46 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -9.3 | 4e-18 | 32/46 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.863× | -3.8 | 0.025 | 16/45 (NCI-H23, J82, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.0 | 0.25 | 13/45 (J82, NCI-H2030, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.891× | -3.0 | 0.25 | 8/46 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 158 | 16 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.05× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.73× (z +13.6) | — |
| [[A549 (line)]] | wt | 182 | 11 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +25.9) | [[Panobinostat (drug)]] 5 µM 0.467× (z -10.4) |
| [[PANC-1 (line)]] | alt | 219 | 13 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.86× (z +19.4) | — |
| [[SW480 (line)]] | alt | 187 | 11 (5 ⚠) | 2 | [[Digitoxin (drug)]] 0.5 µM 2.41× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.501× (z -12.8) |
| [[H4 (line)]] | wt | 118 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.1) | — |
| [[KATO III (line)]] | alt | 134 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.505× (z -9.9) |
| [[LS 180 (line)]] | wt | 197 | 6 (2 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.400× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 190 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +15.6) | — |
| [[BT-474 (line)]] | alt | 465 | 4 (1 ⚠) | 3 (2 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 2.76× (z +12.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Afatinib (drug)]] 0.5 µM 1.84× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.427× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.478× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 212 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.520× (z -10.6) |
| [[HT-29 (line)]] | alt | 270 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.419× (z -12.0) |
| [[LoVo (line)]] | wt | 198 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.43× (z +20.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +17.6) | — |
| [[HEC-1-A (line)]] | alt | 224 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 591 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -16.7) |
| [[NCI-H2030 (line)]] | alt | 347 | 3 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.459× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 113 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.8) | — |
| [[C32 (line)]] | wt | 66.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 132 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.07× (z +13.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 84.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 164 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -8.7) |
| [[RKO (line)]] | wt | 254 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 3.48× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.551× (z -9.7) |
| [[SNU-423 (line)]] | alt | 258 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.7) | — |
| [[SW48 (line)]] | wt | 153 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.40× (z +9.8) | — |
| [[A-172 (line)]] | wt | 105 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.7) | — |
| [[A-427 (line)]] | wt | 157 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 133 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.4) | — |
| [[J82 (line)]] | alt | 208 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.48× (z +12.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.8) | — |
| [[SW1417 (line)]] | alt | 237 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.6) | — |
| [[A498 (line)]] | wt | 171 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 87.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 246 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.9) | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 2 | — | [[(S)-Crizotinib (drug)]] 0.5 µM 0.0713× (z -8.8) |
| [[SW 900 (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.96× (z +11.8) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.84× (z +12.5) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 81.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.15× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 160 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 162 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 302 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENAH]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GALNT7]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CCDC50]] | +0.53 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[SHTN1]] | +0.53 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PARD3B]] | +0.53 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[USP46]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BEND7]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[VSIG10]] | +0.52 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[ZNF326]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[NFIB]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RUFY3]] | +0.50 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[SBDSP1]] | +0.50 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIABLO]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[NAA80]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[HAUS3]] | -0.49 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ATAT1]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[MEA1]] | -0.48 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[SEC16A]] | -0.48 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[RCOR1]] | -0.48 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CYBA]] | -0.48 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ZBTB48]] | -0.46 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[ZKSCAN5]] | -0.46 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[MAP1S]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[PDCD6]] | -0.45 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.270). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-11.0, 11.3); signed map (25.8, -34.5). **Vector** length 110, 36.2% of its response variance represented; |z| ≥ 3 in 1,493 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +17.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.9 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.1 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.8 | -10.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.8 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.8 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Pimitespib (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | pro-apoptotic WT1 regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:79,574,979-79,690,964 (-) |
| Ensembl biotype | protein_coding |
| Also known as | par-4, PAR4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IZ0](https://www.uniprot.org/uniprotkb/Q96IZ0) (PRKC apoptosis WT1 regulator protein):

> Pro-apoptotic protein capable of selectively inducing apoptosis in cancer cells, sensitizing the cells to diverse apoptotic stimuli and causing regression of tumors in animal models. Induces apoptosis in certain cancer cells by activation of the Fas prodeath pathway and coparallel inhibition of NF-kappa-B transcriptional activity. Inhibits the transcriptional activation and augments the transcriptional repression mediated by WT1. Down-regulates the anti-apoptotic protein BCL2 via its …

**Summary**, from NCBI Gene [5074](https://www.ncbi.nlm.nih.gov/gene/5074):

> This gene encodes a tumor suppressor protein that selectively induces apoptosis in cancer cells through intracellular and extracellular mechanisms. The intracellular mechanism involves the inhibition of pro-survival pathways and the activation of Fas-mediated apoptosis, while the extracellular mechanism involves the binding of a secreted form of this protein to glucose regulated protein 78 (GRP78) on the cell surface, which leads to activation of the extrinsic apoptotic pathway. This gene is …

**Accessions** — [HGNC:8614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8614) · Entrez [5074](https://www.ncbi.nlm.nih.gov/gene/5074) · UniProt [Q96IZ0](https://www.uniprot.org/uniprotkb/Q96IZ0) · Ensembl [ENSG00000177425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177425)

## Data

Gene col 10820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10820); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10820]; `tensor/DDL_lfc|DDL_z.npy` [10820]; `embed/gene_vectors.npy` [10820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10820 or target_col == 10820). Every well: [[PAWR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAWR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
