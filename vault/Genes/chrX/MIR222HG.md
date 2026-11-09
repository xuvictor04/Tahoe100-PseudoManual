---
symbol: "MIR222HG"
type: "gene"
col: 15652
ensembl_id: "ENSG00000270069"
name: "miR222/221 cluster host gene"
location: "Xp11.3"
module: 78
arm: "+"
pooled_cpm: 135.12
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# MIR222HG

*miR222/221 cluster host gene* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 2.10× (z +7.2, q 3e-10, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.453× (z -10.8, q 1e-24, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOSL1]] (+0.67, fdr 7e-06), [[DCBLD2]] (+0.66, fdr 7e-06), [[F2RL1]] (+0.65, fdr 7e-06); moves opposite to [[DHX29]] (-0.58, fdr 7e-06), [[FBXO9]] (-0.58, fdr 1e-05), [[PUS10]] (-0.57, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02595]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **2.10×** | +7.2 | 3e-10 | 40/46 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +5.2 | 5e-05 | 32/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 0.002 | 28/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +3.8 | 0.024 | 25/46 (PANC-1, HS-578T, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +3.4 | 0.085 | 26/47 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.3 | 0.098 | 25/46 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -10.8 | 1e-24 | 42/47 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -8.9 | 1e-16 | 35/42 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.399×** | -8.6 | 2e-15 | 38/46 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.441×** | -7.6 | 3e-12 | 38/48 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -7.0 | 2e-10 | 33/47 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.532×** | -5.9 | 4e-07 | 38/46 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.563×** | -5.6 | 2e-06 | 38/46 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.613×** | -4.9 | 6e-05 | 34/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.604×** | -4.9 | 7e-05 | 33/46 (SW 1271, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.615×** | -4.7 | 1e-04 | 36/47 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.651×** | -4.7 | 2e-04 | 33/48 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.660×** | -3.9 | 0.005 | 26/45 (C32, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.006 | 27/46 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.767×** | -3.6 | 0.014 | 25/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.495×** | -3.6 | 0.014 | 28/45 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.024 | 26/47 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.024 | 24/46 (NCI-H23, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.770×** | -3.3 | 0.026 | 23/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 87.5 | 0 | 8 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.503× (z -14.8) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0799× (z -14.8) |
| [[A-172 (line)]] | wt | 154 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -10.0) |
| [[C32 (line)]] | wt | 99.5 | 0 | 7 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.154× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 184 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 60.6 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 8.48× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 94.3 | 0 | 6 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.172× (z -12.0) |
| [[H4 (line)]] | wt | 280 | 0 | 5 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.4) |
| [[SW48 (line)]] | wt | 570 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -19.8) |
| [[HEC-1-A (line)]] | alt | 89.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 267 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.9) |
| [[RKO (line)]] | wt | 418 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 217 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.6) |
| [[SW480 (line)]] | alt | 145 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.260× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 263 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -15.4) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 134 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +10.5) | — |
| [[A-427 (line)]] | wt | 76.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 126 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.2) |
| [[J82 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -14.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.1) |
| [[SNU-423 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.2) |
| [[CHP-212 (line)]] | wt | 59.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0923× (z -8.7) |
| [[COLO 205 (line)]] | alt | 268 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -8.7) |
| [[HCT15 (line)]] | alt | 71.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -10.0) |
| [[HOP62 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.656× (z -10.0) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 192 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.5) |
| [[LS 180 (line)]] | wt | 87.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SNU-1 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -8.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW 1088 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0587× (z -10.1) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.0) |
| [[A549 (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 143 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSL1]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[F2RL1]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[C3orf52]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[EMP1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[VPS37B]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CORO1C]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.62 | +0.45 / +0.72 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX29]] | -0.58 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[FBXO9]] | -0.58 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[PUS10]] | -0.57 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DRAM2]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[HOXA3]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CEP57]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZNF451]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[YY1AP1]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LINC02256]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02595]] | B | LINC02595 activity raises MIR222HG's level | lines that do not express LINC02595 (9) vs lines expressing it (41) | 2.50× lower at baseline in the lines without LINC02595 | 0.036 | ⚠ within organs, on part of the lines |
| [[MIR100HG]] | B | MIR100HG activity raises MIR222HG's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without MIR100HG | 0.056 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[LINC01204]] | B | LINC01204 activity raises MIR222HG's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without LINC01204 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent |
| [[CCN1]] | B | CCN1 activity raises MIR222HG's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without CCN1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[BCAR3]] | B | BCAR3 activity raises MIR222HG's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without BCAR3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises MIR222HG's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[CCDC190]] | B | CCDC190 activity raises MIR222HG's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.49× lower at baseline in the lines without CCDC190 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[FOSL1]] | B | FOSL1 activity raises MIR222HG's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 3.03× lower at baseline in the lines without FOSL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2 |
| [[OSBPL3]] | C | OSBPL3 activity raises MIR222HG's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 7.05× lower at baseline in the lines without OSBPL3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, 6.3); signed map (6.3, 44.4). **Vector** length 127, 45.6% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +2.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.4 | +2.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.2 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.3 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -6.3 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.9 | -5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.8 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.8 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | miR222/221 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xp11.3 — chrX:45,745,211-45,851,567 (-) |
| Ensembl biotype | lncRNA |
| Also known as | Lnc-Ang362; previously LINC02595 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [104457406](https://www.ncbi.nlm.nih.gov/gene/104457406):

> Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49555) · Entrez [104457406](https://www.ncbi.nlm.nih.gov/gene/104457406) · Ensembl [ENSG00000270069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270069)

## Data

Gene col 15652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15652); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15652]; `tensor/DDL_lfc|DDL_z.npy` [15652]; `embed/gene_vectors.npy` [15652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15652 or target_col == 15652). Every well: [[MIR222HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR222HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
