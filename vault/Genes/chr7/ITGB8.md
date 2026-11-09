---
symbol: "ITGB8"
type: "gene"
col: 2677
ensembl_id: "ENSG00000105855"
name: "integrin subunit beta 8"
location: "7p21.1"
module: 143
arm: "+"
pooled_cpm: 74.99
n_lines_expressing: 33
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ITGB8

*integrin subunit beta 8* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +8.8, q 6e-16, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.287× (z -14.6, q 1e-45, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MACC1]] (+0.60, fdr 1e-05), [[ARHGAP42]] (+0.59, fdr 1e-05), [[CASC9]] (+0.56, fdr 3e-05); moves opposite to [[NQO2]] (-0.65, fdr 1e-05), [[PKD1P6]] (-0.62, fdr 1e-05), [[AZIN2]] (-0.56, fdr 4e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[EPIC1]] → it (grade B ⚠); 17 go from it, the strongest it → [[INPP4B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +8.8 | 6e-16 | 15/31 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +8.5 | 4e-15 | 19/31 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.2 | 9e-08 | 15/27 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +5.2 | 3e-05 | 14/32 (BT-474, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.5 | 7e-04 | 14/31 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.002 | 15/33 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.95×** | +4.1 | 0.003 | 16/33 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.022 | 16/31 (BT-474, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.6 | 0.022 | 14/32 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.4 | 0.039 | 9/28 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.042 | 15/31 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.042 | 11/30 (A498, Hs 766T, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.2 | 0.068 | 10/31 (A498, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.287×** | -14.6 | 1e-45 | 28/31 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.320×** | -13.4 | 2e-38 | 26/31 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.341×** | -12.6 | 4e-34 | 28/31 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.358×** | -12.0 | 3e-31 | 26/31 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.439×** | -9.6 | 6e-20 | 26/31 (C32, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.433×** | -8.4 | 3e-15 | 23/31 (SW1417, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.501×** | -8.1 | 5e-14 | 21/31 (C32, SW1417, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -7.3 | 2e-11 | 24/31 (C32, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.577×** | -6.4 | 8e-09 | 20/30 (SW480, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.596×** | -6.1 | 7e-08 | 21/31 (C32, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.410×** | -5.5 | 2e-06 | 22/31 (SW1417, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.728×** | -5.2 | 7e-06 | 19/31 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.491×** | -4.4 | 6e-04 | 20/31 (C32, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.697×** | -4.2 | 1e-03 | 21/31 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.609×** | -4.1 | 0.001 | 18/31 (NCI-H2030, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.006 | 18/31 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.015 | 15/32 (SW1417, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.573×** | -3.4 | 0.020 | 17/31 (C32, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.591×** | -3.2 | 0.037 | 15/31 (C32, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.044 | 13/31 (HEC-1-A, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 319 | 0 | 32 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0872× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.4) |
| [[SW1417 (line)]] | alt | 155 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.211× (z -12.6) |
| [[BT-474 (line)]] | alt | 42.5 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +18.8) | [[Belinostat (drug)]] 5 µM 0.104× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 217 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.242× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 649 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0487× (z -25.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0884× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 161 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.143× (z -16.2) |
| [[COLO 205 (line)]] | alt | 82.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0760× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0994× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 63.3 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.106× (z -12.4) |
| [[SW48 (line)]] | wt | 72.8 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.178× (z -9.1) |
| [[SW480 (line)]] | alt | 58.2 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.177× (z -13.0) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.188× (z -9.9) |
| [[SW 900 (line)]] | alt | 57.6 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0864× (z -14.3) |
| [[A-172 (line)]] | wt | 22.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +18.3) | — |
| [[A498 (line)]] | wt | 25.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +23.0) | — |
| [[NCI-H2030 (line)]] | alt | 67.1 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.155× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.180× (z -9.9) |
| [[H4 (line)]] | wt | 39.4 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 26.3× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 26.3× (z +12.9) | — |
| [[KATO III (line)]] | alt | 84.9 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.194× (z -11.1) |
| [[LoVo (line)]] | wt | 22.4 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 12.2× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 36.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +23.4) | — |
| [[HT-29 (line)]] | alt | 62.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 30.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 55.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +9.2) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -8.5) |
| [[AN3 CA (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0835× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 19.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 14.3× (z +10.0) | — |
| [[A-427 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACC1]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CASC9]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CILK1]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[STAT5A]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[PTPRK]] | +0.54 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[GUCY1B2]] | +0.53 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[RARRES1]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[NFKB1]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[PLPP3]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.52 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[LEPROT]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NQO2]] | -0.65 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PKD1P6]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[AZIN2]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DNASE1L1]] | -0.55 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PWWP3A]] | -0.55 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ITGB1BP1]] | -0.54 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SS18L1]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[KCTD7]] | -0.53 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[BAHD1]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[FLYWCH1]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SGTB]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPIC1]] | B | EPIC1 activity weakens ITGB8's drug response | lines that do not express EPIC1 (16) vs lines expressing it (15) | the lines without EPIC1 respond 1.32× as strongly (z diff -1.41); strongest at Auranofin 5 µM: 0.29x vs 0.66x (z diff -5.1) | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1; target measured in part of the lines; artifact flags |
| [[LOXL4]] | B | LOXL4 activity raises ITGB8's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LOXL4 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[DPP4]] | B | DPP4 activity raises ITGB8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without DPP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[ANK3]] | B | ANK3 activity raises ITGB8's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.62× lower at baseline in the lines without ANK3 | 0.023 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[MACC1]] | B | MACC1 activity raises ITGB8's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.76× lower at baseline in the lines without MACC1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[VNN1]] | B | VNN1 activity raises ITGB8's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without VNN1 | 0.029 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[RBPMS]] | B | RBPMS activity raises ITGB8's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without RBPMS | 0.067 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises ITGB8's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without MTUS1-DT | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[FRK]] | C | FRK activity raises ITGB8's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.05× lower at baseline in the lines without FRK | 0.004 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP; co-absent with the target |
| [[SHROOM3]] | C | SHROOM3 activity raises ITGB8's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.70× lower at baseline in the lines without SHROOM3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INPP4B]] | B | ITGB8 activity raises INPP4B's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without ITGB8 | 0.004 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[WDR41]] | B | ITGB8 activity lowers WDR41's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without ITGB8 | 0.011 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[MACC1]] | B | ITGB8 activity raises MACC1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without ITGB8 | 0.014 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[ARHGAP42]] | B | ITGB8 activity raises ARHGAP42's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without ITGB8 | 0.019 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[ITGB1BP1]] | B | ITGB8 activity lowers ITGB1BP1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.32× higher at baseline in the lines without ITGB8 | 0.025 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[ARHGAP42]] | B | ITGB8 activity strengthens ARHGAP42's drug response | lines that do not express ITGB8 (11) vs lines expressing it (25) | the lines without ITGB8 respond 0.71× as strongly (z diff +1.75); strongest at Idarubicin (hydrochloride) 5 µM: 0.74x vs 0.49x (z diff +4.1) | 0.026 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5; target measured in part of the lines; artifact flags |
| [[DPP4]] | B | ITGB8 activity raises DPP4's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 3.09× lower at baseline in the lines without ITGB8 | 0.027 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[TBCEL]] | B | ITGB8 activity lowers TBCEL's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.65× higher at baseline in the lines without ITGB8 | 0.034 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[OGG1]] | B | ITGB8 activity lowers OGG1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without ITGB8 | 0.050 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[MTUS1]] | B | ITGB8 activity raises MTUS1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 2.52× lower at baseline in the lines without ITGB8 | 0.055 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[LINC00662]] | B | ITGB8 activity lowers LINC00662's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.54× higher at baseline in the lines without ITGB8 | 0.061 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[FLYWCH1]] | B | ITGB8 activity lowers FLYWCH1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.22× higher at baseline in the lines without ITGB8 | 0.061 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, -2.4); signed map (46.1, 14.9). **Vector** length 122, 34.7% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -9.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -12.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -8.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:20,330,702-20,415,754 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin beta subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 7 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [P26012](https://www.uniprot.org/uniprotkb/P26012) (Integrin beta-8):

> Integrin alpha-V:beta-8 (ITGAV:ITGB8) is a receptor for fibronectin. It recognizes the sequence R-G-D in its ligands. Integrin alpha-V:beta-6 (ITGAV:ITGB6) mediates R-G-D-dependent release of transforming growth factor beta-1 (TGF-beta-1) from regulatory Latency-associated peptide (LAP), thereby playing a key role in TGF-beta-1 activation on the surface of activated regulatory T-cells (Tregs) (Probable). Required during vasculogenesis (By similarity).

**Summary**, from NCBI Gene [3696](https://www.ncbi.nlm.nih.gov/gene/3696):

> This gene is a member of the integrin beta chain family and encodes a single-pass type I membrane protein with a VWFA domain and four cysteine-rich repeats. This protein noncovalently binds to an alpha subunit to form a heterodimeric integrin complex. In general, integrin complexes mediate cell-cell and cell-extracellular matrix interactions and this complex plays a role in human airway epithelial proliferation. Alternatively spliced variants which encode different protein isoforms have been …

**Accessions** — [HGNC:6163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6163) · Entrez [3696](https://www.ncbi.nlm.nih.gov/gene/3696) · UniProt [P26012](https://www.uniprot.org/uniprotkb/P26012) · Ensembl [ENSG00000105855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105855)

## Data

Gene col 2677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2677); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2677]; `tensor/DDL_lfc|DDL_z.npy` [2677]; `embed/gene_vectors.npy` [2677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2677 or target_col == 2677). Every well: [[ITGB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
