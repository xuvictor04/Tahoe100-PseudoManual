---
symbol: "SLFN11"
type: "gene"
col: 10283
ensembl_id: "ENSG00000172716"
name: "schlafen family member 11"
location: "17q12"
module: 152
arm: "+"
pooled_cpm: 24.97
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# SLFN11

*schlafen family member 11* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.10× (z +14.7, q 0e+00, up in 20 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.610× (z -6.9, q 4e-09, down in 20 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.636× (z -6.3, q 8e-08, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDNF]] (+0.61, fdr 1e-05), [[ST8SIA4]] (+0.58, fdr 1e-05), [[OR4F15]] (+0.58, fdr 2e-05); moves opposite to [[ITGA9-AS1]] (-0.51, fdr 1e-04), [[KPNA6]] (-0.51, fdr 1e-04), [[CYBRD1]] (-0.51, fdr 7e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BHLHE41]] → it (grade C ⚠); 3 go from it, the strongest it → [[PPP1R3C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +14.7 | 0e+00 | 20/20 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +12.5 | 1e-33 | 0/20 | two highest doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +11.9 | 2e-30 | 20/20 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +9.7 | 3e-20 | 18/20 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.91×** | +9.0 | 2e-17 | 18/20 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.9 | 2e-13 | 11/20 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.4 | 9e-12 | 3/19 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.70×** | +7.4 | 1e-11 | 16/20 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.44×** | +4.9 | 5e-05 | 0/17 | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 5e-04 | 10/20 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 3/20 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +4.1 | 0.002 | 15/20 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.003 | 4/20 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 11/20 (CFPAC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.008 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -6.9 | 4e-09 | 20/20 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -6.3 | 8e-08 | 18/20 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -4.8 | 2e-04 | 18/20 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.7 | 3e-04 | 15/20 (PANC-1, C32, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 5e-04 | 17/20 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -4.5 | 8e-04 | 19/20 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -4.1 | 0.003 | 19/19 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.745×** | -4.1 | 0.003 | 13/20 (C32, A-172, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.008 | 18/20 (C32, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.026 | 3/20 (CFPAC-1, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -3.3 | 0.055 | 12/20 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.792×** | -3.2 | 0.059 | 8/20 (CFPAC-1, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -3.2 | 0.071 | 7/20 (C32, HOP62, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.802×** | -3.1 | 0.088 | 8/19 (Panc 03.27, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.789×** | -3.0 | 0.090 | 1/20 (C32) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.9 | 7 (3 ⚠) | 7 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.70× (z +14.9) | [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 49.1 | 3 (1 ⚠) | 10 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.82× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 65.8 | 3 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.8) |
| [[H4 (line)]] | wt | 73.0 | 1 | 8 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.63× (z +8.7) | [[Digitoxin (drug)]] 0.5 µM 0.152× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 88.5 | 4 (2 ⚠) | 5 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.92× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0904× (z -19.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 84.2 | 3 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -9.3) |
| [[C32 (line)]] | wt | 60.2 | 1 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.85× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.247× (z -12.7) |
| [[A-172 (line)]] | wt | 75.2 | 4 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.18× (z +17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.76× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 25.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.13× (z +14.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 82.0 | 2 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.49× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.13× (z +14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.97× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.233× (z -9.8) |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -12.3) |
| [[SW 900 (line)]] | alt | 54.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.63× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.03× (z +13.6) | — |
| [[SW 1271 (line)]] | alt | 88.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0778× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.5) |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDNF]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[OR4F15]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP28]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ZNF184]] | +0.56 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[EPHA3]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MRPL17]] | +0.55 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[DPY19L2P1]] | +0.55 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[SYT11]] | +0.54 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[NOL4]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TNFRSF1B]] | +0.54 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[TRIM9]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA9-AS1]] | -0.51 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[KPNA6]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[CYBRD1]] | -0.51 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[FAM185A]] | -0.50 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[DHX35]] | -0.50 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[VSIG10]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[AMFR]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CERS2]] | -0.49 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[ANXA2R-OT1]] | -0.49 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[NAGPA]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[LINC03006-1]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[POU6F1]] | -0.48 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | C | BHLHE41 activity raises SLFN11's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 4.34× lower at baseline in the lines without BHLHE41 | 0.011 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises SLFN11's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 4.64× lower at baseline in the lines without LINC01583 | 0.029 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises SLFN11's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 5.27× lower at baseline in the lines without SLC8A1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[KCTD16]] | C | KCTD16 activity raises SLFN11's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 4.80× lower at baseline in the lines without KCTD16 | 0.043 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[PPP1R3C]] | C | PPP1R3C activity raises SLFN11's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 4.39× lower at baseline in the lines without PPP1R3C | 0.050 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1; co-absent with the target |
| [[SNAP25]] | C | SNAP25 activity raises SLFN11's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.51× lower at baseline in the lines without SNAP25 | 0.074 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises SLFN11's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without ZMAT4 | 0.087 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R3C]] | C | SLFN11 activity raises PPP1R3C's level | lines that do not express SLFN11 (28) vs lines expressing it (22) | 4.40× lower at baseline in the lines without SLFN11 | 0.023 | ⚠ within organs, on part of the lines; also absent: IGF2BP1, INSYN2B, DPY19L2; co-absent with the target |
| [[SLC8A1]] | C | SLFN11 activity raises SLC8A1's level | lines that do not express SLFN11 (28) vs lines expressing it (22) | 3.89× lower at baseline in the lines without SLFN11 | 0.035 | ⚠ within organs, on part of the lines; also absent: IGF2BP1, INSYN2B, DPY19L2; co-absent with the target |
| [[GFPT2]] | C | SLFN11 activity raises GFPT2's level | lines that do not express SLFN11 (28) vs lines expressing it (22) | 3.54× lower at baseline in the lines without SLFN11 | 0.069 | ⚠ within organs, on part of the lines; also absent: IGF2BP1, INSYN2B, DPY19L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.9, 30.5); signed map (32.0, 31.6). **Vector** length 83.8, 25.8% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | schlafen family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,350,305-35,373,701 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34922 |
| Gene groups (HGNC) | Schlafen family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7L1](https://www.uniprot.org/uniprotkb/Q7Z7L1) (Schlafen family member 11):

> Inhibitor of DNA replication that promotes cell death in response to DNA damage. Acts as a guardian of the genome by killing cells with defective replication. Persistently blocks stressed replication forks by opening chromatin across replication initiation sites at stressed replication forks, possibly leading to unwind DNA ahead of the MCM helicase and block fork progression, ultimately leading to cell death. Upon DNA damage, inhibits translation of ATR or ATM based on distinct codon usage …

**Summary**, from NCBI Gene [91607](https://www.ncbi.nlm.nih.gov/gene/91607):

> Enables ATP hydrolysis activity and tRNA binding activity. Involved in several processes, including defense response to virus; negative regulation of G1/S transition of mitotic cell cycle; and replication fork arrest. Located in nucleoplasm and site of DNA damage. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26633) · Entrez [91607](https://www.ncbi.nlm.nih.gov/gene/91607) · UniProt [Q7Z7L1](https://www.uniprot.org/uniprotkb/Q7Z7L1) · Ensembl [ENSG00000172716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172716)

## Data

Gene col 10283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10283); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10283]; `tensor/DDL_lfc|DDL_z.npy` [10283]; `embed/gene_vectors.npy` [10283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10283 or target_col == 10283). Every well: [[SLFN11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLFN11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
