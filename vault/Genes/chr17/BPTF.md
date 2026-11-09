---
symbol: "BPTF"
type: "gene"
col: 10144
ensembl_id: "ENSG00000171634"
name: "bromodomain PHD finger transcription factor"
location: "17q24.2"
module: 51
arm: "+"
pooled_cpm: 396.01
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# BPTF

*bromodomain PHD finger transcription factor* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +16.7, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.424× (z -18.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP11]] (+0.79, fdr 7e-06), [[LZIC]] (+0.76, fdr 7e-06), [[ZNF764]] (+0.74, fdr 7e-06); moves opposite to [[SDHAP4]] (-0.72, fdr 7e-06), [[PMS2P3-1]] (-0.72, fdr 7e-06), [[CPSF4]] (-0.65, fdr 9e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +16.7 | 0e+00 | 41/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.9 | 1e-20 | 37/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.6 | 4e-06 | 30/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.014 | 24/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.047 | 21/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.16× | +3.3 | 0.096 | 20/48 (hTERT-HPNE, KATO III, …) | rises with dose | position effect removed |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.10 | 18/48 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.13 | 12/48 (CFPAC-1, SW1417, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.15 | 9/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -18.5 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.434×** | -18.0 | 0e+00 | 48/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -17.1 | 0e+00 | 48/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.593×** | -11.2 | 4e-27 | 45/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.645×** | -9.1 | 1e-17 | 42/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -9.0 | 1e-17 | 47/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -7.9 | 2e-13 | 46/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.797×** | -6.9 | 4e-10 | 31/49 (A549, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -5.9 | 3e-07 | 28/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.761×** | -5.9 | 3e-07 | 32/48 (BT-474, SW 1088, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.788×** | -5.1 | 2e-05 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.635×** | -5.1 | 2e-05 | 46/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.658×** | -4.7 | 1e-04 | 25/38 (HT-29, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.799×** | -4.6 | 2e-04 | 28/47 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.801×** | -4.4 | 4e-04 | 24/45 (NCI-H23, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -4.3 | 5e-04 | 28/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.811×** | -4.3 | 5e-04 | 27/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.039 | 26/48 (LOX-IMVI, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.903× | -3.1 | 0.045 | 5/49 (CFPAC-1, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 471 | 3 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +19.7) | [[Belinostat (drug)]] 5 µM 0.342× (z -20.6) |
| [[HT-29 (line)]] | alt | 620 | 1 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +13.5) | [[Belinostat (drug)]] 5 µM 0.365× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 412 | 2 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -15.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.410× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 496 | 1 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +20.5) | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -17.6) |
| [[PANC-1 (line)]] | alt | 297 | 3 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +20.5) | [[Digitoxin (drug)]] 5 µM 0.468× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -14.3) |
| [[COLO 205 (line)]] | alt | 460 | 3 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.286× (z -21.2) |
| [[LoVo (line)]] | wt | 402 | 5 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +19.5) | [[Belinostat (drug)]] 5 µM 0.416× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 458 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.292× (z -20.3) |
| [[LOX-IMVI (line)]] | wt | 504 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 448 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.369× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 388 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +29.4) | [[Belinostat (drug)]] 5 µM 0.482× (z -14.3) |
| [[SW480 (line)]] | alt | 578 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.365× (z -22.0) |
| [[A-172 (line)]] | wt | 415 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -17.4) |
| [[SNU-423 (line)]] | alt | 417 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.303× (z -18.7) |
| [[A-427 (line)]] | wt | 557 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -14.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.527× (z -13.4) |
| [[H4 (line)]] | wt | 437 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.354× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 376 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +24.1) | [[Auranofin (drug)]] 5 µM 0.361× (z -13.3) |
| [[BT-474 (line)]] | alt | 438 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -17.3) |
| [[C32 (line)]] | wt | 307 | 2 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -10.1) |
| [[HCT15 (line)]] | alt | 514 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.363× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 393 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -11.4) |
| [[HOP62 (line)]] | alt | 461 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.340× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 372 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.5) | [[Belinostat (drug)]] 5 µM 0.419× (z -12.2) |
| [[RKO (line)]] | wt | 299 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.396× (z -11.7) |
| [[A498 (line)]] | wt | 290 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.503× (z -9.5) |
| [[C-33 A (line)]] | alt | 458 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 701 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -19.2) |
| [[LS 180 (line)]] | wt | 353 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 320 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -10.9) |
| [[SW 900 (line)]] | alt | 385 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.433× (z -11.7) |
| [[SW48 (line)]] | wt | 351 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.329× (z -13.2) |
| [[A549 (line)]] | wt | 440 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -15.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.488× (z -9.4) |
| [[CHP-212 (line)]] | wt | 926 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -12.5) |
| [[Hs 766T (line)]] | wt | 211 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.3) | [[Belinostat (drug)]] 5 µM 0.431× (z -10.7) |
| [[HS-578T (line)]] | alt | 260 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.380× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 367 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.327× (z -16.0) |
| [[J82 (line)]] | alt | 285 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.5) |
| [[SW1417 (line)]] | alt | 327 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 165 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 369 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.485× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 288 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.500× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SNU-1 (line)]] | wt | 359 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -9.2) |
| [[AN3 CA (line)]] | alt | 367 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 219 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 407 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 413 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | +0.79 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[LZIC]] | +0.76 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.74 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[ASH1L]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | same gene group; STRING 688 |
| [[HELQ]] | +0.73 | +0.84 / +0.55 | both halves | 1e-05 |  |
| [[SON]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 | STRING 403 |
| [[LARP7]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[GTF2H1]] | +0.72 | +0.85 / +0.54 | both halves | 1e-05 |  |
| [[TIAM2]] | +0.71 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[RBM23]] | +0.71 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[CEP350]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4]] | -0.72 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | -0.72 | -0.75 / -0.65 | both halves | 7e-06 |  |
| [[CPSF4]] | -0.65 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[NAPB]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ABHD17A]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[RPA1]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[RIMS3]] | -0.63 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.63 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[RNF4]] | -0.62 | -0.73 / -0.46 | both halves | 2e-05 |  |
| [[DHRS1]] | -0.62 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[NPDC1]] | -0.62 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[METAP1]] | -0.62 | -0.76 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.0, 8.2); signed map (6.1, -16.8). **Vector** length 155, 63.2% of its response variance represented; |z| ≥ 3 in 1,350 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +18.6 | +16.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +16.3 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.1 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +8.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.7 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -18.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -4.7 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -3.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain PHD finger transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:67,825,503-67,984,378 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAC1, NURF301; previously FALZ |
| Gene groups (HGNC) | PHD finger proteins; Bromodomain containing; NURF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12830](https://www.uniprot.org/uniprotkb/Q12830) (Nucleosome-remodeling factor subunit BPTF):

> Regulatory subunit of the ATP-dependent NURF-1 and NURF-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. The NURF-1 ISWI chromatin remodeling complex has a lower ATP hydrolysis rate than the NURF-5 ISWI chromatin remodeling complex. Within the NURF-1 ISWI chromatin-remodeling complex, binds to the promoters of En1 and En2 to positively regulate …

**Summary**, from NCBI Gene [2186](https://www.ncbi.nlm.nih.gov/gene/2186):

> This gene was identified by the reactivity of its encoded protein to a monoclonal antibody prepared against brain homogenates from patients with Alzheimer's disease. Analysis of the original protein (fetal Alz-50 reactive clone 1, or FAC1), identified as an 810 aa protein containing a DNA-binding domain and a zinc finger motif, suggested it might play a role in the regulation of transcription. High levels of FAC1 were detected in fetal brain and in patients with neurodegenerative diseases. The …

**Accessions** — [HGNC:3581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3581) · Entrez [2186](https://www.ncbi.nlm.nih.gov/gene/2186) · UniProt [Q12830](https://www.uniprot.org/uniprotkb/Q12830) · Ensembl [ENSG00000171634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171634)

## Data

Gene col 10144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10144); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10144]; `tensor/DDL_lfc|DDL_z.npy` [10144]; `embed/gene_vectors.npy` [10144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10144 or target_col == 10144). Every well: [[BPTF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BPTF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
