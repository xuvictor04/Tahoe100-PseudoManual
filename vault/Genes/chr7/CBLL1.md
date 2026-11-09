---
symbol: "CBLL1"
type: "gene"
col: 2683
ensembl_id: "ENSG00000105879"
name: "Cbl proto-oncogene like 1"
location: "7q22.3"
module: 7
arm: "+"
pooled_cpm: 40.91
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CBLL1

*Cbl proto-oncogene like 1* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.53× (z +42.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.566× (z -13.6, q 4e-39, down in 39 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (AsPC-1 0.0713×, A-172 0.0791×, HEC-1-A 0.112×, NCI-H1573 0.187×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.156×, NCI-H1792 0.200×, NCI-H460 0.340×, SNU-423 0.269×, …; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.228×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB6]] (+0.89, fdr 7e-06), [[GTF3C4]] (+0.83, fdr 7e-06), [[SMG8]] (+0.78, fdr 7e-06); moves opposite to [[PTMAP5]] (-0.64, fdr 4e-05), [[CBFA2T2]] (-0.64, fdr 9e-06), [[PTMA]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.53×** | +42.4 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.70×** | +29.9 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.51×** | +28.5 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **9.05×** | +27.4 | 0e+00 | 48/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.56×** | +22.4 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.57×** | +21.4 | 0e+00 | 45/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +13.5 | 2e-39 | 42/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +12.6 | 2e-34 | 42/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +11.8 | 4e-30 | 42/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +10.9 | 6e-26 | 40/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +10.9 | 6e-26 | 42/48 (SW480, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +8.0 | 8e-14 | 29/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +7.3 | 1e-11 | 30/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +7.1 | 4e-11 | 26/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +7.0 | 8e-11 | 26/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +6.1 | 3e-08 | 22/48 (J82, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.0 | 8e-08 | 24/48 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (AsPC-1 0.0713×, A-172 0.0791×, HEC-1-A 0.112×, NCI-H1573 0.187×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.156×, NCI-H1792 0.200×, NCI-H460 0.340×, SNU-423 0.269×, …; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.228×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.566×** | -13.6 | 4e-39 | 39/47 (RKO, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -12.1 | 3e-31 | 33/40 (AsPC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.841× | -4.1 | 0.006 | 13/48 (SHP-77, SW48, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | 0.848× | -3.8 | 0.020 | 13/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.895× | -3.8 | 0.020 | 5/48 (CHP-212, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.910× | -3.2 | 0.12 | 8/48 (A498, NCI-H1792, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.830× | -3.2 | 0.12 | 7/48 (NCI-H23, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.18 | 7/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.2 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +23.1) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.1 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.0791× (z -24.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.4 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -12.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.0 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -20.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 74.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.7× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -19.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.2 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.3 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 46.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +31.6) | — |
| [[SW480 (line)]] | alt | 47.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +20.6) | — |
| [[AsPC-1 (line)]] | alt | 45.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -26.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 81.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +20.2) | — |
| [[HS-578T (line)]] | alt | 37.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.4) | — |
| [[J82 (line)]] | alt | 36.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 52.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +18.7) | — |
| [[Hs 766T (line)]] | wt | 44.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 38.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 44.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.2) | — |
| [[LOX-IMVI (line)]] | wt | 31.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.3) | — |
| [[SNU-423 (line)]] | alt | 34.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 36.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.9) | — |
| [[SW48 (line)]] | wt | 53.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 35.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 50.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +17.7) | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 62.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.6) | — |
| [[A-427 (line)]] | wt | 39.3 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.10× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 28.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +16.1) | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.8) | [[Acetazolamide (drug)]] 0.5 µM 0.228× (z -9.2) |
| [[C-33 A (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB6]] | +0.89 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.83 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[SMG8]] | +0.78 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.78 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[ZNF845]] | +0.76 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.76 | +0.80 / +0.63 | both halves | 7e-06 | pathway: Activation of STAT3 by cadherin engagement |
| [[TACO1]] | +0.75 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[THUMPD3]] | +0.75 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.75 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.73 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.73 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMAP5]] | -0.64 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[CBFA2T2]] | -0.64 | -0.66 / -0.57 | both halves | 9e-06 |  |
| [[PTMA]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.884). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.7, 10.1); signed map (-1.2, -26.1). **Vector** length 89.7, 22.4% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.8 | +22.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +27.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +28.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +21.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +10.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +10.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.0 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -13.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.8 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.7 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Cbl proto-oncogene like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,743,073-107,761,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAKAI, FLJ23109, RNF188 |
| Gene groups (HGNC) | Ring finger proteins; m6A methyltransferase complex; WTAP complex; Cbl proto-oncogene like family |
| Reactome | 14 pathways, smallest: InlA-mediated entry of Listeria monocytogenes into host cells; Listeria monocytogenes entry into host cells; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q75N03](https://www.uniprot.org/uniprotkb/Q75N03) (E3 ubiquitin-protein ligase Hakai):

> E3 ubiquitin-protein ligase that mediates ubiquitination of several tyrosine-phosphorylated Src substrates, including CDH1, CTTN and DOK1 (By similarity). Targets CDH1 for endocytosis and degradation (By similarity). Associated component of the WMM complex, a complex that mediates N6-methyladenosine (m6A) methylation of RNAs, a modification that plays a role in the efficiency of mRNA splicing and RNA processing. Its function in the WMM complex is unknown.

**Summary**, from NCBI Gene [79872](https://www.ncbi.nlm.nih.gov/gene/79872):

> This gene encodes an E3 ubiquitin-ligase for the E-cadherin complex and mediates its ubiquitination, endocytosis, and degradation in the lysosomes. The encoded protein contains a RING-finger domain and is also thought to have a role in control of cell proliferation. A related pseudogene has been identified on chromosome X. Alternative splicing results in a non-coding transcript variant. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:21225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21225) · Entrez [79872](https://www.ncbi.nlm.nih.gov/gene/79872) · UniProt [Q75N03](https://www.uniprot.org/uniprotkb/Q75N03) · Ensembl [ENSG00000105879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105879)

## Data

Gene col 2683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2683); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2683]; `tensor/DDL_lfc|DDL_z.npy` [2683]; `embed/gene_vectors.npy` [2683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2683 or target_col == 2683). Every well: [[CBLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
