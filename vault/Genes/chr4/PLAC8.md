---
symbol: "PLAC8"
type: "gene"
col: 6972
ensembl_id: "ENSG00000145287"
name: "placenta associated 8"
location: "4q21.22"
module: 44
arm: "+"
pooled_cpm: 41.54
n_lines_expressing: 24
n_dd_up: 17
n_dd_down: 39
n_dd_up_clean: 14
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 14
direction_downstream: 6
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PLAC8

*placenta associated 8* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +9.8, q 5e-20, up in 7 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.32× (z +4.2, q 0.004, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.428× (z -9.1, q 5e-17, down in 19 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHROOM3]] (+0.70, fdr 7e-06), [[PLEKHG6]] (+0.66, fdr 1e-05), [[SORL1]] (+0.62, fdr 1e-05); moves opposite to [[CFAP20DC]] (-0.50, fdr 5e-05), [[ZNF83]] (-0.48, fdr 6e-05), [[TM4SF19]] (-0.48, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SORL1]] → it (grade B ⚠); 6 go from it, the strongest it → [[VILL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.8 | 5e-20 | 7/19 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.7 | 5e-12 | 5/17 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.1 | 6e-05 | 4/18 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.004 | 9/22 (A498, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.009 | 9/21 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.96×** | +3.7 | 0.022 | 8/20 (AsPC-1, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.027 | 10/22 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.034 | 9/22 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.045 | 10/22 (AsPC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.050 | 8/22 (AsPC-1, Panc 03.27, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.076 | 6/21 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.076 | 8/20 (AsPC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[DT-061 (drug)]] 5 µM |  | **1.75×** | +3.1 | 0.091 | 6/20 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.091 | 6/21 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.43×** | +3.0 | 0.092 | 4/21 (J82, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.092 | 10/21 (HOP62, NCI-H23, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.092 | 7/20 (AsPC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -9.1 | 5e-17 | 19/21 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -8.0 | 2e-13 | 17/21 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -7.6 | 5e-12 | 20/21 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.513×** | -7.2 | 1e-10 | 19/22 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.630×** | -7.0 | 3e-10 | 17/22 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.538×** | -6.6 | 3e-09 | 17/21 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -6.4 | 1e-08 | 16/22 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -6.3 | 2e-08 | 20/21 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -6.3 | 2e-08 | 19/21 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.604×** | -5.4 | 4e-06 | 19/22 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.619×** | -5.1 | 1e-05 | 16/21 (KATO III, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -5.1 | 2e-05 | 19/21 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.541×** | -5.1 | 2e-05 | 19/22 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -4.9 | 4e-05 | 18/22 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.632×** | -4.7 | 9e-05 | 16/21 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.637×** | -4.6 | 1e-04 | 12/21 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 1e-04 | 17/21 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.655×** | -4.5 | 2e-04 | 14/21 (CFPAC-1, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.664×** | -4.4 | 4e-04 | 10/21 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 363 | 0 | 23 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0312× (z -26.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -25.4) |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -24.5) |
| [[KATO III (line)]] | alt | 95.4 | 1 (1 ⚠) | 17 (6 ⚠) | [[Selinexor (drug)]] 5 µM 2.45× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -20.1) |
| [[PANC-1 (line)]] | alt | 91.7 | 0 | 17 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.3) |
| [[Hs 766T (line)]] | wt | 191 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 84.3 | 7 (1 ⚠) | 7 (3 ⚠) | [[Trametinib (drug)]] 0.5 µM 4.69× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.0674× (z -14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.7) |
| [[LS 180 (line)]] | wt | 79.8 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0683× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 86.0 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.213× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 88.3 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -16.6) |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0510× (z -22.1) |
| [[CFPAC-1 (line)]] | alt | 73.2 | 1 | 7 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 4.32× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.60× (z +11.6) | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -8.9) |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0629× (z -9.8) |
| [[A-172 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHROOM3]] | +0.70 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SORL1]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TJP3]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[SIDT1]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MUC1]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[UGT1A6]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TSPAN8]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CRACDL]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PTPRR]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[UGT1A1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP20DC]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ZNF83]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TM4SF19]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CORO2B]] | -0.47 | -0.39 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises PLAC8's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.57× lower at baseline in the lines without SORL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MMP28]] | B | MMP28 activity raises PLAC8's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without MMP28 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[CRACDL]] | B | CRACDL activity raises PLAC8's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.50× lower at baseline in the lines without CRACDL | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises PLAC8's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without PLEKHG6 | 0.056 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[DNAJC15]] | B | DNAJC15 activity raises PLAC8's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without DNAJC15 | 0.060 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[TJP3]] | B | TJP3 activity raises PLAC8's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without TJP3 | 0.063 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[PRR15-DT]] | B | PRR15-DT activity raises PLAC8's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.83× lower at baseline in the lines without PRR15-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[MECOM]] | B | MECOM activity raises PLAC8's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without MECOM | 0.096 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[SLC44A4]] | C | SLC44A4 activity raises PLAC8's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.83× lower at baseline in the lines without SLC44A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[C4BPB]] | C | C4BPB activity raises PLAC8's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 4.87× lower at baseline in the lines without C4BPB | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises PLAC8's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 4.74× lower at baseline in the lines without ST6GALNAC1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises PLAC8's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 3.51× lower at baseline in the lines without UGT1A6 | 0.063 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VILL]] | B | PLAC8 activity raises VILL's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without PLAC8 | 0.076 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2 |
| [[DNAJC15]] | B | PLAC8 activity raises DNAJC15's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without PLAC8 | 0.090 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2 |
| [[LINC02331]] | B | PLAC8 activity raises LINC02331's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without PLAC8 | 0.094 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2 |
| [[GPA33]] | C | PLAC8 activity raises GPA33's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 1.67× lower at baseline in the lines without PLAC8 | 0.051 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2; co-absent with the target |
| [[C4BPB]] | C | PLAC8 activity raises C4BPB's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without PLAC8 | 0.052 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2; co-absent with the target |
| [[CDH17]] | C | PLAC8 activity raises CDH17's level | lines that do not express PLAC8 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without PLAC8 | 0.084 | ⚠ within organs, on part of the lines; also absent: KISS1, TFF2, BARX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 53.1); signed map (62.1, 4.2). **Vector** length 89.1, 25.6% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.56 to 4); *Aspirin ADME* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +9.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | placenta associated 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:83,090,048-83,137,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | onzin, C15 |
| Gene groups (HGNC) | PLAC8 family |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: Formation of the nephric duct; Kidney development; Neutrophil degranulation |
| Matched by | ensembl_id |

UniProt [Q9NZF1](https://www.uniprot.org/uniprotkb/Q9NZF1) carries no function annotation.

**Summary**, from NCBI Gene [51316](https://www.ncbi.nlm.nih.gov/gene/51316):

> Predicted to enable chromatin binding activity. Predicted to be involved in positive regulation of cold-induced thermogenesis and positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within several processes, including brown fat cell differentiation; defense response to bacterium; and response to cold. Predicted to be located in azurophil granule lumen and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19254) · Entrez [51316](https://www.ncbi.nlm.nih.gov/gene/51316) · UniProt [Q9NZF1](https://www.uniprot.org/uniprotkb/Q9NZF1) · Ensembl [ENSG00000145287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145287)

## Data

Gene col 6972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6972); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6972]; `tensor/DDL_lfc|DDL_z.npy` [6972]; `embed/gene_vectors.npy` [6972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6972 or target_col == 6972). Every well: [[PLAC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
