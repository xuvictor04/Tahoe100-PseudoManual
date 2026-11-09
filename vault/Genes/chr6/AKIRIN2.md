---
symbol: "AKIRIN2"
type: "gene"
col: 5684
ensembl_id: "ENSG00000135334"
name: "akirin 2"
location: "6q15"
module: 20
arm: "-"
pooled_cpm: 40.35
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# AKIRIN2

*akirin 2* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +17.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.595× (z -9.2, q 2e-17, down in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.710× (z -6.1, q 2e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERTAD1]] (+0.58, fdr 1e-05), [[KLF5]] (+0.54, fdr 1e-05), [[ARRDC2]] (+0.52, fdr 3e-05); moves opposite to [[UGGT1]] (-0.57, fdr 3e-05), [[SETD3]] (-0.55, fdr 2e-04), [[NBAS]] (-0.51, fdr 2e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GGT7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +17.7 | 0e+00 | 44/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +16.6 | 0e+00 | 46/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +14.8 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +13.9 | 1e-41 | 45/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +13.5 | 3e-39 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +11.7 | 8e-30 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +10.6 | 3e-24 | 43/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +10.0 | 7e-22 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.6 | 3e-20 | 37/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +9.1 | 4e-18 | 36/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.0 | 2e-17 | 37/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.4 | 9e-12 | 36/48 (SW480, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.1 | 6e-11 | 4/49 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.0 | 1e-07 | 28/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 2e-07 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.7 | 9e-05 | 20/48 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 23/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 3e-04 | 22/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -9.2 | 2e-17 | 33/41 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -9.0 | 4e-17 | 32/47 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.710×** | -6.1 | 2e-07 | 28/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.027 | 19/48 (LoVo, AN3 CA, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.6 | 0.031 | 17/47 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.042 | 21/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.879× | -3.3 | 0.087 | 13/48 (LS 180, RKO, …) | all doses, flat |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.16 | 10/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.851× | -3.0 | 0.16 | 10/48 (CHP-212, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.5 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.7 | 9 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.34× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +15.5) | — |
| [[SW480 (line)]] | alt | 46.4 | 9 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.64× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +15.6) | — |
| [[KATO III (line)]] | alt | 33.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 7.73× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.68× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 52.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 66.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 42.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 50.4 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 49.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 40.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +9.0) | — |
| [[A498 (line)]] | wt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.1) | — |
| [[AN3 CA (line)]] | alt | 69.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -9.4) |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.5 µM 0.0941× (z -9.7) |
| [[HOP62 (line)]] | alt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 29.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.3) | — |
| [[J82 (line)]] | alt | 40.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[LoVo (line)]] | wt | 42.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 49.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 40.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.04× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0903× (z -10.8) ⚠ toxic |
| [[A549 (line)]] | wt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 50.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERTAD1]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KLF5]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ARRDC2]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[ZNF397]] | +0.50 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[IER5]] | +0.50 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[GSPT2]] | +0.49 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[PNRC2]] | +0.48 | +0.27 / +0.61 | both halves | 3e-04 |  |
| [[ZNF585B]] | +0.48 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[MED18]] | +0.48 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[ACAP1]] | +0.48 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[WASL-DT]] | +0.47 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[PIM3]] | +0.47 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGGT1]] | -0.57 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SETD3]] | -0.55 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[NBAS]] | -0.51 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[GLB1]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[NDUFA10]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[PDHA1]] | -0.50 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[GDI2]] | -0.48 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[EIF2AK1]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CMPK1]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HTT]] | -0.47 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[CRTAP]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[PIGN]] | -0.47 | -0.29 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGT7]] | B | GGT7 activity lowers AKIRIN2's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 1.16× higher at baseline in the lines without GGT7 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.3, 19.9); signed map (-1.7, 14.4). **Vector** length 63.8, 12.9% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | -0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | -2.2 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | akirin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:87,674,860-87,702,233 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10342, dJ486L4.2; previously C6orf166 |
| Gene groups (HGNC) | Akirin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H80](https://www.uniprot.org/uniprotkb/Q53H80) (Akirin-2):

> Molecular adapter that acts as a bridge between a variety of multiprotein complexes, and which is involved in embryonic development, immunity, myogenesis and brain development. Plays a key role in nuclear protein degradation by promoting import of proteasomes into the nucleus: directly binds to fully assembled 20S proteasomes at one end and to nuclear import receptor IPO9 at the other end, bridging them together and mediating the import of pre-assembled proteasome complexes through the nuclear …

**Summary**, from NCBI Gene [55122](https://www.ncbi.nlm.nih.gov/gene/55122):

> Enables enzyme binding activity; identical protein binding activity; and protein-macromolecule adaptor activity. Involved in proteasome localization and protein import into nucleus. Acts upstream of with a positive effect on nuclear protein quality control by the ubiquitin-proteasome system. Located in nucleoplasm. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21407) · Entrez [55122](https://www.ncbi.nlm.nih.gov/gene/55122) · UniProt [Q53H80](https://www.uniprot.org/uniprotkb/Q53H80) · Ensembl [ENSG00000135334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135334)

## Data

Gene col 5684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5684); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5684]; `tensor/DDL_lfc|DDL_z.npy` [5684]; `embed/gene_vectors.npy` [5684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5684 or target_col == 5684). Every well: [[AKIRIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKIRIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
