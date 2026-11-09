---
symbol: "ABHD2"
type: "gene"
col: 6425
ensembl_id: "ENSG00000140526"
name: "abhydrolase domain containing 2, acylglycerol lipase"
location: "15q26.1"
module: 97
arm: "+"
pooled_cpm: 116.8
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ABHD2

*abhydrolase domain containing 2, acylglycerol lipase* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.44× (z +17.7, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -12.8, q 6e-35, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A1]] (+0.61, fdr 7e-06), [[AKAP13]] (+0.57, fdr 3e-05), [[ZDHHC3]] (+0.55, fdr 1e-05); moves opposite to [[HOXD3]] (-0.53, fdr 2e-04), [[ZNF425]] (-0.53, fdr 3e-04), [[HMGN2P46]] (-0.53, fdr 2e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +17.7 | 0e+00 | 39/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +17.1 | 0e+00 | 40/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +15.9 | 0e+00 | 41/47 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +9.5 | 2e-19 | 31/47 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.45×** | +7.2 | 5e-11 | 29/48 (C-33 A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.0 | 2e-10 | 28/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.0 | 3e-10 | 32/47 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.42×** | +6.8 | 1e-09 | 23/39 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +6.5 | 4e-09 | 27/48 (A549, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +6.2 | 4e-08 | 29/46 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.6 | 9e-07 | 28/47 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +5.6 | 1e-06 | 27/47 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.22×** | +5.6 | 1e-06 | 22/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.27×** | +4.8 | 7e-05 | 23/47 (A-172, A549, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 3e-04 | 23/46 (SW480, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.001 | 24/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 22/47 (A549, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.008 | 18/47 (A549, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.18× | +3.2 | 0.037 | 21/47 (A549, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -12.8 | 6e-35 | 35/47 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -9.3 | 3e-18 | 32/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -6.2 | 9e-08 | 27/47 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.747×** | -5.6 | 3e-06 | 26/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -4.5 | 7e-04 | 24/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.655×** | -4.4 | 1e-03 | 22/48 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -4.3 | 0.001 | 20/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -3.8 | 0.010 | 17/47 (LS 180, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.842× | -3.3 | 0.057 | 19/47 (LoVo, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.085 | 21/47 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.885× | -3.1 | 0.090 | 17/48 (LoVo, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.090 | 17/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.090 | 17/47 (COLO 205, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 95.9 | 18 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.5) |
| [[A498 (line)]] | wt | 109 | 10 | 0 | [[Budesonide (drug)]] 0.5 µM 2.55× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 567 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0876× (z -33.0) |
| [[SW480 (line)]] | alt | 321 | 2 (1 ⚠) | 6 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.38× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -18.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.474× (z -8.5) |
| [[A-172 (line)]] | wt | 50.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 509 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 51.8 | 4 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.2) |
| [[LoVo (line)]] | wt | 199 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.454× (z -9.2) |
| [[RKO (line)]] | wt | 62.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.04× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0950× (z -22.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 62.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.42× (z +15.7) | — |
| [[KATO III (line)]] | alt | 373 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 54.4 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.55× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 65.9 | 3 | 1 | [[Belinostat (drug)]] 5 µM 2.57× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 71.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +10.6) | — |
| [[J82 (line)]] | alt | 53.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 52.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 56.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 54.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +16.4) | — |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.6) |
| [[SNU-423 (line)]] | alt | 76.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.13× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 50.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 87.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.1) |
| [[HT-29 (line)]] | alt | 331 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -14.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 64.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 67.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.13× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -8.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 39.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 68.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 70.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.3) |
| [[SHP-77 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -8.5) |
| [[SW 900 (line)]] | alt | 73.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.1) |
| [[SW48 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A1]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[AKAP13]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC3]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ENTPD6]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D8]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[APMAP]] | +0.53 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[ACTN4]] | +0.52 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[MPRIP]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PPARG]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TGOLN2]] | +0.51 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[DIAPH1]] | +0.50 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[TGFBR2]] | +0.50 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXD3]] | -0.53 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ZNF425]] | -0.53 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[HMGN2P46]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MSANTD3]] | -0.52 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[ZDBF2]] | -0.52 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[NEURL3]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ATF5]] | -0.50 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[LINC02384]] | -0.49 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[DHDH]] | -0.49 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[LINC02100]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MSANTD3-TMEFF1]] | -0.48 | -0.58 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[AGBL2]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[N4BP2L1]] | -0.47 | -0.42 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises ABHD2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without TBC1D8 | 0.023 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[TNS4]] | B | TNS4 activity raises ABHD2's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.14× lower at baseline in the lines without TNS4 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[PPARG]] | B | PPARG activity raises ABHD2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without PPARG | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 11.6); signed map (12.0, 34.2). **Vector** length 138, 41.7% of its response variance represented; |z| ≥ 3 in 1,609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +8.3 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +7.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +7.0 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +6.6 | +6.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.1 | +3.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.1 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.9 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 2, acylglycerol lipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,087,459-89,202,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LABH2 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P08910](https://www.uniprot.org/uniprotkb/P08910) (Monoacylglycerol lipase ABHD2):

> Progesterone-dependent acylglycerol lipase that catalyzes hydrolysis of endocannabinoid arachidonoylglycerol (AG) from cell membrane. Acts as a progesterone receptor: progesterone-binding activates the acylglycerol lipase activity, mediating degradation of 1-arachidonoylglycerol (1AG) and 2-arachidonoylglycerol (2AG) to glycerol and arachidonic acid (AA). Also displays an ester hydrolase activity against acetyl ester, butanoate ester and hexadecanoate ester. Plays a key role in sperm …

**Summary**, from NCBI Gene [11057](https://www.ncbi.nlm.nih.gov/gene/11057):

> This gene encodes a protein containing an alpha/beta hydrolase fold, which is a catalytic domain found in a wide range of enzymes. The encoded protein is an acylglycerol lipase that catalyzes the hydrolysis of endocannabinoid arachidonoylglycerol from the cell membrane. This leads to activation of the sperm calcium channel CatSper, which results in sperm activation. Alternative splicing of this gene results in two transcript variants encoding the same protein. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:18717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18717) · Entrez [11057](https://www.ncbi.nlm.nih.gov/gene/11057) · UniProt [P08910](https://www.uniprot.org/uniprotkb/P08910) · Ensembl [ENSG00000140526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140526)

## Data

Gene col 6425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6425); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6425]; `tensor/DDL_lfc|DDL_z.npy` [6425]; `embed/gene_vectors.npy` [6425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6425 or target_col == 6425). Every well: [[ABHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
