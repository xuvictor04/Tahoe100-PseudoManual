---
symbol: "DYNLT3"
type: "gene"
col: 9078
ensembl_id: "ENSG00000165169"
name: "dynein light chain Tctex-type 3"
location: "Xp11.4"
module: 208
arm: "+"
pooled_cpm: 42.91
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# DYNLT3

*dynein light chain Tctex-type 3* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +14.6, q 1e-45, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +5.0, q 8e-05, up in 32 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1573 4.67×, LoVo 3.96×, SW480 3.27×, LOX-IMVI 5.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 4.95×, NCI-H1573 3.63×, A549 4.23×, SW480 3.37×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 2.04×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.856× (z -7.8, q 4e-12, down in 8 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.761× (z -5.5, q 9e-06, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDS]] (+0.64, fdr 7e-06), [[SH3BGRL3]] (+0.62, fdr 1e-05), [[TUBA1A]] (+0.59, fdr 1e-05); moves opposite to [[RPRD1B]] (-0.53, fdr 8e-05), [[RPRD2]] (-0.52, fdr 4e-05), [[SART3]] (-0.49, fdr 4e-04).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADAM19]] → it (grade B ⚠); 16 go from it, the strongest it → [[ARPC5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H1573 4.67×, LoVo 3.96×, SW480 3.27×, LOX-IMVI 5.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 4.95×, NCI-H1573 3.63×, A549 4.23×, SW480 3.37×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +14.6 | 1e-45 | 39/39 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +13.1 | 5e-37 | 33/35 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +10.3 | 2e-22 | 33/37 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.9 | 6e-07 | 24/40 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.0 | 8e-05 | 32/44 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +3.8 | 0.011 | 20/44 (SW1417, LoVo, …) | inconsistent across doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.053 | 14/44 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 1.24× | +3.2 | 0.11 | 10/44 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.856× | -7.8 | 4e-12 | 8/45 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.761×** | -5.5 | 9e-06 | 24/44 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.751×** | -4.1 | 0.008 | 19/44 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.040 | 23/44 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -3.6 | 0.040 | 19/44 (HOP62, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.787× | -3.2 | 0.11 | 15/43 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.801× | -3.2 | 0.12 | 12/44 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.858× | -3.1 | 0.13 | 12/44 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.810× | -3.0 | 0.13 | 20/44 (LS 180, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.13 | 19/44 (SW 1088, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.811× | -3.0 | 0.13 | 15/44 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 169 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +13.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 35.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 88.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.4) |
| [[SW480 (line)]] | alt | 29.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[A549 (line)]] | wt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 39.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.9) |
| [[KATO III (line)]] | alt | 142 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -18.0) |
| [[A-427 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0781× (z -8.9) |
| [[H4 (line)]] | wt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.6) |
| [[HS-578T (line)]] | alt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -22.5) |
| [[HT-29 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 67.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDS]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SH3BGRL3]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TUBA1A]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 | STRING 400 |
| [[PKIA]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZCCHC24]] | +0.58 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[MMP1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[C3orf52]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RHOC]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RASSF2]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD1B]] | -0.53 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[RPRD2]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SART3]] | -0.49 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[DUS3L]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[NNMT]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[UNC5CL]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PATZ1]] | -0.46 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[MRM1]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[AKAP8]] | -0.46 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ACTR3C]] | -0.45 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[ZNRF3]] | -0.45 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[LETMD1]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM19]] | B | ADAM19 activity raises DYNLT3's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without ADAM19 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[ASPH]] | B | ASPH activity raises DYNLT3's level | lines that do not express ASPH (5) vs lines expressing it (45) | 2.55× lower at baseline in the lines without ASPH | 0.021 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[KHDRBS3]] | B | KHDRBS3 activity raises DYNLT3's level | lines that do not express KHDRBS3 (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without KHDRBS3 | 0.064 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers DYNLT3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NMNAT2]] | B | NMNAT2 activity raises DYNLT3's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without NMNAT2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARPC5]] | C | DYNLT3 activity raises ARPC5's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without DYNLT3 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | DYNLT3 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.57× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| [[ADAM19]] | C | DYNLT3 activity raises ADAM19's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 5.78× lower at baseline in the lines without DYNLT3 | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| [[PPFIBP1]] | C | DYNLT3 activity strengthens PPFIBP1's drug response | lines that do not express DYNLT3 (4) vs lines expressing it (45) | the lines without DYNLT3 respond 0.08× as strongly (z diff +4.43); strongest at Homoharringtonine 5 µM: 1.42x vs 0.67x (z diff +9.2) | 0.032 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1; target measured in part of the lines; the reference differs; artifact flags |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | DYNLT3 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.75× the cells of the other lines | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| [[LPCAT2]] | C | DYNLT3 activity raises LPCAT2's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 4.97× lower at baseline in the lines without DYNLT3 | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| [[CFAP20DC]] | C | DYNLT3 activity raises CFAP20DC's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 5.19× lower at baseline in the lines without DYNLT3 | 0.056 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| cells under [[Harringtonine (drug)]] 0.5 µM | C | DYNLT3 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.38× the cells of the other lines | 0.056 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| cells under [[Tucatinib (drug)]] 5 µM | C | DYNLT3 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.73× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| cells under [[AZD2858 (drug)]] 0.5 µM | C | DYNLT3 activity raises the cells' numbers under AZD2858 0.5 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.69× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | DYNLT3 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express DYNLT3 (4) vs lines expressing it (44) | the lines without DYNLT3: 0.79× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |
| [[PPFIBP1]] | C | DYNLT3 activity raises PPFIBP1's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without DYNLT3 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.8, 1.4); signed map (-2.8, 47.3). **Vector** length 105, 27.9% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +10.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.9 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.5 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain Tctex-type 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:37,836,757-37,847,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCTEX1L; previously TCTE1L |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein 2 complex subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein light chain Tctex-type family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P51808](https://www.uniprot.org/uniprotkb/P51808) (Dynein light chain Tctex-type 3):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. Probably binds BUB3 as part of transport cargo. Required for the efficient progression through mitosis (By similarity).

**Summary**, from NCBI Gene [6990](https://www.ncbi.nlm.nih.gov/gene/6990):

> This gene encodes a member of a subclass of dynein light chains. The encoded protein homodimerizes and forms the light chain component of the cytoplasmic dynein motor protein complex. This protein may be important for binding dynein to specific cargos including the spindle checkpoint protein BUB3. This protein may also function independently of dynein as a transcriptional modulator. Pseudogenes of this gene are found on chromosomes 2 and 20.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:11694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11694) · Entrez [6990](https://www.ncbi.nlm.nih.gov/gene/6990) · UniProt [P51808](https://www.uniprot.org/uniprotkb/P51808) · Ensembl [ENSG00000165169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165169)

## Data

Gene col 9078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9078); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9078]; `tensor/DDL_lfc|DDL_z.npy` [9078]; `embed/gene_vectors.npy` [9078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9078 or target_col == 9078). Every well: [[DYNLT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
