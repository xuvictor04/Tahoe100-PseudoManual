---
symbol: "TMEM267"
type: "gene"
col: 7574
ensembl_id: "ENSG00000151881"
name: "transmembrane protein 267"
location: "5p12"
module: 15
arm: "+"
pooled_cpm: 36.05
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMEM267

*transmembrane protein 267* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +12.6, q 1e-33, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.361× (z -9.9, q 2e-20, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGLS-DT]] (+0.76, fdr 7e-06), [[TRAPPC13]] (+0.71, fdr 9e-06), [[STARD7-AS1]] (+0.69, fdr 7e-06); moves opposite to [[GDF11]] (-0.57, fdr 1e-04), [[USP9X]] (-0.56, fdr 3e-05), [[BCAM]] (-0.55, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +12.6 | 1e-33 | 37/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +8.4 | 9e-15 | 39/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.9 | 4e-13 | 34/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +7.1 | 2e-10 | 29/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +6.7 | 3e-09 | 31/48 (NCI-H460, Hs 766T, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.25×** | +5.9 | 3e-07 | 28/48 (NCI-H460, C-33 A, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.36×** | +5.7 | 8e-07 | 27/47 (NCI-H460, C-33 A, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +5.5 | 3e-06 | 24/47 (C-33 A, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 5e-04 | 18/47 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.4 | 6e-04 | 18/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.16× | +3.9 | 0.004 | 18/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 14/48 (C-33 A, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 13/47 (A549, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.074 | 13/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.087 | 7/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -9.9 | 2e-20 | 40/48 (PANC-1, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.588×** | -9.5 | 4e-19 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.626×** | -8.7 | 4e-16 | 27/43 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.656×** | -7.9 | 5e-13 | 30/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -7.3 | 2e-11 | 36/48 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.682×** | -7.1 | 8e-11 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.765×** | -7.1 | 1e-10 | 26/47 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.687×** | -6.1 | 6e-08 | 28/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.727×** | -6.0 | 2e-07 | 23/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.696×** | -5.9 | 2e-07 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.755×** | -5.2 | 8e-06 | 23/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -5.0 | 3e-05 | 24/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.761×** | -4.7 | 1e-04 | 21/42 (PANC-1, HT-29, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **0.794×** | -4.3 | 7e-04 | 21/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.650×** | -4.2 | 0.001 | 16/47 (SW480, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.2 | 0.001 | 17/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.006 | 15/47 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.8 | 0 | 14 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -25.0) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.273× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 39.7 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 86.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW480 (line)]] | alt | 38.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A498 (line)]] | wt | 32.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.3) ⚠ cell-cycle shift, explains ~84% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.0) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.8) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 31.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.8) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HT-29 (line)]] | alt | 38.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[LoVo (line)]] | wt | 39.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H23 (line)]] | alt | 70.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HEC-1-A (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.7) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.208× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~67% of this change |
| [[HOP62 (line)]] | alt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 40.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[KATO III (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGLS-DT]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[TRAPPC13]] | +0.71 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[STARD7-AS1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.66 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[LSM8]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PCK2]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SPAG7]] | +0.63 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[DMGDH]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC35D2]] | +0.63 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[CCZ1P1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZBTB8A]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDF11]] | -0.57 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[USP9X]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[BCAM]] | -0.55 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[HPSE]] | -0.55 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[JUNB]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[BCKDK]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[POLR2E]] | -0.51 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[ZDHHC11B]] | -0.51 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ATP7A]] | -0.51 | -0.35 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.5, 21.3); signed map (-0.5, 0.4). **Vector** length 111, 28.7% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.4 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +12.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.5 | +5.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -6.0 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.7 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.6 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.9 | -6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 267 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,444,252-43,483,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21657; previously C5orf28 |
| Matched by | ensembl_id |

UniProt [Q0VDI3](https://www.uniprot.org/uniprotkb/Q0VDI3) carries no function annotation.

**Summary**, from NCBI Gene [64417](https://www.ncbi.nlm.nih.gov/gene/64417):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26139) · Entrez [64417](https://www.ncbi.nlm.nih.gov/gene/64417) · UniProt [Q0VDI3](https://www.uniprot.org/uniprotkb/Q0VDI3) · Ensembl [ENSG00000151881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151881)

## Data

Gene col 7574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7574); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7574]; `tensor/DDL_lfc|DDL_z.npy` [7574]; `embed/gene_vectors.npy` [7574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7574 or target_col == 7574). Every well: [[TMEM267 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM267.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
