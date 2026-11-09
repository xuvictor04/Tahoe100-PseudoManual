---
symbol: "MPZL2"
type: "gene"
col: 7391
ensembl_id: "ENSG00000149573"
name: "myelin protein zero like 2"
location: "11q23.3"
module: 8
arm: "+"
pooled_cpm: 28.06
n_lines_expressing: 21
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 115
direction_downstream: 151
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MPZL2

*myelin protein zero like 2* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +13.0, q 9e-36, up in 9 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sapanisertib (drug)]] 0.5 µM: 1.49× (z +3.8, q 0.022, up in 0 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.488× (z -13.4, q 2e-38, down in 19 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM45B]] (+0.83, fdr 7e-06), [[ITGB6]] (+0.76, fdr 7e-06), [[EPS8L3]] (+0.74, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 115 arrows point to it, the strongest [[LINC03041]] → it (grade B ⚠); 151 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +13.0 | 9e-36 | 9/20 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.8 | 6e-35 | 8/17 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.6 | 8e-09 | 4/17 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.022 | 0/19 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.040 | 3/19 (Hs 766T, SW1417, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.050 | 2/19 (SW480, AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.29×** | +3.4 | 0.050 | 3/18 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.056 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -13.4 | 2e-38 | 19/19 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -11.7 | 4e-29 | 19/19 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -10.8 | 7e-25 | 19/19 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.626×** | -6.2 | 7e-08 | 18/19 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 9e-08 | 18/19 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -6.1 | 1e-07 | 17/19 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.727×** | -5.8 | 4e-07 | 4/19 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -4.8 | 1e-04 | 14/19 (SW480, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.6 | 3e-04 | 11/19 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.712×** | -4.5 | 4e-04 | 15/19 (SW480, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -4.2 | 0.001 | 16/19 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.491×** | -4.1 | 0.002 | 15/19 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.017 | 2/19 (NCI-H1573, NCI-H2347) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.5 | 0.019 | 2/20 (hTERT-HPNE, NCI-H2122) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.830×** | -3.5 | 0.019 | 17/19 (SW480, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.755×** | -3.4 | 0.021 | 2/19 (SW480, BT-474) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -3.2 | 0.043 | 8/19 (SW480, HCT15, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 73.3 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.5) |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0293× (z -32.0) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.1) |
| [[KATO III (line)]] | alt | 34.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.2) |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -17.2) |
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.7) |
| [[LS 180 (line)]] | wt | 55.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 80.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.6) |
| [[LoVo (line)]] | wt | 31.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 99.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -23.6) |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.8) |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.9) |
| [[SW48 (line)]] | wt | 52.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.6) |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.4) |
| [[SW1417 (line)]] | alt | 44.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.8) |
| [[A-172 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45B]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[FGD5]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KRT23]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SLC6A14]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[C9orf152]] | +0.68 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CEACAM5]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |
| [[SPINT1]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*115 arrows, 115 of them with an alert ⚠; grade A 0, B 12, C 103. Shown: the 12 strongest; 103 more arrows (103 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03041]] | B | LINC03041 activity lowers MPZL2's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 8.18× higher at baseline in the lines without LINC03041 | 0.001 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers MPZL2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.57× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[BNC2]] | B | BNC2 activity lowers MPZL2's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 5.85× higher at baseline in the lines without BNC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[TJP2]] | B | TJP2 activity raises MPZL2's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 4.29× lower at baseline in the lines without TJP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises MPZL2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.02× lower at baseline in the lines without LMO7 | 0.017 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises MPZL2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without RAPGEF5 | 0.028 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises MPZL2's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.86× lower at baseline in the lines without ATP1B1 | 0.033 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises MPZL2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.42× lower at baseline in the lines without EPS8L1 | 0.041 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[FAM20C]] | B | FAM20C activity lowers MPZL2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 4.23× higher at baseline in the lines without FAM20C | 0.089 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[DMTN]] | B | DMTN activity raises MPZL2's level | lines that do not express DMTN (14) vs lines expressing it (36) | 3.93× lower at baseline in the lines without DMTN | 0.094 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises MPZL2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.78× lower at baseline in the lines without TNFRSF21 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[MAPK13]] | B | MAPK13 activity raises MPZL2's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 4.18× lower at baseline in the lines without MAPK13 | 0.096 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |

### Downstream of this gene

*151 arrows, 151 of them with an alert ⚠; grade A 0, B 42, C 109. Shown: the 12 strongest; 139 more arrows (139 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | MPZL2 activity raises EPS8L1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.28× lower at baseline in the lines without MPZL2 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[TJP2]] | B | MPZL2 activity raises TJP2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without MPZL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[LMO7]] | B | MPZL2 activity raises LMO7's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 5.09× lower at baseline in the lines without MPZL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[FAM83E]] | B | MPZL2 activity raises FAM83E's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.92× lower at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[ARHGEF16]] | B | MPZL2 activity raises ARHGEF16's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.55× lower at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[ELMO3]] | B | MPZL2 activity raises ELMO3's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 2.40× lower at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[DCLK2]] | B | MPZL2 activity lowers DCLK2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 5.82× higher at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[DLG3]] | B | MPZL2 activity raises DLG3's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.40× lower at baseline in the lines without MPZL2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[PLS1]] | B | MPZL2 activity raises PLS1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.90× lower at baseline in the lines without MPZL2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[TNFRSF21]] | B | MPZL2 activity raises TNFRSF21's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.16× lower at baseline in the lines without MPZL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[MROH7]] | B | MPZL2 activity raises MROH7's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 2.41× lower at baseline in the lines without MPZL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[BNC2]] | B | MPZL2 activity lowers BNC2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 6.85× higher at baseline in the lines without MPZL2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.1, 56.5); signed map (59.9, 8.1). **Vector** length 84.0, 31.7% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.1 | +1.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | myelin protein zero like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,253,416-118,264,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EVA; previously EVA1 |
| Gene groups (HGNC) | V-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | KRAS_SIGNALING_UP, APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [O60487](https://www.uniprot.org/uniprotkb/O60487) (Myelin protein zero-like protein 2):

> Mediates homophilic cell-cell adhesion.

**Summary**, from NCBI Gene [10205](https://www.ncbi.nlm.nih.gov/gene/10205):

> Thymus development depends on a complex series of interactions between thymocytes and the stromal component of the organ. Epithelial V-like antigen (EVA) is expressed in thymus epithelium and strongly downregulated by thymocyte developmental progression. This gene is expressed in the thymus and in several epithelial structures early in embryogenesis. It is highly homologous to the myelin protein zero and, in thymus-derived epithelial cell lines, is poorly soluble in nonionic detergents, …

**Accessions** — [HGNC:3496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3496) · Entrez [10205](https://www.ncbi.nlm.nih.gov/gene/10205) · UniProt [O60487](https://www.uniprot.org/uniprotkb/O60487) · Ensembl [ENSG00000149573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149573)

## Data

Gene col 7391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7391); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7391]; `tensor/DDL_lfc|DDL_z.npy` [7391]; `embed/gene_vectors.npy` [7391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7391 or target_col == 7391). Every well: [[MPZL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPZL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
