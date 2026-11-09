---
symbol: "LYZ"
type: "gene"
col: 1621
ensembl_id: "ENSG00000090382"
name: "lysozyme"
location: "12q15"
module: 44
arm: "+"
pooled_cpm: 33.56
n_lines_expressing: 10
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 67
direction_downstream: 68
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# LYZ

*lysozyme* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.59× (z +17.0, q 0e+00, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +8.8, q 1e-16, up in 5 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.513× (z -5.0, q 3e-04, down in 8 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HT-29 0.135×, HepG2/C3A 0.307×, KATO III 0.306×, COLO 205 0.190×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (KATO III 0.154×, COLO 205 0.0864×, LS 180 0.162×); [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.137×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPCAM]] (+0.79, fdr 7e-06), [[PPP1R1B]] (+0.74, fdr 7e-06), [[PHGR1]] (+0.73, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[MUC5B]] → it (grade C ⚠); 68 go from it, the strongest it → [[BCL2L15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.59×** | +17.0 | 0e+00 | 7/8 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.57×** | +12.5 | 3e-33 | 7/7 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.44×** | +10.4 | 5e-23 | 7/7 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +8.8 | 1e-16 | 5/8 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +6.2 | 5e-08 | 7/8 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +6.0 | 2e-07 | 1/8 (LS 180) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.27×** | +5.7 | 8e-07 | 5/5 (HT-29, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.94×** | +5.0 | 4e-05 | 4/8 (KATO III, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.58×** | +3.5 | 0.031 | 1/8 (CFPAC-1) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.52×** | +3.2 | 0.079 | 4/8 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.087 | 0/8 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.75× | +3.0 | 0.11 | 1/8 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1621.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HT-29 0.135×, HepG2/C3A 0.307×, KATO III 0.306×, COLO 205 0.190×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (KATO III 0.154×, COLO 205 0.0864×, LS 180 0.162×); [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.137×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -5.0 | 3e-04 | 8/8 (KATO III, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.636× | -3.4 | 0.20 | 0/8 | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.668× | -3.0 | 0.48 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 252 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.6) |
| [[COLO 205 (line)]] | alt | 265 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0864× (z -9.8) |
| [[LS 180 (line)]] | wt | 73.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.33× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 90.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 238 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.0) |
| [[HT-29 (line)]] | alt | 648 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.2) |
| [[A-172 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPCAM]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.74 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[PHGR1]] | +0.73 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PIGR]] | +0.71 | +0.63 / +0.66 | both halves | 7e-06 | STRING 639 |
| [[VIL1]] | +0.71 | +0.56 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[KLK6]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PLA2G2A]] | +0.69 | +0.67 / +0.53 | both halves | 1e-05 | pathway: Antimicrobial peptides; STRING 410 |
| [[FXYD3]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[KLK7]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[TM4SF4]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 0, C 67. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC5B]] | C | MUC5B activity raises LYZ's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 5.94× lower at baseline in the lines without MUC5B | 7e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises LYZ's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 11.63× lower at baseline in the lines without AGR3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises LYZ's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.40× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises LYZ's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 8.44× lower at baseline in the lines without TFF3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises LYZ's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 9.20× lower at baseline in the lines without MUC13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises LYZ's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 16.33× lower at baseline in the lines without MUC17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises LYZ's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 9.28× lower at baseline in the lines without TRIM31 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises LYZ's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 8.61× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises LYZ's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 6.19× lower at baseline in the lines without TMEM139 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises LYZ's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 8.02× lower at baseline in the lines without AZGP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises LYZ's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 5.02× lower at baseline in the lines without TMPRSS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises LYZ's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 9.47× lower at baseline in the lines without CLRN3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 7, C 61. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L15]] | B | LYZ activity raises BCL2L15's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.06× lower at baseline in the lines without LYZ | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[RSPH1]] | B | LYZ activity raises RSPH1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.44× lower at baseline in the lines without LYZ | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[SH3BGRL2]] | B | LYZ activity raises SH3BGRL2's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.45× lower at baseline in the lines without LYZ | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[PROM2]] | B | LYZ activity raises PROM2's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.56× lower at baseline in the lines without LYZ | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[SEC16B]] | B | LYZ activity raises SEC16B's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without LYZ | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[CRYZL2P]] | B | LYZ activity raises CRYZL2P's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.76× lower at baseline in the lines without LYZ | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[CTSH]] | B | LYZ activity raises CTSH's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without LYZ | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[AZGP1]] | C | LYZ activity raises AZGP1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 9.23× lower at baseline in the lines without LYZ | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[LGALS4]] | C | LYZ activity raises LGALS4's level | lines that do not express LYZ (40) vs lines expressing it (10) | 8.10× lower at baseline in the lines without LYZ | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[VIL1]] | C | LYZ activity raises VIL1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 8.20× lower at baseline in the lines without LYZ | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[HNF1A-AS1]] | C | LYZ activity raises HNF1A-AS1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 7.53× lower at baseline in the lines without LYZ | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[MUC13]] | C | LYZ activity raises MUC13's level | lines that do not express LYZ (40) vs lines expressing it (10) | 10.68× lower at baseline in the lines without LYZ | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 50.7); signed map (65.4, 5.2). **Vector** length 39.6, 18.8% of its response variance represented; |z| ≥ 3 in 145 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.52 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.52 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | lysozyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,348,381-69,354,234 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Lysozymes, c-type |
| Reactome | 4 pathways, smallest: Antimicrobial peptides; Amyloid fiber formation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61626](https://www.uniprot.org/uniprotkb/P61626) (Lysozyme C):

> Lysozymes have primarily a bacteriolytic function; those in tissues and body fluids are associated with the monocyte-macrophage system and enhance the activity of immunoagents.

**Summary**, from NCBI Gene [4069](https://www.ncbi.nlm.nih.gov/gene/4069):

> This gene encodes human lysozyme, whose natural substrate is the bacterial cell wall peptidoglycan (cleaving the beta[1-4]glycosidic linkages between N-acetylmuramic acid and N-acetylglucosamine). Lysozyme is one of the antimicrobial agents found in human milk, and is also present in spleen, lung, kidney, white blood cells, plasma, saliva, and tears. The protein has antibacterial activity against a number of bacterial species. Missense mutations in this gene have been identified in heritable …

**Accessions** — [HGNC:6740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6740) · Entrez [4069](https://www.ncbi.nlm.nih.gov/gene/4069) · UniProt [P61626](https://www.uniprot.org/uniprotkb/P61626) · Ensembl [ENSG00000090382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090382)

## Data

Gene col 1621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1621); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1621]; `tensor/DDL_lfc|DDL_z.npy` [1621]; `embed/gene_vectors.npy` [1621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1621 or target_col == 1621). Every well: [[LYZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
