---
symbol: "MYO7B"
type: "gene"
col: 9890
ensembl_id: "ENSG00000169994"
name: "myosin VIIB"
location: "2q14.3"
module: 55
arm: "+"
pooled_cpm: 10.36
n_lines_expressing: 14
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 83
direction_downstream: 105
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MYO7B

*myosin VIIB* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.94× (z +12.9, q 2e-35, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +12.9, q 2e-35, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.486× (z -7.0, q 1e-09, down in 10 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.85, fdr 7e-06), [[GCNT3]] (+0.84, fdr 7e-06), [[ABO]] (+0.82, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 83 arrows point to it, the strongest [[LPAR5]] → it (grade B ⚠); 105 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +12.9 | 2e-35 | 1/7 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +12.9 | 2e-35 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.1 | 3e-10 | 2/9 (J82, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +4.9 | 1e-04 | 1/7 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.002 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.013 | 6/11 (LoVo, LS 180, …) | two highest doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.68×** | +3.6 | 0.023 | 1/10 (A-172) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.10 | 0/11 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.85× | +3.2 | 0.10 | 5/10 (COLO 205, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.80× | +3.0 | 0.14 | 0/6 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.486×** | -7.0 | 1e-09 | 10/11 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -5.1 | 9e-05 | 9/11 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -4.9 | 2e-04 | 7/11 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.605×** | -4.7 | 4e-04 | 8/11 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -4.1 | 0.004 | 6/11 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.600×** | -4.0 | 0.006 | 2/11 (J82, SW480) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.676×** | -3.8 | 0.011 | 8/11 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.666×** | -3.7 | 0.013 | 0/11 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.018 | 9/11 (COLO 205, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.018 | 0/11 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.709×** | -3.3 | 0.043 | 3/11 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.547×** | -3.1 | 0.100 | 7/11 (LS 180, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 26.2 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0544× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -16.2) |
| [[LS 180 (line)]] | wt | 120 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0752× (z -26.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -15.7) |
| [[COLO 205 (line)]] | alt | 99.8 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -17.8) |
| [[LoVo (line)]] | wt | 29.8 | 0 | 12 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0664× (z -17.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.105× (z -15.1) |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.9) |
| [[SW480 (line)]] | alt | 3.43 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0694× (z -10.1) |
| [[A-172 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.968 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.84 | +0.80 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.82 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 | same gene group |
| [[TMPRSS2]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.80 | +0.77 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.80 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*83 arrows, 83 of them with an alert ⚠; grade A 0, B 1, C 82. Shown: the 12 strongest; 71 more arrows (71 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR5]] | B | LPAR5 activity raises MYO7B's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without LPAR5 | 0.088 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[CDH17]] | C | CDH17 activity raises MYO7B's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.07× lower at baseline in the lines without CDH17 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises MYO7B's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 8.67× lower at baseline in the lines without MUC13 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises MYO7B's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 11.89× lower at baseline in the lines without GPA33 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises MYO7B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 9.55× lower at baseline in the lines without CLRN3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises MYO7B's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.08× lower at baseline in the lines without GCNT3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises MYO7B's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 10.27× lower at baseline in the lines without NPSR1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises MYO7B's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 7.03× lower at baseline in the lines without LGALS4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises MYO7B's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 6.62× lower at baseline in the lines without LINC01559 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises MYO7B's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 4.90× lower at baseline in the lines without PPP1R1B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises MYO7B's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 5.08× lower at baseline in the lines without CEACAM5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises MYO7B's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.30× lower at baseline in the lines without TMPRSS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |

### Downstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 25, C 80. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | MYO7B activity raises TLDC2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without MYO7B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[SDCBP2]] | B | MYO7B activity raises SDCBP2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 3.30× lower at baseline in the lines without MYO7B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[NUDT4]] | B | MYO7B activity raises NUDT4's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.75× lower at baseline in the lines without MYO7B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[CRYBG2]] | B | MYO7B activity raises CRYBG2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.52× lower at baseline in the lines without MYO7B | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[NOSTRIN]] | B | MYO7B activity raises NOSTRIN's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without MYO7B | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[MUC12]] | B | MYO7B activity raises MUC12's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without MYO7B | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[LPAR5]] | B | MYO7B activity raises LPAR5's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without MYO7B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[IL22RA1]] | B | MYO7B activity raises IL22RA1's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.13× lower at baseline in the lines without MYO7B | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[MUC3A]] | B | MYO7B activity raises MUC3A's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without MYO7B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[CALML4]] | B | MYO7B activity raises CALML4's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without MYO7B | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[PPARG]] | B | MYO7B activity raises PPARG's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without MYO7B | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[SMAD9]] | B | MYO7B activity lowers SMAD9's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.56× higher at baseline in the lines without MYO7B | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.3, 51.0); signed map (63.2, 8.2). **Vector** length 62.2, 27.3% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin VIIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,535,683-127,637,729 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myosin heavy chains, class VII; FERM domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIF6](https://www.uniprot.org/uniprotkb/Q6PIF6) (Unconventional myosin-VIIb):

> Myosins are actin-based motor molecules with ATPase activity. Their highly divergent tails are presumed to bind to membranous compartments, which would be moved relative to actin filaments. As part of the intermicrovillar adhesion complex/IMAC plays a role in epithelial brush border differentiation, controlling microvilli organization and length. May link the complex to the actin core bundle of microvilli.

**Summary**, from NCBI Gene [4648](https://www.ncbi.nlm.nih.gov/gene/4648):

> The protein encoded by this gene is found in brush border microvilli of epithelial cells in the intestines and kidneys. The encoded protein is involved in linking protocadherins to the actin cytoskeleton and is essential for proper microvilli function. This protein aids in the accumulation of intermicrovillar adhesion components such as harmonin and ANKS4B, and this accumulation is necessary for normal brush border action. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:7607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7607) · Entrez [4648](https://www.ncbi.nlm.nih.gov/gene/4648) · UniProt [Q6PIF6](https://www.uniprot.org/uniprotkb/Q6PIF6) · Ensembl [ENSG00000169994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169994)

## Data

Gene col 9890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9890); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9890]; `tensor/DDL_lfc|DDL_z.npy` [9890]; `embed/gene_vectors.npy` [9890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9890 or target_col == 9890). Every well: [[MYO7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
