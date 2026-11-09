---
symbol: "GOLGA2P5"
type: "gene"
col: 14169
ensembl_id: "ENSG00000238105"
name: "GOLGA2 pseudogene 5"
location: "12q23.1"
module: 27
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GOLGA2P5

*GOLGA2 pseudogene 5* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +8.8, q 6e-16, up in 17 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -6.7, q 1e-08, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2P5-1]] (+0.87, fdr 7e-06, ⚠ same locus), [[SPINT1-AS1]] (+0.63, fdr 1e-05), [[HOTAIR]] (+0.58, fdr 4e-05), [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.56, fdr 1e-05); moves opposite to [[ACTG1]] (-0.53, fdr 3e-05), [[SH3BGRL3]] (-0.51, fdr 1e-04), [[FLNB]] (-0.49, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPCAM-DT]] → it (grade B ⚠); 2 go from it, the strongest it → [[EPCAM-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +8.8 | 6e-16 | 17/29 (SHP-77, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +7.5 | 2e-11 | 3/8 (LS 180, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.4 | 2e-11 | 5/8 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.2 | 7e-08 | 9/16 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.3 | 1e-05 | 15/26 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.4 | 0.001 | 4/18 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.015 | 8/38 (KATO III, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 1.43× | +3.1 | 0.12 | 2/18 (NCI-H1792, PANC-1) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.14 | 7/39 (COLO 205, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -6.7 | 1e-08 | 24/41 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -5.5 | 1e-05 | 17/35 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.670×** | -5.1 | 5e-05 | 18/39 (SW480, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -4.4 | 0.001 | 14/40 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -4.3 | 0.002 | 15/29 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -4.0 | 0.007 | 14/34 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -3.8 | 0.009 | 14/39 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -3.8 | 0.009 | 13/36 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.010 | 14/35 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.027 | 8/38 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.683×** | -3.5 | 0.028 | 11/40 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -3.4 | 0.036 | 14/34 (LS 180, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -3.3 | 0.048 | 8/25 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -3.2 | 0.064 | 12/32 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 8.94 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.45 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.264× (z -10.9) |
| [[HOP62 (line)]] | alt | 3.25 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0964× (z -8.9) |
| [[LoVo (line)]] | wt | 4.79 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -9.5) |
| [[LS 180 (line)]] | wt | 8.30 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0459× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 5.30 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0567× (z -10.1) |
| [[PANC-1 (line)]] | alt | 4.20 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2P5-1]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SPINT1-AS1]] | +0.63 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[HOTAIR]] | +0.58 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[P4HTM]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PRRG2]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HNF1A-AS1]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[NEIL1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[FCGRT]] | +0.54 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[UNC5CL]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ERBB2]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[C11orf52]] | +0.52 | +0.61 / +0.32 | both halves | 1e-04 |  |
| [[WBP11]] | +0.52 | +0.36 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTG1]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SH3BGRL3]] | -0.51 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[FLNB]] | -0.49 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ELOVL1]] | -0.49 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[RHOC]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RSU1]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[UCHL3]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ABCC10]] | -0.47 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[GTDC1]] | -0.46 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[LRRFIP1]] | -0.46 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[EHD2]] | -0.46 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[EXTL3]] | -0.45 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM-DT]] | B | EPCAM-DT activity raises GOLGA2P5's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without EPCAM-DT | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[ACTR3C]] | B | ACTR3C activity raises GOLGA2P5's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without ACTR3C | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[RDM1P5]] | B | RDM1P5 activity raises GOLGA2P5's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without RDM1P5 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[DSCAML1]] | B | DSCAML1 activity raises GOLGA2P5's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.44× lower at baseline in the lines without DSCAML1 | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[GOLGA2P5-1]] | C | GOLGA2P5-1 activity raises GOLGA2P5's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without GOLGA2P5-1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM-DT]] | B | GOLGA2P5 activity raises EPCAM-DT's level | lines that do not express GOLGA2P5 (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without GOLGA2P5 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000257489, GOLGA2P5-1, GRHL1; its own permutation p |
| [[GOLGA2P5-1]] | C | GOLGA2P5 activity raises GOLGA2P5-1's level | lines that do not express GOLGA2P5 (6) vs lines expressing it (44) | 3.13× lower at baseline in the lines without GOLGA2P5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000257489, GOLGA2P5-1, GRHL1; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.322). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, 29.4); signed map (38.4, -15.2). **Vector** length 47.9, 6.69% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | GOLGA2 pseudogene 5 |
| Locus type | pseudogene |
| Location | 12q23.1 — chr12:100,156,621-100,173,159 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp434M0331; previously GOLGA2L1, GOLGA2B |
| Matched by | ensembl_id |

UniProt [Q9HBQ8](https://www.uniprot.org/uniprotkb/Q9HBQ8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25315) · Entrez [55592](https://www.ncbi.nlm.nih.gov/gene/55592) · UniProt [Q9HBQ8](https://www.uniprot.org/uniprotkb/Q9HBQ8) · Ensembl [ENSG00000238105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238105)

## Data

Gene col 14169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14169); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14169]; `tensor/DDL_lfc|DDL_z.npy` [14169]; `embed/gene_vectors.npy` [14169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14169 or target_col == 14169). Every well: [[GOLGA2P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA2P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
