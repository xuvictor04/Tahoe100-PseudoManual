---
symbol: "MST1R"
type: "gene"
col: 8858
ensembl_id: "ENSG00000164078"
name: "macrophage stimulating 1 receptor"
location: "3p21.31"
module: 31
arm: "+"
pooled_cpm: 10.67
n_lines_expressing: 26
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 79
direction_downstream: 54
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MST1R

*macrophage stimulating 1 receptor* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.671× (z -6.5, q 5e-08, down in 15 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.82, fdr 7e-06), [[GPR35]] (+0.79, fdr 7e-06), [[ITGB4]] (+0.78, fdr 7e-06); moves opposite to [[SELENOP]] (-0.54, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 79 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); 54 go from it, the strongest it → [[LMO7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.671×** | -6.5 | 5e-08 | 15/24 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.605×** | -5.8 | 2e-06 | 14/24 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.3 | 2e-05 | 15/22 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -5.2 | 3e-05 | 14/24 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -5.0 | 6e-05 | 18/24 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -4.7 | 3e-04 | 12/24 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.669×** | -4.6 | 3e-04 | 15/24 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -4.6 | 3e-04 | 14/23 (A-427, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -3.9 | 0.007 | 16/23 (KATO III, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -3.8 | 0.010 | 10/21 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -3.7 | 0.012 | 13/21 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.013 | 13/24 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -3.4 | 0.027 | 14/23 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.069 | 8/23 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.762×** | -3.0 | 0.099 | 11/24 (HEC-1-A, SW480, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.4) |
| [[KATO III (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.3) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -9.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0539× (z -11.3) |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.162× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -14.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.986 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.82 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GPR35]] | +0.79 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; STRING 479 |
| [[TNS4]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CAPN8]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[SH2D3A]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PADI1]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LAMA3]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[C1orf116]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOP]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 25, C 54. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises MST1R's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without PCDH1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[EPS8L1]] | B | EPS8L1 activity raises MST1R's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.92× lower at baseline in the lines without EPS8L1 | 0.014 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CRYBG2]] | B | CRYBG2 activity strengthens MST1R's drug response | lines that do not express CRYBG2 (6) vs lines expressing it (18) | the lines without CRYBG2 respond 0.23× as strongly (z diff +2.63); strongest at Panobinostat 5 µM: 1.14x vs 0.41x (z diff +5.4) | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; target measured in part of the lines; artifact flags |
| [[LEMD1]] | B | LEMD1 activity raises MST1R's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 3.00× lower at baseline in the lines without LEMD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[ZNF860]] | B | ZNF860 activity raises MST1R's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.20× lower at baseline in the lines without ZNF860 | 0.018 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[CCDC120]] | B | CCDC120 activity raises MST1R's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.89× lower at baseline in the lines without CCDC120 | 0.035 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[ABCC3]] | B | ABCC3 activity raises MST1R's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without ABCC3 | 0.035 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[PDE9A]] | B | PDE9A activity raises MST1R's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without PDE9A | 0.038 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[B3GNT3]] | B | B3GNT3 activity strengthens MST1R's drug response | lines that do not express B3GNT3 (10) vs lines expressing it (14) | the lines without B3GNT3 respond 0.39× as strongly (z diff +2.01); strongest at Panobinostat 0.5 µM: 0.76x vs 0.42x (z diff +3.8) | 0.039 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; target measured in part of the lines; artifact flags |
| [[LMO7]] | B | LMO7 activity raises MST1R's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.82× lower at baseline in the lines without LMO7 | 0.043 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises MST1R's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without ALS2CL | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[IL1RN]] | B | IL1RN activity raises MST1R's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without IL1RN | 0.055 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 19, C 35. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | MST1R activity raises LMO7's level | lines that do not express MST1R (24) vs lines expressing it (26) | 4.07× lower at baseline in the lines without MST1R | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[EPS8L1]] | B | MST1R activity raises EPS8L1's level | lines that do not express MST1R (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without MST1R | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[PKP3]] | B | MST1R activity raises PKP3's level | lines that do not express MST1R (24) vs lines expressing it (26) | 3.51× lower at baseline in the lines without MST1R | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[SNRK]] | B | MST1R activity raises SNRK's level | lines that do not express MST1R (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without MST1R | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[BCL2L1]] | B | MST1R activity raises BCL2L1's level | lines that do not express MST1R (24) vs lines expressing it (26) | 2.55× lower at baseline in the lines without MST1R | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[TJP2]] | B | MST1R activity raises TJP2's level | lines that do not express MST1R (24) vs lines expressing it (26) | 2.48× lower at baseline in the lines without MST1R | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[ALS2CL]] | B | MST1R activity raises ALS2CL's level | lines that do not express MST1R (24) vs lines expressing it (26) | 3.74× lower at baseline in the lines without MST1R | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[TMC6]] | B | MST1R activity raises TMC6's level | lines that do not express MST1R (24) vs lines expressing it (26) | 3.45× lower at baseline in the lines without MST1R | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[SELENOP]] | B | MST1R activity raises SELENOP's level | lines that do not express MST1R (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without MST1R | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[CCDC120]] | B | MST1R activity raises CCDC120's level | lines that do not express MST1R (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without MST1R | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[KRT8]] | B | MST1R activity raises KRT8's level | lines that do not express MST1R (24) vs lines expressing it (26) | 3.54× lower at baseline in the lines without MST1R | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[PSORS1C1]] | B | MST1R activity raises PSORS1C1's level | lines that do not express MST1R (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without MST1R | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 51.4); signed map (4.4, 37.9). **Vector** length 72.1, 22.0% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.5 | +1.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +0.4 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.1 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | macrophage stimulating 1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,886,902-49,903,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDw136, CD136; previously RON, PTK8, SEA |
| Gene groups (HGNC) | CD molecules; IPT domain containing; MET proto-oncogene, receptor tyrosine kinase family |
| Reactome | 2 pathways, smallest: Signaling by MST1; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04912](https://www.uniprot.org/uniprotkb/Q04912) (Macrophage-stimulating protein receptor):

> Receptor tyrosine kinase that transduces signals from the extracellular matrix into the cytoplasm by binding to MST1 ligand. Regulates many physiological processes including cell survival, migration and differentiation. Ligand binding at the cell surface induces autophosphorylation of RON on its intracellular domain that provides docking sites for downstream signaling molecules. Following activation by ligand, interacts with the PI3-kinase subunit PIK3R1, PLCG1 or the adapter GAB1. Recruitment …

**Summary**, from NCBI Gene [4486](https://www.ncbi.nlm.nih.gov/gene/4486):

> This gene encodes a cell surface receptor for macrophage-stimulating protein (MSP) with tyrosine kinase activity. The mature form of this protein is a heterodimer of disulfide-linked alpha and beta subunits, generated by proteolytic cleavage of a single-chain precursor. The beta subunit undergoes tyrosine phosphorylation upon stimulation by MSP. This protein is expressed on the ciliated epithelia of the mucociliary transport apparatus of the lung, and together with MSP, thought to be involved …

**Accessions** — [HGNC:7381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7381) · Entrez [4486](https://www.ncbi.nlm.nih.gov/gene/4486) · UniProt [Q04912](https://www.uniprot.org/uniprotkb/Q04912) · Ensembl [ENSG00000164078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164078)

## Data

Gene col 8858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8858); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8858]; `tensor/DDL_lfc|DDL_z.npy` [8858]; `embed/gene_vectors.npy` [8858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8858 or target_col == 8858). Every well: [[MST1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MST1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
