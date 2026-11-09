---
symbol: "INTS13"
type: "gene"
col: 737
ensembl_id: "ENSG00000064102"
name: "integrator complex subunit 13"
location: "12p11.23"
module: 134
arm: "+"
pooled_cpm: 86.35
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# INTS13

*integrator complex subunit 13* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.66× (z +11.1, q 5e-26, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.37× (z +6.8, q 1e-09, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -13.6, q 2e-39, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFB1M]] (+0.68, fdr 1e-05), [[CABIN1]] (+0.62, fdr 2e-05), [[MRPL17]] (+0.61, fdr 3e-05); moves opposite to [[POU6F1]] (-0.58, fdr 1e-04), [[KLF3-AS1]] (-0.56, fdr 1e-04), [[SETD1B]] (-0.56, fdr 1e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.66×** | +11.1 | 5e-26 | 42/48 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.61×** | +10.4 | 5e-23 | 41/48 (A-172, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.58×** | +10.0 | 2e-21 | 40/48 (A-172, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.8 | 1e-09 | 37/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 1e-08 | 28/48 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.8 | 6e-07 | 30/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +5.1 | 2e-05 | 29/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.1 | 2e-05 | 26/47 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.18× | +5.1 | 2e-05 | 22/48 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +4.5 | 4e-04 | 25/48 (NCI-H2347, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +4.4 | 5e-04 | 20/48 (A-172, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +4.2 | 0.001 | 22/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +3.9 | 0.004 | 22/48 (SW480, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 12/49 (SW480, HOP62, …) | top dose only | plate-row cell shift |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.007 | 16/49 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.023 | 12/49 (A498, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.023 | 16/48 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.037 | 13/48 (NCI-H2347, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.037 | 11/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.040 | 17/48 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.071 | 17/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -13.6 | 2e-39 | 41/49 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -5.3 | 3e-05 | 31/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -4.5 | 0.001 | 17/48 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.871× | -4.3 | 0.002 | 12/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.832×** | -4.1 | 0.006 | 19/48 (MIA PaCa-2, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.708×** | -4.0 | 0.007 | 20/49 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.820×** | -3.8 | 0.014 | 19/48 (C32, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.4 | 0.040 | 15/48 (RKO, BT-474, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -3.4 | 0.040 | 20/45 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.040 | 17/50 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.858× | -3.3 | 0.056 | 19/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.2 | 0.056 | 21/50 (C32, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 131 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -23.1) |
| [[SW480 (line)]] | alt | 195 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.10× (z +13.3) | — |
| [[A-172 (line)]] | wt | 45.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 75.0 | 0 | 2 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.113× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.5) |
| [[A498 (line)]] | wt | 37.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 63.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.0) |
| [[HOP62 (line)]] | alt | 126 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.27× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 51.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.35× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 61.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.16× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 62.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.12× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 175 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 58.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.3) |
| [[PANC-1 (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -10.2) |
| [[RKO (line)]] | wt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.9) |
| [[SNU-1 (line)]] | wt | 88.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.456× (z -9.0) |
| [[SNU-423 (line)]] | alt | 59.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.5) |
| [[A-427 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFB1M]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.62 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MRPL17]] | +0.61 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[TBC1D9B]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[FAM234B]] | +0.58 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[YEATS2]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CRYBG3]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PHF6]] | +0.57 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SLX9]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SMYD3]] | +0.56 | +0.32 / +0.35 | both halves | 2e-04 |  |
| [[RALGAPA2]] | +0.56 | +0.32 / +0.41 | both halves | 2e-04 |  |
| [[CEP290]] | +0.56 | +0.37 / +0.49 | both halves | 8e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU6F1]] | -0.58 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[KLF3-AS1]] | -0.56 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[SETD1B]] | -0.56 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[GATA2-AS1]] | -0.56 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.55 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[SLC25A53]] | -0.54 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ZNF213-AS1]] | -0.53 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[YPEL5]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[RUSC1-AS1]] | -0.53 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[MED28-DT]] | -0.52 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[SEC24B-AS1]] | -0.51 | -0.35 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises INTS13's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without FAM216A | 0.056 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[MED21]] | C | MED21's natural level strengthens INTS13's drug response | MED21's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.13; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.2, -13.5); signed map (-38.2, 25.9). **Vector** length 129, 36.7% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.9 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.4 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.3 | +10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.7 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.9 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:26,905,181-26,938,326 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10637, NET48, Mat89Bb, SPATA30; previously C12orf11, ASUN |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVM9](https://www.uniprot.org/uniprotkb/Q9NVM9) (Integrator complex subunit 13):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [55726](https://www.ncbi.nlm.nih.gov/gene/55726):

> Enables DNA-binding transcription factor binding activity. Involved in RNA metabolic process; regulation of mitotic cell cycle; and regulation of transcription elongation by RNA polymerase II. Acts upstream of or within centrosome localization; mitotic spindle organization; and protein localization to nuclear envelope. Located in cytoplasm and nuclear body. Part of INTAC complex and integrator complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20174) · Entrez [55726](https://www.ncbi.nlm.nih.gov/gene/55726) · UniProt [Q9NVM9](https://www.uniprot.org/uniprotkb/Q9NVM9) · Ensembl [ENSG00000064102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064102)

## Data

Gene col 737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 737); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 737]; `tensor/DDL_lfc|DDL_z.npy` [737]; `embed/gene_vectors.npy` [737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 737 or target_col == 737). Every well: [[INTS13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
