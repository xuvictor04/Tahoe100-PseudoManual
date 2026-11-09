---
symbol: "PCK1"
type: "gene"
col: 4512
ensembl_id: "ENSG00000124253"
name: "phosphoenolpyruvate carboxykinase 1"
location: "20q13.31"
module: 44
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 12
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 45
direction_downstream: 40
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PCK1

*phosphoenolpyruvate carboxykinase 1* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.55× (z +8.0, q 5e-13, up in 7 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.481× (z -4.5, q 0.004, down in 7 of 10 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.645× (z -3.8, q 0.032, down in 7 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.0387×, COLO 205 0.0384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (LS 180 0.0394×, COLO 205 0.0364×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (COLO 205 0.0640×, LS 180 0.0753×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (COLO 205 0.0805×, LS 180 0.0939×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 2 lines (LS 180 0.113×, COLO 205 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ILDR2]] (+0.75, fdr 7e-06), [[GPA33]] (+0.74, fdr 7e-06), [[PPP1R1B]] (+0.70, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 40 go from it, the strongest it → [[MYB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.55×** | +8.0 | 5e-13 | 7/10 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +6.7 | 7e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.93×** | +4.7 | 6e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +4.6 | 6e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +4.5 | 7e-04 | 6/10 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +3.9 | 0.007 | 6/10 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.7 | 0.015 | 3/9 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.31×** | +3.6 | 0.021 | 1/8 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.5 | 0.032 | 2/9 (KATO III, SW480) | inconsistent across doses | low cells (technical?); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.62× | +3.1 | 0.12 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.60× | +3.0 | 0.12 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Posaconazole (drug)]] 0.5 µM |  | 1.65× | +3.0 | 0.12 | 0/10 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.0387×, COLO 205 0.0384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (LS 180 0.0394×, COLO 205 0.0364×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (COLO 205 0.0640×, LS 180 0.0753×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (COLO 205 0.0805×, LS 180 0.0939×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 2 lines (LS 180 0.113×, COLO 205 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.481×** | -4.5 | 0.004 | 7/10 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.032 | 7/10 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.546×** | -3.7 | 0.032 | 6/10 (LS 180, LoVo, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.548×** | -3.7 | 0.032 | 7/10 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.589× | -3.2 | 0.13 | 6/10 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 138 | 0 | 18 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0387× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0753× (z -11.5) |
| [[COLO 205 (line)]] | alt | 133 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0384× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0640× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0437× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 1.89 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 20.4× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.730 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.924 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILDR2]] | +0.75 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.74 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[PPP1R1B]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 | STRING 594 |
| [[PRR15L]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[AGR3]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[C9orf152]] | +0.67 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[TJP3]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.65 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[BMP4]] | +0.65 | +0.53 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 1, C 44. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PCK1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PLA2G2A]] | C | PLA2G2A activity raises PCK1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 6.42× lower at baseline in the lines without PLA2G2A | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises PCK1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 5.02× lower at baseline in the lines without MUC6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises PCK1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 6.62× lower at baseline in the lines without LGR5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises PCK1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 4.38× lower at baseline in the lines without TFF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises PCK1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without HNF1A-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises PCK1's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 6.32× lower at baseline in the lines without PHGR1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises PCK1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.21× lower at baseline in the lines without GPX2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises PCK1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.54× lower at baseline in the lines without NPSR1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises PCK1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.84× lower at baseline in the lines without TOX3 | 0.026 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises PCK1's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without NPSR1-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises PCK1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 4.30× lower at baseline in the lines without AGR3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 9, C 31. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYB]] | B | PCK1 activity raises MYB's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without PCK1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[DNAJC15]] | B | PCK1 activity strengthens DNAJC15's drug response | lines that do not express PCK1 (30) vs lines expressing it (8) | the lines without PCK1 respond 0.46× as strongly (z diff +2.57); strongest at Panobinostat 5 µM: 0.74x vs 0.29x (z diff +5.6) | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; target measured in part of the lines; artifact flags |
| [[TMEM141]] | B | PCK1 activity strengthens TMEM141's drug response | lines that do not express PCK1 (36) vs lines expressing it (10) | the lines without PCK1 respond 0.63× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 0.43x vs 0.23x (z diff +4.2) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; target measured in part of the lines; artifact flags |
| [[PLS1]] | B | PCK1 activity raises PLS1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.77× lower at baseline in the lines without PCK1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[PAQR8]] | B | PCK1 activity raises PAQR8's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without PCK1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[GCOM1]] | B | PCK1 activity raises GCOM1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without PCK1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[FZD5]] | B | PCK1 activity raises FZD5's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.12× lower at baseline in the lines without PCK1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[LRP4]] | B | PCK1 activity raises LRP4's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.51× lower at baseline in the lines without PCK1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[SPIRE2]] | B | PCK1 activity raises SPIRE2's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 1.74× lower at baseline in the lines without PCK1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[TOX3]] | C | PCK1 activity raises TOX3's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 7.72× lower at baseline in the lines without PCK1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[TFF3]] | C | PCK1 activity raises TFF3's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 5.78× lower at baseline in the lines without PCK1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[NPSR1-AS1]] | C | PCK1 activity raises NPSR1-AS1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 5.00× lower at baseline in the lines without PCK1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 50.4); signed map (64.3, 6.4). **Vector** length 53.1, 20.1% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.55 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.55 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphoenolpyruvate carboxykinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:57,561,080-57,568,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEPCK-C |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | HYPOXIA |
| Reactome | 19 pathways, smallest: Abacavir metabolism; NR1H2 & NR1H3 regulate gene expression linked to gluconeogenesis; Abacavir ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P35558](https://www.uniprot.org/uniprotkb/P35558) (Phosphoenolpyruvate carboxykinase, cytosolic):

> Cytosolic phosphoenolpyruvate carboxykinase that catalyzes the reversible decarboxylation and phosphorylation of oxaloacetate (OAA) and acts as the rate-limiting enzyme in gluconeogenesis. Regulates cataplerosis and anaplerosis, the processes that control the levels of metabolic intermediates in the citric acid cycle. At low glucose levels, it catalyzes the cataplerotic conversion of oxaloacetate to phosphoenolpyruvate (PEP), the rate-limiting step in the metabolic pathway that produces glucose …

**Summary**, from NCBI Gene [5105](https://www.ncbi.nlm.nih.gov/gene/5105):

> This gene is a main control point for the regulation of gluconeogenesis. The cytosolic enzyme encoded by this gene, along with GTP, catalyzes the formation of phosphoenolpyruvate from oxaloacetate, with the release of carbon dioxide and GDP. The expression of this gene can be regulated by insulin, glucocorticoids, glucagon, cAMP, and diet. Defects in this gene are a cause of cytosolic phosphoenolpyruvate carboxykinase deficiency. A mitochondrial isozyme of the encoded protein also has been …

**Accessions** — [HGNC:8724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8724) · Entrez [5105](https://www.ncbi.nlm.nih.gov/gene/5105) · UniProt [P35558](https://www.uniprot.org/uniprotkb/P35558) · Ensembl [ENSG00000124253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124253)

## Data

Gene col 4512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4512); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4512]; `tensor/DDL_lfc|DDL_z.npy` [4512]; `embed/gene_vectors.npy` [4512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4512 or target_col == 4512). Every well: [[PCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
