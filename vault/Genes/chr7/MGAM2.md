---
symbol: "MGAM2"
type: "gene"
col: 15062
ensembl_id: "ENSG00000257743"
name: "maltase-glucoamylase 2 (putative)"
location: "7q34"
module: 44
arm: "+"
pooled_cpm: 8.02
n_lines_expressing: 17
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 43
direction_downstream: 43
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MGAM2

*maltase-glucoamylase 2 (putative)* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.34× (z +17.9, q 0e+00, up in 6 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.136×, SW1417 0.196×, HT-29 0.121×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (KATO III 0.106×, SW1417 0.171×, HT-29 0.121×); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (KATO III 0.134×, HT-29 0.104×, SW1417 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L15]] (+0.80, fdr 7e-06), [[HNF1A-AS1]] (+0.77, fdr 7e-06), [[PIP5K1B]] (+0.75, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 43 go from it, the strongest it → [[HGD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.34×** | +17.9 | 0e+00 | 6/13 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.12×** | +16.9 | 0e+00 | 9/15 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.77×** | +16.2 | 0e+00 | 4/13 (C32, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +10.9 | 9e-26 | 2/6 (C32, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +9.4 | 4e-19 | 4/13 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +9.4 | 8e-19 | 3/5 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.2 | 3e-14 | 7/15 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +8.1 | 5e-14 | 3/12 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +7.9 | 3e-13 | 7/14 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.29×** | +6.8 | 4e-10 | 10/14 (AsPC-1, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **4.29×** | +6.6 | 3e-09 | 7/15 (C32, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +6.5 | 4e-09 | 5/15 (KATO III, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.9 | 1e-07 | 2/5 (C32, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.75×** | +5.8 | 2e-07 | 8/15 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.66×** | +4.6 | 2e-04 | 8/15 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.5 | 2e-04 | 7/15 (AsPC-1, C32, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +4.4 | 4e-04 | 8/15 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.66×** | +4.3 | 4e-04 | 4/15 (LS 180, COLO 205, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.136×, SW1417 0.196×, HT-29 0.121×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (KATO III 0.106×, SW1417 0.171×, HT-29 0.121×); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (KATO III 0.134×, HT-29 0.104×, SW1417 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -3.7 | 0.10 | 4/15 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.749× | -3.6 | 0.10 | 3/15 (SW1417, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.681× | -3.3 | 0.16 | 12/15 (KATO III, SW1417, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.693× | -3.2 | 0.18 | 0/15 | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.686× | -3.2 | 0.18 | 4/15 (SW1417, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 183 | 0 | 11 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0182× (z -20.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.136× (z -14.6) |
| [[SW1417 (line)]] | alt | 64.8 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.2) |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.6) |
| [[C32 (line)]] | wt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 9.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L15]] | +0.80 | +0.78 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[HNF1A-AS1]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PIP5K1B]] | +0.75 | +0.75 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NPNT]] | +0.75 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TM4SF4]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.71 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MUC13]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 3, C 40. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MGAM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHS1]] | B | PLEKHS1 activity raises MGAM2's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without PLEKHS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[STS]] | B | STS activity raises MGAM2's level | lines that do not express STS (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without STS | 0.096 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[LYZ]] | C | LYZ activity raises MGAM2's level | lines that do not express LYZ (40) vs lines expressing it (10) | 5.03× lower at baseline in the lines without LYZ | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[KRT20]] | C | KRT20 activity raises MGAM2's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.86× lower at baseline in the lines without KRT20 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises MGAM2's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.58× lower at baseline in the lines without MUC13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises MGAM2's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.08× lower at baseline in the lines without CDH17 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[VIL1]] | C | VIL1 activity raises MGAM2's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without VIL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises MGAM2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.75× lower at baseline in the lines without GCNT3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises MGAM2's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 5.40× lower at baseline in the lines without ATP10B | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises MGAM2's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without FXYD3 | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises MGAM2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.04× lower at baseline in the lines without LGALS4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 12, C 31. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | MGAM2 activity raises HGD's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without MGAM2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[C4orf19]] | B | MGAM2 activity raises C4orf19's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without MGAM2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[PLEKHS1]] | B | MGAM2 activity raises PLEKHS1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without MGAM2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[SNTB1]] | B | MGAM2 activity raises SNTB1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 3.56× lower at baseline in the lines without MGAM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[SLC44A3]] | B | MGAM2 activity raises SLC44A3's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without MGAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[SLC44A3-AS1]] | B | MGAM2 activity raises SLC44A3-AS1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without MGAM2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[PRRG2]] | B | MGAM2 activity raises PRRG2's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 1.99× lower at baseline in the lines without MGAM2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| cells under [[Neratinib (maleate) (drug)]] 0.5 µM | B | MGAM2 activity lowers the cells' numbers under Neratinib (maleate) 0.5 µM (makes them more sensitive) | lines that do not express MGAM2 (33) vs lines expressing it (15) | the lines without MGAM2: 1.19× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[LINC02580]] | B | MGAM2 activity raises LINC02580's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 1.86× lower at baseline in the lines without MGAM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[MUC20]] | B | MGAM2 activity raises MUC20's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without MGAM2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[MANSC1]] | B | MGAM2 activity raises MANSC1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without MGAM2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[STS]] | B | MGAM2 activity raises STS's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without MGAM2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 51.9); signed map (60.8, 2.5). **Vector** length 56.6, 17.2% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.69 to 4); *Aspirin ADME* (reactome, mean cos +0.69 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +16.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -1.2 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | maltase-glucoamylase 2 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:142,111,718-142,222,324 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Matched by | ensembl_id |

UniProt [Q2M2H8](https://www.uniprot.org/uniprotkb/Q2M2H8) carries no function annotation.

**Summary**, from NCBI Gene [93432](https://www.ncbi.nlm.nih.gov/gene/93432):

> Predicted to enable alpha-1,4-glucosidase activity. Predicted to be involved in disaccharide catabolic process. Predicted to be located in several cellular components, including apical part of cell; endomembrane system; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28101) · Entrez [93432](https://www.ncbi.nlm.nih.gov/gene/93432) · UniProt [Q2M2H8](https://www.uniprot.org/uniprotkb/Q2M2H8) · Ensembl [ENSG00000257743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257743)

## Data

Gene col 15062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15062); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15062]; `tensor/DDL_lfc|DDL_z.npy` [15062]; `embed/gene_vectors.npy` [15062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15062 or target_col == 15062). Every well: [[MGAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
