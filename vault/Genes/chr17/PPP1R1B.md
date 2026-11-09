---
symbol: "PPP1R1B"
type: "gene"
col: 5242
ensembl_id: "ENSG00000131771"
name: "protein phosphatase 1 regulatory inhibitor subunit 1B"
location: "17q12"
module: 44
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 13
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 68
direction_downstream: 82
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PPP1R1B

*protein phosphatase 1 regulatory inhibitor subunit 1B* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.73× (z +13.8, q 8e-41, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +5.9, q 6e-07, up in 4 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.440× (z -5.3, q 5e-05, down in 9 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 0.0620×, COLO 205 0.0562×, KATO III 0.131×, LoVo 0.208×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (COLO 205 0.0102×, LS 180 0.0462×, KATO III 0.0510×, LoVo 0.144×); [[Bortezomib (drug)]] 0.05 µM in 2 lines (KATO III 0.0680×, COLO 205 0.0568×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.152×, KATO III 0.143×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.222×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC1]] (+0.87, fdr 7e-06), [[MUC5B]] (+0.85, fdr 7e-06), [[GPA33]] (+0.85, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 68 arrows point to it, the strongest [[MUC5B]] → it (grade C ⚠); 82 go from it, the strongest it → [[FUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.73×** | +13.8 | 8e-41 | 7/9 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.21×** | +12.9 | 2e-35 | 3/4 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.59×** | +9.5 | 3e-19 | 4/6 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.9 | 6e-07 | 4/10 (SK-MEL-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.9 | 1e-04 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.1 | 0.005 | 0/10 | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.54×** | +4.0 | 0.005 | 1/9 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.49×** | +3.9 | 0.007 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +3.9 | 0.007 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.33×** | +3.6 | 0.017 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.5 | 0.024 | 1/9 (AsPC-1) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.65×** | +3.4 | 0.033 | 1/8 (SW1417) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Silodosin (drug)]] 5 µM |  | **1.64×** | +3.2 | 0.054 | 2/10 (SK-MEL-2, HT-29) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 0.0620×, COLO 205 0.0562×, KATO III 0.131×, LoVo 0.208×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (COLO 205 0.0102×, LS 180 0.0462×, KATO III 0.0510×, LoVo 0.144×); [[Bortezomib (drug)]] 0.05 µM in 2 lines (KATO III 0.0680×, COLO 205 0.0568×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.152×, KATO III 0.143×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -5.3 | 5e-05 | 9/11 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.583× | -3.4 | 0.21 | 0/11 | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.712× | -3.3 | 0.22 | 4/11 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0102× (z -21.3) |
| [[KATO III (line)]] | alt | 82.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0510× (z -15.1) |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -21.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0462× (z -16.6) |
| [[LoVo (line)]] | wt | 13.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -9.3) |
| [[BT-474 (line)]] | alt | 8.91 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0923× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0499× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.609 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC1]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[MUC5B]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[FXYD3]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.79 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.78 | +0.84 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.78 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[GPX2]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[PHGR1]] | +0.77 | +0.62 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 0, C 68. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC5B]] | C | MUC5B activity raises PPP1R1B's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 4.24× lower at baseline in the lines without MUC5B | 0.001 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises PPP1R1B's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 7.28× lower at baseline in the lines without NPSR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises PPP1R1B's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 5.63× lower at baseline in the lines without PLA2G2A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises PPP1R1B's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 5.19× lower at baseline in the lines without CEACAM5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises PPP1R1B's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 6.57× lower at baseline in the lines without ATP10B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises PPP1R1B's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 4.88× lower at baseline in the lines without PHGR1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises PPP1R1B's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 5.37× lower at baseline in the lines without MUC13 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises PPP1R1B's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.41× lower at baseline in the lines without CDH17 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises PPP1R1B's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.65× lower at baseline in the lines without LGALS4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises PPP1R1B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 5.45× lower at baseline in the lines without CLRN3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises PPP1R1B's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without LAD1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises PPP1R1B's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.26× lower at baseline in the lines without TMEM139 | 0.012 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 9, C 73. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | PPP1R1B activity raises FUT2's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.87× lower at baseline in the lines without PPP1R1B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[PLS1]] | B | PPP1R1B activity raises PLS1's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without PPP1R1B | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[CTSH]] | B | PPP1R1B activity raises CTSH's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 1.90× lower at baseline in the lines without PPP1R1B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[CALML4]] | B | PPP1R1B activity raises CALML4's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 1.69× lower at baseline in the lines without PPP1R1B | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| cells under [[Trifluridine (drug)]] 5 µM | B | PPP1R1B activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express PPP1R1B (37) vs lines expressing it (11) | the lines without PPP1R1B: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[CMTM3]] | B | PPP1R1B activity lowers CMTM3's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.70× higher at baseline in the lines without PPP1R1B | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[RSPH1]] | B | PPP1R1B activity raises RSPH1's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.04× lower at baseline in the lines without PPP1R1B | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[MANSC1]] | B | PPP1R1B activity raises MANSC1's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.46× lower at baseline in the lines without PPP1R1B | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[FAM3B]] | B | PPP1R1B activity raises FAM3B's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.17× lower at baseline in the lines without PPP1R1B | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[MUC13]] | C | PPP1R1B activity raises MUC13's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 9.42× lower at baseline in the lines without PPP1R1B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | PPP1R1B activity raises CDH17's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 5.29× lower at baseline in the lines without PPP1R1B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[MYO7B]] | C | PPP1R1B activity raises MYO7B's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 4.90× lower at baseline in the lines without PPP1R1B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 51.0); signed map (64.3, 5.8). **Vector** length 56.5, 25.2% of its response variance represented; |z| ≥ 3 in 314 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.61 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.61 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.61 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +0.6 |
| fall | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,626,740-39,636,626 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DARPP-32, FLJ20940 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Reactome | 5 pathways, smallest: DARPP-32 events; Opioid Signalling; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UD71](https://www.uniprot.org/uniprotkb/Q9UD71) (Protein phosphatase 1 regulatory subunit 1B):

> Inhibitor of protein-phosphatase 1.

**Summary**, from NCBI Gene [84152](https://www.ncbi.nlm.nih.gov/gene/84152):

> This gene encodes a bifunctional signal transduction molecule. Dopaminergic and glutamatergic receptor stimulation regulates its phosphorylation and function as a kinase or phosphatase inhibitor. As a target for dopamine, this gene may serve as a therapeutic target for neurologic and psychiatric disorders. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:9287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9287) · Entrez [84152](https://www.ncbi.nlm.nih.gov/gene/84152) · UniProt [Q9UD71](https://www.uniprot.org/uniprotkb/Q9UD71) · Ensembl [ENSG00000131771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131771)

## Data

Gene col 5242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5242); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5242]; `tensor/DDL_lfc|DDL_z.npy` [5242]; `embed/gene_vectors.npy` [5242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5242 or target_col == 5242). Every well: [[PPP1R1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
