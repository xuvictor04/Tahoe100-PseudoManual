---
symbol: "DZIP3"
type: "gene"
col: 12738
ensembl_id: "ENSG00000198919"
name: "DAZ interacting zinc finger protein 3"
location: "3q13.13"
module: 28
arm: "+"
pooled_cpm: 51.61
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 15
n_dd_up_clean: 26
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DZIP3

*DAZ interacting zinc finger protein 3* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.75× (z +37.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.446× (z -13.6, q 3e-39, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.456× (z -13.2, q 3e-37, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ5]] (+0.75, fdr 7e-06), [[DARS1]] (+0.72, fdr 1e-05), [[ZNF429]] (+0.71, fdr 1e-05); moves opposite to [[FOXK2]] (-0.67, fdr 1e-05), [[DCUN1D2]] (-0.66, fdr 3e-05), [[CPSF4]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LGALS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.75×** | +37.2 | 0e+00 | 47/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.65×** | +21.8 | 0e+00 | 46/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.14×** | +18.6 | 0e+00 | 46/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.2 | 8e-11 | 31/48 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.4 | 1e-08 | 28/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 2e-08 | 27/47 (SW480, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.0 | 2e-07 | 32/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.9 | 3e-07 | 31/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.8 | 4e-07 | 25/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 5e-07 | 31/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.38×** | +5.5 | 3e-06 | 27/48 (HT-29, HEC-1-A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.2 | 1e-05 | 24/48 (A498, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 1e-05 | 24/48 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.36×** | +5.1 | 2e-05 | 22/42 (LS 180, SHP-77, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.9 | 3e-05 | 26/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +4.9 | 3e-05 | 25/48 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 6e-05 | 21/48 (SW480, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -13.6 | 3e-39 | 41/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -13.2 | 3e-37 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -13.0 | 2e-36 | 39/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -11.1 | 3e-26 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -7.0 | 2e-10 | 30/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -6.0 | 2e-07 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -5.6 | 1e-06 | 29/48 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.729×** | -5.3 | 8e-06 | 24/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -5.2 | 1e-05 | 23/48 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -5.2 | 1e-05 | 25/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.6 | 2e-04 | 26/47 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -4.5 | 3e-04 | 23/47 (COLO 205, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.654×** | -3.7 | 0.009 | 14/48 (C-33 A, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.023 | 17/48 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.678×** | -3.4 | 0.024 | 15/48 (SK-MEL-2, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.880× | -3.0 | 0.092 | 7/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 141 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +29.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.207× (z -20.3) |
| [[SW480 (line)]] | alt | 35.9 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.9) | [[Digitoxin (drug)]] 0.5 µM 0.227× (z -13.6) |
| [[A-172 (line)]] | wt | 44.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +25.8) | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.361× (z -9.1) |
| [[RKO (line)]] | wt | 65.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.36× (z +27.4) | — |
| [[A-427 (line)]] | wt | 132 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +24.3) | — |
| [[A498 (line)]] | wt | 24.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.96× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.6 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +17.5) | [[PH-797804 (drug)]] 5 µM 0.158× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 43.2 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +29.4) | [[TAK-901 (drug)]] 0.05 µM 0.403× (z -8.6) |
| [[LoVo (line)]] | wt | 20.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +24.0) | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +20.4) | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 103 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +17.5) | [[Digitoxin (drug)]] 5 µM 0.389× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.400× (z -8.8) |
| [[SNU-423 (line)]] | alt | 48.6 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +19.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -9.7) |
| [[A549 (line)]] | wt | 58.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +21.5) | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0901× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 86.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.9) | — |
| [[HOP62 (line)]] | alt | 37.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +23.4) | — |
| [[HS-578T (line)]] | alt | 39.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +25.1) | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +14.8) | — |
| [[J82 (line)]] | alt | 22.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +20.0) | — |
| [[NCI-H23 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +24.0) | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +17.8) | [[Ixazomib citrate (drug)]] 5 µM 0.331× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 47.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -10.1) |
| [[SW 1271 (line)]] | alt | 78.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +9.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0950× (z -9.4) |
| [[SW48 (line)]] | wt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +18.1) | — |
| [[BT-474 (line)]] | alt | 19.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +18.0) | — |
| [[C32 (line)]] | wt | 30.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +16.3) | — |
| [[Hs 766T (line)]] | wt | 48.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.262× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +14.2) | — |
| [[KATO III (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 40.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 49.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +19.6) | — |
| [[SNU-1 (line)]] | wt | 43.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 42.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.9) | — |
| [[C-33 A (line)]] | alt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 70.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +18.7) | — |
| [[CHP-212 (line)]] | wt | 49.7 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.134× (z -9.2) |
| [[H4 (line)]] | wt | 48.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.6) |
| [[HCT15 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +17.0) | — |
| [[SW1417 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ5]] | +0.75 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[DARS1]] | +0.72 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ZNF429]] | +0.71 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[USP40]] | +0.70 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | +0.69 | +0.80 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD26]] | +0.68 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[IFT74]] | +0.68 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[TIA1]] | +0.67 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.66 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[DPY19L2P2]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.66 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[OCIAD1]] | +0.66 | +0.78 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | -0.67 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.66 | -0.75 / -0.46 | both halves | 3e-05 |  |
| [[CPSF4]] | -0.65 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[STARD3]] | -0.65 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[HIRA]] | -0.64 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.63 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[GNA12]] | -0.63 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[TRABD]] | -0.63 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SS18L1]] | -0.62 | -0.69 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers DZIP3's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.75× higher at baseline in the lines without LGALS3 | 0.038 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers DZIP3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[IKBKE]] | C | IKBKE activity lowers DZIP3's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.29× higher at baseline in the lines without IKBKE | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.4, 8.0); signed map (10.7, -24.6). **Vector** length 122, 38.0% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.0 | +37.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.4 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.4 | +21.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +5.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | -13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DAZ interacting zinc finger protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:108,589,705-108,694,840 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRUL138, PPP1R66 |
| Gene groups (HGNC) | Ring finger proteins; Protein phosphatase 1 regulatory subunits; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y13](https://www.uniprot.org/uniprotkb/Q86Y13) (E3 ubiquitin-protein ligase DZIP3):

> E3 Ubiquitin ligase proteins mediate ubiquitination and subsequent proteasomal degradation of target proteins. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Able to specifically bind RNA.

**Summary**, from NCBI Gene [9666](https://www.ncbi.nlm.nih.gov/gene/9666):

> Enables several functions, including phosphatase binding activity; polyubiquitin modification-dependent protein binding activity; and ubiquitin-protein transferase activity. Involved in protein polyubiquitination. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30938) · Entrez [9666](https://www.ncbi.nlm.nih.gov/gene/9666) · UniProt [Q86Y13](https://www.uniprot.org/uniprotkb/Q86Y13) · Ensembl [ENSG00000198919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198919)

## Data

Gene col 12738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12738); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12738]; `tensor/DDL_lfc|DDL_z.npy` [12738]; `embed/gene_vectors.npy` [12738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12738 or target_col == 12738). Every well: [[DZIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DZIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
