---
symbol: "HNF4A"
type: "gene"
col: 2066
ensembl_id: "ENSG00000101076"
name: "hepatocyte nuclear factor 4 alpha"
location: "20q13.12"
module: 55
arm: "+"
pooled_cpm: 43.61
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 125
direction_downstream: 145
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# HNF4A

*hepatocyte nuclear factor 4 alpha* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +11.8, q 3e-29, up in 0 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.5, q 0.001, up in 3 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.512× (z -8.9, q 5e-16, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO7B]] (+0.81, fdr 7e-06), [[NPSR1]] (+0.81, fdr 7e-06), [[EPS8L3]] (+0.81, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 125 arrows point to it, the strongest [[NOSTRIN]] → it (grade B ⚠); 145 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +11.8 | 3e-29 | 0/14 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.7 | 4e-09 | 1/13 (HCT15) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.001 | 3/14 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.001 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.003 | 0/14 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.003 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.27× | +3.1 | 0.15 | 0/14 | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -8.9 | 5e-16 | 13/14 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -8.0 | 3e-13 | 13/14 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -7.3 | 4e-11 | 13/14 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -7.1 | 2e-10 | 14/14 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -5.5 | 5e-06 | 14/14 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.685×** | -5.0 | 6e-05 | 13/14 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -4.7 | 2e-04 | 10/14 (A498, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.775×** | -4.6 | 4e-04 | 1/14 (SW480) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.692×** | -4.5 | 5e-04 | 0/14 | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.700×** | -4.4 | 8e-04 | 2/14 (SW480, LoVo) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.730×** | -4.1 | 0.002 | 0/14 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.003 | 14/14 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.563×** | -4.0 | 0.003 | 7/14 (KATO III, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | **0.740×** | -4.0 | 0.003 | 0/14 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.728×** | -3.9 | 0.003 | 0/14 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.740×** | -3.7 | 0.007 | 1/14 (HCT15) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.007 | 8/14 (HT-29, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.3 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0757× (z -13.7) |
| [[LoVo (line)]] | wt | 219 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -29.0) |
| [[LS 180 (line)]] | wt | 181 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -26.3) |
| [[KATO III (line)]] | alt | 166 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -19.6) |
| [[SW480 (line)]] | alt | 112 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -21.9) |
| [[A549 (line)]] | wt | 41.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -19.7) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.3) |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.8) |
| [[SW48 (line)]] | wt | 69.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.6) |
| [[SW1417 (line)]] | alt | 274 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -16.2) |
| [[HT-29 (line)]] | alt | 148 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -22.1) |
| [[A-172 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO7B]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.81 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.81 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Kidney development; STRING 559 |
| [[LINC01819]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.78 | +0.82 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2B]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*125 arrows, 125 of them with an alert ⚠; grade A 0, B 7, C 118. Shown: the 12 strongest; 113 more arrows (113 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | NOSTRIN activity raises HNF4A's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without NOSTRIN | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises HNF4A's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.99× lower at baseline in the lines without ZNF860 | 0.013 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises HNF4A's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.07× lower at baseline in the lines without TNFRSF21 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[SMAD9]] | B | SMAD9 activity lowers HNF4A's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 6.46× higher at baseline in the lines without SMAD9 | 0.058 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[LINC00511]] | B | LINC00511 activity raises HNF4A's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 3.41× lower at baseline in the lines without LINC00511 | 0.060 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[EPS8L1]] | B | EPS8L1 activity raises HNF4A's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.56× lower at baseline in the lines without EPS8L1 | 0.090 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[PDE9A]] | B | PDE9A activity raises HNF4A's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without PDE9A | 0.093 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[EPS8L3]] | C | EPS8L3 activity raises HNF4A's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 15.12× lower at baseline in the lines without EPS8L3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises HNF4A's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 15.26× lower at baseline in the lines without GCNT3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises HNF4A's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 15.02× lower at baseline in the lines without MUC13 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[INAVA]], [[MROH3P]] | C | INAVA, MROH3P activity raises HNF4A's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 9.20× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent with the target; co-absent genes |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises HNF4A's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 8.73× lower at baseline in the lines without NPSR1-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*145 arrows, 145 of them with an alert ⚠; grade A 0, B 29, C 116. Shown: the 12 strongest; 133 more arrows (133 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | HNF4A activity raises TLDC2's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without HNF4A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[NUDT4]] | B | HNF4A activity raises NUDT4's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[NOSTRIN]] | B | HNF4A activity raises NOSTRIN's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[PLEKHA7]] | B | HNF4A activity raises PLEKHA7's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[EPS8L1]] | B | HNF4A activity raises EPS8L1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.81× lower at baseline in the lines without HNF4A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[PDE9A]] | B | HNF4A activity raises PDE9A's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.93× lower at baseline in the lines without HNF4A | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[ANXA11]] | B | HNF4A activity raises ANXA11's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.90× lower at baseline in the lines without HNF4A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[MROH7]] | B | HNF4A activity raises MROH7's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without HNF4A | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[NGEF]] | B | HNF4A activity raises NGEF's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without HNF4A | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[KLF3]] | B | HNF4A activity raises KLF3's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without HNF4A | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[DTX2]] | B | HNF4A activity raises DTX2's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without HNF4A | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[SPATA13]] | B | HNF4A activity raises SPATA13's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without HNF4A | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 50.1); signed map (63.3, 9.8). **Vector** length 90.0, 42.5% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | hepatocyte nuclear factor 4 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,355,699-44,432,845 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NR2A1, HNF4; previously TCF14, MODY, MODY1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Hepatocyte nuclear factor 4 family |
| Hallmark sets | COAGULATION, XENOBIOTIC_METABOLISM, COMPLEMENT |
| Reactome | 5 pathways, smallest: Regulation of gene expression in beta cells; Nephron development; Regulation of beta-cell development |
| Matched by | ensembl_id |

**Function**, from UniProt [P41235](https://www.uniprot.org/uniprotkb/P41235) (Hepatocyte nuclear factor 4-alpha):

> Transcriptional regulator which controls the expression of hepatic genes during the transition of endodermal cells to hepatic progenitor cells, facilitating the recruitment of RNA pol II to the promoters of target genes. Activates the transcription of CYP2C38 (By similarity). Represses the CLOCK-BMAL1 transcriptional activity and is essential for circadian rhythm maintenance and period regulation in the liver and colon cells.

**Summary**, from NCBI Gene [3172](https://www.ncbi.nlm.nih.gov/gene/3172):

> The protein encoded by this gene is a nuclear transcription factor which binds DNA as a homodimer. The encoded protein controls the expression of several genes, including hepatocyte nuclear factor 1 alpha, a transcription factor which regulates the expression of several hepatic genes. This gene may play a role in development of the liver, kidney, and intestines. Mutations in this gene have been associated with monogenic autosomal dominant non-insulin-dependent diabetes mellitus type I. …

**Accessions** — [HGNC:5024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5024) · Entrez [3172](https://www.ncbi.nlm.nih.gov/gene/3172) · UniProt [P41235](https://www.uniprot.org/uniprotkb/P41235) · Ensembl [ENSG00000101076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101076)

## Data

Gene col 2066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2066); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2066]; `tensor/DDL_lfc|DDL_z.npy` [2066]; `embed/gene_vectors.npy` [2066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2066 or target_col == 2066). Every well: [[HNF4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNF4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
