---
symbol: "ING3"
type: "gene"
col: 981
ensembl_id: "ENSG00000071243"
name: "inhibitor of growth family member 3"
location: "7q31.31"
module: 51
arm: "+"
pooled_cpm: 36.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ING3

*inhibitor of growth family member 3* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.48× (z +32.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.668× (z -6.2, q 3e-07, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.78, fdr 7e-06), [[BRAF]] (+0.67, fdr 7e-06), [[CUTALP]] (+0.65, fdr 7e-06); moves opposite to [[RNF4]] (-0.66, fdr 7e-06), [[BCAP31]] (-0.62, fdr 9e-06), [[MXRA7]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.48×** | +32.4 | 0e+00 | 48/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.47×** | +19.0 | 0e+00 | 47/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.79×** | +18.2 | 0e+00 | 48/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.0 | 4e-21 | 40/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.91×** | +9.9 | 7e-21 | 42/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.9 | 2e-13 | 37/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +6.2 | 4e-08 | 29/48 (NCI-H460, NCI-H1792, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +6.0 | 1e-07 | 32/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 7e-07 | 27/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 1e-06 | 30/48 (NCI-H2347, HS-578T, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +5.1 | 1e-05 | 30/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 6e-04 | 26/48 (A498, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +4.1 | 0.002 | 22/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 22/48 (NCI-H2347, A-427, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.012 | 22/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.012 | 17/48 (CFPAC-1, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.073 | 12/48 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.076 | 15/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.668×** | -6.2 | 3e-07 | 32/47 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.807×** | -4.7 | 9e-04 | 20/48 (C32, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.016 | 20/48 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.016 | 20/48 (KATO III, H4, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.798×** | -3.5 | 0.057 | 16/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.822× | -3.0 | 0.22 | 12/48 (SW1417, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.4 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +27.6) | — |
| [[LoVo (line)]] | wt | 41.5 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 76.7 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +23.4) | [[Belinostat (drug)]] 0.5 µM 0.354× (z -9.1) |
| [[SW48 (line)]] | wt | 47.8 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 31.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +17.6) | — |
| [[A-172 (line)]] | wt | 22.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +21.0) | — |
| [[A498 (line)]] | wt | 51.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +29.5) | — |
| [[HEC-1-A (line)]] | alt | 33.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +23.3) | — |
| [[KATO III (line)]] | alt | 41.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +19.7) | — |
| [[RKO (line)]] | wt | 51.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 30.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.1) | — |
| [[A549 (line)]] | wt | 21.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +18.6) | — |
| [[CFPAC-1 (line)]] | alt | 30.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +20.2) | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 3 (2 ⚠) | — | [[Acetohexamide (drug)]] 0.5 µM 0.0384× (z -16.3) |
| [[HOP62 (line)]] | alt | 22.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +18.0) | — |
| [[HS-578T (line)]] | alt | 23.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +20.4) | — |
| [[PANC-1 (line)]] | alt | 31.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +22.2) | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +15.4) | — |
| [[SW480 (line)]] | alt | 40.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +18.4) | — |
| [[C-33 A (line)]] | alt | 45.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 45.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +16.3) | — |
| [[SNU-1 (line)]] | wt | 80.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 41.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +20.4) | — |
| [[SW1417 (line)]] | alt | 53.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +12.7) | — |
| [[H4 (line)]] | wt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 43.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.0) | — |
| [[J82 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +15.6) | — |
| [[SW 900 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 996 |
| [[BRAF]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CUTALP]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LARP7]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[KMT5B]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[KAT5]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 999 |
| [[INO80]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 | STRING 916 |
| [[DECR2]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BPTF]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 | same gene group; STRING 750 |
| [[RBM5]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PHACTR4]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.62 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[MXRA7]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.60 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[SDHAP4]] | -0.59 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[PIGF]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[P3H1]] | -0.58 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MFN1]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SETD3]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[TMEM181]] | -0.57 | -0.40 / -0.62 | both halves | 4e-05 |  |
| [[SNHG30]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ING3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ING3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[P3H1]] | C | P3H1 activity raises ING3's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without P3H1 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.4, 13.1); signed map (7.7, -17.8). **Vector** length 99.1, 26.0% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +32.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +19.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +18.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.2 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -6.5 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of growth family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:120,950,763-120,977,216 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p47ING3, FLJ20089, Eaf4, MEAF4 |
| Gene groups (HGNC) | PHD finger proteins; Tip60/Nua4 histone acetyltransferase complex subunits; Inhibitor of growth family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXR8](https://www.uniprot.org/uniprotkb/Q9NXR8) (Inhibitor of growth protein 3):

> Component of the NuA4 histone acetyltransferase (HAT) complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome - DNA interactions and promote interaction of the modified histones with other proteins which positively regulate transcription. This complex may be required for the activation of transcriptional programs associated with oncogene and proto-oncogene mediated growth …

**Summary**, from NCBI Gene [54556](https://www.ncbi.nlm.nih.gov/gene/54556):

> The protein encoded by this gene is similar to ING1, a tumor suppressor protein that can interact with TP53, inhibit cell growth, and induce apoptosis. This protein contains a PHD-finger, which is a common motif in proteins involved in chromatin remodeling. This gene can activate p53 trans-activated promoters, including promoters of p21/waf1 and bax. Overexpression of this gene has been shown to inhibit cell growth and induce apoptosis. Allelic loss and reduced expression of this gene were …

**Accessions** — [HGNC:14587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14587) · Entrez [54556](https://www.ncbi.nlm.nih.gov/gene/54556) · UniProt [Q9NXR8](https://www.uniprot.org/uniprotkb/Q9NXR8) · Ensembl [ENSG00000071243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071243)

## Data

Gene col 981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 981); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 981]; `tensor/DDL_lfc|DDL_z.npy` [981]; `embed/gene_vectors.npy` [981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 981 or target_col == 981). Every well: [[ING3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
