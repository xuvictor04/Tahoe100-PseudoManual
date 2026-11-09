---
symbol: "SLAIN1"
type: "gene"
col: 6343
ensembl_id: "ENSG00000139737"
name: "SLAIN family member 1"
location: "13q22.3"
module: 9
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 15
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SLAIN1

*SLAIN family member 1* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.69× (z +19.3, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.583× (z -7.4, q 7e-11, down in 13 of 26 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUSD4]] (+0.65, fdr 7e-06), [[NELL2]] (+0.60, fdr 2e-05), [[CA8]] (+0.56, fdr 3e-05); moves opposite to [[NMNAT1]] (-0.52, fdr 2e-04), [[RECQL5]] (-0.52, fdr 3e-04), [[VPS39]] (-0.51, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PREX1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SGSM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.69×** | +19.3 | 0e+00 | 23/24 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.81×** | +18.4 | 0e+00 | 22/25 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.41×** | +16.9 | 0e+00 | 20/25 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.17×** | +15.9 | 0e+00 | 20/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.08×** | +15.5 | 0e+00 | 19/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +14.7 | 0e+00 | 19/25 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.00×** | +9.6 | 9e-20 | 14/22 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.62×** | +9.2 | 2e-18 | 17/24 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 2e-11 | 11/22 (LOX-IMVI, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.0 | 1e-07 | 2/7 (CFPAC-1, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.7 | 6e-07 | 10/24 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +5.3 | 4e-06 | 7/23 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +5.3 | 6e-06 | 2/14 (SHP-77, A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +4.7 | 1e-04 | 6/24 (LoVo, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 5/25 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.008 | 3/22 (NCI-H2030, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.010 | 4/23 (KATO III, LoVo, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.013 | 1/25 (J82) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -7.4 | 7e-11 | 13/26 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -4.4 | 0.003 | 14/24 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -4.3 | 0.003 | 11/24 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -4.2 | 0.004 | 10/25 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.1 | 0.005 | 5/26 (Panc 03.27, CHP-212, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.824×** | -3.8 | 0.016 | 4/26 (SHP-77, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.016 | 0/22 | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.764×** | -3.7 | 0.016 | 9/24 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.018 | 9/25 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.774×** | -3.5 | 0.024 | 10/22 (BT-474, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.622×** | -3.4 | 0.031 | 7/23 (SK-MEL-2, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Rucaparib (phosphate) (drug)]] 0.05 µM |  | **0.765×** | -3.4 | 0.031 | 5/25 (C32, CHP-212, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -3.2 | 0.060 | 6/25 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.794×** | -3.2 | 0.060 | 6/24 (HCT15, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.6 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.50× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0964× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.42× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.03× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.847 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.667 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUSD4]] | +0.65 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[NELL2]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CA8]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[NCAM1]] | +0.55 | +0.21 / +0.51 | both halves | 7e-04 |  |
| [[SPTB]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TMEM170B]] | +0.53 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[ATP8A1]] | +0.53 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[UGT8]] | +0.53 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[ELOVL4]] | +0.53 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FAM102B]] | +0.53 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[TSPAN12]] | +0.52 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT1]] | -0.52 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[RECQL5]] | -0.52 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[VPS39]] | -0.51 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ATXN1L]] | -0.50 | -0.15 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF431]] | -0.49 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[ACAD9]] | -0.49 | -0.19 / -0.50 | ⚠ not reproduced | 9e-04 |  |
| [[UQCC1]] | -0.49 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[COMMD1]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[GPALPP1]] | -0.47 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[PAAF1]] | -0.46 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[TMEM199]] | -0.46 | -0.14 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[EXOC7]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ERVK13-1]] | -0.46 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[IREB2]] | -0.45 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[MEF2B]] | -0.45 | -0.28 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PREX1]] | B | PREX1 activity raises SLAIN1's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without PREX1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |
| [[SORL1]] | B | SORL1 activity raises SLAIN1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without SORL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MPP7]] | B | MPP7 activity raises SLAIN1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without MPP7 | 0.027 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[POU3F2]] | B | POU3F2 activity raises SLAIN1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without POU3F2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[KSR2]] | B | KSR2 activity raises SLAIN1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without KSR2 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SLC4A8]] | B | SLC4A8 activity raises SLAIN1's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 2.38× lower at baseline in the lines without SLC4A8 | 0.058 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[FGF9]] | B | FGF9 activity raises SLAIN1's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.71× lower at baseline in the lines without FGF9 | 0.059 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[KLHL32]] | B | KLHL32 activity raises SLAIN1's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without KLHL32 | 0.065 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[TSPAN12]] | B | TSPAN12 activity raises SLAIN1's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without TSPAN12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[ATP8A1]] | B | ATP8A1 activity raises SLAIN1's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without ATP8A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[GABRA2]] | B | GABRA2 activity raises SLAIN1's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without GABRA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[SLC27A2]] | B | SLC27A2 activity raises SLAIN1's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SLC27A2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSM1]] | B | SLAIN1 activity raises SGSM1's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without SLAIN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[STOX2]] | B | SLAIN1 activity raises STOX2's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without SLAIN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[CXADR]] | B | SLAIN1 activity raises CXADR's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without SLAIN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[AMOT]] | B | SLAIN1 activity raises AMOT's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without SLAIN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[COL4A4]] | C | SLAIN1 activity raises COL4A4's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without SLAIN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[COL4A3]] | C | SLAIN1 activity raises COL4A3's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without SLAIN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[SPTB]] | C | SLAIN1 activity raises SPTB's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without SLAIN1 | 0.073 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[SH3GL2]] | C | SLAIN1 activity raises SH3GL2's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without SLAIN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 34.6); signed map (43.0, 36.6). **Vector** length 38.9, 6.17% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +19.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +16.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +9.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | SLAIN family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:77,697,687-77,764,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30046; previously C13orf32 |
| Gene groups (HGNC) | SLAIN family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND83](https://www.uniprot.org/uniprotkb/Q8ND83) (SLAIN motif-containing protein 1):

> Microtubule plus-end tracking protein that might be involved in the regulation of cytoplasmic microtubule dynamics, microtubule organization and microtubule elongation.

**Summary**, from NCBI Gene [122060](https://www.ncbi.nlm.nih.gov/gene/122060):

> Predicted to be involved in cytoplasmic microtubule organization; microtubule nucleation; and positive regulation of microtubule polymerization. Predicted to be located in microtubule plus-end. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26387) · Entrez [122060](https://www.ncbi.nlm.nih.gov/gene/122060) · UniProt [Q8ND83](https://www.uniprot.org/uniprotkb/Q8ND83) · Ensembl [ENSG00000139737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139737)

## Data

Gene col 6343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6343); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6343]; `tensor/DDL_lfc|DDL_z.npy` [6343]; `embed/gene_vectors.npy` [6343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6343 or target_col == 6343). Every well: [[SLAIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLAIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
