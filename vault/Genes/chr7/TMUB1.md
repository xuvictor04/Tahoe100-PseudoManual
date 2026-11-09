---
symbol: "TMUB1"
type: "gene"
col: 9023
ensembl_id: "ENSG00000164897"
name: "transmembrane and ubiquitin like domain containing 1"
location: "7q36.1"
module: 30
arm: "+"
pooled_cpm: 14.26
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TMUB1

*transmembrane and ubiquitin like domain containing 1* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.16× (z +6.2, q 3e-07, up in 10 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 4.45×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.364× (z -17.6, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC42]] (+0.72, fdr 7e-06), [[UBAC1]] (+0.67, fdr 1e-05), [[BAG4]] (+0.66, fdr 1e-05); moves opposite to [[NEPRO-AS1]] (-0.63, fdr 3e-05), [[ARRDC3-AS1]] (-0.58, fdr 5e-05), [[RGS5]] (-0.57, fdr 9e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 4.45×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.2 | 3e-07 | 10/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +6.1 | 3e-07 | 24/41 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.6 | 9e-04 | 12/27 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.7 | 0.026 | 15/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.22 | 11/44 (CFPAC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.364×** | -17.6 | 0e+00 | 44/47 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.380×** | -11.9 | 4e-30 | 42/45 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -7.9 | 6e-13 | 34/47 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -6.6 | 5e-09 | 34/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -6.5 | 1e-08 | 30/48 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -5.7 | 1e-06 | 28/48 (A498, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -4.7 | 2e-04 | 22/46 (SK-MEL-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -4.7 | 2e-04 | 18/48 (A-172, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.766×** | -4.6 | 2e-04 | 26/46 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.700×** | -4.2 | 0.001 | 21/46 (NCI-H2030, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.2 | 0.001 | 18/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -3.8 | 0.006 | 18/46 (hTERT-HPNE, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -3.8 | 0.008 | 19/46 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.732×** | -3.6 | 0.011 | 20/47 (A549, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -3.6 | 0.011 | 16/45 (J82, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.011 | 19/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.750×** | -3.5 | 0.013 | 16/47 (BT-474, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -17.1) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.9) |
| [[BT-474 (line)]] | alt | 8.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.9) |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0880× (z -10.2) |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.4) |
| [[SW48 (line)]] | wt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0457× (z -14.3) |
| [[A549 (line)]] | wt | 9.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 9.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -16.2) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.2) |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.2) |
| [[KATO III (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.9) |
| [[LoVo (line)]] | wt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -15.8) |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 8.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.1) |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -12.6) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.1) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC42]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.67 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[BAG4]] | +0.66 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RUSC1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.65 | +0.78 / +0.33 | both halves | 1e-04 |  |
| [[GET1]] | +0.65 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[ALKBH5]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.62 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[PHAF1]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PRRC1]] | +0.62 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.63 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.58 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[RGS5]] | -0.57 | -0.66 / -0.37 | both halves | 9e-05 |  |
| [[MSRA]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[FKRP]] | -0.56 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[GABPB2]] | -0.55 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[ITPR2-AS1]] | -0.55 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[KRR1]] | -0.55 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[JPX]] | -0.55 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | -0.54 | -0.63 / -0.23 | both halves | 5e-04 |  |
| [[HNRNPA2B1]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[ST7L]] | -0.54 | -0.65 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.8, -14.0); signed map (-39.6, -0.8). **Vector** length 64.9, 11.0% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.4 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.3 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -7.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and ubiquitin like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,081,085-151,083,493 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SB144, HOPS; previously C7orf21 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVT8](https://www.uniprot.org/uniprotkb/Q9BVT8) (Transmembrane and ubiquitin-like domain-containing protein 1):

> Involved in sterol-regulated ubiquitination and degradation of HMG-CoA reductase HMGCR. Involved in positive regulation of AMPA-selective glutamate receptor GRIA2 recycling to the cell surface (By similarity). Acts as a negative regulator of hepatocyte growth during regeneration (By similarity).; [iHOPS]: May contribute to the regulation of translation during cell-cycle progression. May contribute to the regulation of cell proliferation (By similarity). May be involved in centrosome assembly. …

**Summary**, from NCBI Gene [83590](https://www.ncbi.nlm.nih.gov/gene/83590):

> Involved in ERAD pathway. Predicted to be located in several cellular components, including centrosome; postsynaptic membrane; and recycling endosome. Predicted to be active in postsynaptic recycling endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21709) · Entrez [83590](https://www.ncbi.nlm.nih.gov/gene/83590) · UniProt [Q9BVT8](https://www.uniprot.org/uniprotkb/Q9BVT8) · Ensembl [ENSG00000164897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164897)

## Data

Gene col 9023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9023); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9023]; `tensor/DDL_lfc|DDL_z.npy` [9023]; `embed/gene_vectors.npy` [9023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9023 or target_col == 9023). Every well: [[TMUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
