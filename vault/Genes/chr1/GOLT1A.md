---
symbol: "GOLT1A"
type: "gene"
col: 10504
ensembl_id: "ENSG00000174567"
name: "golgi transport 1A"
location: "1q32.1"
module: 158
arm: "+"
pooled_cpm: 7.87
n_lines_expressing: 26
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 14
direction_downstream: 37
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# GOLT1A

*golgi transport 1A* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.68× (z +24.4, q 0e+00, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.615× (z -5.8, q 3e-06, down in 17 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTAFR]] (+0.64, fdr 1e-05), [[MYL12A]] (+0.61, fdr 2e-05), [[PFN1]] (+0.61, fdr 5e-05); moves opposite to [[SUPV3L1]] (-0.57, fdr 2e-05), [[TMEM183A]] (-0.55, fdr 1e-05), [[PHB2]] (-0.53, fdr 3e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CCDC120]] → it (grade B ⚠); 37 go from it, the strongest it → [[CCDC120]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.68×** | +24.4 | 0e+00 | 15/23 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.07×** | +12.6 | 1e-33 | 18/23 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +9.3 | 2e-18 | 9/24 (LoVo, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.2 | 4e-18 | 2/14 (SW1417, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +9.1 | 7e-18 | 18/24 (SW1417, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.7 | 2e-16 | 5/22 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +7.3 | 2e-11 | 18/24 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +7.2 | 5e-11 | 15/24 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.6 | 2e-09 | 18/23 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +6.3 | 1e-08 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +6.1 | 4e-08 | 13/24 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.60×** | +5.3 | 6e-06 | 2/19 (LoVo, NCI-H1573) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.6 | 2e-04 | 15/24 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 7e-04 | 1/21 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +3.7 | 0.007 | 7/24 (SW1417, KATO III, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.026 | 7/23 (A549, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.038 | 8/24 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.068 | 2/22 (NCI-H2030, HepG2/C3A) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.070 | 2/24 (COLO 205, AsPC-1) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.615×** | -5.8 | 3e-06 | 17/24 (HepG2/C3A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.715×** | -5.2 | 5e-05 | 12/24 (HepG2/C3A, SW 900, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.691×** | -5.1 | 5e-05 | 14/24 (NCI-H2030, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.643×** | -4.9 | 1e-04 | 12/24 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.690×** | -4.9 | 1e-04 | 11/24 (HepG2/C3A, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.689×** | -4.8 | 2e-04 | 14/24 (NCI-H2030, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.650×** | -4.4 | 8e-04 | 10/24 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -4.4 | 9e-04 | 14/24 (SW480, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.015 | 17/24 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -3.2 | 0.062 | 7/23 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.739×** | -3.2 | 0.062 | 10/23 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.747× | -3.1 | 0.10 | 12/24 (HepG2/C3A, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 18.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 13.1× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 10.7× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.0 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0998× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.42 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0841× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 8.62 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.139× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 4.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0236× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -8.6) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 7.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.175× (z -9.5) |
| [[A-172 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.866 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTAFR]] | +0.64 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[MYL12A]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PFN1]] | +0.61 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[PRKG2-AS1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EIF5A2]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | +0.60 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SLC45A3]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[IER5]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[EPHA2]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPV3L1]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[TMEM183A]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[PHB2]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TSN]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ALDH2]] | -0.50 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[GANC]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[MFSD14A]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GLB1]] | -0.49 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[PMS2]] | -0.49 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PLBD1]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GHITM]] | -0.48 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[CLASP1]] | -0.47 | -0.49 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | CCDC120 activity raises GOLT1A's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.21× lower at baseline in the lines without CCDC120 | 0.020 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[MAP2K2]] | B | MAP2K2 activity raises GOLT1A's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CD22]] | B | CD22 activity raises GOLT1A's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without CD22 | 0.074 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises GOLT1A's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.63× lower at baseline in the lines without PHLDA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[PRAG1]] | B | PRAG1 activity raises GOLT1A's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without PRAG1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SH2D3A]] | C | SH2D3A activity raises GOLT1A's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 4.81× lower at baseline in the lines without SH2D3A | 1e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[PTAFR]] | C | PTAFR activity raises GOLT1A's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 4.07× lower at baseline in the lines without PTAFR | 8e-04 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent; co-absent with the target |
| [[PRKG2-AS1]] | C | PRKG2-AS1 activity raises GOLT1A's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without PRKG2-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |
| [[AREG]] | C | AREG activity raises GOLT1A's level | lines that do not express AREG (26) vs lines expressing it (24) | 3.75× lower at baseline in the lines without AREG | 0.003 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3; co-absent with the target |
| [[VAV1]] | C | VAV1 activity raises GOLT1A's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without VAV1 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises GOLT1A's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without SPNS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises GOLT1A's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without TINAGL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 26, C 11. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | GOLT1A activity raises CCDC120's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without GOLT1A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[BAIAP2L1]] | B | GOLT1A activity raises BAIAP2L1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without GOLT1A | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[MYO15B]] | B | GOLT1A activity raises MYO15B's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without GOLT1A | 0.008 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[SDC4]] | B | GOLT1A activity raises SDC4's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without GOLT1A | 0.013 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[PMEPA1]] | B | GOLT1A activity raises PMEPA1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without GOLT1A | 0.015 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[ANGEL2]] | B | GOLT1A activity lowers ANGEL2's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.28× higher at baseline in the lines without GOLT1A | 0.017 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[S100A11]] | B | GOLT1A activity raises S100A11's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without GOLT1A | 0.021 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[GALE]] | B | GOLT1A activity raises GALE's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without GOLT1A | 0.041 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[PRAG1]] | B | GOLT1A activity raises PRAG1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without GOLT1A | 0.049 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[ALDH2]] | B | GOLT1A activity raises ALDH2's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without GOLT1A | 0.053 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[SCAT1]] | B | GOLT1A activity raises SCAT1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without GOLT1A | 0.055 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| cells under [[Torkinib (drug)]] 5 µM | B | GOLT1A activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express GOLT1A (24) vs lines expressing it (24) | the lines without GOLT1A: 0.80× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.7, 3.1); signed map (8.9, 41.0). **Vector** length 66.0, 16.2% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +24.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +12.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | golgi transport 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,198,163-204,213,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42654, CGI-141, YMR292W, GOT1, MGC62027 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZVE7](https://www.uniprot.org/uniprotkb/Q6ZVE7) (Vesicle transport protein GOT1A):

> May be involved in fusion of ER-derived transport vesicles with the Golgi complex.

**Summary**, from NCBI Gene [127845](https://www.ncbi.nlm.nih.gov/gene/127845):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Located in Golgi apparatus; endoplasmic reticulum; and nuclear envelope. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24766) · Entrez [127845](https://www.ncbi.nlm.nih.gov/gene/127845) · UniProt [Q6ZVE7](https://www.uniprot.org/uniprotkb/Q6ZVE7) · Ensembl [ENSG00000174567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174567)

## Data

Gene col 10504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10504); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10504]; `tensor/DDL_lfc|DDL_z.npy` [10504]; `embed/gene_vectors.npy` [10504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10504 or target_col == 10504). Every well: [[GOLT1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLT1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
