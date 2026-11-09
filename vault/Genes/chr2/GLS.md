---
symbol: "GLS"
type: "gene"
col: 3672
ensembl_id: "ENSG00000115419"
name: "glutaminase"
location: "2q32.2"
module: 119
arm: "+"
pooled_cpm: 374.28
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# GLS

*glutaminase* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +23.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.756× (z -3.9, q 0.041, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 0.5 µM in 2 lines (SW480 0.473×, NCI-H23 0.471×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SW480 0.408×, NCI-H23 0.361×); [[Binimetinib (drug)]] 0.5 µM in 2 lines (SW480 0.535×, NCI-H23 0.497×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L2]] (+0.57, fdr 6e-05), [[ITGA6]] (+0.56, fdr 1e-05), [[C3orf52]] (+0.56, fdr 1e-05); moves opposite to [[RBSN]] (-0.62, fdr 7e-06), [[GUSBP2-1]] (-0.60, fdr 1e-05), [[YTHDF1]] (-0.60, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +23.1 | 0e+00 | 46/48 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.73×** | +14.3 | 4e-44 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +12.8 | 5e-35 | 41/49 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +11.8 | 3e-30 | 42/48 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.16×** | +11.0 | 5e-26 | 44/48 (HS-578T, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +10.7 | 7e-25 | 42/48 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +10.3 | 8e-23 | 43/48 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +10.1 | 3e-22 | 47/48 (A-172, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +9.4 | 2e-19 | 43/48 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +9.4 | 3e-19 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +9.4 | 4e-19 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.86×** | +8.8 | 5e-17 | 39/48 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +8.8 | 6e-17 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.81×** | +8.1 | 2e-14 | 41/50 (C32, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +7.2 | 2e-11 | 42/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.5 | 2e-09 | 44/49 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.5 | 3e-09 | 40/48 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +6.3 | 9e-09 | 38/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.7 | 4e-07 | 34/48 (BT-474, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 1e-06 | 36/48 (KATO III, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3672.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 0.5 µM in 2 lines (SW480 0.473×, NCI-H23 0.471×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SW480 0.408×, NCI-H23 0.361×); [[Binimetinib (drug)]] 0.5 µM in 2 lines (SW480 0.535×, NCI-H23 0.497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.756×** | -3.9 | 0.041 | 28/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.692×** | -3.8 | 0.041 | 36/48 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.843× | -3.4 | 0.13 | 22/49 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.15 | 27/48 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.801× | -3.2 | 0.15 | 24/49 (SW480, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.809× | -3.1 | 0.15 | 26/48 (NCI-H661, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.809× | -3.1 | 0.15 | 25/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.15 | 25/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.811× | -3.0 | 0.15 | 26/48 (NCI-H23, KATO III, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 287 | 10 (2 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +20.2) | [[Adagrasib (drug)]] 0.05 µM 0.605× (z -19.0) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.361× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 297 | 18 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.50× (z +19.5) | — |
| [[SW480 (line)]] | alt | 398 | 6 (2 ⚠) | 10 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.9) | [[Trametinib (drug)]] 0.5 µM 0.473× (z -11.5) |
| [[HT-29 (line)]] | alt | 199 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +21.0) | — |
| [[A-427 (line)]] | wt | 187 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +21.0) | — |
| [[HS-578T (line)]] | alt | 250 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +25.5) | — |
| [[SW 900 (line)]] | alt | 195 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +21.9) | — |
| [[hTERT-HPNE (line)]] | wt | 275 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +26.5) | — |
| [[KATO III (line)]] | alt | 185 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +16.9) | — |
| [[A-172 (line)]] | wt | 387 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +22.0) | — |
| [[HOP62 (line)]] | alt | 334 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +24.2) | — |
| [[A498 (line)]] | wt | 746 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +25.5) | — |
| [[A549 (line)]] | wt | 320 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.0) | — |
| [[J82 (line)]] | alt | 385 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +19.7) | — |
| [[PANC-1 (line)]] | alt | 238 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.7) | — |
| [[C32 (line)]] | wt | 351 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +22.8) | — |
| [[HepG2_C3A (line)]] | wt | 360 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +14.7) | — |
| [[Hs 766T (line)]] | wt | 292 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.0) | — |
| [[RPMI-7951 (line)]] | alt | 358 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.6) | — |
| [[BT-474 (line)]] | alt | 179 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 137 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +23.8) | — |
| [[NCI-H1573 (line)]] | alt | 347 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +17.8) | — |
| [[SNU-423 (line)]] | alt | 239 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.8) | — |
| [[HCT15 (line)]] | alt | 257 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +15.0) | — |
| [[RKO (line)]] | wt | 483 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 725 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +20.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 279 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 386 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 270 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +19.9) | — |
| [[H4 (line)]] | wt | 391 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 242 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +24.3) | — |
| [[C-33 A (line)]] | alt | 218 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 556 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 287 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.6) | — |
| [[SHP-77 (line)]] | alt | 265 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 347 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.5) | — |
| [[SW1417 (line)]] | alt | 718 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.3) | — |
| [[SW48 (line)]] | wt | 305 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 282 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 483 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | — |
| [[LoVo (line)]] | wt | 389 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 546 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 472 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 441 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 526 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 706 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 293 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | +0.57 | +0.39 / +0.68 | both halves | 6e-05 | pathway: Neuronal System |
| [[ITGA6]] | +0.56 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[C3orf52]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ASPH]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TBILA]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PITRM1]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[DIAPH1]] | +0.55 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CTNNA1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TEX14]] | +0.54 | +0.36 / +0.65 | both halves | 1e-04 | same gene group |
| [[YWHAZ]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[TFRC]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_UP |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBSN]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[GUSBP2-1]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[YTHDF1]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[GTF3C2]] | -0.59 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ZNF16]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[BRPF1]] | -0.57 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ALKBH4]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ZNF576]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TIMM29]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[BRAP]] | -0.55 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[VIRMA]] | -0.55 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TMEM11]] | -0.55 | -0.44 / -0.67 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction -0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.6, -6.0); signed map (-7.9, 37.0). **Vector** length 107, 45.5% of its response variance represented; |z| ≥ 3 in 1,722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.3 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -9.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | +23.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.3 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | glutaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,880,821-190,965,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0838, GLS1, GAC, GAM, KGA |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 8 pathways, smallest: Glutamate and glutamine metabolism; Glutamate Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O94925](https://www.uniprot.org/uniprotkb/O94925) (Glutaminase kidney isoform, mitochondrial):

> Catalyzes the first reaction in the primary pathway for the renal catabolism of glutamine. Plays a role in maintaining acid-base homeostasis. Regulates the levels of the neurotransmitter glutamate, the main excitatory neurotransmitter in the brain.; [Isoform 2]: Lacks catalytic activity.

**Summary**, from NCBI Gene [2744](https://www.ncbi.nlm.nih.gov/gene/2744):

> This gene encodes the K-type mitochondrial glutaminase. The encoded protein is an phosphate-activated amidohydrolase that catalyzes the hydrolysis of glutamine to glutamate and ammonia. This protein is primarily expressed in the brain and kidney plays an essential role in generating energy for metabolism, synthesizing the brain neurotransmitter glutamate and maintaining acid-base balance in the kidney. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:4331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4331) · Entrez [2744](https://www.ncbi.nlm.nih.gov/gene/2744) · UniProt [O94925](https://www.uniprot.org/uniprotkb/O94925) · Ensembl [ENSG00000115419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115419)

## Data

Gene col 3672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3672); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3672]; `tensor/DDL_lfc|DDL_z.npy` [3672]; `embed/gene_vectors.npy` [3672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3672 or target_col == 3672). Every well: [[GLS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
