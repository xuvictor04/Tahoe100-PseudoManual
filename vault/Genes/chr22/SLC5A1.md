---
symbol: "SLC5A1"
type: "gene"
col: 1885
ensembl_id: "ENSG00000100170"
name: "solute carrier family 5 member 1"
location: "22q12.3"
module: 55
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 95
direction_downstream: 130
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SLC5A1

*solute carrier family 5 member 1* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +11.2, q 2e-26, up in 1 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.493× (z -6.0, q 1e-06, down in 11 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKAP1]] (+0.77, fdr 7e-06), [[LINC03040]] (+0.75, fdr 7e-06), [[TMPRSS4]] (+0.75, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 95 arrows point to it, the strongest [[SMAD9]] → it (grade B ⚠); 130 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +11.2 | 2e-26 | 1/12 (HCT15) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.78×** | +11.1 | 2e-26 | 1/8 (SW480) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.09×** | +10.9 | 2e-25 | 1/6 (Panc 03.27) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +10.5 | 8e-24 | 0/5 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +9.2 | 3e-18 | 12/12 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +6.6 | 3e-09 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +6.4 | 1e-08 | 9/11 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +6.0 | 2e-07 | 2/9 (COLO 205, NCI-H2347) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +5.0 | 3e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.94×** | +4.7 | 1e-04 | 0/2 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.16×** | +4.6 | 2e-04 | 1/8 (KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.1 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.003 | 0/11 | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.005 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +3.5 | 0.017 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.027 | 0/11 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.067 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.493×** | -6.0 | 1e-06 | 11/12 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.608×** | -3.9 | 0.026 | 5/12 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.644×** | -3.5 | 0.078 | 0/12 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.645×** | -3.5 | 0.078 | 0/12 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.673×** | -3.4 | 0.082 | 5/12 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.668× | -3.3 | 0.11 | 0/12 | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.689× | -3.2 | 0.11 | 2/11 (Panc 03.27, NCI-H2347) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | 0.691× | -3.2 | 0.11 | 1/12 (NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 21.5 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0794× (z -19.0) |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0657× (z -20.5) |
| [[LS 180 (line)]] | wt | 50.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0448× (z -25.0) |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0924× (z -11.6) |
| [[LoVo (line)]] | wt | 4.11 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0587× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Drospirenone (drug)]] 0.5 µM 0.0682× (z -10.0) |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -13.8) |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 2.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.83× (z +9.0) | — |
| [[SW480 (line)]] | alt | 3.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.614 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKAP1]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC03040]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.75 | +0.72 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.74 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[AFAP1L2]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[ALDH1L1]] | +0.71 | +0.67 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[VILL]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[EDAR]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.70 | +0.72 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*95 arrows, 95 of them with an alert ⚠; grade A 0, B 4, C 91. Shown: the 12 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity lowers SLC5A1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 4.21× higher at baseline in the lines without SMAD9 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[TTC28]] | B | TTC28 activity lowers SLC5A1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.76× higher at baseline in the lines without TTC28 | 0.041 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[ZNF860]] | B | ZNF860 activity raises SLC5A1's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without ZNF860 | 0.075 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises SLC5A1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.08× lower at baseline in the lines without PLEKHG1 | 0.097 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LINC01559]] | C | LINC01559 activity raises SLC5A1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 5.42× lower at baseline in the lines without LINC01559 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises SLC5A1's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 4.82× lower at baseline in the lines without VWA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises SLC5A1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.48× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises SLC5A1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.80× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises SLC5A1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 3.37× lower at baseline in the lines without LINC03040 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises SLC5A1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.44× lower at baseline in the lines without MAL2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises SLC5A1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.44× lower at baseline in the lines without B3GNT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises SLC5A1's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 3.93× lower at baseline in the lines without ANKRD22 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |

### Downstream of this gene

*130 arrows, 130 of them with an alert ⚠; grade A 0, B 42, C 88. Shown: the 12 strongest; 118 more arrows (118 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | SLC5A1 activity raises FAM83E's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 5.06× lower at baseline in the lines without SLC5A1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[TMC6]] | B | SLC5A1 activity raises TMC6's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.63× lower at baseline in the lines without SLC5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[FUT2]] | B | SLC5A1 activity raises FUT2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.23× lower at baseline in the lines without SLC5A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[ABHD11]] | B | SLC5A1 activity raises ABHD11's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.07× lower at baseline in the lines without SLC5A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[SDCBP2]] | B | SLC5A1 activity raises SDCBP2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 5.54× lower at baseline in the lines without SLC5A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[ARHGEF16]] | B | SLC5A1 activity raises ARHGEF16's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.37× lower at baseline in the lines without SLC5A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[PLS1]] | B | SLC5A1 activity raises PLS1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.75× lower at baseline in the lines without SLC5A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[EPS8L1]] | B | SLC5A1 activity raises EPS8L1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.37× lower at baseline in the lines without SLC5A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[PTK2B]] | B | SLC5A1 activity raises PTK2B's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.25× lower at baseline in the lines without SLC5A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[ACOT11]] | B | SLC5A1 activity raises ACOT11's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.60× lower at baseline in the lines without SLC5A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[TLDC2]] | B | SLC5A1 activity raises TLDC2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 2.57× lower at baseline in the lines without SLC5A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[MYO1D]] | B | SLC5A1 activity raises MYO1D's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.59× lower at baseline in the lines without SLC5A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 52.8); signed map (61.6, 10.0). **Vector** length 57.8, 23.0% of its response variance represented; |z| ≥ 3 in 342 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 5 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:32,043,261-32,113,029 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D22S675, NAGT, SGLT-1; previously SGLT1 |
| Gene groups (HGNC) | Solute carrier family 5 |
| Reactome | 6 pathways, smallest: Digestion and absorption; Cellular hexose transport; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [P13866](https://www.uniprot.org/uniprotkb/P13866) (Sodium/glucose cotransporter 1):

> Electrogenic Na(+)-coupled sugar symporter that actively transports D-glucose or D-galactose at the plasma membrane, with a Na(+) to sugar coupling ratio of 2:1. Transporter activity is driven by a transmembrane Na(+) electrochemical gradient set by the Na(+)/K(+) pump. Has a primary role in the transport of dietary monosaccharides from enterocytes to blood. Responsible for the absorption of D-glucose or D-galactose across the apical brush-border membrane of enterocytes, whereas basolateral …

**Summary**, from NCBI Gene [6523](https://www.ncbi.nlm.nih.gov/gene/6523):

> This gene encodes a member of the sodium-dependent glucose transporter (SGLT) family. The encoded integral membrane protein is the primary mediator of dietary glucose and galactose uptake from the intestinal lumen. Mutations in this gene have been associated with glucose-galactose malabsorption. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:11036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11036) · Entrez [6523](https://www.ncbi.nlm.nih.gov/gene/6523) · UniProt [P13866](https://www.uniprot.org/uniprotkb/P13866) · Ensembl [ENSG00000100170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100170)

## Data

Gene col 1885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1885); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1885]; `tensor/DDL_lfc|DDL_z.npy` [1885]; `embed/gene_vectors.npy` [1885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1885 or target_col == 1885). Every well: [[SLC5A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC5A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
