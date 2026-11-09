---
symbol: "PGAP4"
type: "gene"
col: 9076
ensembl_id: "ENSG00000165152"
name: "post-GPI attachment to proteins GalNAc transferase 4"
location: "9q31.1"
module: 107
arm: "+"
pooled_cpm: 4.07
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# PGAP4

*post-GPI attachment to proteins GalNAc transferase 4* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.0, q 2e-16, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.298× (z -13.3, q 2e-37, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (65 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 35 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS4-AS1]] (+0.64, fdr 7e-05), [[DBR1]] (+0.60, fdr 4e-04), [[KLHL42]] (+0.59, fdr 6e-04); moves opposite to [[GNG7]] (-0.56, fdr 8e-05), [[MFSD12]] (-0.56, fdr 3e-04), [[GNAI2]] (-0.56, fdr 8e-04, ⚠ not reproduced), [[CADM4]] (-0.53, fdr 3e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02086]] → it (grade C ⚠); 11 go from it, the strongest it → [[EAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.0 | 2e-16 | 16/23 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +7.4 | 3e-11 | 13/30 (NCI-H460, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +5.6 | 5e-06 | 8/19 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.6 | 6e-04 | 6/19 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.6 | 0.037 | 1/8 (SW480) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 1.32× | +3.0 | 0.21 | 4/28 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.21 | 2/28 (J82, RKO) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.298×** | -13.3 | 2e-37 | 26/30 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.446×** | -12.6 | 8e-34 | 23/26 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.319×** | -12.5 | 8e-34 | 26/30 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -11.1 | 3e-26 | 23/29 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -9.6 | 1e-19 | 19/30 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.547×** | -6.6 | 3e-09 | 13/25 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -6.0 | 1e-07 | 16/27 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -6.0 | 1e-07 | 15/29 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.590×** | -5.8 | 4e-07 | 17/30 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.602×** | -5.6 | 1e-06 | 13/28 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -4.7 | 1e-04 | 10/30 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -3.8 | 0.007 | 6/25 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -3.6 | 0.013 | 9/28 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.016 | 8/27 (NCI-H23, CHP-212, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.018 | 7/27 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.018 | 4/28 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.82 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.9) |
| [[SW480 (line)]] | alt | 8.73 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -12.9) |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.0) |
| [[KATO III (line)]] | alt | 12.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0945× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 7.85 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -13.9) |
| [[J82 (line)]] | alt | 7.48 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -14.7) |
| [[LS 180 (line)]] | wt | 5.99 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0627× (z -11.5) |
| [[SNU-423 (line)]] | alt | 3.48 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0592× (z -8.6) |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0584× (z -9.2) |
| [[HCT15 (line)]] | alt | 7.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -9.3) |
| [[HOP62 (line)]] | alt | 5.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 5.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -9.0) |
| [[PANC-1 (line)]] | alt | 4.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 4.65 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0459× (z -9.5) |
| [[A-172 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS4-AS1]] | +0.64 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[DBR1]] | +0.60 | +0.24 / +0.64 | both halves | 4e-04 |  |
| [[KLHL42]] | +0.59 | +0.22 / +0.47 | both halves | 6e-04 |  |
| [[SMAD1]] | +0.58 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[CCNJ]] | +0.58 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[LINC02086]] | +0.58 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[RWDD2B]] | +0.56 | +0.18 / +0.43 | ⚠ not reproduced | 0.001 |  |
| [[PIGW]] | +0.56 | +0.22 / +0.46 | both halves | 6e-04 |  |
| [[METTL13]] | +0.56 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[PPP1R8]] | +0.56 | +0.17 / +0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[MRM1]] | +0.55 | +0.32 / +0.41 | both halves | 2e-04 |  |
| [[UROD]] | +0.55 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[SLC16A14]] | +0.55 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[ZNF234]] | +0.55 | +0.41 / +0.26 | both halves | 3e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG7]] | -0.56 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[MFSD12]] | -0.56 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.56 | -0.27 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[CADM4]] | -0.53 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[ACAP3]] | -0.52 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[SLC25A42]] | -0.51 | -0.39 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[SPAG9]] | -0.50 | -0.18 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[MARCHF2]] | -0.50 | -0.46 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[CEP131]] | -0.49 | -0.06 / -0.30 | ⚠ not reproduced | 0.004 |  |
| [[KIAA1328]] | -0.49 | -0.20 / -0.20 | both halves | 7e-04 |  |
| [[PI4KA]] | -0.49 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[GGA1]] | -0.49 | -0.28 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[LLGL2]] | -0.49 | -0.27 / -0.24 | both halves | 5e-04 |  |
| [[TBC1D10A]] | -0.47 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[NBEAL1]] | -0.47 | -0.29 / -0.21 | both halves | 7e-04 |  |
| [[ABAT]] | -0.47 | -0.24 / -0.38 | both halves | 4e-04 |  |
| [[MAPK8IP3]] | -0.47 | -0.29 / -0.24 | both halves | 4e-04 |  |
| [[SYP]] | -0.46 | -0.32 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02086]] | C | LINC02086 activity raises PGAP4's level | lines that do not express LINC02086 (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without LINC02086 | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MIR4713HG, SERPINB9, PRSS3; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EAF1]] | B | PGAP4 activity raises EAF1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.23× lower at baseline in the lines without PGAP4 | 0.011 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[NNT-AS1]] | B | PGAP4 activity raises NNT-AS1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PGAP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[MID1IP1]] | B | PGAP4 activity raises MID1IP1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.43× lower at baseline in the lines without PGAP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[ATMIN]] | B | PGAP4 activity lowers ATMIN's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.25× higher at baseline in the lines without PGAP4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[SETMAR]] | B | PGAP4 activity raises SETMAR's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.10× lower at baseline in the lines without PGAP4 | 0.061 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[ITPKB]] | B | PGAP4 activity raises ITPKB's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without PGAP4 | 0.068 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[NNT]] | B | PGAP4 activity raises NNT's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without PGAP4 | 0.079 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[JRKL]] | B | PGAP4 activity raises JRKL's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without PGAP4 | 0.084 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[DBR1]] | B | PGAP4 activity raises DBR1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.10× lower at baseline in the lines without PGAP4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[FN3KRP]] | B | PGAP4 activity raises FN3KRP's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without PGAP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[SMG8]] | B | PGAP4 activity raises SMG8's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.01× lower at baseline in the lines without PGAP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.371). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.0, 10.3); signed map (25.7, -27.0). **Vector** length 45.9, 7.40% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | -0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -13.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.5 | -12.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -9.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | -2.7 |
|  | [[Sildenafil (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Rifaximin (drug)]] 5 µM |  | -0.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | post-GPI attachment to proteins GalNAc transferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:101,473,170-101,533,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12992; previously C9orf125, TMEM246 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRR3](https://www.uniprot.org/uniprotkb/Q9BRR3) (GPI-N-acetylgalactosamine transferase PGAP4):

> Golgi-resident glycosylphosphatidylinositol (GPI)-N-acetylgalactosamine transferase that catalyzes the N-acetyl-beta-D-galactosamine transfer from an UDP-N-acetyl-alpha-D-galactosamine to the 4-OH-position of the first mannose of the glycosylphosphatidylinositol (GPI) of a GPI-anchored protein (GPI-AP). This modification occurs after the fatty acid remodeling step of the GPI-anchor maturation.

**Summary**, from NCBI Gene [84302](https://www.ncbi.nlm.nih.gov/gene/84302):

> Enables glycosyltransferase activity. Involved in GPI anchor biosynthetic process. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28180) · Entrez [84302](https://www.ncbi.nlm.nih.gov/gene/84302) · UniProt [Q9BRR3](https://www.uniprot.org/uniprotkb/Q9BRR3) · Ensembl [ENSG00000165152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165152)

## Data

Gene col 9076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9076); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9076]; `tensor/DDL_lfc|DDL_z.npy` [9076]; `embed/gene_vectors.npy` [9076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9076 or target_col == 9076). Every well: [[PGAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
