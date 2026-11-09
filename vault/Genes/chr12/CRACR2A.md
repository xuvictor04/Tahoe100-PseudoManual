---
symbol: "CRACR2A"
type: "gene"
col: 5019
ensembl_id: "ENSG00000130038"
name: "calcium release activated channel regulator 2A"
location: "12p13.32"
module: 4
arm: "+"
pooled_cpm: 17.65
n_lines_expressing: 30
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CRACR2A

*calcium release activated channel regulator 2A* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +9.0, q 2e-16, up in 10 of 18 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 5.82×; ⚠ cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.292× (z -16.2, q 0e+00, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN2]] (+0.66, fdr 1e-05), [[MAK16]] (+0.64, fdr 1e-05), [[PFAS]] (+0.60, fdr 2e-05); moves opposite to [[GPX4]] (-0.64, fdr 1e-05), [[CDKN2D]] (-0.58, fdr 3e-05), [[TMEM50A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GLDN]] → it (grade B ⚠); 4 go from it, the strongest it → [[BDH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5019.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 5.82×; ⚠ cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +9.0 | 2e-16 | 10/18 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.2 | 6e-14 | 9/24 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.6 | 0.047 | 10/23 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.6 | 0.047 | 12/28 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.28× | +3.3 | 0.11 | 8/27 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.14 | 4/27 (SW 900, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.292×** | -16.2 | 0e+00 | 25/27 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.495×** | -13.0 | 2e-36 | 22/26 (RKO, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.391×** | -12.3 | 9e-33 | 25/28 (HT-29, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.391×** | -12.3 | 9e-33 | 25/28 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.400×** | -12.0 | 3e-31 | 22/28 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.467×** | -10.0 | 2e-21 | 22/26 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.559×** | -7.6 | 2e-12 | 21/27 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.573×** | -7.0 | 1e-10 | 22/27 (RKO, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.601×** | -6.7 | 1e-09 | 18/28 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.605×** | -6.6 | 3e-09 | 21/27 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -6.3 | 2e-08 | 22/26 (RKO, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.675×** | -5.1 | 1e-05 | 13/27 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.019 | 15/28 (HOP62, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.766×** | -3.5 | 0.019 | 17/26 (COLO 205, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.770×** | -3.4 | 0.023 | 16/26 (RKO, KATO III, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -3.1 | 0.074 | 15/25 (KATO III, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.642×** | -3.0 | 0.075 | 12/26 (SW48, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.646×** | -3.0 | 0.080 | 11/26 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 108 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -17.0) |
| [[HOP62 (line)]] | alt | 30.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -14.5) |
| [[KATO III (line)]] | alt | 33.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -14.8) |
| [[SW48 (line)]] | wt | 47.4 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0620× (z -17.1) |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.234× (z -9.7) |
| [[HT-29 (line)]] | alt | 39.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.232× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -13.0) |
| [[SW 900 (line)]] | alt | 53.9 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.146× (z -11.3) |
| [[SW480 (line)]] | alt | 66.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -9.3) |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.218× (z -10.1) |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -8.7) |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 7.81 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +10.6) ⚠ cell-cycle shift, explains ~44% of this change | [[Simotinib (drug)]] 5 µM 0.117× (z -8.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.197× (z -9.0) |
| [[A-172 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN2]] | +0.66 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[MAK16]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PFAS]] | +0.60 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ATIC]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[BDH1]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PUM3]] | +0.58 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[UTP20]] | +0.58 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[DHX37]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[GNL3L]] | +0.56 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[IPO4]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[WDR46]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[FAM136A]] | +0.56 | +0.35 / +0.65 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX4]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[TMEM50A]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.55 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[WIPF2]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[HCFC1R1]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[COX6A1]] | -0.53 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[DDT]] | -0.53 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[AAMDC]] | -0.52 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[UPK1A-AS1]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MIEN1]] | -0.52 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[GABARAPL2]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLDN]] | B | GLDN activity raises CRACR2A's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without GLDN | 0.019 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[BDH1]] | B | BDH1 activity raises CRACR2A's level | lines that do not express BDH1 (11) vs lines expressing it (39) | 3.92× lower at baseline in the lines without BDH1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF785, STAP2 |
| [[SLC43A1]] | B | SLC43A1 activity raises CRACR2A's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 2.71× lower at baseline in the lines without SLC43A1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDH1]] | B | CRACR2A activity raises BDH1's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without CRACR2A | 0.009 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[GLDN]] | B | CRACR2A activity raises GLDN's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CRACR2A | 0.061 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[SHOC2]] | B | CRACR2A activity lowers SHOC2's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 1.16× higher at baseline in the lines without CRACR2A | 0.073 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[SLC43A1]] | B | CRACR2A activity raises SLC43A1's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CRACR2A | 0.089 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.9, -34.2); signed map (-5.5, -44.1). **Vector** length 73.8, 18.8% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -0.1 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | -12.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -16.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | calcium release activated channel regulator 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:3,606,633-3,764,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4266, RAB46; previously EFCAB4B |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; EF-hand domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSW2](https://www.uniprot.org/uniprotkb/Q9BSW2) (EF-hand calcium-binding domain-containing protein 4B):

> [Isoform 1]: Ca(2+)-binding protein that plays a key role in store-operated Ca(2+) entry (SOCE) in T-cells by regulating CRAC channel activation. Acts as a cytoplasmic calcium-sensor that facilitates the clustering of ORAI1 and STIM1 at the junctional regions between the plasma membrane and the endoplasmic reticulum upon low Ca(2+) concentration. It thereby regulates CRAC channel activation, including translocation and clustering of ORAI1 and STIM1. Upon increase of cytoplasmic Ca(2+) resulting …

**Summary**, from NCBI Gene [84766](https://www.ncbi.nlm.nih.gov/gene/84766):

> Enables G protein activity and calcium ion binding activity. Involved in several processes, including positive regulation of JNK cascade; positive regulation of monoatomic ion transport; and store-operated calcium entry. Located in several cellular components, including Golgi apparatus; Weibel-Palade body; and immunological synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28657) · Entrez [84766](https://www.ncbi.nlm.nih.gov/gene/84766) · UniProt [Q9BSW2](https://www.uniprot.org/uniprotkb/Q9BSW2) · Ensembl [ENSG00000130038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130038)

## Data

Gene col 5019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5019); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5019]; `tensor/DDL_lfc|DDL_z.npy` [5019]; `embed/gene_vectors.npy` [5019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5019 or target_col == 5019). Every well: [[CRACR2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRACR2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
