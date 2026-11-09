---
symbol: "ETV3"
type: "gene"
col: 3870
ensembl_id: "ENSG00000117036"
name: "ETS variant transcription factor 3"
location: "1q23.1"
module: 109
arm: "+"
pooled_cpm: 79.95
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# ETV3

*ETS variant transcription factor 3* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.52× (z +14.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.593× (z -9.2, q 2e-17, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.795× (z -5.8, q 1e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.68, fdr 7e-06), [[CSRNP1]] (+0.64, fdr 7e-06), [[EGR1]] (+0.62, fdr 7e-06); moves opposite to [[TRPM7]] (-0.52, fdr 1e-05), [[ABHD18]] (-0.51, fdr 2e-05), [[CHPT1]] (-0.48, fdr 4e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LIF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.52×** | +14.7 | 0e+00 | 47/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +12.6 | 4e-34 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +11.3 | 2e-27 | 41/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +10.3 | 9e-23 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 2e-21 | 34/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.2 | 4e-18 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +9.1 | 9e-18 | 34/45 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +8.8 | 8e-17 | 35/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.3 | 2e-08 | 34/48 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +6.1 | 7e-08 | 26/48 (NCI-H460, BT-474, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +6.0 | 7e-08 | 31/48 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.28×** | +4.6 | 2e-04 | 28/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 24/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 3e-04 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.3 | 6e-04 | 22/48 (NCI-H2347, Panc 03.27, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.001 | 24/48 (C32, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.035 | 15/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.080 | 6/48 (SW1417, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -9.2 | 2e-17 | 36/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.795×** | -5.8 | 1e-06 | 27/48 (C32, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.804×** | -5.4 | 1e-05 | 28/49 (C32, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.748×** | -5.1 | 4e-05 | 25/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.761×** | -5.0 | 6e-05 | 26/47 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.755×** | -5.0 | 7e-05 | 29/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.785×** | -4.9 | 7e-05 | 30/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.778×** | -4.9 | 8e-05 | 28/50 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.833×** | -4.7 | 1e-04 | 22/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -4.6 | 2e-04 | 28/48 (NCI-H23, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.773×** | -4.5 | 4e-04 | 23/49 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.698×** | -4.2 | 0.001 | 28/48 (RPMI-7951, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.801×** | -4.1 | 0.002 | 24/48 (hTERT-HPNE, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.002 | 24/50 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.002 | 24/48 (C32, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.005 | 22/49 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.807×** | -3.7 | 0.007 | 21/48 (C32, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 142 | 16 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +20.7) | — |
| [[NCI-H2347 (line)]] | alt | 63.8 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 95.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 40.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.9 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.16× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.0) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.8) | — |
| [[SNU-423 (line)]] | alt | 47.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.5) | — |
| [[LoVo (line)]] | wt | 55.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.45× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 87.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.2) | — |
| [[J82 (line)]] | alt | 56.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +17.0) | — |
| [[LOX-IMVI (line)]] | wt | 66.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.29× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.83× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 66.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.20× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 60.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 80.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.53× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 50.0 | 0 | 2 | — | [[(S)-Crizotinib (drug)]] 0.5 µM 0.0651× (z -9.1) |
| [[SW480 (line)]] | alt | 69.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 54.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.66× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 95.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.5) | — |
| [[HCT15 (line)]] | alt | 67.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 99.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +10.7) | — |
| [[RKO (line)]] | wt | 65.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -16.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 53.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.45× (z +11.8) | — |
| [[A-427 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 185 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CSRNP1]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EGR1]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[BACH1]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[IER2]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[NES]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[EGR2]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZFP69B]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[FOSL1]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MYO10]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPM7]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ABHD18]] | -0.51 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ANP32B]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[STRN3]] | -0.48 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[BMPR1A]] | -0.48 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[CNIH4]] | -0.47 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MZT2A]] | -0.47 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ENY2]] | -0.47 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[NDUFB2]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[FBXO9]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[KIF13A]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIF]] | B | LIF activity raises ETV3's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without LIF | 0.039 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[MAP2K1]] | B | MAP2K1 activity raises ETV3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, 0.2); signed map (7.5, 29.1). **Vector** length 110, 32.9% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.53 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.52 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +14.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.0 | +4.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.5 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -3.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:157,121,191-157,138,474 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PE-1 |
| Gene groups (HGNC) | ETS transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [P41162](https://www.uniprot.org/uniprotkb/P41162) (ETS translocation variant 3):

> Transcriptional repressor that contribute to growth arrest during terminal macrophage differentiation by repressing target genes involved in Ras-dependent proliferation. Represses MMP1 promoter activity.

**Summary**, from NCBI Gene [2117](https://www.ncbi.nlm.nih.gov/gene/2117):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in cell differentiation and regulation of transcription by RNA polymerase II. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be part of RNA polymerase II transcription repressor complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3492) · Entrez [2117](https://www.ncbi.nlm.nih.gov/gene/2117) · UniProt [P41162](https://www.uniprot.org/uniprotkb/P41162) · Ensembl [ENSG00000117036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117036)

## Data

Gene col 3870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3870); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3870]; `tensor/DDL_lfc|DDL_z.npy` [3870]; `embed/gene_vectors.npy` [3870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3870 or target_col == 3870). Every well: [[ETV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
