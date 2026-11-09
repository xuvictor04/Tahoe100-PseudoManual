---
symbol: "TMC5"
type: "gene"
col: 2380
ensembl_id: "ENSG00000103534"
name: "transmembrane channel like 5"
location: "16p12.3"
module: 8
arm: "+"
pooled_cpm: 72.84
n_lines_expressing: 21
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 103
direction_downstream: 94
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMC5

*transmembrane channel like 5* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +7.1, q 7e-10, up in 4 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +6.4, q 4e-08, up in 7 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.637× (z -7.3, q 2e-10, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12-AS1]] (+0.74, fdr 7e-06), [[MUC4]] (+0.74, fdr 7e-06), [[ITGB6]] (+0.73, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 103 arrows point to it, the strongest [[MTUS1]] → it (grade B ⚠); 94 go from it, the strongest it → [[BAG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.1 | 7e-10 | 4/17 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.4 | 4e-08 | 7/19 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 8e-04 | 11/20 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.0 | 0.008 | 1/19 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.017 | 11/19 (AsPC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.078 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.637×** | -7.3 | 2e-10 | 17/19 (CFPAC-1, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.591×** | -6.0 | 6e-07 | 14/19 (COLO 205, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.723×** | -5.2 | 3e-05 | 17/19 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.012 | 5/19 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -3.9 | 0.012 | 15/19 (BT-474, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.730×** | -3.6 | 0.033 | 6/19 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.735×** | -3.5 | 0.035 | 8/19 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.035 | 12/19 (BT-474, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.729×** | -3.5 | 0.035 | 14/19 (SW48, RKO, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.042 | 15/20 (SHP-77, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.747×** | -3.3 | 0.045 | 12/19 (CFPAC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.740×** | -3.3 | 0.045 | 12/19 (SW48, COLO 205, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.045 | 14/20 (SHP-77, HT-29, …) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.741×** | -3.2 | 0.066 | 2/19 (RKO, SHP-77) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.069 | 15/19 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.757×** | -3.0 | 0.086 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 73.4 | 0 | 21 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0644× (z -25.7) |
| [[BT-474 (line)]] | alt | 216 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0470× (z -29.9) |
| [[HT-29 (line)]] | alt | 415 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.444× (z -9.9) |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 112 | 9 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.5 µM 4.41× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 327 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.3) |
| [[KATO III (line)]] | alt | 933 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -21.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.9) |
| [[COLO 205 (line)]] | alt | 708 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.499× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 93.4 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.16× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.223× (z -13.2) |
| [[SW48 (line)]] | wt | 56.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.5) |
| [[LoVo (line)]] | wt | 38.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.2) |
| [[LS 180 (line)]] | wt | 145 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.53× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12-AS1]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CATSPERB]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ALOX5]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PDZK1IP1]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RBM47]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TC2N]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[FLRT3]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*103 arrows, 103 of them with an alert ⚠; grade A 0, B 11, C 92. Shown: the 12 strongest; 91 more arrows (91 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | MTUS1 activity raises TMC5's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.55× lower at baseline in the lines without MTUS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TMC5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.15× lower at baseline in the lines without ELF3-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[DAPK2]] | B | DAPK2 activity raises TMC5's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 4.24× lower at baseline in the lines without DAPK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[PTPRB]] | B | PTPRB activity raises TMC5's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.71× lower at baseline in the lines without PTPRB | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[ENKUR]] | B | ENKUR activity raises TMC5's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ENKUR | 0.054 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises TMC5's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without LGALS9 | 0.069 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[KIRREL1]] | B | KIRREL1 activity lowers TMC5's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 5.58× higher at baseline in the lines without KIRREL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[SPATA6L]] | B | SPATA6L activity raises TMC5's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.66× lower at baseline in the lines without SPATA6L | 0.088 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises TMC5's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.12× lower at baseline in the lines without HNF4G | 0.092 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[FUT2]] | B | FUT2 activity raises TMC5's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without FUT2 | 0.092 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[KLF5]] | B | KLF5 activity raises TMC5's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.18× lower at baseline in the lines without KLF5 | 0.096 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[ALOX5]] | C | ALOX5 activity raises TMC5's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 4.72× lower at baseline in the lines without ALOX5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |

### Downstream of this gene

*94 arrows, 94 of them with an alert ⚠; grade A 0, B 23, C 71. Shown: the 12 strongest; 82 more arrows (82 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAG1]] | B | TMC5 activity raises BAG1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without TMC5 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[TSPAN3]] | B | TMC5 activity raises TSPAN3's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without TMC5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[ELF3-AS1]] | B | TMC5 activity raises ELF3-AS1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without TMC5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[KLF5]] | B | TMC5 activity raises KLF5's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 4.60× lower at baseline in the lines without TMC5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[TNFRSF21]] | B | TMC5 activity raises TNFRSF21's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.77× lower at baseline in the lines without TMC5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[MTUS1]] | B | TMC5 activity raises MTUS1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without TMC5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[ASS1]] | B | TMC5 activity raises ASS1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without TMC5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[GAREM1]] | B | TMC5 activity raises GAREM1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.84× lower at baseline in the lines without TMC5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[PCAT1]] | B | TMC5 activity raises PCAT1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.71× lower at baseline in the lines without TMC5 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[LMO7]] | B | TMC5 activity raises LMO7's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without TMC5 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[FZD5]] | B | TMC5 activity raises FZD5's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without TMC5 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[STS]] | B | TMC5 activity raises STS's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.56× lower at baseline in the lines without TMC5 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 55.1); signed map (59.5, 3.9). **Vector** length 101, 37.8% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.56 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane channel like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,410,496-19,499,113 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13593 |
| Gene groups (HGNC) | Transmembrane channel like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXY8](https://www.uniprot.org/uniprotkb/Q6UXY8) (Transmembrane channel-like protein 5):

> Probable component of an ion channel (Probable). Molecular function hasn't been characterized yet (Probable).

**Summary**, from NCBI Gene [79838](https://www.ncbi.nlm.nih.gov/gene/79838):

> Predicted to enable mechanosensitive monoatomic ion channel activity. Predicted to be involved in monoatomic ion transmembrane transport. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22999) · Entrez [79838](https://www.ncbi.nlm.nih.gov/gene/79838) · UniProt [Q6UXY8](https://www.uniprot.org/uniprotkb/Q6UXY8) · Ensembl [ENSG00000103534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103534)

## Data

Gene col 2380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2380); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2380]; `tensor/DDL_lfc|DDL_z.npy` [2380]; `embed/gene_vectors.npy` [2380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2380 or target_col == 2380). Every well: [[TMC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
