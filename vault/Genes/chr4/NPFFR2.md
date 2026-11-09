---
symbol: "NPFFR2"
type: "gene"
col: 636
ensembl_id: "ENSG00000056291"
name: "neuropeptide FF receptor 2"
location: "4q13.3"
module: 9
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 17
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NPFFR2

*neuropeptide FF receptor 2* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.88× (z +20.8, q 0e+00, up in 7 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.269×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.461×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01695]] (+0.65, fdr 2e-04), [[MSR1]] (+0.61, fdr 6e-05), [[SLCO2B1]] (+0.59, fdr 1e-05); moves opposite to [[PACSIN2]] (-0.51, fdr 2e-04), [[CPD]] (-0.49, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[GPR158]] → it (grade B ⚠); 11 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.88×** | +20.8 | 0e+00 | 7/8 (SK-MEL-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.09×** | +12.2 | 1e-31 | 8/9 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +12.1 | 3e-31 | 4/8 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.63×** | +9.6 | 2e-19 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.22×** | +9.3 | 1e-18 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +8.6 | 9e-16 | 1/6 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.07×** | +7.5 | 4e-12 | 5/10 (NCI-H1573, SHP-77, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +6.1 | 5e-08 | 9/10 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +5.3 | 6e-06 | 7/12 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.99×** | +5.3 | 8e-06 | 2/2 (SK-MEL-2, SHP-77) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +5.1 | 1e-05 | 5/12 (NCI-H1573, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.5 | 4e-04 | 2/12 (NCI-H1573, SK-MEL-2) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +4.5 | 4e-04 | 5/9 (SHP-77, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.2 | 0.001 | 2/5 (CFPAC-1, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.0 | 0.002 | 2/8 (NCI-H1573, SHP-77) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +3.8 | 0.004 | 5/9 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +3.8 | 0.004 | 6/13 (SHP-77, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.039 | 1/12 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +3.1 | 0.054 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.0 | 0.054 | 1/10 (SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.056 | 3/12 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 636.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.269×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.461×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.589× | -3.6 | 0.15 | 4/11 (SNU-423, hTERT-HPNE, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.575× | -3.5 | 0.15 | 0/12 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.617× | -3.3 | 0.19 | 2/12 (SW 900, NCI-H661) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 106 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 65.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +16.2) | — |
| [[BT-474 (line)]] | alt | 1.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 218× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 4.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 3.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +8.6) | — |
| [[A-172 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.452 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01695]] | +0.65 | +0.30 / +0.71 | both halves | 2e-04 |  |
| [[MSR1]] | +0.61 | +0.38 / +0.69 | both halves | 6e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[SLCO2B1]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC01611]] | +0.58 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NKAIN2]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[LINC02335]] | +0.58 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[EGFEM1P]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SEMA3E]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CPEB1]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[KCNH7]] | +0.57 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[HYDIN]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MARCHF1]] | +0.56 | +0.44 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACSIN2]] | -0.51 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[CPD]] | -0.49 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR158]] | B | GPR158 activity raises NPFFR2's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 1.83× lower at baseline in the lines without GPR158 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968 |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises NPFFR2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without CCDC144NL-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises NPFFR2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.80× lower at baseline in the lines without FUT9 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises NPFFR2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without KCNH7 | 0.023 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[NTNG1]] | C | NTNG1 activity raises NPFFR2's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without NTNG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises NPFFR2's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without MSR1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises NPFFR2's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without LINC01320 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[LINC01266]] | C | LINC01266 activity raises NPFFR2's level | lines that do not express LINC01266 (35) vs lines expressing it (15) | 2.77× lower at baseline in the lines without LINC01266 | 0.046 | ⚠ within organs, on part of the lines; also absent: UNC5D, KHDRBS2, ENSG00000260958; maybe low, not absent; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises NPFFR2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.10× lower at baseline in the lines without CARD18 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises NPFFR2's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.06× lower at baseline in the lines without LINC02492 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises NPFFR2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.92× lower at baseline in the lines without RUNX1T1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[MIR4307HG]] | C | MIR4307HG activity raises NPFFR2's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 2.55× lower at baseline in the lines without MIR4307HG | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | NPFFR2 activity raises SEMA6D's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without NPFFR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[SLC35F1]] | B | NPFFR2 activity raises SLC35F1's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without NPFFR2 | 0.037 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[OFCC1]] | B | NPFFR2 activity raises OFCC1's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without NPFFR2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[EML5]] | B | NPFFR2 activity raises EML5's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without NPFFR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[GPR158]] | B | NPFFR2 activity raises GPR158's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without NPFFR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[GRIA4]] | B | NPFFR2 activity raises GRIA4's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 1.90× lower at baseline in the lines without NPFFR2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[FUT9]] | C | NPFFR2 activity raises FUT9's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.95× lower at baseline in the lines without NPFFR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |
| [[MSR1]] | C | NPFFR2 activity raises MSR1's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without NPFFR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |
| [[GRIA2]] | C | NPFFR2 activity raises GRIA2's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.45× lower at baseline in the lines without NPFFR2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |
| [[LINC00470]] | C | NPFFR2 activity raises LINC00470's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without NPFFR2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |
| [[RUNX1T1]] | C | NPFFR2 activity raises RUNX1T1's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 3.39× lower at baseline in the lines without NPFFR2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 27.1); signed map (39.4, 28.0). **Vector** length 23.1, 5.07% of its response variance represented; |z| ≥ 3 in 214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | neuropeptide FF receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:72,031,902-72,148,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPFF2, NPGPR; previously GPR74 |
| Gene groups (HGNC) | Neuropeptide FF receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X5](https://www.uniprot.org/uniprotkb/Q9Y5X5) (Neuropeptide FF receptor 2):

> Receptor for NPAF (A-18-F-amide) and NPFF (F-8-F-amide) neuropeptides, also known as morphine-modulating peptides. Can also be activated by a variety of naturally occurring or synthetic FMRF-amide like ligands. This receptor mediates its action by association with G proteins that activate a phosphatidylinositol-calcium second messenger system.

**Summary**, from NCBI Gene [10886](https://www.ncbi.nlm.nih.gov/gene/10886):

> This gene encodes a member of a subfamily of G-protein-coupled neuropeptide receptors. This protein is activated by the neuropeptides A-18-amide (NPAF) and F-8-amide (NPFF) and may function in pain modulation and regulation of the opioid system. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:4525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4525) · Entrez [10886](https://www.ncbi.nlm.nih.gov/gene/10886) · UniProt [Q9Y5X5](https://www.uniprot.org/uniprotkb/Q9Y5X5) · Ensembl [ENSG00000056291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056291)

## Data

Gene col 636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 636); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 636]; `tensor/DDL_lfc|DDL_z.npy` [636]; `embed/gene_vectors.npy` [636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 636 or target_col == 636). Every well: [[NPFFR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPFFR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
