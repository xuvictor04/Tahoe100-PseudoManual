---
symbol: "PRR15L"
type: "gene"
col: 9430
ensembl_id: "ENSG00000167183"
name: "proline rich 15 like"
location: "17q21.32"
module: 44
arm: "+"
pooled_cpm: 3.73
n_lines_expressing: 12
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 106
direction_downstream: 109
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PRR15L

*proline rich 15 like* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.89× (z +12.1, q 8e-31, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +4.7, q 3e-04, up in 0 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0506×, HT-29 0.0223×, COLO 205 0.0269×, LoVo 0.0549×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.0146×, LS 180 0.0311×, HT-29 0.0149×, COLO 205 0.0409×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HT-29 0.0469×, COLO 205 0.0731×, LoVo 0.0889×, KATO III 0.106×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (COLO 205 0.00873×, LoVo 0.0457×, KATO III 0.0494×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15]] (+0.84, fdr 7e-06), [[LGALS4]] (+0.83, fdr 7e-06), [[ATP10B]] (+0.81, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 106 arrows point to it, the strongest [[CREB3L1]] → it (grade B ⚠); 109 go from it, the strongest it → [[DTX4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.89×** | +12.1 | 8e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.54×** | +7.1 | 3e-10 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +6.4 | 2e-08 | 1/7 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.66×** | +5.9 | 4e-07 | 1/7 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.7 | 3e-04 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.1 | 0.004 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.97×** | +4.0 | 0.005 | 7/9 (KATO III, HCT15, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.90×** | +3.8 | 0.010 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.24×** | +3.7 | 0.012 | 1/6 (KATO III) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.032 | 10/10 (LS 180, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.74×** | +3.2 | 0.069 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.73×** | +3.2 | 0.069 | 6/9 (LS 180, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 2.76× | +3.0 | 0.11 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0506×, HT-29 0.0223×, COLO 205 0.0269×, LoVo 0.0549×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.0146×, LS 180 0.0311×, HT-29 0.0149×, COLO 205 0.0409×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HT-29 0.0469×, COLO 205 0.0731×, LoVo 0.0889×, KATO III 0.106×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (COLO 205 0.00873×, LoVo 0.0457×, KATO III 0.0494×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 23.3 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0223× (z -24.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0469× (z -20.0) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 16 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.00740× (z -23.6) |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0269× (z -24.3) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.00873× (z -22.5) |
| [[KATO III (line)]] | alt | 16.7 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -13.9) |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0506× (z -25.3) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0311× (z -20.8) |
| [[SW1417 (line)]] | alt | 8.00 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0295× (z -13.2) |
| [[BT-474 (line)]] | alt | 5.03 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.336 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15]] | +0.84 | +0.82 / +0.80 | both halves | 7e-06 | STRING 580 |
| [[LGALS4]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ATP10B]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.80 | +0.79 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.80 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.79 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.78 | +0.84 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*106 arrows, 106 of them with an alert ⚠; grade A 0, B 1, C 105. Shown: the 12 strongest; 94 more arrows (94 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | CREB3L1 activity raises PRR15L's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without CREB3L1 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[PHGR1]] | C | PHGR1 activity raises PRR15L's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 9.18× lower at baseline in the lines without PHGR1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises PRR15L's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 6.62× lower at baseline in the lines without CDH17 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises PRR15L's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 6.14× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises PRR15L's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 7.33× lower at baseline in the lines without FAM3D | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises PRR15L's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 6.44× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises PRR15L's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.53× lower at baseline in the lines without GCNT3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises PRR15L's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 7.60× lower at baseline in the lines without NPSR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises PRR15L's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 6.08× lower at baseline in the lines without ATP10B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises PRR15L's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 4.05× lower at baseline in the lines without FXYD3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises PRR15L's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 5.20× lower at baseline in the lines without LGALS4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises PRR15L's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 5.17× lower at baseline in the lines without TRIM31 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |

### Downstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 18, C 91. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTX4]] | B | PRR15L activity raises DTX4's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without PRR15L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[CMTM3]] | B | PRR15L activity lowers CMTM3's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 4.19× higher at baseline in the lines without PRR15L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[ARHGEF16]] | B | PRR15L activity raises ARHGEF16's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.60× lower at baseline in the lines without PRR15L | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[PIK3C2B]] | B | PRR15L activity raises PIK3C2B's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without PRR15L | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[ELMO3]] | B | PRR15L activity raises ELMO3's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.96× lower at baseline in the lines without PRR15L | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[SLC44A3]] | B | PRR15L activity raises SLC44A3's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.77× lower at baseline in the lines without PRR15L | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[MROH7]] | B | PRR15L activity raises MROH7's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without PRR15L | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[ATP8B1]] | B | PRR15L activity raises ATP8B1's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.92× lower at baseline in the lines without PRR15L | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[LINC01290]] | B | PRR15L activity raises LINC01290's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.27× lower at baseline in the lines without PRR15L | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[ABHD11]] | B | PRR15L activity raises ABHD11's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without PRR15L | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[POU5F1B]] | B | PRR15L activity raises POU5F1B's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without PRR15L | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[IL17RE]] | B | PRR15L activity raises IL17RE's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.96× lower at baseline in the lines without PRR15L | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.882). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.4, 51.5); signed map (63.2, 5.3). **Vector** length 72.4, 38.7% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.66 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.66 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.66 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +1.4 | +1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.0 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 15 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,951,967-47,957,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11242; previously ATAD4 |
| Matched by | ensembl_id |

UniProt [Q9BU68](https://www.uniprot.org/uniprotkb/Q9BU68) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28149) · Entrez [79170](https://www.ncbi.nlm.nih.gov/gene/79170) · UniProt [Q9BU68](https://www.uniprot.org/uniprotkb/Q9BU68) · Ensembl [ENSG00000167183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167183)

## Data

Gene col 9430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9430); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9430]; `tensor/DDL_lfc|DDL_z.npy` [9430]; `embed/gene_vectors.npy` [9430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9430 or target_col == 9430). Every well: [[PRR15L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR15L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
