---
symbol: "CYSTM1"
type: "gene"
col: 4175
ensembl_id: "ENSG00000120306"
name: "cysteine rich transmembrane module containing 1"
location: "5q31.3"
module: 141
arm: "+"
pooled_cpm: 107.57
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 28
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# CYSTM1

*cysteine rich transmembrane module containing 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.57× (z +8.1, q 3e-13, up in 32 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.40× (z +6.0, q 4e-07, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.610× (z -4.7, q 0.002, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAIAP2L1]] (+0.62, fdr 1e-05), [[RDH13]] (+0.55, fdr 3e-05), [[FA2H]] (+0.54, fdr 3e-05); moves opposite to [[CDC23]] (-0.48, fdr 3e-05), [[THBS4]] (-0.47, fdr 1e-04), [[ALKBH3]] (-0.46, fdr 6e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[CEACAM5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.1 | 3e-13 | 32/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.0 | 4e-07 | 30/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.38×** | +5.8 | 1e-06 | 25/47 (SNU-1, RPMI-7951, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 2e-06 | 24/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 7e-06 | 23/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.4 | 1e-03 | 24/46 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.3 | 0.001 | 14/46 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +4.3 | 0.001 | 24/46 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.005 | 23/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.8 | 0.007 | 21/46 (HCT15, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.5 | 0.023 | 18/46 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.035 | 19/46 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.4 | 0.035 | 19/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.21×** | +3.3 | 0.045 | 17/39 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.070 | 16/46 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.077 | 11/46 (KATO III, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.610×** | -4.7 | 0.002 | 27/45 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.776×** | -4.4 | 0.003 | 22/48 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.853× | -4.0 | 0.012 | 17/46 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.791×** | -3.9 | 0.012 | 21/46 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.875× | -3.4 | 0.060 | 20/46 (NCI-H1573, A549, …) | top dose only | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.060 | 17/46 (SW 1088, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.060 | 18/46 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.836× | -3.2 | 0.080 | 15/46 (KATO III, Hs 766T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.080 | 17/46 (SW48, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.0 | 0.15 | 20/46 (SW1417, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 385 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 46.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.518× (z -9.4) |
| [[PANC-1 (line)]] | alt | 96.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.0) | — |
| [[A-427 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.434× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 252 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 298 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 314 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 58.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | — |
| [[A-172 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 166 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 81.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP2L1]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[RDH13]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[FA2H]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[GP6]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CD55]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[EZR]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[NR4A1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CHKA]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[PLK3]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KRT20]] | +0.50 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[ZBTB7C]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MIR23AHG]] | +0.50 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC23]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[THBS4]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ALKBH3]] | -0.46 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[FASTKD3]] | -0.46 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[SAFB]] | -0.46 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[NUP37]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MIX23]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[MOB4]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RBM17]] | -0.45 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ANGEL2]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[TACO1]] | -0.44 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[MRPL9]] | -0.44 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 26, C 2. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM5]] | B | CEACAM5 activity raises CYSTM1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without CEACAM5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[MUC3A]] | B | MUC3A activity raises CYSTM1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without MUC3A | 0.008 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[JUP]] | B | JUP activity raises CYSTM1's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without JUP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[FAM3D]] | B | FAM3D activity raises CYSTM1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.50× lower at baseline in the lines without FAM3D | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[KIAA0040]] | B | KIAA0040 activity raises CYSTM1's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without KIAA0040 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[SULT2B1]] | B | SULT2B1 activity raises CYSTM1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without SULT2B1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[AREG]] | B | AREG activity raises CYSTM1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without AREG | 0.026 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[CEACAM6]] | B | CEACAM6 activity raises CYSTM1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without CEACAM6 | 0.027 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[ST14]] | B | ST14 activity raises CYSTM1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without ST14 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[SLC52A3]] | B | SLC52A3 activity raises CYSTM1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without SLC52A3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises CYSTM1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without TMPRSS4 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises CYSTM1's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without ZDHHC11B | 0.043 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.1, 56.2); signed map (-0.6, 37.5). **Vector** length 135, 40.5% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +5.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.0 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.8 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.7 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +1.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.5 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich transmembrane module containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,175,156-140,282,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ORF1-FL49; previously C5orf32 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q9H1C7](https://www.uniprot.org/uniprotkb/Q9H1C7) carries no function annotation.

**Summary**, from NCBI Gene [84418](https://www.ncbi.nlm.nih.gov/gene/84418):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30239) · Entrez [84418](https://www.ncbi.nlm.nih.gov/gene/84418) · UniProt [Q9H1C7](https://www.uniprot.org/uniprotkb/Q9H1C7) · Ensembl [ENSG00000120306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120306)

## Data

Gene col 4175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4175); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4175]; `tensor/DDL_lfc|DDL_z.npy` [4175]; `embed/gene_vectors.npy` [4175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4175 or target_col == 4175). Every well: [[CYSTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYSTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
