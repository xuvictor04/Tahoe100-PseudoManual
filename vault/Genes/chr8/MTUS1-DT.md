---
symbol: "MTUS1-DT"
type: "gene"
col: 14849
ensembl_id: "ENSG00000253944"
name: "MTUS1 divergent transcript"
location: "8p22"
module: 23
arm: "+"
pooled_cpm: 3.98
n_lines_expressing: 33
n_dd_up: 44
n_dd_down: 6
n_dd_up_clean: 37
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 21
direction_downstream: 40
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MTUS1-DT

*MTUS1 divergent transcript* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.50× (z +11.9, q 9e-30, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +10.7, q 3e-24, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Abemaciclib (drug)]] 0.5 µM: 0.450× (z -4.9, q 5e-04, down in 10 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (SW1417 0.0516×; ⚠ cell-cycle shift, explains ~41% of this change); [[Pemetrexed (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0693×); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (A549 0.0547×); [[Flutamide (drug)]] 0.5 µM in 1 line (LS 180 0.0644×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFAP2A-AS1]] (+0.68, fdr 3e-05), [[CHODL]] (+0.68, fdr 3e-05), [[NR1D2]] (+0.66, fdr 1e-05); moves opposite to [[ATG16L1]] (-0.68, fdr 1e-05), [[RNGTT]] (-0.64, fdr 2e-05), [[PLEK2]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[VNN1]] → it (grade B ⚠); 40 go from it, the strongest it → [[RNF103]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.50×** | +11.9 | 9e-30 | 8/10 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +10.7 | 3e-24 | 20/26 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +10.5 | 2e-23 | 7/9 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +9.5 | 4e-19 | 11/17 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +9.2 | 6e-18 | 16/24 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +6.9 | 5e-10 | 15/29 (A-172, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +6.5 | 7e-09 | 13/23 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.11×** | +6.1 | 6e-08 | 17/28 (SW48, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.97×** | +6.1 | 7e-08 | 20/29 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +6.0 | 1e-07 | 9/20 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.67×** | +6.0 | 1e-07 | 17/29 (SW48, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.66×** | +6.0 | 1e-07 | 15/29 (AsPC-1, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.97×** | +5.8 | 4e-07 | 17/29 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.95×** | +5.7 | 6e-07 | 19/29 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.94×** | +5.7 | 6e-07 | 16/29 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 1e-06 | 16/29 (A549, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.70×** | +5.5 | 1e-06 | 13/29 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.3 | 3e-06 | 12/29 (KATO III, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +5.2 | 7e-06 | 15/26 (NCI-H2030, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (SW1417 0.0516×; ⚠ cell-cycle shift, explains ~41% of this change); [[Pemetrexed (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0693×); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (A549 0.0547×); [[Flutamide (drug)]] 0.5 µM in 1 line (LS 180 0.0644×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.450×** | -4.9 | 5e-04 | 10/30 (SK-MEL-2, SW48, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.574×** | -4.8 | 5e-04 | 14/30 (NCI-H2347, SW48, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -4.5 | 0.002 | 13/27 (SW48, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -4.2 | 0.003 | 15/29 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.664×** | -3.5 | 0.046 | 12/29 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.672×** | -3.4 | 0.057 | 9/29 (SW48, HepG2/C3A, …) | rises with dose |  |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.680× | -3.1 | 0.14 | 5/29 (HCT15, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.479× | -3.0 | 0.19 | 6/25 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 4.10 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +9.4) | [[Flutamide (drug)]] 0.5 µM 0.0644× (z -8.5) |
| [[SW48 (line)]] | wt | 36.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -8.9) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A549 (line)]] | wt | 6.29 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0547× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 4.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.01× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 6.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0693× (z -9.1) |
| [[KATO III (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 7.12 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0516× (z -12.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2A-AS1]] | +0.68 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[CHODL]] | +0.68 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[NR1D2]] | +0.66 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[STX19]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.65 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[KLRK1-AS1]] | +0.64 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[UNC79]] | +0.63 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[AHI1-DT]] | +0.63 | +0.59 / +0.33 | both halves | 1e-04 | same gene group |
| [[KANSL1L]] | +0.62 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[UFL1-AS1]] | +0.62 | +0.61 / +0.27 | both halves | 3e-04 |  |
| [[COL28A1]] | +0.61 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[DNAI4]] | +0.61 | +0.60 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG16L1]] | -0.68 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PLEK2]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[KIF21B]] | -0.60 | -0.63 / -0.25 | both halves | 4e-04 |  |
| [[S100A16]] | -0.60 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[DGKD]] | -0.60 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[LYPD3]] | -0.59 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[FLNB]] | -0.58 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[PAQR5]] | -0.57 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[PLEKHG5]] | -0.57 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[PBX4]] | -0.56 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[HPCAL1]] | -0.56 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 11, C 10. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VNN1]] | B | VNN1 activity raises MTUS1-DT's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without VNN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[STEAP4]] | B | STEAP4 activity raises MTUS1-DT's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.73× lower at baseline in the lines without STEAP4 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[MAOB]] | B | MAOB activity raises MTUS1-DT's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without MAOB | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[PLEK2]] | B | PLEK2 activity raises MTUS1-DT's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.98× lower at baseline in the lines without PLEK2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[KIF21B]] | B | KIF21B activity raises MTUS1-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without KIF21B | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MTUS1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HAVCR1]] | B | HAVCR1 activity raises MTUS1-DT's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.17× lower at baseline in the lines without HAVCR1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[HDAC6]] | B | HDAC6 activity raises MTUS1-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGL1]] | B | FGL1 activity raises MTUS1-DT's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.19× lower at baseline in the lines without FGL1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[RASGEF1B]] | B | RASGEF1B activity raises MTUS1-DT's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without RASGEF1B | 0.074 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[LINC01836]] | B | LINC01836 activity raises MTUS1-DT's level | lines that do not express LINC01836 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without LINC01836 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANXA3, SLC9A2, SHROOM3 |
| [[MTUS1]] | C | MTUS1 activity raises MTUS1-DT's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.46× lower at baseline in the lines without MTUS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 27, C 13. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103]] | B | MTUS1-DT activity raises RNF103's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without MTUS1-DT | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[RASGEF1B]] | B | MTUS1-DT activity raises RASGEF1B's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without MTUS1-DT | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[MARVELD2]] | B | MTUS1-DT activity raises MARVELD2's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without MTUS1-DT | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[HLA-V-1]] | B | MTUS1-DT activity raises HLA-V-1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without MTUS1-DT | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[STAP2]] | B | MTUS1-DT activity raises STAP2's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.33× lower at baseline in the lines without MTUS1-DT | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | [[ENSG00000253671]], MTUS1-DT activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000253671, MTUS1-DT (17) vs lines expressing them (31) | the lines without ENSG00000253671, MTUS1-DT: 1.14× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: MTUS1, ELF3-AS1, ELF3; co-absent genes |
| cells under [[Trifluridine (drug)]] 5 µM | B | [[ENSG00000253671]], MTUS1-DT activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express ENSG00000253671, MTUS1-DT (17) vs lines expressing them (31) | the lines without ENSG00000253671, MTUS1-DT: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: MTUS1, ELF3-AS1, ELF3; co-absent genes |
| [[LINC01090]] | B | MTUS1-DT activity raises LINC01090's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without MTUS1-DT | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[LYPD3]] | B | MTUS1-DT activity raises LYPD3's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.73× lower at baseline in the lines without MTUS1-DT | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[MUC20]] | B | MTUS1-DT activity raises MUC20's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.53× lower at baseline in the lines without MTUS1-DT | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[VNN1]] | B | MTUS1-DT activity raises VNN1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without MTUS1-DT | 0.021 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[ATP9A]] | B | MTUS1-DT activity raises ATP9A's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without MTUS1-DT | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (17.6, 7.7); signed map (29.2, -4.7). **Vector** length 67.5, 15.6% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +6.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -2.9 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.8 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -2.3 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.2 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MTUS1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p22 — chr8:17,801,345-17,861,069 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55525) · Entrez [101930275](https://www.ncbi.nlm.nih.gov/gene/101930275) · Ensembl [ENSG00000253944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253944)

## Data

Gene col 14849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14849); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14849]; `tensor/DDL_lfc|DDL_z.npy` [14849]; `embed/gene_vectors.npy` [14849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14849 or target_col == 14849). Every well: [[MTUS1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTUS1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
