---
symbol: "CTSH"
type: "gene"
col: 2396
ensembl_id: "ENSG00000103811"
name: "cathepsin H"
location: "15q25.1"
module: 29
arm: "+"
pooled_cpm: 12.02
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CTSH

*cathepsin H* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +15.2, q 0e+00, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +4.5, q 7e-04, up in 12 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.656× (z -5.1, q 2e-04, down in 14 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYZ]] (+0.63, fdr 1e-05), [[SOD3]] (+0.61, fdr 1e-05), [[ASAH1]] (+0.61, fdr 1e-05); moves opposite to [[C10orf88]] (-0.51, fdr 1e-04), [[KCTD5]] (-0.51, fdr 4e-05), [[TRAPPC12]] (-0.49, fdr 7e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 4 go from it, the strongest it → [[PRXL2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +15.2 | 0e+00 | 26/27 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +14.1 | 1e-42 | 18/20 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +10.4 | 6e-23 | 20/22 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +6.0 | 2e-07 | 20/39 (PANC-1, J82, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +5.9 | 4e-07 | 18/34 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.5 | 7e-04 | 12/39 (HOP62, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.4 | 8e-04 | 14/33 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +4.2 | 0.002 | 16/39 (PANC-1, J82, …) | all doses, flat | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.005 | 12/35 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.8 | 0.008 | 7/17 (HT-29, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.051 | 5/35 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +3.2 | 0.061 | 7/39 (PANC-1, J82, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +3.1 | 0.077 | 12/36 (HEC-1-A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -5.1 | 2e-04 | 14/33 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.759×** | -4.7 | 7e-04 | 19/36 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.544×** | -3.8 | 0.023 | 16/39 (KATO III, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.055 | 11/37 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.833× | -3.1 | 0.19 | 8/40 (BT-474, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 56.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -9.3) |
| [[A498 (line)]] | wt | 21.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.1) |
| [[PANC-1 (line)]] | alt | 10.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 99.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -9.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[Hs 766T (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0715× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 6.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.7) |
| [[A-172 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYZ]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SOD3]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.61 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MSLN]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SUMF2]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GSTK1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[EPCAM]] | +0.59 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[TSPAN6]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CPVL]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ACO1]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CXADR]] | +0.57 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[PLBD1]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C10orf88]] | -0.51 | -0.48 / -0.32 | both halves | 1e-04 |  |
| [[KCTD5]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TRAPPC12]] | -0.49 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[SETX]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ADRM1]] | -0.48 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[NME6]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ZNF621]] | -0.47 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[ADCY7]] | -0.46 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CCDC137]] | -0.46 | -0.39 / -0.29 | both halves | 3e-04 |  |
| [[PRKAG1]] | -0.46 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[DNTTIP2]] | -0.46 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[RFFL]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises CTSH's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without CXADR | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[FXYD3]] | B | FXYD3 activity raises CTSH's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without FXYD3 | 0.029 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[SORL1]] | B | SORL1 activity raises CTSH's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without SORL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[SMPDL3B]] | B | SMPDL3B activity raises CTSH's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without SMPDL3B | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[CD74]] | B | CD74 activity raises CTSH's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.70× lower at baseline in the lines without CD74 | 0.037 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[PPP1R1B]] | B | PPP1R1B activity raises CTSH's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 1.90× lower at baseline in the lines without PPP1R1B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[TMEM139]] | B | TMEM139 activity raises CTSH's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without TMEM139 | 0.060 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[TSPAN1]] | B | TSPAN1 activity raises CTSH's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without TSPAN1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[PRXL2A]] | B | PRXL2A activity raises CTSH's level | lines that do not express PRXL2A (9) vs lines expressing it (41) | 1.16× lower at baseline in the lines without PRXL2A | 0.067 | ⚠ within organs, on part of the lines; also absent: ACSS1, LONRF3, AP1G2 |
| [[PHGR1]] | B | PHGR1 activity raises CTSH's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 2.03× lower at baseline in the lines without PHGR1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20 |
| [[LYZ]] | B | LYZ activity raises CTSH's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without LYZ | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRXL2A]] | B | CTSH activity raises PRXL2A's level | lines that do not express CTSH (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without CTSH | 0.039 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[PLBD1]] | B | CTSH activity raises PLBD1's level | lines that do not express CTSH (8) vs lines expressing it (42) | 3.47× lower at baseline in the lines without CTSH | 0.042 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[RFFL]] | B | CTSH activity raises RFFL's level | lines that do not express CTSH (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without CTSH | 0.091 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[SLC25A23]] | B | CTSH activity raises SLC25A23's level | lines that do not express CTSH (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without CTSH | 0.096 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (31.9, 57.4); signed map (60.7, -5.5). **Vector** length 52.9, 9.05% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.7 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,921,058-78,949,574 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACC-4, ACC-5, ACC4, ACC5; previously CPSB |
| Gene groups (HGNC) | Cathepsins; Minor histocompatibility antigens; Cysteine endopeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 8 pathways, smallest: Surfactant metabolism; Processing of antigen in germinal center B cells; MHC class II antigen presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09668](https://www.uniprot.org/uniprotkb/P09668) (Pro-cathepsin H):

> Important for the overall degradation of proteins in lysosomes.

**Summary**, from NCBI Gene [1512](https://www.ncbi.nlm.nih.gov/gene/1512):

> The protein encoded by this gene is a lysosomal cysteine proteinase important in the overall degradation of lysosomal proteins. It is composed of a dimer of disulfide-linked heavy and light chains, both produced from a single protein precursor. The encoded protein, which belongs to the peptidase C1 protein family, can act both as an aminopeptidase and as an endopeptidase. Increased expression of this gene has been correlated with malignant progression of prostate tumors. Alternate splicing of …

**Accessions** — [HGNC:2535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2535) · Entrez [1512](https://www.ncbi.nlm.nih.gov/gene/1512) · UniProt [P09668](https://www.uniprot.org/uniprotkb/P09668) · Ensembl [ENSG00000103811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103811)

## Data

Gene col 2396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2396); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2396]; `tensor/DDL_lfc|DDL_z.npy` [2396]; `embed/gene_vectors.npy` [2396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2396 or target_col == 2396). Every well: [[CTSH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
