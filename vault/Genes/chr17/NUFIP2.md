---
symbol: "NUFIP2"
type: "gene"
col: 2928
ensembl_id: "ENSG00000108256"
name: "nuclear FMR1 interacting protein 2"
location: "17q11.2"
module: 38
arm: "+"
pooled_cpm: 322.84
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# NUFIP2

*nuclear FMR1 interacting protein 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +22.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.737× (z -6.8, q 7e-09, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.367×, A498 0.486×, A-172 0.591×, SNU-423 0.533×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 0.406×, A-172 0.545×, SNU-423 0.495×, LOX-IMVI 0.575×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.488×, SNU-423 0.545×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.500×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC23]] (+0.64, fdr 1e-05), [[LRIF1]] (+0.62, fdr 1e-05), [[INTS6]] (+0.60, fdr 3e-05); moves opposite to [[DLD]] (-0.58, fdr 2e-05), [[PABIR2]] (-0.55, fdr 3e-05), [[RPP30]] (-0.53, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +22.2 | 0e+00 | 46/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +15.8 | 0e+00 | 48/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +12.9 | 1e-35 | 44/48 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.6 | 6e-24 | 44/48 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +9.7 | 4e-20 | 33/49 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +9.4 | 6e-19 | 42/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.8 | 8e-17 | 41/48 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +8.7 | 2e-16 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +8.4 | 3e-15 | 43/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.4 | 3e-15 | 41/48 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +7.8 | 3e-13 | 44/49 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 6e-10 | 35/48 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 4e-08 | 39/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 6e-07 | 37/48 (Hs 766T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +5.4 | 3e-06 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.0 | 2e-05 | 37/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.8 | 5e-05 | 27/50 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H23 0.367×, A498 0.486×, A-172 0.591×, SNU-423 0.533×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 0.406×, A-172 0.545×, SNU-423 0.495×, LOX-IMVI 0.575×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.488×, SNU-423 0.545×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.500×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -6.8 | 7e-09 | 44/48 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -5.4 | 2e-05 | 22/44 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.802×** | -5.1 | 6e-05 | 25/49 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.831×** | -4.0 | 0.010 | 23/45 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.850× | -3.8 | 0.017 | 15/48 (KATO III, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.018 | 19/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.737×** | -3.7 | 0.018 | 30/49 (NCI-H2347, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.3 | 0.061 | 11/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.12 | 10/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.877× | -3.1 | 0.13 | 10/48 (SW 900, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 317 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.594× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 277 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 330 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 335 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.532× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 198 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +18.7) | — |
| [[A-172 (line)]] | wt | 394 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.545× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 244 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 361 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 232 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +21.5) | — |
| [[COLO 205 (line)]] | alt | 364 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +24.8) | — |
| [[HEC-1-A (line)]] | alt | 480 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.5) | — |
| [[Hs 766T (line)]] | wt | 209 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.6) | — |
| [[PANC-1 (line)]] | alt | 400 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 351 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.6) | — |
| [[J82 (line)]] | alt | 331 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +18.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 326 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 338 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.500× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 210 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +25.8) | — |
| [[Panc 03.27 (line)]] | alt | 426 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.8) | — |
| [[SNU-1 (line)]] | wt | 291 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.3) | — |
| [[A498 (line)]] | wt | 503 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 305 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +17.6) | — |
| [[H4 (line)]] | wt | 239 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 337 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +22.5) | — |
| [[LOX-IMVI (line)]] | wt | 402 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.575× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 168 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 228 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +23.6) | — |
| [[HCT15 (line)]] | alt | 371 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 240 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +23.1) | — |
| [[LoVo (line)]] | wt | 284 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 214 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.9) | — |
| [[SK-MEL-2 (line)]] | alt | 324 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.576× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 278 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 337 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +17.1) | — |
| [[A-427 (line)]] | wt | 252 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.39× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 285 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.2) | — |
| [[RKO (line)]] | wt | 322 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[SW48 (line)]] | wt | 240 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.9) | — |
| [[A549 (line)]] | wt | 398 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 226 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 277 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.87× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 456 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -15.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 283 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 535 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 221 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 491 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC23]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LRIF1]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[INTS6]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[THUMPD3-AS1]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[SYCE2]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[LINC00862]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ABHD5]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[POLG2]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[CFAP53]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[LINC02936]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PYY]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[PHKG1]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.58 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PABIR2]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RPP30]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MPP7]] | -0.52 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[APOO]] | -0.52 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[EXT2]] | -0.52 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[DHX9]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 | STRING 828 |
| [[TMTC3]] | -0.51 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[BRD7]] | -0.51 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[FAM98B]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ECHS1]] | -0.48 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[SPATA6]] | -0.48 | -0.43 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, -21.3); signed map (10.5, 11.4). **Vector** length 95.6, 32.6% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -5.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +5.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear FMR1 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,255,839-29,294,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1321, MGC117262, PIG1, 182-FIP, FIP-82, 82-FIP, NUFP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z417](https://www.uniprot.org/uniprotkb/Q7Z417) (FMR1-interacting protein NUFIP2):

> Binds RNA.

**Summary**, from NCBI Gene [57532](https://www.ncbi.nlm.nih.gov/gene/57532):

> Enables RNA binding activity. Located in several cellular components, including cytoplasmic stress granule; nuclear body; and ribosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17634) · Entrez [57532](https://www.ncbi.nlm.nih.gov/gene/57532) · UniProt [Q7Z417](https://www.uniprot.org/uniprotkb/Q7Z417) · Ensembl [ENSG00000108256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108256)

## Data

Gene col 2928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2928); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2928]; `tensor/DDL_lfc|DDL_z.npy` [2928]; `embed/gene_vectors.npy` [2928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2928 or target_col == 2928). Every well: [[NUFIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUFIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
