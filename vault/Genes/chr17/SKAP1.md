---
symbol: "SKAP1"
type: "gene"
col: 6499
ensembl_id: "ENSG00000141293"
name: "src kinase associated phosphoprotein 1"
location: "17q21.32"
module: 55
arm: "+"
pooled_cpm: 64.5
n_lines_expressing: 16
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 89
direction_downstream: 108
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SKAP1

*src kinase associated phosphoprotein 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +14.0, q 1e-41, up in 1 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +9.5, q 6e-19, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.610× (z -7.1, q 6e-10, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDAR]] (+0.84, fdr 7e-06), [[VWA2]] (+0.81, fdr 7e-06), [[SLC5A1]] (+0.77, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 89 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 108 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +14.0 | 1e-41 | 1/15 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +13.6 | 9e-40 | 2/12 (LoVo, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +9.5 | 6e-19 | 9/14 (LS 180, HCT15, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.2 | 8e-18 | 1/15 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.5 | 8e-12 | 13/14 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +7.0 | 2e-10 | 3/13 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.8 | 0.010 | 3/14 (HEC-1-A, NCI-H2347, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.036 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -7.1 | 6e-10 | 13/14 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -5.6 | 5e-06 | 14/14 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -5.2 | 4e-05 | 11/14 (LS 180, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.709×** | -5.0 | 1e-04 | 0/14 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -4.4 | 0.001 | 6/14 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.816×** | -4.2 | 0.003 | 13/14 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.003 | 12/14 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -4.1 | 0.003 | 6/14 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.747×** | -3.9 | 0.006 | 0/14 | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.027 | 0/14 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.031 | 0/14 | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.775×** | -3.4 | 0.033 | 2/14 (LoVo, LS 180) | inconsistent across doses |  |
| [[Ivermectin (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.040 | 1/14 (HEC-1-A) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.784×** | -3.2 | 0.044 | 0/14 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.791×** | -3.2 | 0.044 | 13/14 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.046 | 1/14 (HEC-1-A) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 552 | 0 | 21 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -32.4) |
| [[SW48 (line)]] | wt | 326 | 0 | 19 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -21.7) |
| [[LS 180 (line)]] | wt | 85.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.8) |
| [[HT-29 (line)]] | alt | 192 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -16.5) |
| [[KATO III (line)]] | alt | 251 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -23.5) |
| [[Panc 03.27 (line)]] | alt | 94.7 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -16.6) |
| [[SW1417 (line)]] | alt | 89.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.5) |
| [[LoVo (line)]] | wt | 43.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.1) |
| [[COLO 205 (line)]] | alt | 197 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -16.8) |
| [[A-172 (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDAR]] | +0.84 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SLC5A1]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ADGRG5]] | +0.76 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[KCNH8]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.73 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 | same gene group |
| [[KCNE3]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 1, C 88. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises SKAP1's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without ZNF860 | 0.078 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[CLIC5]] | C | CLIC5 activity raises SKAP1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 8.30× lower at baseline in the lines without CLIC5 | 6e-05 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises SKAP1's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 8.92× lower at baseline in the lines without VWA2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[KCNE3]] | C | KCNE3 activity raises SKAP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 9.84× lower at baseline in the lines without KCNE3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises SKAP1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 6.53× lower at baseline in the lines without ATP2C2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises SKAP1's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 4.57× lower at baseline in the lines without PADI1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises SKAP1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 5.15× lower at baseline in the lines without BSPRY | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises SKAP1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 6.88× lower at baseline in the lines without PROM1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises SKAP1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.84× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[TSPOAP1]] | C | TSPOAP1 activity raises SKAP1's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 3.65× lower at baseline in the lines without TSPOAP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises SKAP1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.89× lower at baseline in the lines without C1orf116 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises SKAP1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 5.56× lower at baseline in the lines without AZGP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |

### Downstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 22, C 86. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | SKAP1 activity raises EPS8L1's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 4.43× lower at baseline in the lines without SKAP1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[ARHGEF3]] | B | SKAP1 activity raises ARHGEF3's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without SKAP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[TMC6]] | B | SKAP1 activity raises TMC6's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 4.24× lower at baseline in the lines without SKAP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[ABHD11]] | B | SKAP1 activity raises ABHD11's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without SKAP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[GPR143]] | B | SKAP1 activity raises GPR143's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 1.64× lower at baseline in the lines without SKAP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[TLDC2]] | B | SKAP1 activity raises TLDC2's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without SKAP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[VILL]] | B | SKAP1 activity raises VILL's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without SKAP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | SKAP1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SKAP1 (34) vs lines expressing it (14) | the lines without SKAP1: 1.22× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | SKAP1 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express SKAP1 (34) vs lines expressing it (14) | the lines without SKAP1: 0.71× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[ARHGAP32]] | B | SKAP1 activity raises ARHGAP32's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without SKAP1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[IQANK1]] | B | SKAP1 activity raises IQANK1's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 3.63× lower at baseline in the lines without SKAP1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[PPARG]] | B | SKAP1 activity raises PPARG's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without SKAP1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 46.7); signed map (63.7, 11.9). **Vector** length 82.0, 36.3% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -7.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | src kinase associated phosphoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,133,442-48,430,275 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKAP55; previously SCAP1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WV1](https://www.uniprot.org/uniprotkb/Q86WV1) (Src kinase-associated phosphoprotein 1):

> Positively regulates T-cell receptor signaling by enhancing the MAP kinase pathway. Required for optimal conjugation between T-cells and antigen-presenting cells by promoting the clustering of integrin ITGAL on the surface of T-cells. May be involved in high affinity immunoglobulin epsilon receptor signaling in mast cells.

**Summary**, from NCBI Gene [8631](https://www.ncbi.nlm.nih.gov/gene/8631):

> This gene encodes a T cell adaptor protein, a class of intracellular molecules with modular domains capable of recruiting additional proteins but that exhibit no intrinsic enzymatic activity. The encoded protein contains a unique N-terminal region followed by a PH domain and C-terminal SH3 domain. Along with the adhesion and degranulation-promoting adaptor protein, the encoded protein plays a critical role in inside-out signaling by coupling T-cell antigen receptor stimulation to the activation …

**Accessions** — [HGNC:15605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15605) · Entrez [8631](https://www.ncbi.nlm.nih.gov/gene/8631) · UniProt [Q86WV1](https://www.uniprot.org/uniprotkb/Q86WV1) · Ensembl [ENSG00000141293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141293)

## Data

Gene col 6499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6499); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6499]; `tensor/DDL_lfc|DDL_z.npy` [6499]; `embed/gene_vectors.npy` [6499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6499 or target_col == 6499). Every well: [[SKAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
