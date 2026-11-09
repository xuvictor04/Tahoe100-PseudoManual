---
symbol: "KREMEN1"
type: "gene"
col: 11450
ensembl_id: "ENSG00000183762"
name: "kringle containing transmembrane protein 1"
location: "22q12.1"
module: 100
arm: "+"
pooled_cpm: 24.18
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# KREMEN1

*kringle containing transmembrane protein 1* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.56× (z +8.0, q 7e-13, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.427× (z -21.6, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC29A4]] (+0.62, fdr 1e-05), [[STX2]] (+0.62, fdr 3e-05), [[RIMS3]] (+0.61, fdr 3e-05); moves opposite to [[MCTS1]] (-0.50, fdr 2e-04), [[MCPH1]] (-0.50, fdr 1e-04), [[MRPS16]] (-0.49, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[L1CAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 7e-13 | 28/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.9 | 2e-04 | 21/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 2e-04 | 15/46 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +4.8 | 2e-04 | 18/45 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 3e-04 | 20/45 (H4, HOP62, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.6 | 3e-04 | 10/31 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +4.6 | 3e-04 | 13/46 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.002 | 17/44 (SW1417, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +4.0 | 0.003 | 17/45 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.0 | 0.003 | 19/46 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 14/46 (KATO III, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.7 | 0.010 | 8/46 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.7 | 0.010 | 9/45 (A-427, HCT15, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.017 | 16/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.022 | 8/46 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.023 | 5/46 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.024 | 12/46 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.024 | 4/46 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.050 | 9/43 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.060 | 3/46 (A498, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.427×** | -21.6 | 0e+00 | 39/45 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -18.0 | 0e+00 | 40/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -17.2 | 0e+00 | 43/46 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.489×** | -12.9 | 9e-36 | 35/46 (COLO 205, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -12.3 | 1e-32 | 37/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -11.3 | 2e-27 | 33/45 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -10.5 | 7e-24 | 34/46 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -9.9 | 5e-21 | 35/46 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -9.8 | 7e-21 | 28/42 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -8.4 | 2e-15 | 27/46 (SW48, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -8.4 | 2e-15 | 30/46 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.645×** | -7.9 | 2e-13 | 28/46 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -7.4 | 4e-12 | 24/46 (SW480, SW 1088, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -7.4 | 6e-12 | 28/46 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -7.3 | 1e-11 | 29/45 (A-172, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.689×** | -4.8 | 6e-05 | 15/46 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.788×** | -4.0 | 0.002 | 15/46 (NCI-H23, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.809×** | -3.8 | 0.004 | 15/46 (RPMI-7951, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -22.3) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.2) |
| [[A-172 (line)]] | wt | 29.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -26.3) |
| [[A549 (line)]] | wt | 18.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.5) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -18.9) |
| [[KATO III (line)]] | alt | 25.7 | 3 (2 ⚠) | 2 | [[Belinostat (drug)]] 5 µM 3.65× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.64× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.0) |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.6) |
| [[A-427 (line)]] | wt | 23.9 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -22.2) |
| [[HT-29 (line)]] | alt | 14.4 | 3 (2 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 4.99× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.60× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.7) |
| [[J82 (line)]] | alt | 14.3 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0613× (z -16.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0826× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0912× (z -15.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -14.8) |
| [[SW480 (line)]] | alt | 99.7 | 1 | 3 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.13× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.306× (z -9.9) |
| [[H4 (line)]] | wt | 18.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0637× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0857× (z -11.7) |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -9.4) |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -18.0) |
| [[A498 (line)]] | wt | 25.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.6) |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -18.7) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.220× (z -10.0) |
| [[LoVo (line)]] | wt | 20.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 7.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 7.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.3) |
| [[PANC-1 (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -19.3) |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0873× (z -9.5) |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC29A4]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[STX2]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[RIMS3]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CABLES2]] | +0.60 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CIB2]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SNN]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NTAN1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GET1]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[GNB2]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 | pathway: Signaling by WNT |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.50 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[MCPH1]] | -0.50 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[MRPS16]] | -0.49 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[KICS2]] | -0.49 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[SH2D4A]] | -0.49 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[COX18]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ITPRIPL2]] | -0.48 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ST7L]] | -0.48 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ERAL1]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[MZF1-AS1]] | -0.48 | -0.39 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[L1CAM]] | B | L1CAM activity raises KREMEN1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without L1CAM | 0.055 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[MAP2K1]] | B | MAP2K1 activity lowers KREMEN1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TTLL7]] | B | TTLL7 activity weakens KREMEN1's drug response | lines that do not express TTLL7 (9) vs lines expressing it (37) | the lines without TTLL7 respond 1.41× as strongly (z diff -1.51); strongest at Homoharringtonine 0.5 µM: 0.20x vs 0.40x (z diff -4.0) | 0.063 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.0, 0.0); signed map (-39.2, -3.5). **Vector** length 72.9, 14.2% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | kringle containing transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:29,073,035-29,168,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KRM1; previously KREMEN |
| Gene groups (HGNC) | Kringle domain containing |
| Reactome | 6 pathways, smallest: Signaling by LRP5 mutants; Negative regulation of TCF-dependent signaling by WNT ligand antagonists; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MU8](https://www.uniprot.org/uniprotkb/Q96MU8) (Kremen protein 1):

> Receptor for Dickkopf proteins. Cooperates with DKK1/2 to inhibit Wnt/beta-catenin signaling by promoting the endocytosis of Wnt receptors LRP5 and LRP6. In the absence of DKK1, potentiates Wnt-beta-catenin signaling by maintaining LRP5 or LRP6 at the cell membrane. Can trigger apoptosis in a Wnt-independent manner and this apoptotic activity is inhibited upon binding of the ligand DKK1. Plays a role in limb development; attenuates Wnt signaling in the developing limb to allow normal limb …

**Summary**, from NCBI Gene [83999](https://www.ncbi.nlm.nih.gov/gene/83999):

> This gene encodes a high-affinity dickkopf homolog 1 (DKK1) transmembrane receptor that functionally cooperates with DKK1 to block wingless (WNT)/beta-catenin signaling. The encoded protein is a component of a membrane complex that modulates canonical WNT signaling through lipoprotein receptor-related protein 6 (LRP6). It contains extracellular kringle, WSC, and CUB domains. Mutations in this gene result in ectodermal dysplasia. This protein has also been found to be a functional receptor for …

**Accessions** — [HGNC:17550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17550) · Entrez [83999](https://www.ncbi.nlm.nih.gov/gene/83999) · UniProt [Q96MU8](https://www.uniprot.org/uniprotkb/Q96MU8) · Ensembl [ENSG00000183762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183762)

## Data

Gene col 11450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11450); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11450]; `tensor/DDL_lfc|DDL_z.npy` [11450]; `embed/gene_vectors.npy` [11450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11450 or target_col == 11450). Every well: [[KREMEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KREMEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
