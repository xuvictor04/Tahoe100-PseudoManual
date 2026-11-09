---
symbol: "CLEC16A"
type: "gene"
col: 456
ensembl_id: "ENSG00000038532"
name: "C-type lectin domain containing 16A"
location: "16p13.13"
module: 211
arm: "+"
pooled_cpm: 86.24
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# CLEC16A

*C-type lectin domain containing 16A* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.82× (z +31.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.705× (z -8.1, q 3e-13, down in 31 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.797× (z -7.5, q 2e-11, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK3]] (+0.57, fdr 3e-05), [[RABGAP1L]] (+0.54, fdr 1e-05), [[RABEP1]] (+0.53, fdr 1e-05); moves opposite to [[GOT1-DT]] (-0.56, fdr 2e-04), [[PMS2]] (-0.55, fdr 3e-05), [[EEF1AKMT3]] (-0.54, fdr 2e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.82×** | +31.2 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.53×** | +29.4 | 0e+00 | 48/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.49×** | +29.2 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +23.7 | 0e+00 | 39/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +19.4 | 0e+00 | 35/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +15.1 | 0e+00 | 47/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +12.6 | 2e-34 | 45/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +9.5 | 2e-19 | 45/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +7.8 | 4e-13 | 35/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +7.7 | 5e-13 | 42/48 (A549, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 1e-08 | 26/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +6.2 | 2e-08 | 32/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +5.4 | 3e-06 | 26/48 (COLO 205, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +5.4 | 3e-06 | 25/50 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.3 | 3e-06 | 20/48 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +4.4 | 4e-04 | 22/49 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 18/47 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.011 | 7/48 (HepG2/C3A, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.012 | 21/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.013 | 17/48 (LoVo, HepG2/C3A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.705×** | -8.1 | 3e-13 | 31/49 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.797×** | -7.5 | 2e-11 | 28/48 (KATO III, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.731×** | -6.7 | 3e-09 | 28/45 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -6.7 | 3e-09 | 25/44 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.780×** | -5.8 | 8e-07 | 29/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.7 | 2e-04 | 23/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.703×** | -4.3 | 0.001 | 23/48 (HS-578T, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.839× | -3.8 | 0.012 | 19/47 (CHP-212, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.851× | -3.6 | 0.020 | 20/47 (SHP-77, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.870× | -3.2 | 0.070 | 13/48 (AN3 CA, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 160 | 9 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 142 | 4 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.530× (z -13.3) |
| [[SW480 (line)]] | alt | 115 | 7 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.659× (z -10.5) |
| [[BT-474 (line)]] | alt | 92.8 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +27.3) | — |
| [[A-172 (line)]] | wt | 82.9 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +20.8) | — |
| [[HEC-1-A (line)]] | alt | 95.5 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -12.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 106 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +38.7) | [[Docetaxel (drug)]] 0.05 µM 0.510× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 96.4 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +17.9) | — |
| [[A549 (line)]] | wt | 69.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.87× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 94.6 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.95× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 85.0 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.32× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 63.3 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 133 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 64.2 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +20.8) | — |
| [[HOP62 (line)]] | alt | 48.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.38× (z +19.5) | — |
| [[HS-578T (line)]] | alt | 66.7 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 5.19× (z +19.2) | [[Selinexor (drug)]] 5 µM 0.574× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 68.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.51× (z +18.3) | — |
| [[J82 (line)]] | alt | 65.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +30.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.28× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +21.6) | — |
| [[SK-MEL-2 (line)]] | alt | 86.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 56.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.39× (z +19.7) | — |
| [[SW48 (line)]] | wt | 87.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 154 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.58× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 76.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 91.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 104 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.93× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 93.5 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 3.53× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 80.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -13.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 63.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +14.7) | — |
| [[SHP-77 (line)]] | alt | 133 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 74.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +12.5) | [[Simotinib (drug)]] 5 µM 0.389× (z -8.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 55.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +13.0) | — |
| [[LoVo (line)]] | wt | 98.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 70.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 70.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.05× (z +14.8) | — |
| [[SNU-1 (line)]] | wt | 69.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 105 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +16.2) | — |
| [[A-427 (line)]] | wt | 71.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +15.9) | — |
| [[C32 (line)]] | wt | 104 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 77.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.7) | — |
| [[RKO (line)]] | wt | 115 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 74.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 93.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +12.6) | — |
| [[NCI-H2122 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK3]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[RABGAP1L]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RABEP1]] | +0.53 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[VPS13D]] | +0.53 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[HSD17B10]] ⚠ | +0.51 | +0.52 / +0.37 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SCAPER]] | +0.50 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[EIF4G3]] | +0.50 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FER]] | +0.50 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PPP6R2]] | +0.49 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ATP9B]] | +0.49 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[ZNF609]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TJP1]] | +0.48 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[NUTM2B-AS1]] | +0.47 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT1-DT]] | -0.56 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[PMS2]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[EEF1AKMT3]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[DYNLT2]] | -0.52 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[ZNF589]] | -0.52 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[NIPBL-DT]] | -0.52 | -0.17 / -0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[PHOSPHO2]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ZNF141]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MRPS30-DT]] | -0.51 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[CTTN-DT]] | -0.50 | -0.07 / -0.52 | ⚠ one half (not replicated) | 0.004 |  |
| [[TIGD1]] | -0.50 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[VAMP1]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ZNF17]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LINC00115]] | -0.49 | -0.37 / -0.56 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLEC16A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.0, 22.6); signed map (-1.5, -9.9). **Vector** length 96.0, 27.4% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +19.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.5 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.9 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.4 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | +0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.5 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | C-type lectin domain containing 16A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:10,944,539-11,182,186 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gop-1; previously KIAA0350 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2KHT3](https://www.uniprot.org/uniprotkb/Q2KHT3) (Protein CLEC16A):

> Regulator of mitophagy through the upstream regulation of the RNF41/NRDP1-PRKN pathway. Mitophagy is a selective form of autophagy necessary for mitochondrial quality control. The RNF41/NRDP1-PRKN pathway regulates autophagosome-lysosome fusion during late mitophagy. May protect RNF41/NRDP1 from proteasomal degradation, RNF41/NRDP1 which regulates proteasomal degradation of PRKN. Plays a key role in beta cells functions by regulating mitophagy/autophagy and mitochondrial health.

**Summary**, from NCBI Gene [23274](https://www.ncbi.nlm.nih.gov/gene/23274):

> This gene encodes a member of the C-type lectin domain containing family. Single nucleotide polymorphisms in introns of this gene have been associated with diabetes mellitus, multiple sclerosis and rheumatoid arthritis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:29013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29013) · Entrez [23274](https://www.ncbi.nlm.nih.gov/gene/23274) · UniProt [Q2KHT3](https://www.uniprot.org/uniprotkb/Q2KHT3) · Ensembl [ENSG00000038532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038532)

## Data

Gene col 456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 456); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 456]; `tensor/DDL_lfc|DDL_z.npy` [456]; `embed/gene_vectors.npy` [456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 456 or target_col == 456). Every well: [[CLEC16A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLEC16A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
