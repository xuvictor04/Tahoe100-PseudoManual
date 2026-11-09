---
symbol: "OBI1"
type: "gene"
col: 7599
ensembl_id: "ENSG00000152193"
name: "ORC ubiquitin ligase 1"
location: "13q31.1"
module: 11
arm: "+"
pooled_cpm: 34.67
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# OBI1

*ORC ubiquitin ligase 1* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.41× (z +28.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.658× (z -9.5, q 2e-18, down in 30 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.303×, HEC-1-A 0.269×, NCI-H23 0.225×, C32 0.193×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0988×, NCI-H460 0.236×, SW1417 0.263×, SW48 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C32 0.115×, LS 180 0.171×, HT-29 0.250×, NCI-H460 0.387×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COIL]] (+0.73, fdr 7e-06), [[C1orf131]] (+0.71, fdr 7e-06), [[RDH14]] (+0.71, fdr 7e-06); moves opposite to [[EIF2S3]] (-0.57, fdr 4e-05), [[QSOX1]] (-0.56, fdr 1e-05), [[PMPCA]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +28.0 | 0e+00 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.81×** | +22.3 | 0e+00 | 48/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +19.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.15×** | +19.3 | 0e+00 | 48/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.25×** | +18.2 | 0e+00 | 47/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.82×** | +13.4 | 5e-39 | 40/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +12.8 | 1e-35 | 37/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +12.8 | 2e-35 | 42/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.54×** | +9.7 | 2e-20 | 31/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +8.8 | 8e-17 | 32/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +8.6 | 5e-16 | 32/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.46×** | +8.4 | 2e-15 | 30/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.45×** | +8.3 | 4e-15 | 32/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.45×** | +8.3 | 5e-15 | 29/48 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.40×** | +7.3 | 1e-11 | 28/47 (LOX-IMVI, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +6.0 | 5e-08 | 27/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 2e-07 | 26/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.006 | 11/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.6 | 0.007 | 10/48 (J82, LOX-IMVI, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.011 | 10/47 (SNU-1, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.040 | 9/48 (J82, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.043 | 8/47 (A498, SW 900, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.303×, HEC-1-A 0.269×, NCI-H23 0.225×, C32 0.193×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0988×, NCI-H460 0.236×, SW1417 0.263×, SW48 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C32 0.115×, LS 180 0.171×, HT-29 0.250×, NCI-H460 0.387×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.658×** | -9.5 | 2e-18 | 30/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -7.6 | 1e-11 | 21/38 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.804×** | -4.6 | 0.001 | 20/42 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Posaconazole (drug)]] 5 µM |  | 0.846× | -3.7 | 0.037 | 5/48 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.21 | 8/47 (HepG2/C3A, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.8 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +20.7) | — |
| [[HEC-1-A (line)]] | alt | 38.4 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.6 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -16.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.0) | — |
| [[SW480 (line)]] | alt | 80.5 | 6 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.79× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -16.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 67.6 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -14.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 66.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 35.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 70.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.2) | — |
| [[KATO III (line)]] | alt | 45.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 35.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.2) | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.7) | — |
| [[A498 (line)]] | wt | 40.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.2) | — |
| [[A549 (line)]] | wt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.1) | — |
| [[C32 (line)]] | wt | 28.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -14.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.5) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 18.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -16.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.1) | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.122× (z -9.7) |
| [[HS-578T (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 50.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.84× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[RDH14]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PHAX]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[RPP38]] | +0.71 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.69 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[DDX20]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ETAA1]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MRM2]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S3]] | -0.57 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[QSOX1]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.56 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.9, 4.7); signed map (1.2, -19.8). **Vector** length 88.0, 21.3% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +22.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +19.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +19.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.1 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +12.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | -9.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -2.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -7.6 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ORC ubiquitin ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.1 — chr13:78,614,289-78,659,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13449; previously C13orf7, RNF219 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; G2/M Transition; Mitotic G2-G2/M phases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W0B1](https://www.uniprot.org/uniprotkb/Q5W0B1) (ORC ubiquitin ligase 1):

> E3 ubiquitin ligase essential for DNA replication origin activation during S phase. Acts as a replication origin selector which selects the origins to be fired and catalyzes the multi-mono-ubiquitination of a subset of chromatin-bound ORC3 and ORC5 during S-phase.

**Summary**, from NCBI Gene [79596](https://www.ncbi.nlm.nih.gov/gene/79596):

> Enables chromatin binding activity and ubiquitin-protein transferase activity. Involved in protein autoubiquitination; protein monoubiquitination; and regulation of DNA replication. Located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20308) · Entrez [79596](https://www.ncbi.nlm.nih.gov/gene/79596) · UniProt [Q5W0B1](https://www.uniprot.org/uniprotkb/Q5W0B1) · Ensembl [ENSG00000152193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152193)

## Data

Gene col 7599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7599); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7599]; `tensor/DDL_lfc|DDL_z.npy` [7599]; `embed/gene_vectors.npy` [7599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7599 or target_col == 7599). Every well: [[OBI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OBI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
