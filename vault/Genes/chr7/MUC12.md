---
symbol: "MUC12"
type: "gene"
col: 12964
ensembl_id: "ENSG00000205277"
name: "mucin 12, cell surface associated"
location: "7q22.1"
module: 44
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 32
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 38
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MUC12

*mucin 12, cell surface associated* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.78× (z +14.6, q 3e-45, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +8.4, q 6e-15, up in 9 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.147×, LS 180 0.251×); [[Selinexor (drug)]] 5 µM in 1 line (HT-29 0.0903×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.158×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC3A]] (+0.71, fdr 7e-06, ⚠ same locus), [[PLEKHG6]] (+0.71, fdr 7e-06), [[FAM3D]] (+0.65, fdr 1e-05), [[CFTR]] (+0.64, fdr 1e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[MUC13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.78×** | +14.6 | 3e-45 | 3/5 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.50×** | +11.3 | 4e-27 | 7/10 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +8.4 | 6e-15 | 9/17 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +8.4 | 8e-15 | 2/6 (PANC-1, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +7.4 | 2e-11 | 17/27 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +7.2 | 5e-11 | 8/19 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +6.1 | 8e-08 | 4/9 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +5.3 | 9e-06 | 11/22 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +4.5 | 4e-04 | 4/18 (SW480, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +4.4 | 7e-04 | 8/21 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.007 | 4/27 (PANC-1, A549, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.013 | 2/16 (HEC-1-A, A549) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.91× | +3.0 | 0.10 | 1/12 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.58× | +3.0 | 0.10 | 5/18 (RKO, SW480, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.147×, LS 180 0.251×); [[Selinexor (drug)]] 5 µM in 1 line (HT-29 0.0903×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.158×; ⚠ toxic).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0903× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.1) |
| [[LoVo (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.6) |
| [[A-172 (line)]] | wt | 0.888 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC3A]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 826; ⚠ same locus (1.2 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHG6]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CFTR]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[FXYD3]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ATP10B]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[FUT2]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LINC02580]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[LINC01133]] | +0.63 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[MUC13]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 980 |
| [[LGALS4]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[BCL2L14]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PRR15L]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 38, C 0. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC13]] | B | MUC13 activity raises MUC12's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.79× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[NPSR1]] | B | NPSR1 activity raises MUC12's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.16× lower at baseline in the lines without NPSR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[TRIM31]] | B | TRIM31 activity raises MUC12's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.36× lower at baseline in the lines without TRIM31 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MUC17]] | B | MUC17 activity raises MUC12's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.91× lower at baseline in the lines without MUC17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[LGALS4]] | B | LGALS4 activity raises MUC12's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.27× lower at baseline in the lines without LGALS4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[CDH17]] | B | CDH17 activity raises MUC12's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.47× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[GCNT3]] | B | GCNT3 activity raises MUC12's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TM4SF4]] | B | TM4SF4 activity raises MUC12's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.59× lower at baseline in the lines without TM4SF4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[GPA33]] | B | GPA33 activity raises MUC12's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.50× lower at baseline in the lines without GPA33 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC01133]] | B | LINC01133 activity raises MUC12's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without LINC01133 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1 |
| [[PTPRR]] | B | PTPRR activity raises MUC12's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without PTPRR | 0.013 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[HEPH]] | B | HEPH activity raises MUC12's level | lines that do not express HEPH (41) vs lines expressing it (9) | 3.24× lower at baseline in the lines without HEPH | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 52.5); signed map (62.3, 4.8). **Vector** length 41.7, 7.65% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.56 to 4); *Aspirin ADME* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mucin 12, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,969,565-101,018,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MUC11 |
| Gene groups (HGNC) | Mucins; SEA domain containing |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKN1](https://www.uniprot.org/uniprotkb/Q9UKN1) (Mucin-12):

> Involved in epithelial cell protection, adhesion modulation, and signaling. May be involved in epithelial cell growth regulation. Stimulated by both cytokine TNF and TGF-beta in intestinal epithelium.

**Summary**, from NCBI Gene [10071](https://www.ncbi.nlm.nih.gov/gene/10071):

> This gene encodes an integral membrane glycoprotein that is a member of the mucin family. Mucins are O-glycosylated proteins that play an essential role in forming protective mucous barriers on epithelial surfaces and have been implicated in epithelial renewal and differentiation. These glycoproteins also play a role in intracellular signaling. This protein is expressed on the apical membrane surface of epithelial cells that line the mucosal surfaces of many different tissues including the …

**Accessions** — [HGNC:7510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7510) · Entrez [10071](https://www.ncbi.nlm.nih.gov/gene/10071) · UniProt [Q9UKN1](https://www.uniprot.org/uniprotkb/Q9UKN1) · Ensembl [ENSG00000205277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205277)

## Data

Gene col 12964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12964); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12964]; `tensor/DDL_lfc|DDL_z.npy` [12964]; `embed/gene_vectors.npy` [12964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12964 or target_col == 12964). Every well: [[MUC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
