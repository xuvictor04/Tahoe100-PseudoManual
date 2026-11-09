---
symbol: "CDH17"
type: "gene"
col: 1240
ensembl_id: "ENSG00000079112"
name: "cadherin 17"
location: "8q22.1"
module: 44
arm: "+"
pooled_cpm: 21.45
n_lines_expressing: 10
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 75
direction_downstream: 114
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CDH17

*cadherin 17* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.25× (z +14.3, q 2e-43, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +10.5, q 2e-23, up in 1 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (COLO 205 0.197×, LoVo 0.328×, LS 180 0.402×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.146×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.205×; ⚠ cell-cycle shift, explains ~64% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.0868×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.264×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.84, fdr 7e-06), [[MUC13]] (+0.83, fdr 7e-06), [[TSPAN8]] (+0.81, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[NPSR1]] → it (grade C ⚠); 114 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.25×** | +14.3 | 2e-43 | 3/7 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +12.9 | 2e-35 | 3/5 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +11.7 | 2e-29 | 3/5 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +10.5 | 2e-23 | 1/8 (AsPC-1) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.83×** | +8.4 | 5e-15 | 2/8 (AsPC-1, SW1417) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.16×** | +5.9 | 3e-07 | 2/3 (AsPC-1, SW1417) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.4 | 5e-06 | 3/8 (KATO III, SW1417, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.003 | 0/8 | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 5/8 (AsPC-1, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.8 | 0.008 | 1/8 (NCI-H1573) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.45×** | +3.7 | 0.013 | 1/8 (NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 3/8 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.018 | 0/8 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.040 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +3.3 | 0.040 | 3/8 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.041 | 4/8 (NCI-H1573, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.041 | 2/8 (KATO III, SW1417) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (COLO 205 0.197×, LoVo 0.328×, LS 180 0.402×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.146×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.205×; ⚠ cell-cycle shift, explains ~64% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.0868×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.264×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -3.4 | 0.34 | 0/8 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.716× | -3.1 | 0.34 | 0/8 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.34 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 320 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -10.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.9) |
| [[LoVo (line)]] | wt | 162 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -11.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -9.4) |
| [[COLO 205 (line)]] | alt | 63.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -9.8) |
| [[HT-29 (line)]] | alt | 7.37 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0868× (z -9.0) |
| [[A-172 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.84 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.83 | +0.73 / +0.81 | both halves | 7e-06 | STRING 575 |
| [[TSPAN8]] | +0.81 | +0.75 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.79 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MUC17]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[NPNT]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 | STRING 762 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 0, C 75. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPSR1]] | C | NPSR1 activity raises CDH17's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 13.09× lower at baseline in the lines without NPSR1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises CDH17's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 9.68× lower at baseline in the lines without MUC13 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises CDH17's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 11.47× lower at baseline in the lines without GPA33 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises CDH17's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 6.72× lower at baseline in the lines without CEACAM5 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises CDH17's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.54× lower at baseline in the lines without GCNT3 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises CDH17's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 7.82× lower at baseline in the lines without TRIM31 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[VIL1]] | C | VIL1 activity raises CDH17's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 4.76× lower at baseline in the lines without VIL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises CDH17's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 5.89× lower at baseline in the lines without LINC02582 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises CDH17's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 5.29× lower at baseline in the lines without PPP1R1B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises CDH17's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 10.47× lower at baseline in the lines without PHGR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises CDH17's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 7.51× lower at baseline in the lines without LGALS4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises CDH17's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 4.53× lower at baseline in the lines without MYO7B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |

### Downstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 21, C 93. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | CDH17 activity raises NOSTRIN's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.91× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[RHOU]] | B | CDH17 activity raises RHOU's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.64× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[RSPH1]] | B | CDH17 activity raises RSPH1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.06× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[MUC12]] | B | CDH17 activity raises MUC12's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.47× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[GCOM1]] | B | CDH17 activity raises GCOM1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[C4orf19]] | B | CDH17 activity raises C4orf19's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.10× lower at baseline in the lines without CDH17 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[TNFRSF21]] | B | CDH17 activity raises TNFRSF21's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.10× lower at baseline in the lines without CDH17 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[CALML4]] | B | CDH17 activity raises CALML4's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 2.21× lower at baseline in the lines without CDH17 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[FUT2]] | B | CDH17 activity raises FUT2's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.34× lower at baseline in the lines without CDH17 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[PLS1]] | B | CDH17 activity raises PLS1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.56× lower at baseline in the lines without CDH17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[ABHD11]] | B | CDH17 activity raises ABHD11's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.05× lower at baseline in the lines without CDH17 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[GAREM1]] | B | CDH17 activity raises GAREM1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.52× lower at baseline in the lines without CDH17 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 51.7); signed map (63.4, 5.7). **Vector** length 41.0, 20.0% of its response variance represented; |z| ≥ 3 in 169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.59 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.59 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.1 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Ixazomib (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,127,162-94,217,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPT-1, cadherin |
| Gene groups (HGNC) | 7D cadherins |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12864](https://www.uniprot.org/uniprotkb/Q12864) (Cadherin-17):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. LI-cadherin may have a role in the morphological organization of liver and intestine. Involved in intestinal peptide transport.

**Summary**, from NCBI Gene [1015](https://www.ncbi.nlm.nih.gov/gene/1015):

> This gene is a member of the cadherin superfamily, genes encoding calcium-dependent, membrane-associated glycoproteins. The encoded protein is cadherin-like, consisting of an extracellular region, containing 7 cadherin domains, and a transmembrane region but lacking the conserved cytoplasmic domain. The protein is a component of the gastrointestinal tract and pancreatic ducts, acting as an intestinal proton-dependent peptide transporter in the first step in oral absorption of many medically …

**Accessions** — [HGNC:1756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1756) · Entrez [1015](https://www.ncbi.nlm.nih.gov/gene/1015) · UniProt [Q12864](https://www.uniprot.org/uniprotkb/Q12864) · Ensembl [ENSG00000079112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079112)

## Data

Gene col 1240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1240); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1240]; `tensor/DDL_lfc|DDL_z.npy` [1240]; `embed/gene_vectors.npy` [1240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1240 or target_col == 1240). Every well: [[CDH17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
