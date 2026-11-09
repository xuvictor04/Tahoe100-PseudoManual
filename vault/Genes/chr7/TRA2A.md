---
symbol: "TRA2A"
type: "gene"
col: 8962
ensembl_id: "ENSG00000164548"
name: "transformer 2 alpha homolog"
location: "7p15.3"
module: 59
arm: "+"
pooled_cpm: 331.97
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TRA2A

*transformer 2 alpha homolog* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +18.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.545× (z -9.7, q 1e-19, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.590× (z -8.8, q 3e-16, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2E]] (+0.69, fdr 7e-06), [[FAM53C]] (+0.67, fdr 7e-06), [[IST1]] (+0.66, fdr 7e-06); moves opposite to [[TTL]] (-0.59, fdr 1e-05), [[TMEM33]] (-0.59, fdr 1e-05), [[EIF2S1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +18.5 | 0e+00 | 46/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +11.9 | 2e-30 | 43/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.7 | 6e-20 | 40/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.3 | 4e-11 | 35/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +6.3 | 2e-08 | 42/49 (SW48, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.7 | 1e-06 | 31/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.6 | 2e-06 | 34/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 8e-06 | 28/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.38×** | +5.2 | 1e-05 | 34/48 (A498, HS-578T, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +4.8 | 9e-05 | 32/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 26/48 (SNU-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.034 | 1/50 (NCI-H2030) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.10 | 6/49 (HT-29, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -9.7 | 1e-19 | 43/44 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -9.1 | 4e-17 | 44/49 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -8.8 | 3e-16 | 44/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -7.3 | 3e-11 | 41/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.656×** | -7.0 | 2e-10 | 43/48 (HCT15, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -5.8 | 8e-07 | 44/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.710×** | -5.7 | 9e-07 | 42/48 (AN3 CA, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.4 | 6e-04 | 30/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.004 | 30/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -4.0 | 0.004 | 28/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.007 | 33/49 (NCI-H23, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.5 | 0.023 | 16/48 (AN3 CA, SHP-77, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.872× | -3.2 | 0.053 | 9/48 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.079 | 23/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.079 | 21/48 (HEC-1-A, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 313 | 5 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.463× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 317 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.14× (z +24.2) | — |
| [[SW48 (line)]] | wt | 382 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.447× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 354 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.570× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 534 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -8.5) |
| [[COLO 205 (line)]] | alt | 232 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.453× (z -9.6) |
| [[H4 (line)]] | wt | 622 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 292 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.66× (z +25.3) | — |
| [[LoVo (line)]] | wt | 288 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +23.5) | — |
| [[NCI-H1573 (line)]] | alt | 225 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 385 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -10.7) |
| [[SW1417 (line)]] | alt | 513 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -12.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 251 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -10.9) |
| [[HT-29 (line)]] | alt | 383 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 265 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 391 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 347 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 359 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.7) |
| [[HOP62 (line)]] | alt | 256 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +19.9) | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.4) |
| [[Hs 766T (line)]] | wt | 286 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 259 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 284 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 283 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.73× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 440 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +18.0) | — |
| [[RKO (line)]] | wt | 252 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 386 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 313 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 285 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 562 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 299 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 266 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 267 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.2) | — |
| [[J82 (line)]] | alt | 254 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 414 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 379 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 179 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.6) | — |
| [[A498 (line)]] | wt | 343 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.6) | — |
| [[A549 (line)]] | wt | 306 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 348 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 422 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.461× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 367 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 261 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.4) | — |
| [[SNU-1 (line)]] | wt | 286 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.2) | — |
| [[SW 1088 (line)]] | alt | 698 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 390 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 384 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 425 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[FAM53C]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[IST1]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RBM39]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 | same gene group; STRING 653 |
| [[RSRP1]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ODR4]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[CLK1]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 | STRING 799 |
| [[CCDC115]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 | STRING 617 |
| [[CDK7]] | +0.59 | +0.69 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NF2]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NBPF20]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 | STRING 548 |
| [[ZNF8]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[EXOC2]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PINX1]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.54 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[RTEL1]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (26.2, -30.1); signed map (-8.3, 3.8). **Vector** length 110, 46.9% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +18.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.3 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +3.0 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | -0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.1 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.4 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.0 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transformer 2 alpha homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,504,780-23,532,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | htra-2-alpha, AWMS1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13595](https://www.uniprot.org/uniprotkb/Q13595) (Transformer-2 protein homolog alpha):

> Sequence-specific RNA-binding protein which participates in the control of pre-mRNA splicing.

**Summary**, from NCBI Gene [29896](https://www.ncbi.nlm.nih.gov/gene/29896):

> This gene is a member of the transformer 2 homolog family and encodes a protein with several RRM (RNA recognition motif) domains. This phosphorylated nuclear protein binds to specific RNA sequences and plays a role in the regulation of pre-mRNA splicing. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:16645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16645) · Entrez [29896](https://www.ncbi.nlm.nih.gov/gene/29896) · UniProt [Q13595](https://www.uniprot.org/uniprotkb/Q13595) · Ensembl [ENSG00000164548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164548)

## Data

Gene col 8962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8962); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8962]; `tensor/DDL_lfc|DDL_z.npy` [8962]; `embed/gene_vectors.npy` [8962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8962 or target_col == 8962). Every well: [[TRA2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRA2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
