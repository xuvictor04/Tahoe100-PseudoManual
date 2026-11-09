---
symbol: "UNC13D"
type: "gene"
col: 1712
ensembl_id: "ENSG00000092929"
name: "unc-13 homolog D"
location: "17q25.3"
module: 31
arm: "+"
pooled_cpm: 17.05
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 33
direction_downstream: 17
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# UNC13D

*unc-13 homolog D* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +10.4, q 2e-22, up in 12 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +4.5, q 0.001, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.496× (z -9.4, q 4e-18, down in 21 of 33 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.614× (z -6.5, q 2e-08, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKP3]] (+0.71, fdr 7e-06), [[ARHGAP27]] (+0.69, fdr 7e-06), [[PTK6]] (+0.63, fdr 7e-06); moves opposite to [[ZNRF2P1]] (-0.47, fdr 1e-04), [[ZNRF2P2]] (-0.45, fdr 2e-04), [[WHAMMP1]] (-0.44, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 17 go from it, the strongest it → [[WHAMMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +10.4 | 2e-22 | 12/25 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.6 | 2e-19 | 14/19 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +6.9 | 8e-10 | 6/21 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.5 | 0.001 | 9/30 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.007 | 5/29 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.14 | 8/32 (SW480, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.496×** | -9.4 | 4e-18 | 21/33 (A-172, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -6.5 | 2e-08 | 20/33 (A-427, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -6.4 | 2e-08 | 19/33 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.637×** | -6.0 | 2e-07 | 21/33 (AsPC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.647×** | -5.8 | 6e-07 | 19/33 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -5.0 | 6e-05 | 17/33 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.702×** | -4.8 | 2e-04 | 14/31 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.4 | 6e-04 | 15/33 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -4.3 | 0.001 | 14/33 (HOP62, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.570×** | -3.9 | 0.005 | 12/30 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.615×** | -3.4 | 0.035 | 9/31 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.782×** | -3.3 | 0.046 | 19/33 (A-172, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.789×** | -3.2 | 0.062 | 11/33 (HOP62, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -15.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 64.2 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.8) |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.1) ⚠ cell-cycle shift, explains ~94% of this change |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 53.7 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.142× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 87.1 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 67.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -16.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 26.1 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -11.5) ⚠ cell-cycle shift, explains ~94% of this change |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 5.04 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.115× (z -8.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 6.01 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0459× (z -11.2) |
| [[A-427 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP3]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP27]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PTK6]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ALS2CL]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PSORS1C1]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ADAP1]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CLTB]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GJB3]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[IL2RG]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2P1]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[ZNRF2P2]] | -0.45 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[WHAMMP1]] | -0.44 | -0.39 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises UNC13D's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.11× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[C1orf116]] | B | C1orf116 activity raises UNC13D's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.11× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LPAR5]] | B | LPAR5 activity raises UNC13D's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without LPAR5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises UNC13D's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without MROH3P | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ANXA3]] | B | ANXA3 activity raises UNC13D's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.18× lower at baseline in the lines without ANXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[KLK10]] | B | KLK10 activity raises UNC13D's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.07× lower at baseline in the lines without KLK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[ITGB4]] | B | ITGB4 activity raises UNC13D's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.98× lower at baseline in the lines without ITGB4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PCDH1]] | B | PCDH1 activity raises UNC13D's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[GJB3]] | B | GJB3 activity raises UNC13D's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.96× lower at baseline in the lines without GJB3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[MISP]] | B | MISP activity raises UNC13D's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without MISP | 0.007 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[SEMA3B]] | B | SEMA3B activity raises UNC13D's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without SEMA3B | 0.008 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[KRT16]] | B | KRT16 activity raises UNC13D's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.36× lower at baseline in the lines without KRT16 | 0.009 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHAMMP1]] | B | UNC13D activity lowers WHAMMP1's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.66× higher at baseline in the lines without UNC13D | 0.008 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[B3GNT3]] | B | UNC13D activity raises B3GNT3's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without UNC13D | 0.021 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[TMC6]] | B | UNC13D activity raises TMC6's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without UNC13D | 0.022 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[TMEM184A]] | B | UNC13D activity raises TMEM184A's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without UNC13D | 0.024 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[LPAR5]] | B | UNC13D activity raises LPAR5's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without UNC13D | 0.025 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[KCP]] | B | UNC13D activity raises KCP's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without UNC13D | 0.033 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[UBXN11]] | B | UNC13D activity raises UBXN11's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without UNC13D | 0.041 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[SH2D3A]] | B | UNC13D activity raises SH2D3A's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.60× lower at baseline in the lines without UNC13D | 0.042 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[ARHGEF5]] | B | UNC13D activity raises ARHGEF5's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without UNC13D | 0.048 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[PCDH1]] | B | UNC13D activity raises PCDH1's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without UNC13D | 0.048 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[CRYBG2]] | B | UNC13D activity raises CRYBG2's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without UNC13D | 0.049 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[BAIAP2L2]] | B | UNC13D activity raises BAIAP2L2's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without UNC13D | 0.074 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, 53.2); signed map (1.4, 35.9). **Vector** length 67.0, 13.4% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -6.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | unc-13 homolog D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:75,827,225-75,844,785 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Munc13-4 |
| Gene groups (HGNC) | UNC13 homologs |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70J99](https://www.uniprot.org/uniprotkb/Q70J99) (Protein unc-13 homolog D):

> Plays a role in cytotoxic granule exocytosis in lymphocytes. Required for both granule maturation and granule docking and priming at the immunologic synapse. Regulates assembly of recycling and late endosomal structures, leading to the formation of an endosomal exocytic compartment that fuses with perforin-containing granules at the immunologic synapse and licences them for exocytosis. Regulates Ca(2+)-dependent secretory lysosome exocytosis in mast cells.

**Summary**, from NCBI Gene [201294](https://www.ncbi.nlm.nih.gov/gene/201294):

> This gene encodes a protein that is a member of the UNC13 family, containing similar domain structure as other family members but lacking an N-terminal phorbol ester-binding C1 domain present in other Munc13 proteins. The protein appears to play a role in vesicle maturation during exocytosis and is involved in regulation of cytolytic granules secretion. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis type 3, a genetically heterogeneous, rare autosomal …

**Accessions** — [HGNC:23147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23147) · Entrez [201294](https://www.ncbi.nlm.nih.gov/gene/201294) · UniProt [Q70J99](https://www.uniprot.org/uniprotkb/Q70J99) · Ensembl [ENSG00000092929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092929)

## Data

Gene col 1712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1712); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1712]; `tensor/DDL_lfc|DDL_z.npy` [1712]; `embed/gene_vectors.npy` [1712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1712 or target_col == 1712). Every well: [[UNC13D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC13D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
