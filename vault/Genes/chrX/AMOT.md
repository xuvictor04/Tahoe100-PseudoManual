---
symbol: "AMOT"
type: "gene"
col: 4710
ensembl_id: "ENSG00000126016"
name: "angiomotin"
location: "Xq23"
module: 44
arm: "+"
pooled_cpm: 7.8
n_lines_expressing: 38
n_dd_up: 30
n_dd_down: 23
n_dd_up_clean: 26
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 13
direction_downstream: 6
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AMOT

*angiomotin* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.29× (z +13.4, q 3e-38, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.490× (z -8.2, q 1e-13, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXADR]] (+0.67, fdr 3e-05), [[CGN]] (+0.67, fdr 7e-06), [[ELAPOR2]] (+0.64, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.67, fdr 1e-05), [[ANKMY1]] (-0.63, fdr 1e-05), [[MEF2B]] (-0.61, fdr 5e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SLC7A8]] → it (grade B ⚠); 6 go from it, the strongest it → [[PADI2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +13.4 | 3e-38 | 27/36 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.40×** | +10.0 | 4e-21 | 24/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +9.0 | 5e-17 | 18/33 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +8.0 | 2e-13 | 23/35 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.99×** | +7.6 | 4e-12 | 22/34 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +7.3 | 2e-11 | 17/35 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +6.4 | 1e-08 | 18/35 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.8 | 4e-07 | 5/11 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +5.8 | 4e-07 | 16/35 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.63×** | +5.8 | 4e-07 | 19/36 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 8e-06 | 14/36 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.51×** | +5.2 | 9e-06 | 16/36 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +5.1 | 2e-05 | 16/34 (BT-474, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.52×** | +5.0 | 3e-05 | 13/36 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 3e-05 | 15/36 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.57×** | +4.8 | 5e-05 | 15/35 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.490×** | -8.2 | 1e-13 | 23/34 (COLO 205, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -7.9 | 7e-13 | 19/35 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -7.0 | 4e-10 | 21/34 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -6.3 | 5e-08 | 20/35 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -6.1 | 9e-08 | 17/34 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.7 | 1e-06 | 18/32 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -5.2 | 2e-05 | 19/35 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.646×** | -5.0 | 3e-05 | 14/35 (C32, C-33 A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.647×** | -4.8 | 8e-05 | 14/34 (Panc 03.27, SNU-423, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.745×** | -4.8 | 8e-05 | 14/36 (C32, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -4.6 | 3e-04 | 12/32 (SK-MEL-2, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -4.4 | 5e-04 | 16/35 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.772×** | -4.2 | 9e-04 | 14/33 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.006 | 12/35 (SW480, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.4 | 0.022 | 11/31 (COLO 205, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.750×** | -3.3 | 0.032 | 9/33 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.037 | 4/35 (C32, SNU-423, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.584×** | -3.2 | 0.037 | 14/35 (COLO 205, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0581× (z -14.0) |
| [[PANC-1 (line)]] | alt | 9.12 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.187× (z -10.9) |
| [[C32 (line)]] | wt | 35.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.183× (z -9.2) |
| [[SW480 (line)]] | alt | 13.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0793× (z -9.2) |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.105× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 9.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[LoVo (line)]] | wt | 4.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.52 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0817× (z -9.1) |
| [[SW 900 (line)]] | alt | 6.20 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0792× (z -8.9) |
| [[SW1417 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.5) | — |
| [[A-172 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | +0.67 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[CGN]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 | STRING 475 |
| [[ELAPOR2]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MPP7]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 | same gene group; STRING 570 |
| [[TBL1XR1]] | +0.60 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ECH1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.59 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[MAPRE2]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PPFIBP2]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ZNF608]] | +0.58 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[BCOR]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[RAB30]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.67 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[ANKMY1]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[MEF2B]] | -0.61 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[SENP5]] | -0.59 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[TRAPPC12]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PPP1R26-AS1]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[MOSMO]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ARPC5L]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[MIATNB]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ZNF778]] | -0.56 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[TIMM23B-AGAP6]] | -0.55 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A8]] | B | SLC7A8 activity raises AMOT's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without SLC7A8 | 0.009 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[VWA5A]] | B | VWA5A activity raises AMOT's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without VWA5A | 0.042 | ⚠ within organs, on part of the lines |
| [[NTRK2]] | B | NTRK2 activity raises AMOT's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without NTRK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent |
| [[KSR2]] | B | KSR2 activity raises AMOT's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without KSR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[DGAT2]] | B | DGAT2 activity raises AMOT's level | lines that do not express DGAT2 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without DGAT2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CA8]] | B | CA8 activity raises AMOT's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without CA8 | 0.072 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[PADI2]] | B | PADI2 activity raises AMOT's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without PADI2 | 0.084 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[POTEF]] | B | POTEF activity raises AMOT's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.60× lower at baseline in the lines without POTEF | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises AMOT's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 3.44× lower at baseline in the lines without ZDHHC11B | 0.087 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[CXADR]] | B | CXADR activity raises AMOT's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without CXADR | 0.093 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers AMOT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[QPRT]] | B | QPRT activity raises AMOT's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.93× lower at baseline in the lines without QPRT | 0.095 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PADI2]] | B | AMOT activity raises PADI2's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without AMOT | 0.016 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[TIRAP]] | B | AMOT activity raises TIRAP's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without AMOT | 0.040 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[CXADR]] | B | AMOT activity raises CXADR's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.79× lower at baseline in the lines without AMOT | 0.048 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[PRR14L]] | B | AMOT activity raises PRR14L's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without AMOT | 0.079 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[ZDHHC11B]] | B | AMOT activity raises ZDHHC11B's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without AMOT | 0.096 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[COMMD8]] | B | AMOT activity raises COMMD8's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without AMOT | 0.099 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 1.3); signed map (49.0, 5.3). **Vector** length 73.7, 14.7% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +4.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | angiomotin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:112,774,503-112,840,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1071 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 9 pathways, smallest: Regulation of CDH11 function; Signaling by Hippo; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4VCS5](https://www.uniprot.org/uniprotkb/Q4VCS5) (Angiomotin):

> Plays a central role in tight junction maintenance via the complex formed with ARHGAP17, which acts by regulating the uptake of polarity proteins at tight junctions. Appears to regulate endothelial cell migration and tube formation. May also play a role in the assembly of endothelial cell-cell junctions. Repressor of YAP1 and WWTR1/TAZ transcription of target genes, potentially via regulation of Hippo signaling-mediated phosphorylation of YAP1 which results in its recruitment to tight junctions.

**Summary**, from NCBI Gene [154796](https://www.ncbi.nlm.nih.gov/gene/154796):

> This gene belongs to the motin family of angiostatin binding proteins characterized by conserved coiled-coil domains and C-terminal PDZ binding motifs. The encoded protein is expressed predominantly in endothelial cells of capillaries as well as larger vessels of the placenta where it may mediate the inhibitory effect of angiostatin on tube formation and the migration of endothelial cells toward growth factors during the formation of new blood vessels. Alternative splicing results in multiple …

**Accessions** — [HGNC:17810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17810) · Entrez [154796](https://www.ncbi.nlm.nih.gov/gene/154796) · UniProt [Q4VCS5](https://www.uniprot.org/uniprotkb/Q4VCS5) · Ensembl [ENSG00000126016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126016)

## Data

Gene col 4710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4710); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4710]; `tensor/DDL_lfc|DDL_z.npy` [4710]; `embed/gene_vectors.npy` [4710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4710 or target_col == 4710). Every well: [[AMOT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMOT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
