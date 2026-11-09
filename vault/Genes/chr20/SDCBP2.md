---
symbol: "SDCBP2"
type: "gene"
col: 4661
ensembl_id: "ENSG00000125775"
name: "syndecan binding protein 2"
location: "20p13"
module: 31
arm: "+"
pooled_cpm: 21.36
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 85
direction_downstream: 36
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SDCBP2

*syndecan binding protein 2* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.03× (z +14.0, q 1e-41, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.692× (z -6.6, q 2e-08, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8L1]] (+0.78, fdr 7e-06), [[DSG3]] (+0.69, fdr 7e-06), [[TMPRSS4]] (+0.69, fdr 7e-06); moves opposite to [[SEC22C]] (-0.51, fdr 3e-05), [[SOX2]] (-0.48, fdr 9e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 85 arrows point to it, the strongest [[NPSR1]] → it (grade B ⚠); 36 go from it, the strongest it → [[LAMB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.03×** | +14.0 | 1e-41 | 26/29 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +11.1 | 2e-26 | 12/30 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +6.1 | 1e-07 | 3/11 (AsPC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.1 | 1e-07 | 4/20 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.5 | 4e-06 | 9/31 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.13×** | +5.0 | 6e-05 | 10/31 (HEC-1-A, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 3e-04 | 13/29 (HT-29, LoVo, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 8e-04 | 12/30 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.4 | 8e-04 | 7/28 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.0 | 0.004 | 9/29 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.014 | 6/29 (HEC-1-A, LS 180, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.3 | 0.051 | 6/28 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 8/29 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -6.6 | 2e-08 | 18/31 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -5.3 | 4e-05 | 18/30 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.654×** | -5.2 | 4e-05 | 13/29 (LoVo, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.710×** | -4.3 | 0.002 | 14/30 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -4.3 | 0.002 | 12/29 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.700×** | -4.0 | 0.005 | 10/30 (SW480, KATO III, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.731×** | -4.0 | 0.005 | 6/31 (SW480, CHP-212, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.012 | 10/31 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.745×** | -3.7 | 0.012 | 10/30 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.797×** | -3.6 | 0.016 | 8/31 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.016 | 10/31 (LoVo, LS 180, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.070 | 7/30 (LoVo, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.070 | 7/32 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.092 | 8/31 (HOP62, SW 1271, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.093 | 9/29 (SW480, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 114 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.8) |
| [[LoVo (line)]] | wt | 55.5 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.1) |
| [[KATO III (line)]] | alt | 148 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -20.4) |
| [[NCI-H1573 (line)]] | alt | 66.4 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0707× (z -28.3) |
| [[COLO 205 (line)]] | alt | 186 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.9) |
| [[HT-29 (line)]] | alt | 82.0 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 62.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.1) |
| [[BT-474 (line)]] | alt | 12.3 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 27.1× (z +13.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0994× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 16.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.03× (z +8.6) | — |
| [[A-172 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8L1]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[DSG3]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[FA2H]] | +0.64 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[CALB1]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[KIAA0040]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[LIPH]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[RDH13]] | +0.62 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[FUT3]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC22C]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SOX2]] | -0.48 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*85 arrows, 85 of them with an alert ⚠; grade A 0, B 68, C 17. Shown: the 12 strongest; 73 more arrows (73 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPSR1]] | B | NPSR1 activity raises SDCBP2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 10.86× lower at baseline in the lines without NPSR1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[FAM3D]] | B | FAM3D activity raises SDCBP2's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 9.47× lower at baseline in the lines without FAM3D | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[ADCY4]] | B | ADCY4 activity raises SDCBP2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 5.19× lower at baseline in the lines without ADCY4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[LINC01559]] | B | LINC01559 activity raises SDCBP2's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 6.44× lower at baseline in the lines without LINC01559 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises SDCBP2's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 4.00× lower at baseline in the lines without INAVA, MROH3P | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[CATSPERB]] | B | CATSPERB activity raises SDCBP2's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.17× lower at baseline in the lines without CATSPERB | 0.001 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[SGPP2]] | B | SGPP2 activity raises SDCBP2's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 4.82× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[B3GNT3]] | B | B3GNT3 activity raises SDCBP2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.08× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SLC44A4]] | B | SLC44A4 activity raises SDCBP2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.55× lower at baseline in the lines without SLC44A4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[GCNT3]] | B | GCNT3 activity raises SDCBP2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.82× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TFF1]] | B | TFF1 activity raises SDCBP2's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.38× lower at baseline in the lines without TFF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[SLC5A1]] | B | SLC5A1 activity raises SDCBP2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 5.54× lower at baseline in the lines without SLC5A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 21, C 15. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB3]] | B | SDCBP2 activity raises LAMB3's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.23× lower at baseline in the lines without SDCBP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[TMEM154]] | B | SDCBP2 activity raises TMEM154's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without SDCBP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[ALS2CL]] | B | SDCBP2 activity strengthens ALS2CL's drug response | lines that do not express SDCBP2 (11) vs lines expressing it (24) | the lines without SDCBP2 respond 0.43× as strongly (z diff +1.65); strongest at Panobinostat 0.5 µM: 1.25x vs 0.45x (z diff +5.6) | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2; target measured in part of the lines; artifact flags |
| [[SGPP2]] | B | SDCBP2 activity raises SGPP2's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.07× lower at baseline in the lines without SDCBP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[KPNA7]] | B | SDCBP2 activity raises KPNA7's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.29× lower at baseline in the lines without SDCBP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[CAPN8]] | B | SDCBP2 activity raises CAPN8's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 3.29× lower at baseline in the lines without SDCBP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[MROH3P]] | B | SDCBP2 activity raises MROH3P's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without SDCBP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[ADCY4]] | B | SDCBP2 activity raises ADCY4's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.16× lower at baseline in the lines without SDCBP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[PADI1]] | B | SDCBP2 activity raises PADI1's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.74× lower at baseline in the lines without SDCBP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[LPAR5]] | B | SDCBP2 activity raises LPAR5's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without SDCBP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[MYO5B]] | B | SDCBP2 activity raises MYO5B's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.12× lower at baseline in the lines without SDCBP2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[LINC01564]] | B | SDCBP2 activity raises LINC01564's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without SDCBP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.5, 54.9); signed map (58.0, 8.6). **Vector** length 95.0, 27.1% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -2.5 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | syndecan binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,309,909-1,329,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST-2, SITAC18 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H190](https://www.uniprot.org/uniprotkb/Q9H190) (Syntenin-2):

> Binds phosphatidylinositol 4,5-bisphosphate (PIP2). May play a role in the organization of nuclear PIP2, cell division and cell survival.

**Summary**, from NCBI Gene [27111](https://www.ncbi.nlm.nih.gov/gene/27111):

> The protein encoded by this gene contains two class II PDZ domains. PDZ domains facilitate protein-protein interactions by binding to the cytoplasmic C-terminus of transmembrane proteins, and PDZ-containing proteins mediate cell signaling and the organization of protein complexes. The encoded protein binds to phosphatidylinositol 4, 5-bisphosphate (PIP2) and plays a role in nuclear PIP2 organization and cell division. Alternatively spliced transcript variants encoding multiple isoforms have …

**Accessions** — [HGNC:15756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15756) · Entrez [27111](https://www.ncbi.nlm.nih.gov/gene/27111) · UniProt [Q9H190](https://www.uniprot.org/uniprotkb/Q9H190) · Ensembl [ENSG00000125775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125775)

## Data

Gene col 4661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4661); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4661]; `tensor/DDL_lfc|DDL_z.npy` [4661]; `embed/gene_vectors.npy` [4661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4661 or target_col == 4661). Every well: [[SDCBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDCBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
