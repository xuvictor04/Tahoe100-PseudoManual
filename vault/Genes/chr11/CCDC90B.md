---
symbol: "CCDC90B"
type: "gene"
col: 6025
ensembl_id: "ENSG00000137500"
name: "coiled-coil domain containing 90B"
location: "11q14.1"
module: 28
arm: "+"
pooled_cpm: 34.87
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CCDC90B

*coiled-coil domain containing 90B* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +11.2, q 1e-26, up in 33 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +6.2, q 1e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.428× (z -12.0, q 1e-30, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPC]] (+0.74, fdr 7e-06), [[LACC1]] (+0.71, fdr 7e-06), [[TAB3]] (+0.69, fdr 7e-06); moves opposite to [[CASP2]] (-0.60, fdr 2e-05), [[TUFM]] (-0.60, fdr 8e-05), [[SHMT1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +11.2 | 1e-26 | 33/38 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.2 | 1e-26 | 40/44 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.2 | 1e-07 | 35/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.0 | 3e-07 | 31/48 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 4e-07 | 32/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.8 | 5e-07 | 25/48 (A-427, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 1e-06 | 35/48 (A-172, LS 180, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.9 | 5e-05 | 26/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 6e-04 | 23/47 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.3 | 8e-04 | 22/47 (PANC-1, NCI-H1792, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +4.1 | 0.002 | 23/39 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.21×** | +3.7 | 0.009 | 19/47 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.011 | 18/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.020 | 19/47 (LoVo, A-172, …) | all doses, flat | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.041 | 16/48 (NCI-H1792, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.052 | 16/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.089 | 18/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.48×** | +2.9 | 0.097 | 10/48 (A-427, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -12.0 | 1e-30 | 45/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -12.0 | 1e-30 | 45/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -9.3 | 4e-18 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -9.2 | 5e-18 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -5.6 | 2e-06 | 29/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -5.5 | 4e-06 | 28/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.683×** | -5.4 | 5e-06 | 30/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -4.8 | 1e-04 | 29/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -4.0 | 0.004 | 26/48 (A549, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.006 | 23/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.607×** | -3.7 | 0.011 | 18/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.770×** | -3.5 | 0.021 | 20/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.782×** | -3.5 | 0.021 | 20/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | 0.855× | -3.1 | 0.085 | 8/48 (RPMI-7951, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 58.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -19.6) |
| [[SW480 (line)]] | alt | 39.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -11.2) |
| [[A498 (line)]] | wt | 30.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 35.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.5) |
| [[KATO III (line)]] | alt | 48.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.264× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 39.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.6) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 0.05 µM 0.238× (z -11.0) |
| [[LS 180 (line)]] | wt | 29.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.220× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 30.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -8.5) |
| [[LoVo (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.319× (z -10.0) |
| [[A-427 (line)]] | wt | 73.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.273× (z -13.2) |
| [[A549 (line)]] | wt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0732× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.6) |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPC]] | +0.74 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[LACC1]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TAB3]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SNRNP27]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[TAF9]] | +0.67 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[SMIM19]] | +0.65 | +0.74 / +0.46 | both halves | 3e-05 |  |
| [[STAMBP]] | +0.64 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[COQ5]] | +0.64 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[APLF]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[RRM2B]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.64 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[BCDIN3D]] | +0.63 | +0.68 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP2]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[TUFM]] | -0.60 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[SHMT1]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[BRI3BP]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.55 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[FAM118A]] | -0.55 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[FANCA]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PARP1]] | -0.55 | -0.36 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC90B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.5, 20.4); signed map (19.3, -16.8). **Vector** length 100, 27.6% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.9 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -12.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -12.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 90B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:83,259,081-83,286,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDS025, MDS011 |
| Matched by | ensembl_id |

UniProt [Q9GZT6](https://www.uniprot.org/uniprotkb/Q9GZT6) carries no function annotation.

**Summary**, from NCBI Gene [60492](https://www.ncbi.nlm.nih.gov/gene/60492):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28108) · Entrez [60492](https://www.ncbi.nlm.nih.gov/gene/60492) · UniProt [Q9GZT6](https://www.uniprot.org/uniprotkb/Q9GZT6) · Ensembl [ENSG00000137500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137500)

## Data

Gene col 6025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6025); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6025]; `tensor/DDL_lfc|DDL_z.npy` [6025]; `embed/gene_vectors.npy` [6025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6025 or target_col == 6025). Every well: [[CCDC90B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC90B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
