---
symbol: "MUC13"
type: "gene"
col: 10419
ensembl_id: "ENSG00000173702"
name: "mucin 13, cell surface associated"
location: "3q21.2"
module: 44
arm: "+"
pooled_cpm: 57.38
n_lines_expressing: 10
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 119
direction_downstream: 140
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MUC13

*mucin 13, cell surface associated* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +10.2, q 8e-22, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +6.6, q 5e-09, up in 6 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.578× (z -5.4, q 3e-05, down in 6 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.137×, HT-29 0.148×, COLO 205 0.206×, KATO III 0.182×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.132×, KATO III 0.109×, COLO 205 0.178×, HT-29 0.221×); [[Auranofin (drug)]] 5 µM in 2 lines (KATO III 0.119×, LoVo 0.254×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM31]] (+0.85, fdr 7e-06), [[CDH17]] (+0.83, fdr 7e-06), [[POF1B]] (+0.81, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 119 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 140 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +10.2 | 8e-22 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.2 | 1e-13 | 1/9 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +6.7 | 3e-09 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +6.6 | 5e-09 | 6/8 (LS 180, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.6 | 5e-04 | 1/9 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 9e-04 | 7/8 (AsPC-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 9e-04 | 3/9 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.3 | 0.001 | 2/8 (KATO III, AsPC-1) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.1 | 0.002 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.005 | 5/8 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.7 | 0.013 | 0/8 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.026 | 6/8 (AsPC-1, HT-29, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.029 | 7/9 (AsPC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.48×** | +3.3 | 0.034 | 2/8 (LoVo, SW1417) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.075 | 7/8 (AsPC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.075 | 4/8 (AsPC-1, COLO 205, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.081 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.137×, HT-29 0.148×, COLO 205 0.206×, KATO III 0.182×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.132×, KATO III 0.109×, COLO 205 0.178×, HT-29 0.221×); [[Auranofin (drug)]] 5 µM in 2 lines (KATO III 0.119×, LoVo 0.254×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -5.4 | 3e-05 | 6/8 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.712× | -3.3 | 0.17 | 4/8 (KATO III, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.3 | 0.17 | 0/9 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.711× | -3.2 | 0.17 | 0/8 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.725× | -3.2 | 0.17 | 0/8 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 149 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.4) |
| [[COLO 205 (line)]] | alt | 380 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -10.1) |
| [[LoVo (line)]] | wt | 583 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 55.5 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 6.36× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 270 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -8.7) |
| [[LS 180 (line)]] | wt | 476 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +10.2) | — |
| [[A-172 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM31]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.83 | +0.73 / +0.81 | both halves | 7e-06 | STRING 575 |
| [[POF1B]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.80 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ATP10B]] | +0.80 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.79 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.76 | +0.81 / +0.70 | both halves | 7e-06 | pathway: O-linked glycosylation; STRING 658 |
| [[PRR15L]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[HEPH]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[NPNT]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*119 arrows, 119 of them with an alert ⚠; grade A 0, B 7, C 112. Shown: the 12 strongest; 107 more arrows (107 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises MUC13's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without PLAAT4 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MUC13's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[MTUS1]] | B | MTUS1 activity raises MUC13's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.13× lower at baseline in the lines without MTUS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises MUC13's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.89× lower at baseline in the lines without ELF3-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises MUC13's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.13× lower at baseline in the lines without SHROOM3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[HNF4G]] | B | HNF4G activity raises MUC13's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without HNF4G | 0.093 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[STS]] | B | STS activity raises MUC13's level | lines that do not express STS (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without STS | 0.094 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[TRIM31]] | C | TRIM31 activity raises MUC13's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 16.92× lower at baseline in the lines without TRIM31 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises MUC13's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 14.08× lower at baseline in the lines without GCNT3 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises MUC13's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 18.09× lower at baseline in the lines without CDH17 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises MUC13's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 26.34× lower at baseline in the lines without PHGR1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises MUC13's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 16.44× lower at baseline in the lines without GPA33 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*140 arrows, 140 of them with an alert ⚠; grade A 0, B 33, C 107. Shown: the 12 strongest; 128 more arrows (128 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | MUC13 activity raises MUC12's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.79× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[FUT2]] | B | MUC13 activity raises FUT2's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.35× lower at baseline in the lines without MUC13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[PKDCC]] | B | MUC13 activity raises PKDCC's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.25× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[IL22RA1]] | B | MUC13 activity raises IL22RA1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.80× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[ELF3-AS1]] | B | MUC13 activity raises ELF3-AS1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.08× lower at baseline in the lines without MUC13 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[SLC37A1]] | B | MUC13 activity raises SLC37A1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.95× lower at baseline in the lines without MUC13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[MYH14]] | B | MUC13 activity raises MYH14's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 7.18× lower at baseline in the lines without MUC13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[CALML4]] | B | MUC13 activity raises CALML4's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.28× lower at baseline in the lines without MUC13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[SERINC5]] | B | MUC13 activity raises SERINC5's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.10× lower at baseline in the lines without MUC13 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[C4orf19]] | B | MUC13 activity raises C4orf19's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.74× lower at baseline in the lines without MUC13 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[TNFRSF21]] | B | MUC13 activity raises TNFRSF21's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 5.15× lower at baseline in the lines without MUC13 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[RSPH1]] | B | MUC13 activity raises RSPH1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.88× lower at baseline in the lines without MUC13 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 52.3); signed map (62.0, 4.9). **Vector** length 57.5, 32.4% of its response variance represented; |z| ≥ 3 in 244 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.67 to 4); *Aspirin ADME* (reactome, mean cos +0.67 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mucin 13, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:124,905,442-124,953,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DRCC1 |
| Gene groups (HGNC) | Mucins; SEA domain containing |
| Reactome | 18 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3R2](https://www.uniprot.org/uniprotkb/Q9H3R2) (Mucin-13):

> Epithelial and hemopoietic transmembrane mucin that may play a role in cell signaling.

**Summary**, from NCBI Gene [56667](https://www.ncbi.nlm.nih.gov/gene/56667):

> Epithelial mucins, such as MUC13, are a family of secreted and cell surface glycoproteins expressed by ductal and glandular epithelial tissues (Williams et al., 2001 [PubMed 11278439]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:7511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7511) · Entrez [56667](https://www.ncbi.nlm.nih.gov/gene/56667) · UniProt [Q9H3R2](https://www.uniprot.org/uniprotkb/Q9H3R2) · Ensembl [ENSG00000173702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173702)

## Data

Gene col 10419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10419); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10419]; `tensor/DDL_lfc|DDL_z.npy` [10419]; `embed/gene_vectors.npy` [10419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10419 or target_col == 10419). Every well: [[MUC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
