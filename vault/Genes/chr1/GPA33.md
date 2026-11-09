---
symbol: "GPA33"
type: "gene"
col: 6690
ensembl_id: "ENSG00000143167"
name: "glycoprotein A33"
location: "1q24.1"
module: 44
arm: "+"
pooled_cpm: 4.73
n_lines_expressing: 9
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 66
direction_downstream: 82
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# GPA33

*glycoprotein A33* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 22.5× (z +29.7, q 0e+00, up in 5 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0491×, LoVo 0.193×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0242×, LS 180 0.0499×); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.123×, LoVo 0.119×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.169×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM3D]] (+0.87, fdr 7e-06), [[NPSR1]] (+0.85, fdr 7e-06), [[PPP1R1B]] (+0.85, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 82 go from it, the strongest it → [[FUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **22.5×** | +29.7 | 0e+00 | 5/7 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.20×** | +11.1 | 2e-26 | 2/3 (AsPC-1, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +9.8 | 3e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +7.5 | 1e-11 | 1/3 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +7.2 | 5e-11 | 1/7 (HT-29) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.51×** | +6.2 | 5e-08 | 2/7 (HCT15, HT-29) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.1 | 7e-08 | 1/7 (SW1417) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +6.1 | 8e-08 | 0/7 | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.24×** | +5.5 | 3e-06 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.8 | 1e-04 | 0/4 | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.41×** | +4.3 | 7e-04 | 0/1 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.56×** | +4.2 | 0.001 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 1/7 (AsPC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.8 | 0.005 | 1/6 (AsPC-1) | top dose only | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.32×** | +3.8 | 0.005 | 1/4 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.014 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.015 | 1/7 (HCT15) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.066 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.56×** | +2.9 | 0.086 | 0/5 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0491×, LoVo 0.193×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0242×, LS 180 0.0499×); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.123×, LoVo 0.119×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.169×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.586× | -3.6 | 0.20 | 6/7 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ivermectin (drug)]] 5 µM |  | 0.638× | -3.0 | 0.70 | 0/7 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 143 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0491× (z -20.8) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0242× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 4.64 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.0323× (z -8.9) |
| [[A-172 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.775 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3D]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.85 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.81 | +0.81 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.80 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.79 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.79 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[HEPH]] | +0.76 | +0.79 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 1, C 65. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPA33's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPSR1]] | C | NPSR1 activity raises GPA33's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.26× lower at baseline in the lines without NPSR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises GPA33's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.35× lower at baseline in the lines without PLA2G2A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises GPA33's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.05× lower at baseline in the lines without CDH17 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises GPA33's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.30× lower at baseline in the lines without CEACAM5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises GPA33's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.22× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises GPA33's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.01× lower at baseline in the lines without MUC13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises GPA33's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.83× lower at baseline in the lines without LINC02582 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises GPA33's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 5.86× lower at baseline in the lines without PHGR1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises GPA33's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.18× lower at baseline in the lines without MUC6 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises GPA33's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.00× lower at baseline in the lines without LINC02474 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises GPA33's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 5.30× lower at baseline in the lines without FAM3D | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 13, C 69. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | GPA33 activity raises FUT2's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.62× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[NOSTRIN]] | B | GPA33 activity raises NOSTRIN's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 4.64× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[ABHD11]] | B | GPA33 activity raises ABHD11's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.15× lower at baseline in the lines without GPA33 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[MUC12]] | B | GPA33 activity raises MUC12's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.50× lower at baseline in the lines without GPA33 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[IL22RA1]] | B | GPA33 activity raises IL22RA1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.86× lower at baseline in the lines without GPA33 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC02580]] | B | GPA33 activity raises LINC02580's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 2.19× lower at baseline in the lines without GPA33 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[HTR1D]] | B | GPA33 activity raises HTR1D's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 2.26× lower at baseline in the lines without GPA33 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[RSPH1]] | B | GPA33 activity raises RSPH1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 2.93× lower at baseline in the lines without GPA33 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[MROH7]] | B | GPA33 activity raises MROH7's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.43× lower at baseline in the lines without GPA33 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CDC42EP5]] | B | GPA33 activity raises CDC42EP5's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without GPA33 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CMTM3]] | B | GPA33 activity lowers CMTM3's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.40× higher at baseline in the lines without GPA33 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CYP2S1]] | B | GPA33 activity raises CYP2S1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 4.94× lower at baseline in the lines without GPA33 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 50.6); signed map (64.4, 6.3). **Vector** length 43.8, 23.5% of its response variance represented; |z| ≥ 3 in 192 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.64 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.64 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +29.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | +1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein A33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:167,052,836-167,166,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A33 |
| Gene groups (HGNC) | V-set domain containing; Immunoglobulin like domain containing; IgCAM CXADR-related subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99795](https://www.uniprot.org/uniprotkb/Q99795) (Cell surface A33 antigen):

> May play a role in cell-cell recognition and signaling.

**Summary**, from NCBI Gene [10223](https://www.ncbi.nlm.nih.gov/gene/10223):

> The glycoprotein encoded by this gene is a cell surface antigen that is expressed in greater than 95% of human colon cancers. The open reading frame encodes a 319-amino acid polypeptide having a putative secretory signal sequence and 3 potential glycosylation sites. The predicted mature protein has a 213-amino acid extracellular region, a single transmembrane domain, and a 62-amino acid intracellular tail. The sequence of the extracellular region contains 2 domains characteristic of the CD2 …

**Accessions** — [HGNC:4445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4445) · Entrez [10223](https://www.ncbi.nlm.nih.gov/gene/10223) · UniProt [Q99795](https://www.uniprot.org/uniprotkb/Q99795) · Ensembl [ENSG00000143167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143167)

## Data

Gene col 6690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6690); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6690]; `tensor/DDL_lfc|DDL_z.npy` [6690]; `embed/gene_vectors.npy` [6690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6690 or target_col == 6690). Every well: [[GPA33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPA33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
