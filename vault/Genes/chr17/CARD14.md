---
symbol: "CARD14"
type: "gene"
col: 6538
ensembl_id: "ENSG00000141527"
name: "caspase recruitment domain family member 14"
location: "17q25.3"
module: 8
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 58
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CARD14

*caspase recruitment domain family member 14* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.28× (z +21.0, q 0e+00, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -5.7, q 8e-06, down in 18 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0411×; ⚠ cell-cycle shift, explains ~66% of this change); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0379×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0531×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM16-AS1]] (+0.64, fdr 8e-06), [[STEAP4]] (+0.59, fdr 1e-05), [[ARSL]] (+0.58, fdr 1e-05); moves opposite to [[DCBLD2]] (-0.46, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[TCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.28×** | +21.0 | 0e+00 | 21/31 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.7 | 4e-12 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.6 | 5e-06 | 16/42 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.4 | 1e-05 | 3/16 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.4 | 0.001 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.006 | 8/32 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.006 | 10/35 (A-172, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.007 | 10/43 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.011 | 11/36 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.012 | 9/35 (HepG2/C3A, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.5 | 0.020 | 1/16 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.024 | 4/25 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.034 | 2/31 (SNU-423, NCI-H1792) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.057 | 8/39 (HOP62, COLO 205, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.070 | 10/37 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.070 | 8/40 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.073 | 8/36 (LoVo, CFPAC-1, …) | two highest doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.073 | 3/28 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0411×; ⚠ cell-cycle shift, explains ~66% of this change); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0379×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0531×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.575×** | -5.7 | 8e-06 | 18/45 (COLO 205, Panc 03.27, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.6 | 0.096 | 11/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.722× | -3.4 | 0.15 | 12/39 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.739× | -3.1 | 0.21 | 13/35 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.21 | 7/41 (MIA PaCa-2, SNU-423, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.569× | -3.0 | 0.21 | 0/42 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -12.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-172 (line)]] | wt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.9) | — |
| [[A498 (line)]] | wt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +11.1) | — |
| [[A549 (line)]] | wt | 3.05 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0279× (z -10.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[CFPAC-1 (line)]] | alt | 4.92 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0531× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 1.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.67× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0379× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 1.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 3.06 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0874× (z -9.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 3.29 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0802× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +10.1) | — |
| [[SW480 (line)]] | alt | 0.936 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +9.0) | — |
| [[A-427 (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.933 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM16-AS1]] | +0.64 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[STEAP4]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ARSL]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TMC1]] | +0.56 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[FAM177B]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RNF183]] | +0.56 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SMIM2-AS1]] | +0.56 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CASP10]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[HLA-DRB1]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[UNC5CL]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.46 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 58, C 0. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCN1]] | B | TCN1 activity raises CARD14's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.44× lower at baseline in the lines without TCN1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[CYP4F12]] | B | CYP4F12 activity raises CARD14's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CYP4F12 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[DUOX2]] | B | DUOX2 activity raises CARD14's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.98× lower at baseline in the lines without DUOX2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[LCN2]] | B | LCN2 activity raises CARD14's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without LCN2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises CARD14's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[SLC44A4]] | B | SLC44A4 activity raises CARD14's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without SLC44A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[STEAP4]] | B | STEAP4 activity raises CARD14's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without STEAP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ALOX5]] | B | ALOX5 activity raises CARD14's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without ALOX5 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CARD14's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without ELF3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[SIDT1]] | B | SIDT1 activity raises CARD14's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without SIDT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[SLC28A3]] | B | SLC28A3 activity raises CARD14's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.94× lower at baseline in the lines without SLC28A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises CARD14's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without SYNPR-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, 53.9); signed map (60.4, -1.1). **Vector** length 57.5, 8.47% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +21.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.7 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,169,992-80,216,073 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CARMA2, BIMP2; previously PSORS2 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Caspase recruitment domain containing; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXL6](https://www.uniprot.org/uniprotkb/Q9BXL6) (Caspase recruitment domain-containing protein 14):

> Acts as a scaffolding protein that can activate the inflammatory transcription factor NF-kappa-B and p38/JNK MAP kinase signaling pathways. Forms a signaling complex with BCL10 and MALT1, and activates MALT1 proteolytic activity and inflammatory gene expression. MALT1 is indispensable for CARD14-induced activation of NF-kappa-B and p38/JNK MAP kinases. May play a role in signaling mediated by TRAF2, TRAF3 and TRAF6 and protects cells against apoptosis.; [Isoform 3]: Not able to activate the …

**Summary**, from NCBI Gene [79092](https://www.ncbi.nlm.nih.gov/gene/79092):

> This gene encodes a caspase recruitment domain-containing protein that is a member of the membrane-associated guanylate kinase (MAGUK) family of proteins. Members of this protein family are scaffold proteins that are involved in a diverse array of cellular processes including cellular adhesion, signal transduction and cell polarity control. This protein has been shown to specifically interact with BCL10, a protein known to function as a positive regulator of cell apoptosis and NF-kappaB …

**Accessions** — [HGNC:16446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16446) · Entrez [79092](https://www.ncbi.nlm.nih.gov/gene/79092) · UniProt [Q9BXL6](https://www.uniprot.org/uniprotkb/Q9BXL6) · Ensembl [ENSG00000141527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141527)

## Data

Gene col 6538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6538); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6538]; `tensor/DDL_lfc|DDL_z.npy` [6538]; `embed/gene_vectors.npy` [6538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6538 or target_col == 6538). Every well: [[CARD14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
