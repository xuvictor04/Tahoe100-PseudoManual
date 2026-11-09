---
symbol: "KDM5D"
type: "gene"
col: 260
ensembl_id: "ENSG00000012817"
name: "lysine demethylase 5D"
location: "Yq11.223"
module: 177
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 20
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# KDM5D

*lysine demethylase 5D* — Yq11.223

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +7.1, q 8e-10, up in 13 of 18 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +5.5, q 5e-06, up in 15 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.654× (z -5.9, q 2e-06, down in 15 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.144×, C32 0.197×, A549 0.226×, SNU-1 0.184×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.0894×, H4 0.103×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.146×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.375×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTY]] (+0.67, fdr 1e-05), [[LINC02335]] (+0.64, fdr 3e-05), [[BAGE2]] (+0.61, fdr 9e-05); moves opposite to [[SNTB2]] (-0.48, fdr 1e-04), [[POC1B]] (-0.46, fdr 6e-05), [[DOCK9]] (-0.45, fdr 6e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[NAPRT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.44×** | +7.1 | 8e-10 | 13/18 (A549, A-172, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.8 | 4e-09 | 1/18 (HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.7 | 4e-09 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.7 | 4e-09 | 7/17 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.5 | 5e-06 | 1/16 (HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +5.5 | 5e-06 | 15/18 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 4e-04 | 1/18 (SNU-423) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.3 | 0.001 | 1/14 (A-427) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.001 | 1/18 (HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.1 | 0.002 | 2/14 (C32, J82) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 0/18 | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.008 | 1/18 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 0/18 | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 4/18 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.3 | 0.034 | 3/17 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.061 | 8/18 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 260.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.144×, C32 0.197×, A549 0.226×, SNU-1 0.184×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.0894×, H4 0.103×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.146×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.375×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -5.9 | 2e-06 | 15/18 (NCI-H460, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.750×** | -5.7 | 4e-06 | 18/18 (NCI-H460, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.668×** | -5.6 | 4e-06 | 15/18 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.675×** | -5.5 | 6e-06 | 9/18 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.698×** | -5.0 | 6e-05 | 12/18 (SNU-423, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.726×** | -4.5 | 8e-04 | 5/18 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.772×** | -3.6 | 0.025 | 3/18 (C32, CHP-212, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.763×** | -3.5 | 0.036 | 0/18 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.793× | -3.1 | 0.12 | 14/17 (C32, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.8 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -26.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -9.3) |
| [[C32 (line)]] | wt | 45.1 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -16.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 29.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 33.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -14.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 40.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 69.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -14.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.906 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTY]] | +0.67 | +0.51 / +0.75 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 999 |
| [[LINC02335]] | +0.64 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[BAGE2]] | +0.61 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[FAM230C]] | +0.59 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[LINC01518]] | +0.58 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[SDR39U1]] | +0.55 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[SCAF8]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MLST8]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZEB2]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CHIC1]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[NAPRT]] | +0.53 | +0.43 / +0.44 | both halves | 4e-05 |  |
| [[ZSCAN12]] | +0.51 | +0.39 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[POC1B]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[DOCK9]] | -0.45 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[RECQL]] | -0.45 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[LRRC8A]] | -0.45 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[SENP5]] | -0.45 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[SHPK]] | -0.44 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[BUD23]] | -0.44 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KDM5D's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UTY]] | C | UTY activity raises KDM5D's level | lines that do not express UTY (31) vs lines expressing it (19) | 15.30× lower at baseline in the lines without UTY | 1e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[USP9Y]] | C | USP9Y activity raises KDM5D's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 12.89× lower at baseline in the lines without USP9Y | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises KDM5D's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without ZEB2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises KDM5D's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 3.82× lower at baseline in the lines without LINC02941 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises KDM5D's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 2.20× lower at baseline in the lines without LINC00470 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAPRT]] | B | KDM5D activity lowers NAPRT's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 1.86× higher at baseline in the lines without KDM5D | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[MYL5]] | B | KDM5D activity weakens MYL5's drug response | lines that do not express KDM5D (28) vs lines expressing it (16) | the lines without KDM5D respond 1.58× as strongly (z diff -0.50); strongest at Homoharringtonine 5 µM: 2.37x vs 1.00x (z diff -2.8) | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; target measured in part of the lines; artifact flags |
| [[MYL5]] | B | KDM5D activity raises MYL5's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 1.11× lower at baseline in the lines without KDM5D | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[UTY]] | C | [[DDX3Y]], KDM5D activity raises UTY's level | lines that do not express DDX3Y, KDM5D (30) vs lines expressing them (20) | 24.64× lower at baseline in the lines without DDX3Y, KDM5D | 5e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[USP9Y]] | C | KDM5D activity raises USP9Y's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 20.37× lower at baseline in the lines without KDM5D | 7e-06 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[LINC02941]] | C | KDM5D activity raises LINC02941's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without KDM5D | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[ZEB2]] | C | KDM5D activity raises ZEB2's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 3.85× lower at baseline in the lines without KDM5D | 0.066 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[LINC00470]] | C | KDM5D activity raises LINC00470's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without KDM5D | 0.092 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.6, 27.4); signed map (34.8, 38.0). **Vector** length 42.2, 9.52% of its response variance represented; |z| ≥ 3 in 384 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -4.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 5D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.223 — chrY:19,703,865-19,744,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0234; previously HYA, HY, SMCY, JARID1D |
| Gene groups (HGNC) | PHD finger proteins; AT-rich interaction domain containing; Minor histocompatibility antigens; Lysine demethylase 5 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY66](https://www.uniprot.org/uniprotkb/Q9BY66) (Lysine-specific demethylase 5D):

> Histone demethylase that specifically demethylates 'Lys-4' of histone H3, thereby playing a central role in histone code. Does not demethylate histone H3 'Lys-9', H3 'Lys-27', H3 'Lys-36', H3 'Lys-79' or H4 'Lys-20'. Demethylates trimethylated and dimethylated but not monomethylated H3 'Lys-4'. May play a role in spermatogenesis. Involved in transcriptional repression of diverse metastasis-associated genes; in this function seems to cooperate with ZMYND8. Suppresses prostate cancer cell …

**Summary**, from NCBI Gene [8284](https://www.ncbi.nlm.nih.gov/gene/8284):

> This gene encodes a protein containing zinc finger domains. A short peptide derived from this protein is a minor histocompatibility antigen which can lead to graft rejection of male donor cells in a female recipient. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:11115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11115) · Entrez [8284](https://www.ncbi.nlm.nih.gov/gene/8284) · UniProt [Q9BY66](https://www.uniprot.org/uniprotkb/Q9BY66) · Ensembl [ENSG00000012817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012817)

## Data

Gene col 260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 260); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 260]; `tensor/DDL_lfc|DDL_z.npy` [260]; `embed/gene_vectors.npy` [260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 260 or target_col == 260). Every well: [[KDM5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
