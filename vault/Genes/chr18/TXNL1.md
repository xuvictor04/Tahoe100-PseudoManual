---
symbol: "TXNL1"
type: "gene"
col: 1658
ensembl_id: "ENSG00000091164"
name: "thioredoxin like 1"
location: "18q21.31"
module: 72
arm: "+"
pooled_cpm: 83.53
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TXNL1

*thioredoxin like 1* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.80× (z +19.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.647× (z -7.9, q 1e-12, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.806× (z -5.8, q 1e-06, down in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.371×, NCI-H2347 0.412×, CHP-212 0.186×, hTERT-HPNE 0.371×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.411×, NCI-H2347 0.443×, NCI-H2030 0.391×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.350×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0721×); [[Vilanterol (drug)]] 0.5 µM in 1 line (SW 1271 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC6]] (+0.81, fdr 7e-06), [[CDC40]] (+0.74, fdr 7e-06), [[COPS2]] (+0.74, fdr 7e-06); moves opposite to [[MYL12A]] (-0.52, fdr 3e-05), [[ENTR1]] (-0.51, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.80×** | +19.3 | 0e+00 | 48/48 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.71×** | +18.7 | 0e+00 | 48/48 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.70×** | +17.6 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +14.7 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.30×** | +14.4 | 1e-44 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +11.7 | 7e-30 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.99×** | +10.8 | 4e-25 | 44/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.97×** | +9.1 | 6e-18 | 45/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +9.0 | 2e-17 | 40/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +8.7 | 2e-16 | 31/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +8.4 | 2e-15 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +7.6 | 1e-12 | 42/45 (KATO III, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 1e-12 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +6.2 | 3e-08 | 33/48 (C32, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +6.0 | 1e-07 | 34/48 (A-427, NCI-H460, …) | rises with dose | composition shift |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.054 | 9/48 (NCI-H23, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.371×, NCI-H2347 0.412×, CHP-212 0.186×, hTERT-HPNE 0.371×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.411×, NCI-H2347 0.443×, NCI-H2030 0.391×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.350×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0721×); [[Vilanterol (drug)]] 0.5 µM in 1 line (SW 1271 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -7.9 | 1e-12 | 30/44 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -7.8 | 2e-12 | 34/49 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.8 | 1e-06 | 24/49 (H4, AN3 CA, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.791×** | -4.1 | 0.005 | 23/45 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.819×** | -3.8 | 0.016 | 21/48 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.875× | -3.6 | 0.027 | 9/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.831×** | -3.4 | 0.055 | 21/48 (H4, HS-578T, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -3.3 | 0.070 | 13/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.074 | 15/48 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.2 | 0.074 | 19/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.847× | -3.2 | 0.074 | 15/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.074 | 11/48 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.850× | -3.1 | 0.080 | 13/48 (SW48, A498, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.847× | -3.1 | 0.090 | 20/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.853× | -3.0 | 0.090 | 15/47 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.855× | -3.0 | 0.096 | 12/48 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.098 | 13/49 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.0 | 13 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.48× (z +21.5) | — |
| [[LoVo (line)]] | wt | 72.4 | 11 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.97× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 61.4 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +16.8) | — |
| [[SW480 (line)]] | alt | 48.0 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +16.3) | — |
| [[NCI-H1573 (line)]] | alt | 62.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 112 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 116 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +14.3) | — |
| [[SW48 (line)]] | wt | 108 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.0) | — |
| [[KATO III (line)]] | alt | 87.5 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 78.5 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.59× (z +10.4) | — |
| [[A-427 (line)]] | wt | 97.6 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +12.6) | — |
| [[C32 (line)]] | wt | 80.5 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.02× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 49.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 90.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 88.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.39× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 69.0 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 77.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.39× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 70.8 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 85.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.10× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.29× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 63.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.61× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 119 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.57× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 83.6 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 93.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +9.3) | — |
| [[A498 (line)]] | wt | 75.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +9.2) | — |
| [[A549 (line)]] | wt | 75.2 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.78× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 109 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.53× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 73.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.54× (z +11.8) | — |
| [[H4 (line)]] | wt | 117 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.4) |
| [[HCT15 (line)]] | alt | 82.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 42.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.28× (z +11.9) | — |
| [[J82 (line)]] | alt | 73.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 135 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.29× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 94.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.20× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 98.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 65.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 44.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 128 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 122 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 165 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +10.9) | — |
| [[A-172 (line)]] | wt | 56.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.25× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0721× (z -12.3) |
| [[SW 1271 (line)]] | alt | 75.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.108× (z -9.0) |
| [[SW 900 (line)]] | alt | 65.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC6]] | +0.81 | +0.86 / +0.73 | both halves | 7e-06 | STRING 528 |
| [[CDC40]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[COPS2]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 | pathway: RHOBTB GTPase Cycle |
| [[FXR1]] | +0.68 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.68 | +0.66 / +0.73 | both halves | 7e-06 | STRING 596 |
| [[PSMA3]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.66 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[PSMA6]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 | STRING 591 |
| [[RTCA]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PLAA]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PSMA2]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[HSP90AB2P]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL12A]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ENTR1]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.7, -7.0); signed map (-26.9, -20.5). **Vector** length 80.9, 24.7% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.55 to 12); *proteasome* (control, mean cos +0.55 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +18.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +17.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.4 | +19.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | -1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.7 | +14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | +11.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:56,597,209-56,651,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Txl, TRP32; previously TXNL |
| Reactome | 11 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O43396](https://www.uniprot.org/uniprotkb/O43396) (Thioredoxin-like protein 1):

> Active thioredoxin with a redox potential of about -250 mV.

**Summary**, from NCBI Gene [9352](https://www.ncbi.nlm.nih.gov/gene/9352):

> Enables disulfide oxidoreductase activity. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12436) · Entrez [9352](https://www.ncbi.nlm.nih.gov/gene/9352) · UniProt [O43396](https://www.uniprot.org/uniprotkb/O43396) · Ensembl [ENSG00000091164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091164)

## Data

Gene col 1658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1658); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1658]; `tensor/DDL_lfc|DDL_z.npy` [1658]; `embed/gene_vectors.npy` [1658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1658 or target_col == 1658). Every well: [[TXNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
