---
symbol: "SYT9-AS1"
type: "gene"
col: 14760
ensembl_id: "ENSG00000251364"
name: "SYT9 antisense RNA 1"
location: "11p15.4"
module: 10
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 21
direction_downstream: 15
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SYT9-AS1

*SYT9 antisense RNA 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +6.5, q 3e-08, up in 18 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.266× (z -12.0, q 2e-30, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL2]] (+0.64, fdr 7e-06), [[ARL14EP-DT]] (+0.61, fdr 7e-06), [[MRAS]] (+0.57, fdr 4e-05); moves opposite to [[RNF34]] (-0.49, fdr 1e-04), [[AP1M1]] (-0.47, fdr 1e-04), [[DGCR8]] (-0.45, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CHRNA7]] → it (grade B ⚠); 15 go from it, the strongest it → [[PLS3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.5 | 3e-08 | 18/38 (J82, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.1 | 4e-07 | 15/30 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +5.6 | 4e-06 | 16/33 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +5.5 | 4e-06 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.51×** | +5.3 | 2e-05 | 13/37 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +5.1 | 4e-05 | 13/38 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +4.5 | 5e-04 | 11/37 (KATO III, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +4.4 | 8e-04 | 11/37 (LoVo, SW480, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 8e-04 | 13/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.59×** | +4.2 | 0.002 | 10/33 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.002 | 12/36 (C32, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.003 | 5/37 (C32, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 12/38 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 9/37 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.008 | 10/35 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.021 | 9/37 (KATO III, A498, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.049 | 6/37 (BT-474, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.054 | 7/38 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.266×** | -12.0 | 2e-30 | 29/38 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -9.5 | 5e-19 | 25/36 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.452×** | -7.2 | 1e-10 | 18/23 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -7.1 | 2e-10 | 22/36 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.526×** | -5.5 | 4e-06 | 17/38 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.552×** | -5.4 | 7e-06 | 15/37 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.722×** | -4.2 | 0.002 | 10/36 (H4, HT-29, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -4.2 | 0.002 | 13/34 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.723×** | -4.2 | 0.002 | 15/36 (SNU-1, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -4.0 | 0.003 | 13/38 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.641×** | -3.9 | 0.005 | 14/21 (PANC-1, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.638×** | -3.9 | 0.005 | 16/35 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -3.5 | 0.020 | 8/28 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.681×** | -3.5 | 0.020 | 12/37 (H4, HS-578T, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.683×** | -3.4 | 0.021 | 12/37 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -3.0 | 0.086 | 12/37 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | **0.717×** | -3.0 | 0.086 | 2/33 (SK-MEL-2, HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.92 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0605× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 3 (1 ⚠) | — | [[Clofarabine (drug)]] 0.05 µM 0.0618× (z -10.0) |
| [[KATO III (line)]] | alt | 5.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0489× (z -10.9) |
| [[A-427 (line)]] | wt | 7.54 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 9.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 1.87 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 6.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 9.84 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.13× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 2.35 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0449× (z -8.5) |
| [[SW480 (line)]] | alt | 1.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0514× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL2]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.61 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MRAS]] | +0.57 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ATP6V1E2]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CLIC2]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LRIG2-DT]] | +0.56 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[KSR2]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ENPP7P4]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LRRC4B]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ANKS1B]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[LINC00466]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PACRG]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF34]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[AP1M1]] | -0.47 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[DGCR8]] | -0.45 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SRGAP2D]] | -0.45 | -0.50 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRNA7]] | B | CHRNA7 activity raises SYT9-AS1's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without CHRNA7 | 0.003 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises SYT9-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without MIR1915HG | 0.006 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[LRRC4B]] | B | LRRC4B activity raises SYT9-AS1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without LRRC4B | 0.011 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[ANKS1B]] | B | ANKS1B activity raises SYT9-AS1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without ANKS1B | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[FAM66C]] | B | FAM66C activity raises SYT9-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without FAM66C | 0.025 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[CXCL3]] | B | CXCL3 activity lowers SYT9-AS1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.91× higher at baseline in the lines without CXCL3 | 0.026 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[LINC00466]] | B | LINC00466 activity raises SYT9-AS1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without LINC00466 | 0.027 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises SYT9-AS1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ABCA17P | 0.032 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[KSR2]] | B | KSR2 activity raises SYT9-AS1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without KSR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SCN8A]] | B | SCN8A activity raises SYT9-AS1's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without SCN8A | 0.042 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[KATNAL2]] | B | KATNAL2 activity raises SYT9-AS1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without KATNAL2 | 0.043 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[ZMAT1]] | B | ZMAT1 activity raises SYT9-AS1's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without ZMAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3-AS1]] | B | SYT9-AS1 activity raises PLS3-AS1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without SYT9-AS1 | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CHRNA7]] | B | SYT9-AS1 activity raises CHRNA7's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.82× lower at baseline in the lines without SYT9-AS1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AJUBA-DT]] | B | SYT9-AS1 activity raises AJUBA-DT's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without SYT9-AS1 | 0.016 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C7orf31]] | B | SYT9-AS1 activity raises C7orf31's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without SYT9-AS1 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SGK2]] | B | SYT9-AS1 activity raises SGK2's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without SYT9-AS1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FTCDNL1]] | B | SYT9-AS1 activity raises FTCDNL1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without SYT9-AS1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RDM1P5]] | B | SYT9-AS1 activity raises RDM1P5's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without SYT9-AS1 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIR1915HG]] | B | SYT9-AS1 activity raises MIR1915HG's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without SYT9-AS1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LRRIQ3]] | B | SYT9-AS1 activity raises LRRIQ3's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without SYT9-AS1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATF7IP2]] | B | SYT9-AS1 activity raises ATF7IP2's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.24× lower at baseline in the lines without SYT9-AS1 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPLD1]] | B | SYT9-AS1 activity raises GPLD1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without SYT9-AS1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NUDT7]] | B | SYT9-AS1 activity raises NUDT7's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without SYT9-AS1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.1, 32.6); signed map (37.0, -1.3). **Vector** length 52.3, 7.96% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +5.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +4.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.2 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.2 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.1 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | SYT9 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.4 — chr11:7,418,826-7,513,665 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56173) · Entrez [100506258](https://www.ncbi.nlm.nih.gov/gene/100506258) · Ensembl [ENSG00000251364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251364)

## Data

Gene col 14760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14760); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14760]; `tensor/DDL_lfc|DDL_z.npy` [14760]; `embed/gene_vectors.npy` [14760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14760 or target_col == 14760). Every well: [[SYT9-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT9-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
