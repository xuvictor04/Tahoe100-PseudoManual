---
symbol: "ZIM2-AS1"
type: "gene"
col: 15635
ensembl_id: "ENSG00000269793"
name: "ZIM2 antisense RNA 1"
location: "19q13.43"
module: 129
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 11
direction_downstream: 20
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZIM2-AS1

*ZIM2 antisense RNA 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.43× (z +4.2, q 0.013, up in 3 of 15 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.1, q 0.013, up in 3 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.296× (z -15.0, q 0e+00, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF177]] (+0.71, fdr 7e-06), [[ZNF71]] (+0.71, fdr 7e-06, ⚠ same locus), [[ZNF559-ZNF177]] (+0.69, fdr 7e-06), [[ZNF568]] (+0.64, fdr 8e-06); moves opposite to [[INPP4B]] (-0.51, fdr 1e-05), [[FOXP1]] (-0.50, fdr 3e-05), [[MECOM]] (-0.48, fdr 1e-04).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); 20 go from it, the strongest it → [[ZNF567-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.2 | 0.013 | 3/15 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.013 | 3/33 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.7 | 0.034 | 1/7 (NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.034 | 2/23 (RKO, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.31× | +3.3 | 0.11 | 4/29 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.2 | 0.12 | 2/25 (NCI-H460, A-427) | top dose only |  |
| [[Ataluren (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.12 | 3/28 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.30× | +3.1 | 0.12 | 6/27 (PANC-1, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.296×** | -15.0 | 0e+00 | 29/33 (SW1417, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.305×** | -14.6 | 0e+00 | 28/34 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -12.6 | 5e-34 | 23/33 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -11.4 | 8e-28 | 21/25 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.402×** | -11.2 | 5e-27 | 21/31 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.595×** | -9.0 | 2e-17 | 18/27 (A549, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -5.9 | 3e-07 | 14/30 (hTERT-HPNE, Hs 766T, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -5.8 | 4e-07 | 12/28 (A-172, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.776×** | -4.4 | 7e-04 | 12/29 (A-172, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.696×** | -4.3 | 0.001 | 11/19 (A549, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.707×** | -4.3 | 0.001 | 11/35 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.001 | 8/27 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.732×** | -3.8 | 0.005 | 12/33 (A-172, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -3.6 | 0.013 | 8/26 (A-172, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.1 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0647× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.190× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 5.87 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0618× (z -15.2) |
| [[A549 (line)]] | wt | 6.51 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -17.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0926× (z -9.4) |
| [[HOP62 (line)]] | alt | 4.73 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0384× (z -13.7) |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0447× (z -8.9) |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0823× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.02 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0705× (z -9.9) |
| [[SW480 (line)]] | alt | 2.66 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -9.0) |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0748× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 8.65 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0625× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.55 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0766× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 5.11 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0599× (z -9.3) |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0452× (z -11.8) |
| [[A-427 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.430 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF177]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ZNF71]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF559-ZNF177]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ZFP28]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 | ⚠ same locus (38.5 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF568]] | +0.64 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[ZNF470]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 | ⚠ same locus (6.4 kb, same strand: neighbours can correlate without regulation) |
| [[GET1-SH3BGR]] | +0.56 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ZNF549]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | +0.54 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[INTS4P1]] | +0.53 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ZNF559]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TFAP2E]] | +0.53 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZNF814]] | +0.52 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[LINC02609]] | +0.52 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[LSP1P5-1]] | +0.52 | +0.34 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4B]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[FOXP1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MECOM]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[VCAM1]] | -0.47 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[FIGN]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RFX3]] | -0.46 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[PARP8]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[AKR1B1]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SIPA1L2]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[LEPROT]] | -0.45 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[CD164]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[TRIP12]] | -0.45 | -0.27 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers ZIM2-AS1's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.21× higher at baseline in the lines without THRB | 0.001 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[ZNF471]] | B | ZNF471 activity raises ZIM2-AS1's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 2.90× lower at baseline in the lines without ZNF471 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1 |
| [[ZNF568]] | B | ZNF568 activity raises ZIM2-AS1's level | lines that do not express ZNF568 (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without ZNF568 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF829, ACTN2, ZNF880 |
| [[BOLA3-DT]] | B | BOLA3-DT activity raises ZIM2-AS1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without BOLA3-DT | 0.013 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[CRYBG1]] | B | CRYBG1 activity lowers ZIM2-AS1's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 1.57× higher at baseline in the lines without CRYBG1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[MAP6]] | B | MAP6 activity raises ZIM2-AS1's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without MAP6 | 0.051 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |
| [[ADGRG6]] | B | ADGRG6 activity lowers ZIM2-AS1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.99× higher at baseline in the lines without ADGRG6 | 0.061 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[ZNF567-DT]] | B | ZNF567-DT activity raises ZIM2-AS1's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without ZNF567-DT | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF71]] | C | ZNF71 activity raises ZIM2-AS1's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 3.97× lower at baseline in the lines without ZNF71 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28; co-absent with the target |
| [[ZFP28]] | C | ZFP28 activity raises ZIM2-AS1's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 3.18× lower at baseline in the lines without ZFP28 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6; co-absent with the target |
| [[ZNF470]] | C | ZNF470 activity raises ZIM2-AS1's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 3.20× lower at baseline in the lines without ZNF470 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF567-DT]] | B | ZIM2-AS1 activity raises ZNF567-DT's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ZIM2-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF461]] | B | ZIM2-AS1 activity raises ZNF461's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 2.90× lower at baseline in the lines without ZIM2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF251]] | B | ZIM2-AS1 activity raises ZNF251's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without ZIM2-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[PGBD1]] | B | ZIM2-AS1 activity raises PGBD1's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without ZIM2-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[THRB]] | B | ZIM2-AS1 activity lowers THRB's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 2.45× higher at baseline in the lines without ZIM2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[OGG1]] | B | ZIM2-AS1 activity raises OGG1's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without ZIM2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF329]] | B | ZIM2-AS1 activity raises ZNF329's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without ZIM2-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF782]] | B | ZIM2-AS1 activity raises ZNF782's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.16× lower at baseline in the lines without ZIM2-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF814]] | B | ZIM2-AS1 activity raises ZNF814's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without ZIM2-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF583]] | B | ZIM2-AS1 activity raises ZNF583's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without ZIM2-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF568]] | B | ZIM2-AS1 activity raises ZNF568's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without ZIM2-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF471]] | B | ZIM2-AS1 activity raises ZNF471's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 3.69× lower at baseline in the lines without ZIM2-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, 28.1); signed map (-17.7, -15.7). **Vector** length 49.9, 7.83% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -12.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -14.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -15.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Alpelisib (drug)]] 0.5 µM |  | -0.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ZIM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.43 — chr19:56,595,313-56,799,602 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ZIM2as |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51304) · Entrez [101929059](https://www.ncbi.nlm.nih.gov/gene/101929059) · Ensembl [ENSG00000269793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269793)

## Data

Gene col 15635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15635); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15635]; `tensor/DDL_lfc|DDL_z.npy` [15635]; `embed/gene_vectors.npy` [15635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15635 or target_col == 15635). Every well: [[ZIM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZIM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
