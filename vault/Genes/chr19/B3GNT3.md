---
symbol: "B3GNT3"
type: "gene"
col: 11063
ensembl_id: "ENSG00000179913"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 3"
location: "19p13.11"
module: 31
arm: "+"
pooled_cpm: 10.42
n_lines_expressing: 19
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 154
direction_downstream: 186
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# B3GNT3

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 3* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.93× (z +14.1, q 4e-42, up in 1 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +4.7, q 4e-04, up in 3 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.474× (z -7.4, q 1e-10, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR35]] (+0.84, fdr 7e-06), [[MST1R]] (+0.82, fdr 7e-06), [[PADI1]] (+0.80, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 154 arrows point to it, the strongest [[DCLK2]] → it (grade B ⚠); 186 go from it, the strongest it → [[KRT8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +14.1 | 4e-42 | 1/16 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +11.7 | 3e-29 | 2/13 (NCI-H2347, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.4 | 2e-11 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.7 | 4e-04 | 3/17 (HCT15, LOX-IMVI, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.38× | +3.2 | 0.18 | 0/17 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.25 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.474×** | -7.4 | 1e-10 | 15/17 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -6.9 | 1e-09 | 15/17 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -6.0 | 3e-07 | 13/17 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -5.1 | 5e-05 | 17/17 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.593×** | -5.0 | 8e-05 | 10/17 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.644×** | -4.3 | 0.001 | 8/17 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -4.3 | 0.001 | 14/17 (LoVo, SW1417, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -4.3 | 0.001 | 16/17 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -3.8 | 0.009 | 15/17 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.700×** | -3.7 | 0.014 | 3/17 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.038 | 6/17 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.3 | 0.051 | 13/16 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.056 | 6/17 (SW480, A549, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -3.2 | 0.056 | 3/17 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -3.1 | 0.068 | 5/17 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.746×** | -3.0 | 0.092 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.5 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0755× (z -26.3) |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.2) |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0412× (z -23.3) |
| [[COLO 205 (line)]] | alt | 59.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0195× (z -30.6) |
| [[KATO III (line)]] | alt | 34.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -20.8) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.5) |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0558× (z -24.7) |
| [[NCI-H1573 (line)]] | alt | 6.73 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0767× (z -20.8) |
| [[SW1417 (line)]] | alt | 41.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -12.6) |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.9) |
| [[A-172 (line)]] | wt | 0.833 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR35]] | +0.84 | +0.78 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.82 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PADI1]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LEMD1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TNS4]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.78 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C1orf116]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*154 arrows, 154 of them with an alert ⚠; grade A 0, B 30, C 124. Shown: the 12 strongest; 142 more arrows (142 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | DCLK2 activity lowers B3GNT3's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.76× higher at baseline in the lines without DCLK2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TTC28]] | B | TTC28 activity lowers B3GNT3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.60× higher at baseline in the lines without TTC28 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises B3GNT3's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 3.22× lower at baseline in the lines without BAIAP2L2 | 0.001 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises B3GNT3's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.50× lower at baseline in the lines without ZNF860 | 0.006 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[PRAG1]] | B | PRAG1 activity raises B3GNT3's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without PRAG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[ABCC3]] | B | ABCC3 activity raises B3GNT3's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.68× lower at baseline in the lines without ABCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[LINC03041]] | B | LINC03041 activity lowers B3GNT3's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 5.52× higher at baseline in the lines without LINC03041 | 0.013 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[JUP]] | B | JUP activity raises B3GNT3's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.53× lower at baseline in the lines without JUP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[TJP2]] | B | TJP2 activity raises B3GNT3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.83× lower at baseline in the lines without TJP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[UNC13D]] | B | UNC13D activity raises B3GNT3's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without UNC13D | 0.021 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises B3GNT3's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.04× lower at baseline in the lines without EPS8L1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises B3GNT3's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.11× lower at baseline in the lines without MYO1D | 0.025 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |

### Downstream of this gene

*186 arrows, 186 of them with an alert ⚠; grade A 0, B 72, C 114. Shown: the 12 strongest; 174 more arrows (174 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT8]] | B | B3GNT3 activity raises KRT8's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.49× lower at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[ARHGAP27]] | B | B3GNT3 activity raises ARHGAP27's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.96× lower at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[ZNF25]] | B | B3GNT3 activity lowers ZNF25's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.12× higher at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TLDC2]] | B | B3GNT3 activity raises TLDC2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.64× lower at baseline in the lines without B3GNT3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[ANXA11]] | B | B3GNT3 activity raises ANXA11's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without B3GNT3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[BAIAP2L2]] | B | B3GNT3 activity raises BAIAP2L2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without B3GNT3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[JUP]] | B | B3GNT3 activity raises JUP's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.98× lower at baseline in the lines without B3GNT3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PTK2B]] | B | B3GNT3 activity raises PTK2B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[MYO1D]] | B | B3GNT3 activity raises MYO1D's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.89× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[FAM83E]] | B | B3GNT3 activity raises FAM83E's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.70× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TMC6]] | B | B3GNT3 activity raises TMC6's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.12× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[EPS8L1]] | B | B3GNT3 activity raises EPS8L1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.75× lower at baseline in the lines without B3GNT3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 52.3); signed map (60.2, 10.2). **Vector** length 83.4, 37.5% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,794,828-17,813,576 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3GN-T3, beta3Gn-T3, HP10328, B3GNT-3; previously TMEM3 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 12 pathways, smallest: Keratan sulfate biosynthesis; PD-L1(CD274) glycosylation and translocation to plasma membrane; Keratan sulfate/keratin metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2A9](https://www.uniprot.org/uniprotkb/Q9Y2A9) (N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase 3):

> Beta-1,3-N-acetylglucosaminyltransferase involved in the synthesis of poly-N-acetyllactosamine. Has activity for type 2 oligosaccharides. Also acts as a core1-1,3-N-acetylglucosaminyltransferase (Core1-beta3GlcNAcT) to form the 6-sulfo sialyl Lewis x on extended core1 O-glycans.

**Summary**, from NCBI Gene [10331](https://www.ncbi.nlm.nih.gov/gene/10331):

> This gene encodes a member of the beta-1,3-N-acetylglucosaminyltransferase family. This enzyme is a type II transmembrane protein and contains a signal anchor that is not cleaved. It prefers the substrates of lacto-N-tetraose and lacto-N-neotetraose, and is involved in the biosynthesis of poly-N-acetyllactosamine chains and the biosynthesis of the backbone structure of dimeric sialyl Lewis a. It plays dominant roles in L-selectin ligand biosynthesis, lymphocyte homing and lymphocyte …

**Accessions** — [HGNC:13528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13528) · Entrez [10331](https://www.ncbi.nlm.nih.gov/gene/10331) · UniProt [Q9Y2A9](https://www.uniprot.org/uniprotkb/Q9Y2A9) · Ensembl [ENSG00000179913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179913)

## Data

Gene col 11063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11063); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11063]; `tensor/DDL_lfc|DDL_z.npy` [11063]; `embed/gene_vectors.npy` [11063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11063 or target_col == 11063). Every well: [[B3GNT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
