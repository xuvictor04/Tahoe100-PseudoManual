---
symbol: "ZBTB4"
type: "gene"
col: 10480
ensembl_id: "ENSG00000174282"
name: "zinc finger and BTB domain containing 4"
location: "17p13.1"
module: 16
arm: "+"
pooled_cpm: 38.44
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBTB4

*zinc finger and BTB domain containing 4* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.34× (z +5.0, q 3e-04, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.77×; ⚠ cell-cycle shift, explains ~75% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.423× (z -15.3, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.669× (z -7.1, q 8e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX2]] (+0.73, fdr 7e-06), [[ZNF764]] (+0.67, fdr 7e-06), [[ZNF554]] (+0.65, fdr 1e-05); moves opposite to [[MDH2]] (-0.62, fdr 1e-05), [[NTAQ1]] (-0.62, fdr 1e-05), [[DCAF13]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.77×; ⚠ cell-cycle shift, explains ~75% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-04 | 22/48 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.057 | 21/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.32 | 13/48 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.32 | 12/48 (A-427, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.423×** | -15.3 | 0e+00 | 48/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.425×** | -15.2 | 0e+00 | 46/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.461×** | -13.7 | 2e-40 | 47/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.585×** | -9.2 | 8e-18 | 34/48 (A-427, SW48, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.706×** | -8.7 | 3e-16 | 32/48 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.606×** | -8.5 | 1e-15 | 29/48 (RPMI-7951, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.658×** | -7.1 | 7e-11 | 32/47 (HepG2/C3A, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -7.1 | 8e-11 | 30/48 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -7.0 | 2e-10 | 32/48 (MIA PaCa-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -5.6 | 1e-06 | 29/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.729×** | -5.6 | 1e-06 | 29/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.745×** | -5.2 | 7e-06 | 23/47 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.745×** | -5.2 | 7e-06 | 25/48 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.752×** | -5.1 | 2e-05 | 27/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -4.4 | 5e-04 | 19/47 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.669×** | -3.7 | 0.006 | 15/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.007 | 13/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.017 | 13/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.024 | 10/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.715×** | -3.1 | 0.042 | 14/48 (RPMI-7951, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -2.9 | 0.079 | 17/48 (A-172, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -16.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 89.7 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 42.9 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 5 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 85.6 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 76.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -16.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 47.6 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -11.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -14.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 46.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 38.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.9) ⚠ cell-cycle shift, explains ~75% of this change | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -10.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.126× (z -9.7) |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 31.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -12.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0689× (z -20.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -10.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0965× (z -10.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.274× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0528× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZNF764]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF554]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 | same gene group |
| [[MRFAP1L1]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[GAS8]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 | same gene group |
| [[EID2]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[CCDC102A]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DEDD]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF155]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH2]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[DCAF13]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PIGF]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[MTERF3]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.56 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SETD3]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NHP2]] | -0.54 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[TFRC]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[NDC1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[GK5]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.6, 9.7); signed map (8.9, -20.0). **Vector** length 97.0, 24.0% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +9.2 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.2 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | -2.7 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -7.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,459,366-7,484,263 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1538, KAISO-L1, ZNF903 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1Z0](https://www.uniprot.org/uniprotkb/Q9P1Z0) (Zinc finger and BTB domain-containing protein 4):

> Transcriptional repressor with bimodal DNA-binding specificity. Represses transcription in a methyl-CpG-dependent manner. Binds with a higher affinity to methylated CpG dinucleotides in the consensus sequence 5'-CGCG-3' but can also bind to the non-methylated consensus sequence 5'-CTGCNA-3' also known as the consensus kaiso binding site (KBS). Can also bind specifically to a single methyl-CpG pair and can bind hemimethylated DNA but with a lower affinity compared to methylated DNA. Plays a role …

**Summary**, from NCBI Gene [57659](https://www.ncbi.nlm.nih.gov/gene/57659):

> Enables several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; nucleotide binding activity; and protein homodimerization activity. Involved in DNA damage response and negative regulation of transcription by RNA polymerase II. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23847) · Entrez [57659](https://www.ncbi.nlm.nih.gov/gene/57659) · UniProt [Q9P1Z0](https://www.uniprot.org/uniprotkb/Q9P1Z0) · Ensembl [ENSG00000174282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174282)

## Data

Gene col 10480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10480); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10480]; `tensor/DDL_lfc|DDL_z.npy` [10480]; `embed/gene_vectors.npy` [10480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10480 or target_col == 10480). Every well: [[ZBTB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
