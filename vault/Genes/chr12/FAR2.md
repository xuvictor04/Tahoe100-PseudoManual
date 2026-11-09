---
symbol: "FAR2"
type: "gene"
col: 760
ensembl_id: "ENSG00000064763"
name: "fatty acyl-CoA reductase 2"
location: "12p11.22"
module: 5
arm: "+"
pooled_cpm: 26.93
n_lines_expressing: 31
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# FAR2

*fatty acyl-CoA reductase 2* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.34× (z +4.6, q 0.003, up in 5 of 21 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 5.51×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 7.06×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.273× (z -21.2, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRK1]] (+0.60, fdr 1e-05), [[NIPAL1]] (+0.59, fdr 3e-05), [[SLFNL1-AS1]] (+0.58, fdr 3e-05); moves opposite to [[PLEKHH3]] (-0.55, fdr 2e-04), [[ALAD]] (-0.52, fdr 5e-05), [[PJA2]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[NIPAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 760.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 5.51×); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 7.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.6 | 0.003 | 5/21 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.5 | 0.13 | 8/29 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.24× | +3.4 | 0.13 | 10/28 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.28 | 7/29 (SW 900, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.273×** | -21.2 | 0e+00 | 28/28 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.287×** | -20.4 | 0e+00 | 28/29 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.305×** | -19.4 | 0e+00 | 28/29 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -13.3 | 2e-38 | 22/29 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.449×** | -13.1 | 7e-37 | 25/29 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.581×** | -8.9 | 8e-17 | 23/29 (BT-474, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.590×** | -8.6 | 6e-16 | 24/28 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -7.8 | 4e-13 | 20/29 (RKO, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.621×** | -7.5 | 5e-12 | 19/29 (RKO, J82, …) | top dose only | composition shift; position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.461×** | -6.6 | 2e-09 | 21/28 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.468×** | -6.5 | 5e-09 | 21/29 (J82, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.701×** | -5.8 | 3e-07 | 19/29 (LoVo, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -5.5 | 1e-06 | 17/28 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.740×** | -4.9 | 4e-05 | 17/27 (RPMI-7951, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -4.8 | 8e-05 | 16/29 (CHP-212, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.750×** | -4.7 | 9e-05 | 10/29 (NCI-H2347, SW 1088, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -4.7 | 1e-04 | 16/29 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 6e-04 | 11/29 (C32, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 112 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0539× (z -21.9) |
| [[LoVo (line)]] | wt | 66.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -27.7) |
| [[LS 180 (line)]] | wt | 104 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0823× (z -22.3) |
| [[RKO (line)]] | wt | 119 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0678× (z -23.5) |
| [[J82 (line)]] | alt | 98.1 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0630× (z -23.9) |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -18.6) |
| [[PANC-1 (line)]] | alt | 41.1 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 37.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0838× (z -25.2) |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -13.3) |
| [[A498 (line)]] | wt | 50.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.2) |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0863× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.6) |
| [[A-172 (line)]] | wt | 17.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -10.6) |
| [[HS-578T (line)]] | alt | 50.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -13.0) |
| [[HT-29 (line)]] | alt | 51.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0833× (z -18.1) |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 7.79 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.189× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 7.06× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.107× (z -13.0) |
| [[C32 (line)]] | wt | 28.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -8.9) |
| [[A-427 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRK1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NIPAL1]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SLFNL1-AS1]] | +0.58 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PIGW]] | +0.58 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[PRMT3]] | +0.56 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[E2F3]] | +0.56 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[PRDM5]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[NIP7]] | +0.56 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[PTPRG]] | +0.55 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[DIMT1]] | +0.55 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[WDR4]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZNF710]] | +0.55 | +0.40 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | -0.55 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[ALAD]] | -0.52 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PJA2]] | -0.51 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[FHIP1A]] | -0.51 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[KMT2C]] | -0.50 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[KBTBD3]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ANO8]] | -0.49 | -0.24 / -0.47 | both halves | 5e-04 |  |
| [[RAB3A]] | -0.48 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[SLC25A23]] | -0.48 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ZFP14]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[FBXO16]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[SIRT2]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TBC1D17]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPAL1]] | B | FAR2 activity raises NIPAL1's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without FAR2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[ENOX2]] | B | FAR2 activity lowers ENOX2's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.38× higher at baseline in the lines without FAR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[FHIP1A]] | B | FAR2 activity raises FHIP1A's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without FAR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[GBX2-AS1]] | B | FAR2 activity lowers GBX2-AS1's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.54× higher at baseline in the lines without FAR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[ATR]] | B | FAR2 activity lowers ATR's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.27× higher at baseline in the lines without FAR2 | 0.092 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[PIGW]] | B | FAR2 activity lowers PIGW's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.19× higher at baseline in the lines without FAR2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.1, -32.7); signed map (3.1, -49.8). **Vector** length 75.8, 17.5% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | fatty acyl-CoA reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:29,149,016-29,341,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10462, SDR10E2; previously MLSTD1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 2 pathways, smallest: Wax and plasmalogen biosynthesis; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K12](https://www.uniprot.org/uniprotkb/Q96K12) (Fatty acyl-CoA reductase 2):

> Catalyzes the reduction of saturated but not unsaturated C16 or C18 fatty acyl-CoA to fatty alcohols (FAls). A lower activity can be observed with shorter fatty acyl-CoA substrates. Can produce very long-chain and ultra long-chain FAls, regardless of whether they have a straight or branched chain. Involved in the production of ether lipids/plasmalogens and wax monoesters whose synthesis requires FAls as substrates.

**Summary**, from NCBI Gene [55711](https://www.ncbi.nlm.nih.gov/gene/55711):

> This gene belongs to the short chain dehydrogenase/reductase superfamily. It encodes a reductase enzyme involved in the first step of wax biosynthesis wherein fatty acids are converted to fatty alcohols. The encoded peroxisomal protein utilizes saturated fatty acids of 16 or 18 carbons as preferred substrates. Alternatively spliced transcript variants have been observed for this gene. Related pseudogenes have been identified on chromosomes 2, 14 and 22. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:25531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25531) · Entrez [55711](https://www.ncbi.nlm.nih.gov/gene/55711) · UniProt [Q96K12](https://www.uniprot.org/uniprotkb/Q96K12) · Ensembl [ENSG00000064763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064763)

## Data

Gene col 760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 760); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 760]; `tensor/DDL_lfc|DDL_z.npy` [760]; `embed/gene_vectors.npy` [760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 760 or target_col == 760). Every well: [[FAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
