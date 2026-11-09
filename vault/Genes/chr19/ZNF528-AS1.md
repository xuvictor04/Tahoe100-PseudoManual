---
symbol: "ZNF528-AS1"
type: "gene"
col: 15639
ensembl_id: "ENSG00000269834"
name: "ZNF528 antisense RNA 1"
location: "19q13.41"
module: 15
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 28
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZNF528-AS1

*ZNF528 antisense RNA 1* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.66× (z +7.6, q 2e-11, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.75× (z +6.4, q 6e-08, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.461× (z -8.9, q 4e-16, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF737]] (+0.66, fdr 7e-06), [[INTS4P1]] (+0.62, fdr 1e-05), [[NGDN]] (+0.61, fdr 6e-05); moves opposite to [[POLR2E]] (-0.54, fdr 5e-04), [[EFHD2]] (-0.46, fdr 2e-04), [[NAB1]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF665]] → it (grade C ⚠); 7 go from it, the strongest it → [[ZNF585B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +7.6 | 2e-11 | 5/12 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +6.4 | 6e-08 | 20/26 (J82, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +4.6 | 7e-04 | 15/25 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 7e-04 | 13/24 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.5 | 7e-04 | 10/23 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.2 | 0.12 | 4/22 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.46× | +3.1 | 0.18 | 12/25 (H4, J82, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -8.9 | 4e-16 | 21/25 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -6.1 | 4e-07 | 20/26 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -5.7 | 2e-06 | 14/25 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.541×** | -5.0 | 9e-05 | 16/24 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -4.7 | 3e-04 | 16/25 (PANC-1, SNU-423, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -4.4 | 0.001 | 15/25 (SK-MEL-2, AN3 CA, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -4.2 | 0.002 | 15/25 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -3.9 | 0.008 | 12/25 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.641×** | -3.6 | 0.019 | 13/26 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.648×** | -3.5 | 0.024 | 12/25 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.657×** | -3.1 | 0.085 | 7/25 (BT-474, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.157× (z -10.1) |
| [[HOP62 (line)]] | alt | 6.78 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.5) |
| [[PANC-1 (line)]] | alt | 9.27 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.7) |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0764× (z -9.9) |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.2) |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -11.8) |
| [[J82 (line)]] | alt | 45.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.8) |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.8) |
| [[A-172 (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.561 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF737]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[INTS4P1]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NGDN]] | +0.61 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[ZNF493]] | +0.60 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[SREK1IP1]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZNF358]] | +0.57 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[ZNF529-AS1]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 | same gene group |
| [[PGLS-DT]] | +0.57 | +0.21 / +0.61 | both halves | 7e-04 |  |
| [[COA6]] | +0.56 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[TAF11]] | +0.56 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[PCF11-AS1]] | +0.56 | +0.36 / +0.55 | both halves | 1e-04 | same gene group |
| [[DYNLT2]] | +0.55 | +0.39 / +0.42 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | -0.54 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[EFHD2]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[NAB1]] | -0.46 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TRAF7]] | -0.46 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[AKAP11]] | -0.45 | -0.23 / -0.57 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF665]] | C | ZNF665 activity raises ZNF528-AS1's level | lines that do not express ZNF665 (24) vs lines expressing it (26) | 3.94× lower at baseline in the lines without ZNF665 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF818P, ZNF347; co-absent with the target |
| [[ZNF626]] | C | ZNF626 activity raises ZNF528-AS1's level | lines that do not express ZNF626 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without ZNF626 | 0.038 | ⚠ within organs, on part of the lines; also absent: ROS1, GDNF, HTRA3; co-absent with the target |
| [[ZNF737]] | C | ZNF737 activity raises ZNF528-AS1's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 3.50× lower at baseline in the lines without ZNF737 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF585B]] | B | ZNF528-AS1 activity raises ZNF585B's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without ZNF528-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880 |
| [[ZNF493]] | B | ZNF528-AS1 activity raises ZNF493's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without ZNF528-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880 |
| [[ZKSCAN7-AS1]] | B | ZNF528-AS1 activity raises ZKSCAN7-AS1's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without ZNF528-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880 |
| [[ZNF626]] | C | ZNF528-AS1 activity raises ZNF626's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 3.76× lower at baseline in the lines without ZNF528-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880; co-absent with the target |
| [[ZNF813]] | C | ZNF528-AS1 activity raises ZNF813's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without ZNF528-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880; co-absent with the target |
| [[ZNF665]] | C | ZNF528-AS1 activity raises ZNF665's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without ZNF528-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880; co-absent with the target |
| [[ZNF345]] | C | ZNF528-AS1 activity raises ZNF345's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 3.39× lower at baseline in the lines without ZNF528-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.8, 25.4); signed map (-1.3, -1.6). **Vector** length 43.8, 8.33% of its response variance represented; |z| ≥ 3 in 505 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.5 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -0.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.7 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ZNF528 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.41 — chr19:52,388,836-52,397,791 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51305) · Entrez [102724105](https://www.ncbi.nlm.nih.gov/gene/102724105) · Ensembl [ENSG00000269834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269834)

## Data

Gene col 15639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15639); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15639]; `tensor/DDL_lfc|DDL_z.npy` [15639]; `embed/gene_vectors.npy` [15639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15639 or target_col == 15639). Every well: [[ZNF528-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF528-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
