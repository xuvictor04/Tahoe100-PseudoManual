---
symbol: "HDAC2"
type: "gene"
col: 12245
ensembl_id: "ENSG00000196591"
name: "histone deacetylase 2"
location: "6q21"
module: 182
arm: "+"
pooled_cpm: 103.59
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 599
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# HDAC2

*histone deacetylase 2* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.18× (z +14.5, q 7e-45, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.29× (z +5.1, q 3e-05, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.12×, A-172 2.96×, SNU-423 3.51×, A498 2.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 3.03×, A498 3.03×, A-172 2.76×, NCI-H460 2.78×, …; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.203×, LS 180 0.514×, A-427 0.575×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.261×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.492×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1A]] (+0.67, fdr 7e-06), [[DHX15]] (+0.63, fdr 1e-05), [[MATR3]] (+0.59, fdr 1e-05); moves opposite to [[COPE]] (-0.60, fdr 1e-05), [[BLZF1]] (-0.58, fdr 1e-05), [[COQ10B]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.12×, A-172 2.96×, SNU-423 3.51×, A498 2.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 3.03×, A498 3.03×, A-172 2.76×, NCI-H460 2.78×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +14.5 | 7e-45 | 44/49 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +12.9 | 7e-36 | 35/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +8.9 | 2e-16 | 36/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.36×** | +6.1 | 1e-07 | 29/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.37×** | +6.1 | 2e-07 | 33/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.35×** | +6.0 | 2e-07 | 25/48 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.1 | 3e-05 | 27/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 2e-04 | 21/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.3 | 1e-03 | 25/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +3.9 | 0.005 | 21/50 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +3.8 | 0.009 | 22/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.017 | 16/38 (Panc 03.27, A-172, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +3.4 | 0.032 | 19/47 (C32, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.18× | +3.4 | 0.032 | 18/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.034 | 20/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.047 | 11/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.049 | 16/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.053 | 5/49 (A498, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.203×, LS 180 0.514×, A-427 0.575×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.261×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.492×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ranolazine (drug)]] 0.05 µM |  | 0.847× | -3.3 | 0.47 | 11/48 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.853× | -3.0 | 0.47 | 14/49 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.860× | -3.0 | 0.47 | 10/48 (Panc 03.27, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 57.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 83.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 128 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.4) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LoVo (line)]] | wt | 83.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 73.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +12.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +15.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 429 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 85.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 67.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 82.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 97.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 236 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 78.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 93.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.67× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[DHX15]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MATR3]] | +0.59 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 692 |
| [[NAE1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RBM17]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[MRPS35]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RYK]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MEST]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RAVER2]] | +0.56 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[ANP32A]] | +0.56 | +0.64 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPE]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[BLZF1]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[COQ10B]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TUT7]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[VRK3]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[DIABLO]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SEC16A]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SAP30BP]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression; STRING 520 |
| [[JMJD6]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 | pathway: Chromatin modifying enzymes |
| [[SYS1]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ARFIP2]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | [[HDAC1]], HDAC2, [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-28.0, -28.6); signed map (-20.5, -43.4). **Vector** length 98.4, 27.6% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:113,933,028-114,011,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPD3, YAF1, KDAC2 |
| Gene groups (HGNC) | Histone deacetylases, class I; EMSY complex; NuRD complex subunits; SIN3 histone deacetylase complex subunits; CoREST complex subunits; MiDAC complex subunits |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 72 pathways, smallest: p75NTR negatively regulates cell cycle via SC1; STAT3 nuclear events downstream of ALK signaling; MECP2 regulates neuronal receptors and channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92769](https://www.uniprot.org/uniprotkb/Q92769) (Histone deacetylase 2):

> Histone deacetylase that catalyzes the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events (By similarity). Histone deacetylases act via the formation of large multiprotein complexes (By similarity). Forms transcriptional repressor complexes by associating with MAD, SIN3, YY1 and …

**Summary**, from NCBI Gene [3066](https://www.ncbi.nlm.nih.gov/gene/3066):

> This gene product belongs to the histone deacetylase family. Histone deacetylases act via the formation of large multiprotein complexes, and are responsible for the deacetylation of lysine residues at the N-terminal regions of core histones (H2A, H2B, H3 and H4). This protein forms transcriptional repressor complexes by associating with many different proteins, including YY1, a mammalian zinc-finger transcription factor. Thus, it plays an important role in transcriptional regulation, cell cycle …

**Accessions** — [HGNC:4853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4853) · Entrez [3066](https://www.ncbi.nlm.nih.gov/gene/3066) · UniProt [Q92769](https://www.uniprot.org/uniprotkb/Q92769) · Ensembl [ENSG00000196591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196591)

## Data

Gene col 12245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12245); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12245]; `tensor/DDL_lfc|DDL_z.npy` [12245]; `embed/gene_vectors.npy` [12245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12245 or target_col == 12245). Every well: [[HDAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
