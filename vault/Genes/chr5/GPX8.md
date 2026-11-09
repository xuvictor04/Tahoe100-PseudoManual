---
symbol: "GPX8"
type: "gene"
col: 8920
ensembl_id: "ENSG00000164294"
name: "glutathione peroxidase 8 (putative)"
location: "5q11.2"
module: 30
arm: "+"
pooled_cpm: 18.24
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 44
n_dd_up_clean: 10
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GPX8

*glutathione peroxidase 8 (putative)* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +7.4, q 8e-11, up in 26 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 2.49× (z +6.0, q 3e-07, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.254× (z -24.4, q 0e+00, down in 35 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC10A7]] (+0.63, fdr 1e-05), [[ANKMY2]] (+0.59, fdr 1e-05), [[GNPDA2]] (+0.57, fdr 1e-05); moves opposite to [[KDM7A-DT]] (-0.55, fdr 1e-05), [[TLNRD1]] (-0.50, fdr 2e-05), [[PLEKHN1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMC6]] → it (grade B ⚠); 5 go from it, the strongest it → [[GLT8D1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.4 | 8e-11 | 26/35 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.8 | 2e-09 | 14/21 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **2.49×** | +6.0 | 3e-07 | 26/39 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.7 | 2e-06 | 25/40 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.0 | 8e-05 | 16/32 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 17/40 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.008 | 16/40 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.008 | 12/40 (MIA PaCa-2, C-33 A, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.008 | 19/40 (RKO, A-427, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +3.8 | 0.008 | 14/40 (PANC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.012 | 19/39 (HOP62, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.013 | 11/40 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.030 | 9/40 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.055 | 9/39 (MIA PaCa-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.254×** | -24.4 | 0e+00 | 35/39 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.240×** | -18.0 | 0e+00 | 32/39 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -15.5 | 0e+00 | 32/39 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.332×** | -13.4 | 2e-38 | 34/39 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.357×** | -13.0 | 1e-36 | 33/40 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -12.2 | 3e-32 | 34/40 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -12.2 | 3e-32 | 31/40 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -11.9 | 5e-31 | 33/40 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.394×** | -11.7 | 6e-30 | 33/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -10.6 | 2e-24 | 34/40 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.446×** | -10.2 | 1e-22 | 31/40 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -10.0 | 1e-21 | 26/40 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.475×** | -9.4 | 3e-19 | 30/40 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -6.9 | 2e-10 | 29/40 (Hs 766T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -6.1 | 4e-08 | 24/39 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.624×** | -5.9 | 1e-07 | 23/39 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.0411× (z -32.5) |
| [[HS-578T (line)]] | alt | 43.1 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.5) |
| [[A498 (line)]] | wt | 68.1 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -25.9) |
| [[A-172 (line)]] | wt | 37.4 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.7) |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -21.3) |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -26.8) |
| [[H4 (line)]] | wt | 40.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0405× (z -17.6) |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -14.1) |
| [[C32 (line)]] | wt | 21.4 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -15.8) |
| [[J82 (line)]] | alt | 27.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -21.8) |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.8) |
| [[RKO (line)]] | wt | 28.7 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0787× (z -16.8) |
| [[SW480 (line)]] | alt | 6.51 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.9) |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.3) |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 7.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 9.41 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.199× (z -8.5) |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.0) |
| [[SW 1088 (line)]] | alt | 69.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -10.1) |
| [[SW48 (line)]] | wt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.3) |
| [[A549 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC10A7]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[POPDC3]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GFM2]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EPRS1]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[COPB1]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PARP2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[EIF2AK1]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[TXNL1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SEC13]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CKAP4]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM7A-DT]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PLEKHN1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CCDC71L]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[CLCF1]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[PHLDA2]] | -0.48 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[LIF]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[S100A11]] | -0.48 | -0.35 / -0.46 | both halves | 1e-04 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[BAIAP2L1]] | -0.47 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[EPHA2]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TNFAIP8]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TMC6]] | -0.47 | -0.46 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | TMC6 activity lowers GPX8's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.50× higher at baseline in the lines without TMC6 | 0.047 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[MAP2K1]] | B | MAP2K1 activity lowers GPX8's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[DZIP1L]] | B | DZIP1L activity raises GPX8's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.55× lower at baseline in the lines without DZIP1L | 0.064 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises GPX8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers GPX8's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.8% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLT8D1]] | B | GPX8 activity raises GLT8D1's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without GPX8 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |
| [[DFFB]] | B | GPX8 activity raises DFFB's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without GPX8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |
| [[EPRS1]] | B | GPX8 activity raises EPRS1's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.17× lower at baseline in the lines without GPX8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |
| [[TNFAIP8]] | B | GPX8 activity strengthens TNFAIP8's drug response | lines that do not express GPX8 (8) vs lines expressing it (40) | the lines without GPX8 respond 0.84× as strongly (z diff +1.22); strongest at Ixazomib citrate 0.5 µM: 1.16x vs 0.63x (z diff +6.2) | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1; target measured in part of the lines; artifact flags |
| [[CDC40]] | B | GPX8 activity raises CDC40's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without GPX8 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.333). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-19.8, -8.5); signed map (-28.8, -23.0). **Vector** length 102, 27.2% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -15.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -12.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | glutathione peroxidase 8 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,160,167-55,167,297 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ847, EPLA847 |
| Gene groups (HGNC) | Glutathione peroxidase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TED1](https://www.uniprot.org/uniprotkb/Q8TED1) (Protein peroxidase GPX8):

> Acts as an endoplasmic reticulum (ER) thiol peroxidase that maintains ER redox homeostasis and protects the cytosol from ER-derived H(2)O(2). Functions in a redox relay with ERO1A, using ERO1A-generated H(2)O(2) to drive PDI oxidation, linking peroxide detoxification to productive disulfide formation. Modulates endoplasmic reticulum Ca(2+) levels mainly through SERCA pump activity and partially by influencing passive Ca(2+) leakage.

**Summary**, from NCBI Gene [493869](https://www.ncbi.nlm.nih.gov/gene/493869):

> Enables peroxidase activity. Predicted to be involved in cellular response to oxidative stress. Predicted to be located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33100) · Entrez [493869](https://www.ncbi.nlm.nih.gov/gene/493869) · UniProt [Q8TED1](https://www.uniprot.org/uniprotkb/Q8TED1) · Ensembl [ENSG00000164294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164294)

## Data

Gene col 8920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8920); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8920]; `tensor/DDL_lfc|DDL_z.npy` [8920]; `embed/gene_vectors.npy` [8920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8920 or target_col == 8920). Every well: [[GPX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
