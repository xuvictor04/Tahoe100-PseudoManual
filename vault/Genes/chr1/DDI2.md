---
symbol: "DDI2"
type: "gene"
col: 12379
ensembl_id: "ENSG00000197312"
name: "DDI proteasomal shuttling factor 2"
location: "1p36.21"
module: 20
arm: "-"
pooled_cpm: 59.86
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DDI2

*DDI proteasomal shuttling factor 2* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.74× (z +12.1, q 7e-31, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.628× (z -9.8, q 5e-20, down in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.782× (z -5.4, q 8e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSPH3]] (+0.58, fdr 1e-05), [[ZNF696]] (+0.53, fdr 3e-05), [[CSGALNACT2]] (+0.51, fdr 3e-05); moves opposite to [[ILF3]] (-0.56, fdr 1e-05), [[ATP2A2]] (-0.50, fdr 3e-05), [[ANP32E]] (-0.49, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +12.1 | 7e-31 | 42/48 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +10.7 | 5e-24 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +10.5 | 2e-23 | 38/48 (HT-29, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +10.2 | 2e-22 | 36/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +9.1 | 8e-18 | 34/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.5 | 6e-12 | 29/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.0 | 2e-10 | 31/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +6.0 | 2e-07 | 29/48 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.9 | 2e-07 | 26/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 9e-07 | 23/48 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.51×** | +4.7 | 1e-04 | 21/48 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +4.4 | 5e-04 | 20/48 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.2 | 9e-04 | 13/49 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +4.2 | 9e-04 | 22/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +4.2 | 9e-04 | 20/48 (SW480, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.5 | 0.017 | 19/48 (SW480, NCI-H460, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.026 | 16/48 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -9.8 | 5e-20 | 29/41 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.681×** | -8.4 | 1e-14 | 30/49 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -7.4 | 3e-11 | 27/44 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -5.7 | 1e-06 | 4/49 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -5.4 | 8e-06 | 25/48 (HOP62, AsPC-1, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.836× | -4.3 | 0.002 | 16/48 (NCI-H661, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.888× | -3.6 | 0.024 | 14/49 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.732×** | -3.6 | 0.024 | 17/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.737×** | -3.5 | 0.029 | 18/45 (HOP62, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.858× | -3.4 | 0.040 | 20/48 (HepG2/C3A, COLO 205, …) | two highest doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.853× | -3.4 | 0.040 | 15/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.855× | -3.3 | 0.043 | 11/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.056 | 14/47 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Capmatinib (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.075 | 14/47 (COLO 205, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.8 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.25× (z +11.2) | — |
| [[SW480 (line)]] | alt | 55.7 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.40× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 55.3 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.57× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.33× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 165 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.58× (z +9.7) | [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -9.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[KATO III (line)]] | alt | 43.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 68.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 96.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -14.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 75.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.40× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 89.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -18.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 51.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +10.5) | — |
| [[C32 (line)]] | wt | 65.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -14.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 86.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 88.0 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0549× (z -11.0) |
| [[A-172 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 54.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.31× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.451× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPH3]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ZNF696]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[CSGALNACT2]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[PARD6B]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[ZXDC]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[MINDY2]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[GPR157]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PURA]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RSC1A1]] | +0.48 | +0.59 / +0.41 | both halves | 4e-05 | STRING 924; ⚠ **readthrough risk**: RSC1A1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TMEM158]] | +0.47 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ZCCHC9]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CLEC2B]] | +0.47 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[ORAI1]] | +0.47 | +0.26 / +0.48 | both halves | 4e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF3]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ANP32E]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[PSMD11]] | -0.48 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[CSDE1]] | -0.47 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[CAPS2]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[SARS2]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CHD3]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PHTF1]] | -0.46 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[JAKMIP3]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ABCC2]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[STXBP4]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.299). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-54.6, -20.0); signed map (-1.9, 10.1). **Vector** length 110, 28.8% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.2 | +10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +1.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +3.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -6.6 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -5.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.2 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DDI proteasomal shuttling factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,617,458-15,669,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14844; previously RSC1A1 |
| Gene groups (HGNC) | Peptidase family A28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TDH0](https://www.uniprot.org/uniprotkb/Q5TDH0) (Protein DDI1 homolog 2):

> Aspartic protease that mediates the cleavage of NFE2L1/NRF1 during proteasome 'bounce-back' response, a mechanism that takes place in response to proteasome inhibition and activates expression of new proteasome subunits, triggering de novo proteasome assembly to restore protein homeostasis. Specifically recognizes and binds ubiquitinated NFE2L1/NRF1 and mediates the cleavage of NFE2L1/NRF1 at 'Leu-104', promoting NFE2L1/NRF1 release from the endoplasmic reticulum membrane, a key step for …

**Summary**, from NCBI Gene [84301](https://www.ncbi.nlm.nih.gov/gene/84301):

> The protein encoded by this intronless gene inhibits the expression of the solute carrier family 5 (sodium/glucose cotransporter), member 1 gene (SLC5A1) and downregulates exocytosis of the SLC5A1 protein. The encoded protein is sometimes found coating the trans-Golgi network and other times is localized to the nucleus, depending on the cell cycle stage. This protein also inhibits the expression of solute carrier family 22 (organic cation transporter), member 2 (SLC22A2). [provided by RefSeq, …

**Accessions** — [HGNC:24578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24578) · Entrez [84301](https://www.ncbi.nlm.nih.gov/gene/84301) · UniProt [Q5TDH0](https://www.uniprot.org/uniprotkb/Q5TDH0) · Ensembl [ENSG00000197312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197312)

## Data

Gene col 12379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12379); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12379]; `tensor/DDL_lfc|DDL_z.npy` [12379]; `embed/gene_vectors.npy` [12379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12379 or target_col == 12379). Every well: [[DDI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
