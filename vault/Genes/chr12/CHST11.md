---
symbol: "CHST11"
type: "gene"
col: 10089
ensembl_id: "ENSG00000171310"
name: "carbohydrate sulfotransferase 11"
location: "12q23.3"
module: 9
arm: "+"
pooled_cpm: 124.33
n_lines_expressing: 37
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CHST11

*carbohydrate sulfotransferase 11* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +22.9, q 0e+00, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.545× (z -10.7, q 6e-24, down in 25 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.733× (z -5.7, q 1e-06, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRM3]] (+0.56, fdr 2e-05), [[MMP16]] (+0.56, fdr 1e-05), [[RASGRF1]] (+0.55, fdr 2e-05); moves opposite to [[FAM149B1]] (-0.58, fdr 2e-05), [[SMAD4]] (-0.49, fdr 2e-05), [[OSTC]] (-0.47, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CA8]] → it (grade B ⚠); 4 go from it, the strongest it → [[DMRTA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +22.9 | 0e+00 | 23/35 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +16.1 | 0e+00 | 27/35 (HOP62, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +11.2 | 7e-27 | 23/35 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +10.8 | 5e-25 | 25/35 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +10.4 | 4e-23 | 28/35 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.71×** | +10.0 | 2e-21 | 22/35 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.65×** | +9.3 | 1e-18 | 22/35 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.5 | 2e-15 | 24/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.4 | 2e-15 | 21/35 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 7e-11 | 23/36 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +6.6 | 2e-09 | 18/36 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 2e-09 | 22/35 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +6.2 | 2e-08 | 13/36 (HOP62, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +5.9 | 2e-07 | 17/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 3e-06 | 14/35 (HOP62, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.026 | 12/35 (NCI-H23, COLO 205, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.046 | 10/35 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.076 | 9/35 (AsPC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.077 | 17/34 (SW 900, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.083 | 6/35 (AsPC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -10.7 | 6e-24 | 25/36 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -9.5 | 4e-19 | 22/34 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.623×** | -8.1 | 1e-13 | 25/32 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -7.5 | 7e-12 | 24/32 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -5.7 | 1e-06 | 20/35 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -5.4 | 5e-06 | 18/30 (SK-MEL-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -5.4 | 5e-06 | 18/36 (SK-MEL-2, C32, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.601×** | -4.9 | 6e-05 | 26/35 (J82, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.794×** | -4.2 | 0.001 | 18/35 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.808×** | -3.9 | 0.005 | 17/35 (SW 1088, Panc 03.27, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.010 | 16/35 (C32, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.869× | -3.7 | 0.011 | 11/35 (NCI-H1573, J82, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.774×** | -3.4 | 0.033 | 14/35 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.885× | -3.2 | 0.062 | 8/36 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.839× | -3.1 | 0.070 | 13/34 (SHP-77, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.086 | 16/34 (C32, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 758 | 0 | 21 (12 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -13.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.313× (z -11.5) |
| [[COLO 205 (line)]] | alt | 935 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -22.4) |
| [[HOP62 (line)]] | alt | 75.5 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +24.7) | — |
| [[NCI-H460 (line)]] | wt | 45.7 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.19× (z +21.0) | — |
| [[NCI-H23 (line)]] | alt | 67.8 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 288 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -17.1) ⚠ toxic · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.514× (z -9.7) |
| [[C32 (line)]] | wt | 337 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.474× (z -9.8) |
| [[HS-578T (line)]] | alt | 61.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 63.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +22.5) | — |
| [[A-172 (line)]] | wt | 48.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.03× (z +14.1) | — |
| [[A498 (line)]] | wt | 324 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 36.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 88.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +31.7) | — |
| [[AN3 CA (line)]] | alt | 82.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 363 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.95× (z +10.7) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -14.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 73.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 79.4 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.69× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.465× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 41.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.2) | — |
| [[J82 (line)]] | alt | 77.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 89.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 151 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.2) | — |
| [[SW 900 (line)]] | alt | 144 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.20× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 84.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.70× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -9.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.97× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 29.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 28.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRM3]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[MMP16]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ERC2]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 | same gene group |
| [[SLCO3A1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[EGFEM1P]] | +0.52 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SOX5]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 | STRING 512 |
| [[OSBPL3]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CA8]] | +0.49 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[ENTREP2]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[LRMDA]] | +0.49 | +0.33 / +0.57 | both halves | 1e-04 | same gene group |
| [[FGF13]] | +0.49 | +0.51 / +0.50 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM149B1]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SMAD4]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[OSTC]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CDADC1]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ALDH6A1]] | -0.47 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PPOX]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FPGT]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[MMUT]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF559-ZNF177]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SLC28A2-AS1]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[KLHDC2]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[RUSF1]] | -0.45 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA8]] | B | CA8 activity raises CHST11's level | lines that do not express CA8 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without CA8 | 0.010 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[DMRTA1]] | B | DMRTA1 activity raises CHST11's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 3.44× lower at baseline in the lines without DMRTA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[TNC]] | B | TNC activity raises CHST11's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.97× lower at baseline in the lines without TNC | 0.034 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[FGF19]] | B | FGF19 activity raises CHST11's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.44× lower at baseline in the lines without FGF19 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[ARNT2]] | B | ARNT2 activity raises CHST11's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without ARNT2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMRTA1]] | B | CHST11 activity raises DMRTA1's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without CHST11 | 0.043 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[CCDC144CP]] | B | CHST11 activity raises CCDC144CP's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without CHST11 | 0.063 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[CA8]] | B | CHST11 activity raises CA8's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without CHST11 | 0.070 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[CLCC1]] | B | CHST11 activity lowers CLCC1's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 1.15× higher at baseline in the lines without CHST11 | 0.084 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.9, 31.7); signed map (36.6, 32.1). **Vector** length 116, 31.1% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +22.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -9.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -5.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,455,295-104,762,014 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C4ST1, C4St-1, C4ST, HSA269537 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPF2](https://www.uniprot.org/uniprotkb/Q9NPF2) (Carbohydrate sulfotransferase 11):

> Catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of chondroitin. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage and is distributed on the surfaces of many cells and extracellular matrices. Can also sulfate Gal residues in desulfated dermatan sulfate. Preferentially sulfates in GlcA->GalNAc unit than in IdoA->GalNAc unit. Does not form 4, 6-di-O-sulfated GalNAc when chondroitin sulfate C is used as an acceptor.

**Summary**, from NCBI Gene [50515](https://www.ncbi.nlm.nih.gov/gene/50515):

> The protein encoded by this gene belongs to the sulfotransferase 2 family. It is localized to the golgi membrane, and catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of chondroitin. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage, and is distributed on the surfaces of many cells and extracellular matrices. A chromosomal translocation involving this gene and IgH, t(12;14)(q23;q32), has been reported in a patient with …

**Accessions** — [HGNC:17422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17422) · Entrez [50515](https://www.ncbi.nlm.nih.gov/gene/50515) · UniProt [Q9NPF2](https://www.uniprot.org/uniprotkb/Q9NPF2) · Ensembl [ENSG00000171310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171310)

## Data

Gene col 10089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10089); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10089]; `tensor/DDL_lfc|DDL_z.npy` [10089]; `embed/gene_vectors.npy` [10089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10089 or target_col == 10089). Every well: [[CHST11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
