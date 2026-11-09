---
symbol: "AREL1"
type: "gene"
col: 4096
ensembl_id: "ENSG00000119682"
name: "apoptosis resistant E3 ubiquitin protein ligase 1"
location: "14q24.3"
module: 36
arm: "+"
pooled_cpm: 61.27
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# AREL1

*apoptosis resistant E3 ubiquitin protein ligase 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.40× (z +12.6, q 2e-33, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.414× (z -15.6, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (NCI-H1573 0.0719×, HEC-1-A 0.136×, SW1417 0.157×, NCI-H23 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0788×, NCI-H23 0.0972×, A549 0.199×, SNU-1 0.121×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.193×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC10]] (+0.77, fdr 7e-06), [[PIK3R4]] (+0.66, fdr 7e-06), [[CHUK]] (+0.65, fdr 7e-06); moves opposite to [[LGALS3]] (-0.54, fdr 3e-05), [[NOTCH2NLR]] (-0.52, fdr 2e-05), [[AHI1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.40×** | +12.6 | 2e-33 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +9.3 | 5e-18 | 44/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.65×** | +8.7 | 6e-16 | 41/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.18×** | +8.6 | 9e-16 | 41/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.2 | 4e-14 | 42/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 6e-12 | 37/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +6.7 | 2e-09 | 32/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +6.3 | 2e-08 | 27/48 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +6.1 | 6e-08 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +5.8 | 3e-07 | 40/48 (HOP62, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +5.7 | 5e-07 | 24/49 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.6 | 8e-07 | 30/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.6 | 9e-07 | 32/48 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 26/48 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.9 | 0.003 | 23/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.006 | 19/48 (BT-474, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.018 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.047 | 16/48 (SW480, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4096.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (NCI-H1573 0.0719×, HEC-1-A 0.136×, SW1417 0.157×, NCI-H23 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0788×, NCI-H23 0.0972×, A549 0.199×, SNU-1 0.121×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.193×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.414×** | -15.6 | 0e+00 | 43/49 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -15.3 | 0e+00 | 40/43 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -7.8 | 8e-13 | 34/45 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.1 | 0.007 | 20/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -3.2 | 0.14 | 20/48 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.834× | -3.1 | 0.16 | 17/48 (J82, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | 0.843× | -3.1 | 0.17 | 18/48 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.724× | -3.0 | 0.17 | 16/47 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.5 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -17.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 63.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -15.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 62.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.06× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 91.6 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0719× (z -28.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -16.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 57.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.11× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 93.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -13.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 85.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -16.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 74.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -19.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 56.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 52.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 52.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -24.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 62.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 82.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -15.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -25.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 62.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[C32 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0817× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 86.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 67.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -16.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC10]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[PIK3R4]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CHUK]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZNF410]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PGS1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NPLOC4]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NDOR1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.58 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[SENP5]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HIRA]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.57 | +0.38 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS3]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NOTCH2NLR]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[AHI1]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[IQCN]] | -0.48 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SPDYA]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[NOTCH2NLC]] | -0.46 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[ZBTB10]] | -0.46 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[AP1AR]] | -0.45 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[KPNA5]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CHMP2B]] | -0.45 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-11.1, -16.4); signed map (-44.7, -22.9). **Vector** length 81.9, 20.6% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.3 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +8.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | -1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis resistant E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,653,437-74,713,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FIEL1; previously KIAA0317 |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O15033](https://www.uniprot.org/uniprotkb/O15033) (Apoptosis-resistant E3 ubiquitin protein ligase 1):

> E3 ubiquitin-protein ligase that catalyzes 'Lys-11'- or 'Lys-33'-linked polyubiquitin chains, with some preference for 'Lys-33' linkages. E3 ubiquitin-protein ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Ubiquitinates SEPTIN4, DIABLO/SMAC and HTRA2 in vitro. Modulates pulmonary inflammation by targeting SOCS2 for ubiquitination and subsequent degradation by the proteasome.

**Summary**, from NCBI Gene [9870](https://www.ncbi.nlm.nih.gov/gene/9870):

> Enables ubiquitin protein ligase activity. Involved in negative regulation of apoptotic process; protein polyubiquitination; and ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20363) · Entrez [9870](https://www.ncbi.nlm.nih.gov/gene/9870) · UniProt [O15033](https://www.uniprot.org/uniprotkb/O15033) · Ensembl [ENSG00000119682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119682)

## Data

Gene col 4096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4096); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4096]; `tensor/DDL_lfc|DDL_z.npy` [4096]; `embed/gene_vectors.npy` [4096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4096 or target_col == 4096). Every well: [[AREL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AREL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
