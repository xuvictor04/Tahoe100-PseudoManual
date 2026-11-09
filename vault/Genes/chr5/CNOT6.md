---
symbol: "CNOT6"
type: "gene"
col: 3446
ensembl_id: "ENSG00000113300"
name: "CCR4-NOT transcription complex subunit 6"
location: "5q35.3"
module: 4
arm: "+"
pooled_cpm: 93.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CNOT6

*CCR4-NOT transcription complex subunit 6* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.22× (z +8.6, q 3e-15, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW48 0.260×, NCI-H460 0.393×, SHP-77 0.377×, HS-578T 0.391×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.109×, NCI-H460 0.277×, SW 900 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.377×, AsPC-1 0.403×, A-427 0.427×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (SW 1088 0.0675×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1088 0.0906×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR1A]] (+0.57, fdr 1e-05), [[KPNA1]] (+0.54, fdr 1e-05), [[GNB1]] (+0.53, fdr 2e-05); moves opposite to [[HMGCL]] (-0.55, fdr 1e-05), [[FKBP15]] (-0.52, fdr 3e-05), [[HLA-V-1]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +8.6 | 3e-15 | 40/48 (C32, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +8.4 | 1e-14 | 44/49 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.9 | 5e-07 | 27/48 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.1 | 6e-05 | 29/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +5.0 | 8e-05 | 25/48 (HT-29, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.014 | 22/48 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.015 | 18/48 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.023 | 20/48 (HT-29, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +3.5 | 0.025 | 22/48 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.034 | 18/48 (LS 180, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.049 | 20/48 (HEC-1-A, A498, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW48 0.260×, NCI-H460 0.393×, SHP-77 0.377×, HS-578T 0.391×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.109×, NCI-H460 0.277×, SW 900 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.377×, AsPC-1 0.403×, A-427 0.427×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (SW 1088 0.0675×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1088 0.0906×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -5.1 | 2e-04 | 20/49 (NCI-H1792, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 141 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +19.0) | — |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 59.7 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.11× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 65.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.0) | — |
| [[LoVo (line)]] | wt | 93.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 71.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.1) | — |
| [[SW 1088 (line)]] | alt | 80.1 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 5 µM 0.0675× (z -10.1) |
| [[A-427 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 89.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 67.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.12× (z +9.8) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 71.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0877× (z -10.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 70.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.123× (z -14.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.451× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR1A]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[KPNA1]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[GNB1]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[STK25]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ELAC2]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CSE1L]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ZNF37BP]] | +0.50 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[TFDP1]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 | pathway: TP53 Regulates Transcription of Cell Cycle Genes |
| [[DARS2]] | +0.50 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[RPRD1A]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[USP14]] | +0.49 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | -0.55 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[FKBP15]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HLA-V-1]] | -0.51 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[LPIN2]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[BTG1]] | -0.49 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[SIRT2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FUT11]] | -0.48 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[GCAT]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TMEM167B]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ZKSCAN1]] | -0.47 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[TXNL4B]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.46 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises CNOT6's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without SLC4A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.8, -33.2); signed map (-21.5, -53.2). **Vector** length 81.6, 17.6% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.7 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -3.6 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.4 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,494,379-180,578,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCR4, KIAA1194, Ccr4a |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 10 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULM6](https://www.uniprot.org/uniprotkb/Q9ULM6) (CCR4-NOT transcription complex subunit 6):

> Poly(A) nuclease with 3'-5' RNase activity. Catalytic component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Involved in mRNA decay mediated by the major-protein-coding determinant …

**Summary**, from NCBI Gene [57472](https://www.ncbi.nlm.nih.gov/gene/57472):

> This gene encodes the catalytic component of the CCR4-NOT core transcriptional regulation complex. The encoded protein has a 3'-5' RNase activity and prefers polyadenylated substrates. The CCR4-NOT complex plays a role in many cellular processes, including miRNA-mediated repression, mRNA degradation, and transcriptional regulation. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:14099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14099) · Entrez [57472](https://www.ncbi.nlm.nih.gov/gene/57472) · UniProt [Q9ULM6](https://www.uniprot.org/uniprotkb/Q9ULM6) · Ensembl [ENSG00000113300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113300)

## Data

Gene col 3446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3446); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3446]; `tensor/DDL_lfc|DDL_z.npy` [3446]; `embed/gene_vectors.npy` [3446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3446 or target_col == 3446). Every well: [[CNOT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
