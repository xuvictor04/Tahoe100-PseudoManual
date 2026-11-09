---
symbol: "PNO1"
type: "gene"
col: 3741
ensembl_id: "ENSG00000115946"
name: "partner of NOB1 homolog"
location: "2p14"
module: 5
arm: "+"
pooled_cpm: 33.15
n_lines_expressing: 50
n_dd_up: 51
n_dd_down: 12
n_dd_up_clean: 26
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PNO1

*partner of NOB1 homolog* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (25 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.44× (z +18.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.678× (z -5.7, q 7e-06, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.80, fdr 7e-06), [[PUM3]] (+0.80, fdr 7e-06), [[PUS1]] (+0.79, fdr 7e-06); moves opposite to [[ELF2]] (-0.65, fdr 7e-06), [[AAMDC]] (-0.65, fdr 1e-05), [[PLEKHH3]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSF2BP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 25 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.44×** | +18.0 | 0e+00 | 44/48 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.21×** | +16.3 | 0e+00 | 40/48 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.59×** | +13.8 | 4e-41 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.53×** | +13.5 | 2e-39 | 45/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.44×** | +13.0 | 3e-36 | 45/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.52×** | +12.9 | 3e-36 | 43/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +11.2 | 2e-27 | 45/48 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.31×** | +11.2 | 2e-27 | 40/43 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +11.0 | 1e-26 | 40/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **2.00×** | +10.1 | 4e-22 | 35/45 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.97×** | +9.9 | 3e-21 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.65×** | +9.8 | 4e-21 | 38/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.94×** | +9.6 | 2e-20 | 38/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +9.5 | 1e-19 | 37/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +9.0 | 9e-18 | 40/46 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +8.8 | 6e-17 | 40/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.48×** | +6.9 | 1e-10 | 36/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +6.8 | 4e-10 | 32/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.32×** | +6.4 | 4e-09 | 32/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.16×** | +5.9 | 1e-07 | 32/47 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +5.2 | 5e-06 | 26/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 5e-05 | 22/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.81×** | +4.5 | 1e-04 | 25/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.81×** | +4.5 | 1e-04 | 22/45 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.78×** | +4.4 | 2e-04 | 22/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.678×** | -5.7 | 7e-06 | 28/48 (LoVo, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.795×** | -4.6 | 1e-03 | 24/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.733×** | -4.5 | 0.001 | 25/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.727×** | -4.5 | 0.001 | 21/47 (A-427, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -4.0 | 0.007 | 18/48 (A498, CHP-212, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.751×** | -3.9 | 0.010 | 19/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.015 | 18/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.631×** | -3.5 | 0.031 | 12/47 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.067 | 12/48 (KATO III, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.803×** | -3.2 | 0.067 | 15/47 (LoVo, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.803×** | -3.2 | 0.067 | 16/48 (MIA PaCa-2, SW 1088, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.067 | 12/48 (COLO 205, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.836× | -3.2 | 0.067 | 12/48 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.800× | -3.0 | 0.10 | 12/48 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.815× | -3.0 | 0.10 | 12/47 (A-172, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.3 | 12 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.48× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.51× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 63.2 | 12 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +13.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 9 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.76× (z +11.4) | [[Adagrasib (drug)]] 0.05 µM 0.610× (z -12.5) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 26.3 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.83× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 7 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.23× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.54× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 19.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.95× (z +12.9) | — |
| [[A-172 (line)]] | wt | 19.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +10.1) | — |
| [[A549 (line)]] | wt | 38.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +11.4) | — |
| [[SW480 (line)]] | alt | 35.1 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.27× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 42.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.16× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 34.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.79× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.49× (z +13.2) | — |
| [[H4 (line)]] | wt | 27.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.13× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 15.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.40× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 17.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.41× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 66.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +13.7) | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 13.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 43.1 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.93× (z +9.5) ⚠ unreliable plate only | [[Verteporfin (drug)]] 5 µM 0.364× (z -8.7) |
| [[COLO 205 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.12× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | STRING 422 |
| [[PUM3]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 665 |
| [[PUS1]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[NOLC1]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | STRING 772 |
| [[MAK16]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | STRING 705 |
| [[POLR1A]] | +0.78 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[BYSL]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[LTV1]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[DDX21]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 618 |
| [[UTP14A]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 996 |
| [[NOL6]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 980 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF2]] | -0.65 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.65 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.64 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.64 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.63 | -0.66 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSF2BP]] | C | HSF2BP activity raises PNO1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without HSF2BP | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, -35.9); signed map (-1.8, -45.8). **Vector** length 82.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,575 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.68 to 13); *ribosome biogenesis* (control, mean cos +0.63 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.60 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +13.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +5.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.5 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -5.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | partner of NOB1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:68,157,888-68,176,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RRP20; previously KHRBP1 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRX1](https://www.uniprot.org/uniprotkb/Q9NRX1) (RNA-binding protein PNO1):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Positively regulates dimethylation of two adjacent adenosines in …

**Summary**, from NCBI Gene [56902](https://www.ncbi.nlm.nih.gov/gene/56902):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32790) · Entrez [56902](https://www.ncbi.nlm.nih.gov/gene/56902) · UniProt [Q9NRX1](https://www.uniprot.org/uniprotkb/Q9NRX1) · Ensembl [ENSG00000115946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115946)

## Data

Gene col 3741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3741); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3741]; `tensor/DDL_lfc|DDL_z.npy` [3741]; `embed/gene_vectors.npy` [3741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3741 or target_col == 3741). Every well: [[PNO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
