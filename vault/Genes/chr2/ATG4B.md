---
symbol: "ATG4B"
type: "gene"
col: 9643
ensembl_id: "ENSG00000168397"
name: "autophagy related 4B cysteine peptidase"
location: "2q37.3"
module: 3
arm: "+"
pooled_cpm: 50.66
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ATG4B

*autophagy related 4B cysteine peptidase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.33× (z +26.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.553× (z -13.0, q 1e-35, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.831× (z -4.1, q 0.007, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.0745×, NCI-H1573 0.0952×, A549 0.275×, CFPAC-1 0.351×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.190×, RKO 0.165×, NCI-H1792 0.329×, H4 0.207×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.175×, A-172 0.253×, NCI-H23 0.306×, Panc 03.27 0.296×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3GL1]] (+0.79, fdr 7e-06), [[MRPL55]] (+0.73, fdr 1e-05), [[ARID3A]] (+0.71, fdr 7e-06); moves opposite to [[CHRAC1]] (-0.68, fdr 1e-05), [[HNRNPK]] (-0.68, fdr 1e-05), [[GALNT7]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLS3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.33×** | +26.2 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.25×** | +25.7 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.71×** | +21.7 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +11.7 | 1e-29 | 37/48 (BT-474, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +11.4 | 5e-28 | 40/49 (NCI-H1573, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +11.4 | 5e-28 | 33/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +9.9 | 2e-21 | 39/48 (COLO 205, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.1 | 8e-18 | 33/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +8.6 | 5e-16 | 35/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +8.4 | 4e-15 | 37/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.5 | 4e-12 | 32/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 3e-07 | 33/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.2 | 1e-05 | 23/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.9 | 4e-05 | 27/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.9 | 5e-05 | 26/49 (HEC-1-A, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 1e-04 | 20/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.0745×, NCI-H1573 0.0952×, A549 0.275×, CFPAC-1 0.351×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.190×, RKO 0.165×, NCI-H1792 0.329×, H4 0.207×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.175×, A-172 0.253×, NCI-H23 0.306×, Panc 03.27 0.296×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.553×** | -13.0 | 1e-35 | 39/49 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -10.6 | 9e-24 | 30/42 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -7.9 | 5e-13 | 26/45 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.831×** | -4.1 | 0.007 | 19/48 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.013 | 16/47 (SW 1271, NCI-H1792, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -3.7 | 0.023 | 12/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.891× | -3.4 | 0.058 | 6/48 (H4, C32, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.860× | -3.3 | 0.064 | 13/49 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.2 | 0.086 | 10/48 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.964× | -3.2 | 0.086 | 1/49 (SW 1271) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.086 | 8/49 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.870× | -3.1 | 0.11 | 4/48 (NCI-H661, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 75.3 | 10 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -22.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 59.0 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.52× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.545× (z -8.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 58.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +19.9) | — |
| [[BT-474 (line)]] | alt | 49.7 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.42× (z +15.0) | — |
| [[KATO III (line)]] | alt | 49.4 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.0745× (z -25.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 51.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -17.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.98× (z +12.4) | — |
| [[A549 (line)]] | wt | 42.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -11.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 38.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 59.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 56.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 35.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 44.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.63× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.31× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 62.4 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.54× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 65.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 69.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +13.0) | — |
| [[RKO (line)]] | wt | 61.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -16.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.2) | — |
| [[SW48 (line)]] | wt | 48.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +9.1) | — |
| [[A498 (line)]] | wt | 36.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 46.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.61× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.9) | — |
| [[J82 (line)]] | alt | 30.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 61.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 57.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 37.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 54.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +9.9) | — |
| [[H4 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 67.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 78.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.64× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GL1]] | +0.79 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.73 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.71 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.71 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.71 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[SDHAP2]] | +0.70 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MPG]] | +0.70 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[UBE2O]] | +0.68 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NPRL2]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.68 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRAC1]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.68 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GALNT7]] | -0.67 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.66 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SEPTIN11]] | -0.66 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SNX5]] | -0.64 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[OXCT1]] | -0.63 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[LEPROT]] | -0.63 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SLC39A10]] | -0.63 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[PHACTR2]] | -0.63 | -0.54 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3]] | C | PLS3 activity weakens ATG4B's drug response | lines that do not express PLS3 (4) vs lines expressing it (45) | the lines without PLS3 respond 1.11× as strongly (z diff -1.16); strongest at Auranofin 5 µM: 3.29x vs 1.63x (z diff -4.7) | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.0, -15.1); signed map (-29.2, 13.6). **Vector** length 87.2, 22.2% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.9 | +26.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +25.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +21.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +3.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.6 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 4B cysteine peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,637,213-241,673,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Apg4B, KIAA0943, DKFZp586D1822, AUTL1; previously APG4B |
| Gene groups (HGNC) | Autophagy related; Autophagy related 4 family cysteine peptidases |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4P1](https://www.uniprot.org/uniprotkb/Q9Y4P1) (Cysteine protease ATG4B):

> Cysteine protease that plays a key role in autophagy by mediating both proteolytic activation and delipidation of ATG8 family proteins. Required for canonical autophagy (macroautophagy), non-canonical autophagy as well as for mitophagy. The protease activity is required for proteolytic activation of ATG8 family proteins: cleaves the C-terminal amino acid of ATG8 proteins MAP1LC3A, MAP1LC3B, MAP1LC3C, GABARAPL1, GABARAPL2 and GABARAP, to reveal a C-terminal glycine. Exposure of the glycine at …

**Summary**, from NCBI Gene [23192](https://www.ncbi.nlm.nih.gov/gene/23192):

> Autophagy is the process by which endogenous proteins and damaged organelles are destroyed intracellularly. Autophagy is postulated to be essential for cell homeostasis and cell remodeling during differentiation, metamorphosis, non-apoptotic cell death, and aging. Reduced levels of autophagy have been described in some malignant tumors, and a role for autophagy in controlling the unregulated cell growth linked to cancer has been proposed. This gene encodes a member of the autophagin protein …

**Accessions** — [HGNC:20790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20790) · Entrez [23192](https://www.ncbi.nlm.nih.gov/gene/23192) · UniProt [Q9Y4P1](https://www.uniprot.org/uniprotkb/Q9Y4P1) · Ensembl [ENSG00000168397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168397)

## Data

Gene col 9643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9643); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9643]; `tensor/DDL_lfc|DDL_z.npy` [9643]; `embed/gene_vectors.npy` [9643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9643 or target_col == 9643). Every well: [[ATG4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
