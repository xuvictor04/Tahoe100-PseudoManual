---
symbol: "GLIPR2"
type: "gene"
col: 4367
ensembl_id: "ENSG00000122694"
name: "GLI pathogenesis related 2"
location: "9p13.3"
module: 115
arm: "+"
pooled_cpm: 5.79
n_lines_expressing: 41
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# GLIPR2

*GLI pathogenesis related 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.83× (z +15.6, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -8.9, q 4e-16, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTN1]] (+0.62, fdr 7e-06), [[WIPF3]] (+0.61, fdr 7e-06), [[ARVCF]] (+0.61, fdr 1e-05); moves opposite to [[FARS2]] (-0.53, fdr 4e-04), [[IPO11]] (-0.52, fdr 2e-05), [[TCEANC2]] (-0.48, fdr 4e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADAMTS7]] → it (grade B ⚠); 6 go from it, the strongest it → [[PDZD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.83×** | +15.6 | 0e+00 | 35/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.69×** | +10.5 | 2e-23 | 30/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +10.4 | 3e-23 | 28/38 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +9.5 | 2e-19 | 29/38 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +9.4 | 5e-19 | 25/39 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +8.5 | 2e-15 | 25/39 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +6.5 | 7e-09 | 22/38 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.88×** | +6.5 | 7e-09 | 4/8 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.81×** | +6.3 | 1e-08 | 12/23 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.77×** | +5.8 | 3e-07 | 13/21 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +4.6 | 2e-04 | 13/38 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.006 | 13/32 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.007 | 11/35 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.011 | 7/38 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +3.4 | 0.025 | 8/36 (SW480, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.030 | 6/39 (SW480, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -8.9 | 4e-16 | 28/39 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.506×** | -6.8 | 3e-09 | 24/36 (CHP-212, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -6.6 | 6e-09 | 21/31 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -6.1 | 1e-07 | 20/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -5.7 | 2e-06 | 11/26 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -5.4 | 6e-06 | 19/37 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -5.2 | 2e-05 | 15/33 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.622×** | -5.1 | 3e-05 | 14/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.686×** | -4.0 | 0.004 | 12/37 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -3.9 | 0.005 | 12/37 (Panc 03.27, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.93 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.17× (z +11.8) | — |
| [[LoVo (line)]] | wt | 10.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.1) ⚠ cell-cycle shift, explains ~44% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0787× (z -14.2) ⚠ toxic |
| [[A498 (line)]] | wt | 18.8 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 6.50 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HOP62 (line)]] | alt | 3.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.5 µM 0.0514× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 2.03 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTN1]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[WIPF3]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ARVCF]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[BIK]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PLD5]] | +0.57 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FSD1]] | +0.56 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.55 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[ACHE]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CCDC136]] | +0.54 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NPL]] | +0.53 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.53 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[TMEM40]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARS2]] | -0.53 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[IPO11]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[TCEANC2]] | -0.48 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[MIPEP]] | -0.47 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ULK4]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SLC16A4-AS1]] | -0.47 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[CEP20]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SPATA17]] | -0.47 | -0.12 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[ANKRD42]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[LINC00630]] | -0.46 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[POLR1HASP]] | -0.46 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[TSN]] | -0.46 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[DPAGT1]] | -0.46 | -0.51 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS7]] | B | ADAMTS7 activity raises GLIPR2's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without ADAMTS7 | 0.005 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises GLIPR2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without PDZD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SEMA6B]] | B | SEMA6B activity raises GLIPR2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without SEMA6B | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ADGRA2]] | B | ADGRA2 activity raises GLIPR2's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.62× lower at baseline in the lines without ADGRA2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises GLIPR2's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without SLC29A4 | 0.042 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[FERMT2]] | B | FERMT2 activity raises GLIPR2's level | lines that do not express FERMT2 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without FERMT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF512B, HLTF, SIX1 |
| [[ROBO3]] | B | ROBO3 activity raises GLIPR2's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 2.91× lower at baseline in the lines without ROBO3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[TMCC2]] | B | TMCC2 activity raises GLIPR2's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 3.43× lower at baseline in the lines without TMCC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[FSD1]] | B | FSD1 activity raises GLIPR2's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without FSD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | GLIPR2 activity raises PDZD4's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.91× lower at baseline in the lines without GLIPR2 | 0.024 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[ADAMTS7]] | B | GLIPR2 activity raises ADAMTS7's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without GLIPR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[KSR1]] | B | GLIPR2 activity raises KSR1's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 1.61× lower at baseline in the lines without GLIPR2 | 0.065 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[STX11]] | B | GLIPR2 activity raises STX11's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without GLIPR2 | 0.066 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[LINC00630]] | B | GLIPR2 activity raises LINC00630's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without GLIPR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[FERMT2]] | B | GLIPR2 activity raises FERMT2's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.30× lower at baseline in the lines without GLIPR2 | 0.081 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.0, 35.2); signed map (29.9, 24.0). **Vector** length 62.2, 11.1% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +15.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.5 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.8 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | GLI pathogenesis related 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:36,136,536-36,163,913 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAPR-1; previously C9orf19 |
| Gene groups (HGNC) | CAP superfamily |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

UniProt [Q9H4G4](https://www.uniprot.org/uniprotkb/Q9H4G4) carries no function annotation.

**Summary**, from NCBI Gene [152007](https://www.ncbi.nlm.nih.gov/gene/152007):

> Enables protein homodimerization activity. Involved in positive regulation of ERK1 and ERK2 cascade; positive regulation of epithelial cell migration; and positive regulation of epithelial to mesenchymal transition. Located in Golgi membrane. Biomarker of pancreatic ductal adenocarcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18007) · Entrez [152007](https://www.ncbi.nlm.nih.gov/gene/152007) · UniProt [Q9H4G4](https://www.uniprot.org/uniprotkb/Q9H4G4) · Ensembl [ENSG00000122694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122694)

## Data

Gene col 4367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4367); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4367]; `tensor/DDL_lfc|DDL_z.npy` [4367]; `embed/gene_vectors.npy` [4367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4367 or target_col == 4367). Every well: [[GLIPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
