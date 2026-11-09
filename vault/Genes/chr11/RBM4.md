---
symbol: "RBM4"
type: "gene"
col: 10447
ensembl_id: "ENSG00000173933"
name: "RNA binding motif protein 4"
location: "11q13.2"
module: 96
arm: "+"
pooled_cpm: 76.54
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# RBM4

*RNA binding motif protein 4* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +21.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.707× (z -6.1, q 7e-07, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.355×, Panc 03.27 0.406×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Methylprednisolone succinate (drug)]] 5 µM in 1 line (CHP-212 0.0481×); [[Vismodegib (drug)]] 0.5 µM in 1 line (SW 1088 0.0691×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R1A]] (+0.66, fdr 1e-05), [[CPSF7]] (+0.65, fdr 1e-05), [[HNRNPL]] (+0.63, fdr 1e-05); moves opposite to [[SGTB]] (-0.59, fdr 1e-05), [[SERAC1]] (-0.57, fdr 1e-04), [[SPIRE1]] (-0.57, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +21.5 | 0e+00 | 46/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +15.2 | 0e+00 | 43/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +12.4 | 4e-33 | 46/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +12.4 | 5e-33 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.62×** | +12.2 | 3e-32 | 46/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +10.4 | 1e-23 | 47/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +9.8 | 9e-21 | 44/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.2 | 3e-18 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.60×** | +8.5 | 9e-16 | 43/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 3e-14 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.8 | 3e-13 | 2/50 (HOP62, SW 1088) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.9 | 3e-10 | 38/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 2e-09 | 30/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.37×** | +5.5 | 2e-06 | 31/47 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.2 | 6e-06 | 34/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 1e-03 | 25/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.007 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 1.13× | +3.1 | 0.050 | 8/48 (Hs 766T, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10447.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.355×, Panc 03.27 0.406×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Methylprednisolone succinate (drug)]] 5 µM in 1 line (CHP-212 0.0481×); [[Vismodegib (drug)]] 0.5 µM in 1 line (SW 1088 0.0691×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -6.1 | 7e-07 | 32/42 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.784×** | -4.4 | 0.002 | 26/49 (J82, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.833× | -3.2 | 0.29 | 18/47 (J82, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +20.1) | — |
| [[NCI-H1792 (line)]] | alt | 80.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +20.9) | — |
| [[SW480 (line)]] | alt | 94.7 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +14.6) | — |
| [[LoVo (line)]] | wt | 64.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +22.0) | — |
| [[NCI-H460 (line)]] | wt | 42.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 67.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +18.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 72.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 73.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.2) | — |
| [[A-172 (line)]] | wt | 53.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.3) | — |
| [[A498 (line)]] | wt | 43.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.6) | — |
| [[A549 (line)]] | wt | 65.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 82.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 63.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 84.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 58.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +20.5) | — |
| [[C32 (line)]] | wt | 55.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 66.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 75.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 87.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 64.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 60.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.9) | — |
| [[KATO III (line)]] | alt | 89.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 58.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H2347 (line)]] | alt | 60.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 80.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 74.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[SW48 (line)]] | wt | 78.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[A-427 (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 152 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 1 | — | [[Methylprednisolone succinate (drug)]] 5 µM 0.0481× (z -9.8) |
| [[HCT15 (line)]] | alt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.6) | — |
| [[J82 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 85.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 65.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.8) | — |
| [[SW 1088 (line)]] | alt | 64.5 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0691× (z -9.1) |
| [[SW1417 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R1A]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CPSF7]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 | same gene group |
| [[HNRNPL]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 | same gene group; STRING 640 |
| [[RAVER1]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 | same gene group |
| [[SRCAP]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SRSF6]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 | same gene group; STRING 463 |
| [[LINC00641]] | +0.57 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[SP2]] | +0.57 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[REXO1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[VPS52]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGTB]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.57 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[SPIRE1]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[STX7]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.53 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CAMLG]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RALBP1]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FNBP1L]] | -0.52 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[ANO10]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MPST]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[EPS15]] | -0.51 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[USP3]] | -0.50 | -0.54 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.2, -1.4); signed map (8.5, -34.9). **Vector** length 71.7, 17.5% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +4.6 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.7 | +3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +9.8 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,638,667-66,668,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LARK, RBM4A, ZCRB3A, ZCCHC21 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; RNA binding motif containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWF3](https://www.uniprot.org/uniprotkb/Q9BWF3) (RNA-binding protein 4):

> RNA-binding factor involved in multiple aspects of cellular processes like alternative splicing of pre-mRNA and translation regulation. Modulates alternative 5'-splice site and exon selection. Acts as a muscle cell differentiation-promoting factor. Activates exon skipping of the PTB pre-mRNA during muscle cell differentiation. Antagonizes the activity of the splicing factor PTBP1 to modulate muscle cell-specific exon selection of alpha tropomyosin. Binds to intronic pyrimidine-rich sequence of …

**Summary**, from NCBI Gene [5936](https://www.ncbi.nlm.nih.gov/gene/5936):

> Enables RNA binding activity and cyclin binding activity. Involved in several processes, including IRES-dependent translational initiation of linear mRNA; negative regulation of translation; and regulation of alternative mRNA splicing, via spliceosome. Located in cytoplasmic stress granule; nuclear speck; and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9901) · Entrez [5936](https://www.ncbi.nlm.nih.gov/gene/5936) · UniProt [Q9BWF3](https://www.uniprot.org/uniprotkb/Q9BWF3) · Ensembl [ENSG00000173933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173933)

## Data

Gene col 10447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10447); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10447]; `tensor/DDL_lfc|DDL_z.npy` [10447]; `embed/gene_vectors.npy` [10447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10447 or target_col == 10447). Every well: [[RBM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
