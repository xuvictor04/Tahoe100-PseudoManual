---
symbol: "RNF4"
type: "gene"
col: 734
ensembl_id: "ENSG00000063978"
name: "ring finger protein 4"
location: "4p16.3"
module: 168
arm: "+"
pooled_cpm: 54.27
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# RNF4

*ring finger protein 4* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 6.52× (z +13.0, q 6e-36, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.412× (z -11.4, q 3e-27, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.602× (z -9.2, q 5e-18, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.80, fdr 7e-06), [[SNHG30]] (+0.78, fdr 7e-06), [[ARHGEF7]] (+0.76, fdr 7e-06); moves opposite to [[OCIAD1]] (-0.69, fdr 7e-06), [[TIA1]] (-0.67, fdr 1e-05), [[TFE3]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **6.52×** | +13.0 | 6e-36 | 46/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **5.55×** | +11.9 | 4e-30 | 48/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.9 | 9e-10 | 37/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.8 | 9e-07 | 27/36 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +5.8 | 1e-06 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +5.6 | 2e-06 | 38/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +5.0 | 4e-05 | 35/47 (RKO, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.44×** | +4.8 | 1e-04 | 32/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 28/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +4.5 | 4e-04 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 6e-04 | 33/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.007 | 24/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.007 | 22/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.011 | 25/48 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.014 | 24/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.036 | 21/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.047 | 22/48 (PANC-1, A-427, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.055 | 18/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.081 | 19/47 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -11.4 | 3e-27 | 37/42 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.434×** | -11.2 | 2e-26 | 45/49 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -9.2 | 5e-18 | 41/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -6.8 | 2e-09 | 42/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.711×** | -4.6 | 5e-04 | 31/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -4.5 | 5e-04 | 26/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.777×** | -3.4 | 0.053 | 21/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.073 | 22/47 (C32, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.794× | -3.1 | 0.11 | 17/47 (SK-MEL-2, A-427, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.715× | -3.1 | 0.12 | 21/48 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.2 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 57.6 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.10× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 41.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +11.9) | — |
| [[RKO (line)]] | wt | 63.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.2× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -17.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 11.9× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 45.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 10.8× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 69.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.6) |
| [[A-172 (line)]] | wt | 54.7 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.28× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.3) |
| [[A-427 (line)]] | wt | 57.2 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.94× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 63.7 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.7) |
| [[LS 180 (line)]] | wt | 50.8 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 12.8× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 57.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.94× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 77.7 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.24× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.3) |
| [[AN3 CA (line)]] | alt | 69.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -11.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 49.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.7) |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -12.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.8) |
| [[KATO III (line)]] | alt | 41.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +9.7) | — |
| [[LoVo (line)]] | wt | 36.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.89× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.97× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 53.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0950× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.1) |
| [[SNU-423 (line)]] | alt | 49.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.7) |
| [[C32 (line)]] | wt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0617× (z -21.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 9.84× (z +9.3) | — |
| [[SW48 (line)]] | wt | 69.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.83× (z +10.5) | — |
| [[A498 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.80 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[ARHGEF7]] | +0.76 | +0.84 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.75 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[NDC1]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[GRB2]] | +0.74 | +0.78 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[MFSD14CP]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[POM121]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.70 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MED17]] | +0.70 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[PHB2]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.67 | +0.74 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | -0.69 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[TIA1]] | -0.67 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[TFE3]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[CHMP4A]] | -0.66 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[USP16]] | -0.66 | -0.65 / -0.56 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[LZIC]] | -0.66 | -0.76 / -0.51 | both halves | 1e-05 |  |
| [[ING3]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[LARP7]] | -0.66 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.66 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[JUN]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[LGALS3]] | -0.64 | -0.60 / -0.53 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[ZNF764]] | -0.63 | -0.71 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.865). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-5.2, -15.1); signed map (-41.6, -12.4). **Vector** length 118, 38.3% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.5 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +13.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.4 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.8 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -11.1 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,462,220-2,515,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RES4-26, SNURF, SLX5 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | COMPLEMENT |
| Reactome | 8 pathways, smallest: Processing of DNA double-strand break ends; HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA); Homology Directed Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [P78317](https://www.uniprot.org/uniprotkb/P78317) (E3 ubiquitin-protein ligase RNF4):

> E3 ubiquitin-protein ligase which binds polysumoylated chains covalently attached to proteins and mediates 'Lys-6'-, 'Lys-11'-, 'Lys-48'- and 'Lys-63'-linked polyubiquitination of those substrates and their subsequent targeting to the proteasome for degradation. Regulates the degradation of several proteins including PML and the transcriptional activator PEA3. Involved in chromosome alignment and spindle assembly, it regulates the kinetochore CENPH-CENPI-CENPK complex by targeting …

**Summary**, from NCBI Gene [6047](https://www.ncbi.nlm.nih.gov/gene/6047):

> The protein encoded by this gene contains a RING finger motif and acts as a transcription regulator. This protein has been shown to interact with, and inhibit the activity of, TRPS1, a transcription suppressor of GATA-mediated transcription. Transcription repressor ZNF278/PATZ is found to interact with this protein, and thus reduce the enhancement of androgen receptor-dependent transcription mediated by this protein. Studies of the mouse and rat counterparts suggested a role of this protein in …

**Accessions** — [HGNC:10067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10067) · Entrez [6047](https://www.ncbi.nlm.nih.gov/gene/6047) · UniProt [P78317](https://www.uniprot.org/uniprotkb/P78317) · Ensembl [ENSG00000063978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063978)

## Data

Gene col 734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 734); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 734]; `tensor/DDL_lfc|DDL_z.npy` [734]; `embed/gene_vectors.npy` [734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 734 or target_col == 734). Every well: [[RNF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
