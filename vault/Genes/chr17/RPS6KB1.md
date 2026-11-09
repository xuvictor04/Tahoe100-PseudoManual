---
symbol: "RPS6KB1"
type: "gene"
col: 2948
ensembl_id: "ENSG00000108443"
name: "ribosomal protein S6 kinase B1"
location: "17q23.1"
module: 69
arm: "+"
pooled_cpm: 89.26
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# RPS6KB1

*ribosomal protein S6 kinase B1* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +19.2, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.717× (z -7.5, q 4e-11, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.230×, Panc 03.27 0.358×, SW48 0.245×, CHP-212 0.252×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (CHP-212 0.241×, C32 0.304×, HEC-1-A 0.464×, RKO 0.436×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 0.331×, C-33 A 0.328×, Panc 03.27 0.435×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.388×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLPX]] (+0.55, fdr 1e-05), [[AMBRA1]] (+0.47, fdr 4e-05), [[PAN3]] (+0.46, fdr 2e-04); moves opposite to [[FOSL1]] (-0.48, fdr 6e-05), [[TM4SF19]] (-0.43, fdr 4e-05), [[ZNF215]] (-0.42, fdr 4e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +19.2 | 0e+00 | 43/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +15.2 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +11.0 | 5e-26 | 42/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +10.7 | 2e-24 | 39/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +10.3 | 1e-22 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.1 | 7e-22 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +10.0 | 1e-21 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.7 | 3e-20 | 39/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +9.4 | 3e-19 | 36/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +8.8 | 1e-16 | 40/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +8.6 | 5e-16 | 36/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +7.6 | 1e-12 | 32/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.6 | 2e-12 | 32/48 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-07 | 28/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +5.7 | 6e-07 | 33/49 (Panc 03.27, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +5.0 | 2e-05 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.8 | 5e-05 | 20/48 (A-172, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2948.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.230×, Panc 03.27 0.358×, SW48 0.245×, CHP-212 0.252×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (CHP-212 0.241×, C32 0.304×, HEC-1-A 0.464×, RKO 0.436×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 0.331×, C-33 A 0.328×, Panc 03.27 0.435×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.388×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.717×** | -7.5 | 4e-11 | 30/45 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.757×** | -6.8 | 3e-09 | 28/49 (CHP-212, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -5.6 | 4e-06 | 27/44 (SW 900, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.860× | -3.7 | 0.034 | 13/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~5% of this change | 0.863× | -3.6 | 0.036 | 21/48 (SW1417, H4, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.0 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +19.9) | — |
| [[NCI-H460 (line)]] | wt | 79.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +19.6) | — |
| [[BT-474 (line)]] | alt | 472 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.1) | [[Lonafarnib (drug)]] 5 µM 0.216× (z -11.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 82.1 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 71.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +23.2) | — |
| [[KATO III (line)]] | alt | 114 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 60.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +14.6) | — |
| [[A-172 (line)]] | wt | 63.4 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -13.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 119 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -11.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[C32 (line)]] | wt | 64.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 93.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 80.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.0) | — |
| [[J82 (line)]] | alt | 59.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 63.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 86.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.8) | — |
| [[NCI-H1792 (line)]] | alt | 94.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 81.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 104 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.20× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 84.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +25.8) | — |
| [[CFPAC-1 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.7) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 209 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 89.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.9) | — |
| [[HepG2_C3A (line)]] | wt | 96.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 67.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 63.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 80.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +20.4) | — |
| [[RKO (line)]] | wt | 78.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 97.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.4) | — |
| [[A-427 (line)]] | wt | 113 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.86× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +24.9) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[C-33 A (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -11.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.140× (z -9.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 88.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.388× (z -9.6) |
| [[Hs 766T (line)]] | wt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 78.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPX]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[AMBRA1]] | +0.47 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[PAN3]] | +0.46 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[NTN4]] | +0.46 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[CP]] | +0.46 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[CD38]] | +0.46 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DHX8]] | +0.45 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[NEK7]] | +0.45 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[BMPR2]] | +0.45 | +0.41 / +0.30 | both halves | 2e-04 |  |
| [[KDM6A]] | +0.44 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[PCMTD1]] | +0.44 | +0.49 / +0.26 | both halves | 4e-04 |  |
| [[STRN3]] | +0.44 | +0.28 / +0.47 | both halves | 3e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSL1]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TM4SF19]] | -0.43 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ZNF215]] | -0.42 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[NRIP3]] | -0.42 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[NGEF]] | -0.41 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[ADTRP]] | -0.41 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ARFGEF3]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[N4BP3]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[LCP1]] | -0.41 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[ENTPD7]] | -0.39 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[TMSB15B]] | -0.39 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[LINC02970]] | -0.39 | -0.32 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, -10.8); signed map (-14.5, 12.8). **Vector** length 61.3, 12.3% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +8.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +2.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,893,046-59,950,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S6K1, p70(S6K)-alpha, PS6K, S6K; previously STK14A |
| Gene groups (HGNC) | Ribosomal protein S6 kinase family |
| Reactome | 2 pathways, smallest: mTORC1-mediated signalling; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P23443](https://www.uniprot.org/uniprotkb/P23443) (Ribosomal protein S6 kinase beta-1):

> Serine/threonine-protein kinase that acts downstream of mTOR signaling in response to growth factors and nutrients to promote cell proliferation, cell growth and cell cycle progression. Regulates protein synthesis through phosphorylation of EIF4B, RPS6 and EEF2K, and contributes to cell survival by repressing the pro-apoptotic function of BAD. Under conditions of nutrient depletion, the inactive form associates with the EIF3 translation initiation complex. Upon mitogenic stimulation, …

**Summary**, from NCBI Gene [6198](https://www.ncbi.nlm.nih.gov/gene/6198):

> This gene encodes a member of the ribosomal S6 kinase family of serine/threonine kinases. The encoded protein responds to mTOR (mammalian target of rapamycin) signaling to promote protein synthesis, cell growth, and cell proliferation. Activity of this gene has been associated with human cancer. Alternatively spliced transcript variants have been observed. The use of alternative translation start sites results in isoforms with longer or shorter N-termini which may differ in their subcellular …

**Accessions** — [HGNC:10436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10436) · Entrez [6198](https://www.ncbi.nlm.nih.gov/gene/6198) · UniProt [P23443](https://www.uniprot.org/uniprotkb/P23443) · Ensembl [ENSG00000108443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108443)

## Data

Gene col 2948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2948); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2948]; `tensor/DDL_lfc|DDL_z.npy` [2948]; `embed/gene_vectors.npy` [2948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2948 or target_col == 2948). Every well: [[RPS6KB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
