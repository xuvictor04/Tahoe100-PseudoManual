---
symbol: "TXLNG"
type: "gene"
col: 1469
ensembl_id: "ENSG00000086712"
name: "taxilin gamma"
location: "Xp22.2"
module: 5
arm: "+"
pooled_cpm: 87.43
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TXLNG

*taxilin gamma* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.82× (z +12.2, q 1e-31, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.773× (z -5.6, q 2e-05, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A19]] (+0.66, fdr 7e-06), [[MIR17HG]] (+0.61, fdr 1e-05), [[TAF4B]] (+0.60, fdr 1e-05); moves opposite to [[ZNF221]] (-0.50, fdr 1e-04), [[ZNF780A]] (-0.49, fdr 4e-05), [[RNF25]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +12.2 | 1e-31 | 42/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +11.9 | 6e-30 | 32/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +9.9 | 5e-21 | 39/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.6 | 1e-19 | 35/48 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.6 | 1e-19 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +8.4 | 3e-15 | 41/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +7.9 | 2e-13 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.47×** | +7.9 | 3e-13 | 35/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.8 | 4e-13 | 38/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +7.3 | 2e-11 | 29/49 (J82, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.9 | 2e-07 | 33/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.32×** | +5.7 | 7e-07 | 29/48 (HT-29, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.4 | 3e-06 | 29/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +5.1 | 1e-05 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.28×** | +5.1 | 2e-05 | 24/48 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 4e-05 | 26/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 17/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.016 | 4/49 (SHP-77, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -5.6 | 2e-05 | 30/47 (LoVo, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.786×** | -5.4 | 2e-05 | 26/47 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.783×** | -5.1 | 7e-05 | 23/45 (C-33 A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.818×** | -4.5 | 1e-03 | 23/49 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -4.4 | 0.001 | 24/48 (AN3 CA, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.870× | -4.4 | 0.001 | 17/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.827×** | -4.3 | 0.002 | 23/49 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.824×** | -4.2 | 0.002 | 25/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.838× | -3.8 | 0.009 | 20/42 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.869× | -3.5 | 0.031 | 16/48 (SW480, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.876× | -3.1 | 0.10 | 12/50 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.874× | -3.0 | 0.12 | 13/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.12 | 13/48 (A-427, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.3 | 9 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.84× (z +14.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.7) | — |
| [[SW480 (line)]] | alt | 135 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +13.1) | — |
| [[LoVo (line)]] | wt | 46.5 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 50.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 67.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +21.4) | — |
| [[HT-29 (line)]] | alt | 88.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 77.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.1) | — |
| [[A-172 (line)]] | wt | 59.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 190 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 67.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 87.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 42.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.9) |
| [[A-427 (line)]] | wt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 79.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.8) | — |
| [[A549 (line)]] | wt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 56.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 197 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.9) | — |
| [[RKO (line)]] | wt | 179 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A19]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MIR17HG]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TAF4B]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[USP2-AS1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[RRP12]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PABPC4]] | +0.53 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[KCNJ14]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[POLR1E]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[BZW2]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[UBAP2]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[POLR1C]] | +0.49 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[IFT140]] | +0.49 | +0.39 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF221]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ZNF780A]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RNF25]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ARRDC1-AS1]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ZNF211]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[NDUFAF5]] | -0.46 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TAB2]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DLD]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[RRP36]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[EXOC5]] | -0.46 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[TMEM175]] | -0.46 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ABHD13]] | -0.45 | -0.37 / -0.41 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.315). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.9, -42.9); signed map (-0.5, -56.2). **Vector** length 87.7, 22.4% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.9 | +7.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.7 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | taxilin gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:16,786,432-16,844,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11209, LSR5, FIAT, MGC126621, MGC126625, TXLNGX; previously CXorf15 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUQ3](https://www.uniprot.org/uniprotkb/Q9NUQ3) (Gamma-taxilin):

> May be involved in intracellular vesicle traffic. Inhibits ATF4-mediated transcription, possibly by dimerizing with ATF4 to form inactive dimers that cannot bind DNA. May be involved in regulating bone mass density through an ATF4-dependent pathway. May be involved in cell cycle progression.

**Summary**, from NCBI Gene [55787](https://www.ncbi.nlm.nih.gov/gene/55787):

> This gene encodes a member of the taxilin family. The encoded protein binds to the C-terminal coiled-coil region of syntaxin family members 1A, 3A and 4A, and may play a role in intracellular vesicle trafficking. This gene is up-regulated by lipopolysaccharide and the gene product may be involved in cell cycle regulation. The related mouse protein was also shown to inhibit activating transcription factor 4-mediated transcription and thus regulate bone mass accrual. Alternatively spliced …

**Accessions** — [HGNC:18578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18578) · Entrez [55787](https://www.ncbi.nlm.nih.gov/gene/55787) · UniProt [Q9NUQ3](https://www.uniprot.org/uniprotkb/Q9NUQ3) · Ensembl [ENSG00000086712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086712)

## Data

Gene col 1469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1469); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1469]; `tensor/DDL_lfc|DDL_z.npy` [1469]; `embed/gene_vectors.npy` [1469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1469 or target_col == 1469). Every well: [[TXLNG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXLNG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
