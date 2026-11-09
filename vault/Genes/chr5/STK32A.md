---
symbol: "STK32A"
type: "gene"
col: 9794
ensembl_id: "ENSG00000169302"
name: "serine/threonine kinase 32A"
location: "5q32"
module: 94
arm: "+"
pooled_cpm: 8.97
n_lines_expressing: 27
n_dd_up: 58
n_dd_down: 9
n_dd_up_clean: 53
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# STK32A

*serine/threonine kinase 32A* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 58 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 4.50× (z +22.7, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.448× (z -8.6, q 4e-15, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP15]] (+0.75, fdr 7e-06), [[PCLO]] (+0.68, fdr 1e-05), [[NGFR]] (+0.67, fdr 1e-05); moves opposite to [[SNTB2]] (-0.54, fdr 2e-05), [[ANKMY1]] (-0.53, fdr 2e-05), [[SLFNL1-AS1]] (-0.49, fdr 4e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RRAGD]] → it (grade B ⚠); 12 go from it, the strongest it → [[SH3TC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 58 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **4.50×** | +22.7 | 0e+00 | 23/24 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **6.90×** | +20.6 | 0e+00 | 25/25 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **4.46×** | +15.9 | 0e+00 | 23/24 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **3.94×** | +14.6 | 0e+00 | 24/24 (A498, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.58×** | +14.3 | 5e-44 | 20/25 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.71×** | +10.6 | 2e-24 | 20/24 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +9.3 | 9e-19 | 18/25 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +7.4 | 1e-11 | 14/24 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.61×** | +7.1 | 6e-11 | 19/25 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.95×** | +7.1 | 6e-11 | 19/25 (SW 900, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.7 | 5e-07 | 2/13 (NCI-H1792, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +5.6 | 1e-06 | 8/25 (C32, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.5 | 1e-06 | 2/19 (HEC-1-A, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.43×** | +5.3 | 4e-06 | 13/25 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.2 | 7e-06 | 9/22 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +5.0 | 2e-05 | 8/23 (C32, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +4.9 | 3e-05 | 16/25 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.448×** | -8.6 | 4e-15 | 21/25 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.502×** | -7.4 | 4e-11 | 21/25 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.550×** | -6.4 | 2e-08 | 13/23 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.566×** | -6.1 | 1e-07 | 17/23 (Hs 766T, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.692×** | -5.6 | 2e-06 | 15/25 (NCI-H2347, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.696×** | -3.9 | 0.009 | 11/25 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Allantoin (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.040 | 5/25 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.4 | 0.040 | 3/25 (A-172, CHP-212, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -3.4 | 0.040 | 5/23 (SW1417, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.736×** | -3.3 | 0.052 | 17/22 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Simotinib (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.10 | 3/22 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.37 | 3 | 4 (3 ⚠) | [[Osimertinib (mesylate) (drug)]] 5 µM 5.97× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.4) |
| [[SW480 (line)]] | alt | 8.47 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.3) | [[Digitoxin (drug)]] 0.05 µM 0.121× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 87.4 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -17.3) |
| [[J82 (line)]] | alt | 13.6 | 3 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 4.65× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0681× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 25.9 | 1 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.75× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0805× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -9.1) |
| [[SHP-77 (line)]] | alt | 17.2 | 3 | 1 | [[Selinexor (drug)]] 5 µM 6.45× (z +12.0) | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -9.6) |
| [[A-172 (line)]] | wt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 3 | 0 | [[Selinexor (drug)]] 5 µM 12.0× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 3 | 0 | [[Selinexor (drug)]] 5 µM 5.60× (z +11.5) | — |
| [[LoVo (line)]] | wt | 6.38 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0543× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 10.8 | 2 | 0 | [[Selinexor (drug)]] 5 µM 7.26× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 2 | 0 | [[Selinexor (drug)]] 5 µM 11.0× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0618× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 5.71 | 1 | 0 | [[Selinexor (drug)]] 0.05 µM 17.8× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 9.15 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0608× (z -10.4) |
| [[SW1417 (line)]] | alt | 3.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +11.2) | — |
| [[A-427 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP15]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[PCLO]] | +0.68 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[NGFR]] | +0.67 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[RNF150]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[SLC44A2]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SULT1C2]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GNG2]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RRAGD]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PREPL]] | +0.58 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[TATDN3]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[CAPN5]] | +0.57 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[TPD52L1]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ANKMY1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SLFNL1-AS1]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[NSD2]] | -0.48 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PGP]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[C2CD3]] | -0.48 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[NPLOC4]] | -0.48 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[SCHIP1]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HNRNPAB]] | -0.46 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[MAPKAPK2]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GPAA1]] | -0.46 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[MFSD14CP-1]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | RRAGD activity raises STK32A's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without RRAGD | 0.013 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[TPD52L1]] | B | TPD52L1 activity raises STK32A's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without TPD52L1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[SH3TC1]] | B | SH3TC1 activity raises STK32A's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without SH3TC1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[ENTREP1]] | B | ENTREP1 activity raises STK32A's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without ENTREP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[TNFRSF14]] | B | TNFRSF14 activity raises STK32A's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without TNFRSF14 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[STK33]] | B | STK33 activity raises STK32A's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without STK33 | 0.082 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[ICA1]] | B | ICA1 activity raises STK32A's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ICA1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[GPNMB]] | C | GPNMB activity raises STK32A's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without GPNMB | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[SULT1C2]] | C | SULT1C2 activity raises STK32A's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without SULT1C2 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139; co-absent with the target |
| [[GNG2]] | C | GNG2 activity raises STK32A's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without GNG2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3TC1]] | B | STK32A activity raises SH3TC1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without STK32A | 0.012 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[NEURL3]] | B | STK32A activity raises NEURL3's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without STK32A | 0.013 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[ATP6V0D2]] | B | STK32A activity raises ATP6V0D2's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without STK32A | 0.019 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[SLFNL1-AS1]] | B | STK32A activity lowers SLFNL1-AS1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.76× higher at baseline in the lines without STK32A | 0.029 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[ENTREP1]] | B | STK32A activity raises ENTREP1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.030 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[TPD52L1]] | B | STK32A activity raises TPD52L1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without STK32A | 0.030 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[ARL4D]] | B | STK32A activity raises ARL4D's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.043 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[DIAPH2-AS1]] | B | STK32A activity raises DIAPH2-AS1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.44× lower at baseline in the lines without STK32A | 0.044 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[STK33]] | B | STK32A activity raises STK33's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without STK32A | 0.059 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[PRUNE2]] | C | STK32A activity raises PRUNE2's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without STK32A | 0.011 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1; co-absent with the target |
| [[SULT1C2]] | C | STK32A activity raises SULT1C2's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without STK32A | 0.067 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1; co-absent with the target |
| [[FRG1FP]] | C | STK32A activity raises FRG1FP's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.088 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.0, 24.8); signed map (14.2, -16.1). **Vector** length 83.1, 21.9% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.6 | +22.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.4 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +14.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.6 | +20.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +10.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.5 | +14.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -8.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.5 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.2 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.2 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -5.6 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 32A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:147,234,963-147,387,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22688, YANK1 |
| Gene groups (HGNC) | Serine/threonine kinase 32 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU08](https://www.uniprot.org/uniprotkb/Q8WU08) (Serine/threonine-protein kinase 32A):

> Probable serine/threonine kinase with currently unidentified substrates. In the inner ear, functions as a planar cell polarity (PCP) factor acting antagonistically to EMX2. It regulates the orientation of stereociliary bundles in hair cells by interacting with the PCP signaling pathway in opposition to EMX2. Additionally, it may play a role in controlling the apical localization of the GPR156 receptor in inner ear hair cells.

**Summary**, from NCBI Gene [202374](https://www.ncbi.nlm.nih.gov/gene/202374):

> Predicted to enable protein serine/threonine kinase activity. Predicted to be involved in intracellular signal transduction. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28317) · Entrez [202374](https://www.ncbi.nlm.nih.gov/gene/202374) · UniProt [Q8WU08](https://www.uniprot.org/uniprotkb/Q8WU08) · Ensembl [ENSG00000169302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169302)

## Data

Gene col 9794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9794); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9794]; `tensor/DDL_lfc|DDL_z.npy` [9794]; `embed/gene_vectors.npy` [9794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9794 or target_col == 9794). Every well: [[STK32A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK32A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
