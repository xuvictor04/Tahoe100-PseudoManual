---
symbol: "PLSCR4"
type: "gene"
col: 3576
ensembl_id: "ENSG00000114698"
name: "phospholipid scramblase 4"
location: "3q24"
module: 8
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 39
n_dd_up: 18
n_dd_down: 39
n_dd_up_clean: 17
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PLSCR4

*phospholipid scramblase 4* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +7.8, q 5e-12, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.244× (z -13.3, q 7e-38, down in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.346× (z -10.0, q 1e-21, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A1]] (+0.58, fdr 1e-05), [[SEC16B]] (+0.57, fdr 2e-05), [[PLA2R1]] (+0.57, fdr 1e-05); moves opposite to [[ST3GAL3]] (-0.46, fdr 9e-05), [[PARVB]] (-0.46, fdr 4e-05), [[FAM86DP-1]] (-0.44, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[IL7]] → it (grade B ⚠); 12 go from it, the strongest it → [[CARMIL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.8 | 5e-12 | 31/37 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +7.1 | 3e-10 | 30/36 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.005 | 16/36 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.011 | 16/37 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.011 | 17/36 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.011 | 16/36 (HOP62, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.017 | 15/36 (Hs 766T, A-172, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.022 | 11/37 (AsPC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.023 | 16/36 (LoVo, NCI-H2347, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.03×** | +3.5 | 0.025 | 14/36 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.027 | 12/36 (LoVo, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.051 | 10/36 (LoVo, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.051 | 12/36 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.91×** | +3.2 | 0.051 | 10/33 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.070 | 11/37 (BT-474, SW 900, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.244×** | -13.3 | 7e-38 | 31/35 (AsPC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.397×** | -12.3 | 2e-32 | 29/36 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.273×** | -12.3 | 2e-32 | 32/36 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.287×** | -11.8 | 7e-30 | 34/36 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.323×** | -10.3 | 1e-22 | 28/36 (A549, Panc 03.27, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.346×** | -10.0 | 1e-21 | 29/35 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.438×** | -7.8 | 6e-13 | 26/36 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.456×** | -7.4 | 9e-12 | 28/36 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.469×** | -7.1 | 6e-11 | 24/36 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.477×** | -7.0 | 2e-10 | 27/36 (H4, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.497×** | -6.6 | 2e-09 | 25/36 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.502×** | -6.5 | 4e-09 | 28/36 (H4, HT-29, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.274×** | -6.4 | 7e-09 | 23/36 (A498, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.545×** | -5.7 | 4e-07 | 24/36 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.666×** | -5.4 | 2e-06 | 24/37 (HT-29, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.335×** | -5.4 | 2e-06 | 23/35 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -5.1 | 1e-05 | 24/35 (A498, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.583×** | -5.1 | 1e-05 | 21/36 (HT-29, H4, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.360×** | -5.0 | 1e-05 | 22/36 (H4, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.475×** | -5.0 | 2e-05 | 22/37 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.583×** | -4.8 | 4e-05 | 21/36 (H4, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.389×** | -4.7 | 8e-05 | 21/36 (Panc 03.27, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.601×** | -4.6 | 1e-04 | 24/37 (CFPAC-1, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 25.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -17.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.166× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 40.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.201× (z -10.4) |
| [[A498 (line)]] | wt | 28.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -17.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.218× (z -10.4) |
| [[COLO 205 (line)]] | alt | 39.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -19.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0359× (z -15.8) |
| [[LoVo (line)]] | wt | 29.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -19.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0338× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.2) |
| [[H4 (line)]] | wt | 22.5 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0828× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0813× (z -10.7) |
| [[A549 (line)]] | wt | 24.8 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0509× (z -15.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.137× (z -10.6) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 38.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.94× (z +9.3) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -9.5) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0959× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.120× (z -8.7) |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -11.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[BT-474 (line)]] | alt | 6.25 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0494× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.214× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SEC16B]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PLA2R1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MMP7]] | +0.56 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[SCIN]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[IFNGR1]] | +0.55 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[SIDT1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[STEAP4]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[GPR37]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[IL7]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[PLAC8]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[MUC16]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.46 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[PARVB]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[FAM86DP-1]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PRKAR1B]] | -0.42 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[EEFSEC]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[XXYLT1]] | -0.42 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[PLEKHH1]] | -0.41 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[GOLGA1]] | -0.41 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[DDX50]] | -0.41 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL7]] | B | IL7 activity raises PLSCR4's level | lines that do not express IL7 (7) vs lines expressing it (43) | 4.61× lower at baseline in the lines without IL7 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[CARMIL1]] | B | CARMIL1 activity raises PLSCR4's level | lines that do not express CARMIL1 (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without CARMIL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SYNJ2, SLC22A15, MYO1D; maybe low, not absent |
| [[APOL1]] | B | APOL1 activity raises PLSCR4's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without APOL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[PDLIM1]] | B | PDLIM1 activity raises PLSCR4's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without PDLIM1 | 0.030 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[DAPK1]] | B | DAPK1 activity raises PLSCR4's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without DAPK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[SPTLC3]] | B | SPTLC3 activity raises PLSCR4's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without SPTLC3 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[MMP7]] | B | MMP7 activity raises PLSCR4's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.64× lower at baseline in the lines without MMP7 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[ARSL]] | B | ARSL activity raises PLSCR4's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without ARSL | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[PLD1]] | B | PLD1 activity raises PLSCR4's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 3.71× lower at baseline in the lines without PLD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[GPR37]] | C | GPR37 activity raises PLSCR4's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without GPR37 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARMIL1]] | B | PLSCR4 activity raises CARMIL1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without PLSCR4 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[MTUS1]] | B | PLSCR4 activity raises MTUS1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without PLSCR4 | 0.006 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[PDLIM1]] | B | PLSCR4 activity raises PDLIM1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PLSCR4 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[DPP4]] | B | PLSCR4 activity raises DPP4's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without PLSCR4 | 0.030 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[PLEKHG6]] | B | PLSCR4 activity raises PLEKHG6's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without PLSCR4 | 0.035 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[SMPDL3A]] | B | PLSCR4 activity raises SMPDL3A's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without PLSCR4 | 0.044 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[IFNGR1]] | B | PLSCR4 activity raises IFNGR1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without PLSCR4 | 0.054 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[SCARB2]] | B | PLSCR4 activity raises SCARB2's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without PLSCR4 | 0.063 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[MAPRE2]] | B | PLSCR4 activity raises MAPRE2's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without PLSCR4 | 0.082 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[AFF1]] | B | PLSCR4 activity raises AFF1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without PLSCR4 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[PON3]] | B | PLSCR4 activity raises PON3's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without PLSCR4 | 0.086 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[MBNL1]] | B | PLSCR4 activity raises MBNL1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.24× lower at baseline in the lines without PLSCR4 | 0.099 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 53.6); signed map (62.1, 0.1). **Vector** length 84.2, 19.5% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -11.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.6 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid scramblase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:146,192,335-146,251,179 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipid scramblases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRQ2](https://www.uniprot.org/uniprotkb/Q9NRQ2) (Phospholipid scramblase 4):

> Catalyzes metal ion-induced ATP-independent rapid bidirectional and non-specific movement of phospholipids (lipid scrambling or lipid flip-flop) between the inner and outer leaflet of the plasma membrane and participates in the redistribution of phospholipids between membrane leaflets. Metal ions bind to the calcium-binding site and induce conformation change in the protein. Has a greater affi nity for Ca(2+) than Mg(2+) and Zn(2+).

**Summary**, from NCBI Gene [57088](https://www.ncbi.nlm.nih.gov/gene/57088):

> Enables CD4 receptor binding activity; enzyme binding activity; and phospholipid scramblase activity. Involved in calcium activated phosphatidylcholine scrambling and calcium activated phosphatidylserine scrambling. Located in nucleus and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16497) · Entrez [57088](https://www.ncbi.nlm.nih.gov/gene/57088) · UniProt [Q9NRQ2](https://www.uniprot.org/uniprotkb/Q9NRQ2) · Ensembl [ENSG00000114698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114698)

## Data

Gene col 3576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3576); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3576]; `tensor/DDL_lfc|DDL_z.npy` [3576]; `embed/gene_vectors.npy` [3576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3576 or target_col == 3576). Every well: [[PLSCR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLSCR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
