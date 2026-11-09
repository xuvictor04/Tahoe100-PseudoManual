---
symbol: "HBS1L"
type: "gene"
col: 3360
ensembl_id: "ENSG00000112339"
name: "HBS1 like translational GTPase"
location: "6q23.3"
module: 57
arm: "+"
pooled_cpm: 124.88
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 7
n_dd_up_clean: 22
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# HBS1L

*HBS1 like translational GTPase* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.10× (z +17.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 0.05 µM: 0.786× (z -4.6, q 0.003, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP30]] (+0.70, fdr 7e-06), [[ATP5F1C]] (+0.67, fdr 7e-06), [[MRS2]] (+0.67, fdr 7e-06); moves opposite to [[KDSR]] (-0.65, fdr 7e-06), [[TLNRD1]] (-0.59, fdr 1e-05), [[CRK]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.10×** | +17.8 | 0e+00 | 49/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +16.1 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.13×** | +13.9 | 7e-42 | 48/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +13.7 | 1e-40 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +12.7 | 1e-34 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +10.7 | 2e-24 | 46/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +10.5 | 7e-24 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +10.3 | 7e-23 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +9.3 | 6e-19 | 40/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.3 | 6e-19 | 45/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +8.8 | 8e-17 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.5 | 6e-16 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.1 | 2e-14 | 44/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +8.0 | 4e-14 | 42/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +8.0 | 4e-14 | 40/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +7.0 | 1e-10 | 40/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.6 | 2e-09 | 29/48 (HT-29, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 0.05 µM |  | **0.786×** | -4.6 | 0.003 | 27/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -4.1 | 0.013 | 26/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.812×** | -3.9 | 0.015 | 28/47 (AsPC-1, HOP62, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.038 | 24/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.830×** | -3.5 | 0.038 | 24/49 (COLO 205, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.038 | 23/48 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.038 | 21/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.046 | 20/48 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.839× | -3.3 | 0.046 | 20/48 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.046 | 15/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.046 | 17/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.836× | -3.3 | 0.046 | 21/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.046 | 17/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.047 | 18/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.067 | 17/48 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.855× | -3.0 | 0.094 | 14/48 (NCI-H2030, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 163 | 15 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +20.1) | — |
| [[PANC-1 (line)]] | alt | 144 | 13 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +20.7) | — |
| [[NCI-H460 (line)]] | wt | 97.6 | 12 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +19.0) | — |
| [[COLO 205 (line)]] | alt | 394 | 9 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.9× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 98.4 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +19.2) | — |
| [[BT-474 (line)]] | alt | 110 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 80.5 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 150 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +14.4) | — |
| [[KATO III (line)]] | alt | 107 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +17.8) | — |
| [[C-33 A (line)]] | alt | 144 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.4) | — |
| [[A-427 (line)]] | wt | 121 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.18× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 97.8 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.18× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 108 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 7.95× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 120 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +12.7) | — |
| [[RKO (line)]] | wt | 157 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 5.77× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 134 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.66× (z +9.8) | — |
| [[SW48 (line)]] | wt | 144 | 5 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.57× (z +12.3) | — |
| [[J82 (line)]] | alt | 129 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 187 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.24× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 118 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 129 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.89× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 85.8 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.91× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 160 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.48× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 187 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.10× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 81.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.64× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 175 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 132 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 135 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.14× (z +10.1) | — |
| [[A498 (line)]] | wt | 96.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.5) | — |
| [[A549 (line)]] | wt | 80.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.6) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.74× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +10.5) | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 2 | — | [[Simotinib (drug)]] 0.05 µM 0.0867× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 94.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.53× (z +9.2) | — |
| [[C32 (line)]] | wt | 115 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.75× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 82.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.57× (z +9.8) | — |
| [[H4 (line)]] | wt | 78.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 96.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.62× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 142 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 154 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.55× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP30]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MRS2]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FXR1]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RTCA]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 | same gene group |
| [[TFG]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[STAM]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[LONP2]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CYB5R4]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDSR]] | -0.65 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[TLNRD1]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[CRK]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RIPK1]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ERF]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[IGF2BP3]] | -0.52 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[RESF1]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[KDM6B]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PKNOX1]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.2, -11.3); signed map (-33.0, -15.0). **Vector** length 67.4, 21.4% of its response variance represented; |z| ≥ 3 in 1,406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | +8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | +16.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | +1.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | +1.6 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | HBS1 like translational GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:134,960,378-135,103,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERFS, HBS1, HSPC276, KIAA1038, DKFZp434g247, EF-1a, eRF3c |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Translational GTPases |
| Reactome | 6 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Deadenylation-dependent mRNA decay; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y450](https://www.uniprot.org/uniprotkb/Q9Y450) (HBS1-like protein):

> GTPase component of the Pelota-HBS1L complex, a complex that recognizes stalled ribosomes and triggers the No-Go Decay (NGD) pathway. The Pelota-HBS1L complex recognizes ribosomes stalled at the 3' end of an mRNA and engages stalled ribosomes by destabilizing mRNA in the mRNA channel. Following mRNA extraction from stalled ribosomes by the SKI complex, the Pelota-HBS1L complex promotes recruitment of ABCE1, which drives the disassembly of stalled ribosomes, followed by degradation of damaged …

**Summary**, from NCBI Gene [10767](https://www.ncbi.nlm.nih.gov/gene/10767):

> This gene encodes a member of the GTP-binding elongation factor family. It is expressed in multiple tissues with the highest expression in heart and skeletal muscle. The intergenic region of this gene and the MYB gene has been identified to be a quantitative trait locus (QTL) controlling fetal hemoglobin level, and this region influnces erythrocyte, platelet, and monocyte counts as well as erythrocyte volume and hemoglobin content. DNA polymorphisms at this region associate with fetal …

**Accessions** — [HGNC:4834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4834) · Entrez [10767](https://www.ncbi.nlm.nih.gov/gene/10767) · UniProt [Q9Y450](https://www.uniprot.org/uniprotkb/Q9Y450) · Ensembl [ENSG00000112339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112339)

## Data

Gene col 3360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3360); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3360]; `tensor/DDL_lfc|DDL_z.npy` [3360]; `embed/gene_vectors.npy` [3360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3360 or target_col == 3360). Every well: [[HBS1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HBS1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
