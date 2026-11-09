---
symbol: "TMC4"
type: "gene"
col: 9499
ensembl_id: "ENSG00000167608"
name: "transmembrane channel like 4"
location: "19q13.42"
module: 8
arm: "+"
pooled_cpm: 17.21
n_lines_expressing: 24
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 136
direction_downstream: 144
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMC4

*transmembrane channel like 4* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +8.2, q 2e-13, up in 5 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.5, q 2e-11, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.461× (z -9.2, q 3e-17, down in 18 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY4]] (+0.78, fdr 7e-06), [[SLC44A4]] (+0.77, fdr 7e-06), [[TMEM125]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 136 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 144 go from it, the strongest it → [[PATJ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.2 | 2e-13 | 5/19 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.5 | 2e-11 | 2/20 (A498, PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.1 | 2e-10 | 4/13 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.1 | 2e-07 | 2/20 (A498, NCI-H2030) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.1 | 3e-05 | 3/16 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 6e-04 | 1/21 (AsPC-1) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +4.1 | 0.003 | 9/20 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.036 | 7/21 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.064 | 4/21 (SW48, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.064 | 2/20 (PANC-1, NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -9.2 | 3e-17 | 18/19 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -7.2 | 2e-10 | 19/20 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -6.9 | 9e-10 | 18/21 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -5.2 | 3e-05 | 16/21 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -5.0 | 8e-05 | 15/20 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -4.4 | 8e-04 | 10/21 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.701×** | -4.2 | 0.002 | 16/21 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.799×** | -3.8 | 0.012 | 18/20 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.730×** | -3.7 | 0.013 | 14/20 (COLO 205, KATO III, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.743×** | -3.5 | 0.026 | 14/21 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.728×** | -3.5 | 0.027 | 3/21 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.609×** | -3.1 | 0.096 | 13/21 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.096 | 2/20 (A498, LS 180) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 81.2 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -16.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.0) |
| [[LoVo (line)]] | wt | 38.8 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -12.4) |
| [[COLO 205 (line)]] | alt | 69.5 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -22.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -14.0) |
| [[HCT15 (line)]] | alt | 96.7 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0406× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.2) |
| [[KATO III (line)]] | alt | 40.1 | 0 | 8 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.204× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.7) |
| [[LS 180 (line)]] | wt | 54.7 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.205× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 80.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -9.1) |
| [[SW480 (line)]] | alt | 17.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -10.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -9.1) |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 5.32 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0801× (z -10.1) |
| [[PANC-1 (line)]] | alt | 4.64 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.54× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY4]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TMEM125]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ESRP1]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF14-AS1]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[ERBB3]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CLDN3]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PROM1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[RORC]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ST14]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*136 arrows, 136 of them with an alert ⚠; grade A 0, B 29, C 107. Shown: the 12 strongest; 124 more arrows (124 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers TMC4's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.26× higher at baseline in the lines without TTC28 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[DCLK2]] | B | DCLK2 activity lowers TMC4's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 5.74× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises TMC4's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[MROH7]] | B | MROH7 activity raises TMC4's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 3.35× lower at baseline in the lines without MROH7 | 0.007 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises TMC4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises TMC4's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without TMEM51-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises TMC4's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LPAR5]] | B | LPAR5 activity raises TMC4's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without LPAR5 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity raises TMC4's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without ARHGAP30 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity raises TMC4's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without SLC28A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[MYO1D]] | B | MYO1D activity raises TMC4's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without MYO1D | 0.016 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises TMC4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TJP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |

### Downstream of this gene

*144 arrows, 144 of them with an alert ⚠; grade A 0, B 51, C 93. Shown: the 12 strongest; 132 more arrows (132 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | TMC4 activity raises PATJ's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without TMC4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SLC44A3]] | B | TMC4 activity raises SLC44A3's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without TMC4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[EPS8L1]] | B | TMC4 activity raises EPS8L1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.67× lower at baseline in the lines without TMC4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ELMO3]] | B | TMC4 activity raises ELMO3's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.43× lower at baseline in the lines without TMC4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[PRRG2]] | B | TMC4 activity raises PRRG2's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without TMC4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ARHGEF16]] | B | TMC4 activity raises ARHGEF16's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.13× lower at baseline in the lines without TMC4 | 0.002 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SLC44A3-AS1]] | B | TMC4 activity raises SLC44A3-AS1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.84× lower at baseline in the lines without TMC4 | 0.002 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[FAM83E]] | B | TMC4 activity raises FAM83E's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without TMC4 | 0.003 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[MYO1D]] | B | TMC4 activity raises MYO1D's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without TMC4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[TMEM184A]] | B | TMC4 activity raises TMEM184A's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without TMC4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[KLHL2P1]] | B | TMC4 activity raises KLHL2P1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without TMC4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[EPCAM-DT]] | B | TMC4 activity raises EPCAM-DT's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without TMC4 | 0.012 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.0, 55.1); signed map (58.3, 5.8). **Vector** length 85.7, 31.6% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane channel like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,160,108-54,173,250 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Transmembrane channel like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z404](https://www.uniprot.org/uniprotkb/Q7Z404) (Voltage-gated chloride channel TMC4):

> Voltage-gated chloride channel involved in high-concentration salt taste sensation. Depolarization induced by high NaCl concentration may trigger the activation of TMC4-mediated chloride influx into taste bud cells, helping the return to resting potential. Also allows permeation of organic anions including gluconate, but their current amplitudes at positive potentials are less than that of chloride. Involved in pH and temperature-dependent modulation of salty taste.

**Summary**, from NCBI Gene [147798](https://www.ncbi.nlm.nih.gov/gene/147798):

> Enables voltage-gated chloride channel activity. Predicted to be involved in sensory perception of salty taste. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22998) · Entrez [147798](https://www.ncbi.nlm.nih.gov/gene/147798) · UniProt [Q7Z404](https://www.uniprot.org/uniprotkb/Q7Z404) · Ensembl [ENSG00000167608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167608)

## Data

Gene col 9499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9499); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9499]; `tensor/DDL_lfc|DDL_z.npy` [9499]; `embed/gene_vectors.npy` [9499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9499 or target_col == 9499). Every well: [[TMC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
