---
symbol: "DUSP6"
type: "gene"
col: 6290
ensembl_id: "ENSG00000139318"
name: "dual specificity phosphatase 6"
location: "12q21.33"
module: 174
arm: "+"
pooled_cpm: 115.17
n_lines_expressing: 46
n_dd_up: 2
n_dd_down: 51
n_dd_up_clean: 0
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# DUSP6

*dual specificity phosphatase 6* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.65× (z +4.5, q 0.004, up in 31 of 44 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 4.08×, BT-474 3.47×, PANC-1 2.42×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (C32 4.42×, A549 4.23×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 3.68×, SW1417 3.89×; ⚠ cell-cycle shift, explains ~87% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 4.22×).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (9 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.0700× (z -21.6, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4]] (+0.78, fdr 7e-06), [[PHC2]] (+0.77, fdr 7e-06), [[ITGB5]] (+0.76, fdr 7e-06); moves opposite to [[CSDE1]] (-0.56, fdr 3e-05), [[SETD7]] (-0.56, fdr 2e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 4.08×, BT-474 3.47×, PANC-1 2.42×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (C32 4.42×, A549 4.23×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 3.68×, SW1417 3.89×; ⚠ cell-cycle shift, explains ~87% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 4.22×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.65×** | +4.5 | 0.004 | 31/44 (C32, A549, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.52×** | +3.6 | 0.077 | 22/44 (A-427, SW1417, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.28× | +3.1 | 0.32 | 23/44 (LS 180, BT-474, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.0700×** | -21.6 | 0e+00 | 45/46 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.0864×** | -21.0 | 0e+00 | 42/43 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.109×** | -19.7 | 0e+00 | 44/45 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.113×** | -18.6 | 0e+00 | 44/44 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.176×** | -18.4 | 0e+00 | 44/44 (SW480, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.141×** | -16.1 | 0e+00 | 44/44 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.167×** | -15.9 | 0e+00 | 42/43 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.161×** | -15.7 | 0e+00 | 44/45 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.286×** | -15.5 | 0e+00 | 43/44 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.286×** | -12.6 | 2e-34 | 44/44 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.241×** | -12.2 | 2e-32 | 34/40 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.302×** | -10.6 | 9e-25 | 42/44 (KATO III, HS-578T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.303×** | -9.3 | 5e-19 | 42/44 (SW480, C32, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.396×** | -8.2 | 7e-15 | 36/45 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.397×** | -8.2 | 9e-15 | 40/44 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.509×** | -8.0 | 5e-14 | 42/45 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.107×** | -7.2 | 2e-11 | 43/44 (SW480, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 240 | 0 | 24 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0187× (z -27.2) |
| [[KATO III (line)]] | alt | 129 | 0 | 23 (7 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.0671× (z -17.4) |
| [[Hs 766T (line)]] | wt | 302 | 0 | 22 (6 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0341× (z -25.0) |
| [[SNU-1 (line)]] | wt | 244 | 0 | 22 (6 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0119× (z -27.0) |
| [[C32 (line)]] | wt | 162 | 2 (1 ⚠) | 19 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.42× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.22× (z +9.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0186× (z -23.5) |
| [[HOP62 (line)]] | alt | 347 | 0 | 21 (4 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0219× (z -27.0) |
| [[SW 900 (line)]] | alt | 275 | 0 | 18 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0401× (z -24.7) |
| [[BT-474 (line)]] | alt | 69.7 | 1 | 16 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.8) | [[Trametinib (drug)]] 5 µM 0.0589× (z -14.2) |
| [[H4 (line)]] | wt | 106 | 0 | 17 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0514× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 220 | 0 | 17 (4 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.0982× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 16 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0192× (z -27.3) |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 15 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0704× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 89.3 | 0 | 15 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0637× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 14 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0864× (z -17.6) |
| [[HS-578T (line)]] | alt | 166 | 0 | 14 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0908× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 182 | 1 (1 ⚠) | 12 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Trametinib (drug)]] 0.5 µM 0.150× (z -16.5) |
| [[PANC-1 (line)]] | alt | 47.4 | 1 | 12 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.0) | [[Cobimetinib (drug)]] 0.5 µM 0.113× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 13 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0207× (z -24.5) |
| [[A-427 (line)]] | wt | 107 | 1 (1 ⚠) | 11 | [[Harringtonine (drug)]] 5 µM 3.68× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | [[Trametinib (drug)]] 5 µM 0.0362× (z -22.3) |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 12 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0628× (z -16.7) |
| [[LS 180 (line)]] | wt | 75.0 | 0 | 12 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0692× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0754× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 12 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0762× (z -16.1) |
| [[SHP-77 (line)]] | alt | 59.6 | 0 | 12 | — | [[Binimetinib (drug)]] 0.5 µM 0.104× (z -17.2) |
| [[SW1417 (line)]] | alt | 66.0 | 2 (1 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +13.7) | [[Trametinib (drug)]] 5 µM 0.150× (z -12.3) |
| [[LoVo (line)]] | wt | 89.0 | 0 | 11 | — | [[Trametinib (drug)]] 5 µM 0.0765× (z -13.9) |
| [[RKO (line)]] | wt | 101 | 0 | 11 | — | [[Cobimetinib (drug)]] 5 µM 0.0479× (z -16.4) |
| [[A-172 (line)]] | wt | 97.3 | 0 | 10 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0543× (z -16.1) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 10 | — | [[Cobimetinib (drug)]] 0.5 µM 0.105× (z -13.1) |
| [[A549 (line)]] | wt | 53.5 | 1 (1 ⚠) | 8 | [[Harringtonine (drug)]] 0.5 µM 4.23× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Trametinib (drug)]] 5 µM 0.0776× (z -13.3) |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 9 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0734× (z -12.3) |
| [[J82 (line)]] | alt | 53.7 | 0 | 9 | — | [[Trametinib (drug)]] 5 µM 0.0792× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 81.3 | 0 | 9 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0502× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 8 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0693× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.498× (z -14.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.111× (z -11.9) |
| [[SW48 (line)]] | wt | 85.3 | 0 | 8 | — | [[Trametinib (drug)]] 0.5 µM 0.165× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 6 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0377× (z -20.2) |
| [[HT-29 (line)]] | alt | 57.9 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.0928× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 72.7 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.0592× (z -15.2) |
| [[SNU-423 (line)]] | alt | 76.9 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.115× (z -13.1) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0817× (z -11.9) |
| [[SW 1088 (line)]] | alt | 111 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0375× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.140× (z -9.3) |
| [[SW 1271 (line)]] | alt | 97.9 | 0 | 2 | — | [[Trametinib (drug)]] 0.05 µM 0.123× (z -10.4) |
| [[A498 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | STRING 752 |
| [[PHC2]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[TIMP1]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[SPRED1]] | +0.74 | +0.76 / +0.78 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 450 |
| [[EGR1]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 729 |
| [[EGR3]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 572 |
| [[SPRED2]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 487 |
| [[DUSP4]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 | same gene group; pathway: ERK/MAPK targets; STRING 574 |
| [[PHLDA1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 | STRING 463 |
| [[EGR2]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 458 |
| [[SPRY2]] | +0.71 | +0.75 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 829 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SETD7]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAT]] | B | PLAT activity raises DUSP6's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without PLAT | 0.017 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[MAP2K1]] | B | MAP2K1 activity raises DUSP6's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.2% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR2E3]] | B | NR2E3 activity lowers DUSP6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.51× higher at baseline in the lines without NR2E3 | 0.060 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[EFNB2]] | B | EFNB2 activity raises DUSP6's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without EFNB2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[HEY1]] | B | HEY1 activity raises DUSP6's level | lines that do not express HEY1 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without HEY1 | 0.096 | ⚠ within organs, on part of the lines; also absent: SLC2A14, SDK2, DTX3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.1, 5.6); signed map (7.8, 48.2). **Vector** length 168, 63.3% of its response variance represented; |z| ≥ 3 in 2,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +6.1 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.9 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -16.4 | -21.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -14.6 | -18.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -13.5 | -19.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -13.5 | -18.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -13.3 | -21.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -12.9 | -16.1 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:89,347,235-89,352,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-3, PYST1 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Hallmark sets | COAGULATION, COMPLEMENT, KRAS_SIGNALING_UP |
| Reactome | 36 pathways, smallest: Signaling by MAPK mutants; ERKs are inactivated; ERK/MAPK targets |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16828](https://www.uniprot.org/uniprotkb/Q16828) (Dual specificity protein phosphatase 6):

> Dual specificity protein phosphatase, which mediates dephosphorylation and inactivation of MAP kinases. Has a specificity for the ERK family. Plays an important role in alleviating chronic postoperative pain (By similarity). Necessary for the normal dephosphorylation of the long-lasting phosphorylated forms of spinal MAPK1/3 and MAP kinase p38 induced by peripheral surgery, which drives the resolution of acute postoperative allodynia (By similarity). Also important for dephosphorylation of …

**Summary**, from NCBI Gene [1848](https://www.ncbi.nlm.nih.gov/gene/1848):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3072) · Entrez [1848](https://www.ncbi.nlm.nih.gov/gene/1848) · UniProt [Q16828](https://www.uniprot.org/uniprotkb/Q16828) · Ensembl [ENSG00000139318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139318)

## Data

Gene col 6290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6290); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6290]; `tensor/DDL_lfc|DDL_z.npy` [6290]; `embed/gene_vectors.npy` [6290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6290 or target_col == 6290). Every well: [[DUSP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
