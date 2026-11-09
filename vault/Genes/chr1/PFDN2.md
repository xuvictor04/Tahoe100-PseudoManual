---
symbol: "PFDN2"
type: "gene"
col: 6705
ensembl_id: "ENSG00000143256"
name: "prefoldin subunit 2"
location: "1q23.3"
module: 227
arm: "+"
pooled_cpm: 98.7
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# PFDN2

*prefoldin subunit 2* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +9.2, q 2e-17, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.79× (z +5.5, q 4e-06, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.714× (z -4.4, q 0.005, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6-1]] (+0.62, fdr 1e-05), [[ARHGEF2]] (+0.59, fdr 1e-05), [[GPAT3]] (+0.59, fdr 1e-05); moves opposite to [[ADI1]] (-0.61, fdr 1e-05), [[HMGN2]] (-0.60, fdr 3e-05), [[CUL4B]] (-0.56, fdr 1e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.66×** | +9.2 | 2e-17 | 45/49 (HOP62, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.47×** | +8.2 | 8e-14 | 39/43 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.26×** | +7.7 | 4e-12 | 46/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.02×** | +6.6 | 5e-09 | 43/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.95×** | +5.8 | 7e-07 | 39/45 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.5 | 4e-06 | 41/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.82×** | +5.4 | 5e-06 | 42/47 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +5.1 | 2e-05 | 46/49 (NCI-H1573, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 40/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.62×** | +4.5 | 3e-04 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.60×** | +4.4 | 4e-04 | 34/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +4.3 | 6e-04 | 43/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.88×** | +4.3 | 9e-04 | 44/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 35/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.9 | 0.004 | 28/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +3.7 | 0.006 | 27/48 (C32, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.014 | 31/48 (SW 900, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.01×** | +3.4 | 0.018 | 36/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.023 | 37/48 (BT-474, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.026 | 36/49 (NCI-H460, NCI-H1792, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.027 | 29/47 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.033 | 31/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.033 | 38/48 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.051 | 29/47 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +3.0 | 0.054 | 32/48 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.714×** | -4.4 | 0.005 | 39/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.608×** | -4.3 | 0.005 | 37/50 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.628×** | -4.2 | 0.005 | 37/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.685×** | -3.6 | 0.053 | 29/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.064 | 29/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.678×** | -3.4 | 0.070 | 34/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.526× | -3.2 | 0.13 | 32/50 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.3 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.32× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 62.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 103 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +13.0) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1573 (line)]] | alt | 92.7 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.02× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.582× (z -15.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.336× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 72.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 210 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 53.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.51× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HCT15 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 91.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 72.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.77× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.614× (z -11.0) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-1 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.80× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6-1]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ARHGEF2]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GPAT3]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[STK4]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SPIRE1]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CSGALNACT2]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CORO2B]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[KCTD20]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TMEM41B]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RSKR]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.56 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CUTC]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.60 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[CUL4B]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[JADE2]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SP1]] | -0.56 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[CASD1]] | -0.54 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[CILK1]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[RAB14]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NXT2]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[HFE]] | -0.54 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[WBP11]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ZNF436]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PFDN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises PFDN2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[IL13RA2]] | B | IL13RA2 activity raises PFDN2's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.47× lower at baseline in the lines without IL13RA2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.0, 3.6); signed map (-1.8, 47.6). **Vector** length 90.6, 37.9% of its response variance represented; |z| ≥ 3 in 1,343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +0.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | prefoldin subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,100,556-161,118,055 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Prefoldin subunits; Prefoldin-like complex |
| Reactome | 4 pathways, smallest: Prefoldin mediated transfer of substrate  to CCT/TriC; Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHV9](https://www.uniprot.org/uniprotkb/Q9UHV9) (Prefoldin subunit 2):

> Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins.

**Summary**, from NCBI Gene [5202](https://www.ncbi.nlm.nih.gov/gene/5202):

> This gene encodes a member of the prefoldin beta subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8867) · Entrez [5202](https://www.ncbi.nlm.nih.gov/gene/5202) · UniProt [Q9UHV9](https://www.uniprot.org/uniprotkb/Q9UHV9) · Ensembl [ENSG00000143256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143256)

## Data

Gene col 6705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6705); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6705]; `tensor/DDL_lfc|DDL_z.npy` [6705]; `embed/gene_vectors.npy` [6705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6705 or target_col == 6705). Every well: [[PFDN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFDN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
