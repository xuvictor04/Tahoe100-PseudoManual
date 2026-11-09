---
symbol: "ELOVL7"
type: "gene"
col: 8895
ensembl_id: "ENSG00000164181"
name: "ELOVL fatty acid elongase 7"
location: "5q12.1"
module: 14
arm: "+"
pooled_cpm: 48.89
n_lines_expressing: 39
n_dd_up: 35
n_dd_down: 14
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ELOVL7

*ELOVL fatty acid elongase 7* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.52× (z +28.5, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.615× (z -6.5, q 3e-08, down in 22 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.694× (z -4.9, q 1e-04, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPAMD8]] (+0.68, fdr 7e-06), [[STX11]] (+0.67, fdr 1e-05), [[TRIM36]] (+0.66, fdr 7e-06); moves opposite to [[TOMM70]] (-0.51, fdr 4e-05), [[LAS1L]] (-0.49, fdr 5e-05), [[IPO11]] (-0.49, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[GCH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.52×** | +28.5 | 0e+00 | 37/37 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.43×** | +15.9 | 0e+00 | 33/37 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +12.5 | 2e-33 | 27/37 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +12.4 | 4e-33 | 33/37 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.52×** | +12.3 | 6e-33 | 34/37 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.76×** | +10.9 | 1e-25 | 28/38 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.8 | 8e-17 | 28/36 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +8.5 | 1e-15 | 29/37 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +7.3 | 2e-11 | 27/36 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.3 | 2e-11 | 22/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +7.2 | 3e-11 | 27/36 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +6.3 | 1e-08 | 23/37 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.6 | 9e-07 | 23/36 (LS 180, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +4.7 | 1e-04 | 23/36 (HT-29, H4, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 1e-04 | 19/37 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 1e-04 | 19/37 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 17/38 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -6.5 | 3e-08 | 22/35 (A549, BT-474, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -6.1 | 2e-07 | 22/29 (NCI-H1573, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -5.5 | 9e-06 | 21/32 (SW1417, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.694×** | -4.9 | 1e-04 | 24/36 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.712×** | -4.6 | 5e-04 | 22/37 (A-172, BT-474, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.800×** | -4.3 | 0.002 | 16/37 (A549, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.745×** | -4.0 | 0.006 | 15/37 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.013 | 14/36 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.775×** | -3.4 | 0.037 | 16/37 (A-172, J82, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.037 | 11/37 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.780×** | -3.4 | 0.041 | 10/37 (J82, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.623×** | -3.3 | 0.041 | 16/35 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.066 | 12/36 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.799×** | -3.0 | 0.095 | 12/37 (SW 1271, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.3 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +24.9) | — |
| [[BT-474 (line)]] | alt | 50.9 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 48.2 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +18.8) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 50.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +26.0) | — |
| [[NCI-H1573 (line)]] | alt | 92.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.87× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.0528× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 118 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +18.1) | — |
| [[A498 (line)]] | wt | 61.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +21.6) | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 128 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 80.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +28.8) | — |
| [[SW480 (line)]] | alt | 28.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +19.5) | — |
| [[A-172 (line)]] | wt | 44.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +19.5) | — |
| [[HEC-1-A (line)]] | alt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 42.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 109 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.3× (z +19.6) | — |
| [[KATO III (line)]] | alt | 51.2 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +18.9) | — |
| [[SW 900 (line)]] | alt | 18.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +19.9) | — |
| [[A-427 (line)]] | wt | 80.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 150 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 169 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +19.3) | — |
| [[J82 (line)]] | alt | 66.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +20.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.6) | — |
| [[RKO (line)]] | wt | 50.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 91.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 12.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -12.6) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 106 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.102× (z -8.6) |
| [[AN3 CA (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPAMD8]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[STX11]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TRIM36]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SLC30A4]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.64 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[SERPINB7]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[RASGRP1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[RPLP0P2]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[NTN1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PDLIM3]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[RNF223]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM70]] | -0.51 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[LAS1L]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[IPO11]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[IVD]] | -0.49 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CNOT7]] | -0.48 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[TOMM40]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[XPO7]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TRRAP]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GTF3C2]] | -0.47 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[COASY]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[YLPM1]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCH1]] | B | ELOVL7 activity raises GCH1's level | lines that do not express ELOVL7 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without ELOVL7 | 0.007 | ⚠ within organs, on part of the lines; also absent: KRT86; maybe low, not absent |
| [[USP12]] | B | ELOVL7 activity lowers USP12's level | lines that do not express ELOVL7 (11) vs lines expressing it (39) | 1.12× higher at baseline in the lines without ELOVL7 | 0.082 | ⚠ within organs, on part of the lines; also absent: KRT86; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, -0.0); signed map (39.9, 9.8). **Vector** length 95.1, 26.4% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +8.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +15.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +1.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.0 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:60,751,791-60,844,274 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23563 |
| Gene groups (HGNC) | ELOVL fatty acid elongase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L3X0](https://www.uniprot.org/uniprotkb/A1L3X0) (Very long chain fatty acid elongase 7):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme with higher activity toward C18 acyl-CoAs, especially C18:3(n-3) acyl-CoAs and C18:3(n-6)-CoAs. Also active toward C20:4-, C18:0-, C18:1-, C18:2- and C16:0-CoAs, and weakly toward C20:0-CoA. …

**Summary**, from NCBI Gene [79993](https://www.ncbi.nlm.nih.gov/gene/79993):

> Enables fatty acid elongase activity. Involved in fatty acid elongation, polyunsaturated fatty acid; fatty acid elongation, saturated fatty acid; and very long-chain fatty acid biosynthetic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26292) · Entrez [79993](https://www.ncbi.nlm.nih.gov/gene/79993) · UniProt [A1L3X0](https://www.uniprot.org/uniprotkb/A1L3X0) · Ensembl [ENSG00000164181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164181)

## Data

Gene col 8895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8895); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8895]; `tensor/DDL_lfc|DDL_z.npy` [8895]; `embed/gene_vectors.npy` [8895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8895 or target_col == 8895). Every well: [[ELOVL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
