---
symbol: "RSPH1"
type: "gene"
col: 8310
ensembl_id: "ENSG00000160188"
name: "radial spoke head component 1"
location: "21q22.3"
module: 44
arm: "+"
pooled_cpm: 2.77
n_lines_expressing: 37
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 52
direction_downstream: 12
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# RSPH1

*radial spoke head component 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.77× (z +18.6, q 0e+00, up in 19 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.472× (z -6.3, q 2e-07, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDX2]] (+0.67, fdr 7e-06), [[TJP3]] (+0.65, fdr 7e-06), [[HNF1A-AS1]] (+0.63, fdr 1e-05); moves opposite to [[ZNF595]] (-0.55, fdr 4e-05), [[MDFI]] (-0.50, fdr 3e-05), [[KLC1]] (-0.49, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[PLEKHG6]] → it (grade B ⚠); 12 go from it, the strongest it → [[SLC50A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.77×** | +18.6 | 0e+00 | 19/23 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.38×** | +12.4 | 7e-33 | 26/31 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +12.2 | 8e-32 | 15/22 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +10.4 | 4e-23 | 20/27 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.40×** | +10.3 | 1e-22 | 21/28 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +9.4 | 5e-19 | 2/4 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +8.2 | 1e-14 | 9/21 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +8.2 | 2e-14 | 6/10 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.54×** | +7.5 | 3e-12 | 16/26 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +7.3 | 2e-11 | 5/7 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +5.6 | 9e-07 | 12/29 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +4.7 | 1e-04 | 10/22 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +4.6 | 2e-04 | 8/27 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.10×** | +4.4 | 4e-04 | 2/13 (SW480, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.3 | 8e-04 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.002 | 4/25 (SW480, A-427, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.077 | 5/28 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.098 | 3/24 (SW480, AsPC-1, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.098 | 3/23 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -6.3 | 2e-07 | 16/27 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.507×** | -5.7 | 3e-06 | 15/29 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -4.7 | 6e-04 | 17/30 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.578×** | -4.6 | 6e-04 | 14/24 (HT-29, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.582×** | -4.5 | 6e-04 | 12/23 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.613×** | -4.1 | 0.004 | 11/29 (Panc 03.27, SW480, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.641×** | -3.5 | 0.034 | 12/25 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.683× | -3.1 | 0.13 | 11/25 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.693× | -3.1 | 0.13 | 12/29 (COLO 205, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -13.7) |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -9.1) |
| [[A-172 (line)]] | wt | 0.814 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.4× (z +11.3) | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.000 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.897 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDX2]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TJP3]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CGN]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ELF3]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CLDN3]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.62 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[VIPR1]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PRR15]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PRR15L]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[UGT1A8]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[VIL1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF595]] | -0.55 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MDFI]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[KLC1]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ITGB1BP1]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[BMS1P23]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 51, C 1. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG6]] | B | PLEKHG6 activity raises RSPH1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without PLEKHG6 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[CDH17]] | B | CDH17 activity raises RSPH1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.06× lower at baseline in the lines without CDH17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[TJP3]] | B | TJP3 activity raises RSPH1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TJP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[SMIM2-AS1]] | B | SMIM2-AS1 activity raises RSPH1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without SMIM2-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[TRIM31]] | B | TRIM31 activity raises RSPH1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.89× lower at baseline in the lines without TRIM31 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises RSPH1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without ARHGEF38 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[POF1B]] | B | POF1B activity raises RSPH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without POF1B | 0.009 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[CYP4F12]] | B | CYP4F12 activity raises RSPH1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CYP4F12 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises RSPH1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without TMPRSS2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[RHOV]] | B | RHOV activity raises RSPH1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without RHOV | 0.011 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[MDFI]] | B | MDFI activity raises RSPH1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without MDFI | 0.011 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[CLRN3]] | B | CLRN3 activity raises RSPH1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.97× lower at baseline in the lines without CLRN3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC50A1]] | B | RSPH1 activity raises SLC50A1's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without RSPH1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[PRR15-DT]] | B | RSPH1 activity raises PRR15-DT's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without RSPH1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[RNF43]] | B | RSPH1 activity raises RNF43's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without RSPH1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[BMS1P23]] | B | RSPH1 activity raises BMS1P23's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without RSPH1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[ABHD11]] | B | RSPH1 activity raises ABHD11's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without RSPH1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[CDX2]] | B | RSPH1 activity raises CDX2's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without RSPH1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[PAXIP1-DT]] | B | RSPH1 activity raises PAXIP1-DT's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without RSPH1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[ZDHHC11B]] | B | RSPH1 activity raises ZDHHC11B's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.54× lower at baseline in the lines without RSPH1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[RHOU]] | B | RSPH1 activity raises RHOU's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without RSPH1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[KLC1]] | B | RSPH1 activity strengthens KLC1's drug response | lines that do not express RSPH1 (13) vs lines expressing it (36) | the lines without RSPH1 respond 0.86× as strongly (z diff +0.92); strongest at Ouabain (Octahydrate) 5 µM: 1.21x vs 1.45x (z diff +2.3) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BCL3]] | B | RSPH1 activity strengthens BCL3's drug response | lines that do not express RSPH1 (13) vs lines expressing it (34) | the lines without RSPH1 respond 1.08× as strongly (z diff +0.20); strongest at Idarubicin (hydrochloride) 5 µM: 0.68x vs 0.50x (z diff +2.6) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SORL1]] | C | RSPH1 activity raises SORL1's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without RSPH1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 53.1); signed map (60.5, 3.9). **Vector** length 56.1, 11.7% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.56 to 4); *Aspirin ADME* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | radial spoke head component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,472,486-42,496,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32753, RSP44, RSPH10A, CILD24; previously TSGA2 |
| Gene groups (HGNC) | Axonemal radial spoke subunits; MORN repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYR4](https://www.uniprot.org/uniprotkb/Q8WYR4) (Radial spoke head 1 homolog):

> Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia.

**Summary**, from NCBI Gene [89765](https://www.ncbi.nlm.nih.gov/gene/89765):

> This gene encodes a male meiotic metaphase chromosome-associated acidic protein. This gene is expressed in tissues with motile cilia or flagella, including the trachea, lungs, airway brushings, and testes. Mutations in this gene result in primary ciliary dyskinesia-24. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:12371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12371) · Entrez [89765](https://www.ncbi.nlm.nih.gov/gene/89765) · UniProt [Q8WYR4](https://www.uniprot.org/uniprotkb/Q8WYR4) · Ensembl [ENSG00000160188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160188)

## Data

Gene col 8310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8310); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8310]; `tensor/DDL_lfc|DDL_z.npy` [8310]; `embed/gene_vectors.npy` [8310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8310 or target_col == 8310). Every well: [[RSPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
