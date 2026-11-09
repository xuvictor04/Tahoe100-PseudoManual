---
symbol: "IFNLR1"
type: "gene"
col: 11676
ensembl_id: "ENSG00000185436"
name: "interferon lambda receptor 1"
location: "1p36.11"
module: 31
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 32
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 20
direction_downstream: 27
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# IFNLR1

*interferon lambda receptor 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +6.9, q 4e-09, up in 15 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.397× (z -18.0, q 0e+00, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMCC3]] (+0.59, fdr 1e-05), [[NECTIN4]] (+0.58, fdr 1e-05), [[INAVA]] (+0.58, fdr 1e-05); moves opposite to [[WDR27]] (-0.54, fdr 1e-05), [[FAM120A]] (-0.51, fdr 3e-04), [[PTBP1]] (-0.50, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[GRAMD2B]] → it (grade B ⚠); 27 go from it, the strongest it → [[GRAMD2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.9 | 4e-09 | 15/29 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 1e-05 | 15/29 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.088 | 9/29 (LoVo, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.27× | +3.3 | 0.13 | 5/30 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.14 | 2/29 (KATO III, SW1417) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.18 | 10/29 (CFPAC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.397×** | -18.0 | 0e+00 | 25/28 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.390×** | -12.5 | 3e-33 | 23/28 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -10.5 | 1e-23 | 26/27 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -10.2 | 4e-22 | 23/28 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.505×** | -9.4 | 5e-19 | 19/24 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.528×** | -8.5 | 3e-15 | 15/16 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.656×** | -8.2 | 2e-14 | 20/29 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.556×** | -8.1 | 4e-14 | 21/30 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.661×** | -8.0 | 5e-14 | 24/29 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.567×** | -7.8 | 3e-13 | 23/30 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -5.7 | 7e-07 | 15/29 (KATO III, NCI-H2030, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.692×** | -5.1 | 2e-05 | 18/29 (NCI-H2030, NCI-H460, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -5.0 | 3e-05 | 15/29 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.711×** | -4.7 | 1e-04 | 15/29 (NCI-H1792, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.697×** | -4.6 | 2e-04 | 15/19 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -4.4 | 4e-04 | 12/30 (C32, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -4.4 | 5e-04 | 16/29 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.003 | 12/29 (NCI-H1792, HepG2/C3A, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.004 | 8/30 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.632×** | -3.3 | 0.026 | 8/29 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.027 | 8/29 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.030 | 3/30 (NCI-H1573, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 47.8 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -18.8) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -15.2) |
| [[LoVo (line)]] | wt | 48.4 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -21.1) |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 35.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.4) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 7.78 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.8) |
| [[SW48 (line)]] | wt | 29.6 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -9.0) |
| [[HOP62 (line)]] | alt | 9.72 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -10.9) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.3) |
| [[C-33 A (line)]] | alt | 6.75 | 0 | 1 | — | [[Macitentan (drug)]] 0.05 µM 0.0434× (z -8.8) |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 9.06 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCC3]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[INAVA]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KCNK1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LIPH]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CLDN4]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[CDH1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CBLC]] | +0.53 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[IL22RA1]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 | pathway: Interleukin-20 family signaling; STRING 822; ⚠ same locus (11.0 kb, same strand: neighbours can correlate without regulation) |
| [[HDHD3]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FA2H]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[PRSS3]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR27]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[FAM120A]] | -0.51 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[PTBP1]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MTR]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SNX5]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ERLIN2]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ZRANB3]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SIRT5]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[IPO4]] | -0.45 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SMG1P6]] | -0.45 | -0.20 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[RNH1]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | GRAMD2B activity raises IFNLR1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without GRAMD2B | 0.001 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[KCNK1]] | B | KCNK1 activity raises IFNLR1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without KCNK1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[HS3ST1]] | B | HS3ST1 activity raises IFNLR1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.18× lower at baseline in the lines without HS3ST1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[DAPP1]] | B | DAPP1 activity raises IFNLR1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.50× lower at baseline in the lines without DAPP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[TMEM154]] | B | TMEM154 activity raises IFNLR1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without TMEM154 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[TOP2A]] | B | TOP2A activity raises IFNLR1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASAL1]] | B | RASAL1 activity raises IFNLR1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.86× lower at baseline in the lines without RASAL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[FBLIM1]] | B | FBLIM1 activity raises IFNLR1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without FBLIM1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[JUP]] | B | JUP activity raises IFNLR1's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without JUP | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ADGRF1]] | B | ADGRF1 activity strengthens IFNLR1's drug response | lines that do not express ADGRF1 (17) vs lines expressing it (13) | the lines without ADGRF1 respond 0.56× as strongly (z diff +2.36); strongest at Doxorubicin (hydrochloride) 5 µM: 0.48x vs 0.30x (z diff +3.4) | 0.098 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; target measured in part of the lines; artifact flags |
| [[CLDN4]] | C | CLDN4 activity raises IFNLR1's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without CLDN4 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises IFNLR1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.63× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 13, C 14. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | IFNLR1 activity raises GRAMD2B's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without IFNLR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[PROSER2]] | B | IFNLR1 activity raises PROSER2's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without IFNLR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[JUP]] | B | IFNLR1 activity raises JUP's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 3.24× lower at baseline in the lines without IFNLR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[TLDC2]] | B | IFNLR1 activity raises TLDC2's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without IFNLR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[KCNK1]] | B | IFNLR1 activity raises KCNK1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.99× lower at baseline in the lines without IFNLR1 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[RAB11FIP1]] | B | IFNLR1 activity raises RAB11FIP1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without IFNLR1 | 0.045 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[TMEM154]] | B | IFNLR1 activity raises TMEM154's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without IFNLR1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[DAPP1]] | B | IFNLR1 activity raises DAPP1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.85× lower at baseline in the lines without IFNLR1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[CCDC40]] | B | IFNLR1 activity lowers CCDC40's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.41× higher at baseline in the lines without IFNLR1 | 0.076 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[UBE2H]] | B | IFNLR1 activity raises UBE2H's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without IFNLR1 | 0.081 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| cells under [[IQ 1 (drug)]] 5 µM | B | IFNLR1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express IFNLR1 (18) vs lines expressing it (30) | the lines without IFNLR1: 0.86× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[KIAA1522]] | B | IFNLR1 activity raises KIAA1522's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without IFNLR1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 57.2); signed map (56.1, 8.3). **Vector** length 83.2, 22.6% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.8 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -10.5 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | interferon lambda receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,154,168-24,187,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRF2/12, IFNLR, IL-28R1; previously IL28RA |
| Gene groups (HGNC) | Interferon receptors |
| Reactome | 4 pathways, smallest: Interleukin-20 family signaling; Other interleukin signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IU57](https://www.uniprot.org/uniprotkb/Q8IU57) (Interferon lambda receptor 1):

> The IFNLR1/IL10RB dimer is a receptor for the cytokine ligands IFNL2 and IFNL3 and mediates their antiviral activity. The ligand/receptor complex stimulate the activation of the JAK/STAT signaling pathway leading to the expression of IFN-stimulated genes (ISG), which contribute to the antiviral state. Determines the cell type specificity of the lambda interferon action. Shows a more restricted pattern of expression in the epithelial tissues thereby limiting responses to lambda interferons …

**Summary**, from NCBI Gene [163702](https://www.ncbi.nlm.nih.gov/gene/163702):

> The protein encoded by this gene belongs to the class II cytokine receptor family. This protein forms a receptor complex with interleukine 10 receptor, beta (IL10RB). The receptor complex has been shown to interact with three closely related cytokines, including interleukin 28A (IL28A), interleukin 28B (IL28B), and interleukin 29 (IL29). The expression of all three cytokines can be induced by viral infection. The cells overexpressing this protein have been found to have enhanced responses to …

**Accessions** — [HGNC:18584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18584) · Entrez [163702](https://www.ncbi.nlm.nih.gov/gene/163702) · UniProt [Q8IU57](https://www.uniprot.org/uniprotkb/Q8IU57) · Ensembl [ENSG00000185436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185436)

## Data

Gene col 11676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11676); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11676]; `tensor/DDL_lfc|DDL_z.npy` [11676]; `embed/gene_vectors.npy` [11676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11676 or target_col == 11676). Every well: [[IFNLR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFNLR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
