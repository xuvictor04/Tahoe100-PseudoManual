---
symbol: "TLCD4"
type: "gene"
col: 7588
ensembl_id: "ENSG00000152078"
name: "TLC domain containing 4"
location: "1p21.3"
module: 186
arm: "+"
pooled_cpm: 26.4
n_lines_expressing: 39
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# TLCD4

*TLC domain containing 4* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.91× (z +13.1, q 3e-36, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.593× (z -10.1, q 2e-21, down in 19 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.725× (z -6.5, q 1e-08, down in 18 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD4-RWDD3]] (+0.68, fdr 7e-06, ⚠ read-through risk), [[FZD3]] (+0.57, fdr 1e-05), [[ALDH9A1]] (+0.53, fdr 2e-05), [[GPC4]] (+0.51, fdr 3e-05); moves opposite to [[ENDOV]] (-0.53, fdr 4e-05), [[KATNIP]] (-0.51, fdr 2e-04), [[SMG6]] (-0.50, fdr 5e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[RASGRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +13.1 | 3e-36 | 32/36 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +12.6 | 6e-34 | 29/37 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +10.2 | 5e-22 | 22/36 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.3 | 5e-11 | 14/33 (A498, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.9 | 6e-10 | 21/36 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 16/34 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +6.2 | 4e-08 | 21/36 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +5.8 | 4e-07 | 20/36 (NCI-H2347, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 18/37 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +5.2 | 1e-05 | 14/36 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 3e-05 | 16/37 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 11/36 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 11/37 (NCI-H2347, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +4.6 | 2e-04 | 10/37 (NCI-H2347, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +4.4 | 5e-04 | 17/36 (RKO, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 5e-04 | 12/36 (LS 180, NCI-H2347, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 8e-04 | 12/36 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -10.1 | 2e-21 | 19/33 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -6.7 | 7e-09 | 19/35 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -6.5 | 1e-08 | 18/36 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -6.3 | 4e-08 | 17/36 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -6.2 | 6e-08 | 17/36 (HepG2/C3A, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -5.7 | 1e-06 | 20/36 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.754×** | -5.7 | 1e-06 | 18/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -5.2 | 1e-05 | 16/36 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.583×** | -5.2 | 1e-05 | 15/32 (NCI-H1792, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -5.0 | 3e-05 | 17/35 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.780×** | -5.0 | 3e-05 | 17/36 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -4.8 | 9e-05 | 17/35 (NCI-H2030, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.815×** | -4.1 | 0.002 | 13/36 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.003 | 12/32 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.821×** | -4.0 | 0.003 | 10/33 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -3.9 | 0.003 | 14/33 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.003 | 9/34 (SNU-423, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.9 | 1 | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.35× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 52.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A-427 (line)]] | wt | 31.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | — |
| [[LS 180 (line)]] | wt | 29.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Pyridoxine (drug)]] 0.5 µM 0.115× (z -11.9) |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | — |
| [[BT-474 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.296× (z -9.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.217× (z -9.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.229× (z -9.1) |
| [[RKO (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD4-RWDD3]] | +0.68 | +0.67 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: TLCD4-RWDD3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[FZD3]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ALDH9A1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GPC4]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PLEKHA1]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SLC35D1]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PTGFRN]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CDH24]] | +0.51 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TMEM106C]] | +0.49 | +0.40 / +0.65 | both halves | 4e-05 |  |
| [[EZH2]] | +0.49 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[GLRB]] | +0.48 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CNN3]] | +0.48 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ISOC1]] | +0.48 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOV]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KATNIP]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SMG6]] | -0.50 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[SPOUT1]] | -0.50 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[CHMP1A]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.47 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[CPTP]] | -0.46 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[IFT43]] | -0.46 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[MTERF1]] | -0.46 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ZNF765]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ATG7]] | -0.45 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[GCDH]] | -0.45 | -0.30 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TLCD4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ARHGEF26]] | C | ARHGEF26 activity raises TLCD4's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without ARHGEF26 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGRP1]] | B | TLCD4, [[TLCD4-RWDD3]] activity raises RASGRP1's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 2.08× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| [[KAT2B]] | B | TLCD4 activity raises KAT2B's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without TLCD4 | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[CLDN15]] | B | TLCD4 activity raises CLDN15's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.27× lower at baseline in the lines without TLCD4 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[DERA]] | B | TLCD4, [[TLCD4-RWDD3]] activity raises DERA's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 1.55× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| [[RAVER2]] | B | TLCD4 activity raises RAVER2's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without TLCD4 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[ADCY6]] | B | TLCD4 activity raises ADCY6's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without TLCD4 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 5 µM | B | TLCD4, [[TLCD4-RWDD3]] activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (37) | the lines without TLCD4, TLCD4-RWDD3: 0.69× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.6, -2.9); signed map (-20.7, -27.3). **Vector** length 86.5, 19.8% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +12.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +13.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:95,117,355-95,197,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31842; previously TMEM56 |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

UniProt [Q96MV1](https://www.uniprot.org/uniprotkb/Q96MV1) carries no function annotation.

**Summary**, from NCBI Gene [148534](https://www.ncbi.nlm.nih.gov/gene/148534):

> Predicted to be involved in lipid homeostasis. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26477) · Entrez [148534](https://www.ncbi.nlm.nih.gov/gene/148534) · UniProt [Q96MV1](https://www.uniprot.org/uniprotkb/Q96MV1) · Ensembl [ENSG00000152078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152078)

## Data

Gene col 7588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7588); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7588]; `tensor/DDL_lfc|DDL_z.npy` [7588]; `embed/gene_vectors.npy` [7588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7588 or target_col == 7588). Every well: [[TLCD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
