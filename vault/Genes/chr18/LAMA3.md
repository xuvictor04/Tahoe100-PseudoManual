---
symbol: "LAMA3"
type: "gene"
col: 596
ensembl_id: "ENSG00000053747"
name: "laminin subunit alpha 3"
location: "18q11.2"
module: 34
arm: "+"
pooled_cpm: 288.5
n_lines_expressing: 28
n_dd_up: 1
n_dd_down: 37
n_dd_up_clean: 1
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 78
direction_downstream: 116
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LAMA3

*laminin subunit alpha 3* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +4.4, q 0.006, up in 6 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 4.02×); [[Harringtonine (drug)]] 5 µM in 1 line (BT-474 5.70×); [[Tucidinostat (drug)]] 5 µM in 1 line (BT-474 3.24×).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.446× (z -17.5, q 0e+00, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA0040]] (+0.75, fdr 7e-06), [[LAMC2]] (+0.71, fdr 7e-06), [[SCEL]] (+0.70, fdr 7e-06); moves opposite to [[SELENOP]] (-0.52, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 78 arrows point to it, the strongest [[IL1R2]] → it (grade B ⚠); 116 go from it, the strongest it → [[LMO7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 4.02×); [[Harringtonine (drug)]] 5 µM in 1 line (BT-474 5.70×); [[Tucidinostat (drug)]] 5 µM in 1 line (BT-474 3.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.006 | 6/26 (BT-474, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.24× | +3.3 | 0.18 | 2/25 (A-427, C32) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | 1.23× | +3.3 | 0.18 | 12/27 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.22× | +3.2 | 0.18 | 11/27 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.21× | +3.1 | 0.22 | 6/26 (J82, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.446×** | -17.5 | 0e+00 | 23/26 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -8.8 | 4e-16 | 19/26 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.702×** | -7.7 | 2e-12 | 15/26 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.706×** | -7.4 | 2e-11 | 21/26 (SW48, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -7.4 | 2e-11 | 20/26 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -6.7 | 2e-09 | 22/27 (HT-29, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.642×** | -6.5 | 8e-09 | 15/26 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -6.4 | 9e-09 | 21/26 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -5.9 | 3e-07 | 18/26 (SW 900, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.702×** | -5.6 | 1e-06 | 19/26 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -5.4 | 4e-06 | 17/26 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.707×** | -5.3 | 4e-06 | 18/28 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.716×** | -5.3 | 5e-06 | 19/27 (C32, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -5.1 | 1e-05 | 19/26 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.731×** | -4.9 | 3e-05 | 13/26 (BT-474, C32, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -4.9 | 3e-05 | 15/27 (NCI-H1792, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 398 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -23.1) |
| [[A549 (line)]] | wt | 157 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -21.8) |
| [[HT-29 (line)]] | alt | 600 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -15.4) |
| [[A498 (line)]] | wt | 220 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.7) |
| [[BT-474 (line)]] | alt | 95.8 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.1) | [[Ponatinib (drug)]] 5 µM 0.176× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 451 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 1,264 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -14.5) |
| [[A-427 (line)]] | wt | 105 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.104× (z -11.0) |
| [[C32 (line)]] | wt | 85.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 178 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.0) |
| [[Hs 766T (line)]] | wt | 161 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -15.8) |
| [[J82 (line)]] | alt | 95.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -11.0) |
| [[LoVo (line)]] | wt | 588 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 1,404 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.8) |
| [[SW48 (line)]] | wt | 873 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.121× (z -13.8) |
| [[SW480 (line)]] | alt | 375 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 1,371 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 329 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.7) |
| [[HCT15 (line)]] | alt | 91.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.2) |
| [[KATO III (line)]] | alt | 403 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.6) |
| [[LS 180 (line)]] | wt | 566 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.7) |
| [[A-172 (line)]] | wt | 37.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1,115 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 31.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 69.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 23.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 60.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 56.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0040]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LAMC2]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 998 |
| [[SCEL]] | +0.70 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[HAS3]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TGFA]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Developmental Cell Lineages |
| [[TNS4]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | pathway: MET promotes cell motility |
| [[FERMT1]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 | STRING 498 |
| [[HS3ST1]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CEACAM1]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[ITGA6]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 930 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOP]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*78 arrows, 78 of them with an alert ⚠; grade A 0, B 26, C 52. Shown: the 12 strongest; 66 more arrows (66 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1R2]] | B | IL1R2 activity raises LAMA3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 4.03× lower at baseline in the lines without IL1R2 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[IL1RN]] | B | IL1RN activity raises LAMA3's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 3.11× lower at baseline in the lines without IL1RN | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[GPR39]] | B | GPR39 activity raises LAMA3's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 5.12× lower at baseline in the lines without GPR39 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[GPRC5A]] | B | GPRC5A activity raises LAMA3's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without GPRC5A | 0.012 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LYPD3]] | B | LYPD3 activity raises LAMA3's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without LYPD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[ANKRD29]] | B | ANKRD29 activity raises LAMA3's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without ANKRD29 | 0.020 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[IL2RG]] | B | IL2RG activity raises LAMA3's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.85× lower at baseline in the lines without IL2RG | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[DUSP4]] | B | DUSP4 activity raises LAMA3's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without DUSP4 | 0.022 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[MYEOV]] | B | MYEOV activity raises LAMA3's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.23× lower at baseline in the lines without MYEOV | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[LMO7]] | B | LMO7 activity raises LAMA3's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without LMO7 | 0.038 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[GPRC5D-AS1]] | B | GPRC5D-AS1 activity raises LAMA3's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 4.35× lower at baseline in the lines without GPRC5D-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[B4GALNT3]] | B | B4GALNT3 activity raises LAMA3's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.89× lower at baseline in the lines without B4GALNT3 | 0.046 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |

### Downstream of this gene

*116 arrows, 116 of them with an alert ⚠; grade A 0, B 69, C 47. Shown: the 12 strongest; 104 more arrows (104 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | LAMA3 activity raises LMO7's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 4.02× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[MET]] | B | LAMA3 activity raises MET's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.65× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[MYO1E]] | B | LAMA3 activity raises MYO1E's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[ANKRD29]] | B | LAMA3 activity raises ANKRD29's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[BAIAP2L1]] | B | LAMA3 activity raises BAIAP2L1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[NPC1]] | B | LAMA3 activity raises NPC1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without LAMA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[KIF13B]] | B | LAMA3 activity raises KIF13B's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without LAMA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[GPRC5D-AS1]] | B | LAMA3 activity raises GPRC5D-AS1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.70× lower at baseline in the lines without LAMA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[LYPD3]] | B | LAMA3 activity raises LYPD3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without LAMA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[ARHGAP27]] | B | LAMA3 activity raises ARHGAP27's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without LAMA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[TNFAIP8]] | B | LAMA3 activity raises TNFAIP8's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without LAMA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[ITGA6]] | B | LAMA3 activity raises ITGA6's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without LAMA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, 51.7); signed map (3.5, 39.8). **Vector** length 121, 42.6% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.9 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -7.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,689,453-23,956,222 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nicein-150kDa, kalinin-165kDa, BM600-150kDa, epiligrin; previously LAMNA |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 25 pathways, smallest: Type I hemidesmosome assembly; Anchoring fibril formation; Attachment of bacteria to epithelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16787](https://www.uniprot.org/uniprotkb/Q16787) (Laminin subunit alpha-3):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.; Laminin-5 is thought to be involved in (1) cell adhesion via integrin alpha-3/beta-1 in focal adhesion and integrin alpha-6/beta-4 in hemidesmosomes, (2) signal transduction via tyrosine phosphorylation of pp125-FAK and p80, (3) differentiation of keratinocytes.

**Summary**, from NCBI Gene [3909](https://www.ncbi.nlm.nih.gov/gene/3909):

> The protein encoded by this gene belongs to the laminin family of secreted molecules. Laminins are heterotrimeric molecules that consist of alpha, beta, and gamma subunits that assemble through a coiled-coil domain. Laminins are essential for formation and function of the basement membrane and have additional functions in regulating cell migration and mechanical signal transduction. This gene encodes an alpha subunit and is responsive to several epithelial-mesenchymal regulators including …

**Accessions** — [HGNC:6483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6483) · Entrez [3909](https://www.ncbi.nlm.nih.gov/gene/3909) · UniProt [Q16787](https://www.uniprot.org/uniprotkb/Q16787) · Ensembl [ENSG00000053747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053747)

## Data

Gene col 596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 596); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 596]; `tensor/DDL_lfc|DDL_z.npy` [596]; `embed/gene_vectors.npy` [596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 596 or target_col == 596). Every well: [[LAMA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
