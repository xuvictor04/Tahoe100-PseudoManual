---
symbol: "SRRM2"
type: "gene"
col: 9568
ensembl_id: "ENSG00000167978"
name: "serine/arginine repetitive matrix 2"
location: "16p13.3"
module: 96
arm: "+"
pooled_cpm: 463.62
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# SRRM2

*serine/arginine repetitive matrix 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +11.5, q 5e-28, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.38× (z +6.7, q 1e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.557× (z -12.2, q 3e-31, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT3]] (+0.80, fdr 7e-06), [[CELSR3]] (+0.74, fdr 7e-06), [[AKT1S1]] (+0.71, fdr 1e-05); moves opposite to [[TMEM160]] (-0.69, fdr 7e-06), [[GRB2]] (-0.66, fdr 3e-05), [[PDCD10]] (-0.64, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYNM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.58×** | +11.5 | 5e-28 | 45/48 (NCI-H460, A549, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.3 | 3e-22 | 42/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +9.5 | 5e-19 | 45/49 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +9.3 | 2e-18 | 46/48 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +8.7 | 4e-16 | 43/48 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.9 | 2e-13 | 42/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +7.4 | 8e-12 | 33/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.42×** | +7.0 | 1e-10 | 35/48 (NCI-H460, A549, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 1e-09 | 38/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +5.0 | 3e-05 | 40/49 (NCI-H2030, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +4.5 | 3e-04 | 29/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.016 | 28/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 1.18× | +3.3 | 0.034 | 22/47 (SW48, Panc 03.27, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.034 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 19/48 (AN3 CA, HT-29, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.082 | 28/47 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.082 | 12/48 (KATO III, LOX-IMVI, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -12.2 | 3e-31 | 47/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.590×** | -11.0 | 2e-25 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.610×** | -10.3 | 2e-22 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -9.1 | 1e-17 | 48/48 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -7.5 | 5e-12 | 45/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.564×** | -6.2 | 5e-08 | 46/49 (SK-MEL-2, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.861× | -3.9 | 0.007 | 19/49 (RKO, NCI-H460, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.831×** | -3.9 | 0.008 | 26/49 (NCI-H2030, A-427, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -3.8 | 0.009 | 23/49 (A498, A-427, …) | two highest doses |  |
| [[venetoclax (drug)]] 0.5 µM |  | **0.769×** | -3.7 | 0.013 | 42/49 (SK-MEL-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.845× | -3.5 | 0.022 | 18/49 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.840× | -3.5 | 0.022 | 23/48 (H4, A498, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.034 | 15/48 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.860× | -3.3 | 0.041 | 5/49 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.083 | 13/48 (A-427, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 353 | 11 (9 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +23.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.27× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.455× (z -12.8) |
| [[KATO III (line)]] | alt | 469 | 5 (5 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +14.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Belinostat (drug)]] 5 µM 0.471× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 334 | 7 (7 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.451× (z -12.3) |
| [[PANC-1 (line)]] | alt | 569 | 5 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +12.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.402× (z -17.0) |
| [[LoVo (line)]] | wt | 622 | 6 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.85× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.517× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 408 | 4 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +16.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -12.6) |
| [[A498 (line)]] | wt | 457 | 3 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.4) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -14.9) |
| [[A549 (line)]] | wt | 409 | 6 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +21.1) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.562× (z -9.1) |
| [[C32 (line)]] | wt | 356 | 5 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.461× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 611 | 6 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.8) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.556× (z -9.6) |
| [[J82 (line)]] | alt | 451 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.1) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.508× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 438 | 5 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +15.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.86× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.519× (z -9.5) |
| [[LS 180 (line)]] | wt | 569 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.87× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 377 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.7) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.408× (z -13.8) |
| [[SNU-1 (line)]] | wt | 547 | 4 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.29× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.514× (z -9.2) |
| [[SW480 (line)]] | alt | 448 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.83× (z +9.6) | — |
| [[A-172 (line)]] | wt | 460 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.7) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 5 µM 0.554× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 641 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 5 µM 0.545× (z -8.8) |
| [[A-427 (line)]] | wt | 419 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.584× (z -9.1) |
| [[H4 (line)]] | wt | 383 | 0 | 4 | — | [[Panobinostat (drug)]] 0.05 µM 0.420× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 488 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.446× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 318 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 597 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Belinostat (drug)]] 5 µM 0.539× (z -9.1) |
| [[C-33 A (line)]] | alt | 617 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.524× (z -9.5) |
| [[COLO 205 (line)]] | alt | 538 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 567 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.551× (z -10.6) |
| [[HT-29 (line)]] | alt | 496 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.85× (z +9.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.550× (z -9.9) |
| [[RKO (line)]] | wt | 784 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Belinostat (drug)]] 5 µM 0.564× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 440 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.1) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 390 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.553× (z -8.9) |
| [[SW 900 (line)]] | alt | 432 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.474× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 373 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.4) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[HepG2_C3A (line)]] | wt | 403 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 341 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.3) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 553 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.502× (z -9.3) |
| [[SHP-77 (line)]] | alt | 376 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 490 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.581× (z -8.6) |
| [[BT-474 (line)]] | alt | 473 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -9.8) |
| [[HCT15 (line)]] | alt | 717 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 444 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 323 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 419 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.550× (z -8.9) |
| [[AN3 CA (line)]] | alt | 504 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 459 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 437 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 452 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 462 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 487 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 385 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT3]] | +0.80 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.71 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SRSF6]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 599 |
| [[CHTOP]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EIF2B5]] | +0.70 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DCAF8]] | +0.69 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[MED12]] | +0.69 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SRCAP]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 | STRING 505 |
| [[USP16]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.66 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM160]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GRB2]] | -0.66 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[PDCD10]] | -0.64 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[COX5B]] | -0.64 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SRPK2]] | -0.63 | -0.63 / -0.46 | both halves | 3e-05 | STRING 569 |
| [[MPZL1]] | -0.62 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CHCHD2]] | -0.61 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MPG]] | -0.61 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[SNRPD2]] | -0.60 | -0.45 / -0.50 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions; STRING 992 |
| [[SEC11A]] | -0.60 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[SCAI]] | -0.60 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NHP2]] | -0.59 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNM]] | B | SYNM activity lowers SRRM2's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.32× higher at baseline in the lines without SYNM | 0.015 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises SRRM2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.8, 4.0); signed map (15.5, -22.9). **Vector** length 118, 43.2% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +11.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.2 | +8.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.3 | +1.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +3.0 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.4 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -9.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -3.1 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | serine/arginine repetitive matrix 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,752,626-2,772,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRm300, SRL300, KIAA0324, Cwc21 |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ35](https://www.uniprot.org/uniprotkb/Q9UQ35) (Serine/arginine repetitive matrix protein 2):

> Required for pre-mRNA splicing as component of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [23524](https://www.ncbi.nlm.nih.gov/gene/23524):

> Enables C2H2 zinc finger domain binding activity. Involved in mRNA splicing, via spliceosome. Located in Cajal body and nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in autosomal dominant intellectual developmental disorder 72. Biomarker of Parkinson's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16639) · Entrez [23524](https://www.ncbi.nlm.nih.gov/gene/23524) · UniProt [Q9UQ35](https://www.uniprot.org/uniprotkb/Q9UQ35) · Ensembl [ENSG00000167978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167978)

## Data

Gene col 9568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9568); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9568]; `tensor/DDL_lfc|DDL_z.npy` [9568]; `embed/gene_vectors.npy` [9568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9568 or target_col == 9568). Every well: [[SRRM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
