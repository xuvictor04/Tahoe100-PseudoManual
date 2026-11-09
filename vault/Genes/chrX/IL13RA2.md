---
symbol: "IL13RA2"
type: "gene"
col: 4439
ensembl_id: "ENSG00000123496"
name: "interleukin 13 receptor subunit alpha 2"
location: "Xq23"
module: 81
arm: "+"
pooled_cpm: 10.09
n_lines_expressing: 14
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# IL13RA2

*interleukin 13 receptor subunit alpha 2* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.59× (z +12.3, q 9e-32, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +5.2, q 2e-05, up in 8 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 3.23×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.208×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.340×; ⚠ position not correctable); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.229×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFPI2]] (+0.62, fdr 1e-05), [[LAMA1]] (+0.61, fdr 1e-05), [[BCL2A1]] (+0.60, fdr 1e-05); moves opposite to [[RNF115]] (-0.48, fdr 3e-05), [[ZNF793]] (-0.45, fdr 2e-04), [[RBM5]] (-0.43, fdr 2e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADTRP]] → it (grade C ⚠); 14 go from it, the strongest it → [[DELEC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 3.23×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.59×** | +12.3 | 9e-32 | 6/8 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +10.2 | 4e-22 | 7/10 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +6.7 | 4e-09 | 7/9 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +5.6 | 4e-06 | 8/12 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +5.2 | 2e-05 | 8/12 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.7 | 2e-04 | 3/10 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.94×** | +4.2 | 0.002 | 3/8 (A-172, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.013 | 5/12 (LOX-IMVI, A-172, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.87×** | +3.3 | 0.058 | 2/11 (Hs 766T, SK-MEL-2) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.33× | +3.0 | 0.13 | 1/12 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.208×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.340×; ⚠ position not correctable); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.229×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.597× | -3.5 | 0.13 | 3/12 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.622× | -3.5 | 0.13 | 8/12 (H4, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.630× | -3.1 | 0.26 | 1/12 (NCI-H2030) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.26 | 0/12 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.661× | -3.0 | 0.26 | 4/12 (H4, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 98.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 80.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 4.66 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.340× (z -10.0) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.554 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFPI2]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LAMA1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CNST]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[NRIP3]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[TM4SF1]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[PKIA]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[STC1]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CUTC]] | +0.54 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ANOS1]] | +0.54 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[RAB3B]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[MMP1]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 | pathway: Interleukin-4 and Interleukin-13 signaling |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF793]] | -0.45 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[RBM5]] | -0.43 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[CPEB2]] | -0.42 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[FRG1DP]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ARFGAP2]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADTRP]] | C | ADTRP activity raises IL13RA2's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without ADTRP | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[STC1]] | C | STC1 activity raises IL13RA2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.99× lower at baseline in the lines without STC1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises IL13RA2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.79× lower at baseline in the lines without ESM1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DELEC1]] | B | IL13RA2 activity raises DELEC1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.01× lower at baseline in the lines without IL13RA2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[FXYD5]] | B | IL13RA2 activity raises FXYD5's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.20× lower at baseline in the lines without IL13RA2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[NBPF9]] | B | IL13RA2 activity raises NBPF9's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.58× lower at baseline in the lines without IL13RA2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[STK4]] | B | IL13RA2 activity raises STK4's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.28× lower at baseline in the lines without IL13RA2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[PFDN2]] | B | IL13RA2 activity raises PFDN2's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.47× lower at baseline in the lines without IL13RA2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[CTSL]] | B | IL13RA2 activity raises CTSL's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.56× lower at baseline in the lines without IL13RA2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[ESM1]] | C | IL13RA2 activity raises ESM1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without IL13RA2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[STC1]] | C | IL13RA2 activity raises STC1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 7.22× lower at baseline in the lines without IL13RA2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[ADTRP]] | C | IL13RA2 activity raises ADTRP's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.77× lower at baseline in the lines without IL13RA2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[GNG11]] | C | IL13RA2 activity raises GNG11's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 3.40× lower at baseline in the lines without IL13RA2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[LNCOG]] | C | IL13RA2 activity raises LNCOG's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.42× lower at baseline in the lines without IL13RA2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[TFPI2]] | C | IL13RA2 activity raises TFPI2's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 4.53× lower at baseline in the lines without IL13RA2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 12.8); signed map (4.9, 53.8). **Vector** length 29.9, 7.68% of its response variance represented; |z| ≥ 3 in 257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.7 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.7 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -0.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 13 receptor subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:115,003,975-115,019,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IL-13R, IL13BP, CD213a2, CT19 |
| Gene groups (HGNC) | CD molecules; Interleukin receptors |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 3 pathways, smallest: Interleukin-4 and Interleukin-13 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14627](https://www.uniprot.org/uniprotkb/Q14627) (Interleukin-13 receptor subunit alpha-2):

> Cell surface receptor that plays a role in the regulation of IL-13-mediated responses. Functions as a decoy receptor that inhibits IL-13- and IL-4-mediated signal transduction via the JAK-STAT pathway and thereby modulates immune responses and inflammation. Serves as a functional signaling receptor for IL-13 in an alternative pathway involving AP-1 ultimately leading to the production of TGFB1.

**Summary**, from NCBI Gene [3598](https://www.ncbi.nlm.nih.gov/gene/3598):

> The protein encoded by this gene is closely related to Il13RA1, a subuint of the interleukin 13 receptor complex. This protein binds IL13 with high affinity, but lacks cytoplasmic domain, and does not appear to function as a signal mediator. It is reported to play a role in the internalization of IL13. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5975) · Entrez [3598](https://www.ncbi.nlm.nih.gov/gene/3598) · UniProt [Q14627](https://www.uniprot.org/uniprotkb/Q14627) · Ensembl [ENSG00000123496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123496)

## Data

Gene col 4439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4439); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4439]; `tensor/DDL_lfc|DDL_z.npy` [4439]; `embed/gene_vectors.npy` [4439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4439 or target_col == 4439). Every well: [[IL13RA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL13RA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
