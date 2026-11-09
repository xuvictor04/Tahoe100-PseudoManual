---
symbol: "IL20RA"
type: "gene"
col: 299
ensembl_id: "ENSG00000016402"
name: "interleukin 20 receptor subunit alpha"
location: "6q23.3"
module: 55
arm: "+"
pooled_cpm: 11.18
n_lines_expressing: 17
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 105
direction_downstream: 90
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# IL20RA

*interleukin 20 receptor subunit alpha* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +8.4, q 2e-14, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +7.5, q 2e-11, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.415× (z -8.1, q 3e-13, down in 15 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDAR]] (+0.85, fdr 7e-06), [[BMP4]] (+0.84, fdr 7e-06), [[C9orf152]] (+0.81, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 105 arrows point to it, the strongest [[ZNF503-AS1]] → it (grade B ⚠); 90 go from it, the strongest it → [[SEPTIN9-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +8.4 | 2e-14 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.5 | 2e-11 | 3/15 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +7.0 | 5e-10 | 3/13 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.6 | 7e-04 | 2/9 (CFPAC-1, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.5 | 0.045 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.045 | 5/15 (AsPC-1, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.63× | +3.1 | 0.15 | 1/13 (NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.89× | +3.1 | 0.15 | 1/10 (LoVo) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.415×** | -8.1 | 3e-13 | 15/15 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -5.9 | 1e-06 | 14/15 (COLO 205, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -5.8 | 1e-06 | 14/15 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -5.6 | 3e-06 | 10/15 (COLO 205, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -5.4 | 6e-06 | 11/15 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.547×** | -5.1 | 3e-05 | 4/15 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.590×** | -4.7 | 2e-04 | 6/15 (SW480, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.605×** | -4.6 | 3e-04 | 13/15 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.004 | 12/14 (COLO 205, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.008 | 6/15 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.675×** | -3.6 | 0.015 | 12/15 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.477×** | -3.6 | 0.017 | 8/15 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.665×** | -3.5 | 0.017 | 0/15 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -3.5 | 0.017 | 5/15 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.675×** | -3.5 | 0.020 | 9/15 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -3.4 | 0.027 | 11/15 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 203 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0420× (z -31.2) |
| [[LS 180 (line)]] | wt | 93.5 | 0 | 15 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0349× (z -25.1) |
| [[SW480 (line)]] | alt | 45.1 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0495× (z -22.4) |
| [[LoVo (line)]] | wt | 40.8 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0639× (z -18.9) |
| [[SW48 (line)]] | wt | 27.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0768× (z -11.6) |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.0) |
| [[KATO III (line)]] | alt | 15.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -9.8) |
| [[A-172 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDAR]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.81 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.79 | +0.84 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.77 | +0.82 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.77 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.75 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.75 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[HNF4A]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[HSD17B2]] | +0.75 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[TNFRSF14-AS1]] | +0.74 | +0.79 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 4, C 101. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises IL20RA's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without ZNF503-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises IL20RA's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without TJP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ZBTB7C]] | B | ZBTB7C activity raises IL20RA's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.33× lower at baseline in the lines without ZBTB7C | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A |
| [[MAP2K1]] | B | MAP2K1 activity raises IL20RA's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[LINC01559]] | C | LINC01559 activity raises IL20RA's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 8.11× lower at baseline in the lines without LINC01559 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises IL20RA's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 11.11× lower at baseline in the lines without CLRN3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises IL20RA's level | lines that do not express EDAR (36) vs lines expressing it (14) | 7.53× lower at baseline in the lines without EDAR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises IL20RA's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 4.98× lower at baseline in the lines without PADI1 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises IL20RA's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 3.80× lower at baseline in the lines without LINC01819 | 0.001 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises IL20RA's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 7.31× lower at baseline in the lines without CLIC5 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises IL20RA's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without UGT1A6 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises IL20RA's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 6.70× lower at baseline in the lines without TFF2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |

### Downstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 13, C 77. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | B | IL20RA activity raises SEPTIN9-DT's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without IL20RA | 3e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[NUDT4]] | B | IL20RA activity raises NUDT4's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without IL20RA | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[TSPOAP1-AS1]] | B | IL20RA activity raises TSPOAP1-AS1's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 1.66× lower at baseline in the lines without IL20RA | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[SNTB1]] | B | IL20RA activity raises SNTB1's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 3.72× lower at baseline in the lines without IL20RA | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[TJP2]] | B | IL20RA activity raises TJP2's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without IL20RA | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[MGST2]] | B | IL20RA activity raises MGST2's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.90× lower at baseline in the lines without IL20RA | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[PIWIL4]] | B | IL20RA activity raises PIWIL4's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 3.71× lower at baseline in the lines without IL20RA | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[MFSD6]] | B | IL20RA activity raises MFSD6's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without IL20RA | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[USP6NL]] | B | IL20RA activity raises USP6NL's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without IL20RA | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[SLC12A2]] | B | IL20RA activity raises SLC12A2's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without IL20RA | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[DNM3]] | B | IL20RA activity raises DNM3's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 1.41× lower at baseline in the lines without IL20RA | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | IL20RA activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express IL20RA (33) vs lines expressing it (15) | the lines without IL20RA: 0.88× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.870). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 47.9); signed map (63.2, 10.7). **Vector** length 73.5, 29.2% of its response variance represented; |z| ≥ 3 in 440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.4 | +0.7 |
|  | [[Ixazomib (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 20 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,999,971-137,045,180 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZCYTOR7, IL-20R1 |
| Gene groups (HGNC) | Interleukin receptors |
| Reactome | 3 pathways, smallest: Interleukin-20 family signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHF4](https://www.uniprot.org/uniprotkb/Q9UHF4) (Interleukin-20 receptor subunit alpha):

> The IL20RA/IL20RB dimer is a receptor for IL19, IL20 and IL24. The IL20RA/IL10RB dimer is a receptor for IL26.

**Summary**, from NCBI Gene [53832](https://www.ncbi.nlm.nih.gov/gene/53832):

> This gene encodes a member of the type II cytokine receptor family. The encoded protein is a subunit of the receptor for interleukin 20, a cytokine that may be involved in epidermal function. The interleukin 20 receptor is a heterodimeric complex consisting of the encoded protein and interleukin 20 receptor beta. This gene and interleukin 20 receptor beta are highly expressed in skin, and are upregulated in psoriasis. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:6003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6003) · Entrez [53832](https://www.ncbi.nlm.nih.gov/gene/53832) · UniProt [Q9UHF4](https://www.uniprot.org/uniprotkb/Q9UHF4) · Ensembl [ENSG00000016402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000016402)

## Data

Gene col 299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 299); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 299]; `tensor/DDL_lfc|DDL_z.npy` [299]; `embed/gene_vectors.npy` [299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 299 or target_col == 299). Every well: [[IL20RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL20RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
