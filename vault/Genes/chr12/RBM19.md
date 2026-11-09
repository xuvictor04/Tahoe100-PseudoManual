---
symbol: "RBM19"
type: "gene"
col: 4389
ensembl_id: "ENSG00000122965"
name: "RNA binding motif protein 19"
location: "12q24.13-q24.21"
module: 5
arm: "+"
pooled_cpm: 59.68
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 9
n_dd_up_clean: 32
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RBM19

*RNA binding motif protein 19* — 12q24.13-q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.87× (z +18.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.731× (z -7.8, q 4e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT1]] (+0.73, fdr 7e-06), [[DHX37]] (+0.69, fdr 7e-06), [[GNL3L]] (+0.68, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.65, fdr 1e-05), [[PRMT9]] (-0.65, fdr 9e-06), [[DBP]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.87×** | +18.4 | 0e+00 | 46/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.25×** | +14.2 | 4e-43 | 48/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +14.1 | 5e-43 | 45/48 (PANC-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +13.7 | 2e-40 | 41/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.10×** | +13.0 | 2e-36 | 45/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +12.6 | 1e-34 | 44/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +12.3 | 5e-33 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +11.0 | 2e-26 | 47/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +9.6 | 8e-20 | 28/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +9.2 | 3e-18 | 43/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +7.7 | 5e-13 | 34/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.6 | 2e-09 | 39/43 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.90×** | +5.8 | 2e-07 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.40×** | +5.8 | 2e-07 | 30/49 (LoVo, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +5.6 | 8e-07 | 29/49 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +5.4 | 2e-06 | 33/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 25/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 2e-05 | 31/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +5.0 | 2e-05 | 33/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 27/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.8 | 4e-12 | 37/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -6.2 | 2e-07 | 34/48 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.802×** | -4.7 | 6e-04 | 26/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.803×** | -4.4 | 0.002 | 24/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.770×** | -4.0 | 0.006 | 19/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.803×** | -3.9 | 0.009 | 21/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.804×** | -3.9 | 0.009 | 23/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.865× | -3.6 | 0.020 | 19/48 (A-427, RKO, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.864× | -3.5 | 0.027 | 16/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.028 | 20/47 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.863× | -3.4 | 0.038 | 12/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.882× | -3.2 | 0.075 | 9/48 (SW48, SHP-77, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.711×** | -3.1 | 0.076 | 14/49 (NCI-H23, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.0 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 68.1 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +15.6) | — |
| [[AsPC-1 (line)]] | alt | 95.5 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.44× (z +18.7) | — |
| [[NCI-H1573 (line)]] | alt | 95.2 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.40× (z +15.9) | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +17.0) | — |
| [[SW 900 (line)]] | alt | 37.9 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +11.8) | — |
| [[SW480 (line)]] | alt | 57.5 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 150 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 31.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 38.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +13.1) | — |
| [[KATO III (line)]] | alt | 39.1 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.32× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 52.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.93× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 55.3 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.9× (z +16.9) | [[Canagliflozin (drug)]] 0.05 µM 0.249× (z -9.1) |
| [[Hs 766T (line)]] | wt | 35.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.62× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 73.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.18× (z +10.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.66× (z +9.0) | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -15.8) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.468× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 50.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.9) | — |
| [[A498 (line)]] | wt | 57.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +10.0) | — |
| [[J82 (line)]] | alt | 62.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.1) | — |
| [[A-172 (line)]] | wt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 37.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +9.9) | — |
| [[LoVo (line)]] | wt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.9 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.14× (z +10.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 131 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.9) | — |
| [[SNU-1 (line)]] | wt | 56.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.40× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 56.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 70.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 35.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 31.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 88.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 73.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 52.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.6) | — |
| [[A-427 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT1]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 | STRING 422 |
| [[DHX37]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | same gene group; STRING 488 |
| [[GNL3L]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | STRING 828 |
| [[VAC14]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[COX10]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PUM3]] | +0.66 | +0.60 / +0.73 | both halves | 7e-06 | STRING 862 |
| [[PRMT3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[BRD9]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[UTP20]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 | same gene group; STRING 837 |
| [[WDR4]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | STRING 408 |
| [[PEPD]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[PRMT9]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[DBP]] | -0.64 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[FAM229B]] | -0.62 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[LCA5]] | -0.60 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[RNF114]] | -0.59 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | -0.59 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[ZNF14]] | -0.58 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ORC4]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises RBM19's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TOP2A]] | B | TOP2A activity lowers RBM19's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CXXC5]] | B | CXXC5 activity lowers RBM19's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without CXXC5 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.8, -32.7); signed map (0.0, -48.1). **Vector** length 124, 40.7% of its response variance represented; |z| ≥ 3 in 1,525 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +14.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +14.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +6.5 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +11.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +5.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13-q24.21 — chr12:113,816,738-113,966,325 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586F1023, KIAA0682, Mrd1 |
| Gene groups (HGNC) | RNA binding motif containing; SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4C8](https://www.uniprot.org/uniprotkb/Q9Y4C8) (Probable RNA-binding protein 19):

> Plays a role in embryo pre-implantation development.

**Summary**, from NCBI Gene [9904](https://www.ncbi.nlm.nih.gov/gene/9904):

> This gene encodes a nucleolar protein that contains six RNA-binding motifs. The encoded protein may be involved in regulating ribosome biogenesis. Multiple alternatively spliced variants, encoding the same protein, have been identified.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:29098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29098) · Entrez [9904](https://www.ncbi.nlm.nih.gov/gene/9904) · UniProt [Q9Y4C8](https://www.uniprot.org/uniprotkb/Q9Y4C8) · Ensembl [ENSG00000122965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122965)

## Data

Gene col 4389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4389); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4389]; `tensor/DDL_lfc|DDL_z.npy` [4389]; `embed/gene_vectors.npy` [4389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4389 or target_col == 4389). Every well: [[RBM19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
