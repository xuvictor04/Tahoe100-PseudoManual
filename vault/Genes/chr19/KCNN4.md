---
symbol: "KCNN4"
type: "gene"
col: 2497
ensembl_id: "ENSG00000104783"
name: "potassium calcium-activated channel subfamily N member 4"
location: "19q13.31"
module: 84
arm: "+"
pooled_cpm: 19.06
n_lines_expressing: 38
n_dd_up: 3
n_dd_down: 61
n_dd_up_clean: 2
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# KCNN4

*potassium calcium-activated channel subfamily N member 4* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.63× (z +6.8, q 8e-09, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 61 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.242× (z -27.6, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.83, fdr 7e-06), [[RASA3]] (+0.74, fdr 7e-06), [[RAC2]] (+0.74, fdr 7e-06).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[WWTR1]] → it (grade B ⚠); 9 go from it, the strongest it → [[PXN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.63×** | +6.8 | 8e-09 | 21/34 (HOP62, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.61×** | +6.3 | 9e-08 | 21/33 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +3.6 | 0.068 | 11/35 (BT-474, KATO III, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.3 | 0.12 | 10/36 (BT-474, SW480, …) | all doses, flat |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.19 | 3/34 (LS 180, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.19 | 5/32 (A549, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 61 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.242×** | -27.6 | 0e+00 | 33/34 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.356×** | -20.1 | 0e+00 | 27/36 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -16.6 | 0e+00 | 31/36 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.306×** | -15.7 | 0e+00 | 27/34 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.340×** | -14.3 | 4e-44 | 31/36 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -13.8 | 2e-41 | 29/36 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.398×** | -12.7 | 7e-35 | 30/34 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.395×** | -12.3 | 7e-33 | 29/33 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.481×** | -10.1 | 5e-22 | 28/36 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -10.0 | 9e-22 | 23/34 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.484×** | -10.0 | 9e-22 | 22/28 (NCI-H2030, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.482×** | -9.7 | 2e-20 | 27/36 (HS-578T, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.546×** | -8.3 | 4e-15 | 26/36 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.541×** | -8.1 | 2e-14 | 23/34 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.623×** | -8.0 | 3e-14 | 26/35 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.560×** | -7.7 | 6e-13 | 25/34 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.540×** | -7.5 | 2e-12 | 23/36 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.622×** | -6.0 | 4e-08 | 24/36 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 58.1 | 0 | 29 (6 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0273× (z -30.9) ⚠ position correction uncertain · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0135× (z -28.9) |
| [[MIA PaCa-2 (line)]] | alt | 88.5 | 0 | 21 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -25.2) |
| [[HOP62 (line)]] | alt | 38.9 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -25.6) |
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -18.4) |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -22.0) |
| [[A-172 (line)]] | wt | 39.2 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -15.9) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -26.5) |
| [[RKO (line)]] | wt | 32.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -19.3) |
| [[H4 (line)]] | wt | 18.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -13.2) |
| [[LS 180 (line)]] | wt | 28.0 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 6 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0307× (z -18.8) |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 39.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.6) |
| [[KATO III (line)]] | alt | 18.3 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 8.38 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0349× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0460× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -12.1) |
| [[A549 (line)]] | wt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.1) |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -16.8) |
| [[SW480 (line)]] | alt | 8.45 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -8.8) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.83 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Neuronal System |
| [[RASA3]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[RAC2]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RIN1]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHG5]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[SHC4]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ARID3B]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[PHC2]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CYTH4]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWTR1]] | B | WWTR1 activity raises KCNN4's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 3.86× lower at baseline in the lines without WWTR1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[COL13A1]] | B | COL13A1 activity raises KCNN4's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.19× lower at baseline in the lines without COL13A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[SMOX]] | B | SMOX activity raises KCNN4's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.78× lower at baseline in the lines without SMOX | 0.042 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises KCNN4's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.80× lower at baseline in the lines without PLAUR | 0.060 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[FOSL1]] | B | FOSL1 activity raises KCNN4's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 3.79× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[NIBAN2]] | B | NIBAN2 activity raises KCNN4's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[PEAR1]] | B | PEAR1 activity raises KCNN4's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without PEAR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[PLEKHG5]] | B | PLEKHG5 activity raises KCNN4's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without PLEKHG5 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent; its own permutation p |
| [[RHBDF2]] | B | RHBDF2 activity raises KCNN4's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without RHBDF2 | 0.093 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises KCNN4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSCN1]] | C | FSCN1 activity raises KCNN4's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 3.23× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXN]] | B | KCNN4 activity raises PXN's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without KCNN4 | 0.010 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[WWTR1]] | B | KCNN4 activity raises WWTR1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without KCNN4 | 0.011 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[PAEP]] | B | KCNN4 activity lowers PAEP's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.12× higher at baseline in the lines without KCNN4 | 0.026 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[FOSL1]] | B | KCNN4 activity raises FOSL1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without KCNN4 | 0.030 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[MEAK7]] | B | KCNN4 activity raises MEAK7's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without KCNN4 | 0.054 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[COL13A1]] | B | KCNN4 activity raises COL13A1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 4.03× lower at baseline in the lines without KCNN4 | 0.057 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[S100A16]] | B | KCNN4 activity raises S100A16's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without KCNN4 | 0.061 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[MYO10]] | B | KCNN4 activity raises MYO10's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without KCNN4 | 0.072 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[FHOD1]] | B | KCNN4 activity raises FHOD1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without KCNN4 | 0.093 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.3, 1.9); signed map (1.1, 48.8). **Vector** length 111, 32.0% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.4 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.3 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -8.0 |
|  | [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | -5.2 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -8.1 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -4.8 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily N member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,766,533-43,780,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCa3.1, hSK4, hKCa4, hIKCa1, IK |
| Gene groups (HGNC) | Potassium calcium-activated channels |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Ca2+ activated K+ channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O15554](https://www.uniprot.org/uniprotkb/O15554) (Intermediate conductance calcium-activated potassium channel protein 4):

> Intermediate conductance calcium-activated potassium channel that mediates the voltage-independent transmembrane transfer of potassium across the cell membrane through a constitutive interaction with calmodulin which binds the intracellular calcium allowing its opening. The current is characterized by a voltage-independent activation, an intracellular calcium concentration increase-dependent activation and a single-channel conductance of about 25 picosiemens. Also presents an inwardly …

**Summary**, from NCBI Gene [3783](https://www.ncbi.nlm.nih.gov/gene/3783):

> The protein encoded by this gene is part of a potentially heterotetrameric voltage-independent potassium channel that is activated by intracellular calcium. Activation is followed by membrane hyperpolarization, which promotes calcium influx. The encoded protein may be part of the predominant calcium-activated potassium channel in T-lymphocytes. This gene is similar to other KCNN family potassium channel genes, but it differs enough to possibly be considered as part of a new subfamily. [provided …

**Accessions** — [HGNC:6293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6293) · Entrez [3783](https://www.ncbi.nlm.nih.gov/gene/3783) · UniProt [O15554](https://www.uniprot.org/uniprotkb/O15554) · Ensembl [ENSG00000104783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104783)

## Data

Gene col 2497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2497); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2497]; `tensor/DDL_lfc|DDL_z.npy` [2497]; `embed/gene_vectors.npy` [2497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2497 or target_col == 2497). Every well: [[KCNN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
