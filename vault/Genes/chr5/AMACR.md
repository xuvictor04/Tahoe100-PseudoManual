---
symbol: "AMACR"
type: "gene"
col: 14302
ensembl_id: "ENSG00000242110"
name: "alpha-methylacyl-CoA racemase"
location: "5p13.2"
module: 28
arm: "+"
pooled_cpm: 9.27
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 22
n_dd_up_clean: 15
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AMACR

*alpha-methylacyl-CoA racemase* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.59× (z +9.4, q 4e-18, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.407× (z -12.9, q 1e-35, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.62, fdr 7e-06), [[PLEKHF2]] (+0.61, fdr 9e-06), [[FANCF]] (+0.60, fdr 7e-06); moves opposite to [[LMBR1]] (-0.58, fdr 4e-05), [[MBOAT7]] (-0.58, fdr 1e-05), [[B4GALNT3]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WHAMMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +9.4 | 4e-18 | 31/47 (J82, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +8.9 | 1e-16 | 26/38 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +6.8 | 2e-09 | 28/47 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 2e-06 | 15/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 6e-04 | 12/46 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 0.001 | 16/45 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.0 | 0.004 | 11/43 (SW480, A-427, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.004 | 11/46 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +3.8 | 0.009 | 12/45 (J82, SNU-1, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.20× | +3.6 | 0.017 | 3/47 (NCI-H661, BT-474, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.018 | 14/46 (SW480, BT-474, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.018 | 12/47 (SW480, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.022 | 5/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.033 | 5/44 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.066 | 2/47 (NCI-H1573, SW480) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.078 | 8/48 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.082 | 4/40 (SW480, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.082 | 9/47 (SW480, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -12.9 | 1e-35 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.421×** | -12.5 | 3e-33 | 42/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -11.4 | 1e-27 | 36/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -10.6 | 4e-24 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.510×** | -9.7 | 3e-20 | 28/46 (SW480, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.510×** | -9.7 | 3e-20 | 32/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -8.2 | 2e-14 | 30/47 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.564×** | -7.8 | 4e-13 | 30/44 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.358×** | -7.7 | 6e-13 | 29/41 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -7.4 | 1e-11 | 25/46 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -5.8 | 4e-07 | 20/43 (SW480, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.685×** | -5.4 | 2e-06 | 19/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -5.3 | 6e-06 | 18/45 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -4.9 | 5e-05 | 16/38 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.008 | 14/44 (HCT15, RKO, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.725×** | -3.3 | 0.026 | 6/47 (PANC-1, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.026 | 10/46 (NCI-H2347, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0761× (z -18.7) |
| [[SW480 (line)]] | alt | 13.4 | 1 | 5 (1 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.73× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 7.55 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.140× (z -10.8) |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -9.1) |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.175× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 8.18 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0769× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.155× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 7.91 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0960× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -8.5) |
| [[A549 (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 9.17 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0381× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.171× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0728× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 6.55 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.119× (z -9.0) |
| [[SW 900 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHF2]] | +0.61 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[FANCF]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PNPLA4]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MTARC2]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.59 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[PAIP1]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RBM7]] | +0.59 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CLK4]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PPP4R2]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[MBOAT7]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[B4GALNT3]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[SENP5]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[EXD3]] | -0.56 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[MROH1]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[VPS53]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[FBXW7]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ARL17A]] | -0.53 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[GATAD2A]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHAMMP2]] | B | WHAMMP2 activity raises AMACR's level | lines that do not express WHAMMP2 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without WHAMMP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LIFR, ZNF512B, ENSG00000286964; maybe low, not absent; its own permutation p |
| [[BICDL1]] | B | BICDL1 activity raises AMACR's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without BICDL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.9, 3.3); signed map (10.6, -36.5). **Vector** length 72.1, 12.5% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.9 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -10.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -8.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | alpha-methylacyl-CoA racemase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:33,986,165-34,008,104 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RACE, P504S |
| Hallmark sets | BILE_ACID_METABOLISM, IL2_STAT5_SIGNALING |
| Reactome | 11 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHK6](https://www.uniprot.org/uniprotkb/Q9UHK6) (Alpha-methylacyl-CoA racemase):

> Catalyzes the interconversion of (R)- and (S)-stereoisomers of alpha-methyl-branched-chain fatty acyl-CoA esters. Acts only on coenzyme A thioesters, not on free fatty acids, and accepts as substrates a wide range of alpha-methylacyl-CoAs, including pristanoyl-CoA, trihydroxycoprostanoyl-CoA (an intermediate in bile acid synthesis), and arylpropionic acids like the anti-inflammatory drug ibuprofen (2-(4-isobutylphenyl)propionic acid) but neither 3-methyl-branched nor linear-chain acyl-CoAs.

**Summary**, from NCBI Gene [23600](https://www.ncbi.nlm.nih.gov/gene/23600):

> This gene encodes a racemase. The encoded enzyme interconverts pristanoyl-CoA and C27-bile acylCoAs between their (R)- and (S)-stereoisomers. The conversion to the (S)-stereoisomers is necessary for degradation of these substrates by peroxisomal beta-oxidation. Encoded proteins from this locus localize to both mitochondria and peroxisomes. Mutations in this gene may be associated with adult-onset sensorimotor neuropathy, pigmentary retinopathy, and adrenomyeloneuropathy due to defects in bile …

**Accessions** — [HGNC:451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:451) · Entrez [23600](https://www.ncbi.nlm.nih.gov/gene/23600) · UniProt [Q9UHK6](https://www.uniprot.org/uniprotkb/Q9UHK6) · Ensembl [ENSG00000242110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242110)

## Data

Gene col 14302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14302); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14302]; `tensor/DDL_lfc|DDL_z.npy` [14302]; `embed/gene_vectors.npy` [14302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14302 or target_col == 14302). Every well: [[AMACR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMACR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
