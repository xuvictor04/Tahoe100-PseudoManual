---
symbol: "NPSR1"
type: "gene"
col: 11907
ensembl_id: "ENSG00000187258"
name: "neuropeptide S receptor 1"
location: "7p14.3"
module: 73
arm: "+"
pooled_cpm: 82.21
n_lines_expressing: 8
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 82
direction_downstream: 144
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# NPSR1

*neuropeptide S receptor 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +9.2, q 1e-17, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +5.3, q 2e-05, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.504× (z -5.7, q 9e-06, down in 5 of 6 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.89, fdr 7e-06), [[TPRXL]] (+0.89, fdr 7e-06), [[FAM3D]] (+0.88, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[CDH17]] → it (grade C ⚠); 144 go from it, the strongest it → [[SDCBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +9.2 | 1e-17 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +7.4 | 4e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.3 | 2e-05 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +4.7 | 4e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.033 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.54×** | +3.6 | 0.034 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.19 | 0/6 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -5.7 | 9e-06 | 5/6 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.541×** | -5.1 | 1e-04 | 6/6 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -4.4 | 0.002 | 6/6 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -3.8 | 0.019 | 6/6 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.650×** | -3.5 | 0.044 | 6/6 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.636×** | -3.5 | 0.051 | 0/6 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.677× | -3.2 | 0.10 | 5/6 (LoVo, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 1,129 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0253× (z -26.0) |
| [[LoVo (line)]] | wt | 158 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -24.0) |
| [[COLO 205 (line)]] | alt | 216 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -16.0) |
| [[KATO III (line)]] | alt | 1,415 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0220× (z -28.1) |
| [[AsPC-1 (line)]] | alt | 414 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0217× (z -24.5) |
| [[HT-29 (line)]] | alt | 50.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -13.6) |
| [[A-172 (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.89 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.89 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.88 | +0.83 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.85 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.84 | +0.84 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.84 | +0.89 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.84 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[MUC17]] | +0.84 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.83 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TPTEP1-1]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[C4BPB]] | +0.81 | +0.83 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 0, C 82. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH17]] | C | CDH17 activity raises NPSR1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 12.92× lower at baseline in the lines without CDH17 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises NPSR1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 10.09× lower at baseline in the lines without CEACAM5 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises NPSR1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 12.40× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[REG4]] | C | REG4 activity raises NPSR1's level | lines that do not express REG4 (43) vs lines expressing it (7) | 22.07× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises NPSR1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 8.31× lower at baseline in the lines without GCNT3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises NPSR1's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 21.45× lower at baseline in the lines without MUC17 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises NPSR1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 7.08× lower at baseline in the lines without SLC44A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises NPSR1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 12.50× lower at baseline in the lines without CLRN3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises NPSR1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 8.69× lower at baseline in the lines without FAM3D | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises NPSR1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 5.47× lower at baseline in the lines without UGT1A6 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises NPSR1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 9.91× lower at baseline in the lines without LGALS4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises NPSR1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 8.38× lower at baseline in the lines without GPA33 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*144 arrows, 144 of them with an alert ⚠; grade A 0, B 26, C 118. Shown: the 12 strongest; 132 more arrows (132 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDCBP2]] | B | NPSR1 activity raises SDCBP2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 10.86× lower at baseline in the lines without NPSR1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[NOSTRIN]] | B | NPSR1 activity raises NOSTRIN's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 6.28× lower at baseline in the lines without NPSR1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[MUC12]] | B | NPSR1 activity raises MUC12's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.16× lower at baseline in the lines without NPSR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[IL22RA1]] | B | NPSR1 activity raises IL22RA1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.18× lower at baseline in the lines without NPSR1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[CALML4]] | B | NPSR1 activity raises CALML4's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.35× lower at baseline in the lines without NPSR1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[HTR1D]] | B | NPSR1 activity raises HTR1D's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.40× lower at baseline in the lines without NPSR1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[SEPTIN9-DT]] | B | NPSR1 activity raises SEPTIN9-DT's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.82× lower at baseline in the lines without NPSR1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[KLF3]] | B | NPSR1 activity raises KLF3's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 3.18× lower at baseline in the lines without NPSR1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[INPP1]] | B | NPSR1 activity raises INPP1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.08× lower at baseline in the lines without NPSR1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[CALML4]] | B | NPSR1 activity weakens CALML4's drug response | lines that do not express NPSR1 (42) vs lines expressing it (6) | the lines without NPSR1 respond 1.64× as strongly (z diff -0.97); strongest at Homoharringtonine 5 µM: 1.41x vs 0.39x (z diff -9.1) | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; target measured in part of the lines; both ways; artifact flags |
| [[LINC02580]] | B | NPSR1 activity raises LINC02580's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without NPSR1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[FUT2]] | B | NPSR1 activity raises FUT2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 3.47× lower at baseline in the lines without NPSR1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.8, 50.6); signed map (64.9, 7.7). **Vector** length 66.2, 47.1% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | neuropeptide S receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:34,658,218-34,878,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGR14, GPRA; previously GPR154 |
| Gene groups (HGNC) | Neuropeptide S receptor |
| Reactome | 7 pathways, smallest: Peptide ligand-binding receptors; G alpha (s) signalling events; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6W5P4](https://www.uniprot.org/uniprotkb/Q6W5P4) (Neuropeptide S receptor):

> G protein-coupled receptor for neuropeptide S (NPS). Receptor activation by NPS initiates a G(q)/GNAQ-dependent phospholipase C-activating signaling pathway, resulting in Ca(2+) mobilization from intracellular stores and increased intracellular Ca(2+) levels. In addition to this pathway, NPS binding to its receptor activates cAMP/PKA signal transduction. Finally, both pathways converge to activate ERK1/ERK2 phosphorylation and signaling cascade. Inhibits cell growth in response to NPS binding.

**Summary**, from NCBI Gene [387129](https://www.ncbi.nlm.nih.gov/gene/387129):

> This gene encodes a member of the vasopressin/oxytocin subfamily of G protein-coupled receptors. The encoded membrane protein acts as a receptor for neuropeptide S and affects a variety of cellular processes through its signaling. Increased expression of this gene in ciliated cells of the respiratory epithelium and in bronchial smooth muscle cells is associated with asthma. Polymorphisms in this gene have also been associated with asthma susceptibility, panic disorders, inflammatory bowel …

**Accessions** — [HGNC:23631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23631) · Entrez [387129](https://www.ncbi.nlm.nih.gov/gene/387129) · UniProt [Q6W5P4](https://www.uniprot.org/uniprotkb/Q6W5P4) · Ensembl [ENSG00000187258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187258)

## Data

Gene col 11907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11907); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11907]; `tensor/DDL_lfc|DDL_z.npy` [11907]; `embed/gene_vectors.npy` [11907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11907 or target_col == 11907). Every well: [[NPSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
