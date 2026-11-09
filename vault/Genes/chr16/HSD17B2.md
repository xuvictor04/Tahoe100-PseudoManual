---
symbol: "HSD17B2"
type: "gene"
col: 1468
ensembl_id: "ENSG00000086696"
name: "hydroxysteroid 17-beta dehydrogenase 2"
location: "16q23.3"
module: 55
arm: "+"
pooled_cpm: 13.95
n_lines_expressing: 15
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 69
direction_downstream: 127
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# HSD17B2

*hydroxysteroid 17-beta dehydrogenase 2* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +8.6, q 3e-15, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[BAY1125976 (drug)]] 0.5 µM: 1.84× (z +3.5, q 0.072, up in 1 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.481× (z -5.5, q 2e-05, down in 10 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.75, fdr 7e-06), [[IL20RA]] (+0.75, fdr 7e-06), [[HNF4A]] (+0.74, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 69 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); 127 go from it, the strongest it → [[NUDT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +8.6 | 3e-15 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +8.0 | 5e-13 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.4 | 0.002 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.84×** | +3.5 | 0.072 | 1/13 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 2.19× | +3.3 | 0.13 | 5/13 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.76× | +3.2 | 0.13 | 1/13 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.481×** | -5.5 | 2e-05 | 10/13 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.503×** | -5.2 | 6e-05 | 9/13 (LoVo, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.506×** | -5.0 | 1e-04 | 5/13 (HT-29, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -4.5 | 1e-03 | 10/13 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -4.4 | 0.001 | 10/13 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.586×** | -4.4 | 0.001 | 6/13 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.005 | 8/13 (HT-29, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.613×** | -3.8 | 0.009 | 6/13 (HT-29, LoVo, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.868× | -3.8 | 0.010 | 2/13 (SW480, AsPC-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.633×** | -3.6 | 0.020 | 8/13 (Hs 766T, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -3.5 | 0.025 | 7/13 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -3.4 | 0.026 | 9/13 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.645×** | -3.4 | 0.026 | 4/13 (SNU-423, HT-29, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -3.1 | 0.073 | 7/13 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 115 | 0 | 26 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0164× (z -21.2) |
| [[KATO III (line)]] | alt | 71.0 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0319× (z -25.2) |
| [[Hs 766T (line)]] | wt | 285 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0409× (z -21.6) |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0182× (z -21.5) |
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0370× (z -17.2) |
| [[LoVo (line)]] | wt | 13.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -16.8) |
| [[SW480 (line)]] | alt | 5.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.4) |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.75 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.75 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[MYO7B]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.72 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ABO]] | +0.71 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[C4BPB]] | +0.70 | +0.72 / +0.57 | both halves | 8e-06 | **novel candidate** |
| [[ITGB4]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 2, C 67. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises HSD17B2's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without LINC02320 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[ABCC3]] | B | ABCC3 activity raises HSD17B2's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without ABCC3 | 0.091 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises HSD17B2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 6.28× lower at baseline in the lines without ST6GALNAC1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[F5]] | C | F5 activity raises HSD17B2's level | lines that do not express F5 (39) vs lines expressing it (11) | 4.86× lower at baseline in the lines without F5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises HSD17B2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.39× lower at baseline in the lines without CEACAM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises HSD17B2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.99× lower at baseline in the lines without CYP3A5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises HSD17B2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 3.92× lower at baseline in the lines without PRR15 | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[PRKCH-AS1]] | C | PRKCH-AS1 activity raises HSD17B2's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.30× lower at baseline in the lines without PRKCH-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises HSD17B2's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 3.72× lower at baseline in the lines without TSPAN8 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises HSD17B2's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 3.91× lower at baseline in the lines without FOXQ1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises HSD17B2's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 4.44× lower at baseline in the lines without TTC22 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises HSD17B2's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.72× lower at baseline in the lines without GPX2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |

### Downstream of this gene

*127 arrows, 127 of them with an alert ⚠; grade A 0, B 30, C 97. Shown: the 12 strongest; 115 more arrows (115 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT4]] | B | HSD17B2 activity raises NUDT4's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.22× lower at baseline in the lines without HSD17B2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[TNFRSF21]] | B | HSD17B2 activity raises TNFRSF21's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 4.86× lower at baseline in the lines without HSD17B2 | 0.004 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[PTK6]] | B | HSD17B2 activity raises PTK6's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.53× lower at baseline in the lines without HSD17B2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[DLG3]] | B | HSD17B2 activity raises DLG3's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.69× lower at baseline in the lines without HSD17B2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[BCL2L1-AS1]] | B | HSD17B2 activity raises BCL2L1-AS1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 1.53× lower at baseline in the lines without HSD17B2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[TJP2]] | B | HSD17B2 activity raises TJP2's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without HSD17B2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[EPB41L1]] | B | HSD17B2 activity raises EPB41L1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without HSD17B2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[EPS8L1]] | B | HSD17B2 activity raises EPS8L1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without HSD17B2 | 0.024 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[ABHD11]] | B | HSD17B2 activity raises ABHD11's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without HSD17B2 | 0.027 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[TTC28]] | B | HSD17B2 activity lowers TTC28's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.22× higher at baseline in the lines without HSD17B2 | 0.030 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[STK24]] | B | HSD17B2 activity raises STK24's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without HSD17B2 | 0.032 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[FAM83E]] | B | HSD17B2 activity raises FAM83E's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.03× lower at baseline in the lines without HSD17B2 | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.4, 50.5); signed map (63.0, 9.5). **Vector** length 70.8, 26.7% of its response variance represented; |z| ≥ 3 in 499 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 17-beta dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:82,035,004-82,098,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSD17, SDR9C2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Estrogen biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [P37059](https://www.uniprot.org/uniprotkb/P37059) (17-beta-hydroxysteroid dehydrogenase type 2):

> Catalyzes the NAD-dependent oxidation of the highly active 17beta-hydroxysteroids, such as estradiol (E2), testosterone (T), and dihydrotestosterone (DHT), to their less active forms and thus regulates the biological potency of these steroids. Oxidizes estradiol to estrone, testosterone to androstenedione, and dihydrotestosterone to 5alpha-androstan-3,17-dione. Also has 20-alpha-HSD activity.

**Summary**, from NCBI Gene [3294](https://www.ncbi.nlm.nih.gov/gene/3294):

> Enables estradiol 17-beta-dehydrogenase [NAD(P)+] activity and testosterone dehydrogenase (NAD+) activity. Involved in androgen metabolic process; estrogen biosynthetic process; and response to retinoic acid. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5211) · Entrez [3294](https://www.ncbi.nlm.nih.gov/gene/3294) · UniProt [P37059](https://www.uniprot.org/uniprotkb/P37059) · Ensembl [ENSG00000086696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086696)

## Data

Gene col 1468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1468); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1468]; `tensor/DDL_lfc|DDL_z.npy` [1468]; `embed/gene_vectors.npy` [1468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1468 or target_col == 1468). Every well: [[HSD17B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
