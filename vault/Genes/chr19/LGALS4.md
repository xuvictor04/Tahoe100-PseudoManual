---
symbol: "LGALS4"
type: "gene"
col: 10156
ensembl_id: "ENSG00000171747"
name: "galectin 4"
location: "19q13.2"
module: 44
arm: "+"
pooled_cpm: 15.54
n_lines_expressing: 11
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 89
direction_downstream: 116
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# LGALS4

*galectin 4* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.13× (z +12.4, q 2e-32, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +11.6, q 2e-28, up in 2 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.506× (z -6.2, q 3e-07, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A1]] (+0.85, fdr 7e-06), [[NPSR1]] (+0.84, fdr 7e-06), [[GPA33]] (+0.83, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 89 arrows point to it, the strongest [[MUC13]] → it (grade C ⚠); 116 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.13×** | +12.4 | 2e-32 | 2/7 (LoVo, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +11.6 | 2e-28 | 2/9 (PANC-1, HEC-1-A) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +10.5 | 1e-23 | 2/9 (AsPC-1, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +6.9 | 8e-10 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.9 | 4e-07 | 1/9 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.7 | 1e-06 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.003 | 3/9 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.010 | 3/9 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.5 | 0.026 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.5 | 0.027 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.032 | 4/9 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.4 | 0.032 | 3/9 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.042 | 5/9 (LS 180, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -6.2 | 3e-07 | 9/9 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.530×** | -5.8 | 2e-06 | 7/9 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -5.8 | 2e-06 | 9/9 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.607×** | -4.5 | 8e-04 | 8/9 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.589×** | -4.4 | 1e-03 | 1/9 (HEC-1-A) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -4.4 | 1e-03 | 9/9 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -3.9 | 0.007 | 8/9 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.665×** | -3.7 | 0.015 | 2/9 (PANC-1, AsPC-1) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.685×** | -3.2 | 0.092 | 3/9 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.701× | -3.1 | 0.10 | 4/9 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.712× | -3.1 | 0.10 | 5/9 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.694× | -3.1 | 0.10 | 1/9 (PANC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 161 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.1) |
| [[HT-29 (line)]] | alt | 193 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.7) |
| [[COLO 205 (line)]] | alt | 65.5 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.5) |
| [[KATO III (line)]] | alt | 93.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.6) |
| [[PANC-1 (line)]] | alt | 8.45 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0474× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0615× (z -13.9) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.139× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.5) |
| [[A-172 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.84 | +0.84 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.83 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.79 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.79 | +0.72 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CLDN3]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.78 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[PRR15]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 0, C 89. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC13]] | C | MUC13 activity raises LGALS4's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 10.07× lower at baseline in the lines without MUC13 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises LGALS4's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.91× lower at baseline in the lines without CDH17 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises LGALS4's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 12.97× lower at baseline in the lines without NPSR1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises LGALS4's level | lines that do not express LYZ (40) vs lines expressing it (10) | 8.10× lower at baseline in the lines without LYZ | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises LGALS4's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 10.01× lower at baseline in the lines without CLRN3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises LGALS4's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 13.20× lower at baseline in the lines without MUC17 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises LGALS4's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.82× lower at baseline in the lines without GCNT3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises LGALS4's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 10.08× lower at baseline in the lines without PHGR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises LGALS4's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 7.95× lower at baseline in the lines without TRIM31 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises LGALS4's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 8.24× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises LGALS4's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 6.33× lower at baseline in the lines without CEACAM5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises LGALS4's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 6.70× lower at baseline in the lines without LINC01559 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*116 arrows, 116 of them with an alert ⚠; grade A 0, B 23, C 93. Shown: the 12 strongest; 104 more arrows (104 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | LGALS4 activity raises MUC12's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.27× lower at baseline in the lines without LGALS4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[NOSTRIN]] | B | LGALS4 activity raises NOSTRIN's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.34× lower at baseline in the lines without LGALS4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[ABHD11]] | B | LGALS4 activity raises ABHD11's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.24× lower at baseline in the lines without LGALS4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[SDCBP2]] | B | LGALS4 activity raises SDCBP2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 5.61× lower at baseline in the lines without LGALS4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[CALML4]] | B | LGALS4 activity raises CALML4's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without LGALS4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[IL22RA1]] | B | LGALS4 activity raises IL22RA1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.44× lower at baseline in the lines without LGALS4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[LINC02580]] | B | LGALS4 activity raises LINC02580's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without LGALS4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[FUT2]] | B | LGALS4 activity raises FUT2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without LGALS4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[EPS8L1]] | B | LGALS4 activity raises EPS8L1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.33× lower at baseline in the lines without LGALS4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[BICDL2]] | B | LGALS4 activity raises BICDL2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.38× lower at baseline in the lines without LGALS4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[SPIRE2]] | B | LGALS4 activity raises SPIRE2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.10× lower at baseline in the lines without LGALS4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[PLS1]] | B | LGALS4 activity raises PLS1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.44× lower at baseline in the lines without LGALS4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.858). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 51.4); signed map (63.5, 5.7). **Vector** length 63.5, 34.4% of its response variance represented; |z| ≥ 3 in 285 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.63 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.63 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -5.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | galectin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,801,671-38,812,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAL4 |
| Gene groups (HGNC) | Galectins |
| Matched by | ensembl_id |

**Function**, from UniProt [P56470](https://www.uniprot.org/uniprotkb/P56470) (Galectin-4):

> Galectin that binds lactose and a related range of sugars. May be involved in the assembly of adherens junctions.

**Summary**, from NCBI Gene [3960](https://www.ncbi.nlm.nih.gov/gene/3960):

> The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. The expression of this gene is restricted to small intestine, colon, and rectum, and it is underexpressed in colorectal cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6565) · Entrez [3960](https://www.ncbi.nlm.nih.gov/gene/3960) · UniProt [P56470](https://www.uniprot.org/uniprotkb/P56470) · Ensembl [ENSG00000171747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171747)

## Data

Gene col 10156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10156); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10156]; `tensor/DDL_lfc|DDL_z.npy` [10156]; `embed/gene_vectors.npy` [10156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10156 or target_col == 10156). Every well: [[LGALS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
